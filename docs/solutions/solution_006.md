# Problem 006: Sum square difference

## 問題
最初の100個の自然数の平方和と和の平方の差を求めよ。

## 詳細
The sum of the squares of the first ten natural numbers is:
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is: 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)
```python
def solve_naive(n):
    # 平方の和を計算: 1² + 2² + ... + n²
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_squares += i * i

    # 和の平方を計算: (1 + 2 + ... + n)²
    sum_of_numbers = 0
    for i in range(1, n + 1):
        sum_of_numbers += i
    square_of_sum = sum_of_numbers * sum_of_numbers

    # 差を返す
    return square_of_sum - sum_of_squares
```

**特徴:**
- 各項を個別に計算してから和を求める直感的なアプローチ
- 2つのループで平方の和と和の平方を別々に計算
- 理解しやすく実装も簡単

**時間計算量:** O(n)
**空間計算量:** O(1)

### 2. 最適化解法 (Formula-based Approach)
```python
def solve_optimized(n):
    # 和の公式を使用: 1 + 2 + ... + n = n(n+1)/2
    sum_of_numbers = n * (n + 1) // 2
    square_of_sum = sum_of_numbers * sum_of_numbers

    # 平方和の公式を使用: 1² + 2² + ... + n² = n(n+1)(2n+1)/6
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6

    # 差を返す
    return square_of_sum - sum_of_squares
```

**特徴:**
- 数学的公式を使用した定数時間での計算
- 自然数の和の公式: Σi = n(n+1)/2
- 平方数の和の公式: Σi² = n(n+1)(2n+1)/6
- 非常に効率的で高速

**時間計算量:** O(1)
**空間計算量:** O(1)

### 3. 数学的解法 (Direct Formula Derivation)
```python
def solve_mathematical(n):
    # 導出した公式を使用: n(n+1)(n-1)(3n+2)/12
    return n * (n + 1) * (n - 1) * (3 * n + 2) // 12
```

**特徴:**
- 差の公式を代数的に導出した直接計算
- 中間計算を省略した最も効率的なアプローチ
- 一つの式で直接結果を計算

**時間計算量:** O(1)
**空間計算量:** O(1)

## 数学的背景

### 基本公式
1. **自然数の和**:
   ```
   1 + 2 + 3 + ... + n = n(n+1)/2
   ```

2. **平方数の和**:
   ```
   1² + 2² + 3² + ... + n² = n(n+1)(2n+1)/6
   ```

### 差の公式の導出
和の平方と平方の和の差を代数的に計算：

```
(和の平方) - (平方の和) = [n(n+1)/2]² - n(n+1)(2n+1)/6

= n²(n+1)²/4 - n(n+1)(2n+1)/6

= n(n+1)[n(n+1)/4 - (2n+1)/6]

= n(n+1)[3n(n+1) - 2(2n+1)]/12

= n(n+1)[3n² + 3n - 4n - 2]/12

= n(n+1)(3n² - n - 2)/12

= n(n+1)(n-1)(3n+2)/12
```

この導出により、直接計算可能な公式が得られます。

### 具体例 (n=10)
- **和**: 1 + 2 + ... + 10 = 55
- **和の平方**: 55² = 3025
- **平方の和**: 1² + 2² + ... + 10² = 385
- **差**: 3025 - 385 = 2640

### 実際の問題 (n=100)
- **和**: 100 × 101 / 2 = 5050
- **和の平方**: 5050² = 25,502,500
- **平方の和**: 100 × 101 × 201 / 6 = 338,350
- **差**: [隠匿]

## パフォーマンス比較

| 解法 | 時間計算量 | 空間計算量 | 特徴 |
|------|-----------|-----------|------|
| 素直な解法 | O(n) | O(1) | 理解しやすい、直感的 |
| 最適化解法 | O(1) | O(1) | 数学公式使用、高速 |
| 数学的解法 | O(1) | O(1) | 導出公式、最効率 |

大きなnに対しては、定数時間で計算できる最適化解法と数学的解法が圧倒的に高速です。

## 学習ポイント

1. **数学的公式の活用**: 単純なループよりも既知の公式を使用することで大幅な性能向上が可能
2. **代数的変形**: 複雑な式も適切な変形により簡潔な公式に導出可能
3. **パフォーマンス考慮**: 同じ結果でも計算量の違いで実行時間に大きな差が生じる
4. **検証の重要性**: 複数のアプローチで同じ結果を得ることで正確性を確認

## 関連問題
- Project Euler Problem 001: 等差数列の和
- Project Euler Problem 002: フィボナッチ数列の和
- 一般的な数列の和の公式
- 組み合わせ論における二項係数の性質
