#!/usr/bin/env python3
"""
Problem 065: Convergents of e

The continued fraction for e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]
The pattern is: [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...] where every third term (starting from the second) is 2k.

The first ten convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536

Find the sum of digits in the numerator of the 100th convergent of e.

Answer: Project Euler公式サイトで確認してください。
"""


def get_e_continued_fraction_coefficient(n: int) -> int:
    """
    Get the nth coefficient in the continued fraction of e.

    The pattern is: [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
    - a0 = 2
    - For n >= 1: if (n-1) % 3 == 1, then an = 2*((n-1)//3 + 1), else an = 1

    Args:
        n: Index of coefficient (0-based)

    Returns:
        The nth coefficient
    """
    if n == 0:
        return 2

    # For n >= 1, check if it's at position 2, 5, 8, 11, ... (every third starting from 2)
    if (n - 1) % 3 == 1:
        # This is a "2k" term where k is the sequence number
        k = (n - 1) // 3 + 1
        return 2 * k
    return 1


def compute_convergent(n: int) -> tuple[int, int]:
    """
    Compute the nth convergent of e using the standard recurrence.

    For convergents p_n/q_n:
    p_0 = a_0, q_0 = 1
    p_1 = a_1*a_0 + 1, q_1 = a_1
    p_n = a_n*p_{n-1} + p_{n-2}
    q_n = a_n*q_{n-1} + q_{n-2}

    Args:
        n: Which convergent to compute (0-based)

    Returns:
        Tuple of (numerator, denominator)
    """
    if n == 0:
        return (2, 1)

    # Initialize first two convergents
    a0 = get_e_continued_fraction_coefficient(0)  # 2
    a1 = get_e_continued_fraction_coefficient(1)  # 1

    p_prev2, q_prev2 = a0, 1  # p_0, q_0
    p_prev1, q_prev1 = a1 * a0 + 1, a1  # p_1, q_1

    if n == 1:
        return (p_prev1, q_prev1)

    # Compute convergents iteratively
    for i in range(2, n + 1):
        a_i = get_e_continued_fraction_coefficient(i)
        p_curr = a_i * p_prev1 + p_prev2
        q_curr = a_i * q_prev1 + q_prev2

        # Update for next iteration
        p_prev2, q_prev2 = p_prev1, q_prev1
        p_prev1, q_prev1 = p_curr, q_curr

    return (p_prev1, q_prev1)


def sum_of_digits(n: int) -> int:
    """
    Calculate the sum of digits in a number.

    Args:
        n: Number to sum digits for

    Returns:
        Sum of all digits
    """
    return sum(int(digit) for digit in str(n))


def solve_naive() -> int:
    """
    素直な解法: 連分数の収束分数を直接計算して100番目の分子の桁数和を求める
    時間計算量: O(n) - n番目の収束分数まで逐次計算
    空間計算量: O(1) - 前の2つの収束分数のみ保持
    """
    # Calculate the 100th convergent (0-based index, so 99)
    numerator, _ = compute_convergent(99)

    # Return sum of digits in the numerator
    return sum_of_digits(numerator)


def solve_optimized() -> int:
    """
    最適化解法: より効率的な収束分数計算（基本的には同じアルゴリズム）
    時間計算量: O(n) - 収束分数の計算は本質的にO(n)
    空間計算量: O(1) - 定数領域のみ使用
    """
    # Calculate the 100th convergent (0-based index, so 99)
    numerator, _ = compute_convergent(99)

    # Return sum of digits in the numerator
    return sum_of_digits(numerator)


def solve_mathematical() -> int:
    """
    数学的解法: eの連分数の性質を利用した最適化（基本アルゴリズムは同じ）
    時間計算量: O(n) - 連分数の収束分数計算は避けられない
    空間計算量: O(1) - 定数領域のみ使用
    """
    # Calculate the 100th convergent (0-based index, so 99)
    numerator, _ = compute_convergent(99)

    # Return sum of digits in the numerator
    return sum_of_digits(numerator)
