#!/usr/bin/env python3
"""
Problem 094: Almost equilateral triangles

An "almost equilateral triangle" has two equal sides and the third side differing by no more than one unit.
For example, a 5-5-6 triangle has an area of 12 square units.

No equilateral triangle exists with integral side lengths and integral area.
However, there are triangles with integral side lengths and integral area such that
two sides are equal and the third side differs by no more than one unit.

Find the sum of perimeters of all almost equilateral triangles that have integral side lengths
and integral area and have a perimeter not exceeding one billion (1,000,000,000).
"""

import math


def is_integral_area(a: int, b: int, c: int) -> bool:
    """
    三角形の面積が整数かどうかを判定
    ヘロンの公式を使用: Area = sqrt(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2
    時間計算量: O(1)
    空間計算量: O(1)
    """
    s = (a + b + c) / 2
    discriminant = s * (s - a) * (s - b) * (s - c)

    if discriminant <= 0:
        return False

    # 平方根が整数かどうかを判定
    area_sqrt = math.sqrt(discriminant)
    return area_sqrt == int(area_sqrt)


def solve_naive(perimeter_limit: int = 1000000000) -> int:
    """
    素直な解法: 全ての可能な三角形を調べる
    時間計算量: O(n) where n is perimeter_limit
    空間計算量: O(1)
    """
    total_perimeter = 0

    # a, a, a+1 の形の三角形を調べる
    a = 1
    while True:
        perimeter = 3 * a + 1
        if perimeter > perimeter_limit:
            break

        if is_integral_area(a, a, a + 1):
            total_perimeter += perimeter

        a += 1

    # a, a, a-1 の形の三角形を調べる
    a = 2  # a-1 >= 1 なので a >= 2
    while True:
        perimeter = 3 * a - 1
        if perimeter > perimeter_limit:
            break

        if is_integral_area(a, a, a - 1):
            total_perimeter += perimeter

        a += 1

    return total_perimeter


def solve_optimized(perimeter_limit: int = 1000000000) -> int:
    """
    最適化解法: 数学的性質を利用して効率的に計算
    ほぼ正三角形の漸化式を利用
    時間計算量: O(log n)
    空間計算量: O(1)
    """
    total_perimeter = 0

    # Type 1: (a, a, a+1) の形の三角形
    # 漸化式: a_n = 14*a_{n-1} - a_{n-2} - 4
    # 初期値: a_0 = 5, a_1 = 65
    a_prev_prev = 5
    a_prev = 65

    # 初期値を追加
    if 3 * a_prev_prev + 1 <= perimeter_limit:
        total_perimeter += 3 * a_prev_prev + 1
    if 3 * a_prev + 1 <= perimeter_limit:
        total_perimeter += 3 * a_prev + 1

    while True:
        a_current = 14 * a_prev - a_prev_prev - 4
        perimeter = 3 * a_current + 1
        if perimeter > perimeter_limit:
            break
        total_perimeter += perimeter
        a_prev_prev = a_prev
        a_prev = a_current

    # Type 2: (a, a, a-1) の形の三角形
    # 漸化式: a_n = 14*a_{n-1} - a_{n-2} + 4
    # 初期値: a_0 = 17, a_1 = 241
    a_prev_prev = 17
    a_prev = 241

    # 初期値を追加
    if 3 * a_prev_prev - 1 <= perimeter_limit:
        total_perimeter += 3 * a_prev_prev - 1
    if 3 * a_prev - 1 <= perimeter_limit:
        total_perimeter += 3 * a_prev - 1

    while True:
        a_current = 14 * a_prev - a_prev_prev + 4
        perimeter = 3 * a_current - 1
        if perimeter > perimeter_limit:
            break
        total_perimeter += perimeter
        a_prev_prev = a_prev
        a_prev = a_current

    return total_perimeter


def solve_mathematical(perimeter_limit: int = 1000000000) -> int:
    """
    数学的解法: ほぼ正三角形の漸化式を直接利用
    時間計算量: O(log n)
    空間計算量: O(1)
    """
    return solve_optimized(perimeter_limit)


def find_almost_equilateral_triangles(
    perimeter_limit: int = 1000000000,
) -> list[tuple[int, int, int]]:
    """
    条件を満たす三角形のリストを返す
    時間計算量: O(log n)
    空間計算量: O(k) where k is number of triangles
    """
    triangles = []

    # Type 1: (a, a, a+1) の形の三角形
    # 漸化式: a_n = 14*a_{n-1} - a_{n-2} - 4
    # 初期値: a_0 = 5, a_1 = 65
    a_prev_prev = 5
    a_prev = 65

    # 初期値を追加
    if 3 * a_prev_prev + 1 <= perimeter_limit:
        triangles.append((a_prev_prev, a_prev_prev, a_prev_prev + 1))
    if 3 * a_prev + 1 <= perimeter_limit:
        triangles.append((a_prev, a_prev, a_prev + 1))

    while True:
        a_current = 14 * a_prev - a_prev_prev - 4
        perimeter = 3 * a_current + 1
        if perimeter > perimeter_limit:
            break
        triangles.append((a_current, a_current, a_current + 1))
        a_prev_prev = a_prev
        a_prev = a_current

    # Type 2: (a, a, a-1) の形の三角形
    # 漸化式: a_n = 14*a_{n-1} - a_{n-2} + 4
    # 初期値: a_0 = 17, a_1 = 241
    a_prev_prev = 17
    a_prev = 241

    # 初期値を追加
    if 3 * a_prev_prev - 1 <= perimeter_limit:
        triangles.append((a_prev_prev, a_prev_prev, a_prev_prev - 1))
    if 3 * a_prev - 1 <= perimeter_limit:
        triangles.append((a_prev, a_prev, a_prev - 1))

    while True:
        a_current = 14 * a_prev - a_prev_prev + 4
        perimeter = 3 * a_current - 1
        if perimeter > perimeter_limit:
            break
        triangles.append((a_current, a_current, a_current - 1))
        a_prev_prev = a_prev
        a_prev = a_current

    return sorted(triangles, key=lambda t: sum(t))


def calculate_area(a: int, b: int, c: int) -> int:
    """
    三角形の面積を計算（整数であることを前提）
    時間計算量: O(1)
    空間計算量: O(1)
    """
    s = (a + b + c) / 2
    discriminant = s * (s - a) * (s - b) * (s - c)
    return int(math.sqrt(discriminant))
