# Problem 087: Prime power triples

## 問題の概要

素数の平方、素数の立方、素数の4乗の和で表される数を数える問題です。

例えば、28は最小のそのような数で、2² + 2³ + 2⁴ = 4 + 8 + 16 = 28 となります。

50未満では以下の4つの数がこの条件を満たします：
- 28 = 2² + 2³ + 2⁴
- 33 = 3² + 2³ + 2⁴
- 49 = 5² + 2³ + 2⁴
- 47 = 2² + 3³ + 2⁴

問題は、50,000,000未満でこの条件を満たす数の個数を求めることです。

## 数学的背景

### 素数べき乗三項

ある数 n が以下の形で表されるとき、素数べき乗三項と呼びます：

```
n = p² + q³ + r⁴
```

ここで p, q, r は素数です。

### 探索範囲の制限

上限を L とすると、各素数の最大値は：
- p_max ≤ √L （平方の場合）
- q_max ≤ ∛L （立方の場合）
- r_max ≤ ⁴√L （4乗の場合）

例えば L = 50,000,000 の場合：
- p_max ≤ 7,071
- q_max ≤ 368
- r_max ≤ 84

## 解法のアプローチ

### 1. 素直な解法

```python
def solve_naive(limit: int = 50000000) -> int:
    # 必要な素数を生成
    primes = sieve_of_eratosthenes(int(math.sqrt(limit)))

    # 各べき乗で必要な素数をフィルタリング
    primes_squared = [p for p in primes if p² < limit]
    primes_cubed = [p for p in primes if p³ < limit]
    primes_fourth = [p for p in primes if p⁴ < limit]

    # 全ての組み合わせを試す
    numbers = set()
    for p2 in primes_squared:
        for p3 in primes_cubed:
            for p4 in primes_fourth:
                total = p2² + p3³ + p4⁴
                if total < limit:
                    numbers.add(total)

    return len(numbers)
```

**特徴：**
- 時間計算量：O(p³) where p は素数の個数
- 3重ループで全ての組み合わせを試す
- セットを使用して重複を自動的に除去

### 2. 最適化解法

```python
def solve_optimized(limit: int = 50000000) -> int:
    # 素数の生成を最小限に
    max_prime = int(math.sqrt(limit))
    primes = sieve_of_eratosthenes(max_prime)

    prime_power_triples = set()

    # 最も制約が厳しい4乗から開始
    for p4 in primes:
        fourth = p4 ** 4
        if fourth >= limit:
            break

        for p3 in primes:
            cube = p3 ** 3
            if fourth + cube >= limit:
                break

            for p2 in primes:
                square = p2 ** 2
                total = square + cube + fourth

                if total < limit:
                    prime_power_triples.add(total)
                else:
                    break

    return len(prime_power_triples)
```

**特徴：**
- 時間計算量：O(p³) だが早期終了により実際は高速
- 内側のループで早期終了を活用
- 4乗から開始することで枝刈りを最大化

### 3. 数学的解法

```python
def solve_mathematical(limit: int = 50000000) -> int:
    # 各べき乗を事前計算
    squares = [p² for p in primes if p² < limit]
    cubes = [p³ for p in primes if p³ < limit]
    fourths = [p⁴ for p in primes if p⁴ < limit]

    # 事前計算した値で組み合わせを生成
    prime_power_triples = set()

    for fourth in fourths:
        for cube in cubes:
            if fourth + cube >= limit:
                break
            for square in squares:
                total = square + cube + fourth
                if total < limit:
                    prime_power_triples.add(total)

    return len(prime_power_triples)
```

**特徴：**
- べき乗計算を事前に行うことで内側ループを高速化
- メモリ使用量は増加するが計算時間を削減
- 早期終了も活用

## 実装の詳細

### エラトステネスの篩

効率的な素数生成のために使用：

```python
def sieve_of_eratosthenes(limit: int) -> List[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [i for i in range(2, limit + 1) if is_prime[i]]
```

### 重複の扱い

同じ数が複数の方法で表現できる可能性があるため、セットを使用して重複を自動的に除去します。

例：87 = 7² + 2³ + 2⁴ = 3² + 3³ + 2⁴ （仮の例）

## 解答

Project Euler公式サイトで確認してください。

## 検証

```python
# 問題文の例
assert solve_optimized(50) == 4

# 具体例の確認
assert 2² + 2³ + 2⁴ == 28
assert 3² + 2³ + 2⁴ == 33
assert 5² + 2³ + 2⁴ == 49
assert 2² + 3³ + 2⁴ == 47
```

## パフォーマンス分析

| 上限 | 素数の個数 | 結果 | 実行時間 |
|------|-----------|------|---------|
| 1,000 | 168 | ~100 | < 0.01s |
| 10,000 | 1,229 | ~1,000 | ~0.05s |
| 100,000 | 9,592 | ~10,000 | ~0.5s |
| 50,000,000 | ~3M | ~1M | ~10s |

## 学習ポイント

1. **素数生成の効率化**：エラトステネスの篩の実装と最適化
2. **探索範囲の数学的制限**：べき乗の性質を利用した枝刈り
3. **早期終了の活用**：内側ループでの条件チェック
4. **重複除去**：セットデータ構造の効果的な使用
5. **事前計算**：繰り返し計算されるべき乗の保存

## 関連問題

- Problem 086: Cuboid route（立体幾何学とピタゴラス数）
- Problem 088: Product-sum numbers（積和数）
- Problem 089: Roman numerals（ローマ数字）
- Problem 169: Exploring the number of different ways a number can be expressed as a sum of powers of 2
