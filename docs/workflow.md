# 開発ワークフロー

このドキュメントでは、Project Euler First 100プロジェクトの開発ワークフローを説明します。

## 概要

このプロジェクトでは、以下のワークフローに従って開発を行います：

1. **Issue作成** → 2. **ブランチ作成** → 3. **開発作業** → 4. **テスト実行** → 5. **コード品質チェック** → 6. **プルリクエスト作成** → 7. **レビュー** → 8. **マージ**

## 開発環境の準備

### 1. リポジトリのクローン

```bash
# リポジトリをクローン
git clone https://github.com/zeppeki/project-euler-first100.git
cd project-euler-first100

# 開発環境のセットアップ
uv sync
uv run pre-commit install
```

### 2. リモートの設定

```bash
# リモートの確認
git remote -v

# 必要に応じてリモートを追加
git remote add upstream https://github.com/zeppeki/project-euler-first100.git
```

## 新しい問題に取り組む手順

### 1. Issueの作成

新しい問題に取り組む際は、まずIssueを作成します。

```bash
# GitHub CLIを使用
gh issue create --title "Solve Problem XXX: [問題タイトル]" --body "## Problem XXX: [問題タイトル]

### 問題
[問題の日本語説明]

### 詳細
[英語での問題文]

### タスク
- [ ] 問題の分析と理解
- [ ] アルゴリズムの設計
- [ ] Pythonでの実装
- [ ] テストの作成と実行
- [ ] 解答の検証
- [ ] 解答の説明をsolutions/に追加
- [ ] 進捗表の更新

### ファイル
- `problems/problem_XXX.py` （アルゴリズム実装）
- `problems/runners/problem_XXX_runner.py` （実行・表示）
- `tests/problems/test_problem_XXX.py` （テスト）
- `solutions/solution_XXX.md` （解答説明）

### 参考
- [Project Euler Problem XXX](https://projecteuler.net/problem=XXX)" --label "problem,in-progress"
```

### 2. ブランチの作成

```bash
# 新しいブランチを作成
git checkout -b problem-XXX

# または、GitHub CLIを使用
gh issue develop [ISSUE_NUMBER]
git checkout [BRANCH_NAME]
```

### 3. 問題の分析と理解

#### 3.1 問題の読み取り
- 問題文を完全に理解する
- 入力と出力を明確にする
- 制約条件を確認する
- 例題を解いて理解を深める

#### 3.2 数学的背景の調査
- 関連する数学的概念を調べる
- 既存のアルゴリズムを調査する
- 最適化の可能性を探る

#### 3.3 アルゴリズムの設計
- 複数の解法を検討する
- 時間計算量と空間計算量を分析する
- 実装の難易度を評価する

### 4. 実装

#### 4.1 問題ファイルの作成

**アルゴリズム実装ファイル** (`problems/problem_XXX.py`):

```python
#!/usr/bin/env python3
"""
Problem XXX: [問題タイトル]

[問題の詳細説明]

Answer: [解答]
"""

import math  # 必要に応じて

def solve_naive(parameters):
    """
    素直な解法
    時間計算量: O(...)
    空間計算量: O(...)
    """
    # 実装
    pass

def solve_optimized(parameters):
    """
    最適化解法
    時間計算量: O(...)
    空間計算量: O(...)
    """
    # 実装
    pass

def solve_mathematical(parameters):
    """
    数学的解法（明確な数学的洞察がある場合のみ）
    時間計算量: O(...)
    空間計算量: O(...)
    """
    # 実装
    pass
```

**実行・表示ファイル** (`problems/runners/problem_XXX_runner.py`):

```python
#!/usr/bin/env python3
"""
Problem XXX Runner: [問題タイトル]

実行・表示・パフォーマンス測定を担当
"""

from problems.problem_XXX import solve_naive, solve_optimized, solve_mathematical
from problems.utils.display import print_final_answer, print_performance_comparison
from problems.utils.performance import compare_performance

def test_solutions():
    """テストケースで解答を検証"""
    test_cases = [
        (input1, expected1),
        (input2, expected2),
        # ...
    ]

    print("=== テストケース ===")
    for input_val, expected in test_cases:
        result_naive = solve_naive(input_val)
        result_optimized = solve_optimized(input_val)
        result_math = solve_mathematical(input_val)

        print(f"Input: {input_val}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}")
        print(f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}")
        print()

def run_problem():
    """問題の実行"""
    # テストケース
    test_solutions()

    # パフォーマンス比較と結果表示
    solutions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    results = compare_performance(solutions, parameters)
    print_performance_comparison(results)
    print_final_answer(results[0]["result"])

if __name__ == "__main__":
    run_problem()
```

#### 4.2 テストファイルの作成

```python
#!/usr/bin/env python3
"""
Test for Problem XXX: [問題タイトル]
"""

import pytest
from problems.problem_XXX import solve_naive, solve_optimized, solve_mathematical

class TestProblemXXX:
    """Problem XXXのテストクラス"""

    def test_solve_naive(self):
        """素直な解法のテスト"""
        test_cases = [
            (input1, expected1),
            (input2, expected2),
            # ...
        ]

        for input_val, expected in test_cases:
            assert solve_naive(input_val) == expected

    def test_solve_optimized(self):
        """最適化解法のテスト"""
        test_cases = [
            (input1, expected1),
            (input2, expected2),
            # ...
        ]

        for input_val, expected in test_cases:
            assert solve_optimized(input_val) == expected

    def test_solve_mathematical(self):
        """数学的解法のテスト"""
        test_cases = [
            (input1, expected1),
            (input2, expected2),
            # ...
        ]

        for input_val, expected in test_cases:
            assert solve_mathematical(input_val) == expected

    def test_all_solutions_agree(self):
        """すべての解法が同じ結果を返すことを確認"""
        test_cases = [
            input1,
            input2,
            # ...
        ]

        for input_val in test_cases:
            naive_result = solve_naive(input_val)
            optimized_result = solve_optimized(input_val)
            math_result = solve_mathematical(input_val)

            assert naive_result == optimized_result == math_result
```

#### 4.3 解答説明ファイルの作成

```markdown
# Problem XXX: [問題タイトル]

## 問題
[問題の説明]

## 解答: [数値]

## 解法
### 1. [解法名]
[コードと説明]

### 2. [解法名]
[コードと説明]

### 3. [解法名]
[コードと説明]

## 数学的背景
[関連する数学的概念]

## 検証
[テストケースと検証結果]

## パフォーマンス比較
[各解法の性能比較]

## 最適化のポイント
[最適化のポイント]

## 学習ポイント
[学んだこと]

## 参考
[参考リンク]
```

### 5. テスト・実行

```bash
# 問題の実行（推奨）
make run-problem PROBLEM=XXX

# または、直接runnerファイルを実行
uv run python problems/runners/problem_XXX_runner.py

# テストの実行
make test-problem PROBLEM=XXX

# または、直接pytestを実行
uv run pytest tests/problems/test_problem_XXX.py -v

# 全テストの実行
make test

# カバレッジ付きでテスト実行
make test-cov
```

### 6. コード品質チェック

```bash
# コードフォーマット
uv run ruff format problems/problem_XXX.py
uv run ruff format tests/problems/test_problem_XXX.py

# リンティング
uv run ruff check problems/problem_XXX.py
uv run ruff check tests/problems/test_problem_XXX.py

# 型チェック
uv run mypy problems/problem_XXX.py

# pre-commitフックの実行
uv run pre-commit run --all-files
```

### 7. コミットとプッシュ

```bash
# 変更をステージング
git add .

# コミット
git commit -m "Solve Problem XXX: [問題タイトル]

- [実装内容の要約]
- [追加したファイル]
- [重要なポイント]

Answer: [解答]"

# プッシュ
git push origin problem-XXX
```

### 8. プルリクエストの作成

```bash
# GitHub CLIを使用
gh pr create --title "Solve Problem XXX: [問題タイトル]" --body "## Problem XXX: [問題タイトル]

### 解答: [数値]

### 実装内容
- [実装した解法の説明]

### ファイル
- [作成したファイル]

### 特徴
- [実装の特徴]

### 検証
- [検証結果]

### 学習ポイント
- [学んだこと]

Closes #[ISSUE_NUMBER]" --label "problem,XXX,completed"
```

### 9. プルリクエストのマージ

```bash
# プルリクエストをマージ
gh pr merge [PR_NUMBER] --merge

# mainブランチに切り替え
git checkout main
git pull origin main
```

### 10. Issueのクローズ

```bash
# Issueをクローズ
gh issue close [ISSUE_NUMBER] --reason completed
```

### 11. 進捗表の更新

```bash
# PROGRESS.mdを更新
# 問題のステータスを「🟢 完了」に変更
# 完了日を記録
# 統計を更新
```

## ブランチ戦略

### ブランチの命名規則

- **問題解決ブランチ**: `problem-XXX`
- **機能追加ブランチ**: `feature/機能名`
- **バグ修正ブランチ**: `fix/バグ名`
- **ドキュメントブランチ**: `docs/ドキュメント名`
- **リファクタリングブランチ**: `refactor/変更内容`

### ブランチの管理

```bash
# ブランチの一覧表示
git branch -a

# ブランチの削除（マージ後）
git branch -d problem-XXX

# リモートブランチの削除
git push origin --delete problem-XXX
```

### ブランチの更新

```bash
# mainブランチの最新変更を取得
git checkout main
git pull origin main

# 作業ブランチを更新
git checkout problem-XXX
git rebase main

# または、マージを使用
git checkout problem-XXX
git merge main
```

### 並行開発 (Git Worktree)

Git Worktreeを使用することで、複数のProject Euler問題を同時に並行して開発することができます。これにより、ブランチの切り替えなしに複数の問題に取り組むことができます。

#### Git Worktreeの利点

- **並行開発**: 複数の問題を同時に開発可能
- **独立した環境**: 各ワークツリーは独自の作業ディレクトリとインデックスを持つ
- **共有リポジトリ**: すべてのワークツリーが同じGitリポジトリとリモート参照を共有
- **高速なコンテキスト切り替え**: 変更のstashやコミットが不要

#### ワークツリーのセットアップ

**新しい問題用のワークツリーを作成:**

```bash
# 問題025用のワークツリーを作成（サブディレクトリ）
git worktree add ../project-euler-problem-025 problem-025

# または、専用のworktreesディレクトリに作成
mkdir -p ../worktrees
git worktree add ../worktrees/problem-025 problem-025

# GitHub issueからブランチを作成してワークツリーを作成
make issue-develop ISSUE=123  # GitHubのissueからブランチを作成
git worktree add ../worktrees/problem-025 problem-025-branch-name
```

**既存のワークツリーを一覧表示:**

```bash
git worktree list
```

**ワークツリー間の移動:**

```bash
# 異なるワークツリーディレクトリに移動
cd ../worktrees/problem-025

# 各ワークツリーで独立してMakefileコマンドを実行可能
make test-problem PROBLEM=025
make run-problem PROBLEM=025
make ci-check
```

#### 開発ワークフローとの統合

**並行問題開発の例:**

```bash
# メインリポジトリ: 問題024に取り組み中
cd project-euler-first100
make test-problem PROBLEM=024

# ワークツリー1: 問題025に取り組み中
cd ../worktrees/problem-025
make new-problem PROBLEM=025
make test-problem PROBLEM=025

# ワークツリー2: 問題026に取り組み中
cd ../worktrees/problem-026
make new-problem PROBLEM=026
make run-problem PROBLEM=026

# 各ワークツリーは独自の仮想環境と依存関係を維持
```

**独立したCIチェック:**

```bash
# 各ワークツリーで独立してCIチェックを実行
cd ../worktrees/problem-025
make ci-check

cd ../worktrees/problem-026
make ci-check
```

#### ベストプラクティス

**ワークツリーの組織化:**

```bash
# 推奨ディレクトリ構造
project-euler-first100/          # メインリポジトリ
../worktrees/
  ├── problem-025/               # 問題別ワークツリー
  ├── problem-026/
  ├── refactor-testing/          # 機能別ワークツリー
  └── docs-update/
```

**命名規則:**
- 問題用ワークツリー: `problem-XXX` (ブランチ名と一致)
- 機能用ワークツリー: `feature-説明` または `issue-123`
- メンテナンス用ワークツリー: `refactor-コンポーネント`, `docs-update`

**依存関係の共有:**

```bash
# 各ワークツリーには独自の仮想環境が必要
cd ../worktrees/problem-025
uv sync --extra dev           # このワークツリー用の独立した.venvを作成

# または、UVキャッシュを共有して再ダウンロードを回避
export UV_CACHE_DIR="$HOME/.cache/uv"  # 共有キャッシュの場所
```

#### よく使用するコマンド

**既存ブランチからワークツリーを作成:**

```bash
git worktree add ../worktrees/existing-branch 既存ブランチ名
```

**新しいブランチでワークツリーを作成:**

```bash
git worktree add -b 新ブランチ名 ../worktrees/new-feature origin/main
```

**完了したワークツリーを削除:**

```bash
# ブランチをマージ後、ワークツリーディレクトリを削除
git worktree remove ../worktrees/problem-025

# または、自動的に削除とクリーンアップ
git worktree remove --force ../worktrees/problem-025
```

**ワークツリーの場所を移動:**

```bash
git worktree move ../worktrees/problem-025 ../new-location/problem-025
```

#### GitHubワークフローとの統合

**ワークツリーからのPR作成:**

```bash
# どのワークツリーからでも通常通りPRを作成
cd ../worktrees/problem-025
make pr-create ISSUE=123 TITLE="Problem 025を解決"

# PRの状況を監視
make pr-status PR=124

# マージとクリーンアップ
make pr-merge PR=124
git worktree remove ../worktrees/problem-025  # マージ成功後
```

**ブランチの同期:**

```bash
# すべてのワークツリーが同じリポジトリを共有
# mainブランチの変更はすべてのワークツリーで可視
git fetch origin                    # すべてのワークツリーを更新
git branch -a                       # すべてのワークツリー間でブランチを表示
```

#### トラブルシューティング

**よくある問題と解決策:**

```bash
# 問題: ワークツリーディレクトリが既に存在
git worktree add ../worktrees/problem-025 problem-025
# エラー: '../worktrees/problem-025' already exists

# 解決策: まずディレクトリを削除するか、異なるパスを使用
rm -rf ../worktrees/problem-025
git worktree add ../worktrees/problem-025 problem-025

# 問題: ブランチが既に他のワークツリーでチェックアウト済み
# エラー: 'problem-025' is already checked out at '../worktrees/problem-025'

# 解決策: 異なるブランチ名を使用するか、他のワークツリーを削除
git worktree list                   # ブランチがどこでチェックアウトされているか確認
git worktree remove path/to/worktree

# 問題: 仮想環境の競合
# 各ワークツリーが独自の.venvを持つことを確認
cd ../worktrees/problem-025
uv sync --extra dev                 # 独立した.venvを作成

# 問題: 古いワークツリー参照
git worktree prune                  # 削除されたワークツリー参照をクリーンアップ
```

**クリーンアップ:**

```bash
# すべてのワークツリーを一覧表示
git worktree list

# 未使用のワークツリーを削除（ブランチがマージされた後）
git worktree prune

# ワークツリーを強制削除（ディレクトリが手動で削除された場合）
git worktree remove --force path/to/worktree
```

#### ワークツリーを使用するタイミング

**推奨される場面:**
- 複数の問題を同時に開発する場合
- 迅速な修正と並行した長期機能開発
- 異なるアルゴリズムアプローチの並行テスト
- 異なるPythonバージョン用の独立環境の維持

**避けるべき場面:**
- 単純な単一問題開発（従来のブランチングで十分）
- ディスク容量が限られている場合（各ワークツリーに独立した依存関係が必要）
- Git初心者の場合（まず基本的なブランチングから始める）

#### 実践的な使用例

**複数問題の並行開発:**

```bash
# 1. メインリポジトリで問題024を開発
cd project-euler-first100
git checkout -b problem-024
make new-problem PROBLEM=024

# 2. 問題025用のワークツリーを作成
git worktree add ../worktrees/problem-025 -b problem-025 origin/main
cd ../worktrees/problem-025
make new-problem PROBLEM=025

# 3. 問題026用のワークツリーを作成
git worktree add ../worktrees/problem-026 -b problem-026 origin/main
cd ../worktrees/problem-026
make new-problem PROBLEM=026

# 4. 各ワークツリーで独立して作業
# ワークツリー1で作業
cd ../worktrees/problem-025
# 実装、テスト、コミット

# ワークツリー2で作業
cd ../worktrees/problem-026
# 実装、テスト、コミット

# メインリポジトリで作業
cd project-euler-first100
# 実装、テスト、コミット
```

**長期機能開発と迅速な修正の並行:**

```bash
# 1. メインリポジトリで長期リファクタリング
cd project-euler-first100
git checkout -b refactor-performance
# 長期的な性能改善作業

# 2. 緊急のドキュメント修正用ワークツリー
git worktree add ../worktrees/hotfix-docs -b hotfix-docs origin/main
cd ../worktrees/hotfix-docs
# 迅速なドキュメント修正、テスト、PR作成

# 3. 新機能開発用ワークツリー
git worktree add ../worktrees/feature-benchmarks -b feature-benchmarks origin/main
cd ../worktrees/feature-benchmarks
# 新しいベンチマーク機能の開発
```

## テスト戦略

### テストの種類

#### 1. 単体テスト
- 各関数の動作を個別にテスト
- エッジケースのテスト
- 異常系のテスト

#### 2. 統合テスト
- 複数の関数の組み合わせテスト
- エンドツーエンドテスト

#### 3. パフォーマンステスト
- 実行時間の測定
- メモリ使用量の確認

### テストの実行

```bash
# 特定のテストファイルを実行
uv run pytest tests/problems/test_problem_XXX.py

# 特定のテストクラスを実行
uv run pytest tests/problems/test_problem_XXX.py::TestProblemXXX

# 特定のテストメソッドを実行
uv run pytest tests/problems/test_problem_XXX.py::TestProblemXXX::test_solve_naive

# マーカー付きテストを実行
uv run pytest -m "slow"

# 並列実行
uv run pytest -n auto

# カバレッジ付きで実行
uv run pytest --cov=problems --cov=solutions --cov-report=html
```

### テストカバレッジ

```bash
# カバレッジレポートの生成
uv run pytest --cov=problems --cov=solutions --cov-report=html

# カバレッジレポートの確認
open htmlcov/index.html
```

## コード品質チェック

### 自動チェック

```bash
# 全体的なコード品質チェック
uv run pre-commit run --all-files

# 個別のチェック
uv run ruff check problems/ solutions/ tests/
uv run ruff format problems/ solutions/ tests/
uv run mypy problems/ solutions/
```

### 手動チェック

#### 1. コードレビュー
- 機能面の確認
- コード品質の確認
- パフォーマンスの確認
- セキュリティの確認

#### 2. ドキュメントレビュー
- 解答説明の確認
- コメントの確認
- READMEの確認

## デプロイメントプロセス

### 1. ローカル環境での確認

```bash
# 依存関係の確認
uv sync

# テストの実行
uv run pytest

# コード品質チェック
uv run pre-commit run --all-files
```

### 2. CI/CDパイプライン

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install uv
      run: |
        curl -LsSf https://astral.sh/uv/install.sh | sh
        echo "$HOME/.cargo/bin" >> $GITHUB_PATH

    - name: Install dependencies
      run: uv sync

    - name: Run tests
      run: uv run pytest

    - name: Run linting
      run: uv run ruff check problems/ solutions/ tests/

    - name: Run type checking
      run: uv run mypy problems/ solutions/
```

### 3. 本番環境へのデプロイ

```bash
# タグの作成
git tag v1.0.0
git push origin v1.0.0

# リリースノートの作成
gh release create v1.0.0 --title "Release v1.0.0" --notes "## Changes

- Problem 001-005 completed
- Added comprehensive documentation
- Improved test coverage"
```

## トラブルシューティング

### よくある問題

#### 1. マージコンフリクト

```bash
# コンフリクトの解決
git status
# コンフリクトファイルを編集
git add .
git commit -m "Resolve merge conflicts"
```

#### 2. テストの失敗

```bash
# テストの詳細確認
uv run pytest tests/problems/test_problem_XXX.py -v -s

# デバッグモードで実行
uv run pytest tests/problems/test_problem_XXX.py -v -s --pdb
```

#### 3. コード品質チェックの失敗

```bash
# 自動修正
uv run ruff check --fix problems/problem_XXX.py
uv run ruff format problems/problem_XXX.py

# 手動修正
# エラーメッセージに従って修正
```

#### 4. 型チェックの失敗

```bash
# 型チェックの詳細確認
uv run mypy problems/problem_XXX.py --show-error-codes

# 型ヒントの追加
# エラーメッセージに従って修正
```

## ベストプラクティス

### 1. コミットメッセージ

- 明確で簡潔なメッセージ
- 英語で記述
- 動詞で始める
- 50文字以内のタイトル

### 2. コードレビュー

- 建設的なフィードバック
- 具体的な改善提案
- 学習機会の提供

### 3. ドキュメント

- 適切なコメント
- 詳細な解答説明
- 数学的背景の説明

### 4. テスト

- 十分なテストケース
- エッジケースのテスト
- パフォーマンステスト

## 参考資料

- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Pytest Best Practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [Ruff Best Practices](https://docs.astral.sh/ruff/)
