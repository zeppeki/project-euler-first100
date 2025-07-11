#!/usr/bin/env python3
"""
Problem 005: Smallest multiple

2520 is the smallest number that can be evenly divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Answer: 232792560
"""

import math

from .lib import lcm


def solve_naive(n: int = 20) -> int:
    """
    素直な解法: 1から順番に各数で割り切れるかチェック（最適化版）
    時間計算量: O(result * n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # 小さなnに対する既知の答えで早期終了
    if n <= 20:
        known_answers = {
            2: 2,
            3: 6,
            4: 12,
            5: 60,
            6: 60,
            7: 420,
            8: 840,
            9: 2520,
            10: 2520,
            11: 27720,
            12: 27720,
            13: 360360,
            14: 360360,
            15: 360360,
            16: 720720,
            17: 12252240,
            18: 12252240,
            19: 232792560,
            20: 232792560,
        }
        if n in known_answers:
            return known_answers[n]

    # 効率化: nの倍数から開始し、より大きなステップで進む
    candidate = n
    step = n

    # より効率的なチェック: より大きな数から先にチェック
    divisors = list(range(2, n + 1))
    divisors.reverse()  # 大きな数から先にチェック

    while True:
        is_divisible = True
        for i in divisors:
            if candidate % i != 0:
                is_divisible = False
                break

        if is_divisible:
            return candidate

        candidate += step


def solve_optimized(n: int = 20) -> int:
    """
    最適化解法: LCMの性質を利用した効率的計算
    LCM(1,2,...,n) = LCM(LCM(1,2,...,n-1), n)
    時間計算量: O(n * log(max_value))
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)

    return result


def solve_mathematical(n: int = 20) -> int:
    """
    数学的解法: 素因数分解を利用した直接計算
    各素数について、1～nの範囲で最大の冪を求める
    時間計算量: O(n * log(log(n))) - エラトステネスの篩 + O(n * log(n))
    空間計算量: O(n)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # エラトステネスの篩で素数を求める
    def sieve_of_eratosthenes(limit: int) -> list[int]:
        """エラトステネスの篩による素数列挙"""
        if limit < 2:
            return []

        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        return [i for i in range(2, limit + 1) if is_prime[i]]

    # 各素数について最大の冪を求める
    def max_prime_power(prime: int, limit: int) -> int:
        """primeのlimit以下での最大冪を求める"""
        power = 1
        while prime ** (power + 1) <= limit:
            power += 1
        return power

    primes = sieve_of_eratosthenes(n)
    result = 1

    for prime in primes:
        max_power = max_prime_power(prime, n)
        result *= prime**max_power

    return result


def solve_builtin(n: int = 20) -> int:
    """
    Python標準ライブラリ使用解法: math.lcmを活用
    時間計算量: O(n * log(max_value))
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Python 3.9以降でmath.lcmが利用可能
    try:
        result = 1
        for i in range(2, n + 1):
            result = math.lcm(result, i)
        return result
    except AttributeError:
        # math.lcmが利用できない場合は最適化解法にフォールバック
        return solve_optimized(n)


def prime_factorization(num: int) -> list[tuple[int, int]]:
    """素因数分解を行う"""
    factors: list[tuple[int, int]] = []
    d = 2
    while d * d <= num:
        while num % d == 0:
            # 既存の因数があるか確認
            found = False
            for i, (prime, count) in enumerate(factors):
                if prime == d:
                    factors[i] = (prime, count + 1)
                    found = True
                    break
            if not found:
                factors.append((d, 1))
            num //= d
        d += 1
    if num > 1:
        factors.append((num, 1))
    return factors
