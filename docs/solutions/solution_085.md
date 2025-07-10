# Problem 085: Counting rectangles

## 問題の概要

長方形グリッド内に含まれる長方形の総数を数える問題です。例えば、3×2のグリッドには18個の長方形が含まれます。

目標は、ちょうど200万個に最も近い（ただし完全に一致しない）長方形の数を持つ長方形グリッドの面積を見つけることです。

## 数学的背景

### 長方形の数え方

m×nのグリッドに含まれる長方形の総数は、以下の公式で計算できます：

```
長方形数 = C(m+1, 2) × C(n+1, 2) = m(m+1)n(n+1)/4
```

これは、グリッド上で長方形を定義するために：
- 水平方向にm+1本の線から2本選ぶ（左端と右端）
- 垂直方向にn+1本の線から2本選ぶ（上端と下端）

という組み合わせ問題として考えることができるからです。

### 例：3×2グリッドの場合

```
長方形数 = 3×4×2×3/4 = 72/4 = 18
```

## 解法のアプローチ

### 1. 素直な解法（全探索）

```python
def solve_naive(target: int = 2000000) -> int:
    best_area = 0
    min_diff = float("inf")
    max_size = int((4 * target) ** 0.25) + 10

    for m in range(1, max_size):
        for n in range(1, m + 1):
            count = count_rectangles(m, n)
            diff = abs(count - target)

            if diff < min_diff:
                min_diff = diff
                best_area = m * n

            if count > target:
                break

    return best_area
```

**特徴：**
- 時間計算量：O(n²)
- 対称性を利用してn ≤ mの範囲のみ探索
- targetを超えたら早期終了

### 2. 最適化解法（二分探索）

```python
def solve_optimized(target: int = 2000000) -> int:
    best_area = 0
    min_diff = float("inf")
    max_size = int((4 * target) ** 0.25) + 10

    for m in range(1, max_size):
        left, right = 1, m

        while left <= right:
            mid = (left + right) // 2
            count = count_rectangles(m, mid)
            diff = abs(count - target)

            if diff < min_diff:
                min_diff = diff
                best_area = m * mid

            if count < target:
                left = mid + 1
            else:
                right = mid - 1

    return best_area
```

**特徴：**
- 時間計算量：O(n log n)
- 各mに対して最適なnを二分探索で効率的に見つける
- 探索範囲を大幅に削減

## 実装の詳細

### 探索範囲の決定

最大サイズの推定：
- count_rectangles(m, m) ≈ m⁴/4 = target
- したがって m ≈ (4×target)^(1/4)

200万の場合：
- m ≈ (8,000,000)^(1/4) ≈ 53

### 最適化のポイント

1. **対称性の利用**：m×nとn×mのグリッドは同じ数の長方形を持つ
2. **早期終了**：目標値を超えたら、それ以上の探索は不要
3. **二分探索**：単調性を利用して効率的に探索

## 解答

Project Euler公式サイトで確認してください。

## 検証

```python
# 3×2グリッドの例
assert count_rectangles(3, 2) == 18

# 解法の一致確認
assert solve_naive() == solve_optimized()
```

## パフォーマンス分析

| 解法 | 時間計算量 | 空間計算量 | 実行時間（目安） |
|------|------------|------------|------------------|
| 素直な解法 | O(n²) | O(1) | 〜10ms |
| 最適化解法 | O(n log n) | O(1) | 〜1ms |

## 学習ポイント

1. **組み合わせ論**：長方形の数を数える公式の導出
2. **二分探索**：単調性を持つ問題での効率的な探索
3. **最適化**：探索範囲の適切な設定と早期終了
4. **対称性**：問題の性質を利用した計算量の削減

## 関連問題

- Problem 086: Cuboid route（3次元版の最短経路問題）
- Problem 087: Prime power triples（素数の累乗の組み合わせ）
- Problem 088: Product-sum numbers（積和数）
