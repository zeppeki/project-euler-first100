#!/usr/bin/env python3
"""
Problem 007: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime?

Answer: 104743
"""

import math

from .lib import is_prime, is_prime_optimized, sieve_of_eratosthenes


def solve_naive(n: int) -> int:
    """
    素直な解法: 各数を素数判定して順次n番目の素数を見つける
    時間計算量: O(n * sqrt(m)) where m is the nth prime
    空間計算量: O(1)
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 2

    count = 1  # 2を最初の素数として数える
    candidate = 3  # 次の候補は3

    while count < n:
        if is_prime(candidate):
            count += 1
        if count < n:
            candidate += 2  # 奇数のみをチェック

    return candidate


def solve_optimized(n: int) -> int:
    """
    最適化解法: エラトステネスの篩を使用した効率的な素数生成
    時間計算量: O(m * log(log(m))) where m is the upper bound
    空間計算量: O(m)
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 2

    # n番目の素数の近似上限を計算（素数定理より）
    limit = 12 if n < 6 else int(n * (math.log(n) + math.log(math.log(n))))

    # エラトステネスの篩
    primes_result = sieve_of_eratosthenes(limit, "list")
    assert isinstance(primes_result, list)
    primes = primes_result

    # 必要な数の素数が見つからない場合、範囲を拡張
    while len(primes) < n:
        limit *= 2
        primes_result = sieve_of_eratosthenes(limit, "list")
        assert isinstance(primes_result, list)
        primes = primes_result

    return primes[n - 1]


def solve_mathematical(n: int) -> int:
    """
    数学的解法: 試行割り付きの最適化された素数判定
    6k±1の形の数のみをチェックして効率化
    時間計算量: O(n * sqrt(m) / 3) where m is the nth prime
    空間計算量: O(1)
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 2
    if n == 2:
        return 3

    count = 2  # 2と3を既に数えている
    candidate = 5  # 次の候補は5 (6*1-1)
    increment = 2  # 5の次は7 (6*1+1), その次は11 (6*2-1)

    while count < n:
        if is_prime_optimized(candidate):
            count += 1
        if count < n:
            candidate += increment
            increment = 6 - increment  # 2と4を交互に

    return candidate
