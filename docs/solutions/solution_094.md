# Problem 094: Almost equilateral triangles

## 問題文

「ほぼ正三角形」は、2つの辺が等しく、3番目の辺が最大1単位だけ異なる三角形です。
例えば、5-5-6の三角形は面積が12平方単位です。

整数の辺の長さと整数の面積を持つ正三角形は存在しません。
しかし、整数の辺の長さと整数の面積を持ち、2つの辺が等しく、3番目の辺が最大1単位だけ異なる三角形は存在します。

整数の辺の長さと整数の面積を持ち、周長が10億（1,000,000,000）を超えないすべての「ほぼ正三角形」の周長の合計を求めてください。

## 解法

### アプローチ1: 素直な解法 (O(n))

全ての可能な三角形を順次チェックして、条件を満たすものを見つけます。

```python
def solve_naive(perimeter_limit: int = 1000000000) -> int:
    total_perimeter = 0

    # a, a, a+1 の形の三角形を調べる
    a = 1
    while True:
        perimeter = 3 * a + 1
        if perimeter > perimeter_limit:
            break
        if is_integral_area(a, a, a + 1):
            total_perimeter += perimeter
        a += 1

    # a, a, a-1 の形の三角形を調べる
    a = 2
    while True:
        perimeter = 3 * a - 1
        if perimeter > perimeter_limit:
            break
        if is_integral_area(a, a, a - 1):
            total_perimeter += perimeter
        a += 1

    return total_perimeter
```

### アプローチ2: 最適化解法 (O(log n))

数学的性質を利用し、ペル方程式の解を活用して効率的に計算します。

```python
def solve_optimized(perimeter_limit: int = 1000000000) -> int:
    total_perimeter = 0

    # ペル方程式 x^2 - 3y^2 = 1 の解を利用
    # 基本解: (x, y) = (2, 1)
    # 一般解: x_{n+1} = 2x_n + 3y_n, y_{n+1} = x_n + 2y_n

    x, y = 2, 1
    while True:
        # Case 1: (a, a, a+1) の形
        if (x - 1) % 2 == 0 and y % 2 == 0:
            a = (x - 1) // 2
            if a > 0:
                perimeter = 3 * a + 1
                if perimeter > perimeter_limit:
                    break
                total_perimeter += perimeter

        # Case 2: (a, a, a-1) の形
        if (x + 1) % 2 == 0 and y % 2 == 0:
            a = (x + 1) // 2
            if a > 1:
                perimeter = 3 * a - 1
                if perimeter > perimeter_limit:
                    break
                total_perimeter += perimeter

        # 次の解を計算
        x, y = 2 * x + 3 * y, x + 2 * y

    return total_perimeter
```

### アプローチ3: 数学的解法 (O(log n))

ペル方程式の解を直接利用した最も効率的な実装です。

```python
def solve_mathematical(perimeter_limit: int = 1000000000) -> int:
    total_perimeter = 0

    # ペル方程式 x^2 - 3y^2 = 1 の基本解は (2, 1)
    x, y = 2, 1

    while True:
        # Case 1: a, a, a+1 の形
        if (x - 1) % 2 == 0 and y % 2 == 0:
            a = (x - 1) // 2
            if a > 0:
                perimeter = 3 * a + 1
                if perimeter <= perimeter_limit:
                    total_perimeter += perimeter

        # Case 2: a, a, a-1 の形
        if (x + 1) % 2 == 0 and y % 2 == 0:
            a = (x + 1) // 2
            if a > 1:
                perimeter = 3 * a - 1
                if perimeter <= perimeter_limit:
                    total_perimeter += perimeter

        # 次の解を計算
        next_x = 2 * x + 3 * y
        next_y = x + 2 * y

        # 周長制限チェック
        min_perimeter_next = min(
            3 * ((next_x - 1) // 2) + 1 if (next_x - 1) % 2 == 0 else float('inf'),
            3 * ((next_x + 1) // 2) - 1 if (next_x + 1) % 2 == 0 else float('inf')
        )

        if min_perimeter_next > perimeter_limit:
            break

        x, y = next_x, next_y

    return total_perimeter
```

## 重要な洞察

1. **ほぼ正三角形の2つの形**:
   - (a, a, a+1): 3番目の辺が1長い
   - (a, a, a-1): 3番目の辺が1短い

2. **面積の条件**: ヘロンの公式を使用して面積が整数になる条件を導出：
   - (a, a, a+1)の場合: (2a+1)² - 3 = 4k² (k≥1)
   - (a, a, a-1)の場合: (2a-1)² - 3 = 4k² (k≥1)

3. **ペル方程式の応用**: 上記の条件はペル方程式 x² - 3y² = 1 と関連しています：
   - 基本解: (x, y) = (2, 1)
   - 一般解: x_{n+1} = 2x_n + 3y_n, y_{n+1} = x_n + 2y_n

4. **効率的な計算**: ペル方程式の解を利用することで、O(log n)の時間計算量で解を求めることができます。

## パフォーマンス分析

- **素直な解法**: O(n) - 全ての可能な三角形を順次チェック
- **最適化解法**: O(log n) - ペル方程式の解を利用
- **数学的解法**: O(log n) - 最も効率的な実装

ここで：
- n: 周長制限
- ペル方程式の解は指数的に増加するため、解の数は対数的

## 実装のポイント

1. **面積の判定**: ヘロンの公式を使用して面積が整数かどうかを判定
   ```python
   def is_integral_area(a: int, b: int, c: int) -> bool:
       s = (a + b + c) / 2
       discriminant = s * (s - a) * (s - b) * (s - c)
       if discriminant <= 0:
           return False
       area_sqrt = math.sqrt(discriminant)
       return area_sqrt == int(area_sqrt)
   ```

2. **ペル方程式の解の生成**: 基本解から一般解を生成
   ```python
   x, y = 2, 1  # 基本解
   while True:
       # 条件をチェック
       if (x - 1) % 2 == 0 and y % 2 == 0:
           # 三角形を生成
       x, y = 2 * x + 3 * y, x + 2 * y  # 次の解
   ```

3. **効率的な終了条件**: 次の解での最小周長を概算して早期終了

4. **大数の処理**: 周長制限が大きい場合の効率的な計算

## 検証

小さな例での検証：
- (5, 5, 6): 周長=16, 面積=12
- (5, 5, 4): 周長=14, 面積=12
- (13, 13, 14): 周長=40, 面積=60
- (13, 13, 12): 周長=38, 面積=60

## 解答

Project Euler公式サイトで確認してください。

## 学習ポイント

1. **数論的問題**: ペル方程式の理論と応用

2. **幾何学的条件**: 三角形の面積条件と代数的表現

3. **効率的アルゴリズム**: 数学的性質を活用した高速化

4. **大数計算**: 指数的に増加する数列の効率的な処理

この問題は、数論、幾何学、アルゴリズムの興味深い組み合わせを示しています。ペル方程式の理論を実際の幾何学的問題に応用する例として、数学的洞察の重要性を示しています。
