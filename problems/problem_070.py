#!/usr/bin/env python3
"""
Problem 070: Totient permutation

Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive integers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9) = 6.
The number 1 is considered to be relatively prime to every positive number, so φ(1) = 1.

Interestingly, φ(87109) = 79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the
ratio n/φ(n) is a minimum.
"""

from problems.lib.primes import get_prime_factors, sieve_of_eratosthenes


def euler_totient(n: int) -> int:
    """
    オイラーのトーシェント関数 φ(n) を計算
    素因数分解を使用: φ(n) = n × ∏(1 - 1/p) for all prime factors p

    時間計算量: O(√n)
    空間計算量: O(log n)

    Args:
        n: 計算対象の整数

    Returns:
        φ(n)の値
    """
    if n <= 1:
        return n

    result = n
    prime_factors = get_prime_factors(n)

    for p in prime_factors:
        result = result * (p - 1) // p

    return result


def is_permutation(a: int, b: int) -> bool:
    """
    2つの数値が同じ桁の並び替えかどうかを判定

    時間計算量: O(k log k) where k = max(digits in a, digits in b)
    空間計算量: O(k)

    Args:
        a: 第一の数値
        b: 第二の数値

    Returns:
        aとbが同じ桁の並び替えの場合True
    """
    return sorted(str(a)) == sorted(str(b))


def solve_naive(limit: int) -> int:
    """
    素直な解法: 全ての数値についてφ(n)を計算し、順列かつ最小比率を探す

    時間計算量: O(n√n) - nまでの各数値についてO(√n)でφ(n)を計算
    空間計算量: O(log n)

    Args:
        limit: 上限値（1 < n < limit）

    Returns:
        φ(n)がnの順列で、n/φ(n)が最小となるn
    """
    min_ratio = float("inf")
    min_n = 0

    for n in range(2, limit):
        phi_n = euler_totient(n)

        if is_permutation(n, phi_n):
            ratio = n / phi_n
            if ratio < min_ratio:
                min_ratio = ratio
                min_n = n

    return min_n


def solve_optimized(limit: int) -> int:
    """
    最適化解法: 数学的性質を利用した効率的な探索

    n/φ(n)が小さくなるのは、nが2つの近い素数の積の場合。
    φ(p*q) = (p-1)(q-1) where p, q are primes

    時間計算量: O(π(√limit)²) - 素数ペアの組み合わせ
    空間計算量: O(π(limit))

    Args:
        limit: 上限値（1 < n < limit）

    Returns:
        φ(n)がnの順列で、n/φ(n)が最小となるn
    """
    # limitの平方根付近の素数を生成
    sqrt_limit = int(limit**0.5) + 1000  # 少し余裕を持つ
    primes = sieve_of_eratosthenes(sqrt_limit)

    min_ratio = float("inf")
    min_n = 0

    # 2つの素数の積を調べる
    for i, p in enumerate(primes):
        if p * p >= limit:
            break

        for j in range(i, len(primes)):
            q = primes[j]
            n = p * q

            if n >= limit:
                break

            # φ(p*q) = (p-1)(q-1) for distinct primes p, q
            phi_n = (p - 1) * (q - 1)

            if is_permutation(n, phi_n):
                ratio = n / phi_n
                if ratio < min_ratio:
                    min_ratio = ratio
                    min_n = n

    return min_n


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: より焦点を絞った探索

    n/φ(n)を最小化するには、pとqができるだけ近い素数である必要がある。
    sqrt(limit)付近の素数に焦点を当てる。

    時間計算量: O(π(√limit)²)
    空間計算量: O(π(√limit))

    Args:
        limit: 上限値（1 < n < limit）

    Returns:
        φ(n)がnの順列で、n/φ(n)が最小となるn
    """
    # sqrt(limit)付近の素数に焦点を当てる
    sqrt_limit = int(limit**0.5)
    start_range = max(2, sqrt_limit - 1000)
    end_range = min(sqrt_limit + 1000, limit)

    primes = sieve_of_eratosthenes(end_range)
    # sqrt_limit付近の素数に絞る
    relevant_primes = [p for p in primes if start_range <= p <= end_range]

    min_ratio = float("inf")
    min_n = 0

    # 近い素数ペアを優先的に調べる
    for i, p in enumerate(relevant_primes):
        for j in range(i, len(relevant_primes)):
            q = relevant_primes[j]
            n = p * q

            if n >= limit:
                break

            phi_n = (p - 1) * (q - 1)

            if is_permutation(n, phi_n):
                ratio = n / phi_n
                if ratio < min_ratio:
                    min_ratio = ratio
                    min_n = n

    return min_n


def find_totient_permutations(
    limit: int, max_results: int = 10
) -> list[tuple[int, int, float]]:
    """
    指定範囲内でφ(n)がnの順列になる数値を探索

    Args:
        limit: 探索する上限値
        max_results: 返す結果の最大数

    Returns:
        (n, φ(n), n/φ(n))のタプルのリスト（比率でソート済み）
    """
    results = []

    # sqrt(limit)付近の素数ペアに焦点を当てる
    sqrt_limit = int(limit**0.5)
    primes = sieve_of_eratosthenes(sqrt_limit + 1000)

    for i, p in enumerate(primes):
        if p * p >= limit:
            break

        for j in range(i, len(primes)):
            q = primes[j]
            n = p * q

            if n >= limit:
                break

            phi_n = (p - 1) * (q - 1)

            if is_permutation(n, phi_n):
                ratio = n / phi_n
                results.append((n, phi_n, ratio))

    # 比率でソートして上位結果を返す
    results.sort(key=lambda x: x[2])
    return results[:max_results]


def analyze_totient_permutation_example() -> tuple[int, int, float]:
    """
    問題文の例（87109）の分析

    Returns:
        (n, φ(n), n/φ(n))のタプル
    """
    n = 87109
    phi_n = euler_totient(n)
    ratio = n / phi_n

    return n, phi_n, ratio
