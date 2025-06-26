# Problem 022: Names Scores

## 問題文

テキストファイル（約5000以上の名前を含む）を読み込み、アルファベット順にソートして各名前の「アルファベット値」を計算する問題です。

各名前のアルファベット値は、各文字の位置（A=1, B=2, ..., Z=26）の合計です。
各名前のスコアは、アルファベット値にソート後のリスト位置を掛けた値です。
全ての名前スコアの合計を求めます。

**例**: 「COLIN」のアルファベット値は53（3+15+12+9+14）、ソート後938番目の位置なので、スコアは938 × 53 = 49,714

## 解答

Project Euler公式サイトで確認してください。

## 解法

### アプローチ1: 素直な解法 (`solve_naive`)

最も直感的なアプローチ：

1. 名前リストをアルファベット順にソート
2. 各名前に対してアルファベット値を計算
3. 位置×アルファベット値でスコアを計算
4. 全スコアを合計

```python
def solve_naive(names: List[str]) -> int:
    sorted_names = sorted(names)
    total_score = 0

    for position, name in enumerate(sorted_names, 1):
        alphabetical_value = get_alphabetical_value(name)
        name_score = position * alphabetical_value
        total_score += name_score

    return total_score
```

- **時間計算量**: O(n log n) - ソートが支配的
- **空間計算量**: O(n) - ソート用の新しいリスト

### アプローチ2: 最適化解法 (`solve_optimized`)

メモリ効率を改善したアプローチ：

1. リストのコピーを作成してインプレースソート
2. 効率的なアルファベット値計算
3. 一度のループで処理完了

```python
def solve_optimized(names: List[str]) -> int:
    names_copy = names.copy()
    names_copy.sort()

    total_score = 0
    for position, name in enumerate(names_copy, 1):
        alphabetical_value = sum(ord(char) - ord('A') + 1 for char in name)
        total_score += position * alphabetical_value

    return total_score
```

- **時間計算量**: O(n log n) - ソートのボトルネック
- **空間計算量**: O(1) - インプレースソート使用

### アプローチ3: 数学的解法 (`solve_mathematical`)

より数学的な表現を使用したアプローチ：

1. ソートとスコア計算を一つの式で表現
2. 関数型プログラミングスタイルの実装

```python
def solve_mathematical(names: List[str]) -> int:
    sorted_names = sorted(names)

    total_score = sum(
        (position + 1) * sum(ord(char) - ord('A') + 1 for char in name)
        for position, name in enumerate(sorted_names)
    )

    return total_score
```

- **時間計算量**: O(n log n) - ソートが支配的
- **空間計算量**: O(n) - ソート用のリスト

## 実装のポイント

### 1. アルファベット値計算

```python
def get_alphabetical_value(name: str) -> int:
    return sum(ord(char) - ord('A') + 1 for char in name.upper())
```

- ASCII値を利用した効率的な計算
- 大文字小文字に対応

### 2. ファイル読み込み

```python
def load_names_from_file(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        names = [name.strip('"') for name in content.split(',')]
        return names
```

- カンマ区切りの引用符付き形式に対応
- エラーハンドリング付き

### 3. データ構造の選択

- リスト: 順序が重要でソートが必要
- 文字列: アルファベット値計算が主要操作

## アルゴリズム分析

### 時間計算量

全てのアプローチで **O(n log n)** となります：

- ソート処理: O(n log n)
- アルファベット値計算: O(n × m) ここでmは名前の平均長
- 実質的にソートが支配的

### 空間計算量

- 素直な解法: O(n) - ソート用の新しいリスト
- 最適化解法: O(n) - リストのコピー
- 数学的解法: O(n) - ソート用のリスト

### 実際のパフォーマンス

5000名程度のデータセットでは：
- 実行時間: 数ミリ秒以下
- メモリ使用量: 数百KB程度

## エッジケースと考慮事項

### 1. データファイル

- 公式のnames.txtファイルが必要
- カンマ区切り、引用符付き形式
- UTF-8エンコーディング推奨

### 2. 名前の重複

重複する名前がある場合：
- それぞれ異なる位置を持つ
- 同じアルファベット値でも異なるスコア

### 3. 空データ

- 空リスト: スコア0
- 単一名前: 1位×アルファベット値

## 検証

### テストケース

```python
# 基本例
names = ["COLIN", "ANN", "MARY"]
# ソート後: ["ANN", "COLIN", "MARY"]
# スコア: 1×29 + 2×53 + 3×57 = 306
```

### 問題文の例

- COLIN: アルファベット値53
- 実際のデータでは938番目
- スコア: 938 × 53 = 49,714

## 学習ポイント

### 1. 文字列処理

- ASCII値を使用した効率的な文字変換
- 大文字小文字の統一処理

### 2. ソートアルゴリズム

- Pythonの組み込みソート（Timsort）の活用
- 安定ソートの特性

### 3. ファイルI/O

- CSVライクなデータ形式の処理
- エラーハンドリングの重要性

### 4. アルゴリズム設計

- 複数のアプローチによる問題解決
- 時間vs空間のトレードオフ

### 5. データ処理パターン

- 前処理（ソート）→計算→集約のパターン
- バッチ処理とストリーム処理の選択

## まとめ

Problem 022は文字列処理とソートアルゴリズムを組み合わせた問題です。主要な学習ポイントは：

1. **効率的な文字列処理**: ASCII値を活用した計算
2. **ソートの重要性**: アルゴリズムの時間計算量を決定
3. **ファイル処理**: 実際のデータファイルとの連携
4. **スケーラビリティ**: 大量データへの対応

実装では可読性と効率性のバランスを考慮し、適切なデータ構造とアルゴリズムの選択が重要です。
