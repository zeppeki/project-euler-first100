#!/usr/bin/env python3
"""
Problem 069: Totient maximum

Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9) = 6.

n | Relatively Prime | φ(n) | n/φ(n)
--|------------------|------|-------
2 | 1                | 1    | 2
3 | 1,2              | 2    | 1.5
4 | 1,3              | 2    | 2
5 | 1,2,3,4          | 4    | 1.25
6 | 1,5              | 2    | 3
7 | 1,2,3,4,5,6      | 6    | 1.1666...
8 | 1,3,5,7          | 4    | 2
9 | 1,2,4,5,7,8      | 6    | 1.5
10| 1,3,7,9          | 4    | 2.5

It can be seen that n=6 produces a maximum n/φ(n) = 3 for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

from problems.lib.math_utils import gcd
from problems.lib.primes import get_prime_factors, sieve_of_eratosthenes


def euler_totient_naive(n: int) -> int:
    """
    オイラーのφ関数の素直な実装
    nと互いに素な数を直接カウント

    時間計算量: O(n log n)
    空間計算量: O(1)

    Args:
        n: 計算対象の整数

    Returns:
        φ(n)の値
    """
    if n <= 1:
        return 0

    count = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1

    return count


def euler_totient_optimized(n: int) -> int:
    """
    オイラーのφ関数の最適化実装
    素因数分解を使用: φ(n) = n × ∏(1 - 1/p) for all prime factors p

    時間計算量: O(√n)
    空間計算量: O(log n)

    Args:
        n: 計算対象の整数

    Returns:
        φ(n)の値
    """
    if n <= 1:
        return 0

    result = n
    prime_factors = get_prime_factors(n)

    for p in prime_factors:
        result = result * (p - 1) // p

    return result


def solve_naive(limit: int) -> int:
    """
    素直な解法: 各数値について個別にφ(n)を計算し、n/φ(n)が最大となるnを求める

    時間計算量: O(n² log n) - nまでの各数値についてO(n log n)でφ(n)を計算
    空間計算量: O(1)

    Args:
        limit: 上限値

    Returns:
        n/φ(n)が最大となるn
    """
    max_ratio = 0.0
    max_n = 0

    for n in range(2, limit + 1):
        phi_n = euler_totient_naive(n)
        ratio = n / phi_n

        if ratio > max_ratio:
            max_ratio = ratio
            max_n = n

    return max_n


def solve_optimized(limit: int) -> int:
    """
    最適化解法: 素因数分解ベースのφ(n)計算を使用

    時間計算量: O(n√n) - nまでの各数値についてO(√n)でφ(n)を計算
    空間計算量: O(log n)

    Args:
        limit: 上限値

    Returns:
        n/φ(n)が最大となるn
    """
    max_ratio = 0.0
    max_n = 0

    for n in range(2, limit + 1):
        phi_n = euler_totient_optimized(n)
        ratio = n / phi_n

        if ratio > max_ratio:
            max_ratio = ratio
            max_n = n

    return max_n


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: 素数を利用した効率的な計算

    n/φ(n)が最大になるのは、nが多くの異なる小さな素因数を持つ場合。
    実際には、n = 2 × 3 × 5 × 7 × ... の形の数値が最大比率を持つ。

    時間計算量: O(π(√limit)) - limit以下の素数の個数
    空間計算量: O(π(limit)) - limit以下の素数を格納

    Args:
        limit: 上限値

    Returns:
        n/φ(n)が最大となるn
    """
    # limitまでの素数を生成
    primes = sieve_of_eratosthenes(limit)

    # 小さな素数から順に掛け合わせていく
    product = 1
    max_n = 1

    for prime in primes:
        next_product = product * prime
        if next_product > limit:
            break
        product = next_product
        max_n = product

    return max_n


def get_totient_ratio(n: int) -> float:
    """
    指定された数値のn/φ(n)比率を計算

    Args:
        n: 計算対象の整数

    Returns:
        n/φ(n)の値
    """
    phi_n = euler_totient_optimized(n)
    return n / phi_n if phi_n > 0 else 0.0


def analyze_totient_pattern(limit: int) -> list[tuple[int, int, float]]:
    """
    指定範囲内のφ(n)とn/φ(n)のパターンを分析

    Args:
        limit: 分析する上限値

    Returns:
        (n, φ(n), n/φ(n))のタプルのリスト
    """
    results = []

    for n in range(2, min(limit + 1, 21)):  # 分析は20まで
        phi_n = euler_totient_optimized(n)
        ratio = n / phi_n
        results.append((n, phi_n, ratio))

    return results
