# Problem 047: Distinct primes factors

## 問題
4つの異なる素因数を持つ連続する4つの整数を見つけよ。その最初の数を求めよ。

## 詳細
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these four numbers?

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Brute Force)
```python
def solve_naive(target_factors):
    n = 2

    while True:
        # 連続するtarget_factors個の数をチェック
        consecutive_found = True
        for i in range(target_factors):
            if count_distinct_prime_factors(n + i) != target_factors:
                consecutive_found = False
                break

        if consecutive_found:
            return n

        n += 1
```

**特徴:**
- 2から始めて連続する数の素因数の個数をチェック
- 条件を満たすまで線形探索
- 各数について素因数分解を実行

**時間計算量:** O(n√n) - nは解までの数、各数の素因数分解にO(√n)
**空間計算量:** O(1)

### 2. 最適化解法 (Efficient Search with Caching)
```python
@lru_cache(maxsize=10000)
def count_distinct_prime_factors_cached(n):
    return count_distinct_prime_factors(n)

def solve_optimized(target_factors):
    n = 2

    while True:
        consecutive_found = True
        for i in range(target_factors):
            if count_distinct_prime_factors_cached(n + i) != target_factors:
                consecutive_found = False
                # 次の候補位置まで飛ばす
                n += i + 1
                break

        if consecutive_found:
            return n

        if not consecutive_found and i == 0:
            n += 1
```

**特徴:**
- LRUキャッシュで素因数計算結果を保存
- 失敗時に効率的にスキップ
- 重複計算を回避

**時間計算量:** O(n√n) - キャッシュヒットにより実際は改善
**空間計算量:** O(キャッシュサイズ)

### 3. 数学的解法 (Smart Skipping)
```python
def solve_mathematical(target_factors):
    n = 2

    while True:
        # 最初の数をチェック
        if count_distinct_prime_factors(n) != target_factors:
            n += 1
            continue

        # 連続する残りの数をチェック
        all_match = True
        for i in range(1, target_factors):
            if count_distinct_prime_factors(n + i) != target_factors:
                all_match = False
                # より効率的にスキップ: 失敗した位置まで進む
                n += i
                break

        if all_match:
            return n

        n += 1
```

**特徴:**
- 最初の数をまずチェックして早期除外
- 失敗した位置まで効率的にスキップ
- 無駄な計算を最小化

**時間計算量:** O(n√n)
**空間計算量:** O(1)

## 数学的背景

### 素因数分解
```python
def get_prime_factors(n):
    factors = set()
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1

    if n > 1:
        factors.add(n)

    return factors
```

**特徴:**
- √nまでの試し割りで効率的な素因数分解
- 重複する素因数は除外（distinctのみ）
- 残った数は素数として処理

### 異なる素因数の計算
数nの異なる素因数の個数ω(n)：
- **ω(p) = 1** (pが素数)
- **ω(p^k) = 1** (素数の冪)
- **ω(ab) = ω(a) + ω(b)** (gcd(a,b) = 1の場合)

### 連続数の性質
連続する整数の素因数分解には興味深い性質がある：
- **2の冪の分布**: 偶数と奇数の交互パターン
- **3の倍数**: 3つごとに出現
- **素数の分布**: 素数定理による密度

## 具体例

### 2つの異なる素因数を持つ連続数
- **14 = 2 × 7** (2つの異なる素因数)
- **15 = 3 × 5** (2つの異なる素因数)

最初の連続ペア: 14, 15

### 3つの異なる素因数を持つ連続数
- **644 = 2² × 7 × 23** (3つの異なる素因数: 2, 7, 23)
- **645 = 3 × 5 × 43** (3つの異なる素因数: 3, 5, 43)
- **646 = 2 × 17 × 19** (3つの異なる素因数: 2, 17, 19)

最初の連続トリプル: 644, 645, 646

### 4つの異なる素因数を持つ連続数
4つの連続する整数で、各数が4つの異なる素因数を持つ最初の組み合わせ：
- **[隠匿] = [隠匿]** (4つの異なる素因数)
- **[隠匿] = [隠匿]** (4つの異なる素因数)
- **[隠匿] = [隠匿]** (4つの異なる素因数)
- **[隠匿] = [隠匿]** (4つの異なる素因数)

## パフォーマンス比較

| 解法 | 時間計算量 | 空間計算量 | 特徴 |
|------|-----------|-----------|------|
| 素直な解法 | O(n√n) | O(1) | シンプル、理解しやすい |
| 最適化解法 | O(n√n) | O(キャッシュ) | キャッシュによる高速化 |
| 数学的解法 | O(n√n) | O(1) | 効率的なスキップ戦略 |

### 実行時間の傾向
- **target_factors = 2**: 全ての解法が高速
- **target_factors = 3**: 最適化の効果が現れる
- **target_factors = 4**: キャッシュとスキップの重要性が顕著

## 学習ポイント

1. **素因数分解の効率化**: √nまでの試し割りによる効率的な実装
2. **重複計算の回避**: LRUキャッシュによる計算結果の再利用
3. **探索の最適化**: 失敗時の効率的なスキップ戦略
4. **数論の応用**: 異なる素因数を持つ数の分布特性

## 応用と発展

### 関連する数論的問題
- **ω(n)の分布**: 異なる素因数の個数の分布則
- **Ω(n)の性質**: 重複を含む素因数の個数
- **radical**: nの全ての異なる素因数の積
- **smooth numbers**: 小さな素因数のみを持つ数

### 素因数分解の改良
- **Pollard's rho algorithm**: 大きな数の素因数分解
- **試し割りの最適化**: 小さな素数のリストによる効率化
- **並列化**: 複数の数の同時処理

### 実世界での応用
- **暗号学**: RSA暗号における素因数分解の困難性
- **コンピュータ代数**: 多項式の因数分解
- **数値解析**: 最大公約数・最小公倍数の計算

## アルゴリズムの詳細

### 素因数分解の効率性
```python
def count_distinct_prime_factors(n):
    count = 0
    d = 2

    while d * d <= n:
        if n % d == 0:
            count += 1
            while n % d == 0:  # 同じ素因数を全て除去
                n //= d
        d += 1

    if n > 1:  # 残った数は素数
        count += 1

    return count
```

### キャッシュ戦略
- **LRU Cache**: 最近使用した計算結果を保持
- **キャッシュサイズ**: メモリと速度のトレードオフ
- **局所性**: 連続する数の計算での効果

### スキップ戦略
```python
# 失敗した位置まで効率的にスキップ
if not consecutive_found:
    n += i + 1  # i番目で失敗した場合、n+i+1から再開
```

## 数学的考察

### 連続数の素因数分解パターン
- **偶数・奇数の交互**: 連続数の2による分割パターン
- **3の倍数**: 3つごとの周期的パターン
- **素数の間隔**: 素数定理による素数の分布

### 確率論的考察
k個の異なる素因数を持つ数の密度：
- **平均的な異なる素因数の個数**: log log n
- **分布**: 正規分布に近似
- **希少性**: より多くの異なる素因数を持つ連続数列の希少性

## 関連問題
- Project Euler Problem 005: Smallest multiple（最小公倍数）
- Project Euler Problem 012: Highly divisible triangular number（約数の個数）
- Project Euler Problem 070: Totient permutation（オイラーのトーシェント関数）
- Project Euler Problem 087: Prime power triples（素数の冪の和）
