#!/usr/bin/env python3
"""
Problem 073: Counting fractions in a range

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the set of reduced proper fractions for d ≤ 12,000?
"""

from math import gcd
from typing import Any


def solve_naive(limit: int) -> int:
    """
    素直な解法: すべての分数を生成して範囲内をカウント

    時間計算量: O(n²)
    空間計算量: O(1)

    Args:
        limit: 分母の上限値

    Returns:
        1/3と1/2の間の既約真分数の個数
    """
    count = 0

    for d in range(2, limit + 1):
        # 1/3 < n/d < 1/2の範囲でnを探索
        # 1/3 < n/d → n > d/3
        # n/d < 1/2 → n < d/2
        min_n = d // 3 + 1
        max_n = (d - 1) // 2 if d % 2 == 1 else d // 2 - 1

        for n in range(min_n, max_n + 1):
            # 厳密に範囲内かチェック
            if gcd(n, d) == 1 and 3 * n > d and 2 * n < d:
                count += 1

    return count


def solve_optimized(limit: int) -> int:
    """
    最適化解法: 範囲計算を最適化

    時間計算量: O(n log n)
    空間計算量: O(1)

    Args:
        limit: 分母の上限値

    Returns:
        1/3と1/2の間の既約真分数の個数
    """
    count = 0

    for d in range(2, limit + 1):
        # 1/3 < n/d < 1/2の範囲を正確に計算
        # n > d/3 and n < d/2
        min_n = d // 3 + 1
        max_n = (d - 1) // 2 if d % 2 == 1 else d // 2 - 1

        # 範囲が有効かチェック
        if min_n <= max_n:
            for n in range(min_n, max_n + 1):
                # 厳密に範囲内かチェック
                if gcd(n, d) == 1 and 3 * n > d and 2 * n < d:
                    count += 1

    return count


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: 連分数とメディアント性質を利用

    時間計算量: O(n log n)
    空間計算量: O(1)

    Args:
        limit: 分母の上限値

    Returns:
        1/3と1/2の間の既約真分数の個数
    """
    count = 0

    # 各分母について、範囲内の分数をカウント
    for d in range(2, limit + 1):
        # 1/3 < n/d < 1/2
        # d/3 < n < d/2

        # 最小の分子: floor(d/3) + 1
        min_n = d // 3 + 1

        # 最大の分子: floor(d/2) - 1 (if d is even) or floor(d/2) (if d is odd)
        max_n = d // 2 - 1 if d % 2 == 0 else d // 2

        # 範囲が有効な場合のみ処理
        if min_n <= max_n:
            for n in range(min_n, max_n + 1):
                # 既約分数かチェック (数値誤差を避けるため整数演算)
                if gcd(n, d) == 1 and 3 * n > d and 2 * n < d:
                    count += 1

    return count


def count_fractions_in_range(
    limit: int, lower_num: int, lower_den: int, upper_num: int, upper_den: int
) -> int:
    """
    指定された範囲内の既約真分数の個数をカウント

    Args:
        limit: 分母の上限値
        lower_num: 下限分数の分子
        lower_den: 下限分数の分母
        upper_num: 上限分数の分子
        upper_den: 上限分数の分母

    Returns:
        指定範囲内の既約真分数の個数
    """
    count = 0

    for d in range(2, limit + 1):
        # lower_num/lower_den < n/d < upper_num/upper_den
        # lower_num * d < n * lower_den
        # upper_num * d > n * upper_den

        min_n = (lower_num * d) // lower_den + 1
        max_n = (upper_num * d - 1) // upper_den

        if min_n <= max_n:
            for n in range(min_n, max_n + 1):
                # 厳密に範囲内かチェック
                if (
                    gcd(n, d) == 1
                    and lower_num * d < n * lower_den
                    and n * upper_den < upper_num * d
                ):
                    count += 1

    return count


def analyze_fraction_distribution(limit: int) -> dict[str, Any]:
    """
    分数の分布を分析

    Args:
        limit: 分母の上限値

    Returns:
        分析結果の辞書
    """
    total_count = 0
    denominator_counts = {}
    fraction_values = []

    for d in range(2, limit + 1):
        d_count = 0
        min_n = d // 3 + 1
        max_n = (d - 1) // 2 if d % 2 == 1 else d // 2 - 1

        if min_n <= max_n:
            for n in range(min_n, max_n + 1):
                if gcd(n, d) == 1 and 3 * n > d and 2 * n < d:
                    d_count += 1
                    total_count += 1
                    fraction_values.append(n / d)

        if d_count > 0:
            denominator_counts[d] = d_count

    return {
        "total_count": total_count,
        "denominator_counts": denominator_counts,
        "fraction_values": sorted(fraction_values),
        "min_value": min(fraction_values) if fraction_values else 0,
        "max_value": max(fraction_values) if fraction_values else 0,
        "avg_value": sum(fraction_values) / len(fraction_values)
        if fraction_values
        else 0,
    }


def get_fractions_by_denominator(limit: int) -> dict[int, list[tuple[int, int]]]:
    """
    分母ごとの分数リストを取得

    Args:
        limit: 分母の上限値

    Returns:
        分母をキーとした分数リストの辞書
    """
    result = {}

    for d in range(2, limit + 1):
        fractions = []
        min_n = d // 3 + 1
        max_n = (d - 1) // 2 if d % 2 == 1 else d // 2 - 1

        if min_n <= max_n:
            for n in range(min_n, max_n + 1):
                if gcd(n, d) == 1 and 3 * n > d and 2 * n < d:
                    fractions.append((n, d))

        if fractions:
            result[d] = fractions

    return result


def find_closest_fractions(
    limit: int,
) -> tuple[tuple[int, int] | None, tuple[int, int] | None]:
    """
    1/3と1/2に最も近い分数を見つける

    Args:
        limit: 分母の上限値

    Returns:
        (1/3に最も近い分数, 1/2に最も近い分数)
    """
    closest_to_third = None
    closest_to_half = None
    min_diff_third = float("inf")
    min_diff_half = float("inf")

    for d in range(2, limit + 1):
        min_n = d // 3 + 1
        max_n = (d - 1) // 2 if d % 2 == 1 else d // 2 - 1

        if min_n <= max_n:
            for n in range(min_n, max_n + 1):
                if gcd(n, d) == 1 and 3 * n > d and 2 * n < d:
                    fraction_value = n / d

                    # 1/3との差
                    diff_third = fraction_value - 1 / 3
                    if diff_third > 0 and diff_third < min_diff_third:
                        min_diff_third = diff_third
                        closest_to_third = (n, d)

                    # 1/2との差
                    diff_half = 1 / 2 - fraction_value
                    if diff_half > 0 and diff_half < min_diff_half:
                        min_diff_half = diff_half
                        closest_to_half = (n, d)

    return closest_to_third, closest_to_half
