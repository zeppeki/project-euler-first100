# 貢献ガイドライン

このドキュメントでは、Project Euler First 100プロジェクトへの貢献方法を説明します。

## はじめに

このプロジェクトへの貢献を検討していただき、ありがとうございます。どのような形での貢献も歓迎します。

## 貢献の種類

### 1. 問題の解決
- 新しいProject Euler問題の解答実装
- 既存解答の最適化
- 複数言語での実装

### 2. ドキュメントの改善
- 解答説明の追加・改善
- コードコメントの追加
- READMEファイルの更新

### 3. テストの追加
- 新しいテストケースの追加
- テストカバレッジの向上
- テストの最適化

### 4. バグ修正
- 既存コードのバグ修正
- パフォーマンスの改善
- セキュリティの向上

### 5. 機能追加
- 新しいツールやスクリプトの追加
- CI/CDパイプラインの改善
- 開発環境の改善

## 開発環境のセットアップ

貢献を始める前に、開発環境をセットアップしてください。

```bash
# リポジトリをフォークしてクローン
git clone https://github.com/YOUR_USERNAME/project-euler-first100.git
cd project-euler-first100

# 開発環境のセットアップ
uv sync
uv run pre-commit install
```

詳細なセットアップ手順は [`setup.md`](./setup.md) を参照してください。

## 開発ワークフロー

### 1. Issueの作成

新しい問題に取り組む際は、まずIssueを作成してください。

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
- [ ] 解答の検証
- [ ] 解答の説明をsolutions/に追加
- [ ] 進捗表の更新

### ファイル
- `problems/problem_XXX.py`
- `solutions/solution_XXX.md`

### 参考
- [Project Euler Problem XXX](https://projecteuler.net/problem=XXX)" --label "problem,XXX,in-progress"
```

### 2. ブランチの作成

```bash
# 新しいブランチを作成
git checkout -b problem-XXX

# または、GitHub CLIを使用
gh issue develop [ISSUE_NUMBER]
git checkout [BRANCH_NAME]
```

### 3. 開発作業

#### 3.1 問題ファイルの作成

```python
#!/usr/bin/env python3
"""
Problem XXX: [問題タイトル]

[問題の詳細説明]

Answer: [解答]
"""

import time
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
    数学的解法
    時間計算量: O(...)
    空間計算量: O(...)
    """
    # 実装
    pass

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

def main():
    """メイン関数"""
    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(parameters)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(parameters)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(parameters)
    math_time = time.time() - start_time

    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized == result_math:
        print(f"✓ 解答: {result_optimized:,}")
    else:
        print("✗ 解答が一致しません")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time/fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time/fastest_time:.2f}x")
    print(f"数学的解法: {math_time/fastest_time:.2f}x")

if __name__ == "__main__":
    main()
```

#### 3.2 テストファイルの作成

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

#### 3.3 解答説明ファイルの作成

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

### 4. テストとコード品質チェック

```bash
# テストの実行
uv run pytest tests/problems/test_problem_XXX.py -v

# コード品質チェック
uv run ruff check problems/problem_XXX.py
uv run ruff format problems/problem_XXX.py

# 型チェック
uv run mypy problems/problem_XXX.py

# pre-commitフックの実行
uv run pre-commit run --all-files
```

### 5. コミットとプッシュ

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

### 6. プルリクエストの作成

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

### 7. プルリクエストのマージ

```bash
# プルリクエストをマージ
gh pr merge [PR_NUMBER] --merge

# mainブランチに切り替え
git checkout main
git pull origin main
```

### 8. Issueのクローズ

```bash
# Issueをクローズ
gh issue close [ISSUE_NUMBER] --reason completed
```

## コミットメッセージの規約

### 基本形式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### タイプ

- **feat**: 新機能
- **fix**: バグ修正
- **docs**: ドキュメントのみの変更
- **style**: コードの意味に影響しない変更（空白、フォーマット等）
- **refactor**: バグ修正や機能追加ではないコードの変更
- **test**: テストの追加や修正
- **chore**: ビルドプロセスや補助ツールの変更

### 例

```
feat(problem-001): add solution for Multiples of 3 and 5

- Implement naive solution with O(n) time complexity
- Add optimized solution using arithmetic series formula
- Include comprehensive test cases
- Add detailed solution explanation

Answer: 233168

Closes #1
```

## コードレビューのプロセス

### レビューの準備

1. **自己レビュー**: プルリクエストを作成する前に、自分のコードをレビュー
2. **テスト実行**: すべてのテストが通ることを確認
3. **コード品質チェック**: ruff、mypy等のチェックが通ることを確認

### レビューのポイント

#### 機能面
- [ ] 正しい解答を返すか
- [ ] エッジケースを適切に処理しているか
- [ ] パフォーマンスは適切か
- [ ] メモリ使用量は適切か

#### コード品質
- [ ] コードは読みやすいか
- [ ] 適切なコメントがあるか
- [ ] 関数名は分かりやすいか
- [ ] 型ヒントは適切か

#### テスト
- [ ] テストケースは十分か
- [ ] エッジケースのテストがあるか
- [ ] テストは理解しやすいか

#### ドキュメント
- [ ] 解答説明は分かりやすいか
- [ ] 数学的背景は適切に説明されているか
- [ ] 参考資料は適切か

### レビューコメントの例

```markdown
## 良い点
- 複数の解法を実装している
- テストケースが充実している
- パフォーマンス分析が詳細

## 改善点
- 関数名をより具体的にしてください
- この部分のコメントを追加してください
- エッジケースのテストを追加してください

## 質問
- このアルゴリズムの時間計算量は？
- なぜこのデータ構造を選択したのですか？
```

## Issue作成のガイドライン

### Issueの種類

#### 1. 問題解決Issue
- **タイトル**: `Solve Problem XXX: [問題タイトル]`
- **ラベル**: `problem`, `XXX`, `in-progress`
- **テンプレート**: 上記の開発ワークフローを参照

#### 2. バグ報告Issue
- **タイトル**: `Fix: [バグの簡潔な説明]`
- **ラベル**: `bug`
- **内容**:
  - バグの詳細な説明
  - 再現手順
  - 期待される動作
  - 実際の動作
  - 環境情報

#### 3. 機能要求Issue
- **タイトル**: `Feature: [機能の簡潔な説明]`
- **ラベル**: `enhancement`
- **内容**:
  - 機能の詳細な説明
  - 必要性の説明
  - 実装案（可能であれば）

#### 4. ドキュメントIssue
- **タイトル**: `Docs: [ドキュメントの簡潔な説明]`
- **ラベル**: `documentation`
- **内容**:
  - 改善したいドキュメント
  - 改善内容の詳細
  - 理由

### Issueテンプレート

```markdown
## 概要
[簡潔な説明]

## 詳細
[詳細な説明]

## 再現手順（バグの場合）
1. [手順1]
2. [手順2]
3. [手順3]

## 期待される動作
[期待される動作]

## 実際の動作
[実際の動作]

## 環境情報
- OS: [OS名とバージョン]
- Python: [バージョン]
- uv: [バージョン]

## 追加情報
[その他の情報]
```

## 行動規範

### コミュニケーション

- **敬意を払う**: 他の貢献者を尊重し、建設的なフィードバックを提供
- **明確に伝える**: 質問や提案は明確に、具体的に
- **協力的**: 他の貢献者をサポートし、知識を共有

### コード品質

- **読みやすさ**: 他の開発者が理解しやすいコードを書く
- **保守性**: 将来の変更を考慮した設計
- **テスト**: 適切なテストケースを提供
- **ドキュメント**: 必要なコメントとドキュメントを追加

### プロジェクトの目標

- **学習**: 数学とプログラミングのスキル向上
- **共有**: 知識と経験の共有
- **品質**: 高品質なコードとドキュメント
- **コミュニティ**: 建設的な開発者コミュニティの構築

## よくある質問

### Q: どの問題から始めればよいですか？
A: 未着手の問題（🔴）から始めることをお勧めします。PROGRESS.mdで現在の状況を確認してください。

### Q: 複数の解法を実装する必要がありますか？
A: はい、最低3つの解法（素直な解法、最適化解法、数学的解法）の実装を推奨します。

### Q: テストはどの程度書けばよいですか？
A: 基本的なテストケースとエッジケースを含めて、十分なカバレッジを確保してください。

### Q: プルリクエストのレビューはどのくらい時間がかかりますか？
A: 通常1-3日以内にレビューを行います。緊急の場合は、Issueでお知らせください。

## サポート

貢献に関する質問や問題がある場合は、以下の方法でサポートを受けることができます：

1. **Issue作成**: GitHubでIssueを作成
2. **ディスカッション**: GitHub Discussionsを使用
3. **ドキュメント**: このドキュメントと他のドキュメントを参照

## 謝辞

このプロジェクトに貢献していただき、ありがとうございます。皆さんの貢献により、より良い学習環境とコミュニティを作ることができます。 