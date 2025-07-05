#!/usr/bin/env python3
"""
Problem 066: Diophantine equation

Find the value of D ≤ 1000 in the Diophantine equation x² - Dy² = 1
that has the largest minimal solution x.

Note: Perfect squares are excluded as they have no solutions.

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


def get_continued_fraction_period(n: int) -> tuple[int, list[int]]:
    """
    Get the continued fraction representation of √n.

    Args:
        n: Number to find continued fraction for

    Returns:
        Tuple of (a0, period) where a0 is the integer part and period is the repeating sequence
    """
    if is_perfect_square(n):
        return (int(math.sqrt(n)), [])

    a0 = int(math.sqrt(n))
    m, d, a = 0, 1, a0

    # Store seen states to detect period
    seen: dict[tuple[int, int], int] = {}
    period: list[int] = []

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d

        state = (m, d)
        if state in seen:
            break

        seen[state] = len(period)
        period.append(a)

    return (a0, period)


def solve_pell_equation(d: int) -> tuple[int, int]:
    """
    Solve the Pell equation x² - dy² = 1 for the minimal positive solution.

    Uses continued fractions to find the fundamental solution.

    Args:
        d: The parameter D in the Pell equation

    Returns:
        Tuple of (x, y) for the minimal solution
    """
    if is_perfect_square(d):
        return (0, 0)  # No solution for perfect squares

    a0, period = get_continued_fraction_period(d)

    # The period length determines when we find the solution
    period_length = len(period)

    # Start with the continued fraction convergents
    h_prev2, h_prev1 = 1, a0
    k_prev2, k_prev1 = 0, 1

    # Check if the first convergent is already a solution
    if h_prev1 * h_prev1 - d * k_prev1 * k_prev1 == 1:
        return (h_prev1, k_prev1)

    # Continue with the periodic part
    for i in range(period_length):
        a = period[i]
        h_curr = a * h_prev1 + h_prev2
        k_curr = a * k_prev1 + k_prev2

        # Check if this is a solution
        if h_curr * h_curr - d * k_curr * k_curr == 1:
            return (h_curr, k_curr)

        h_prev2, h_prev1 = h_prev1, h_curr
        k_prev2, k_prev1 = k_prev1, k_curr

    # If period length is even, we need to go through the period once more
    for i in range(period_length):
        a = period[i]
        h_curr = a * h_prev1 + h_prev2
        k_curr = a * k_prev1 + k_prev2

        # Check if this is a solution
        if h_curr * h_curr - d * k_curr * k_curr == 1:
            return (h_curr, k_curr)

        h_prev2, h_prev1 = h_prev1, h_curr
        k_prev2, k_prev1 = k_prev1, k_curr

    # This shouldn't happen for a valid Pell equation
    return (h_prev1, k_prev1)


def solve_naive() -> int:
    """
    素直な解法: 各D値について最小解を求め、最大のxを持つDを見つける
    時間計算量: O(n * p) - nは上限値、pは平均周期長
    空間計算量: O(p) - 周期検出のためのハッシュマップ
    """
    max_x = 0
    result_d = 0

    for d in range(2, 1001):
        if not is_perfect_square(d):
            x, y = solve_pell_equation(d)
            if x > max_x:
                max_x = x
                result_d = d

    return result_d


def solve_optimized() -> int:
    """
    最適化解法: 完全平方数の事前計算で効率化
    時間計算量: O(n * p) - 基本的には同じだが完全平方数チェックを高速化
    空間計算量: O(√n + p) - 完全平方数のセットと周期検出用ハッシュマップ
    """
    max_x = 0
    result_d = 0

    # 完全平方数のセットを事前計算
    perfect_squares = set()
    i = 1
    while i * i <= 1000:
        perfect_squares.add(i * i)
        i += 1

    for d in range(2, 1001):
        if d not in perfect_squares:
            x, y = solve_pell_equation(d)
            if x > max_x:
                max_x = x
                result_d = d

    return result_d


def solve_mathematical() -> int:
    """
    数学的解法: 連分数の性質を利用した最適化（基本アルゴリズムは同じ）
    時間計算量: O(n * p) - Pell方程式の解法は避けられない
    空間計算量: O(√n + p) - 完全平方数のセットと周期検出用ハッシュマップ
    """
    # この問題では数学的ショートカットは限定的なので、optimizedと同じ実装
    return solve_optimized()
