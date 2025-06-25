# Problem 018: Maximum Path Sum I

## 問題概要

三角形状に配置された数値において、上から下への隣接する数値のみに移動できる条件で、経路の合計値が最大となるパスを見つける問題です。

### 問題文

三角形の頂点から始めて、下の行の隣接する数値に移動していき、頂点から底辺までの最大合計を求めます。

例題:
```
   3
  7 4
 2 4 6
8 5 9 3
```

この場合、3 + 7 + 4 + 9 = 23 が最大合計となります。

### 制約条件

- 15行の三角形が与えられる
- 各位置から次の行では隣接する2つの位置のみに移動可能
- 全経路数: 2^14 = 16,384通り（ブルートフォース可能だが非効率）

## 解法

### 1. 素直な解法 (solve_naive)

**アプローチ**: 全経路を再帰的に探索

```python
def solve_naive(triangle: List[List[int]]) -> int:
    def max_path_from(row: int, col: int) -> int:
        if row >= len(triangle):
            return 0

        current = triangle[row][col]
        if row == len(triangle) - 1:
            return current

        left = max_path_from(row + 1, col)
        right = max_path_from(row + 1, col + 1)

        return current + max(left, right)

    return max_path_from(0, 0)
```

**特徴**:
- 時間計算量: O(2^n) - 指数時間
- 空間計算量: O(n) - 再帰スタック
- 同じ部分問題を繰り返し計算するため非効率

### 2. 最適化解法 (solve_optimized)

**アプローチ**: 動的プログラミング（メモ化）

```python
def solve_optimized(triangle: List[List[int]]) -> int:
    memo = {}

    def max_path_from(row: int, col: int) -> int:
        if (row, col) in memo:
            return memo[(row, col)]

        # 計算結果をメモ化
        result = current + max(left, right)
        memo[(row, col)] = result
        return result

    return max_path_from(0, 0)
```

**特徴**:
- 時間計算量: O(n²) - 各位置を1回だけ計算
- 空間計算量: O(n²) - メモ化テーブル
- 重複計算を排除して大幅に高速化

### 3. 数学的解法 (solve_mathematical)

**アプローチ**: ボトムアップ動的プログラミング

```python
def solve_mathematical(triangle: List[List[int]]) -> int:
    dp = [row[:] for row in triangle]

    # 底辺から上に向かって計算
    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]
```

**特徴**:
- 時間計算量: O(n²)
- 空間計算量: O(n) - インプレース更新可能
- 再帰オーバーヘッドがなく最も効率的

## アルゴリズム解説

### 動的プログラミングの原理

この問題は**最適部分構造**を持つため、動的プログラミングが有効です：

1. **部分問題**: 各位置からの最大パス合計
2. **再帰関係**: `dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])`
3. **基底条件**: 最下行では現在の値がそのまま答え

### ボトムアップ vs トップダウン

**ボトムアップ（推奨）**:
- 底辺から計算するため依存関係が明確
- 再帰スタックが不要
- 空間効率が良い

**トップダウン（メモ化）**:
- 直感的な実装
- 不要な部分問題は計算しない
- メモリ使用量が多い

## 実装のポイント

### 1. 三角形の表現

```python
triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    # ...
]
```

### 2. 隣接関係の処理

位置 `(i, j)` から移動可能な位置:
- `(i+1, j)` - 左下
- `(i+1, j+1)` - 右下

### 3. 境界条件の処理

- 最下行: 現在の値がそのまま答え
- インデックス範囲チェック

## パフォーマンス分析

| 解法 | 時間計算量 | 空間計算量 | 15行での実行時間 |
|------|------------|------------|------------------|
| 素直な解法 | O(2^n) | O(n) | 〜0.1秒 |
| 最適化解法 | O(n²) | O(n²) | <0.001秒 |
| 数学的解法 | O(n²) | O(n) | <0.001秒 |

## 発展的考察

### Problem 67との関係

Problem 67では100行の三角形を扱うため、効率的なアルゴリズムが必須：
- ブルートフォース: 2^99通り（計算不可能）
- 動的プログラミング: O(100²) = 10,000回（十分高速）

### 空間最適化

ボトムアップDPでは前の行の情報のみ必要なため、O(n)空間で実装可能：

```python
def solve_space_optimized(triangle):
    prev_row = triangle[-1][:]  # 最下行をコピー

    for i in range(len(triangle) - 2, -1, -1):
        current_row = []
        for j in range(len(triangle[i])):
            max_below = max(prev_row[j], prev_row[j + 1])
            current_row.append(triangle[i][j] + max_below)
        prev_row = current_row

    return prev_row[0]
```

## 関連問題

- **Problem 067**: Maximum Path Sum II（100行版）
- **Problem 081**: Path sum: two ways（グリッド版）
- **Problem 082**: Path sum: three ways
- **Problem 083**: Path sum: four ways

## 学習ポイント

1. **動的プログラミングの適用判断**
2. **トップダウン vs ボトムアップの選択**
3. **メモ化による最適化技法**
4. **空間効率の改善方法**
5. **再帰の深さとスタックオーバーフロー対策**

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **例題入力**: 4行の三角形
- **例題解答**: [隠匿]
- **本問題解答**: [隠匿]
- **検証**: ✓ 全解法で一致確認
