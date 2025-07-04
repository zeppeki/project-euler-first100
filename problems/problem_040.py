#!/usr/bin/env python3
"""
Problem 040: Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression:
d1 × d10 × d100 × d1,000 × d10,000 × d100,000 × d1,000,000

Answer: Check Project Euler official site
"""

from .lib import get_digit_at_position


def solve_naive() -> int:
    """
    素直な解法: 文字列として数列を生成し、指定位置の文字を取得
    時間計算量: O(n) where n is the target position
    空間計算量: O(n) for storing the concatenated string
    """
    positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    max_pos = max(positions)

    champernowne = ""
    num = 1

    while len(champernowne) < max_pos:
        champernowne += str(num)
        num += 1

    result = 1
    for pos in positions:
        digit = int(champernowne[pos - 1])
        result *= digit

    return result


def solve_optimized() -> int:
    """
    最適化解法: 各位置に対応する数字を数学的に計算
    時間計算量: O(log n) for each position lookup
    空間計算量: O(1)
    """
    positions = [1, 10, 100, 1000, 10000, 100000, 1000000]

    # Use get_digit_at_position from common library

    result = 1
    for pos in positions:
        digit = get_digit_at_position(pos)
        result *= digit

    return result
