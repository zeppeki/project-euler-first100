#!/usr/bin/env python3
"""
Problem 063: Powerful digit counts

The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?

Answer: Project Euler公式サイトで確認してください。
"""

import math


def count_digits(n: int) -> int:
    """
    Count the number of digits in a number.

    Args:
        n: Number to count digits for

    Returns:
        Number of digits
    """
    if n == 0:
        return 1
    return len(str(n))


def solve_naive() -> int:
    """
    素直な解法: 全ての底と指数の組み合わせをチェックして条件を満たすものを数える
    時間計算量: O(n * m) - nは最大指数、mは最大底
    空間計算量: O(1) - 定数領域のみ使用
    """
    count = 0

    # For each possible power n
    for n in range(1, 100):  # 100は十分大きな上限値
        # For each possible base
        for base in range(1, 100):  # 100は十分大きな上限値
            power = base**n
            digits = count_digits(power)

            if digits == n:
                count += 1
            elif digits > n:
                # 桁数がnを超えたら、それ以上大きい底では条件を満たさない
                break

    return count


def solve_optimized() -> int:
    """
    最適化解法: 数学的な上限を使って探索範囲を制限
    時間計算量: O(n * log(10)) - より効率的な範囲探索
    空間計算量: O(1) - 定数領域のみ使用
    """
    count = 0

    # For each possible power n
    for n in range(1, 100):  # 100は十分大きな上限値
        # n桁の数の範囲: 10^(n-1) <= base^n < 10^n
        # これから: 10^((n-1)/n) <= base < 10^(n/n) = 10
        # 数学的に、base >= 10の場合、base^n は必ずn桁を超える

        min_base = math.ceil(10 ** ((n - 1) / n))
        max_base = 10  # base が 10 以上だと base^n は n+1 桁以上になる

        for base in range(min_base, max_base):
            power = base**n
            digits = count_digits(power)

            if digits == n:
                count += 1
            elif digits > n:
                break

    return count


def solve_mathematical() -> int:
    """
    数学的解法: より厳密な数学的条件を使用
    時間計算量: O(n) - 各nに対して有効な底の範囲を直接計算
    空間計算量: O(1) - 定数領域のみ使用
    """
    count = 0

    # n桁のn乗の条件: 10^(n-1) <= base^n < 10^n
    # log10(10^(n-1)) <= n*log10(base) < log10(10^n)
    # (n-1) <= n*log10(base) < n
    # (n-1)/n <= log10(base) < 1
    # 10^((n-1)/n) <= base < 10

    for n in range(1, 22):  # n=22以上では条件を満たす整数底が存在しない
        min_base_float = 10 ** ((n - 1) / n)
        max_base = 9  # base=10では10^n はn+1桁になる

        # 有効な底の範囲を整数で計算
        min_base = max(1, math.ceil(min_base_float))

        for base in range(min_base, max_base + 1):
            power = base**n

            # n桁であることを確認
            if 10 ** (n - 1) <= power < 10**n:
                count += 1

    return count
