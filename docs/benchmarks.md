# シンプルベンチマークフレームワーク

Project Euler First 100プロジェクトの学習重視・理解促進を目的としたシンプルなベンチマークシステムです。

## 概要

このシンプルベンチマークフレームワークは、Project Eulerの学習目標に合わせて設計されており、以下の特徴があります：

- **学習重視**: アルゴリズムの理解と比較を重視
- **One-minute Rule**: Project Eulerの1分ルール準拠チェック
- **シンプル設計**: 複雑な統計分析を排除し、直感的で理解しやすい結果
- **自動問題検出**: 実装済み問題の自動発見と実行
- **高速実行**: 単発測定による迅速なフィードバック

## クイックスタート

### 基本的な使用方法

```bash
# 全問題のシンプルベンチマーク実行
make benchmark-simple

# 特定問題のベンチマーク
make benchmark-simple-problem PROBLEM=001

# 従来の複雑なベンチマーク（互換性のため残存）
make benchmark
make benchmark-problem PROBLEM=001
```

## シンプルベンチマーク結果

### ディレクトリ構成

```
benchmarks/
└── results/                    # シンプルベンチマーク結果
    ├── simple_benchmark_2025-06-29T14-30-00.json
    └── ...
```

### 結果の例

実行時の表示形式：

```
Benchmarking Problem 001: Multiples of 3 and 5
Found 2 solution(s)

素直な解法 (Naive): 0.000123s
最適化解法 (Optimized): 0.000012s ⭐ (fastest)

Algorithm Comparison: 最適化解法 is 10.3x faster than 素直な解法
One-minute Rule: ✅ All solutions pass (< 60.0s)

Result: [隠匿]
```

### データ形式

#### 結果ファイル (`simple_benchmark_*.json`)

```json
{
  "001": {
    "problem_title": "Multiples of 3 and 5",
    "timestamp": "2025-06-29T14:30:00.123456",
    "solutions": [
      {
        "name": "素直な解法 (Naive)",
        "time": 0.000123,
        "result": "[隠匿]",
        "complexity": "O(n)"
      },
      {
        "name": "最適化解法 (Optimized)",
        "time": 0.000012,
        "result": "[隠匿]",
        "complexity": "O(1)"
      }
    ],
    "fastest_solution": "最適化解法 (Optimized)",
    "speed_ratio": 10.3,
    "one_minute_rule": true
  }
}
```

## アーキテクチャ

### コンポーネント構成

```
problems/utils/
├── simple_benchmark.py  # シンプルベンチマーククラス
└── simple_runner.py     # 自動問題検出・実行システム
```

### シンプルベンチマーク実行フロー

1. **問題検出**: `problems/problem_*.py`ファイルを自動検出
2. **解法抽出**: 各問題から解法関数を抽出（`solve_*`, `solve`パターン）
3. **引数設定**: 問題に応じた適切な引数を自動設定
4. **単発測定**: 単回実行による迅速な性能測定
5. **結果表示**: 即座の結果表示とアルゴリズム比較
6. **One-minute Rule検証**: Project Eulerの1分ルール準拠チェック

### 測定の特徴

- **単発測定**: 複雑な統計計算を排除し、理解しやすい結果
- **高精度タイマー**: `time.perf_counter()`による高分解能測定
- **学習重視**: アルゴリズムの性能差を直感的に理解
- **高速実行**: 即座のフィードバックによる効率的な学習

## One-minute Rule検証

### Project Eulerの1分ルール

Project Eulerは「効率的なアルゴリズムによって1分以内に解ける」ことを前提としています。シンプルベンチマークフレームワークは、この重要な制約を自動的に検証します。

### 検証プロセス

1. **実行時間測定**: 各解法の実行時間を測定
2. **閾値チェック**: 60秒を超える解法があるかチェック
3. **結果表示**:
   - ✅ 全解法が1分以内: `One-minute Rule: ✅ All solutions pass (< 60.0s)`
   - ⚠️ 一部解法が制限超過: `One-minute Rule: ⚠️ Some solutions exceed 60s`
   - ❌ 全解法が制限超過: `One-minute Rule: ❌ All solutions exceed 60s`

### アルゴリズム比較

解法間の性能差を明確に表示：

```
Algorithm Comparison: 最適化解法 is 10.3x faster than 素直な解法
```

この情報により、アルゴリズムの効率性の違いを直感的に理解できます。

## 結果の表示形式

### コンソール出力

実行時には以下の形式で結果を表示：

```
Benchmarking Problem 007: 10001st prime
Found 3 solution(s)

素直な解法 (Naive): 0.045123s
最適化解法 (Optimized): 0.002341s ⭐ (fastest)
数学的解法 (Mathematical): 0.003892s

Algorithm Comparison: 最適化解法 is 19.3x faster than 素直な解法
One-minute Rule: ✅ All solutions pass (< 60.0s)

Result: [隠匿]
```

### Project Eulerポリシー準拠

- **解答値の非表示**: 具体的な解答値は`[隠匿]`で表示
- **学習重視**: アルゴリズムの理解と性能比較に焦点
- **教育的価値**: 複数解法の比較による学習効果の最大化

## 使用例

### 個別問題の実行

```bash
# Problem 006のベンチマーク
make benchmark-simple-problem PROBLEM=006
```

実行結果：
```
Benchmarking Problem 006: Sum square difference
Found 3 solution(s)

素直な解法 (Naive): 0.000045s
最適化解法 (Optimized): 0.000002s ⭐ (fastest)
数学的解法 (Mathematical): 0.000001s ⭐ (fastest)

Algorithm Comparison: 数学的解法 is 45.0x faster than 素直な解法
One-minute Rule: ✅ All solutions pass (< 60.0s)

Result: [隠匿]
```

### 全問題の実行

```bash
# 全問題のベンチマーク
make benchmark-simple
```

実行結果：
```
Found 43 problems
Running benchmarks for all problems...
============================================================

[各問題の詳細結果...]

Completed: 43/43 problems
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
3. **引数設定**: `simple_runner.py`の`get_problem_arguments()`メソッドで引数を定義
   ```python
   problem_args: dict[str, tuple[tuple, dict]] = {
       "050": ((1000,), {}),  # 新しい問題の引数
       # ...
   }
   ```
4. **ベンチマーク実行**: `make benchmark-simple-problem PROBLEM=050`

### 特殊なデータ要件

データファイルが必要な問題の場合：

```python
# simple_runner.py内で特殊ケースを処理
if problem_number == "NEW_PROBLEM":
    try:
        problem_module = importlib.import_module(
            f"problems.problem_{problem_number.zfill(3)}"
        )
        data = problem_module.get_data_function()
        return ((data,), {})
    except (ImportError, AttributeError):
        return ((), {})
```

### 関数発見の拡張

異なる命名パターンを使用する場合は、`discover_solutions()`メソッドを拡張：

```python
# 新しいパターンを追加
if (
    (name.startswith("solve_") or name == "solve" or name.startswith("custom_"))
    and inspect.isfunction(obj)
    and not name.endswith("_test")
):
    # 処理を追加
```

## トラブルシューティング

### よくある問題

**Q: ベンチマークが実行されない**
```bash
# 問題モジュールが正しく実装されているか確認
python -m problems.problem_001

# 依存関係を確認
uv sync --extra dev

# シンプルベンチマークを直接実行
python -m problems.utils.simple_runner 001
```

**Q: 引数エラーが発生する**
```bash
# Error running benchmark for problem XXX: solve_function() takes X arguments but Y were given

# simple_runner.pyの引数設定を確認
# get_problem_arguments()メソッドで正しい引数を設定
```

**Q: 解法関数が見つからない**
```bash
# No solution functions found in problems.problem_XXX

# 関数名がsolve_*またはsolveパターンに従っているか確認
# 関数がtest関数でないことを確認（_testで終わらない）
```

**Q: データインポートエラー**
```bash
# 特殊なデータが必要な問題（011, 018, 022など）
# simple_runner.pyでデータインポート処理が正しく設定されているか確認
```

### 結果ファイルの確認

```bash
# 結果ファイルが保存されているか確認
ls benchmarks/results/

# 最新の結果を確認
cat benchmarks/results/simple_benchmark_*.json | jq .
```

## API リファレンス

### SimpleBenchmark クラス

```python
class SimpleBenchmark:
    def __init__(self) -> None
    def benchmark_solution(self, name: str, func: Callable, *args, **kwargs) -> float
    def benchmark_problem(self, problem_number: str, problem_title: str,
                         solutions: list[tuple[str, Callable]], *args, **kwargs) -> None
    def display_results(self, problem_number: str) -> None
    def check_one_minute_rule(self, times: list[float]) -> bool
    def save_results(self, filepath: str) -> None
```

### SimpleBenchmarkRunner クラス

```python
class SimpleBenchmarkRunner:
    def __init__(self) -> None
    def extract_problem_number(self, module_name: str) -> str | None
    def get_problem_title(self, problem_module: Any) -> str
    def discover_solutions(self, problem_module: Any) -> list[tuple[str, Callable]]
    def get_problem_arguments(self, problem_number: str) -> tuple[tuple, dict]
    def run_problem(self, problem_number: str) -> bool
    def run_all_problems(self) -> None
    def save_all_results(self) -> None
```

## 設計理念と改善履歴

### シンプルベンチマーク v1.0 (2025-06)

**設計理念**:
- **学習重視**: Project Eulerの教育目標に焦点
- **理解促進**: 複雑な統計を排除し、アルゴリズムの本質的な違いを強調
- **即座のフィードバック**: 単発測定による迅速な結果提供
- **One-minute Rule**: Project Eulerの基本原則の自動検証

**実装されている機能**:
- ✅ シンプルな単発測定
- ✅ 自動問題検出・実行
- ✅ One-minute Rule検証
- ✅ アルゴリズム性能比較
- ✅ Project Eulerポリシー準拠（解答値非表示）
- ✅ 全43問題対応（引数自動設定）

**従来の複雑ベンチマークからの改善点**:
- 統計的複雑性を排除（1,450行 → 516行、約65%削減）
- 学習価値の最大化
- 実行時間の大幅短縮
- 理解しやすい結果表示

### 将来の拡張可能性

- **メモリ使用量測定**: 実行時間に加えてメモリプロファイリング
- **複雑度検証**: docstringの計算量表記と実測値の比較
- **学習進捗追跡**: 解法理解度の可視化
- **カスタム問題対応**: ユーザー定義問題のベンチマーク

## 参考文献・リンク

- [Project Euler公式サイト](https://projecteuler.net/)
- [Project Euler One-minute Rule](https://projecteuler.net/about)
- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [時間計算量解析](https://en.wikipedia.org/wiki/Time_complexity)
