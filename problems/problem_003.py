#!/usr/bin/env python3
"""
Problem 003: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Answer: 6857
"""

import math


def solve_naive(n: int) -> int:
    """
    素直な解法: 2から順番に試し割り

    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0

    if n == 1:
        return 1

    largest_factor = 1

    # 2で割り切れるだけ割る
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # 奇数の約数を試す
    for i in range(3, n + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i
        if n == 1:
            break

    return largest_factor


def solve_optimized(n: int) -> int:
    """
    最適化解法: 平方根まで試し割り

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0

    if n == 1:
        return 1

    largest_factor = 1

    # 2で割り切れるだけ割る
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # 奇数の約数を平方根まで試す
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i

    # nが1より大きい場合、n自体が素数
    if n > 1:
        largest_factor = n

    return largest_factor
