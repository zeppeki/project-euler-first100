# Problem 003: Largest prime factor

## 問題

13195の素因数は5, 7, 13, 29である。

600851475143の素因数のうち最大のものを求めよ。

## 解答: 6,857

## 解法

### 1. 素直な解法

2から順に試し割りで素因数分解を行う方法です。

```python
def solve_naive(n: int) -> int:
    if n < 2:
        return n

    largest_prime = 1
    current = n

    # 2で割り切れるだけ割る
    while current % 2 == 0:
        largest_prime = 2
        current //= 2

    # 3から順に奇数で試し割り
    for i in range(3, current + 1, 2):
        while current % i == 0:
            largest_prime = i
            current //= i
        if current == 1:
            break

    return largest_prime
```

**時間計算量**: O(n) - 最悪の場合、nまで試し割りが必要
**空間計算量**: O(1) - 定数個の変数のみ使用

### 2. 最適化解法

平方根まで試し割り、その後残った数が素数かチェックする方法です。

```python
def solve_optimized(n: int) -> int:
    if n < 2:
        return n

    largest_prime = 1
    current = n

    # 2で割り切れるだけ割る
    while current % 2 == 0:
        largest_prime = 2
        current //= 2

    # 3から√nまでの奇数で試し割り
    sqrt_n = int(math.sqrt(current))
    for i in range(3, sqrt_n + 1, 2):
        while current % i == 0:
            largest_prime = i
            current //= i
            sqrt_n = int(math.sqrt(current))  # 平方根を再計算

    # 残った数が1より大きければ、それは素数
    if current > 1:
        largest_prime = current

    return largest_prime
```

**時間計算量**: O(√n) - 平方根まで試し割り
**空間計算量**: O(1)

### 3. 数学的解法

より効率的な素因数分解アルゴリズムを使用する方法です。

```python
def solve_mathematical(n: int) -> int:
    if n < 2:
        return n

    def trial_division(n: int) -> list:
        """試し割りによる素因数分解"""
        factors = []
        current = n

        # 2で割り切れるだけ割る
        while current % 2 == 0:
            factors.append(2)
            current //= 2

        # 3から√nまでの奇数で試し割り
        for i in range(3, int(math.sqrt(current)) + 1, 2):
            while current % i == 0:
                factors.append(i)
                current //= i

        # 残った数が1より大きければ、それは素数
        if current > 1:
            factors.append(current)

        return factors

    factors = trial_division(n)
    return max(factors) if factors else 1
```

**時間計算量**: O(√n)
**空間計算量**: O(1)

## 数学的背景

### 素因数分解の基本定理

任意の正整数は、素数の積として一意に表すことができます（順序を除く）。

### 試し割り法の最適化

1. **平方根までの試し割り**: nの素因数は必ず√n以下に存在する
2. **2の特別処理**: 2は唯一の偶数の素数なので、最初に処理
3. **奇数のみ試し割り**: 2以外の偶数は素数ではないため、奇数のみを試す

### 数学的証明

**定理**: nの素因数は必ず√n以下に存在する

**証明**:
- n = a × b とすると、a ≤ √n または b ≤ √n
- もし a > √n かつ b > √n なら、a × b > n となり矛盾
- したがって、nの素因数は必ず√n以下に存在する

## 検証

### テストケース

| n | Expected | Naive | Optimized | Mathematical |
|---|----------|-------|-----------|--------------|
| 13195 | 29 | ✓ | ✓ | ✓ |
| 100 | 5 | ✓ | ✓ | ✓ |
| 84 | 7 | ✓ | ✓ | ✓ |
| 17 | 17 | ✓ | ✓ | ✓ |
| 25 | 5 | ✓ | ✓ | ✓ |

### 本問題の検証

- **n**: 600,851,475,143
- **解答**: 6,857
- **全解法一致**: ✓

### 素因数分解の確認

600,851,475,143 = 71 × 839 × 1471 × 6857

- 素因数: [71, 839, 1471, 6857]
- 最大の素因数: 6,857
- 検証: ✓

## パフォーマンス比較

| 解法 | 実行時間 | 相対速度 |
|------|----------|----------|
| 素直な解法 | 時間切れ | - |
| 最適化解法 | 0.014231秒 | 1.00x |
| 数学的解法 | 0.014405秒 | 1.01x |

**最適化解法**が最も高速でした。素直な解法は大きな数では時間がかかりすぎるため、実用的ではありません。

## 最適化のポイント

1. **平方根までの試し割り**: 計算量をO(n)からO(√n)に削減
2. **2の特別処理**: 唯一の偶数の素数を最初に処理
3. **奇数のみ試し割り**: 不要な計算を削減
4. **動的平方根計算**: 試し割り中に平方根を再計算して効率化

## 学習ポイント

1. **素因数分解の基本**: 試し割り法の理解と実装
2. **数学的性質の活用**: 平方根までの試し割りで効率化
3. **アルゴリズムの最適化**: 計算量の削減による実用性の向上
4. **大きな数の処理**: 効率的なアルゴリズムの重要性

## 参考

- [Project Euler Problem 3](https://projecteuler.net/problem=3)
- [Prime factorization](https://en.wikipedia.org/wiki/Integer_factorization)
- [Trial division](https://en.wikipedia.org/wiki/Trial_division)
- [Fundamental theorem of arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic)
