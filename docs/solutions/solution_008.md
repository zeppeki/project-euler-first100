# Problem 008: Largest product in a series

## 問題
1000桁の数の中で隣接する4桁の数字の積が最大となるのは 9 × 9 × 8 × 9 = 5832 である。

この1000桁の数の中で隣接する13桁の数字の積の最大値を求めよ。

## 詳細
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?

**1000桁の数:**
```
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
```

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)
```python
def solve_naive(adjacent_digits=13):
    max_product = 0

    # 全ての可能な隣接する桁のシーケンスをチェック
    for i in range(len(THOUSAND_DIGIT_NUMBER) - adjacent_digits + 1):
        # 現在のシーケンスの積を計算
        current_product = 1
        for j in range(i, i + adjacent_digits):
            digit = int(THOUSAND_DIGIT_NUMBER[j])
            current_product *= digit

        max_product = max(max_product, current_product)

    return max_product
```

**特徴:**
- 全ての隣接するシーケンスを順次チェック
- 各シーケンスで積を個別に計算
- 理解しやすい直感的なアプローチ

**時間計算量:** O(n * k) where n is number length, k is adjacent digits
**空間計算量:** O(1)

### 2. 最適化解法 (Sliding Window with Zero Skip)
```python
def solve_optimized(adjacent_digits=13):
    max_product = 0

    # スライディングウィンドウでゼロを含まないシーケンスのみを処理
    i = 0
    while i <= len(THOUSAND_DIGIT_NUMBER) - adjacent_digits:
        # 現在位置からadjacent_digits分の桁を取得
        sequence = THOUSAND_DIGIT_NUMBER[i:i + adjacent_digits]

        # ゼロが含まれている場合、ゼロの次の位置まで スキップ
        if "0" in sequence:
            zero_pos = sequence.find("0")
            i += zero_pos + 1
            continue

        # ゼロが含まれていない場合、積を計算
        current_product = 1
        for digit_char in sequence:
            current_product *= int(digit_char)

        max_product = max(max_product, current_product)
        i += 1

    return max_product
```

**特徴:**
- スライディングウィンドウ技法を使用
- ゼロを含むシーケンスを効率的にスキップ
- ゼロがある場合、その位置の次から再開

**時間計算量:** O(n) where n is number length
**空間計算量:** O(1)

### 3. 数学的解法 (Efficient Product Calculation)
```python
def solve_mathematical(adjacent_digits=13):
    max_product = 0

    i = 0
    while i <= len(THOUSAND_DIGIT_NUMBER) - adjacent_digits:
        # 現在位置からadjacent_digits分のシーケンスを取得
        sequence = THOUSAND_DIGIT_NUMBER[i:i + adjacent_digits]

        # ゼロが含まれている場合、ゼロの後まで スキップ
        if "0" in sequence:
            zero_pos = sequence.find("0")
            i += zero_pos + 1
            continue

        # reduce関数を使用して効率的に積を計算
        current_product = reduce(mul, (int(d) for d in sequence), 1)
        max_product = max(max_product, current_product)
        i += 1

    return max_product
```

**特徴:**
- reduce関数とoperator.mulを使用した効率的な積計算
- ゼロスキップの最適化を組み合わせ
- Pythonの内蔵関数を活用した高速化

**時間計算量:** O(n) where n is number length
**空間計算量:** O(1)

## アルゴリズム解析

### ゼロスキップ最適化の効果
1000桁の数において：
- ゼロの個数: [実際の数値は隠匿]
- ゼロの割合: [実際の割合は隠匿]%

ゼロを含むシーケンスは積が必ず0になるため、これらをスキップすることで計算量を大幅に削減できます。

### スライディングウィンドウ技法
連続するシーケンスを効率的に処理する手法：
1. 現在のウィンドウで積を計算
2. ウィンドウを1つずらす
3. 新しい桁を追加、古い桁を除去
4. 積を更新

ただし、この問題では除算が必要になるため、ゼロスキップと組み合わせた方が効率的です。

### 積の計算最適化
```python
# 通常のループ
product = 1
for digit in sequence:
    product *= int(digit)

# reduce関数使用
product = reduce(mul, (int(d) for d in sequence), 1)

# 内包表記 + 乗算
from math import prod  # Python 3.8+
product = prod(int(d) for d in sequence)
```

## 数学的背景

### 積の性質
1. **ゼロ要素**: 積にゼロが含まれると結果は必ず0
2. **最大化条件**: 大きな桁の数字を多く含むシーケンスが有利
3. **桁数の影響**: 隣接する桁数が多いほど、積は指数的に大きくなる可能性

### 最適化戦略
1. **ゼロ回避**: ゼロを含むシーケンスは即座に除外
2. **大きな桁の探索**: 9, 8, 7などの大きな桁が集中している領域を重点的に探索
3. **早期終了**: 理論上の最大値に達した場合の早期終了（実装可能だが通常不要）

## パフォーマンス比較

| 解法 | 時間計算量 | 空間計算量 | 特徴 |
|------|-----------|-----------|------|
| 素直な解法 | O(nk) | O(1) | 理解しやすい、全探索 |
| 最適化解法 | O(n) | O(1) | ゼロスキップで高速化 |
| 数学的解法 | O(n) | O(1) | 内蔵関数で最高速 |

実際の性能差は、ゼロの分布によって大きく左右されます。

## 実装のポイント

### エラーハンドリング
```python
if adjacent_digits <= 0:
    raise ValueError("adjacent_digits must be positive")
if adjacent_digits > len(THOUSAND_DIGIT_NUMBER):
    raise ValueError("adjacent_digits cannot exceed number length")
```

### デバッグ支援
```python
def get_max_product_sequence(adjacent_digits=13):
    """最大積となるシーケンスとその積を返す"""
    # 実装詳細は省略
    return max_sequence, max_product
```

## 学習ポイント

1. **文字列処理**: 大きな数値を文字列として扱う効率的な手法
2. **最適化技法**: ゼロスキップによる計算量削減
3. **スライディングウィンドウ**: 連続するシーケンス処理の基本パターン
4. **Python標準ライブラリ**: reduce, operator.mul, math.prodの活用
5. **計算量解析**: 実際の最適化効果の定量的評価

## 関連問題
- Project Euler Problem 011: 格子内の最大積
- Project Euler Problem 016: べき乗の各桁の和
- Project Euler Problem 020: 階乗の各桁の和
- 一般的な動的プログラミング問題
- 文字列処理とパターンマッチング
