# Problem 070: Totient permutation

## 問題文

オイラーのトーシェント関数φ(n)（時にはファイ関数と呼ばれる）は、n以下の正整数でnと互いに素な数の個数を求めるために使われます。たとえば、1, 2, 4, 5, 7, 8はすべて9未満でかつ9と互いに素なので、φ(9) = 6です。

数字1は全ての正数と互いに素と見なされるため、φ(1) = 1です。

興味深いことに、φ(87109) = 79180で、87109は79180の順列であることが分かります。

1 < n < 10^7の範囲で、φ(n)がnの順列となり、かつn/φ(n)が最小となるnの値を求めてください。

## 解法アプローチ

### アプローチ1: 素直な解法

**戦略:**
全ての数値について順次φ(n)を計算し、順列条件を満たす最小比率を探索します。

**アルゴリズム:**
1. n = 2から上限まで順次処理
2. 各nについてφ(n)を素因数分解で計算
3. φ(n)とnが同じ桁の並び替えかチェック
4. 順列条件を満たす場合、n/φ(n)を計算
5. 最小比率を更新

**計算量:**
- 時間計算量: O(n√n)
- 空間計算量: O(log n)

**実装のポイント:**
```python
def solve_naive(limit: int) -> int:
    min_ratio = float("inf")
    min_n = 0

    for n in range(2, limit):
        phi_n = euler_totient(n)
        if is_permutation(n, phi_n):
            ratio = n / phi_n
            if ratio < min_ratio:
                min_ratio = ratio
                min_n = n

    return min_n
```

### アプローチ2: 最適化解法

**戦略:**
数学的性質を利用して探索空間を大幅に削減します。n/φ(n)が小さくなるのは、nが2つの近い素数の積である場合です。

**数学的洞察:**
- n = p × q（p, qは異なる素数）の場合、φ(n) = (p-1)(q-1)
- n/φ(n) = (p×q)/((p-1)(q-1))
- p ≈ q ≈ √nの時、この比率が最小になる

**アルゴリズム:**
1. √limit付近の素数を生成
2. 素数ペア(p, q)の組み合わせを調べる
3. n = p × q < limitの条件で探索
4. φ(n) = (p-1)(q-1)を直接計算
5. 順列条件と最小比率を確認

**計算量:**
- 時間計算量: O(π(√limit)²)
- 空間計算量: O(π(limit))

**実装のポイント:**
```python
def solve_optimized(limit: int) -> int:
    sqrt_limit = int(limit**0.5) + 1000
    primes = sieve_of_eratosthenes(sqrt_limit)

    min_ratio = float("inf")
    min_n = 0

    for i, p in enumerate(primes):
        for j in range(i, len(primes)):
            q = primes[j]
            n = p * q
            if n >= limit:
                break

            phi_n = (p - 1) * (q - 1)
            if is_permutation(n, phi_n):
                ratio = n / phi_n
                if ratio < min_ratio:
                    min_ratio = ratio
                    min_n = n

    return min_n
```

### アプローチ3: 数学的解法

**戦略:**
√limit付近の素数に焦点を絞ることで、さらに効率的な探索を実現します。

**数学的根拠:**
- n/φ(n)を最小化するには、pとqができるだけ近い値である必要
- √10^7 ≈ 3162付近の素数に探索を集中
- より狭い範囲での集中探索により効率化

**アルゴリズム:**
1. √limit ± 1000の範囲で素数を生成
2. この範囲内の素数ペアのみを調べる
3. 近い素数ペアを優先的に探索
4. 順列条件を満たす最小比率を求める

**計算量:**
- 時間計算量: O(π(√limit)²)
- 空間計算量: O(π(√limit))

**実装のポイント:**
```python
def solve_mathematical(limit: int) -> int:
    sqrt_limit = int(limit**0.5)
    start_range = max(2, sqrt_limit - 1000)
    end_range = min(sqrt_limit + 1000, limit)

    primes = sieve_of_eratosthenes(end_range)
    relevant_primes = [p for p in primes if start_range <= p <= end_range]

    # 近い素数ペアを優先的に探索
    for i, p in enumerate(relevant_primes):
        for j in range(i, len(relevant_primes)):
            q = relevant_primes[j]
            n = p * q
            if n >= limit:
                break

            phi_n = (p - 1) * (q - 1)
            if is_permutation(n, phi_n):
                ratio = n / phi_n
                if ratio < min_ratio:
                    min_ratio = ratio
                    min_n = n

    return min_n
```

## 核心アルゴリズム

### オイラーのトーシェント関数

```python
def euler_totient(n: int) -> int:
    """
    オイラーのトーシェント関数 φ(n) を計算
    φ(n) = n × ∏(1 - 1/p) for all prime factors p
    """
    result = n
    prime_factors = get_prime_factors(n)

    for p in prime_factors:
        result = result * (p - 1) // p

    return result
```

### 順列判定

```python
def is_permutation(a: int, b: int) -> bool:
    """2つの数値が同じ桁の並び替えかどうかを判定"""
    return sorted(str(a)) == sorted(str(b))
```

## 数学的分析

### トーシェント関数の性質

1. **素数に対して**: φ(p) = p - 1
2. **素数の冪に対して**: φ(p^k) = p^k - p^(k-1) = p^(k-1)(p-1)
3. **互いに素な数に対して**: φ(mn) = φ(m)φ(n)
4. **一般的な公式**: φ(n) = n × ∏(1 - 1/p) for all prime factors p

### 最適化の根拠

n/φ(n)の最小化について：

- n = p × q（異なる素数）の場合：
  - φ(n) = (p-1)(q-1)
  - n/φ(n) = (p×q)/((p-1)(q-1))

- p ≈ q ≈ √nの場合：
  - n/φ(n) ≈ n/((√n-1)²) ≈ n/(n-2√n+1)
  - この値はp, qが近いほど小さくなる

### 探索範囲の決定

10^7の場合：
- √10^7 ≈ 3162
- この付近の素数ペアが最適解候補
- 実際の探索範囲: 2162 ≤ p, q ≤ 4162

## 実装の詳細

### 効率化のポイント

1. **素数生成の最適化**
   - エラトステネスの篩を使用
   - 必要範囲のみ生成

2. **順列判定の効率化**
   - 文字列ソートによる比較
   - 時間計算量: O(k log k) where k = 桁数

3. **探索順序の最適化**
   - 近い素数ペアから優先的に探索
   - 早期終了条件の活用

### エラーハンドリング

```python
def find_totient_permutations(limit: int) -> list[tuple[int, int, float]]:
    """指定範囲内でトーシェント順列を探索"""
    results = []

    # 素数生成での例外処理
    try:
        primes = sieve_of_eratosthenes(int(limit**0.5) + 1000)
    except MemoryError:
        # メモリ不足時の代替処理
        primes = sieve_of_eratosthenes(int(limit**0.5))

    # 探索処理...
    return results
```

## 性能分析

### 時間計算量比較

| アプローチ | 時間計算量 | 実際の計算量（10^7） |
|-----------|------------|---------------------|
| 素直な解法 | O(n√n) | ~10^10.5 |
| 最適化解法 | O(π(√n)²) | ~10^6 |
| 数学的解法 | O(π(√n)²) | ~10^5 |

### メモリ使用量

- 素数配列: O(π(√n)) ≈ O(√n / log √n)
- 10^7の場合: 約440個の素数（3162付近）

## 検証

### テストケース

```python
# 基本的な検証
assert euler_totient(9) == 6
assert is_permutation(87109, 79180)  # 問題文の例

# 素数ペアの検証
assert euler_totient(3 * 5) == (3-1) * (5-1)  # 8
assert euler_totient(7 * 11) == (7-1) * (11-1)  # 60
```

### 解答の妥当性

期待される解答の特徴：
- 2つの素数の積
- 両素数が√10^7 ≈ 3162付近
- φ(n)とnが同じ桁の並び替え
- n/φ(n)が最小値

## 解答

Project Euler公式サイトで確認してください。

## 検証
- **入力:** 10000000 (10^7)
- **解答:** [隠匿]
- **検証:** ✓

## 学習ポイント

1. **数論的関数の応用**
   - オイラーのトーシェント関数の性質
   - 素数を用いた効率的な計算

2. **最適化技法**
   - 数学的性質を活用した探索空間削減
   - 素数ペアによる焦点を絞った探索

3. **アルゴリズム設計**
   - 段階的な最適化アプローチ
   - 時間計算量の大幅な改善

4. **実装技法**
   - 効率的な順列判定
   - 素数生成の最適化
   - エラーハンドリングの重要性

この問題は、数学的洞察を活用してアルゴリズムを最適化する優れた例です。素直な解法から始めて、数学的性質を理解し、それを活用して効率的な解法を構築する過程が重要な学習要素となります。
