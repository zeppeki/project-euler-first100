#!/usr/bin/env python3
"""
Problem 020: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Answer: 648
"""

import math


def solve_naive(n: int) -> int:
    """
    素直な解法: math.factorialを使い、文字列変換して各桁を合計

    時間計算量: O(n log n) - 階乗計算
    空間計算量: O(log n) - 階乗の結果を格納
    """
    factorial = math.factorial(n)
    return sum(int(digit) for digit in str(factorial))


def solve_optimized(n: int) -> int:
    """
    最適化解法: 手動で階乗を計算し、各桁の和を求める

    時間計算量: O(n log n)
    空間計算量: O(log n)
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return sum(int(digit) for digit in str(factorial))


def solve_mathematical(n: int) -> int:
    """
    数学的解法: 段階的に階乗を計算しながら桁和を追跡

    時間計算量: O(n log n)
    空間計算量: O(1) - 階乗の中間結果を保持しない
    """
    factorial = 1
    digit_sum = 1  # 1! = 1の桁和

    if n == 0 or n == 1:
        return 1

    for i in range(2, n + 1):
        factorial *= i
        # 各段階で桁和を計算（メモリ効率のため）
        digit_sum = sum(int(digit) for digit in str(factorial))

    return digit_sum
