#!/usr/bin/env python3
"""
Problem 072: Counting fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

from math import gcd
from typing import Any


def euler_totient_individual(n: int) -> int:
    """
    個別のオイラーのトーシェント関数φ(n)を計算

    時間計算量: O(n)
    空間計算量: O(1)

    Args:
        n: 計算対象の整数

    Returns:
        φ(n)の値
    """
    if n <= 1:
        return n

    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1

    return count


def euler_totient_prime_factorization(n: int) -> int:
    """
    素因数分解を使用したオイラーのトーシェント関数φ(n)の計算
    φ(n) = n × ∏(1 - 1/p) for all prime factors p

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
    temp = n

    # 2で割り切れる場合
    if temp % 2 == 0:
        result = result * (2 - 1) // 2
        while temp % 2 == 0:
            temp //= 2

    # 3以上の奇数の素因数
    i = 3
    while i * i <= temp:
        if temp % i == 0:
            result = result * (i - 1) // i
            while temp % i == 0:
                temp //= i
        i += 2

    # tempが1より大きい場合、それは素数
    if temp > 1:
        result = result * (temp - 1) // temp

    return result


def solve_naive(limit: int) -> int:
    """
    素直な解法: 各dについて個別にφ(d)を計算して合計

    時間計算量: O(n²)
    空間計算量: O(1)

    Args:
        limit: 分母の上限値

    Returns:
        既約真分数の総数
    """
    total = 0
    for d in range(2, limit + 1):
        phi_d = euler_totient_individual(d)
        total += phi_d

    return total


def solve_optimized(limit: int) -> int:
    """
    最適化解法: 素因数分解ベースのφ(d)計算

    時間計算量: O(n√n)
    空間計算量: O(log n)

    Args:
        limit: 分母の上限値

    Returns:
        既約真分数の総数
    """
    total = 0
    for d in range(2, limit + 1):
        phi_d = euler_totient_prime_factorization(d)
        total += phi_d

    return total


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: 篩ベースの効率的なφ(n)一括計算

    エラトステネスの篩の変形を使用してすべてのφ(d)を一括計算

    時間計算量: O(n log log n)
    空間計算量: O(n)

    Args:
        limit: 分母の上限値

    Returns:
        既約真分数の総数
    """
    if limit < 2:
        return 0

    # φ(i) = i で初期化
    phi = list(range(limit + 1))

    # エラトステネスの篩方式でφ(i)を計算
    for i in range(2, limit + 1):
        if phi[i] == i:  # iが素数の場合
            # iの倍数すべてについてφ(k) = φ(k) × (1 - 1/i)を適用
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    # d = 2からlimitまでのφ(d)の合計を返す
    return sum(phi[2 : limit + 1])


def solve_sieve_optimized(limit: int) -> int:
    """
    篩最適化解法: メモリ効率を考慮した篩計算

    時間計算量: O(n log log n)
    空間計算量: O(n)

    Args:
        limit: 分母の上限値

    Returns:
        既約真分数の総数
    """
    if limit < 2:
        return 0

    # φ(i) = i で初期化
    phi = list(range(limit + 1))

    # 素数判定と同時にφ計算を実行
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, limit + 1):
        if is_prime[i]:  # iが素数
            # 素数の倍数を処理
            for j in range(i, limit + 1, i):
                is_prime[j] = False
                phi[j] -= phi[j] // i
            is_prime[i] = True  # i自身は素数として復元

    return sum(phi[2 : limit + 1])


def count_reduced_fractions_range(start: int, end: int) -> int:
    """
    指定範囲内の既約真分数の数を計算

    Args:
        start: 分母の下限値
        end: 分母の上限値

    Returns:
        指定範囲内の既約真分数の総数
    """
    if start < 2:
        start = 2
    if end < start:
        return 0

    total = 0
    for d in range(start, end + 1):
        phi_d = euler_totient_prime_factorization(d)
        total += phi_d

    return total


def euler_totient_sieve(limit: int) -> list[int]:
    """
    篩を使用してlimit以下のすべてのφ(n)を計算

    Args:
        limit: 上限値

    Returns:
        φ(0), φ(1), ..., φ(limit)のリスト
    """
    phi = list(range(limit + 1))

    for i in range(2, limit + 1):
        if phi[i] == i:  # iが素数
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    return phi


def analyze_totient_distribution(limit: int) -> dict[str, int | float]:
    """
    トーシェント関数の分布を分析

    Args:
        limit: 上限値

    Returns:
        分析結果の辞書
    """
    phi_values = euler_totient_sieve(limit)

    return {
        "total_count": sum(phi_values[2 : limit + 1]),
        "max_phi": max(phi_values[2 : limit + 1]),
        "min_phi": min(phi_values[2 : limit + 1]),
        "average_phi": sum(phi_values[2 : limit + 1]) / (limit - 1),
    }


def get_mathematical_properties(n: int) -> dict[str, Any]:
    """
    指定された数値nの数学的性質を取得

    Args:
        n: 分析対象の数値

    Returns:
        数学的性質の辞書
    """
    phi_n = euler_totient_prime_factorization(n)

    # 素因数分解
    factors = []
    temp = n
    i = 2
    while i * i <= temp:
        while temp % i == 0:
            factors.append(i)
            temp //= i
        i += 1
    if temp > 1:
        factors.append(temp)

    unique_factors = list(set(factors))

    return {
        "n": n,
        "phi_n": phi_n,
        "ratio": n / phi_n if phi_n > 0 else 0,
        "prime_factors": unique_factors,
        "is_prime": len(unique_factors) == 1 and factors.count(unique_factors[0]) == 1,
        "is_prime_power": len(unique_factors) == 1,
    }
