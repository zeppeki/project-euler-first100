#!/usr/bin/env python3
"""
Problem 004: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""


def is_palindrome(n: int) -> bool:
    """数値が回文かどうかを判定"""
    s = str(n)
    return s == s[::-1]


def solve_naive(min_digits: int, max_digits: int) -> tuple[int, int, int]:
    """
    素直な解法: 全ての組み合わせをチェック
    時間計算量: O(n²)
    空間計算量: O(1)
    """
    if min_digits > max_digits:
        return 0, 0, 0

    min_num = 10 ** (min_digits - 1)
    max_num = 10**max_digits - 1

    largest_palindrome = 0
    factors = (0, 0)

    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):  # j >= i to avoid duplicates
            product = i * j
            if product <= largest_palindrome:
                break  # Early termination since products will only get smaller
            if is_palindrome(product):
                largest_palindrome = product
                factors = (i, j)

    return largest_palindrome, factors[0], factors[1]


def solve_optimized(min_digits: int, max_digits: int) -> tuple[int, int, int]:
    """
    最適化解法: 上から下に向かって探索し、早期終了を活用
    時間計算量: O(n²) but with better pruning
    空間計算量: O(1)
    """
    if min_digits > max_digits:
        return 0, 0, 0

    min_num = 10 ** (min_digits - 1)
    max_num = 10**max_digits - 1

    largest_palindrome = 0
    factors = (0, 0)

    # 大きな数から小さな数に向かって探索
    for i in range(max_num, min_num - 1, -1):
        # 早期終了条件: i * max_num が現在の最大値以下なら終了
        if i * max_num <= largest_palindrome:
            break

        for j in range(min(i, max_num), min_num - 1, -1):
            product = i * j
            if product <= largest_palindrome:
                break  # 内側ループの早期終了

            if is_palindrome(product):
                largest_palindrome = product
                factors = (i, j)
                break  # 最大値を見つけたので内側ループを終了

    return largest_palindrome, factors[0], factors[1]


def solve_mathematical(min_digits: int, max_digits: int) -> tuple[int, int, int]:
    """
    数学的解法: 回文の構造を利用した最適化
    回文は特定の構造を持つため、候補を絞り込める
    時間計算量: O(n²) but with mathematical optimizations
    空間計算量: O(1)
    """
    if min_digits > max_digits:
        return 0, 0, 0

    min_num = 10 ** (min_digits - 1)
    max_num = 10**max_digits - 1

    largest_palindrome = 0
    factors = (0, 0)

    # 1桁や2桁の場合は最適化を適用せず、通常の方法を使用
    if max_digits <= 2:
        return solve_optimized(min_digits, max_digits)

    # 6桁の回文の場合: abccba = 100001*a + 10010*b + 1100*c
    # = 11 * (9091*a + 910*b + 100*c)
    # つまり、6桁の回文は必ず11で割り切れる

    for i in range(max_num, min_num - 1, -1):
        # 早期終了の最適化
        if i * max_num <= largest_palindrome:
            break

        # iが11で割り切れない場合、jは11で割り切れる必要がある
        j_start = min(i, max_num)
        j_step = 1

        if i % 11 != 0:
            # jを11の倍数に調整
            j_start = j_start - (j_start % 11)
            j_step = 11

        j = j_start
        while j >= min_num:
            product = i * j
            if product <= largest_palindrome:
                break

            if is_palindrome(product):
                largest_palindrome = product
                factors = (i, j)
                break

            j -= j_step

    return largest_palindrome, factors[0], factors[1]