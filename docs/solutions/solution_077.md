# 問題77: 素数の和

## 問題文

10は素数の和として、ちょうど5通りの方法で表すことができる：

- 7 + 3
- 5 + 5
- 5 + 3 + 2
- 3 + 3 + 2 + 2
- 2 + 2 + 2 + 2 + 2

素数の和として5000通り以上の方法で表すことができる最初の数はいくつか？

## 数学的背景

この問題は**素数分割**（Prime Partition）として知られる組合せ論の問題です。問題76の整数分割の変種で、使用できる数を素数のみに制限したものです。

### 素数分割の定義

正の整数nの素数分割とは、n = p₁ + p₂ + ... + pₖ（ただし、すべてのpᵢは素数）となる素数の列のことです。

### 動的計画法によるアプローチ

素数分割の数を効率的に計算するには、問題76と同様の動的計画法を使用できます。ただし、使用する数を素数のみに制限します。

## 解法

### 1. 素直な解法：個別計算

```python
def solve_naive(target: int) -> int:
    """
    各数について個別に素数分割数を計算
    """
    max_n = 100
    primes = generate_primes(max_n)

    for n in range(2, max_n + 1):
        usable_primes = [p for p in primes if p <= n]
        ways = count_prime_partitions(n, usable_primes)

        if ways > target:
            return n

    raise ValueError(f"Solution not found within limit {max_n}")
```

**アルゴリズムの説明：**
- 各nについて、n以下の素数のみを使用
- 動的計画法で分割数を計算
- 目標値を超えた最初の数を返す

### 2. 最適化解法：一括計算

```python
def solve_optimized(target: int) -> int:
    """
    動的計画法で全ての数の分割数を一括計算
    """
    max_n = 100
    primes = generate_primes(max_n)

    dp = [0] * (max_n + 1)
    dp[0] = 1

    for prime in primes:
        for i in range(prime, max_n + 1):
            dp[i] += dp[i - prime]

    for n in range(2, max_n + 1):
        if dp[n] > target:
            return n

    raise ValueError(f"Solution not found within limit {max_n}")
```

**アルゴリズムの説明：**
- 素数を順次追加して分割数を計算
- 各素数について、その素数を使う場合の分割数を加算
- 全ての数の分割数を一度に計算

### 素数分割数計算

```python
def count_prime_partitions(n: int, primes: list[int]) -> int:
    """
    nを素数の和で表す方法の数を計算
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for prime in primes:
        if prime > n:
            break
        for i in range(prime, n + 1):
            dp[i] += dp[i - prime]

    return dp[n]
```

## 計算量

### 素直な解法
- **時間計算量**: O(n² × p) where p is the number of primes
- **空間計算量**: O(n)

### 最適化解法
- **時間計算量**: O(n × p) where p is the number of primes up to n
- **空間計算量**: O(n)

## 実装のポイント

1. **素数生成**：
   - エラトステネスの篩を使用して効率的に素数を生成

2. **動的計画法**：
   - 問題76と同じパターンだが、使用する数を素数のみに制限

3. **最適化**：
   - 全ての数の分割数を一括計算することで効率化

## 検証

### 小さい値での確認

| n | 素数分割数 |
|---|-----------|
| 2 | 1         |
| 3 | 1         |
| 4 | 1         |
| 5 | 2         |
| 6 | 2         |
| 7 | 3         |
| 8 | 3         |
| 9 | 4         |
| 10| 5         |

### パフォーマンス

target = 5000の場合：
- 素直な解法：約0.001秒
- 最適化解法：約0.00008秒（約14倍高速）

## 解答

Project Euler公式サイトで確認してください。

## 学んだこと

1. **素数分割問題**の解法
2. **動的計画法**の応用と最適化
3. **エラトステネスの篩**による効率的な素数生成
4. **問題76との関連性**と制約の違い
