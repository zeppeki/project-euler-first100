# 緊急度高: ドキュメント改善作業計画

## Issue作成用テンプレート

### Issue Title
```
緊急: ドキュメント改善 - 不完全な解答ドキュメントの完成と進捗情報の統一
```

### Issue Body
```markdown
## 緊急度: 高 - ドキュメント改善作業

### 問題の概要
プロジェクトのドキュメント品質向上のため、以下の緊急度の高い問題を解決する必要があります。

### 1. 不完全な解答ドキュメントの完成
**問題**: 以下の解答ドキュメントが未完成（TODOタグが残っている）
- `docs/solutions/solution_036.md`
- `docs/solutions/solution_037.md`

**影響**:
- ユーザーが学習内容を理解できない
- プロジェクトの品質評価が下がる
- 新しい貢献者が混乱する

**対応内容**:
- [ ] `solution_036.md`の内容を完成させる
- [ ] `solution_037.md`の内容を完成させる
- [ ] 数学的背景、解法説明、学習ポイントを追加
- [ ] パフォーマンス分析セクションを追加

### 2. 進捗情報の不整合修正
**問題**: 進捗情報が複数ファイルで異なる値を示している
- README.md: 「完了問題: 20/100」
- PROGRESS.md: 「41/100」
- docs/index.md: 「31/100」

**影響**:
- ユーザーが正確な進捗を把握できない
- プロジェクトの信頼性が低下する

**対応内容**:
- [ ] 実際の完了問題数を正確に調査
- [ ] すべてのファイルで進捗情報を統一
- [ ] 進捗情報の自動更新仕組みを検討

### 3. ディレクトリ構造の整理
**問題**: `solutions/`ディレクトリが空で、`docs/solutions/`に解答ドキュメントが存在
**影響**: 混乱を招く可能性がある

**対応内容**:
- [ ] ディレクトリ構造の役割を明確化
- [ ] 必要に応じてリダイレクトまたは統合
- [ ] ドキュメント構造の整理

### 技術的詳細

#### ファイル調査が必要な項目
```bash
# 完了問題数の正確な調査
find problems/ -name "problem_*.py" | wc -l
find docs/solutions/ -name "solution_*.md" | wc -l
grep -r "🟢 完了" PROGRESS.md | wc -l
```

#### 作業手順
1. **現状調査**
   - 実際の完了問題数を正確にカウント
   - 不完全なドキュメントの詳細確認

2. **ドキュメント完成**
   - Problem 036, 037の実装内容を確認
   - 数学的背景と解法説明を追加
   - パフォーマンス分析を追加

3. **進捗情報統一**
   - 正確な進捗数を算出
   - 全ファイルで統一
   - 自動更新の仕組みを検討

4. **構造整理**
   - ディレクトリ構造の最適化
   - ナビゲーションの改善

### 期待される成果
- ✅ すべての解答ドキュメントが完成
- ✅ 進捗情報が正確で統一されている
- ✅ ドキュメント構造が整理されている
- ✅ ユーザビリティの向上

### 参考資料
- [Project Euler Problem 036](https://projecteuler.net/problem=36)
- [Project Euler Problem 037](https://projecteuler.net/problem=37)
- 既存の完成した解答ドキュメント（例: `solution_001.md`）

### ラベル
- `documentation`
- `bug`
- `high-priority`
- `maintenance`
```

## 手動作業手順

### 1. GitHub Web UIでIssue作成
1. https://github.com/zeppeki/project-euler-first100/issues にアクセス
2. "New issue" ボタンをクリック
3. 上記のテンプレートをコピー&ペースト
4. 適切なラベルを設定
5. Issueを作成

### 2. 作業開始前の準備
```bash
# 現在のブランチを確認
git branch

# mainブランチに切り替え
git checkout main

# 最新の変更を取得
git pull origin main

# 新しい作業ブランチを作成
git checkout -b fix/documentation-improvements
```

### 3. 現状調査コマンド
```bash
# 完了問題数の調査
echo "=== 完了問題数調査 ==="
echo "problems/ ディレクトリのファイル数:"
find problems/ -name "problem_*.py" | wc -l

echo "docs/solutions/ ディレクトリのファイル数:"
find docs/solutions/ -name "solution_*.md" | wc -l

echo "PROGRESS.md の完了マーク数:"
grep -r "🟢 完了" PROGRESS.md | wc -l

echo "=== 不完全なドキュメント確認 ==="
grep -r "TODO" docs/solutions/solution_036.md
grep -r "TODO" docs/solutions/solution_037.md
```

### 4. 優先順位
1. **最優先**: 不完全なドキュメントの完成
2. **高優先**: 進捗情報の統一
3. **中優先**: ディレクトリ構造の整理

## 完了基準
- [ ] `solution_036.md` が完成している
- [ ] `solution_037.md` が完成している
- [ ] 全ファイルで進捗情報が統一されている
- [ ] ディレクトリ構造が整理されている
- [ ] テストが通っている
- [ ] CI/CDが成功している
