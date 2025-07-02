# Problem 046: Goldbach's other conjecture

## 問題

クリスチャン・ゴールドバッハによって提唱された予想では、すべての奇数の合成数は、素数と2倍の平方数の和で表すことができるとされています。

- 9 = 7 + 2×1²
- 15 = 7 + 2×2²
- 21 = 3 + 2×3²
- 25 = 7 + 2×3²
- 27 = 19 + 2×2²
- 33 = 31 + 2×1²

しかし、この予想は間違いであることが判明しました。

素数と2倍の平方数の和で表すことのできない最小の奇数の合成数を求めなさい。

## アプローチ

### 1. 素直な解法 (O(n²√n))

各奇数合成数について、すべての素数との組み合わせを試して予想が成り立つかチェックする方法です。

```python
def solve_naive(limit: int = 10000) -> int:
    n = 9  # 最初の奇数合成数
    while n < limit:
        if n % 2 == 1 and not is_prime(n):
            found = False
            for prime in range(2, n):
                if is_prime(prime):
                    remainder = n - prime
                    if remainder > 0 and remainder % 2 == 0:
                        square_part = remainder // 2
                        if is_perfect_square(square_part):
                            found = True
                            break
            if not found:
                return n
        n += 2
    return -1
```

### 2. 最適化解法 (O(n log log n + n²√n))

事前にエラトステネスの篩で素数を生成し、効率的に判定する方法です。

```python
def solve_optimized(limit: int = 10000) -> int:
    primes = generate_primes(limit)
    n = 9
    while n < limit:
        if n % 2 == 1 and not is_prime(n):
            if not can_be_written_as_conjecture(n, primes):
                return n
        n += 2
    return -1
```

### 3. 数学的解法 (O(n log log n + n√n))

素数と平方数のセットを事前計算し、メモ化を活用する方法です。

```python
def solve_mathematical(limit: int = 10000) -> int:
    primes = generate_primes(limit)
    prime_set = set(primes)

    # 平方数のセットを事前計算
    squares = set()
    k = 1
    while 2 * k * k < limit:
        squares.add(2 * k * k)
        k += 1

    n = 9
    while n < limit:
        if n % 2 == 1 and n not in prime_set:
            found = False
            for twice_square in squares:
                if twice_square >= n:
                    break
                if (n - twice_square) in prime_set:
                    found = True
                    break
            if not found:
                return n
        n += 2
    return -1
```

## 重要なアルゴリズム

### エラトステネスの篩

効率的な素数生成アルゴリズムです。

```python
def generate_primes(limit: int) -> list[int]:
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(2, limit + 1) if sieve[i]]
```

### 完全平方数判定

平方根を計算して判定する効率的な方法です。

```python
def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n
```

## 計算量分析

| 手法 | 時間計算量 | 空間計算量 |
|------|------------|------------|
| 素直な解法 | O(n²√n) | O(1) |
| 最適化解法 | O(n log log n + n²√n) | O(n) |
| 数学的解法 | O(n log log n + n√n) | O(n) |

## 学習ポイント

1. **ゴールドバッハ予想の変形**: 有名なゴールドバッハ予想の派生問題です
2. **反例の発見**: 数学的予想が成り立たない例を見つける問題
3. **効率的な素数生成**: エラトステネスの篩の活用
4. **組み合わせ最適化**: セット演算とメモ化による高速化
5. **数学的性質の活用**: 奇数、合成数、完全平方数の性質

## 検証

具体例の確認:
- 9 = 7 + 2×1² ✓
- 15 = 7 + 2×2² ✓
- 21 = 3 + 2×3² ✓
- 25 = 7 + 2×3² ✓
- 27 = 19 + 2×2² ✓
- 33 = 31 + 2×1² ✓

最初の反例は奇数合成数であり、どの素数との組み合わせでも予想の形で表現できません。

## 実装のポイント

1. **効率的な素数判定**: 事前計算とセット化による高速化
2. **平方数の事前計算**: 必要な範囲の2×k²を事前生成
3. **早期終了**: 条件を満たさない場合の即座の判定
4. **メモリ最適化**: 必要最小限のデータ構造の使用

## 解答

Project Euler公式サイトで確認してください。
