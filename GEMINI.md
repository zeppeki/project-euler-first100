# GEMINI.md: Geminiのためのプロジェクト概要

## 1. プロジェクトの目的

このリポジトリは、[Project Euler](https://projecteuler.net/)の最初の100問を体系的に解き、アルゴリズム設計、コード品質、数学的思考の向上を目的とした学習プロジェクトです。

- **体系的学習:** 複数解法（素直な解法、最適化解法など）を実装し、計算量やパフォーマンスを比較・分析します。
- **高品質なコード:** `ruff`, `mypy`による静的解析と`pytest`によるテストを徹底し、品質を維持します。
- **ドキュメント化:** 各問題の解法、数学的背景、学習ポイントを`solutions`ディレクトリにMarkdownでまとめます。

## 2. 技術スタック

- **言語:** Python 3.11+
- **パッケージ管理:** `uv`
- **フォーマッタ/リンター:** `ruff`
- **型チェック:** `mypy`
- **テスト:** `pytest`
- **CI/CD:** GitHub Actions
- **ドキュメント:** MkDocs (Material for MkDocs)

## 3. ディレクトリ構造

- `problems/`: 各問題の解答Pythonスクリプト (`problem_XXX.py`)
- `solutions/`: 各問題の詳細な解説Markdown (`solution_XXX.md`)
- `tests/`: `pytest`用のテストコード
- `docs/`: プロジェクトの規約やワークフローに関するドキュメント
- `pyproject.toml`: プロジェクト設定と依存関係
- `Makefile`: 開発用の便利なコマンド集

## 4. 開発ワークフロー

新しい問題に取り組む際の基本的な流れは以下の通りです。

1.  **Issue作成:** `gh issue create`で新しい問題のIssueを作成します。
2.  **ブランチ作成:** `git checkout -b problem-XXX` のように、問題番号を含むブランチを作成します。
3.  **実装:**
    - `problems/problem_XXX.py` に複数の解法（例: `solve_naive`, `solve_optimized`）を実装します。
    - `tests/problems/test_problem_XXX.py` にテストコードを記述します。
4.  **品質チェック:**
    - `make quality` または `uv run ruff check .`, `uv run mypy .` を実行します。
    - `make test` または `uv run pytest` を実行します。
5.  **ドキュメント作成:** `solutions/solution_XXX.md` に解法の詳細な説明を記述します。
6.  **コミット & PR:** 変更をコミットし、GitHub上でプルリクエストを作成します。コミットメッセージはConventional Commitsに準拠することが推奨されます。

## 5. コーディング規約

- **スタイル:** `ruff`による自動フォーマット（Black準拠、88文字）。
- **命名規則:**
    - 関数/変数: `snake_case`
    - クラス: `PascalCase`
    - 定数: `UPPER_CASE`
- **型ヒント:** Python 3.11+の記法 (`list[int]`, `dict[str, int]`) を使用します。
- **Docstring:** 各モジュール、クラス、関数には、処理内容、引数、返り値などを明確に記述したDocstringが必須です。

## 6. 主要なコマンド

`Makefile`に定義されたコマンドの使用を推奨します。

- **セットアップ:** `make setup`
- **テスト実行:**
    - `make test`: 全てのテストを実行
    - `make test-fast`: 高速なテストのみ実行
    - `make test-problem PROBLEM=001`: 特定の問題のテストを実行
- **問題の実行:** `make run-problem PROBLEM=001`
- **品質チェック:** `make quality`
- **ドキュメントサーバー:** `make docs-serve`

個別のツールを直接実行することも可能です。

- `uv run pytest`
- `uv run ruff check .`
- `uv run mypy .`
