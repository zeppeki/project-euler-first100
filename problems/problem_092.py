#!/usr/bin/env python3
"""
Problem 092: Square digit chains

A number chain is created by continuously adding the square of the digits in a number to form a new number
until it has been seen before.

For example:
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""


def square_digit_sum(n: int) -> int:
    """
    各桁の二乗の和を計算
    時間計算量: O(log n)
    空間計算量: O(1)
    """
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


def get_chain_destination(n: int) -> int:
    """
    数字nから始まる連鎖の最終的な到達点(1または89)を返す
    時間計算量: O(k log n) where k is chain length
    空間計算量: O(1)
    """
    while n != 1 and n != 89:
        n = square_digit_sum(n)
    return n


def solve_naive(limit: int = 10000000) -> int:
    """
    素直な解法: 各数字について個別に連鎖をたどる
    時間計算量: O(n * k * log d) where k is average chain length, d is digits
    空間計算量: O(1)
    """
    count = 0
    for i in range(1, limit):
        if get_chain_destination(i) == 89:
            count += 1
    return count


def solve_optimized(limit: int = 10000000) -> int:
    """
    最適化解法: メモ化を使用して計算済みの結果を再利用
    時間計算量: O(n + k * log d) where k is unique chains
    空間計算量: O(k)
    """
    memo: dict[int, int] = {}
    count = 0

    def get_destination_memoized(n: int) -> int:
        if n in memo:
            return memo[n]

        original = n
        path = []

        # チェーンをたどって既知の値に到達するまで
        while n not in memo and n != 1 and n != 89:
            path.append(n)
            n = square_digit_sum(n)

        # 最終的な到達点を決定
        destination = memo.get(n, n)  # 1 or 89

        # パス上の全ての値をメモ化
        for num in path:
            memo[num] = destination
        memo[original] = destination

        return destination

    for i in range(1, limit):
        if get_destination_memoized(i) == 89:
            count += 1

    return count


def solve_mathematical(limit: int = 10000000) -> int:
    """
    数学的解法: 桁の二乗和の可能な値は限られることを利用
    時間計算量: O(s + n) where s is number of possible square sums
    空間計算量: O(s)
    """
    # 最大桁数を計算
    max_digits = len(str(limit - 1))

    # 可能な桁の二乗和の最大値 (全ての桁が9の場合)
    max_square_sum = max_digits * 81  # 9^2 = 81

    # 各桁の二乗和の値について、最終的な到達点をメモ化
    destinations: dict[int, int] = {}

    def get_destination_cached(n: int) -> int:
        if n in destinations:
            return destinations[n]

        original = n
        while n not in destinations and n != 1 and n != 89:
            n = square_digit_sum(n)

        result = destinations.get(n, n)  # 1 or 89

        destinations[original] = result
        return result

    # 1からmax_square_sumまでの各値について到達点を計算
    for i in range(1, max_square_sum + 1):
        get_destination_cached(i)

    count = 0
    for i in range(1, limit):
        square_sum = square_digit_sum(i)
        if destinations[square_sum] == 89:
            count += 1

    return count
