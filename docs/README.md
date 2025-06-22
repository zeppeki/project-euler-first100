# Documentation Directory

このディレクトリには、Project Euler First 100プロジェクトの包括的なドキュメントが含まれます。

## 📚 ドキュメント一覧

### 🚀 セットアップ・開発環境
- [`setup.md`](./setup.md) - 開発環境のセットアップ手順
  - uv、ruff、pytest等の最新ツールを使用した高速な開発環境の構築
  - トラブルシューティングとベストプラクティス

### 🤝 貢献・開発ガイド
- [`contributing.md`](./contributing.md) - 貢献ガイドライン
  - プロジェクトへの貢献方法
  - Issue作成、プルリクエスト、コードレビューのプロセス
  - コミットメッセージの規約と行動規範

- [`workflow.md`](./workflow.md) - 開発ワークフロー
  - 新しい問題に取り組む手順
  - ブランチ戦略とGitワークフロー
  - CI/CDパイプラインとデプロイメント

### 📝 コーディング・品質管理
- [`coding-standards.md`](./coding-standards.md) - コーディング規約
  - PEP 8準拠のPythonコーディング規約
  - 関数・クラスの命名規則
  - ドキュメント文字列と型ヒントの使用方法
  - テストコードの書き方

- [`testing.md`](./testing.md) - テストガイド
  - 単体テスト、統合テスト、パフォーマンステスト
  - pytestを使用したテストの実装
  - テストカバレッジとCI/CD

## 🎯 ドキュメントの目的

### 1. 開発効率の向上
- 統一された開発環境の構築
- 一貫したコーディング規約の適用
- 効率的なワークフローの実現

### 2. 品質の保証
- 包括的なテスト戦略
- 自動化されたコード品質チェック
- 継続的インテグレーション

### 3. 知識の共有
- 詳細な解答説明と数学的背景
- 学習ポイントの記録
- ベストプラクティスの共有

### 4. コミュニティの構築
- 明確な貢献ガイドライン
- 建設的なコードレビュー
- オープンなコミュニケーション

## 🛠️ 使用技術

### 開発環境
- **uv**: 高速なPythonパッケージマネージャー
- **ruff**: 高速なPythonフォーマッターとリンター
- **pytest**: テストフレームワーク
- **mypy**: 型チェッカー
- **pre-commit**: Gitフックによる自動チェック

### ドキュメント
- **Markdown**: メインドキュメント形式
- **GitHub**: バージョン管理とホスティング
- **GitHub Actions**: CI/CDパイプライン

## 📖 ドキュメントの更新

### 新しいドキュメントの追加
新しいドキュメントを追加する際は、このREADMEファイルも更新してください。

### ドキュメントの改善
- 定期的なレビューと更新
- ユーザーフィードバックの反映
- 最新のベストプラクティスの適用

## 🚀 クイックスタート

開発を始める前に、必ず [`setup.md`](./setup.md) を参照して開発環境をセットアップしてください。

### 基本的なセットアップ

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

### 開発ワークフロー

1. **セットアップ**: [`setup.md`](./setup.md) を参照
2. **貢献**: [`contributing.md`](./contributing.md) を参照
3. **開発**: [`workflow.md`](./workflow.md) を参照
4. **コーディング**: [`coding-standards.md`](./coding-standards.md) を参照
5. **テスト**: [`testing.md`](./testing.md) を参照

## 📋 ドキュメントの品質基準

### 必須要素
- ✅ 明確で分かりやすい説明
- ✅ 実用的な例とコードサンプル
- ✅ 最新の情報とベストプラクティス
- ✅ 適切な構造とナビゲーション

### 推奨要素
- 🔵 視覚的な要素（図表、スクリーンショット）
- 🔵 インタラクティブな要素
- 🔵 多言語対応
- 🔵 検索機能

## 🔗 関連リンク

- [メインREADME](../README.md) - プロジェクトの概要
- [PROGRESS.md](../PROGRESS.md) - 進捗状況
- [Project Euler](https://projecteuler.net/) - 公式サイト
- [uv公式ドキュメント](https://docs.astral.sh/uv/)
- [Ruff公式ドキュメント](https://docs.astral.sh/ruff/)

## 📞 サポート

ドキュメントに関する質問や改善提案がある場合は、以下の方法でお知らせください：

1. **Issue作成**: GitHubでIssueを作成
2. **プルリクエスト**: 直接的な改善提案
3. **ディスカッション**: GitHub Discussionsを使用

---

**Happy Documentation! 📚**

このドキュメントが、Project Euler First 100プロジェクトの成功に貢献することを願っています。
