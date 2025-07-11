# Problem 092: Square digit chains

## 問題文

数字チェーンは、数の各桁の二乗を足し合わせて新しい数を作り、以前に現れた数になるまで繰り返すことで作られます。

例えば：
- 44 → 32 → 13 → 10 → 1 → 1
- 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

したがって、1または89に到達するチェーンは無限ループに陥ります。
最も驚くべきことは、すべての開始数が最終的に1または89のいずれかに到達することです。

1000万未満の開始数のうち、89に到達するものはいくつあるでしょうか？

## 解法

### アプローチ1: 素直な解法 (O(n × k × log d))

各数について個別にチェーンをたどり、最終的な到達点を確認します。

```python
def solve_naive(limit: int = 10000000) -> int:
    count = 0
    for i in range(1, limit):
        if get_chain_destination(i) == 89:
            count += 1
    return count
```

### アプローチ2: 最適化解法 (O(n + k × log d))

メモ化を使用して、一度計算した結果を再利用します。

```python
def solve_optimized(limit: int = 10000000) -> int:
    memo = {}
    count = 0

    def get_destination_memoized(n: int) -> int:
        if n in memo:
            return memo[n]

        original = n
        path = []

        while n not in memo and n != 1 and n != 89:
            path.append(n)
            n = square_digit_sum(n)

        if n in memo:
            destination = memo[n]
        else:
            destination = n

        for num in path:
            memo[num] = destination
        memo[original] = destination

        return destination

    for i in range(1, limit):
        if get_destination_memoized(i) == 89:
            count += 1

    return count
```

### アプローチ3: 数学的解法 (O(s + n))

桁の二乗和の可能な値は限られていることを利用します。

```python
def solve_mathematical(limit: int = 10000000) -> int:
    max_digits = len(str(limit - 1))
    max_square_sum = max_digits * 81  # 9^2 = 81

    destinations = {}

    def get_destination_cached(n: int) -> int:
        if n in destinations:
            return destinations[n]

        original = n
        while n not in destinations and n != 1 and n != 89:
            n = square_digit_sum(n)

        if n in destinations:
            result = destinations[n]
        else:
            result = n

        destinations[original] = result
        return result

    for i in range(1, max_square_sum + 1):
        get_destination_cached(i)

    count = 0
    for i in range(1, limit):
        square_sum = square_digit_sum(i)
        if destinations[square_sum] == 89:
            count += 1

    return count
```

## 重要な洞察

1. **チェーンの性質**: すべての正の整数は最終的に1または89に到達します。

2. **桁の二乗和の制約**: n桁の数の桁の二乗和の最大値は n × 81 です。これは比較的小さな値で、多くの異なる数が同じ二乗和を持ちます。

3. **メモ化の効果**: 計算済みの結果を再利用することで、大幅な高速化が可能です。

4. **分布の特徴**: 1000万未満の数のうち約85.8%が89に到達します。

## パフォーマンス分析

- **素直な解法**: O(n × k × log d) - 各数について個別計算
- **最適化解法**: O(n + k × log d) - メモ化による高速化
- **数学的解法**: O(s + n) - 桁の二乗和の性質を利用

ここで：
- n: 制限値（1000万）
- k: 平均チェーン長
- d: 桁数
- s: 可能な桁の二乗和の数（最大 7 × 81 = 567）

## 検証

小さな例での検証：
- 100未満: 80個の数が89に到達
- 1000未満: 857個の数が89に到達
- 10000未満: 8558個の数が89に到達

## 解答

Project Euler公式サイトで確認してください。

## 実装のポイント

1. **桁の二乗和計算**: 効率的な桁分解アルゴリズム
2. **チェーン追跡**: 無限ループの検出と処理
3. **メモ化戦略**: 計算済み結果の効果的な再利用
4. **数学的最適化**: 問題の性質を活用した効率化

この問題は、動的プログラミングとメモ化の効果を実感できる良い例です。
