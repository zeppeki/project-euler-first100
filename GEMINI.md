# GEMINI.md: Geminiのためのプロジェクト概要

## 1. プロジェクトの目的

このリポジトリは、[Project Euler](https://projecteuler.net/)の最初の100問を体系的に解き、アルゴリズム設計、コード品質、数学的思考の向上を目的とした学習プロジェクトです。

- **体系的学習:** 複数解法（素直な解法、最適化解法など）を実装し、計算量やパフォーマンスを比較・分析します。
- **高品質なコード:** `ruff`, `mypy`による静的解析と`pytest`によるテストを徹底し、品質を維持します。
- **ドキュメント化:** 各問題の解法、数学的背景、学習ポイントを`docs/solutions`ディレクトリにMarkdownでまとめます。

## 2. 技術スタック

- **言語:** Python 3.11+
- **パッケージ管理/タスクランナー:** `uv`
- **自動化/ワークフロー:** `make`, GitHub CLI (`gh`)
- **フォーマッタ/リンター:** `ruff`
- **型チェック:** `mypy`
- **テスト:** `pytest`
- **CI/CD:** GitHub Actions
- **ドキュメント:** MkDocs (Material for MkDocs)

## 3. ディレクトリ構造

- `problems/`: 各問題の解答Pythonスクリプト (`problem_XXX.py`)
- `docs/solutions/`: 各問題の詳細な解説Markdown (`solution_XXX.md`)
- `tests/`: `pytest`用のテストコード
- `docs/`: プロジェクトの規約やワークフローに関するドキュメント
- `pyproject.toml`: プロジェクト設定と依存関係
- `Makefile`: **開発の中心となるコマンド集。`make help`で全コマンドを確認できます。**

## 4. 開発ワークフロー (Makefile中心)

**重要:** このプロジェクトでは、開発の全工程を`Makefile`のコマンドで実行することが強く推奨されています。

1.  **Issue作成:** `make issue-create PROBLEM=030 TITLE="Problem Title"`
2.  **ブランチ作成:** `make issue-develop ISSUE=123` (Issue番号を指定)
3.  **実装:**
    - `make new-problem PROBLEM=030` でテンプレートを生成。
    - `problems/problem_XXX.py` に解法を実装。
    - `tests/problems/test_problem_XXX.py` にテストを記述。
    - `docs/solutions/solution_XXX.md` に解説を記述。
4.  **ローカルでの検証:**
    - `make test-problem PROBLEM=030`: 特定問題のテストを実行。
    - `make check`: CIで行われるチェック（テスト、品質、ドキュメント）をまとめて実行。
    - `make quality`: 全ての品質チェックを実行。
5.  **PR作成:** `make pr-create ISSUE=123 TITLE="Solve Problem 030"`
6.  **マージ:**
    - `make pr-status PR=124`: CIのステータスを確認。
    - `make pr-merge PR=124`: CIが成功していればマージ。

## 5. コーディング・ドキュメント規約

- **スタイル:** `ruff`による自動フォーマット（Black準拠、88文字）。`make format`で実行。
- **命名規則:**
    - 関数/変数: `snake_case`
    - クラス: `PascalCase`
    - 定数: `UPPER_CASE`
- **型ヒント:** Python 3.11+の記法 (`list[int]`, `dict[str, int]`) を使用。
- **Docstring:** 各モジュール、クラス、関数には、処理内容、計算量などを記述。
- **ドキュメントポリシー:** **GitHub Pagesで公開されるドキュメント (`docs/`) には、Project Eulerの解答を直接記載しないこと。** 解答のセクションは「Project Euler公式サイトで確認してください。」と記述する。

## 6. 主要なコマンド (`make`)

`make help` で全てのコマンドが確認できます。以下は特に重要なコマンドです。

- **セットアップ:** `make setup`
- **テスト:**
    - `make test`: 全てのテストを実行
    - `make test-fast`: 高速なテストのみ実行
    - `make test-problem PROBLEM=001`: 特定問題のテスト
- **品質チェック:**
    - `make quality`: `ruff`, `mypy`, `bandit` をすべて実行
    - `make lint-fix`: `ruff` で自動修正
    - `make typecheck`: `mypy` で型チェック
- **CI/CD関連:**
    - `make check`: CIの主要なチェックをローカルで実行
    - `make ci-full`: 完全なCIパイプラインをローカルで実行
- **問題の実行:** `make run-problem PROBLEM=001`
- **ドキュメント:** `make docs-serve` (開発サーバー起動), `make docs-build` (ビルド)
