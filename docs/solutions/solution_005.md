# Problem 005: Smallest multiple

## 問題
1から20までの数すべてで割り切れる最小の正の数を求めよ。

## 詳細
2520 is the smallest number that can be evenly divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)
```python
def solve_naive(n):
    candidate = n
    while True:
        is_divisible = True
        for i in range(1, n + 1):
            if candidate % i != 0:
                is_divisible = False
                break

        if is_divisible:
            return candidate

        candidate += 1
```

**特徴:**
- 候補となる数を1つずつ増やしながら全ての数で割り切れるかチェック
- 最も直感的で理解しやすいアプローチ
- 大きな数では非常に時間がかかる

**時間計算量:** O(result × n)
**空間計算量:** O(1)

### 2. 最適化解法 (LCM-based Approach)
```python
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def solve_optimized(n):
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result
```

**特徴:**
- 最小公倍数（LCM）の性質を活用: LCM(1,2,...,n) = LCM(LCM(1,2,...,n-1), n)
- ユークリッドの互除法による効率的なGCD計算
- 段階的にLCMを計算することで結果を求める

**時間計算量:** O(n × log(max_value))
**空間計算量:** O(1)

### 3. 数学的解法 (Prime Factorization Approach)
```python
def solve_mathematical(n):
    # エラトステネスの篩で素数を求める
    primes = sieve_of_eratosthenes(n)
    result = 1

    for prime in primes:
        max_power = max_prime_power(prime, n)
        result *= prime ** max_power

    return result
```

**特徴:**
- 素因数分解を利用した直接計算
- 各素数について1からnの範囲での最大冪を求める
- 最も効率的で数学的に美しいアプローチ

**時間計算量:** O(n × log(log(n)) + n × log(n))
**空間計算量:** O(n)

### 4. 標準ライブラリ解法 (Built-in Function Approach)
```python
def solve_builtin(n):
    result = 1
    for i in range(2, n + 1):
        result = math.lcm(result, i)
    return result
```

**特徴:**
- Python 3.9以降の`math.lcm`を活用
- 最もシンプルで読みやすいコード
- 内部実装が最適化されている

**時間計算量:** O(n × log(max_value))
**空間計算量:** O(1)

## 数学的背景

### 最小公倍数（LCM）と最大公約数（GCD）の関係
```
LCM(a, b) × GCD(a, b) = a × b
LCM(a, b) = (a × b) / GCD(a, b)
```

### ユークリッドの互除法
最大公約数を効率的に計算するアルゴリズム：
```
GCD(a, b) = GCD(b, a mod b)  (b ≠ 0の場合)
GCD(a, 0) = a
```

### 素因数分解による最小公倍数
複数の数の最小公倍数は、各素数について最大の冪を取ることで計算できる：

例：LCM(12, 18, 24)の場合
- 12 = 2² × 3¹
- 18 = 2¹ × 3²
- 24 = 2³ × 3⁰

各素数の最大冪：2³, 3²
→ LCM = 2³ × 3² = 8 × 9 = 72

### エラトステネスの篩
指定した範囲の素数を効率的に列挙するアルゴリズム：
1. 2からnまでの数を用意
2. 2から√nまで、各素数の倍数を除外
3. 残った数が素数

## 検証

### テストケース
- **n=1**: 1
- **n=2**: 2
- **n=3**: 6
- **n=4**: 12
- **n=5**: 60
- **n=10**: 2520（問題例）

### 本問題（n=20）
- **解答**: [隠匿]
- **素因数分解**: 2⁴ × 3² × 5¹ × 7¹ × 11¹ × 13¹ × 17¹ × 19¹
- **検証**: 1から20までの全ての数で割り切れることを確認

### 素因数分解の詳細
```
[隠匿] = 2⁴ × 3² × 5 × 7 × 11 × 13 × 17 × 19
         = 16 × 9 × 5 × 7 × 11 × 13 × 17 × 19
```

各素数の最大冪の根拠：
- 2⁴: 16 = 2⁴ が1～20の範囲の2の最大冪
- 3²: 9 = 3² が1～20の範囲の3の最大冪
- 5¹, 7¹, 11¹, 13¹, 17¹, 19¹: これらの素数の冪は1

## パフォーマンス比較

| 解法 | 時間計算量 | 実行時間 | 特徴 |
|------|------------|----------|------|
| Naive | O(result × n) | ~数秒 | 理解しやすい |
| Optimized | O(n × log(max)) | ~0.001秒 | 実用的 |
| Mathematical | O(n × log(n)) | ~0.0001秒 | 最速 |
| Builtin | O(n × log(max)) | ~0.0001秒 | 最もシンプル |

## 最適化のポイント

1. **数学的性質の活用**
   - LCMの累積計算による効率化
   - 素因数分解による直接計算

2. **アルゴリズムの選択**
   - エラトステネスの篩による効率的な素数列挙
   - ユークリッドの互除法による高速GCD計算

3. **実装の工夫**
   - 早期終了条件の活用
   - 適切なデータ構造の選択

## 学習ポイント

- **数論の基礎**: GCD、LCM、素因数分解の理解
- **アルゴリズム設計**: 問題の性質を活用した効率的な解法
- **数学的最適化**: 素因数分解による直接計算の威力
- **実装技術**: 標準ライブラリの活用と自作関数の使い分け

## 応用例

### 実世界での応用
1. **スケジューリング**: 異なる周期のイベントが同時に発生するタイミング
2. **音楽理論**: 異なる音程の最小公倍数による和音の周期
3. **工学**: 歯車の組み合わせでの最小回転数

### プログラミングでの応用
1. **タスクスケジューラ**: 異なる実行間隔のタスクの同期
2. **データ構造**: 配列のインデックス計算での周期性
3. **暗号学**: 素因数分解の困難性を利用した暗号

## 実装のポイント

### エラーハンドリング
- 負の数や0に対する適切な処理
- オーバーフローの考慮

### 可読性の向上
- 適切な関数分割
- 明確な変数名とコメント

### テスト戦略
- 境界値テスト
- 既知の結果との比較
- パフォーマンステスト

## 参考
- [Project Euler Problem 5](https://projecteuler.net/problem=5)
- [最小公倍数](https://ja.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0)
- [ユークリッドの互除法](https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89%E3%81%AE%E4%BA%92%E9%99%A4%E6%B3%95)
- [エラトステネスの篩](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)
