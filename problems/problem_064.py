#!/usr/bin/env python3
"""
Problem 064: Odd period square roots

All square roots are periodic when written as continued fractions.
For example, √23 = [4;(1,3,1,8)] where the period is (1,3,1,8) with length 4.
For N ≤ 10000, how many continued fractions for √N have an odd period?

Answer: Project Euler公式サイトで確認してください。
"""

import math


def is_perfect_square(n: int) -> bool:
    """
    Check if a number is a perfect square.

    Args:
        n: Number to check

    Returns:
        True if n is a perfect square, False otherwise
    """
    root = int(math.sqrt(n))
    return root * root == n


def get_continued_fraction_period(n: int) -> int:
    """
    Calculate the period length of the continued fraction for √n.

    Using the algorithm:
    m₀ = 0, d₀ = 1, a₀ = floor(√n)
    mₙ₊₁ = dₙ × aₙ - mₙ
    dₙ₊₁ = (n - mₙ₊₁²) / dₙ
    aₙ₊₁ = floor((a₀ + mₙ₊₁) / dₙ₊₁)

    Args:
        n: Number to find continued fraction period for

    Returns:
        Length of the period
    """
    if is_perfect_square(n):
        return 0  # Perfect squares have no periodic part

    a0 = int(math.sqrt(n))
    m, d, a = 0, 1, a0

    # Store seen states to detect period
    seen: dict[tuple[int, int], int] = {}
    period = 0

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d

        state = (m, d)
        if state in seen:
            period = len(seen) - seen[state]
            break

        seen[state] = len(seen)

    return period


def solve_naive() -> int:
    """
    素直な解法: 各無理数の平方根に対して連分数の周期を計算し、奇数周期のものを数える
    時間計算量: O(n * p) - nは上限値、pは平均周期長
    空間計算量: O(p) - 周期検出のためのハッシュマップ
    """
    count = 0
    limit = 10000

    for n in range(2, limit + 1):
        if not is_perfect_square(n):
            period_length = get_continued_fraction_period(n)
            if period_length % 2 == 1:  # 奇数周期
                count += 1

    return count


def solve_optimized() -> int:
    """
    最適化解法: 完全平方数の事前計算で効率化
    時間計算量: O(n * p) - 基本的には同じだが完全平方数チェックを高速化
    空間計算量: O(√n + p) - 完全平方数のセットと周期検出用ハッシュマップ
    """
    count = 0
    limit = 10000

    # 完全平方数のセットを事前計算
    perfect_squares = set()
    i = 1
    while i * i <= limit:
        perfect_squares.add(i * i)
        i += 1

    for n in range(2, limit + 1):
        if n not in perfect_squares:
            period_length = get_continued_fraction_period(n)
            if period_length % 2 == 1:  # 奇数周期
                count += 1

    return count


def solve_mathematical() -> int:
    """
    数学的解法: 数論的性質を利用した最適化（基本アルゴリズムは同じ）
    時間計算量: O(n * p) - 周期計算は避けられない
    空間計算量: O(√n + p) - 完全平方数のセットと周期検出用ハッシュマップ
    """
    count = 0
    limit = 10000

    # 完全平方数のセットを事前計算
    perfect_squares = set()
    i = 1
    while i * i <= limit:
        perfect_squares.add(i * i)
        i += 1

    for n in range(2, limit + 1):
        if n not in perfect_squares:
            period_length = get_continued_fraction_period(n)
            if period_length % 2 == 1:  # 奇数周期
                count += 1

    return count
