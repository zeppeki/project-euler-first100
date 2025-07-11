#!/usr/bin/env python3
"""
Project Euler Problem 047: Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these four numbers?
"""

from functools import lru_cache


def get_prime_factors(n: int) -> set[int]:
    """
    数値の素因数を取得

    Args:
        n: 正の整数

    Returns:
        素因数の集合

    時間計算量: O(√n)
    空間計算量: O(log n)
    """
    factors = set()
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1

    if n > 1:
        factors.add(n)

    return factors


def count_distinct_prime_factors(n: int) -> int:
    """
    数値の異なる素因数の個数を取得

    Args:
        n: 正の整数

    Returns:
        異なる素因数の個数

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    count = 0
    d = 2

    while d * d <= n:
        if n % d == 0:
            count += 1
            while n % d == 0:
                n //= d
        d += 1

    if n > 1:
        count += 1

    return count


@lru_cache(maxsize=10000)
def count_distinct_prime_factors_cached(n: int) -> int:
    """
    数値の異なる素因数の個数を取得（キャッシュ付き）

    Args:
        n: 正の整数

    Returns:
        異なる素因数の個数

    時間計算量: O(√n) (初回), O(1) (キャッシュヒット)
    空間計算量: O(1) + O(キャッシュサイズ)
    """
    return count_distinct_prime_factors(n)


def solve_naive(target_factors: int) -> int:
    """
    素直な解法: 連続する整数をチェック

    Args:
        target_factors: 必要な異なる素因数の個数

    Returns:
        条件を満たす最初の連続整数列の最初の数

    時間計算量: O(n√n)
    空間計算量: O(1)
    """
    n = 2

    while True:
        # 連続するtarget_factors個の数をチェック
        consecutive_found = True
        for i in range(target_factors):
            if count_distinct_prime_factors(n + i) != target_factors:
                consecutive_found = False
                break

        if consecutive_found:
            return n

        n += 1


def solve_optimized(target_factors: int) -> int:
    """
    最適化解法: 効率的な探索とキャッシュの活用

    Args:
        target_factors: 必要な異なる素因数の個数

    Returns:
        条件を満たす最初の連続整数列の最初の数

    時間計算量: O(n√n) (キャッシュによる改善あり)
    空間計算量: O(キャッシュサイズ)
    """
    n = 2

    while True:
        # 連続するtarget_factors個の数をチェック
        consecutive_found = True
        for i in range(target_factors):
            if count_distinct_prime_factors_cached(n + i) != target_factors:
                consecutive_found = False
                break

        if consecutive_found:
            return n

        n += 1


def solve_mathematical(target_factors: int) -> int:
    """
    数学的解法: 効率的な素因数分解とパターン分析

    Args:
        target_factors: 必要な異なる素因数の個数

    Returns:
        条件を満たす最初の連続整数列の最初の数

    時間計算量: O(n√n)
    空間計算量: O(1)
    """
    n = 2

    while True:
        # 最初の数をチェック
        if count_distinct_prime_factors(n) != target_factors:
            n += 1
            continue

        # 連続する残りの数をチェック
        all_match = True
        for i in range(1, target_factors):
            if count_distinct_prime_factors(n + i) != target_factors:
                all_match = False
                # より効率的にスキップ: 失敗した位置まで進む
                n += i
                break

        if all_match:
            return n

        n += 1
