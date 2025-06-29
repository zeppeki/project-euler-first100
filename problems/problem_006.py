#!/usr/bin/env python3
"""
Problem 006: Sum square difference

The sum of the squares of the first ten natural numbers is:
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is: 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Answer: 25164150
"""


def solve_naive(n: int) -> int:
    """
    素直な解法: 各数値を逐次計算してそれぞれの和を求める
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0

    # 平方の和を計算: 1² + 2² + ... + n²
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_squares += i * i

    # 和の平方を計算: (1 + 2 + ... + n)²
    sum_of_numbers = 0
    for i in range(1, n + 1):
        sum_of_numbers += i
    square_of_sum = sum_of_numbers * sum_of_numbers

    # 差を返す
    return square_of_sum - sum_of_squares


def solve_optimized(n: int) -> int:
    """
    最適化解法: 数学的公式を使用した効率的計算
    和の公式: 1 + 2 + ... + n = n(n+1)/2
    平方和の公式: 1² + 2² + ... + n² = n(n+1)(2n+1)/6
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0

    # 和の公式を使用: 1 + 2 + ... + n = n(n+1)/2
    sum_of_numbers = n * (n + 1) // 2
    square_of_sum = sum_of_numbers * sum_of_numbers

    # 平方和の公式を使用: 1² + 2² + ... + n² = n(n+1)(2n+1)/6
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6

    # 差を返す
    return square_of_sum - sum_of_squares


def solve_mathematical(n: int) -> int:
    """
    数学的解法: 差の公式を直接導出して使用
    (和の平方) - (平方の和) = [n(n+1)/2]² - n(n+1)(2n+1)/6
                            = n²(n+1)²/4 - n(n+1)(2n+1)/6
                            = n(n+1)[n(n+1)/4 - (2n+1)/6]
                            = n(n+1)[3n(n+1) - 2(2n+1)]/12
                            = n(n+1)[3n² + 3n - 4n - 2]/12
                            = n(n+1)(3n² - n - 2)/12
                            = n(n+1)(n-1)(3n+2)/12
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 0  # 1の場合、和の平方も平方の和も1なので差は0

    # 導出した公式を使用: n(n+1)(n-1)(3n+2)/12
    return n * (n + 1) * (n - 1) * (3 * n + 2) // 12
