# Problem 010: Summation of primes

## 問題
200万未満の全ての素数の和を求めよ。

## 詳細
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)
```python
def solve_naive(limit):
    if limit <= 2:
        return 0

    prime_sum = 2  # 最初の素数2を加算

    # 3から始めて奇数のみをチェック
    for num in range(3, limit, 2):
        if is_prime_naive(num):
            prime_sum += num

    return prime_sum

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
- 各数を順次チェックして素数判定し、素数の場合は合計に加算
- 2以外の偶数は除外して効率化
- 素数判定は√nまでの奇数で割り切れるかチェック

**時間計算量:** O(n × √n)
**空間計算量:** O(1)

### 2. 最適化解法 (Sieve of Eratosthenes)
```python
def solve_optimized(limit):
    if limit <= 2:
        return 0

    # エラトステネスの篩で素数を見つけて合計
    primes = sieve_of_eratosthenes(limit - 1)
    return sum(primes)

def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []

    # 篩を初期化
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # 篩を実行
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # 素数のリストを作成
    return [i for i in range(2, limit + 1) if is_prime[i]]
```

**特徴:**
- エラトステネスの篩を使用した効率的な素数生成
- 指定範囲内の全ての素数を一度に生成
- 合成数を篩い落として素数のみを残す

**時間計算量:** O(n × log(log(n)))
**空間計算量:** O(n)

### 3. 数学的解法 (Memory-Optimized Sieve)
```python
def solve_mathematical(limit):
    if limit <= 2:
        return 0

    # 2は別途処理
    prime_sum = 2

    # 奇数のみの篩を使用してメモリを半分に削減
    odd_limit = (limit - 1) // 2
    is_prime_odd = [True] * (odd_limit + 1)

    # 3から始めて奇数の合成数をマーク
    for i in range(1, int(math.sqrt(limit)) // 2 + 1):
        if is_prime_odd[i]:
            prime = 2 * i + 1
            # prime * prime から開始して、prime の奇数倍をマーク
            start = (prime * prime - 1) // 2
            for j in range(start, odd_limit + 1, prime):
                is_prime_odd[j] = False

    # 奇数の素数の合計を計算
    for i in range(1, odd_limit + 1):
        if is_prime_odd[i]:
            prime_sum += 2 * i + 1

    return prime_sum
```

**特徴:**
- 奇数のみを対象とした篩でメモリ使用量を半分に削減
- 2は別途処理し、3以降の奇数のみを篩で処理
- インデックスと実際の数値の変換を効率的に実行

**時間計算量:** O(n × log(log(n)))
**空間計算量:** O(n/2)

## 数学的背景

### エラトステネスの篩の原理
1. **初期化**: 2からnまでの数を全て素数候補として設定
2. **篩い落とし**: 2から順番に、その数の倍数を合成数として除外
3. **最適化**: √nまでの数のみを処理すれば十分

### 素数の分布
- **素数定理**: n以下の素数の個数は約 n/ln(n)
- **ベルトラン・チェビシェフの定理**: nと2nの間には必ず素数が存在
- **リーマン予想**: 素数の分布に関する未解決問題

### メモリ最適化の技法
1. **奇数のみ**: 2以外の偶数は全て合成数なので除外
2. **ビット操作**: booleanの代わりにbitを使用してメモリ削減
3. **セグメント篩**: 大きな範囲を小さなセグメントに分割

## 具体例

### 問題例の検証
10未満の素数: 2, 3, 5, 7
合計: 2 + 3 + 5 + 7 = 17

### より大きな例
30未満の素数: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
合計: 129

### 実際の問題 (limit=2,000,000)
- **200万未満の素数の個数**: 148,933個
- **素数の合計**: [隠匿]
- **素数の密度**: 約7.46%

## パフォーマンス比較

| 解法 | 時間計算量 | 空間計算量 | 特徴 |
|------|-----------|-----------|------|
| 素直な解法 | O(n×√n) | O(1) | 理解しやすい、メモリ効率的 |
| 最適化解法 | O(n×log(log(n))) | O(n) | 最も高速、標準的な篩 |
| 数学的解法 | O(n×log(log(n))) | O(n/2) | メモリ最適化版の篩 |

### 実行時間の傾向
- **小さなn (< 1000)**: 全ての解法が高速
- **中程度のn (< 100,000)**: 篩系が有利
- **大きなn (2,000,000)**: 篩系が圧倒的に高速
- **メモリ制約**: 数学的解法が効果的

## 学習ポイント

1. **篩アルゴリズム**: エラトステネスの篩の実装と最適化
2. **メモリ効率**: 奇数のみを対象とした空間削減技法
3. **時間計算量**: O(n×log(log(n)))の優秀な性能
4. **数学的性質**: 素数の分布と密度の理解

## 応用と発展

### 高速化技法
- **セグメント篩**: メモリ使用量を削減する分割統治法
- **車輪の篩**: 2,3,5などの小さな素数で事前篩
- **並列化**: マルチスレッドによる篩の並列実行

### 関連アルゴリズム
- **線形篩**: O(n)時間での素数生成
- **確率的素数判定**: Miller-Rabin判定法
- **決定論的素数判定**: AKS素数判定法

### 実用的応用
- **暗号学**: RSA暗号の鍵生成
- **ハッシュ関数**: 素数を利用したハッシュ値計算
- **数論**: 素因数分解や約数関数の計算

## 実装のポイント

### エラーの回避
1. **境界条件**: limit=2,3などの小さな値の処理
2. **整数オーバーフロー**: 大きな合計値の処理
3. **メモリ不足**: 大きなlimitでの配列確保

### 最適化のコツ
1. **キャッシュ効率**: 配列アクセスパターンの最適化
2. **分岐予測**: 条件分岐の削減
3. **SIMD活用**: ベクトル化による高速化

## 関連問題
- Project Euler Problem 003: 最大の素因数
- Project Euler Problem 007: 10001番目の素数
- Project Euler Problem 027: 連続する素数を生成する二次式
- Project Euler Problem 035: 循環素数
- Project Euler Problem 037: 切り詰め可能素数
