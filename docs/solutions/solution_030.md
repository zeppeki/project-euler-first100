# Problem 030: Digit fifth powers

## 問題

各桁を5乗した数の和が自分自身と等しい全ての数の総和を求めよ。

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 方針

各桁の数字の5乗の和が、その数自身と等しくなる数を探します。例えば、`1634 = 1^4 + 6^4 + 3^4 + 4^4` のような数です（これは4乗の例）。

この問題の鍵となるのは、探索する数の上限を見積もることです。

- 1桁の数の場合、最大の5乗和は `9^5 = 59049` です。
- 2桁の数の場合、最大の5乗和は `9^5 + 9^5 = 118098` です。
- d桁の数の最大の5乗和は `d * 9^5` となります。

この `d * 9^5` がd桁の数である限り、探索を続ける意味があります。

- `d=1`: `1 * 9^5 = 59049` (5桁)
- `d=2`: `2 * 9^5 = 118098` (6桁)
- `d=3`: `3 * 9^5 = 177147` (6桁)
- `d=4`: `4 * 9^5 = 236196` (6桁)
- `d=5`: `5 * 9^5 = 295245` (6桁)
- `d=6`: `6 * 9^5 = 354294` (6桁)
- `d=7`: `7 * 9^5 = 413343` (6桁)

`d=7` の場合、7桁の数の最大の5乗和は `413343` であり、これは7桁の最小値 `1,000,000` よりも小さいです。したがって、7桁以上の数でこの条件を満たすことはありえません。

よって、探索範囲の上限は `6 * 9^5 = 354294` と見積もることができます。この上限までの数をすべてチェックすれば、解を見つけることができます。

### 2. 実装 (solve)

```python
def solve(power: int = 5) -> int:
    """
    Finds the sum of all numbers that can be written as the sum of the given
    power of their digits.
    """
    # Determine the upper bound for the search.
    # For a number with d digits, the maximum sum of powers is d * 9^power.
    # We need to find the largest d for which d * 9^power has d digits.
    # 6 * 9^5 = 354294 (a 6-digit number)
    # 7 * 9^5 = 413343 (a 6-digit number, less than the smallest 7-digit number 1,000,000)
    # So, the upper bound is around 355000.
    upper_bound = (power + 1) * (9**power)

    total_sum = 0
    for i in range(10, upper_bound):
        sum_of_powers = sum(int(digit)**power for digit in str(i))
        if i == sum_of_powers:
            total_sum += i

    return total_sum
```

- `power` を引数として受け取り、指定された累乗で計算します。
- `upper_bound` を `(power + 1) * (9**power)` として、十分な大きさの探索範囲を設定します。
- `10` から `upper_bound` までループし、各数 `i` について、その桁の数字の `power` 乗の和を計算します。
- 和が `i` と等しい場合、`total_sum` に加算します。
- `1 = 1^n` は問題の定義により「和」ではないため、探索は `10` から開始します。
