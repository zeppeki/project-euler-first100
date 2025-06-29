#!/usr/bin/env python3
"""
Problem 010: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer: 142913828922
"""

import math


def solve_naive(limit: int) -> int:
    """
    素直な解法: 各数を素数判定して合計を計算
    時間計算量: O(n * sqrt(n))
    空間計算量: O(1)
    """
    if limit <= 2:
        return 0

    prime_sum = 2  # 最初の素数2を加算

    # 3から始めて奇数のみをチェック
    for num in range(3, limit, 2):
        if is_prime_naive(num):
            prime_sum += num

    return prime_sum


def is_prime_naive(num: int) -> bool:
    """素数判定（素直な方法）"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    return all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2))


def solve_optimized(limit: int) -> int:
    """
    最適化解法: エラトステネスの篩を使用
    時間計算量: O(n * log(log(n)))
    空間計算量: O(n)
    """
    if limit <= 2:
        return 0

    # エラトステネスの篩で素数を見つけて合計
    primes = sieve_of_eratosthenes(limit - 1)
    return sum(primes)


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """エラトステネスの篩で指定された範囲の素数を全て求める"""
    if limit < 2:
        return []

    # 篩を初期化
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # 篩を実行
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # 素数のリストを作成
    return [i for i in range(2, limit + 1) if is_prime[i]]


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: 最適化されたエラトステネスの篩（メモリ効率版）
    時間計算量: O(n * log(log(n)))
    空間計算量: O(n)
    """
    if limit <= 2:
        return 0

    # 2は別途処理
    prime_sum = 2

    # 奇数のみの篩を使用してメモリを半分に削減
    odd_limit = (limit - 1) // 2
    is_prime_odd = [True] * (odd_limit + 1)

    # 3から始めて奇数の合成数をマーク
    for i in range(1, int(math.sqrt(limit)) // 2 + 1):
        if is_prime_odd[i]:
            prime = 2 * i + 1
            # prime * prime から開始して、prime の奇数倍をマーク
            start = (prime * prime - 1) // 2
            for j in range(start, odd_limit + 1, prime):
                is_prime_odd[j] = False

    # 奇数の素数の合計を計算 (limitより小さい数のみ)
    for i in range(1, odd_limit + 1):
        if is_prime_odd[i]:
            prime = 2 * i + 1
            if prime < limit:
                prime_sum += prime

    return prime_sum
