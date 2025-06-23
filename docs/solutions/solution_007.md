# Problem 007: 10001st prime

## 問題
最初の6つの素数を列挙すると: 2, 3, 5, 7, 11, 13 であり、6番目の素数は13である。

10001番目の素数を求めよ。

## 詳細
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime?

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)
```python
def solve_naive(n):
    if n <= 0:
        raise ValueError("n must be positive")
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

    return all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2))
```

**特徴:**
- 各数を順次チェックして素数判定を行う直感的なアプローチ
- 2を除いて奇数のみをチェックすることで効率化
- 素数判定では√nまでの奇数で割り切れるかをチェック

**時間計算量:** O(n * √m) where m is the nth prime
**空間計算量:** O(1)

### 2. 最適化解法 (Sieve of Eratosthenes)
```python
def solve_optimized(n):
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 2

    # n番目の素数の近似上限を計算（素数定理より）
    limit = 12 if n < 6 else int(n * (math.log(n) + math.log(math.log(n))))

    # エラトステネスの篩
    primes = sieve_of_eratosthenes(limit)

    # 必要な数の素数が見つからない場合、範囲を拡張
    while len(primes) < n:
        limit *= 2
        primes = sieve_of_eratosthenes(limit)

    return primes[n - 1]

def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [i for i in range(2, limit + 1) if is_prime[i]]
```

**特徴:**
- エラトステネスの篩を使用して効率的に素数を生成
- 素数定理を使って必要な範囲を事前に推定
- 範囲が不足した場合は動的に拡張

**時間計算量:** O(m log log m) where m is the upper bound
**空間計算量:** O(m)

### 3. 数学的解法 (6k±1 Optimization)
```python
def solve_mathematical(n):
    if n <= 0:
        raise ValueError("n must be positive")
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
- 6k±1の形の数のみをチェックして効率化
- 2と3で割り切れない数の中で、6k±1の形以外は必ず合成数
- 素数判定でも6k±1の形の除数のみをチェック

**時間計算量:** O(n * √m / 3) where m is the nth prime
**空間計算量:** O(1)

## 数学的背景

### 素数の性質
1. **基本性質**: 1より大きい自然数で、1と自分以外に正の約数を持たない数
2. **分布**: 2を除いて全て奇数
3. **6k±1の性質**: 3より大きい素数は必ず6k±1の形

### 素数定理
n番目の素数pₙの近似式：
```
pₙ ≈ n ln(n)  (n > 5の場合)
```

より精密な近似：
```
pₙ ≈ n(ln(n) + ln(ln(n)))  (n ≥ 6の場合)
```

### エラトステネスの篩
古代ギリシャの数学者エラトステネスが考案した素数生成アルゴリズム：
1. 2からnまでの数を列挙
2. 2の倍数を篩い落とす
3. 次の素数の倍数を篩い落とす
4. √nまで繰り返す

### 6k±1最適化の原理
2と3で割り切れない数は以下の形：
- 6k+1: 1, 7, 13, 19, 25, 31, ...
- 6k+5 (= 6k-1): 5, 11, 17, 23, 29, ...

これらの形以外（6k, 6k+2, 6k+3, 6k+4）は2または3で割り切れるため合成数。

## パフォーマンス比較

| 解法 | 時間計算量 | 空間計算量 | 特徴 |
|------|-----------|-----------|------|
| 素直な解法 | O(n√m) | O(1) | 理解しやすい、メモリ効率的 |
| 最適化解法 | O(m log log m) | O(m) | 高速、メモリ使用量多 |
| 数学的解法 | O(n√m/3) | O(1) | 定数倍の改善、メモリ効率的 |

大きなnに対しては、エラトステネスの篩が最も高速ですが、メモリ使用量が多くなります。

## 学習ポイント

1. **アルゴリズムの選択**: 問題の制約に応じて最適なアルゴリズムを選択する重要性
2. **数学的最適化**: 数論の知識を活用した定数倍の改善
3. **時空間トレードオフ**: メモリ使用量と実行時間のバランス
4. **篩アルゴリズム**: 古典的だが非常に効率的な素数生成手法
5. **近似理論**: 素数定理による事前推定の活用

## 関連問題
- Project Euler Problem 003: 最大の素因数
- Project Euler Problem 010: 素数の和
- Project Euler Problem 027: 二次式で表される素数
- 一般的な素数判定アルゴリズム（Miller-Rabin判定法など）
