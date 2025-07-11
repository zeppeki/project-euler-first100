## 問題

現在、多くのrunnerファイルで`sys.path.insert`を使用してインポートパスを動的に追加しています。これは以下の問題を引き起こします：

### 現在の問題
- **コードの可読性低下**: 動的なパス操作により、依存関係が不明確
- **保守性の問題**: パス構造が変更されると、多くのファイルを修正する必要がある
- **IDEサポートの悪化**: 静的解析ツールが依存関係を正しく追跡できない
- **デバッグの困難**: インポートエラーが発生した際の原因特定が困難

### 影響を受けるファイル
以下の24ファイルで`sys.path.insert`が使用されています：

```
problems/runners/problem_039_runner.py
problems/runners/problem_047_runner.py
problems/runners/problem_058_runner.py
problems/runners/problem_059_runner.py
problems/runners/problem_071_runner.py
problems/runners/problem_072_runner.py
problems/runners/problem_073_runner.py
problems/runners/problem_074_runner.py
problems/runners/problem_075_runner.py
problems/runners/problem_076_runner.py
problems/runners/problem_077_runner.py
problems/runners/problem_078_runner.py
problems/runners/problem_082_runner.py
problems/runners/problem_083_runner.py
problems/runners/problem_084_runner.py
problems/runners/problem_085_runner.py
problems/runners/problem_086_runner.py
problems/runners/problem_087_runner.py
problems/runners/problem_088_runner.py
problems/runners/problem_089_runner.py
problems/runners/problem_091_runner.py
```

### 解決策

#### 1. プロジェクト構造の見直し
- `problems/runners/`ディレクトリを`runners/`に移動
- または、`__init__.py`ファイルを適切に配置してPythonパッケージとして認識させる

#### 2. 相対インポートの使用
- 絶対インポートを相対インポートに変更
- 例: `from problems.problem_XXX import ...` → `from ..problem_XXX import ...`

#### 3. PYTHONPATHの設定
- MakefileやスクリプトでPYTHONPATHを設定
- 環境変数による解決

### 推奨アプローチ

#### オプションA: 相対インポートへの変更
```python
# 現在
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from problems.problem_XXX import ...

# 変更後
from ..problem_XXX import ...
```

#### オプションB: プロジェクト構造の変更
```
project-euler-first100/
├── problems/
│   ├── __init__.py
│   ├── problem_XXX.py
│   └── ...
├── runners/
│   ├── __init__.py
│   ├── problem_XXX_runner.py
│   └── ...
└── ...
```

### タスク
- [ ] 現在のインポート構造の分析
- [ ] 最適な解決策の選択
- [ ] 相対インポートへの変更（オプションA）
- [ ] または、プロジェクト構造の変更（オプションB）
- [ ] すべてのrunnerファイルの修正
- [ ] テストの実行と検証
- [ ] CI/CDの確認

### 期待される効果
- ✅ コードの可読性向上
- ✅ 保守性の向上
- ✅ IDEサポートの改善
- ✅ デバッグの容易化
- ✅ プロジェクト構造の標準化

### 参考
- [Python Import System](https://docs.python.org/3/reference/import.html)
- [Relative vs Absolute Imports](https://realpython.com/absolute-vs-relative-python-imports/)
- [Python Package Structure](https://packaging.python.org/tutorials/packaging-projects/)
