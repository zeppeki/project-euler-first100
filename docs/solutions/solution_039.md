# Problem 039: Integer right triangles

## 問題
周囲の長さpが1000以下で、整数の辺を持つ直角三角形の解の数が最大となる値を求めよ。

## 詳細
If p is the perimeter of a right triangle with integral sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000 is the number of solutions maximised?

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)
```python
def solve_naive(max_perimeter):
    solution_counts = [0] * (max_perimeter + 1)

    for a in range(1, max_perimeter // 3):
        for b in range(a + 1, max_perimeter // 2):
            c_squared = a * a + b * b
            c = int(math.sqrt(c_squared))

            if c * c == c_squared:
                perimeter = a + b + c
                if perimeter <= max_perimeter:
                    solution_counts[perimeter] += 1

    max_solutions = max(solution_counts)
    return solution_counts.index(max_solutions)
```

**特徴:**
- 全ての可能な(a,b,c)の組み合わせを調べる
- a < b < c の制約を利用して探索範囲を制限
- 直角三角形の条件 a² + b² = c² をチェック

**時間計算量:** O(n³)
**空間計算量:** O(n)

### 2. 最適化解法 (Optimized Approach)
```python
def solve_optimized(max_perimeter):
    solution_counts = [0] * (max_perimeter + 1)

    for a in range(1, max_perimeter // 3):
        for b in range(a + 1, (max_perimeter - a) // 2):
            c_squared = a * a + b * b
            c = int(math.sqrt(c_squared))

            if c * c == c_squared and c > b:
                perimeter = a + b + c
                if perimeter <= max_perimeter:
                    solution_counts[perimeter] += 1

    max_solutions = max(solution_counts)
    return solution_counts.index(max_solutions)
```

**特徴:**
- a < b < c の制約をより効率的に利用
- 内側ループの範囲をより厳密に制限
- 不要な計算を削減

**時間計算量:** O(n²)
**空間計算量:** O(n)

### 3. 数学的解法 (Mathematical Approach)
```python
def solve_mathematical(max_perimeter):
    solution_counts = [0] * (max_perimeter + 1)

    m = 2
    while m * m <= max_perimeter:
        for n in range(1, m):
            if math.gcd(m, n) == 1 and (m % 2 != n % 2):
                # ピタゴラス数の基本形を生成
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n

                if a > b:
                    a, b = b, a

                base_perimeter = a + b + c

                # 倍数を含めて全ての解を生成
                k = 1
                while k * base_perimeter <= max_perimeter:
                    perimeter = k * base_perimeter
                    solution_counts[perimeter] += 1
                    k += 1
        m += 1

    max_solutions = max(solution_counts)
    return solution_counts.index(max_solutions)
```

**特徴:**
- ピタゴラス数の公式を活用: a = m²-n², b = 2mn, c = m²+n²
- 互いに素で異なる偶奇性を持つ(m,n)ペアから基本解を生成
- 倍数を考慮して全ての解を網羅
- 最も数学的に洗練されたアプローチ

**時間計算量:** O(n√n)
**空間計算量:** O(n)

## 数学的背景

### ピタゴラス数の性質
直角三角形の整数解(a, b, c)は**ピタゴラス数**と呼ばれ、以下の性質を持つ：

1. **基本ピタゴラス数**: gcd(a,b,c) = 1 となる最小の解
2. **一般ピタゴラス数**: 基本ピタゴラス数の整数倍

### ピタゴラス数の公式
互いに素で異なる偶奇性を持つ正整数 m > n について：
- a = m² - n²
- b = 2mn
- c = m² + n²

この公式により、全ての基本ピタゴラス数を生成できる。

### 例
m=2, n=1 の場合：
- a = 4 - 1 = 3
- b = 2×2×1 = 4
- c = 4 + 1 = 5
- → (3, 4, 5) の基本ピタゴラス数

## アルゴリズム比較

| 解法 | 時間計算量 | 空間計算量 | 特徴 |
|------|------------|------------|------|
| 素直 | O(n³) | O(n) | 直感的、理解しやすい |
| 最適化 | O(n²) | O(n) | 制約による効率化 |
| 数学的 | O(n√n) | O(n) | ピタゴラス数の公式活用 |

## 検証

### 例題の確認
p = 120 の場合の3つの解：
1. (20, 48, 52): 20² + 48² = 400 + 2304 = 2704 = 52²
2. (24, 45, 51): 24² + 45² = 576 + 2025 = 2601 = 51²
3. (30, 40, 50): 30² + 40² = 900 + 1600 = 2500 = 50²

### 小さな値での検証
- p = 12: 1つの解 (3, 4, 5)
- p = 30: 1つの解 (5, 12, 13)
- p = 60: 2つの解 (10, 24, 26), (15, 20, 25)

## 学習ポイント

1. **制約による最適化**: a < b < c の制約で探索空間を大幅削減
2. **数学的性質の活用**: ピタゴラス数の公式による効率的な解生成
3. **倍数関係**: 基本解から倍数を生成して全解を網羅
4. **計算量の改善**: O(n³) → O(n²) → O(n√n) への段階的最適化

この問題は数論とアルゴリズム最適化の良い例題となっている。
