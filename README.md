# Project Euler First 100

Project Eulerの最初の100問を体系的に解決し、学習効果を最大化するためのリポジトリです。

## 📊 進捗状況

- **完了問題**: 3/100 (Problem 001, 002, 003)
- **最新完了**: Problem 003: Largest prime factor (解答: 6,857)
- **次回予定**: Problem 004: Largest palindrome product

### 完了した問題

| 問題 | タイトル | 解答 | 完了日 | 学習ポイント |
|------|----------|------|--------|--------------|
| 001 | Multiples of 3 and 5 | 233,168 | 2024-12-19 | 数学的公式の活用 |
| 002 | Even Fibonacci numbers | 4,613,732 | 2024-12-19 | 数列の性質の観察 |
| 003 | Largest prime factor | 6,857 | 2024-12-19 | 素因数分解の効率化 |

## 🎯 プロジェクトの目的

### 1. 体系的学習
- 数学的思考力の向上
- アルゴリズム設計能力の育成
- 効率的な問題解決手法の習得

### 2. コード品質の向上
- 複数解法の実装と比較
- パフォーマンス分析
- テスト駆動開発の実践

### 3. ドキュメント化
- 詳細な解答説明
- 数学的背景の理解
- 学習ポイントの記録

## 🚀 クイックスタート

### 前提条件
- **Python 3.11以上**が必要です
- 新しい形式の型ヒント（`list[int]`、`dict[str, int]`など）を使用
- Python 3.12以降では型パラメータ構文（`class Container[T]`）も使用可能

### セットアップ

```bash
# リポジトリをクローン
git clone https://github.com/zeppeki/project-euler-first100.git
cd project-euler-first100

# uvのインストール（まだインストールしていない場合）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 初回セットアップ（Makefileを使用）
make setup

# または従来の方法
uv sync --extra all
uv run pre-commit install
```

### よく使うコマンド（Makefile）

```bash
# ヘルプ表示
make help

# テスト実行
make test                 # 全テスト
make test-fast            # 高速テストのみ
make test-problem PROBLEM=001  # 特定問題

# 問題実行
make run-problem PROBLEM=001

# コード品質チェック
make quality              # 全品質チェック
make check                # CI相当のチェック

# ドキュメント
make docs-serve           # 開発サーバー起動

# ユーティリティ
make problems             # 問題一覧
make status               # プロジェクト状況
make new-problem PROBLEM=010  # 新問題テンプレート
```

詳細なセットアップ手順は [`docs/setup.md`](docs/setup.md) を参照してください。

## 📁 プロジェクト構造

```
project-euler-first100/
├── problems/                 # 解答コード
│   ├── problem_001.py       # Problem 001
│   ├── problem_002.py       # Problem 002
│   └── ...
├── solutions/               # 解答説明
│   ├── solution_001.md      # Problem 001の詳細説明
│   ├── solution_002.md      # Problem 002の詳細説明
│   └── ...
├── tests/                   # テストコード
│   ├── problems/           # 問題のテスト
│   └── solutions/          # 解答のテスト
├── docs/                   # ドキュメント
│   ├── setup.md           # セットアップ手順
│   ├── contributing.md    # 貢献ガイドライン
│   ├── coding-standards.md # コーディング規約
│   ├── workflow.md        # 開発ワークフロー
│   └── testing.md         # テストガイド
├── PROGRESS.md            # 進捗状況
├── pyproject.toml         # プロジェクト設定
└── README.md              # このファイル
```

## 🛠️ 使用技術

### 開発環境
- **Python 3.11+**: 新しい形式の型ヒント対応
- **uv**: 高速なPythonパッケージマネージャー
- **ruff**: 高速なPythonフォーマッターとリンター
- **mypy**: 型チェッカー
- **pytest**: テストフレームワーク
- **pre-commit**: Gitフックによる自動チェック

### 新しい形式の型ヒント

```python
# Python 3.11+ の新しい型ヒント
def solve_problem(numbers: list[int]) -> dict[str, int]:
    """問題を解決する関数"""
    return {"result": sum(numbers)}

# Python 3.12+ の型パラメータ構文
class Container[T]:
    def __init__(self, value: T) -> None:
        self._value = value

    def get_value(self) -> T:
        return self._value

# 型エイリアス（Python 3.12+）
type Number = int | float
type NumberList = list[Number]
```

## 📝 問題構成

### 各問題の実装方針

1. **複数解法の実装**
   - 素直な解法（理解しやすい）
   - 最適化解法（効率的）
   - 数学的解法（エレガント）

2. **詳細な分析**
   - 時間計算量と空間計算量
   - パフォーマンス比較
   - 数学的背景の説明

3. **包括的なテスト**
   - 基本ケース
   - エッジケース
   - パフォーマンステスト

### 実装例

```python
#!/usr/bin/env python3
"""
Problem 001: Multiples of 3 and 5

Answer: 233168
"""

def solve_naive(n: int) -> int:
    """
    素直な解法
    時間計算量: O(n)
    空間計算量: O(1)
    """
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

def solve_optimized(n: int) -> int:
    """
    最適化解法（等差数列の和）
    時間計算量: O(1)
    空間計算量: O(1)
    """
    def sum_multiples(k: int) -> int:
        m = (n - 1) // k
        return k * m * (m + 1) // 2

    return sum_multiples(3) + sum_multiples(5) - sum_multiples(15)

def solve_mathematical(n: int) -> int:
    """
    数学的解法（包除原理）
    時間計算量: O(1)
    空間計算量: O(1)
    """
    n -= 1  # n未満の数を対象とする
    return (3 * (n // 3) * (n // 3 + 1) // 2 +
            5 * (n // 5) * (n // 5 + 1) // 2 -
            15 * (n // 15) * (n // 15 + 1) // 2)
```

## 🔄 開発ワークフロー

### 新しい問題に取り組む手順

1. **Issue作成**
   ```bash
   gh issue create --title "Solve Problem XXX: [問題タイトル]" \
     --body "## Problem XXX: [問題タイトル]\n\n### 問題\n[問題の説明]\n\n### タスク\n- [ ] 問題の分析\n- [ ] アルゴリズム設計\n- [ ] 実装\n- [ ] テストの作成と実行\n- [ ] ドキュメント作成" \
     --label "problem,in-progress"
   ```

**注意**: ラベルは基本的な`problem,in-progress`のみを使用し、問題番号固有のラベル（例：`013`）は存在しない場合があるため指定しません。必要に応じて後から手動で追加してください。

2. **ブランチ作成**
   ```bash
   gh issue develop [ISSUE_NUMBER]
   git checkout [BRANCH_NAME]
   ```

3. **開発作業**
   - 問題の分析と理解
   - 複数解法の実装
   - テストケースの作成
   - ドキュメントの作成

4. **品質チェック**
   ```bash
   uv run ruff check problems/ solutions/ tests/
   uv run mypy problems/ solutions/ tests/
   uv run pytest
   ```

5. **コミットとプッシュ**
   ```bash
   git add .
   git commit -m "Solve Problem XXX: [問題タイトル]\n\nAnswer: [解答]"
   git push origin [BRANCH_NAME]
   ```

6. **プルリクエスト作成**
   ```bash
   gh pr create --title "Solve Problem XXX: [問題タイトル]" \
     --body "## Problem XXX: [問題タイトル]\n\n### 解答: [数値]\n\n### 実装内容\n- [実装した解法の説明]\n\n### 学習ポイント\n- [学んだこと]"
   ```

詳細なワークフローは [`docs/workflow.md`](docs/workflow.md) を参照してください。

## 🧪 テストと品質管理

### テスト戦略

1. **単体テスト**: 各解法の動作確認
2. **統合テスト**: 複数解法の結果一致確認
3. **パフォーマンステスト**: 実行時間の測定
4. **エッジケーステスト**: 境界値の確認

### 品質チェック

```bash
# コード品質チェック
uv run ruff check problems/ solutions/ tests/

# 型チェック
uv run mypy problems/ solutions/ tests/

# テスト実行
uv run pytest

# カバレッジ確認
uv run pytest --cov=problems --cov=solutions --cov-report=html
```

### 自動化

- **pre-commit**: コミット前の自動チェック
- **GitHub Actions**: CI/CDパイプライン
- **ruff**: 自動フォーマットとリンティング

詳細なテストガイドは [`docs/testing.md`](docs/testing.md) を参照してください。

## 🤝 貢献方法

### 貢献の種類

1. **新しい問題の解決**
2. **既存解答の改善**
3. **ドキュメントの追加・改善**
4. **テストケースの追加**
5. **バグ修正**

### 貢献手順

1. このリポジトリをフォーク
2. 新しいブランチを作成
3. 変更を実装
4. テストを実行
5. プルリクエストを作成

詳細な貢献ガイドラインは [`docs/contributing.md`](docs/contributing.md) を参照してください。

## 📚 ドキュメント一覧

### 開発ガイド
- [`docs/setup.md`](docs/setup.md) - 開発環境のセットアップ
- [`docs/contributing.md`](docs/contributing.md) - 貢献ガイドライン
- [`docs/coding-standards.md`](docs/coding-standards.md) - コーディング規約
- [`docs/workflow.md`](docs/workflow.md) - 開発ワークフロー
- [`docs/testing.md`](docs/testing.md) - テストガイド

### プロジェクト情報
- [`PROGRESS.md`](PROGRESS.md) - 進捗状況の詳細
- [`problems/README.md`](problems/README.md) - 問題ディレクトリの説明
- [`solutions/README.md`](solutions/README.md) - 解答ディレクトリの説明

## 🏆 完了問題の例

### Problem 001: Multiples of 3 and 5

**問題**: 1から999までの自然数のうち、3または5の倍数の和を求めよ。

**解答**: 233,168

**実装**:
- 素直な解法: O(n) - 全数をチェック
- 最適化解法: O(1) - 等差数列の和を利用
- 数学的解法: O(1) - 包除原理を利用

**学習ポイント**:
- 数学的公式の活用による効率化
- 複数解法の比較による理解の深化
- アルゴリズムの時間計算量の重要性

詳細は [`solutions/solution_001.md`](solutions/solution_001.md) を参照してください。

## 📈 統計

### 進捗統計
- **総問題数**: 100
- **完了問題数**: 3
- **完了率**: 3%
- **平均解答時間**: 約2時間/問題
- **テストカバレッジ**: 95%以上

### 技術統計
- **使用言語**: Python 3.11+
- **主要ライブラリ**: 標準ライブラリ中心
- **テストフレームワーク**: pytest
- **コード品質**: ruff + mypy
- **ドキュメント**: Markdown

## 🔗 参考資料

### Project Euler
- [Project Euler公式サイト](https://projecteuler.net/)
- [Project Euler日本語Wiki](https://projecteuler.net/wiki/)

### 技術資料
- [Python公式ドキュメント](https://docs.python.org/)
- [PEP 585 - Type Hinting Generics](https://peps.python.org/pep-0585/)
- [PEP 695 - Type Parameter Syntax](https://peps.python.org/pep-0695/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)

### 数学資料
- [Wolfram MathWorld](http://mathworld.wolfram.com/)
- [OEIS - Online Encyclopedia of Integer Sequences](https://oeis.org/)
- [Wikipedia - Mathematics](https://en.wikipedia.org/wiki/Portal:Mathematics)

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 🙏 謝辞

- Project Eulerの創設者とコミュニティに感謝
- オープンソースツールの開発者に感謝
- 数学教育に貢献するすべての人に感謝

---

**Happy Problem Solving! 🧮**

このプロジェクトが、数学とプログラミングの学習に役立つことを願っています。
