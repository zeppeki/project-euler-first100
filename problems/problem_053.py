#!/usr/bin/env python3
"""
Project Euler Problem 053: Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, this is written as C(5,3) = 10.

In general, C(n,r) = n! / (r!(n-r)!), where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: C(23,10) = 1144066.

How many, not necessarily distinct, values of C(n,r) for 1 ≤ n ≤ 100, are greater than one-million?
"""

import math
from typing import Any

from .lib import combination_formula

# combination_optimized のエイリアス
from .lib import combination_formula as combination_optimized


def combination_math_lib(n: int, r: int) -> int:
    """数学ライブラリを使った組み合わせ計算"""
    if r < 0 or r > n or n < 0:
        return 0
    return math.comb(n, r)


def solve_naive(max_n: int = 100, threshold: int = 1000000) -> int:
    """
    素直な解法: 全てのC(n,r)を計算して閾値を超える数を数える

    Args:
        max_n: nの最大値
        threshold: 閾値

    Returns:
        閾値を超えるC(n,r)の個数

    時間計算量: O(n^3)
    空間計算量: O(1)
    """
    count = 0

    for n in range(1, max_n + 1):
        for r in range(n + 1):
            if combination_formula(n, r) > threshold:
                count += 1

    return count


def solve_optimized(max_n: int = 100, threshold: int = 1000000) -> int:
    """
    最適化解法: 効率的な組み合わせ計算を使用

    Args:
        max_n: nの最大値
        threshold: 閾値

    Returns:
        閾値を超えるC(n,r)の個数

    時間計算量: O(n^2)
    空間計算量: O(1)
    """
    count = 0

    for n in range(1, max_n + 1):
        for r in range(n + 1):
            if combination_optimized(n, r) > threshold:
                count += 1

    return count


def solve_mathematical(max_n: int = 100, threshold: int = 1000000) -> int:
    """
    数学的解法: 対称性と数学ライブラリを活用

    Args:
        max_n: nの最大値
        threshold: 閾値

    Returns:
        閾値を超えるC(n,r)の個数

    時間計算量: O(n^2)
    空間計算量: O(1)
    """
    count = 0

    for n in range(1, max_n + 1):
        for r in range(n + 1):
            if combination_math_lib(n, r) > threshold:
                count += 1

    return count


def find_first_exceeding_threshold(threshold: int = 1000000) -> tuple[int, int, int]:
    """
    閾値を最初に超えるC(n,r)を見つける

    Args:
        threshold: 閾値

    Returns:
        (n, r, C(n,r)) のタプル
    """
    for n in range(1, 101):
        for r in range(n + 1):
            value = combination_optimized(n, r)
            if value > threshold:
                return n, r, value

    return -1, -1, -1


def get_combinations_above_threshold(
    max_n: int = 100, threshold: int = 1000000
) -> list[tuple[int, int, int]]:
    """
    閾値を超える全てのC(n,r)を取得

    Args:
        max_n: nの最大値
        threshold: 閾値

    Returns:
        (n, r, C(n,r)) のリスト
    """
    results = []

    for n in range(1, max_n + 1):
        for r in range(n + 1):
            value = combination_optimized(n, r)
            if value > threshold:
                results.append((n, r, value))

    return results


def analyze_combinatorial_values(max_n: int = 100) -> dict[str, Any]:
    """
    組み合わせ値の分析

    Args:
        max_n: nの最大値

    Returns:
        分析結果の辞書
    """
    total_values = 0
    max_value = 0
    max_position = (0, 0)
    threshold_count = 0
    threshold = 1000000

    for n in range(1, max_n + 1):
        for r in range(n + 1):
            value = combination_optimized(n, r)
            total_values += 1

            if value > max_value:
                max_value = value
                max_position = (n, r)

            if value > threshold:
                threshold_count += 1

    return {
        "total_values": total_values,
        "max_value": max_value,
        "max_position": max_position,
        "threshold_count": threshold_count,
        "threshold": threshold,
    }


def pascal_triangle_row(n: int) -> list[int]:
    """
    パスカルの三角形のn行目を生成

    Args:
        n: 行番号（0から開始）

    Returns:
        n行目の値のリスト
    """
    if n < 0:
        return []

    row = [1]
    for r in range(1, n + 1):
        row.append(combination_optimized(n, r))

    return row


def demonstrate_symmetry() -> list[tuple[int, list[int]]]:
    """
    組み合わせの対称性をデモンストレーション

    Returns:
        小さなnでのパスカルの三角形
    """
    results = []
    for n in range(11):
        row = pascal_triangle_row(n)
        results.append((n, row))

    return results
