#!/usr/bin/env python3
"""
Problem 034: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

Answer: 40730
"""

import math


def factorial(n: int) -> int:
    """
    階乗を計算
    時間計算量: O(1) - math.factorialを使用
    空間計算量: O(1)
    """
    return math.factorial(n)


def digit_factorial_sum(number: int) -> int:
    """
    数字の各桁の階乗の和を計算
    時間計算量: O(log n) - 数字の桁数に比例
    空間計算量: O(1)
    """
    if number == 0:
        return factorial(0)  # 0! = 1

    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10
    return total


def is_digit_factorial(number: int) -> bool:
    """
    数字が桁階乗数かどうか判定
    時間計算量: O(log n)
    空間計算量: O(1)
    """
    return number == digit_factorial_sum(number)


def solve_naive() -> int:
    """
    素直な解法: 上限まで全ての数をチェック
    時間計算量: O(n * log n) - nは上限値
    空間計算量: O(k) - kは見つかった数の個数
    """
    # 上限の数学的分析:
    # 9! = 362,880なので、7桁の数字でも最大7 * 9! = 2,540,160
    # 8桁の数字だと最大8 * 9! = 2,903,040 < 10,000,000
    # よって7桁までで十分
    upper_limit = 7 * factorial(9)

    digit_factorials = []

    # 1! = 1, 2! = 2は和ではないので除外
    for number in range(3, upper_limit + 1):
        if is_digit_factorial(number):
            digit_factorials.append(number)

    return sum(digit_factorials)


def solve_optimized() -> int:
    """
    最適化解法: より効率的な上限設定と最適化
    時間計算量: O(n * log n) - より小さなnで探索
    空間計算量: O(k) - kは見つかった数の個数
    """
    # より厳密な上限分析:
    # d桁の数の最大値: 10^d - 1
    # d桁の階乗和の最大値: d * 9!
    # d桁の数がd * 9!を超える最小のdを求める

    def find_upper_bound() -> int:
        for d in range(1, 10):
            max_number = 10**d - 1
            max_factorial_sum = d * factorial(9)
            if max_number > max_factorial_sum:
                return max_factorial_sum
        return 7 * factorial(9)  # fallback

    upper_limit = find_upper_bound()
    digit_factorials = []

    # 事前計算した階乗テーブルを使用
    fact_table = [factorial(i) for i in range(10)]

    def digit_factorial_sum_optimized(number: int) -> int:
        total = 0
        temp = number
        while temp > 0:
            digit = temp % 10
            total += fact_table[digit]
            temp //= 10
        return total

    for number in range(3, upper_limit + 1):
        if number == digit_factorial_sum_optimized(number):
            digit_factorials.append(number)

    return sum(digit_factorials)


def solve_mathematical() -> int:
    """
    数学的解法: 数学的性質を利用した最適化
    時間計算量: O(n) - より効率的な探索
    空間計算量: O(1)
    """
    # 数学的分析による上限設定
    # d桁の最大値が d * 9! を超える最初の桁数で打ち切り

    # 階乗テーブルの事前計算
    factorials = [math.factorial(i) for i in range(10)]

    # 上限の計算: d桁の数の最大値 vs d * 9!
    upper_limit = 0
    for d in range(1, 8):
        max_d_digit = 10**d - 1
        max_factorial_sum = d * factorials[9]
        if max_d_digit > max_factorial_sum:
            upper_limit = max_factorial_sum
            break

    if upper_limit == 0:
        upper_limit = 2540160  # 7 * 9!

    total_sum = 0

    # 最適化された桁階乗和計算
    def fast_digit_factorial_sum(n: int) -> int:
        result = 0
        while n > 0:
            result += factorials[n % 10]
            n //= 10
        return result

    # 3から上限まで検索（1!, 2!は除外）
    for number in range(3, upper_limit + 1):
        if number == fast_digit_factorial_sum(number):
            total_sum += number

    return total_sum


def get_digit_factorials() -> list[int]:
    """
    桁階乗数のリストを取得（デバッグ用）
    """
    factorials = [math.factorial(i) for i in range(10)]
    upper_limit = 7 * factorials[9]  # 2,540,160

    def fast_digit_factorial_sum(n: int) -> int:
        result = 0
        while n > 0:
            result += factorials[n % 10]
            n //= 10
        return result

    digit_factorials = []
    for number in range(3, upper_limit + 1):
        if number == fast_digit_factorial_sum(number):
            digit_factorials.append(number)

    return digit_factorials


def verify_examples() -> bool:
    """
    問題の例を検証
    """
    # 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
    example = 145
    expected_sum = factorial(1) + factorial(4) + factorial(5)
    calculated_sum = digit_factorial_sum(example)

    return expected_sum == 145 and calculated_sum == 145 and is_digit_factorial(example)
