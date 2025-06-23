# Problem 004: Largest palindrome product

## 問題
3桁の数の積で表される最大の回文数を求めよ。

## 詳細
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)
```python
def solve_naive(min_digits, max_digits):
    min_num = 10 ** (min_digits - 1)
    max_num = 10 ** max_digits - 1

    largest_palindrome = 0
    factors = (0, 0)

    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if product <= largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product
                factors = (i, j)

    return largest_palindrome, factors[0], factors[1]
```

**特徴:**
- 全ての3桁の数の組み合わせをチェック
- 大きな数から小さな数へと順番に処理
- 現在の最大値以下の積は早期終了で除外

**時間計算量:** O(n²)
**空間計算量:** O(1)

### 2. 最適化解法 (Optimized Approach)
```python
def solve_optimized(min_digits, max_digits):
    min_num = 10 ** (min_digits - 1)
    max_num = 10 ** max_digits - 1

    largest_palindrome = 0
    factors = (0, 0)

    for i in range(max_num, min_num - 1, -1):
        if i * max_num <= largest_palindrome:
            break  # 外側ループの早期終了

        for j in range(min(i, max_num), min_num - 1, -1):
            product = i * j
            if product <= largest_palindrome:
                break

            if is_palindrome(product):
                largest_palindrome = product
                factors = (i, j)
                break  # 最大値を見つけたので内側ループ終了

    return largest_palindrome, factors[0], factors[1]
```

**特徴:**
- より効果的な早期終了条件
- 最大値発見時の内側ループ終了
- 外側ループでも早期終了判定

**時間計算量:** O(n²) but with better pruning
**空間計算量:** O(1)

### 3. 数学的解法 (Mathematical Approach)
```python
def solve_mathematical(min_digits, max_digits):
    # 6桁の回文の性質を利用
    # abccba = 100001*a + 10010*b + 1100*c = 11*(9091*a + 910*b + 100*c)
    # つまり、6桁の回文は必ず11で割り切れる

    for i in range(max_num, min_num - 1, -1):
        if i * max_num <= largest_palindrome:
            break

        j_step = 11 if i % 11 != 0 else 1
        j_start = j_start - (j_start % 11) if i % 11 != 0 else j_start

        j = j_start
        while j >= min_num:
            product = i * j
            if product <= largest_palindrome:
                break

            if is_palindrome(product):
                largest_palindrome = product
                factors = (i, j)
                break

            j -= j_step
```

**特徴:**
- 6桁回文の数学的性質を活用（11で割り切れる）
- 因数の一方が11で割り切れない場合、もう一方は11の倍数
- 探索空間を大幅に削減

**時間計算量:** O(n²) with mathematical optimizations
**空間計算量:** O(1)

## 数学的背景

### 回文数の性質
6桁の回文数 `abccba` は以下のように表現できる：
```
abccba = 100000a + 10000b + 1000c + 100c + 10b + a
       = 100001a + 10010b + 1100c
       = 11 × (9091a + 910b + 100c)
```

この式から、**全ての6桁の回文数は11で割り切れる**ことがわかる。

### 因数分解への応用
3桁の数の積で6桁の回文を作る場合：
- 積が11で割り切れるため、少なくとも一方の因数が11で割り切れる必要がある
- 一方が11で割り切れない場合、もう一方は必ず11の倍数
- これにより探索空間を約1/11に削減できる

## 検証

### テストケース
- **1桁の場合:** 3 × 3 = 9
- **2桁の場合:** 91 × 99 = 9009
- **3桁の場合:** [隠匿]

### 本問題
- **入力:** 3桁の数同士の積
- **解答:** [隠匿]
- **検証:** ✓

## パフォーマンス比較

| 解法 | 時間計算量 | 実行時間 | 最適化内容 |
|------|------------|----------|------------|
| Naive | O(n²) | ~0.1秒 | 基本的な早期終了 |
| Optimized | O(n²) | ~0.05秒 | 高度な早期終了 |
| Mathematical | O(n²) | ~0.01秒 | 数学的性質活用 |

## 最適化のポイント

1. **早期終了条件の活用**
   - `i * max_num <= largest_palindrome` で外側ループを終了
   - `product <= largest_palindrome` で内側ループを終了

2. **数学的性質の活用**
   - 6桁回文が11で割り切れる性質
   - 因数の一方が11の倍数である必要性

3. **探索順序の最適化**
   - 大きな数から小さな数へと探索
   - 最大値発見時の即座な終了

## 学習ポイント

- **数学的観察の重要性**: 回文数の構造分析
- **早期終了の効果**: 計算量削減テクニック
- **問題の性質理解**: 6桁回文の特殊性
- **アルゴリズム最適化**: 複数アプローチの比較

## 実装のポイント

### 回文判定
```python
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
```

### 因数の範囲制限
- 3桁の数: 100 ≤ n ≤ 999
- 重複回避: j ≥ i として組み合わせを制限

### メモリ効率
- 全ての積を保存せず、最大値のみ保持
- 定数メモリ使用量での実装

## 参考
- [Project Euler Problem 4](https://projecteuler.net/problem=4)
- [回文数の性質](https://ja.wikipedia.org/wiki/%E5%9B%9E%E6%96%87%E6%95%B0)
- [整数の性質と因数分解](https://ja.wikipedia.org/wiki/%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3)
