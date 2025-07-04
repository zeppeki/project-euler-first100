#!/usr/bin/env python3
"""
Problem 021: Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Answer: 31626
"""

from .lib import get_proper_divisors_sum

# 関数名のエイリアス
get_proper_divisors_naive = get_proper_divisors_sum
get_proper_divisors_optimized = get_proper_divisors_sum


def solve_naive(limit: int) -> int:
    """
    素直な解法: 各数について真約数の和を計算し友愛数を判定

    時間計算量: O(n²)
    空間計算量: O(1)
    """
    amicable_sum = 0

    for a in range(2, limit):
        b = get_proper_divisors_naive(a)
        # 友愛数の条件をチェック
        if a != b and b < limit and get_proper_divisors_naive(b) == a:
            amicable_sum += a

    return amicable_sum


def solve_optimized(limit: int) -> int:
    """
    最適化解法: 効率的な約数計算を使用

    時間計算量: O(n√n)
    空間計算量: O(1)
    """
    amicable_sum = 0

    for a in range(2, limit):
        b = get_proper_divisors_optimized(a)
        # 友愛数の条件をチェック
        if a != b and b < limit and get_proper_divisors_optimized(b) == a:
            amicable_sum += a

    return amicable_sum


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: 事前計算で全ての真約数の和をキャッシュ

    時間計算量: O(n√n)
    空間計算量: O(n)
    """
    # 全ての数の真約数の和を事前計算
    divisor_sums = [0] * limit

    # エラトステネスの篩的アプローチで効率的に計算
    for i in range(1, limit):
        # iを約数として持つ全ての数に加算
        for j in range(2 * i, limit, i):
            divisor_sums[j] += i

    # 友愛数を探索
    amicable_numbers: set[int] = set()

    for a in range(2, limit):
        b = divisor_sums[a]
        # 友愛数の条件をチェック
        if a != b and b < limit and divisor_sums[b] == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)

    return sum(amicable_numbers)


def find_amicable_pairs(limit: int) -> list[tuple[int, int]]:
    """
    指定した範囲内の友愛数ペアを全て取得

    Args:
        limit: 探索範囲の上限

    Returns:
        友愛数ペアのリスト
    """
    pairs = []
    found = set()

    for a in range(2, limit):
        if a in found:
            continue

        b = get_proper_divisors_optimized(a)
        if a != b and b < limit and get_proper_divisors_optimized(b) == a:
            pairs.append((a, b))
            found.add(a)
            found.add(b)

    return pairs


def validate_amicable_pair(a: int, b: int) -> bool:
    """
    友愛数ペアの検証

    Args:
        a, b: 検証する数のペア

    Returns:
        友愛数ペアの場合True
    """
    return (
        a != b
        and get_proper_divisors_optimized(a) == b
        and get_proper_divisors_optimized(b) == a
    )
