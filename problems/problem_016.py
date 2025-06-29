#!/usr/bin/env python3
"""
Problem 016: Power Digit Sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Answer: 1366
"""


def solve_naive(power: int) -> int:
    """
    素直な解法
    2^powerを計算し、各桁の数字の和を求める

    時間計算量: O(power * log(2^power)) = O(power^2)
    空間計算量: O(power)
    """
    # 2^powerを計算
    result = 2**power

    # 各桁の数字の和を計算
    digit_sum = 0
    while result > 0:
        digit_sum += result % 10
        result //= 10

    return digit_sum


def solve_optimized(power: int) -> int:
    """
    最適化解法
    文字列変換を使用して桁の和を計算

    時間計算量: O(power * log(2^power)) = O(power^2)
    空間計算量: O(power)
    """
    # 2^powerを計算して文字列に変換
    result = str(2**power)

    # 各桁の数字の和を計算
    return sum(int(digit) for digit in result)
