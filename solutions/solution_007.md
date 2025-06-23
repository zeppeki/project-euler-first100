# Problem 007: 10001st prime

## 問題
10001番目の素数を求めよ。

## 詳細
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime?

## 解答: 104743

## 解法

### 1. 素直な解法 (Naive Approach)
```python
def solve_naive(n):
    if n == 1:
        return 2

    count = 1  # 2を最初の素数として数える
    candidate = 3  # 次の候補は3

    while count < n:
        if is_prime_naive(candidate):
            count += 1
        if count < n:
            candidate += 2  # 奇数のみをチェック

    return candidate

def is_prime_naive(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
```

**特徴:**
- 各数を順次チェックして素数判定を行う直感的なアプローチ
- 2以外の偶数は除外して効率化
- 素数判定は√nまでの奇数で割り切れるかチェック

**時間計算量:** O(n × √m) (mはn番目の素数)
**空間計算量:** O(1)

### 2. 最適化解法 (Sieve of Eratosthenes)
```python
def solve_optimized(n):
    if n == 1:
        return 2

    # n番目の素数の近似上限を計算（素数定理より）
    if n < 6:
        limit = 12
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n))))

    # エラトステネスの篩
    primes = sieve_of_eratosthenes(limit)

    # 必要な数の素数が見つからない場合、範囲を拡張
    while len(primes) < n:
        limit *= 2
        primes = sieve_of_eratosthenes(limit)

    return primes[n - 1]

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [i for i in range(2, limit + 1) if is_prime[i]]
```

**特徴:**
- エラトステネスの篩を使用した効率的な素数生成
- 素数定理を使用した上限推定で必要な範囲を予測
- 一度に大量の素数を生成するため、複数のクエリに効率的

**時間計算量:** O(m × log(log(m))) (mは上限値)
**空間計算量:** O(m)

### 3. 数学的解法 (6k±1 Optimization)
```python
def solve_mathematical(n):
    if n == 1:
        return 2
    if n == 2:
        return 3

    count = 2  # 2と3を既に数えている
    candidate = 5  # 次の候補は5 (6*1-1)
    increment = 2  # 5の次は7 (6*1+1), その次は11 (6*2-1)

    while count < n:
        if is_prime_optimized(candidate):
            count += 1
        if count < n:
            candidate += increment
            increment = 6 - increment  # 2と4を交互に

    return candidate

def is_prime_optimized(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    # 5から始めて6k±1の形の数のみをチェック
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True
```

**特徴:**
- 6k±1の形の数のみをチェックする数学的最適化
- 3以上の全ての素数は6k±1の形であることを利用
- 候補数を1/3に削減して効率化

**時間計算量:** O(n × √m / 3) (mはn番目の素数)
**空間計算量:** O(1)

## 数学的背景

### 素数の分布
- **素数定理**: n番目の素数は約 n × ln(n) の値
- **6k±1の性質**: 2と3以外の全ての素数は6k±1の形

### 素数判定の最適化
1. **偶数の除外**: 2以外の偶数は全て合成数
2. **√n まで**: 合成数nの最小の約数は√n以下
3. **6k±1パターン**: 2,3で割り切れない数は6k±1の形

### エラトステネスの篩
- 古代ギリシャの数学者エラトステネスが考案
- 2から順番にその倍数を篩い落とす
- 時間計算量: O(n log log n)

## 具体例

### 最初の10個の素数
2, 3, 5, 7, 11, 13, 17, 19, 23, 29

### 6k±1パターンの検証
- 5 = 6×1-1
- 7 = 6×1+1
- 11 = 6×2-1
- 13 = 6×2+1
- 17 = 6×3-1
- 19 = 6×3+1
- 23 = 6×4-1

### 実際の問題 (n=10001)
- **10001番目の素数**: 104743
- **素数定理による推定**: 10001 × ln(10001) ≈ 92,103
- **実際の値との差**: 104743 - 92103 = 12,640

## パフォーマンス比較

| 解法 | 時間計算量 | 空間計算量 | 特徴 |
|------|-----------|-----------|------|
| 素直な解法 | O(n×√m) | O(1) | 理解しやすい、メモリ効率的 |
| 最適化解法 | O(m×log(log(m))) | O(m) | 大量の素数生成に適している |
| 数学的解法 | O(n×√m/3) | O(1) | 候補数削減、バランスが良い |

### 実行時間の傾向
- **小さなn**: 数学的解法が最高速
- **大きなn**: エラトステネスの篩が効率的
- **メモリ制約**: 素直な解法が適している

## 学習ポイント

1. **素数の性質**: 6k±1の形や素数定理など、素数の数学的性質を活用
2. **アルゴリズムの選択**: 問題の規模と制約に応じた最適なアルゴリズムの選択
3. **前処理と計算量**: エラトステネスの篩のように前処理で効率化する手法
4. **数学的最適化**: 理論的な性質を活用した候補数の削減

## 応用と発展

### 関連する素数問題
- **双子素数**: pとp+2が共に素数 (例: 3,5 や 5,7)
- **素数ギャップ**: 連続する素数間の差
- **メルセンヌ素数**: 2^p - 1の形の素数

### 暗号学への応用
- **RSA暗号**: 大きな素数の積の因数分解の困難性を利用
- **楕円曲線暗号**: 素数を法とする楕円曲線上の演算
- **素数判定**: 確率的素数判定アルゴリズム

### 計算数学
- **分散コンピューティング**: 大きな素数の探索
- **GIMPS**: Great Internet Mersenne Prime Search
- **素数証明**: 決定論的素数判定アルゴリズム

## 関連問題
- Project Euler Problem 003: 最大の素因数
- Project Euler Problem 010: 200万以下の素数の和
- Project Euler Problem 027: 連続する素数を生成する二次式
- Project Euler Problem 035: 循環素数
