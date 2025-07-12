#!/usr/bin/env python3
"""
Project Euler Problem 046: Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1²
15 = 7 + 2×2²
21 = 3 + 2×3²
25 = 7 + 2×3²
27 = 19 + 2×2²
33 = 31 + 2×1²

It turns out that the conjecture is false.

What is the smallest odd composite number that cannot be written as the sum
of a prime and twice a square?
"""

import math

from problems.lib.primes import is_prime


def is_perfect_square(n: int) -> bool:
    """
    完全平方数判定
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n


def generate_primes(limit: int) -> list[int]:
    """
    エラトステネスの篩で素数生成
    時間計算量: O(n log log n)
    空間計算量: O(n)
    """
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(2, limit + 1) if sieve[i]]


def can_be_written_as_conjecture(n: int, primes: list[int]) -> bool:
    """
    数がゴールドバッハの他の予想の形で書けるかチェック
    時間計算量: O(p√n) where p is number of primes less than n
    空間計算量: O(1)
    """
    for prime in primes:
        if prime >= n:
            break

        # n = prime + 2 * k²
        # 2 * k² = n - prime
        # k² = (n - prime) / 2
        remainder = n - prime
        if remainder > 0 and remainder % 2 == 0:
            square_part = remainder // 2
            if is_perfect_square(square_part):
                return True

    return False


def solve_naive(limit: int = 10000) -> int:
    """
    素直な解法: 各奇数合成数について予想が成り立つかチェック
    時間計算量: O(n² √n)
    空間計算量: O(1)
    """
    n = 9  # 最初の奇数合成数
    while n < limit:
        # 奇数かつ合成数かチェック
        if n % 2 == 1 and not is_prime(n):
            # 予想が成り立つかチェック
            found = False
            for prime in range(2, n):
                if is_prime(prime):
                    remainder = n - prime
                    if remainder > 0 and remainder % 2 == 0:
                        square_part = remainder // 2
                        if is_perfect_square(square_part):
                            found = True
                            break

            if not found:
                return n

        n += 2  # 次の奇数へ

    return -1  # 見つからなかった場合


def solve_optimized(limit: int = 10000) -> int:
    """
    最適化解法: 事前に素数を生成して効率化
    時間計算量: O(n log log n + n²√n)
    空間計算量: O(n)
    """
    # 事前に素数を生成
    primes = generate_primes(limit)

    n = 9  # 最初の奇数合成数
    while n < limit:
        # 奇数かつ合成数かチェック
        if (
            n % 2 == 1
            and not is_prime(n)
            and not can_be_written_as_conjecture(n, primes)
        ):
            return n

        n += 2  # 次の奇数へ

    return -1  # 見つからなかった場合


def solve_mathematical(limit: int = 10000) -> int:
    """
    数学的解法: 効率的な判定とメモ化を使用
    時間計算量: O(n log log n + n√n)
    空間計算量: O(n)
    """
    # 事前に素数を生成
    primes = generate_primes(limit)
    prime_set = set(primes)

    # 平方数のリストを事前計算（ソート済み）
    squares = []
    k = 1
    while 2 * k * k < limit:
        squares.append(2 * k * k)
        k += 1

    n = 9  # 最初の奇数合成数
    while n < limit:
        # 奇数かつ合成数かチェック
        if n % 2 == 1 and n not in prime_set:
            # 予想が成り立つかチェック
            found = False
            for twice_square in squares:
                if twice_square >= n:
                    break
                if (n - twice_square) in prime_set:
                    found = True
                    break

            if not found:
                return n

        n += 2  # 次の奇数へ

    return -1  # 見つからなかった場合
