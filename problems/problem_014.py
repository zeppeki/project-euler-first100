#!/usr/bin/env python3
"""
Problem 014: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Conjecture), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Answer: 837799
"""


def solve_naive(limit: int) -> int:
    """
    素直な解法: 全ての数について個別にCollatz数列の長さを計算
    時間計算量: O(n * L) where L is average chain length
    空間計算量: O(1)
    """
    if limit <= 1:
        raise ValueError("limit must be greater than 1")

    max_length = 0
    max_start = 0

    for start in range(1, limit):
        length = collatz_length_simple(start)
        if length > max_length:
            max_length = length
            max_start = start

    return max_start


def collatz_length_simple(n: int) -> int:
    """Collatz数列の長さを計算（単純版）"""
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def solve_optimized(limit: int) -> int:
    """
    最適化解法: メモ化を使用してCollatz数列の長さを効率的に計算
    時間計算量: O(n * log L) where L is average chain length
    空間計算量: O(n)
    """
    if limit <= 1:
        raise ValueError("limit must be greater than 1")

    memo: dict[int, int] = {}
    max_length = 0
    max_start = 0

    for start in range(1, limit):
        length = collatz_length_memoized(start, memo)
        if length > max_length:
            max_length = length
            max_start = start

    return max_start


def collatz_length_memoized(n: int, memo: dict[int, int]) -> int:
    """Collatz数列の長さを計算（メモ化版）"""
    if n in memo:
        return memo[n]

    original_n = n
    path = []

    # 既知の値に達するまで計算
    while n not in memo and n != 1:
        path.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    # 基準値を取得
    base_length = 1 if n == 1 else memo[n]

    # パス上の全ての値をメモ化
    for i in range(len(path) - 1, -1, -1):
        base_length += 1
        memo[path[i]] = base_length

    # original_nが1の場合も処理
    if original_n == 1:
        memo[1] = 1
        return 1

    return memo[original_n]
