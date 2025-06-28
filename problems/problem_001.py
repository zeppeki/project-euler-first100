#!/usr/bin/env python3
"""
Problem 001: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
"""


def solve_naive(limit: int) -> int:
    """
    素直な解法: 1からlimit-1までの数を順番にチェック
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if limit <= 0:
        return 0

    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def solve_optimized(limit: int) -> int:
    """
    最適化解法: 等差数列の和の公式を使用
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if limit <= 0:
        return 0

    def sum_multiples(n: int, limit: int) -> int:
        """nの倍数の和を計算（limit未満）"""
        count = (limit - 1) // n
        return n * count * (count + 1) // 2

    # 3の倍数の和 + 5の倍数の和 - 15の倍数の和（重複を除く）
    return sum_multiples(3, limit) + sum_multiples(5, limit) - sum_multiples(15, limit)
