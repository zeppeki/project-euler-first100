#!/usr/bin/env python3
"""
Problem 023: Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by
analysis even though it is known that the greatest number that cannot be expressed as the sum
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Answer: 4179871
"""


def get_divisor_sum(n: int) -> int:
    """
    nの真の約数の和を計算する
    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n <= 1:
        return 0

    divisor_sum = 1  # 1は常に真の約数
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisor_sum += i
            # i != n//iの場合のみ、n//iも追加
            if i != n // i:
                divisor_sum += n // i
        i += 1
    return divisor_sum


def is_abundant(n: int) -> bool:
    """
    nが過剰数かどうかを判定
    時間計算量: O(√n)
    空間計算量: O(1)
    """
    return get_divisor_sum(n) > n


def solve_naive(limit: int = 28123) -> int:
    """
    素直な解法: 各数について過剰数の和で表せるかを直接チェック
    時間計算量: O(n² × √n)
    空間計算量: O(n)
    """
    # 過剰数を収集
    abundant_numbers = []
    for i in range(1, limit + 1):
        if is_abundant(i):
            abundant_numbers.append(i)

    # 過剰数の和で表せる数をマーク
    can_be_sum = set()
    for i, a in enumerate(abundant_numbers):
        for j in range(i, len(abundant_numbers)):
            b = abundant_numbers[j]
            sum_ab = a + b
            if sum_ab <= limit:
                can_be_sum.add(sum_ab)
            else:
                break  # bが大きくなると全てlimitを超える

    # 表せない数の合計を計算
    total = 0
    for i in range(1, limit + 1):
        if i not in can_be_sum:
            total += i

    return total


def solve_optimized(limit: int = 28123) -> int:
    """
    最適化解法: フラグ配列を使用して効率化
    時間計算量: O(n × √n + A²) where A is number of abundant numbers
    空間計算量: O(n)
    """
    # 過剰数判定の前計算（約数和をキャッシュ）
    divisor_sums = [0] * (limit + 1)
    for i in range(1, limit + 1):
        divisor_sums[i] = get_divisor_sum(i)

    # 過剰数を収集
    abundant_numbers = []
    for i in range(1, limit + 1):
        if divisor_sums[i] > i:
            abundant_numbers.append(i)

    # フラグ配列で過剰数の和を効率的にマーク
    can_be_sum = [False] * (limit + 1)
    for i, a in enumerate(abundant_numbers):
        for j in range(i, len(abundant_numbers)):
            b = abundant_numbers[j]
            sum_ab = a + b
            if sum_ab <= limit:
                can_be_sum[sum_ab] = True
            else:
                break

    # 表せない数の合計を計算
    total = 0
    for i in range(1, limit + 1):
        if not can_be_sum[i]:
            total += i

    return total
