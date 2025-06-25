# Problem 014: Longest Collatz sequence

## 問題
100万未満の数の中で、最も長いCollatz数列を生成する開始数を求めよ。

## 詳細
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Conjecture), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)
```python
def solve_naive(limit):
    max_length = 0
    max_start = 0

    for start in range(1, limit):
        length = collatz_length_simple(start)
        if length > max_length:
            max_length = length
            max_start = start

    return max_start

def collatz_length_simple(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length
```

**特徴:**
- 各数について個別にCollatz数列の長さを計算する直感的なアプローチ
- Collatz予想のルールを忠実に実装
- 計算済みの値を再利用しないため非効率

**時間計算量:** O(n × L) (Lは平均チェーン長)
**空間計算量:** O(1)

### 2. 最適化解法 (Memoization)
```python
def solve_optimized(limit):
    memo = {}
    max_length = 0
    max_start = 0

    for start in range(1, limit):
        length = collatz_length_memoized(start, memo)
        if length > max_length:
            max_length = length
            max_start = start

    return max_start

def collatz_length_memoized(n, memo):
    original_n = n
    path = []

    # 既知の値に達するまで計算
    while n not in memo and n != 1:
        path.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    # 基準値を取得
    if n == 1:
        base_length = 1
    else:
        base_length = memo[n]

    # パス上の全ての値をメモ化
    for i in range(len(path) - 1, -1, -1):
        base_length += 1
        memo[path[i]] = base_length

    return memo[original_n]
```

**特徴:**
- メモ化（動的プログラミング）を使用して計算済みの値を再利用
- 一度計算した数列の長さは記憶して次回の計算で活用
- パス上の全ての値をメモ化することで効率最大化

**時間計算量:** O(n × log L) (Lは平均チェーン長)
**空間計算量:** O(n)

### 3. 数学的解法 (Mathematical Optimization)
```python
def solve_mathematical(limit):
    memo = {1: 1}
    max_length = 0
    max_start = 0

    for start in range(1, limit):
        length = collatz_length_optimized(start, memo)
        if length > max_length:
            max_length = length
            max_start = start

    return max_start

def collatz_length_optimized(n, memo):
    if n in memo:
        return memo[n]

    original_n = n
    length = 0

    while n not in memo and n != 1:
        if n % 2 == 0:
            n //= 2
            length += 1
        else:
            # 奇数の場合、3n+1の後に必ず偶数になるので2ステップまとめて処理
            n = (3 * n + 1) // 2
            length += 2

    # 既知の値に到達
    memo[original_n] = length + memo.get(n, 1)
    return memo[original_n]
```

**特徴:**
- 奇数処理の最適化：3n+1の後は必ず偶数になることを利用
- 2ステップを1回の操作にまとめて処理回数を削減
- メモ化と数学的最適化の組み合わせ

**時間計算量:** O(n × log L)
**空間計算量:** O(n)

## 数学的背景

### Collatz予想（3n+1予想）
- **予想内容**: 全ての正の整数はCollatz数列によって最終的に1に到達する
- **現状**: 未証明だが、現在まで反例は見つかっていない
- **検証範囲**: 2^68 (約2.95×10^20) まで確認済み

### 数列の特徴
1. **偶数処理**: n → n/2 (単純な半分)
2. **奇数処理**: n → 3n+1 (3倍して1を加える)
3. **終了条件**: 1に到達で終了
4. **値の変動**: 一度開始すると値は上下動する

### 数学的性質
- **奇数の後は偶数**: 3n+1は必ず偶数（3×奇数+1 = 偶数）
- **連続する処理**: 奇数 → 3n+1 → (3n+1)/2 の2ステップを1回で処理可能
- **上限なし**: チェーン中の値は開始数より大きくなる場合がある

## 具体例

### 例1: 13から始まる数列
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (10ステップ)

### 例2: 小さな数の比較
- **1**: 1 (1ステップ)
- **2**: 2 → 1 (2ステップ)
- **3**: 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (8ステップ)
- **4**: 4 → 2 → 1 (3ステップ)
- **5**: 5 → 16 → 8 → 4 → 2 → 1 (6ステップ)

### 計算結果の例
- **limit = 10**: 最長は9 (20ステップ)
- **limit = 100**: 最長は97 (119ステップ)
- **limit = 1000**: 最長は871 (179ステップ)
- **limit = 1000000**: 最長は [隠匿] ([隠匿]ステップ)

## パフォーマンス比較

| 解法 | 時間計算量 | 空間計算量 | 特徴 |
|------|-----------|-----------|------|
| 素直な解法 | O(n×L) | O(1) | 理解しやすい、メモリ効率的 |
| 最適化解法 | O(n×log L) | O(n) | メモ化による大幅な高速化 |
| 数学的解法 | O(n×log L) | O(n) | 奇数処理最適化でさらに高速 |

### 実行時間の傾向
- **小さなlimit (< 1000)**: 全解法が高速
- **中程度のlimit (< 100000)**: メモ化の効果が顕著
- **大きなlimit (1000000)**: 数学的最適化が最高速
- **メモリ制約あり**: 素直な解法が適している

## アルゴリズムの詳細

### メモ化の効率性
```python
# 例: 6の計算時に3, 10, 5の長さも同時に計算される
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# memo[6] = 9, memo[3] = 8, memo[10] = 7, memo[5] = 6
```

### 奇数処理の最適化
```python
# 通常の処理
if n % 2 == 1:
    n = 3 * n + 1  # ステップ1
    n = n // 2     # ステップ2（3n+1は必ず偶数）

# 最適化後
if n % 2 == 1:
    n = (3 * n + 1) // 2  # 2ステップを1回で処理
    length += 2
```

## 学習ポイント

1. **動的プログラミング**: メモ化による重複計算の排除
2. **数学的最適化**: 問題の性質を活用した計算量削減
3. **未解決問題**: Collatz予想のような数学の未解決問題への取り組み
4. **パフォーマンス分析**: 異なるアプローチの計算量とメモリ使用量の比較

## 応用と発展

### 関連する数列問題
- **ハイルストーン数列**: Collatz数列の別名
- **Syracuse問題**: 同じ問題の別の呼び名
- **Lothar Collatz**: ドイツの数学者、1937年に予想を提示

### 計算数学への応用
- **分散コンピューティング**: 大きな数の検証
- **数値実験**: パターン認識と統計分析
- **アルゴリズム設計**: メモ化と最適化技法

### プログラミング技法
- **動的プログラミング**: メモ化による効率化
- **数学的最適化**: 問題固有の性質を活用
- **メモリ管理**: 大規模データの効率的処理

## 検証結果

### 小規模テスト
- **入力**: limit = 20
- **解答**: [隠匿]
- **チェーン長**: [隠匿]
- **検証**: ✓

### 中規模テスト
- **入力**: limit = 1000
- **解答**: [隠匿]
- **チェーン長**: [隠匿]
- **検証**: ✓

### 大規模テスト (Project Euler)
- **入力**: limit = 1000000
- **解答**: [隠匿]
- **チェーン長**: [隠匿]
- **検証**: ✓

## 関連問題
- Project Euler Problem 092: Square digit chains
- Project Euler Problem 179: Consecutive positive divisors
- Project Euler Problem 214: Totient chains
