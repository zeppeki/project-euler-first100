# Problem 034: Digit factorials

## 問題

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

**145は興味深い数字です。1! + 4! + 5! = 1 + 24 + 120 = 145となるからです。**

**各桁の階乗の和が元の数と等しくなる全ての数の和を求めてください。**

**注意: 1! = 1 と 2! = 2 は和ではないので含めません。**

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法（総当たり）

上限まで全ての数をチェックして桁階乗数を見つけます。

```python
def solve_naive() -> int:
    # 上限の数学的分析:
    # 9! = 362,880なので、7桁の数字でも最大7 * 9! = 2,540,160
    upper_limit = 7 * factorial(9)

    digit_factorials = []

    # 1! = 1, 2! = 2は和ではないので除外
    for number in range(3, upper_limit + 1):
        if is_digit_factorial(number):
            digit_factorials.append(number)

    return sum(digit_factorials)
```

**時間計算量**: O(n * log n) - nは上限値
**空間計算量**: O(k) - kは見つかった数の個数

### 2. 最適化解法（効率的探索）

事前計算した階乗テーブルを使用して効率化します。

```python
def solve_optimized() -> int:
    # より厳密な上限分析
    def find_upper_bound() -> int:
        for d in range(1, 10):
            max_number = 10 ** d - 1
            max_factorial_sum = d * factorial(9)
            if max_number > max_factorial_sum:
                return max_factorial_sum
        return 7 * factorial(9)

    upper_limit = find_upper_bound()
    digit_factorials = []

    # 事前計算した階乗テーブルを使用
    fact_table = [factorial(i) for i in range(10)]

    def digit_factorial_sum_optimized(number: int) -> int:
        total = 0
        temp = number
        while temp > 0:
            digit = temp % 10
            total += fact_table[digit]
            temp //= 10
        return total

    for number in range(3, upper_limit + 1):
        if number == digit_factorial_sum_optimized(number):
            digit_factorials.append(number)

    return sum(digit_factorials)
```

**時間計算量**: O(n * log n) - より小さなnで探索
**空間計算量**: O(k) - kは見つかった数の個数

### 3. 数学的解法（上限最適化）

数学的性質を利用した上限設定と効率的な計算を行います。

```python
def solve_mathematical() -> int:
    # 階乗テーブルの事前計算
    factorials = [math.factorial(i) for i in range(10)]

    # 上限の計算: d桁の数の最大値 vs d * 9!
    upper_limit = 0
    for d in range(1, 8):
        max_d_digit = 10 ** d - 1
        max_factorial_sum = d * factorials[9]
        if max_d_digit > max_factorial_sum:
            upper_limit = max_factorial_sum
            break

    total_sum = 0

    # 最適化された桁階乗和計算
    def fast_digit_factorial_sum(n: int) -> int:
        result = 0
        while n > 0:
            result += factorials[n % 10]
            n //= 10
        return result

    # 3から上限まで検索（1!, 2!は除外）
    for number in range(3, upper_limit + 1):
        if number == fast_digit_factorial_sum(number):
            total_sum += number

    return total_sum
```

**時間計算量**: O(n) - より効率的な探索
**空間計算量**: O(1)

## 数学的背景

### 桁階乗数の定義

桁階乗数は以下の条件を満たす数です：

- **各桁の階乗の和**: 数字の各桁について階乗を計算し、その和を求める
- **自己等価性**: 計算した和が元の数と等しい
- **非自明性**: 1! = 1, 2! = 2は「和」ではないので除外

### 上限の数学的導出

d桁の数の範囲と階乗和の最大値を比較して上限を決定：

1. **d桁の数の範囲**: 10^(d-1) ≤ n ≤ 10^d - 1
2. **d桁の階乗和の最大値**: d × 9! = d × 362,880
3. **上限条件**: d桁の最小値が d × 9! を超える点で検索終了

具体的な計算：
- 1桁: 最大1, 階乗和最大 1×9! = 362,880
- 2桁: 最大99, 階乗和最大 2×9! = 725,760
- 3桁: 最大999, 階乗和最大 3×9! = 1,088,640
- ...
- 7桁: 最大9,999,999, 階乗和最大 7×9! = 2,540,160
- 8桁: 最小10,000,000 > 8×9! = 2,903,040

よって7×9! = 2,540,160が適切な上限となります。

### 既知の桁階乗数

Problem 034で発見される桁階乗数：

1. **145**: 1! + 4! + 5! = 1 + 24 + 120 = 145
2. **40585**: 4! + 0! + 5! + 8! + 5! = 24 + 1 + 120 + 40320 + 120 = 40585

## 検証

### 例題の検証

**145の計算**:
- 1! = 1
- 4! = 24
- 5! = 120
- 合計: 1 + 24 + 120 = 145 ✓

### 解答

Project Euler公式サイトで確認してください。

### 検証結果
- **素直な解法**: [隠匿]
- **最適化解法**: [隠匿]
- **数学的解法**: [隠匿]
- **一致確認**: ✓

## パフォーマンス比較

実行時間の比較（参考値）：
- **素直な解法**: ~26秒
- **最適化解法**: ~25秒
- **数学的解法**: ~24秒

事前計算により若干の性能向上が見られます。

## 最適化のポイント

1. **上限設定**: 数学的分析による効率的な検索範囲の決定
2. **事前計算**: 階乗値のテーブル化による計算の高速化
3. **除外条件**: 1!, 2!の適切な除外処理
4. **桁処理**: 効率的な桁抽出アルゴリズム

## 学習ポイント

1. **階乗の性質**: 階乗の急激な増加とその数学的意味
2. **上限分析**: 数学的性質を利用した探索範囲の最適化
3. **桁操作**: 数値の桁を効率的に処理する手法
4. **事前計算**: 繰り返し計算の最適化手法
5. **境界条件**: 問題の制約条件の正確な理解と実装

## 参考

- [Project Euler Problem 034](https://projecteuler.net/problem=34)
- [Factorial - Wikipedia](https://en.wikipedia.org/wiki/Factorial)
- [Digital root and related topics](https://en.wikipedia.org/wiki/Digital_root)
