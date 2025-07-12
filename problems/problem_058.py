#!/usr/bin/env python3
"""
Project Euler Problem 058: Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more
interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
"""

from problems.lib.primes import is_prime


def get_diagonal_values(side_length: int) -> list[int]:
    """
    指定された辺の長さのスパイラルの対角線上の値を取得
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if side_length == 1:
        return [1]

    # 辺の長さが奇数でない場合は空のリストを返す
    if side_length % 2 == 0:
        return []

    # 対角線の値を計算
    # 右下の角から反時計回りに: 右下、右上、左上、左下
    diagonal_values = []

    # 最外層の対角線の値を計算
    # 右下の角 (n²)
    bottom_right = side_length * side_length
    diagonal_values.append(bottom_right)

    # 右上の角 (n² - (n-1))
    top_right = bottom_right - (side_length - 1)
    diagonal_values.append(top_right)

    # 左上の角 (n² - 2*(n-1))
    top_left = bottom_right - 2 * (side_length - 1)
    diagonal_values.append(top_left)

    # 左下の角 (n² - 3*(n-1))
    bottom_left = bottom_right - 3 * (side_length - 1)
    diagonal_values.append(bottom_left)

    return diagonal_values


def get_all_diagonal_values(side_length: int) -> list[int]:
    """
    指定された辺の長さまでのスパイラルの全対角線上の値を取得
    時間計算量: O(n)
    空間計算量: O(n)
    """
    all_diagonal_values = [1]  # 中央の1から始める

    # 辺の長さ3から始めて、2ずつ増やしながら対角線の値を追加
    for current_side in range(3, side_length + 1, 2):
        diagonal_values = get_diagonal_values(current_side)
        all_diagonal_values.extend(diagonal_values)

    return all_diagonal_values


def count_primes_in_diagonals(side_length: int) -> tuple[int, int]:
    """
    指定された辺の長さまでのスパイラルの対角線上の素数の数と総数を返す
    時間計算量: O(n * √m) (mは対角線上の最大値)
    空間計算量: O(n)
    """
    diagonal_values = get_all_diagonal_values(side_length)

    # 素数の数をカウント (1は素数ではないので除外)
    prime_count = sum(1 for value in diagonal_values if value > 1 and is_prime(value))
    total_count = len(diagonal_values)

    return prime_count, total_count


def calculate_prime_ratio(side_length: int) -> float:
    """
    指定された辺の長さでの対角線上の素数の割合を計算
    時間計算量: O(n * √m) (mは対角線上の最大値)
    空間計算量: O(n)
    """
    prime_count, total_count = count_primes_in_diagonals(side_length)

    if total_count == 0:
        return 0.0

    return prime_count / total_count


def solve_naive(target_ratio: float = 0.1) -> int:
    """
    素直な解法: 辺の長さを3から順番に試す
    時間計算量: O(n² * √m) (mは対角線上の最大値)
    空間計算量: O(n)
    """
    side_length = 3

    while True:
        ratio = calculate_prime_ratio(side_length)

        if ratio < target_ratio:
            return side_length

        side_length += 2


def solve_optimized(target_ratio: float = 0.1) -> int:
    """
    最適化解法: 対角線の値を段階的に計算して素数をカウント
    時間計算量: O(n * √m) (mは対角線上の最大値)
    空間計算量: O(1)
    """
    side_length = 3
    prime_count = 0
    total_count = 1  # 中央の1から始める

    while True:
        # 現在の辺の長さでの対角線の値を取得
        diagonal_values = get_diagonal_values(side_length)

        # 新しい対角線の値で素数をカウント
        new_primes = sum(1 for value in diagonal_values if is_prime(value))

        prime_count += new_primes
        total_count += len(diagonal_values)

        # 比率を計算
        ratio = prime_count / total_count

        if ratio < target_ratio:
            return side_length

        side_length += 2
