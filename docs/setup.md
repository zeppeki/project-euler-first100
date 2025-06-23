# 開発環境のセットアップ手順

このドキュメントでは、Project Euler First 100プロジェクトの開発環境をセットアップする手順を説明します。

## 前提条件

### Python バージョン
- **Python 3.11以上**が必要です
- 新しい形式の型ヒント（`list[int]`、`dict[str, int]`など）を使用するため、Python 3.11以降を推奨します
- Python 3.12以降では、型パラメータ構文（`class Container[T]`）も使用可能です

### 必要なソフトウェア

- **uv**: 0.1.0以上（推奨: 最新版）
- **Git**: 2.30以上
- **GitHub CLI**: 2.0以上（オプション、推奨）

### オペレーティングシステム

- **Linux**: Ubuntu 20.04以上、WSL2
- **macOS**: 10.15以上
- **Windows**: Windows 10以上（WSL2推奨）

## セットアップ手順

### 1. Python のインストール

#### Linux (Ubuntu/Debian)
```bash
# システムのPythonを更新
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev

# または pyenv を使用
curl https://pyenv.run | bash
pyenv install 3.11.7
pyenv global 3.11.7
```

#### macOS
```bash
# Homebrew を使用
brew install python@3.11

# または pyenv を使用
brew install pyenv
pyenv install 3.11.7
pyenv global 3.11.7
```

#### Windows
```bash
# 公式インストーラーからダウンロード
# https://www.python.org/downloads/

# または Chocolatey を使用
choco install python311
```

### 2. uv のインストール

[uv](https://docs.astral.sh/uv/)は高速なPythonパッケージマネージャーです。

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# インストール確認
uv --version
```

### 3. リポジトリのクローン

```bash
# リポジトリをクローン
git clone https://github.com/zeppeki/project-euler-first100.git
cd project-euler-first100

# 最新の変更を取得
git pull origin main
```

### 4. 仮想環境の作成と依存関係のインストール

```bash
# 仮想環境を作成し、依存関係をインストール
uv sync

# 仮想環境をアクティベート
source .venv/bin/activate  # Linux/macOS
# または
.venv\Scripts\activate     # Windows
```

### 5. pre-commit フックのインストール

```bash
# pre-commitフックをインストール
uv run pre-commit install

# 既存のファイルに対してpre-commitを実行
uv run pre-commit run --all-files
```

### 6. 動作確認

```bash
# テストの実行
uv run pytest

# コード品質チェック
uv run ruff check problems/ solutions/ tests/

# 型チェック
uv run mypy problems/ solutions/ tests/

# コードフォーマット
uv run ruff format problems/ solutions/ tests/
```

### 7. GitHub CLIのセットアップ（オプション）

```bash
# GitHub CLIのインストール（Ubuntu/Debian）
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# GitHub CLIの認証
gh auth login

# 認証の確認
gh auth status
```

### 8. エディタの設定

#### 8.1 VS Code（推奨）

```bash
# VS Codeのインストール（Ubuntu）
sudo snap install code --classic

# または、公式サイトからダウンロード
# https://code.visualstudio.com/
```

**推奨拡張機能**:
- Python
- Pylance
- Ruff
- MyPy Type Checker
- GitLens
- GitHub Pull Requests and Issues

**VS Code設定** (`settings.json`):
```json
{
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.linting.mypyEnabled": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": "explicit"
    },
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.pytestArgs": [
        "tests"
    ],
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    },
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true,
        "**/.mypy_cache": true,
        "**/.ruff_cache": true
    }
}
```

#### 8.2 PyCharm

1. PyCharm ProfessionalまたはCommunity Editionをインストール
2. プロジェクトを開く
3. 仮想環境を設定（File → Settings → Project → Python Interpreter）
4. 推奨プラグインをインストール
5. Ruffプラグインをインストール

## 新しい形式の型ヒントについて

### Python 3.11+ の新しい型ヒント

```python
# 古い形式（Python 3.8-3.10）
from typing import List, Dict, Tuple, Optional

def old_style(numbers: List[int]) -> Dict[str, int]:
    return {"count": len(numbers)}

# 新しい形式（Python 3.11+）
def new_style(numbers: list[int]) -> dict[str, int]:
    return {"count": len(numbers)}

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

### 移行ガイド

既存のコードを新しい形式に移行する場合：

```bash
# ruff の pyupgrade を使用して自動変換
uv run ruff check --select UP --fix problems/ solutions/ tests/
```

## 動作確認

### 1. 基本的な動作確認

```bash
# 仮想環境がアクティブになっていることを確認
which python
# 出力例: /path/to/project-euler-first100/.venv/bin/python

# Pythonのバージョン確認
uv run python --version
# 出力例: Python 3.11.x

# uvの状態確認
uv status
```

### 2. テストの実行

```bash
# 全テストの実行
uv run pytest

# カバレッジ付きでテスト実行
uv run pytest --cov=problems --cov=solutions

# 特定の問題のテスト実行
uv run pytest tests/problems/test_problem_001.py
```

### 3. コード品質チェック

```bash
# コードフォーマットとリンティング
uv run ruff format problems/ solutions/ tests/
uv run ruff check problems/ solutions/ tests/

# インポートの整理
uv run ruff check --select I problems/ solutions/ tests/

# 型チェック
uv run mypy problems/ solutions/
```

### 4. 既存の問題の実行

```bash
# Problem 001の実行
uv run python problems/problem_001.py

# Problem 002の実行
uv run python problems/problem_002.py

# Problem 003の実行
uv run python problems/problem_003.py
```

### 5. ドキュメントのビルドと確認

このプロジェクトはMkDocsを使用してGitHub Pagesで公開される包括的なドキュメントを生成します。

#### 5.1 MkDocs依存関係のインストール

```bash
# MkDocsとプラグインをインストール
uv pip install mkdocs-material mkdocs-git-revision-date-localized-plugin mkdocs-minify-plugin

# インストール確認
uv run mkdocs --version
```

#### 5.2 ドキュメントのビルド

```bash
# 開発用サーバーの起動（リアルタイムプレビュー）
uv run mkdocs serve --dev-addr=127.0.0.1:8000

# ブラウザで http://127.0.0.1:8000 にアクセスして確認
```

#### 5.3 本番用ビルド

```bash
# 静的HTMLファイルの生成
uv run mkdocs build

# 厳密モードでのビルド（警告をエラーとして扱う）
uv run mkdocs build --clean --strict

# 出力先: site/ ディレクトリにHTMLファイルが生成される
```

#### 5.4 ドキュメント構造

- **docs/** - ドキュメントのソースファイル
  - **index.md** - ホームページ
  - **setup.md** - 開発環境セットアップ（このファイル）
  - **contributing.md** - 貢献ガイドライン
  - **problems/index.md** - 問題一覧と進捗状況
  - **solutions/** - 各問題の詳細解説
    - **solution_001.md** - Problem 001の解説
    - **solution_002.md** - Problem 002の解説
    - etc.

#### 5.5 ドキュメント作成時の注意点

```bash
# ドキュメント追加時は必ずビルドエラーをチェック
uv run mkdocs build --clean --strict

# リンク切れや警告がある場合、詳細なエラーメッセージが表示される
# 例: "WARNING - Doc file contains a link 'path/to/file.md', but the target is not found"
```

#### 5.6 GitHub Pagesへの自動デプロイ

- **自動デプロイ**: mainブランチへのプッシュで自動的にGitHub Pagesにデプロイ
- **手動チェック**: ローカルでビルドテストしてからプッシュすることを推奨
- **公開URL**: https://zeppeki.github.io/project-euler-first100/

#### 5.7 解答値の隠匿化ポリシー

Project Eulerの方針に従い、GitHub Pagesでは解答値を直接表示しません：

```markdown
## 解答

Project Euler公式サイトで確認してください。

## 検証
- **入力:** 1000
- **解答:** [隠匿]
- **検証:** ✓
```

## トラブルシューティング

### よくある問題と解決方法

#### 1. Python バージョンが古い
```bash
# Python バージョンを確認
python --version

# 3.11以上であることを確認
python -c "import sys; assert sys.version_info >= (3, 11), 'Python 3.11+ required'"
```

#### 2. uv が見つからない
```bash
# PATH に追加
export PATH="$HOME/.cargo/bin:$PATH"

# または再インストール
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 3. 仮想環境の作成に失敗
```bash
# 既存の仮想環境を削除
rm -rf .venv

# 再作成
uv sync
```

#### 4. 依存関係のインストールに失敗
```bash
# キャッシュをクリア
uv cache clean

# 再インストール
uv sync --reinstall
```

#### 5. pre-commit のエラー
```bash
# pre-commit を再インストール
uv run pre-commit uninstall
uv run pre-commit install

# 手動で実行
uv run pre-commit run --all-files
```

#### 6. 型チェックエラー
```bash
# mypy の設定を確認
cat pyproject.toml | grep -A 10 "\[tool.mypy\]"

# 型チェックを実行
uv run mypy problems/ solutions/ tests/
```

#### 7. MkDocsビルドエラー
```bash
# MkDocs依存関係の再インストール
uv pip install --force-reinstall mkdocs-material mkdocs-git-revision-date-localized-plugin mkdocs-minify-plugin

# 厳密モードでエラー詳細を確認
uv run mkdocs build --clean --strict --verbose

# 一般的な問題と解決策:
# - リンク切れ: 参照先ファイルの存在確認
# - 画像ファイルが見つからない: パスの確認
# - 設定エラー: mkdocs.yml の構文確認
```

#### 8. ドキュメントの表示問題
```bash
# ローカルサーバーでの確認
uv run mkdocs serve --dev-addr=127.0.0.1:8000

# キャッシュクリア
rm -rf site/
uv run mkdocs build --clean

# 特定のページのみビルド確認
uv run mkdocs build --clean --strict 2>&1 | grep "ERROR\|WARNING"
```

### パフォーマンスの問題

#### 1. 遅い依存関係インストール
```bash
# uv の並列インストールを使用
uv sync --jobs 8
```

#### 2. 遅いテスト実行
```bash
# pytest-xdist を使用して並列実行
uv run pytest -n auto

# 特定のテストのみ実行
uv run pytest tests/problems/test_problem_001.py -v
```

#### 3. 遅いコード品質チェック
```bash
# 特定のファイルのみチェック
uv run ruff check problems/problem_001.py

# キャッシュを使用
uv run ruff check --cache-dir .ruff_cache problems/
```

## 開発ワークフロー

### 1. 新しい問題に取り組む際の手順

```bash
# 1. 新しいブランチを作成
git checkout -b problem-XXX

# 2. 問題ファイルを作成
touch problems/problem_XXX.py

# 3. テストファイルを作成
touch tests/problems/test_problem_XXX.py

# 4. 解答説明ファイルを作成
touch solutions/solution_XXX.md

# 5. 開発とテスト
uv run python problems/problem_XXX.py
uv run pytest tests/problems/test_problem_XXX.py

# 6. ドキュメントの作成と確認
# 解答説明ドキュメントを作成
# solutions/solution_XXX.md を編集

# ドキュメントのビルド確認
uv run mkdocs build --clean --strict

# 7. コード品質チェック
uv run pre-commit run --all-files

# 8. コミットとプッシュ
git add .
git commit -m "Solve Problem XXX: [問題タイトル]"
git push origin problem-XXX
```

### 2. 日常的な開発手順

```bash
# 1. 最新の変更を取得
git pull origin main

# 2. 依存関係の更新確認
uv sync

# 3. 開発作業

# 4. テスト実行
uv run pytest

# 5. ドキュメントのビルド確認（ドキュメント変更時）
uv run mkdocs build --clean --strict

# 6. コード品質チェック
uv run pre-commit run --all-files

# 7. コミット
git add .
git commit -m "Update: [変更内容]"
```

### 3. 新しい依存関係の追加

```bash
# 開発用依存関係を追加
uv add --dev package-name

# 本番用依存関係を追加
uv add package-name

# 特定のバージョンを指定
uv add "package-name>=1.0.0,<2.0.0"
```

### 4. コードフォーマットとリンティング

```bash
# コードの自動修正
uv run ruff check --fix problems/ solutions/ tests/

# フォーマットの適用
uv run ruff format problems/ solutions/ tests/

# インポートの自動整理
uv run ruff check --select I --fix problems/ solutions/ tests/

# 全体的なコード品質チェック
uv run ruff check problems/ solutions/ tests/
```

## uvとRuffの利点

### 1. 高速性
- uv: 依存関係の解決とインストールが高速
- ruff: フォーマットとリンティングが高速（Rust実装）

### 2. 一貫性
- uv: ロックファイルによる再現可能なビルド
- ruff: 統一されたフォーマットとリンティングルール

### 3. 使いやすさ
- uv: シンプルなコマンドと自動的な仮想環境管理
- ruff: 複数のツール（Black、isort、flake8）を統合

### 4. 設定の簡素化
- 複数の設定ファイルが不要
- 統一された設定で一貫性を保証

## 設定ファイルの説明

### 主要な設定ファイル

- `pyproject.toml`: プロジェクトのメタデータとツール設定
- `uv.lock`: uvによる依存関係のロックファイル
- `mypy.ini`: MyPy型チェッカーの設定
- `.pre-commit-config.yaml`: Pre-commitフックの設定

### Ruff固有の設定

```toml
# pyproject.tomlでのruff設定例
[tool.ruff]
target-version = "py38"
line-length = 88
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
```

### uv固有の設定

```toml
# pyproject.tomlでのuv設定例
[project]
name = "project-euler-first100"
version = "0.1.0"
dependencies = [
    "pytest>=7.0.0",
    "ruff>=0.1.0",
]

[project.optional-dependencies]
dev = [
    "pytest-cov>=4.0.0",
    "mypy>=1.0.0",
    "pre-commit>=3.0.0",
]
```

## 参考資料

- [uv公式ドキュメント](https://docs.astral.sh/uv/)
- [Ruff公式ドキュメント](https://docs.astral.sh/ruff/)
- [Python公式ドキュメント](https://docs.python.org/)
- [Pytest公式ドキュメント](https://docs.pytest.org/)
- [MyPy公式ドキュメント](https://mypy.readthedocs.io/)
- [Pre-commit公式ドキュメント](https://pre-commit.com/)
- [GitHub CLI公式ドキュメント](https://cli.github.com/)

## サポート

セットアップで問題が発生した場合は、以下の手順でサポートを求めてください：

1. エラーメッセージを確認
2. このドキュメントのトラブルシューティングセクションを参照
3. GitHubのIssuesで問題を報告
4. 必要に応じて、環境情報を含めて詳細を記載
