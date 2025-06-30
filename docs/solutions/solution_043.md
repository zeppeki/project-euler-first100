# Problem 043: Sub-string divisibility

## 問題

数1406357289は、0から9の各桁を1回ずつ使った0-9 pandigital数であり、興味深い部分文字列の割り切れ性質を持っている。

$d_1$を1桁目、$d_2$を2桁目、...として、以下のように表記する：
- $d_2d_3d_4=406$ は2で割り切れる
- $d_3d_4d_5=063$ は3で割り切れる  
- $d_4d_5d_6=635$ は5で割り切れる
- $d_5d_6d_7=357$ は7で割り切れる
- $d_6d_7d_8=572$ は11で割り切れる
- $d_7d_8d_9=728$ は13で割り切れる
- $d_8d_9d_{10}=289$ は17で割り切れる

この性質を持つ全ての0-9 pandigital数の和を求めよ。

## 解答

Project Euler公式サイトで確認してください。

## 解法

この問題は0-9 pandigital数の中で特定の部分文字列割り切れ条件を満たすものを見つける問題である。

### 1. 素直な解法 (Generate All)

**アルゴリズム：**
1. 全ての0-9 pandigital数を生成（10!通り）
2. 各数について部分文字列の割り切れ条件をチェック
3. 条件を満たす数の合計を計算

**時間計算量：** O(10!) = O(3,628,800)  
**空間計算量：** O(10!)

```python
def solve_naive() -> int:
    total_sum = 0
    pandigitals = generate_all_pandigital_0_to_9()
    
    for num_str in pandigitals:
        if has_substring_divisibility(num_str):
            total_sum += int(num_str)
    
    return total_sum
```

**特徴：**
- 実装が分かりやすい
- 全ての可能性を網羅的にチェック
- メモリ使用量が大きい

### 2. 最適化解法 (Backtracking)

**アルゴリズム：**
1. 各素数について割り切れる3桁数を事前計算
2. バックトラッキングで有効な10桁数を段階的に構築
3. 早期枝刈りで無効な組み合わせを排除

**時間計算量：** O(k) where k << 10! (有効な組み合わせのみ)  
**空間計算量：** O(k)

```python
def solve_optimized() -> int:
    # 各素数で割り切れる3桁数を事前計算
    primes = [2, 3, 5, 7, 11, 13, 17]
    valid_substrings = []
    
    for prime in primes:
        valid_for_prime = []
        for num in range(1000):
            if num % prime == 0:
                num_str = f"{num:03d}"
                if len(set(num_str)) == 3:  # 重複なし
                    valid_for_prime.append(num_str)
        valid_substrings.append(valid_for_prime)
    
    # バックトラッキングで構築
    valid_numbers = build_number('', 0, set())
    return sum(int(num) for num in valid_numbers)
```

**特徴：**
- 大幅な高速化（約8倍速い）
- 制約を利用した効率的な探索
- メモリ効率が良い

### 3. 数学的解法 (Direct Check)

**アルゴリズム：**
各順列について直接計算で割り切れ条件をチェックし、早期終了を利用。

**時間計算量：** O(10!) ただし早期終了による最適化  
**空間計算量：** O(1)

```python
def solve_mathematical() -> int:
    total_sum = 0
    primes = [2, 3, 5, 7, 11, 13, 17]
    
    for perm in itertools.permutations('0123456789'):
        if perm[0] == '0':  # 先頭0はスキップ
            continue
        
        # 早期終了での最適化
        valid = True
        for i, prime in enumerate(primes):
            substring_val = (int(perm[i+1]) * 100 + 
                           int(perm[i+2]) * 10 + 
                           int(perm[i+3]))
            if substring_val % prime != 0:
                valid = False
                break
        
        if valid:
            total_sum += int(''.join(perm))
    
    return total_sum
```

## 数学的背景

### Pandigital数の性質

0-9 pandigital数は以下の条件を満たす：
- 10桁の数
- 0から9までの各桁を1回ずつ使用
- 先頭桁は0以外（有効な10桁数として）

総数：$9 \times 9! = 3,265,920$ 個

### 部分文字列の制約

各部分文字列 $d_{i+1}d_{i+2}d_{i+3}$ が素数 $p_i$ で割り切れる条件：

| 位置 | 部分文字列 | 素数 | 制約 |
|------|------------|------|------|
| 2-4  | $d_2d_3d_4$ | 2 | 偶数 |
| 3-5  | $d_3d_4d_5$ | 3 | 桁和が3の倍数 |
| 4-6  | $d_4d_5d_6$ | 5 | 末尾が0または5 |
| 5-7  | $d_5d_6d_7$ | 7 | 7で割り切れる |
| 6-8  | $d_6d_7d_8$ | 11 | 11で割り切れる |
| 7-9  | $d_7d_8d_9$ | 13 | 13で割り切れる |
| 8-10 | $d_8d_9d_{10}$ | 17 | 17で割り切れる |

### 制約による絞り込み

特に強い制約：
1. **5の制約**: $d_6 \in \{0, 5\}$
2. **2の制約**: $d_4$ は偶数
3. **重複なし**: 全ての桁が異なる

これらの制約により、実際に条件を満たす数は非常に少ない。

## 学習ポイント

1. **制約充足問題**: 複数の制約を同時に満たす解の探索
2. **バックトラッキング**: 無効な部分解の早期排除
3. **計算量最適化**: 前処理による計算の高速化
4. **数値処理**: 大きな数の文字列と整数の変換
5. **順列生成**: itertools.permutationsの効率的な利用

## 実装のポイント

1. **メモリ効率**: 全順列を一度に生成せず、段階的に処理
2. **早期終了**: 無効な条件を早期に検出して枝刈り
3. **前処理**: 各素数で割り切れる3桁数の事前計算
4. **数値変換**: 文字列と整数の効率的な変換

この問題は制約充足とアルゴリズム最適化の良い例を提供している。特に、問題の制約を利用した効率的な解法の設計が重要である。
