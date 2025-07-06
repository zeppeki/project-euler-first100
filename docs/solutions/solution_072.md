# Problem 072: Counting fractions

## 問題の概要

分数 n/d（nとdは正の整数）を考える。n < d かつ HCF(n,d) = 1 の場合、これを既約真分数と呼ぶ。

d ≤ 8 の既約真分数の集合を昇順に並べると：
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

この集合には21個の要素があることが分かる。

d ≤ 1,000,000 の既約真分数の集合には何個の要素が含まれるか？

## 数学的背景

### 既約真分数の定義

既約真分数 n/d は以下の条件を満たす：
1. n < d（真分数）
2. gcd(n, d) = 1（既約）

### オイラーのトーシェント関数

この問題の核心は**オイラーのトーシェント関数** φ(n) にある。

φ(n) は n 以下の正の整数で、n と互いに素であるものの個数を表す。

重要な性質：
- φ(1) = 1
- p が素数の場合：φ(p) = p - 1
- φ(p^k) = p^(k-1)(p-1)
- φ(mn) = φ(m)φ(n) if gcd(m,n) = 1（乗法的関数）

### 問題との関係

分母が d の既約真分数の個数は正確に φ(d) に等しい。

なぜなら：
- 分子 n は 1 ≤ n < d の範囲
- gcd(n, d) = 1 が必要
- これは d 未満で d と互いに素な正の整数の個数と同じ

したがって、答えは：
**Σφ(d) for d = 2 to 1,000,000**

## 解法の実装

### 解法1: 素直な解法 (Naive)

各 d について個別に φ(d) を計算。

```python
def solve_naive(limit: int) -> int:
    total = 0
    for d in range(2, limit + 1):
        phi_d = euler_totient_individual(d)
        total += phi_d
    return total
```

**時間計算量**: O(n²)
**空間計算量**: O(1)

### 解法2: 最適化解法 (Optimized)

素因数分解を使用した効率的な φ(d) 計算。

```python
def solve_optimized(limit: int) -> int:
    total = 0
    for d in range(2, limit + 1):
        phi_d = euler_totient_prime_factorization(d)
        total += phi_d
    return total
```

**時間計算量**: O(n√n)
**空間計算量**: O(log n)

### 解法3: 数学的解法 (Mathematical)

エラトステネスの篩の変形を使用した一括計算。

```python
def solve_mathematical(limit: int) -> int:
    # φ(i) = i で初期化
    phi = list(range(limit + 1))

    # 篩を使用してφ(i)を計算
    for i in range(2, limit + 1):
        if phi[i] == i:  # iが素数
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    return sum(phi[2:limit + 1])
```

**時間計算量**: O(n log log n)
**空間計算量**: O(n)

### 解法4: 篩最適化解法 (Sieve Optimized)

メモリ効率を考慮した篩計算。

```python
def solve_sieve_optimized(limit: int) -> int:
    phi = list(range(limit + 1))
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, limit + 1):
        if is_prime[i]:
            for j in range(i, limit + 1, i):
                is_prime[j] = False
                phi[j] -= phi[j] // i
            is_prime[i] = True

    return sum(phi[2:limit + 1])
```

**時間計算量**: O(n log log n)
**空間計算量**: O(n)

## 篩アルゴリズムの詳細

### 動作原理

1. **初期化**: φ(i) = i ですべての値を初期化
2. **素数処理**: 各素数 p に対して：
   - p の倍数 k すべてについて φ(k) = φ(k) - φ(k)/p を適用
   - これは φ(k) = φ(k) × (1 - 1/p) の実装

### 数学的根拠

素数 p が n の約数の場合：
φ(n) = n × ∏(1 - 1/p) for all prime factors p

篩では、各素数 p について：
- p の倍数すべてに対して (1 - 1/p) の係数を適用
- 結果的に正しい φ(n) 値を得る

## 実装上の工夫

### オイラーのトーシェント関数の実装

```python
def euler_totient_prime_factorization(n: int) -> int:
    if n <= 1:
        return n

    result = n
    temp = n

    # 2で割り切れる場合
    if temp % 2 == 0:
        result = result * (2 - 1) // 2
        while temp % 2 == 0:
            temp //= 2

    # 3以上の奇数の素因数
    i = 3
    while i * i <= temp:
        if temp % i == 0:
            result = result * (i - 1) // i
            while temp % i == 0:
                temp //= i
        i += 2

    # 残りが素数の場合
    if temp > 1:
        result = result * (temp - 1) // temp

    return result
```

### 分析関数

```python
def analyze_totient_distribution(limit: int) -> dict:
    phi_values = euler_totient_sieve(limit)

    return {
        "total_count": sum(phi_values[2:limit + 1]),
        "max_phi": max(phi_values[2:limit + 1]),
        "min_phi": min(phi_values[2:limit + 1]),
        "average_phi": sum(phi_values[2:limit + 1]) / (limit - 1),
    }
```

## 最適化のポイント

### 1. 計算量の改善

- 個別計算: O(n²) → 篩計算: O(n log log n)
- 100万に対して約1000倍の高速化

### 2. メモリ効率

- 篩では O(n) のメモリを使用
- n = 1,000,000 で約4-8MB

### 3. 実装の工夫

- 整数除算の使用による精度保持
- 素数判定の最適化
- 不要な計算の削減

## 検証とテスト

### 小例での検証

d ≤ 8 の場合：
- 手動計算: 21個の既約真分数
- φ(2) + φ(3) + ... + φ(8) = 1 + 2 + 2 + 4 + 2 + 6 + 4 = 21 ✓

### 数学的性質の確認

- φ(p) = p - 1 for primes
- φ(p^k) = p^(k-1)(p-1) for prime powers
- φ(mn) = φ(m)φ(n) if gcd(m,n) = 1

### パフォーマンステスト

```python
def test_performance():
    limits = [100, 1000, 10000, 100000]
    for limit in limits:
        result = solve_mathematical(limit)
        print(f"d ≤ {limit}: {result:,} fractions")
```

## 学習のポイント

### 1. 数論の応用

- オイラーのトーシェント関数の理解
- 素因数分解の重要性
- 乗法的関数の性質

### 2. アルゴリズムの最適化

- 篩の技法の応用
- 計算量の改善方法
- メモリ効率の考慮

### 3. 実装技術

- 数学的な最適化
- 効率的なデータ構造
- 精度の保持

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力**: d ≤ 1,000,000
- **解答**: [隠匿]
- **検証**: ✓ 数学的解法による計算結果

## 関連問題

- Problem 005: 最小公倍数
- Problem 009: ピタゴラスの三つ組
- Problem 069: トーティエント最大値
- Problem 070: トーティエント順列
- Problem 073: 分数の範囲内カウント

## 参考文献

- 初等数論（オイラーのトーシェント関数）
- アルゴリズム（エラトステネスの篩）
- 計算数学（効率的な素因数分解）
