# Problem 027: Quadratic primes

## 問題

オイラーは驚くべき二次式を発見した:

n² + n + 41

この式は、0 ≤ n ≤ 39 の連続する整数値に対して40個の素数を生成することが判明した。しかし、n = 40 のとき、40² + 40 + 41 = 40(40 + 1) + 41 は41で割り切れ、n = 41 のとき、41² + 41 + 41 は明らかに41で割り切れる。

80個の素数を連続値 0 ≤ n ≤ 79 に対して生成する驚異的な式 n² - 79n + 1601 が発見された。係数-79と1601の積は-126479である。

以下の形の二次式を考える:
n² + an + b, ここで |a| < 1000 かつ |b| ≤ 1000

(ここで |n| は n の絶対値)
例: |11| = 11 かつ |-4| = 4

n = 0 から始めて連続する値の n に対して最大数の素数を生成する二次式の係数 a と b の積を求めよ。

## 解答

Project Euler公式サイトで確認してください。

## 解法

この問題は、二次式 n² + an + b で連続する素数を最大数生成する係数を見つける問題です。2つのアプローチで解法を実装しました。

### 1. 素直な解法 (`solve_naive`)

制約を絞り込んだ全探索による方法です。

- **時間計算量**: `O(p × limit × k)` (pは素数の個数、kは平均的な連続素数数)
- **空間計算量**: `O(1)`

#### アルゴリズムの考察

二次式 n² + an + b で連続する素数を生成するための制約を分析します：

1. **n = 0の制約**: n² + an + b = b なので、bは素数である必要があります
2. **n = 1の制約**: 1 + a + b が素数である必要があります
3. **bの範囲**: b ≤ 1000 かつ b は正の素数

```python
def solve_naive(limit: int = 1000) -> int:
    """
    素直な解法: 制約を絞り込んだ全探索
    """
    max_primes = 0
    result_product = 0

    # b は n=0 で素数になる必要があるため、正の素数である必要がある
    b_candidates = [i for i in range(2, limit + 1) if is_prime(i)]

    for b in b_candidates:
        for a in range(-limit + 1, limit):
            # n=1の場合: 1 + a + b が正の数になる必要がある
            if 1 + a + b <= 1:
                continue

            primes_count = count_consecutive_primes(a, b)

            if primes_count > max_primes:
                max_primes = primes_count
                result_product = a * b

    return result_product
```

### 2. 最適化解法 (`solve_optimized`)

エラトステネスの篩を使って素数を事前計算し、素数判定を高速化する方法です。

- **時間計算量**: `O(n log log n + p × limit × k)`
- **空間計算量**: `O(n)`

#### 最適化のポイント

1. **素数の事前計算**: エラトステネスの篩で素数セットを生成
2. **高速素数判定**: 事前計算された素数セットでO(1)判定
3. **適切な範囲設定**: 実用的な範囲（10000）に制限

```python
def solve_optimized(limit: int = 1000) -> int:
    """
    最適化解法: 素数を事前計算し、条件を絞り込む
    """
    # 十分大きな範囲で素数を事前計算
    max_possible_value = 10000  # 実用的な範囲に制限
    prime_set = sieve_of_eratosthenes(max_possible_value)

    max_primes = 0
    result_product = 0

    # b は n=0 で素数になる必要があるため、正の素数である必要がある
    primes_up_to_limit = [p for p in prime_set if p <= limit]

    for b in primes_up_to_limit:
        for a in range(-limit + 1, limit):
            # n=1 の場合: 1 + a + b が正の数になる必要がある
            if 1 + a + b <= 1:
                continue

            primes_count = count_consecutive_primes(a, b, prime_set, max_possible_value)

            if primes_count > max_primes:
                max_primes = primes_count
                result_product = a * b

    return result_product
```

## 重要な数学的性質

### 1. 制約条件の導出

**n = 0の制約**:
- n² + an + b = b
- 連続する素数を生成するには b が素数である必要
- よって b ≥ 2

**n = 1の制約**:
- n² + an + b = 1 + a + b
- これも素数である必要
- b ≥ 2 なので 1 + a + b ≥ 3 + a

### 2. オイラーの式の特殊性

オイラーの有名な式 n² + n + 41 (a = 1, b = 41):
- n = 0 から 39 まで40個の連続する素数を生成
- b = 41 は素数で、比較的大きな値
- a = 1 は小さな正の値

### 3. 探索空間の最適化

1. **bの候補絞り込み**: b は 1000 以下の素数のみ
2. **aの範囲制限**: |a| < 1000
3. **早期終了**: 1 + a + b ≤ 1 の場合はスキップ

## パフォーマンス比較

| 解法 | 実行時間（参考） |
| :--- | :--- |
| 素直な解法 (limit=100) | ~0.005秒 |
| 最適化解法 (limit=1000) | ~0.085秒 |

最適化解法は素数の事前計算により、大きな範囲でも効率的に動作します。

## 学習ポイント

- **数論的制約**: 問題の性質から導出される制約条件の活用
- **エラトステネスの篩**: 大量の素数判定が必要な場合の最適化手法
- **探索空間の絞り込み**: 数学的性質を利用した効率的な探索
- **二次式の性質**: 係数が素数生成に与える影響の理解
- **オイラーの発見**: 歴史的に重要な数学的発見の背景
- **最適化のトレードオフ**: メモリ使用量と計算速度のバランス
