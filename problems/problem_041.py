#!/usr/bin/env python3
"""
Problem 041: Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Answer: 7652413
"""

import itertools


def is_prime(n: int) -> bool:
    """
    素数判定関数
    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


def is_pandigital(n: int, digits: int) -> bool:
    """
    n桁のpandigital数かどうかを判定
    時間計算量: O(digits)
    空間計算量: O(digits)
    """
    s = str(n)
    if len(s) != digits:
        return False

    expected = {str(i) for i in range(1, digits + 1)}
    actual = set(s)
    return expected == actual


def solve_naive() -> int:
    """
    素直な解法: 全ての可能なpandigital数を生成して素数判定
    時間計算量: O(n! × √max_number)
    空間計算量: O(n!)

    1桁から9桁までの全てのpandigital数を生成し、
    素数判定を行って最大値を見つける。
    """
    max_pandigital_prime = 0

    # 1桁から9桁まで順次チェック
    for n in range(1, 10):
        # n桁のpandigital数を生成
        digits = [str(i) for i in range(1, n + 1)]

        # 全ての順列を生成
        for perm in itertools.permutations(digits):
            # 先頭が0でないことを確認（実際は1以上なので問題なし）
            if perm[0] != "0":
                number = int("".join(perm))

                # 素数判定
                if is_prime(number):
                    max_pandigital_prime = max(max_pandigital_prime, number)

    return max_pandigital_prime


def solve_optimized() -> int:
    """
    最適化解法: 大きい桁数から降順で探索し、早期終了
    時間計算量: O(k! × √max_number) where k is the optimal digit count
    空間計算量: O(k!)

    最大のpandigital素数を見つけるため、9桁から1桁まで降順で探索。
    各桁数内では降順で数を生成し、最初に見つかった素数が最大値。
    """
    # 9桁から1桁まで降順で探索
    for n in range(9, 0, -1):
        digits = [str(i) for i in range(1, n + 1)]

        # 降順で順列を生成（大きい数から順に）
        for perm in sorted(itertools.permutations(digits), reverse=True):
            number = int("".join(perm))

            # 素数判定
            if is_prime(number):
                return number  # 最初に見つかった素数が最大値

    return 0  # 見つからなかった場合


def solve_mathematical() -> int:
    """
    数学的解法: 桁数の性質を利用した最適化
    時間計算量: O(k! × √max_number) where k ≤ 7
    空間計算量: O(k!)

    数学的洞察:
    - 1+2+...+n の和を考える
    - 1+2+...+8 = 36 (3で割り切れる)
    - 1+2+...+9 = 45 (3で割り切れる)
    - したがって8桁、9桁のpandigital数は必ず3で割り切れ、3より大きい素数にはなれない
    - 最大でも7桁までをチェックすれば十分
    """
    # 7桁から1桁まで降順で探索（8桁、9桁は数学的に不可能）
    for n in range(7, 0, -1):
        digits = [str(i) for i in range(1, n + 1)]

        # 降順で順列を生成（大きい数から順に）
        for perm in sorted(itertools.permutations(digits), reverse=True):
            number = int("".join(perm))

            # 素数判定
            if is_prime(number):
                return number  # 最初に見つかった素数が最大値

    return 0  # 見つからなかった場合
