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


def gcd(a: int, b: int) -> int:
    """ユークリッドの互除法による最大公約数の計算"""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """最小公倍数の計算: LCM(a,b) = a*b / GCD(a,b)"""
    return abs(a * b) // gcd(a, b)


def solve_naive(n: int) -> int:
    """
    素直な解法: 1から順番に各数で割り切れるかチェック
    時間計算量: O(result * n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    candidate = n  # 最小でもnは必要
    while True:
        is_divisible = True
        for i in range(1, n + 1):
            if candidate % i != 0:
                is_divisible = False
                break

        if is_divisible:
            return candidate

        candidate += 1


def solve_optimized(n: int) -> int:
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


def solve_mathematical(n: int) -> int:
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


def solve_builtin(n: int) -> int:
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
