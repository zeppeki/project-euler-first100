# Problem 045: Triangular, pentagonal, and hexagonal

## 問題

三角数、五角数、六角数は以下の公式で生成される：

三角数: $T_n = \frac{n(n+1)}{2}$ → 1, 3, 6, 10, 15, ...
五角数: $P_n = \frac{n(3n-1)}{2}$ → 1, 5, 12, 22, 35, ...
六角数: $H_n = n(2n-1)$ → 1, 6, 15, 28, 45, ...

$T_{285} = P_{165} = H_{143} = 40755$ であることが分かっている。

三角数でもあり五角数でもあり六角数でもある次の数を求めよ。

## 解答

Project Euler公式サイトで確認してください。

## 解法

この問題は3つの数列すべてに含まれる数を見つける問題である。40755より大きい数の中で、3つの条件を同時に満たす最小の数を探す。

### 1. 素直な解法 (Triangle-based)

**アルゴリズム：**
1. 三角数を順次生成（T286から開始）
2. 各三角数が五角数かつ六角数かチェック
3. 条件を満たす最初の数を返す

**時間計算量：** O(n) - 三角数の線形探索
**空間計算量：** O(1)

```python
def solve_naive() -> int:
    n = 286  # T285 = 40755 の次から開始

    while True:
        triangle_num = generate_triangle(n)

        # 三角数が五角数かつ六角数かチェック
        if is_pentagonal(triangle_num) and is_hexagonal(triangle_num):
            return triangle_num

        n += 1
```

**特徴：**
- 実装が直感的
- すべての三角数を順次チェック
- 最初に見つかる解を返す

### 2. 最適化解法 (Hexagonal-based)

**アルゴリズム：**
1. 六角数を順次生成（H144から開始）
2. 各六角数が三角数かつ五角数かチェック
3. 六角数は三角数より少ないので効率的

**時間計算量：** O(m) where m < n (六角数の方が少ない)
**空間計算量：** O(1)

```python
def solve_optimized() -> int:
    n = 144  # H143 = 40755 の次から開始

    while True:
        hexagonal_num = generate_hexagonal(n)

        # 六角数が三角数かつ五角数かチェック
        if is_triangle(hexagonal_num) and is_pentagonal(hexagonal_num):
            return hexagonal_num

        n += 1
```

**特徴：**
- 六角数は三角数より生成頻度が低い
- 探索回数の削減により高速化
- 同じ結果をより効率的に取得

### 3. 数学的解法 (Mathematical properties)

**アルゴリズム：**
すべての六角数は三角数であるという数学的性質を利用

**時間計算量：** O(m) - 六角数のみをチェック
**空間計算量：** O(1)

```python
def solve_mathematical() -> int:
    # 数学的事実: すべての六角数は三角数
    # H_n = n(2n-1) において、H_n = T_{2n-1}

    n = 144  # H143 = 40755 の次から開始

    while True:
        hexagonal_num = generate_hexagonal(n)

        # 六角数は必ず三角数なので、五角数かどうかのみチェック
        if is_pentagonal(hexagonal_num):
            return hexagonal_num

        n += 1
```

## 数学的背景

### 数列の生成公式

各数列の生成公式とその性質：

1. **三角数**: $T_n = \frac{n(n+1)}{2}$
   - 逆公式: $n = \frac{-1 + \sqrt{1 + 8T}}{2}$

2. **五角数**: $P_n = \frac{n(3n-1)}{2}$
   - 逆公式: $n = \frac{1 + \sqrt{1 + 24P}}{6}$

3. **六角数**: $H_n = n(2n-1)$
   - 逆公式: $n = \frac{1 + \sqrt{1 + 8H}}{4}$

### 重要な数学的性質

**定理**: すべての六角数は三角数である

**証明**:
$H_n = n(2n-1) = 2n^2 - n$

$T_k = \frac{k(k+1)}{2}$ において $k = 2n-1$ とすると：

$T_{2n-1} = \frac{(2n-1)(2n)}{2} = \frac{2n(2n-1)}{2} = n(2n-1) = H_n$

したがって、$H_n = T_{2n-1}$ が成り立つ。

### 数の判定アルゴリズム

各数列に属するかの判定は逆公式を使用：

```python
def is_triangle(num: int) -> bool:
    discriminant = 1 + 8 * num
    sqrt_discriminant = int(math.sqrt(discriminant))

    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return False

    if (sqrt_discriminant - 1) % 2 != 0:
        return False

    n = (sqrt_discriminant - 1) // 2
    return n > 0 and generate_triangle(n) == num
```

## 検証

**既知の例の確認:**
- $T_{285} = \frac{285 \times 286}{2} = 40755$ ✓
- $P_{165} = \frac{165 \times (3 \times 165 - 1)}{2} = \frac{165 \times 494}{2} = 40755$ ✓
- $H_{143} = 143 \times (2 \times 143 - 1) = 143 \times 285 = 40755$ ✓

**解答の検証:**
- **入力:** 40755より大きい数の中で3つの条件を満たす数
- **解答:** [隠匿]
- **検証:** 三角数・五角数・六角数すべての条件を満たす ✓

## 学習ポイント

1. **数学的性質の活用**: 六角数が必ず三角数であることを利用した最適化
2. **逆公式の応用**: 平方根を使った効率的な数列判定
3. **探索戦略**: より少ない要素の数列から探索することで効率化
4. **数値計算**: 大きな数での平方根計算の正確性
5. **アルゴリズム比較**: 異なるアプローチの性能と正確性の検証

## 実装のポイント

1. **効率的判定**: 逆公式を使った O(1) 時間での数列判定
2. **数学的最適化**: 六角数⊆三角数の関係を利用した計算削減
3. **探索順序**: 最も少ない六角数から探索開始
4. **数値精度**: 大きな数での整数演算の正確性確保

この問題は数列の性質と効率的なアルゴリズム設計の良い例を提供している。特に、数学的性質を利用した最適化により、計算量を大幅に削減できることが重要である。
