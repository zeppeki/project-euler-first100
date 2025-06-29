#!/usr/bin/env python3
"""
Problem 015: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Answer: 137846528820
"""

import math


def solve_naive(n: int) -> int:
    """
    素直な解法: 動的プログラミングで各点までの経路数を計算
    時間計算量: O(n²)
    空間計算量: O(n²)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1

    # (n+1) × (n+1) のグリッドを作成
    grid = [[0] * (n + 1) for _ in range(n + 1)]

    # 上端と左端の経路数は全て1
    for i in range(n + 1):
        grid[0][i] = 1  # 上端
        grid[i][0] = 1  # 左端

    # 各点までの経路数を計算
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[n][n]


def solve_optimized(n: int) -> int:
    """
    最適化解法: 動的プログラミングで空間効率を向上
    時間計算量: O(n²)
    空間計算量: O(n)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1

    # 1次元配列で空間効率を向上
    prev_row = [1] * (n + 1)

    for _ in range(1, n + 1):
        curr_row = [1] * (n + 1)
        for j in range(1, n + 1):
            curr_row[j] = prev_row[j] + curr_row[j - 1]
        prev_row = curr_row

    return prev_row[n]


def solve_mathematical(n: int) -> int:
    """
    数学的解法: 組み合わせ論を使用した直接計算
    n×nグリッドの経路数は C(2n, n) = (2n)! / (n! * n!)
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1

    # C(2n, n) = (2n)! / (n! * n!)
    # 効率的な計算のため、C(2n, n) = (2n * (2n-1) * ... * (n+1)) / (n * (n-1) * ... * 1)
    result = 1
    for i in range(n):
        result = result * (2 * n - i) // (i + 1)

    return result


def solve_mathematical_factorial(n: int) -> int:
    """
    数学的解法: 階乗を使用した直接計算（参考実装）
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1

    return math.factorial(2 * n) // (math.factorial(n) * math.factorial(n))
