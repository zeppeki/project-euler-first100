# ベンチマーク & パフォーマンス分析フレームワーク

Project Euler First 100プロジェクトの包括的なパフォーマンス分析システムです。

## 概要

このベンチマークフレームワークは、Project Eulerの全問題・全解法について体系的なパフォーマンス測定を行い、以下の機能を提供します：

- **多解法分析**: 素直な解法、最適化解法、数学的解法の性能比較
- **統計的測定**: 複数回実行による統計的に信頼性の高い測定
- **自動化**: CI/CD統合による継続的パフォーマンス監視
- **可視化**: グラフと表による分析結果の可視化
- **回帰検出**: 性能劣化の自動検出とアラート
- **ドキュメント統合**: 解法ドキュメントへの自動反映

## クイックスタート

### 基本的な使用方法

```bash
# 全問題の包括的ベンチマーク実行
make benchmark

# 特定問題のベンチマーク
make benchmark-problem PROBLEM=001

# 結果の可視化
make benchmark-visualize

# ドキュメント更新
make benchmark-docs
```

### 高度な機能

```bash
# 性能劣化検出
make benchmark-regression

# 結果のアーカイブ（ベースライン作成）
make benchmark-archive

# 詳細分析レポート生成
make benchmark-report

# レガシー形式でのベンチマーク（互換性）
make benchmark-legacy
```

## ベンチマーク結果の構造

### ディレクトリ構成

```
benchmarks/
├── individual/          # 問題別詳細結果
│   ├── problem_001.json
│   ├── problem_002.json
│   └── ...
├── aggregated/          # 統合結果
│   ├── latest.json      # 最新の完全ベンチマーク結果
│   └── historical/      # 過去のベースライン結果
│       ├── 2025-06-29_14-30-00.json
│       └── ...
└── reports/             # 生成されたレポート
    ├── performance_summary.txt
    ├── detailed_analysis.txt
    ├── performance_visualization.txt
    ├── regression_analysis.json
    └── regression_report.txt
```

### データ形式

#### 個別問題結果 (`individual/problem_XXX.json`)

```json
{
  "problem_number": "001",
  "problem_title": "Multiples of 3 and 5",
  "timestamp": "2025-06-29T14:30:00.123456",
  "config": {
    "runs": 5,
    "warmup_runs": 2,
    "min_time": 0.001,
    "max_time": 10.0
  },
  "input_parameters": {
    "limit": 1000
  },
  "solutions": [
    {
      "name": "素直な解法",
      "function_name": "solve_naive",
      "algorithm_type": "naive",
      "result": 233168,
      "execution_times": [0.0001, 0.0001, 0.0001, 0.0001, 0.0001],
      "mean_time": 0.0001,
      "median_time": 0.0001,
      "std_deviation": 0.00001,
      "min_time": 0.00009,
      "max_time": 0.00011,
      "relative_speed": 10.5,
      "complexity_class": "O(n)"
    },
    {
      "name": "最適化解法",
      "function_name": "solve_optimized",
      "algorithm_type": "optimized",
      "result": 233168,
      "execution_times": [0.00001, 0.00001, 0.00001, 0.00001, 0.00001],
      "mean_time": 0.00001,
      "median_time": 0.00001,
      "std_deviation": 0.000001,
      "min_time": 0.000009,
      "max_time": 0.000011,
      "relative_speed": 1.0,
      "complexity_class": "O(1)"
    }
  ],
  "fastest_solution": "最適化解法",
  "verified": true,
  "total_benchmark_time": 0.1
}
```

## アーキテクチャ

### コンポーネント構成

```
problems/utils/
├── benchmark.py         # 核となるベンチマーククラス
├── benchmark_runner.py  # 自動実行・統合システム
├── regression_detector.py # 性能劣化検出
├── visualizer.py        # テキストベース可視化
├── doc_updater.py       # ドキュメント自動更新
└── performance.py       # レガシー互換性サポート
```

### ベンチマーク実行フロー

1. **問題検出**: `problems/problem_*.py`ファイルを自動検出
2. **解法抽出**: 各問題から解法関数を抽出（`solve_naive`, `solve_optimized`, `solve_mathematical`）
3. **複雑度解析**: 関数docstringから時間計算量を抽出
4. **統計的測定**:
   - ウォームアップ実行（2回）
   - 本測定（5回、設定可能）
   - 統計計算（平均、中央値、標準偏差、最小・最大値）
5. **結果保存**: JSON形式で個別・統合結果を保存
6. **分析・可視化**: レポート生成とドキュメント更新

### 測定精度の確保

- **ウォームアップ実行**: JITコンパイラ最適化を反映
- **複数回測定**: 統計的信頼性の確保
- **適応的実行回数**: 極めて高速な関数は追加測定
- **異常値検出**: 実行失敗やタイムアウトの適切な処理
- **高精度タイマー**: `time.perf_counter()`による高分解能測定

## 性能劣化検出

### 回帰検出アルゴリズム

1. **ベースライン選択**: 過去7日以内の最新結果をベースラインとして使用
2. **性能比較**: 現在の結果とベースラインを解法単位で比較
3. **閾値判定**:
   - **回帰**: 20%以上の性能低下
   - **改善**: 20%以上の性能向上
4. **重要度分類**:
   - **Critical**: 100%以上の性能低下
   - **Major**: 50-100%の性能低下
   - **Minor**: 20-50%の性能低下

### CI/CD統合

```bash
# .github/workflows/benchmark.yml での使用例
- name: Run Benchmarks
  run: make benchmark

- name: Check for Regressions
  run: make benchmark-regression
  # 回帰が検出された場合、適切な終了コードで失敗
```

## 可視化とレポート

### テキストベース可視化

外部依存関係を避けるため、ASCII文字による可視化を提供：

```
ALGORITHM TYPE DISTRIBUTION
========================================
naive        |██████████████████████████████| 37 ( 33.3%)
optimized    |██████████████████████████████| 37 ( 33.3%)
mathematical |██████████████████████████████| 37 ( 33.3%)

Total: 111 solutions
```

### パフォーマンス比較表

```
PERFORMANCE COMPARISON TABLE
================================================================================
 Problem Solution                   Time (μs) Relative   Complexity
--------------------------------------------------------------------------------
     001 素直な解法                      100.2      10.5x        O(n)
     001 最適化解法                        9.5       1.0x        O(1)

     002 素直な解法                      250.8       5.2x        O(n)
     002 最適化解法                       48.1       1.0x      O(log n)
```

### トップパフォーマー

```
TOP 10 FASTEST SOLUTIONS
============================================================
Rank  Problem Solution             Time   Complexity
------------------------------------------------------------
   1      005 数学的解法              0.12 μs        O(1)
   2      001 最適化解法              9.50 μs        O(1)
   3      006 数学的解法             12.30 μs        O(1)
```

## ドキュメント統合

### 自動ドキュメント更新

ベンチマーク結果は自動的に各問題の解法ドキュメントに統合されます：

```markdown
## パフォーマンス分析

### 実行時間比較

| 解法 | 実行時間 | 相対速度 | 時間計算量 |
|------|----------|----------|------------|
| 素直な解法 | 100.2μs | 10.5x | O(n) |
| 最適化解法 | 9.5μs | 1.0x | O(1) |

**検証結果**: ✅ 全解法で一致
**最速解法**: 最適化解法

*ベンチマーク実行時刻: 2025-06-29 14:30:00*
```

### GitHub Pages対応

- **解答値の非表示**: Project Eulerポリシー準拠
- **学習重視**: アルゴリズム分析と性能比較に焦点
- **自動更新**: ベンチマーク実行時に自動でドキュメント更新

## 設定とカスタマイズ

### ベンチマーク設定

```python
from problems.utils.benchmark import BenchmarkSuite, BenchmarkConfig

# カスタム設定
config = BenchmarkConfig(
    runs=10,           # 測定回数
    warmup_runs=3,     # ウォームアップ回数
    min_time=0.0001,   # 最小測定時間（秒）
    max_time=30.0      # 最大測定時間（秒）
)

suite = BenchmarkSuite(config)
```

### 回帰検出設定

```python
from problems.utils.regression_detector import PerformanceRegressionDetector

# カスタム閾値
detector = PerformanceRegressionDetector(
    regression_threshold=0.15,   # 15%で回帰とみなす
    improvement_threshold=0.25   # 25%で改善とみなす
)
```

## 開発者向けガイド

### 新しい問題の追加

1. **問題モジュール作成**: `problems/problem_XXX.py`
2. **解法関数実装**: 標準的な関数名を使用
   ```python
   def solve_naive(limit: int) -> int:
       """素直な解法: 時間計算量: O(n)"""
       pass

   def solve_optimized(limit: int) -> int:
       """最適化解法: 時間計算量: O(log n)"""
       pass
   ```
3. **ベンチマーク実行**: `make benchmark-problem PROBLEM=XXX`

### カスタム測定パラメータ

`benchmark_runner.py`の`determine_problem_input()`メソッドで新しい問題の入力パラメータを定義：

```python
default_inputs = {
    "050": {"target": 1000, "max_iterations": 10000},
    # 新しいパターンを追加
}
```

### 可視化の拡張

`visualizer.py`で新しい可視化機能を追加：

```python
def create_custom_chart(benchmark_data: dict[str, Any]) -> str:
    """カスタム可視化を作成"""
    # 実装
    pass
```

## トラブルシューティング

### よくある問題

**Q: ベンチマークが実行されない**
```bash
# 問題モジュールが正しく実装されているか確認
python -m problems.problem_001

# 依存関係を確認
uv sync --extra dev
```

**Q: 回帰検出でベースラインが見つからない**
```bash
# 手動でベースラインを作成
make benchmark-archive

# 過去の結果が存在するか確認
ls benchmarks/aggregated/historical/
```

**Q: ドキュメント更新に失敗する**
```bash
# ドキュメントファイルが存在するか確認
ls docs/solutions/solution_*.md

# 権限を確認
chmod +w docs/solutions/
```

### パフォーマンスのデバッグ

```python
# 詳細なプロファイリング
import cProfile
from problems.utils.benchmark import BenchmarkSuite

def profile_problem():
    suite = BenchmarkSuite()
    # ベンチマークコードをプロファイル

cProfile.run('profile_problem()')
```

## API リファレンス

### BenchmarkSuite クラス

```python
class BenchmarkSuite:
    def __init__(self, config: BenchmarkConfig | None = None)
    def benchmark_solution(self, name: str, func: Callable, ...) -> SolutionMetrics
    def benchmark_problem(self, problem_number: str, ...) -> ProblemBenchmark
    def save_results(self, filepath: Path) -> None
    def load_results(self, filepath: Path) -> None
```

### PerformanceRegressionDetector クラス

```python
class PerformanceRegressionDetector:
    def __init__(self, regression_threshold: float = 0.20, ...)
    def analyze_regression(self, current_file: Path | None = None, ...) -> RegressionAnalysis | None
    def save_analysis(self, analysis: RegressionAnalysis, ...) -> None
    def generate_alert_report(self, analysis: RegressionAnalysis) -> str
```

## 履歴とロードマップ

### バージョン 1.0 (現在)

- ✅ 多解法統計的ベンチマーク
- ✅ 自動結果保存・集計
- ✅ 性能劣化検出
- ✅ テキストベース可視化
- ✅ ドキュメント自動更新
- ✅ CI/CD統合

### 将来の拡張予定

- **グラフィカル可視化**: matplotlib統合（オプション）
- **Webダッシュボード**: インタラクティブな結果表示
- **メモリ使用量分析**: 実行時間に加えてメモリプロファイリング
- **並列実行**: 大規模ベンチマークの高速化
- **カスタムメトリクス**: ユーザー定義の測定指標

## 参考文献・リンク

- [Project Euler公式サイト](https://projecteuler.net/)
- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [統計的ベンチマーキング手法](https://en.wikipedia.org/wiki/Benchmark_(computing))
- [時間計算量解析](https://en.wikipedia.org/wiki/Time_complexity)
