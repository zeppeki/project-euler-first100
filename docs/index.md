# Project Euler First 100

Project Eulerの最初の100問を体系的に解決し、学習効果を最大化するためのプロジェクトです。

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

## 📊 現在の進捗

- **完了問題**: 6/100
- **最新完了**: Problem 006: Sum square difference
- **実装済み解法**: 各問題3つの異なるアプローチ
- **テストカバレッジ**: 95%以上

### 完了した問題

| 問題 | タイトル | 解答 | 学習ポイント |
|------|----------|------|--------------|
| 001 | Multiples of 3 and 5 | 233,168 | 数学的公式の活用 |
| 002 | Even Fibonacci numbers | 4,613,732 | 数列の性質の観察 |
| 003 | Largest prime factor | 6,857 | 素因数分解の効率化 |
| 004 | Largest palindrome product | 906,609 | 回文の性質と効率的な探索 |
| 005 | Smallest multiple | 232,792,560 | 最小公倍数の計算 |
| 006 | Sum square difference | 25,164,150 | 数学的公式による最適化 |

## 🚀 特徴

### 複数解法の実装
各問題に対して以下の3つのアプローチを実装：

=== "素直な解法"
    理解しやすい基本的な実装

    ```python
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
    ```

=== "最適化解法"
    効率的なアルゴリズムによる実装

    ```python
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
    ```

=== "数学的解法"
    数学的洞察を活用したエレガントな実装

    ```python
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

### 詳細な分析
- 時間計算量・空間計算量の分析
- パフォーマンス比較
- 数学的背景の説明
- 学習ポイントの整理

### 包括的なテスト
- 基本ケースとエッジケースのテスト
- パフォーマンステスト
- 複数解法の結果一致検証

## 🛠️ 技術スタック

### 開発環境
- **Python 3.11+**: 新しい形式の型ヒント対応
- **uv**: 高速なPythonパッケージマネージャー
- **ruff**: 高速なPythonフォーマッターとリンター
- **mypy**: 型チェッカー
- **pytest**: テストフレームワーク
- **pre-commit**: Gitフックによる自動チェック

### ドキュメント
- **MkDocs Material**: このドキュメントサイト
- **GitHub Pages**: ホスティング
- **GitHub Actions**: 自動デプロイ

## 🚀 クイックスタート

### 前提条件
- **Python 3.11以上**が必要です
- 新しい形式の型ヒント（`list[int]`、`dict[str, int]`など）を使用

### セットアップ

```bash
# リポジトリをクローン
git clone https://github.com/zeppeki/project-euler-first100.git
cd project-euler-first100

# uvのインストール（まだインストールしていない場合）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 仮想環境を作成し、依存関係をインストール
uv sync

# pre-commitフックをインストール
uv run pre-commit install

# 動作確認
uv run pytest

# コード品質チェック
uv run ruff check problems/ solutions/ tests/
```

詳細なセットアップ手順は [セットアップガイド](setup.md) を参照してください。

## 📚 ナビゲーション

### 開発者向け
- [セットアップ](setup.md) - 開発環境の構築
- [貢献ガイド](contributing.md) - プロジェクトへの貢献方法
- [ワークフロー](workflow.md) - 開発プロセス
- [テストガイド](testing.md) - テスト戦略

### 学習者向け
- [進捗状況](progress.md) - 全体の進捗管理
- [問題一覧](problems/index.md) - 実装済み問題の概要
- 解答詳細 - 各問題の詳細な解説

## 🤝 コミュニティ

このプロジェクトは学習を目的としており、コミュニティからの貢献を歓迎しています。

### 貢献の種類
1. **新しい問題の解決**
2. **既存解答の改善**
3. **ドキュメントの追加・改善**
4. **テストケースの追加**
5. **バグ修正**

### 参加方法
- [GitHub Issues](https://github.com/zeppeki/project-euler-first100/issues) - 質問や提案
- [Pull Requests](https://github.com/zeppeki/project-euler-first100/pulls) - コード貢献
- [Discussions](https://github.com/zeppeki/project-euler-first100/discussions) - ディスカッション

## 🔗 参考資料

### Project Euler
- [Project Euler公式サイト](https://projecteuler.net/)
- [Project Euler日本語Wiki](https://projecteuler.net/wiki/)

### 技術資料
- [Python公式ドキュメント](https://docs.python.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)

### 数学資料
- [Wolfram MathWorld](http://mathworld.wolfram.com/)
- [OEIS - Online Encyclopedia of Integer Sequences](https://oeis.org/)

---

**Happy Problem Solving! 🧮**

このプロジェクトが、数学とプログラミングの学習に役立つことを願っています。
