#!/usr/bin/env python3
"""
Problem 049: Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the three 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you get by concatenating the three terms of this sequence?

Answer: [Hidden]
"""

from .lib import (
    get_digit_signature,
    is_prime,
)
from .lib.primes import sieve_of_eratosthenes


def find_arithmetic_sequences(numbers: list[int]) -> list[tuple[int, int, int]]:
    """
    数のリストから算術数列を見つける
    時間計算量: O(n²)
    空間計算量: O(1)
    """
    sequences = []
    numbers = sorted(numbers)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            a, b = numbers[i], numbers[j]
            diff = b - a
            c = b + diff

            if c in numbers:
                sequences.append((a, b, c))

    return sequences


def solve_naive() -> int:
    """
    素直な解法: 全ての4桁の素数をチェックして順列グループを作り、算術数列を探す
    時間計算量: O(n² log n)
    空間計算量: O(n)
    """
    # 4桁の素数をすべて生成
    primes = []
    for n in range(1000, 10000):
        if is_prime(n):
            primes.append(n)

    # 順列グループごとに分類
    permutation_groups: dict[str, list[int]] = {}
    for prime in primes:
        signature = get_digit_signature(prime)
        if signature not in permutation_groups:
            permutation_groups[signature] = []
        permutation_groups[signature].append(prime)

    # 各グループで算術数列を探す
    for _signature, group in permutation_groups.items():
        if len(group) >= 3:
            sequences = find_arithmetic_sequences(group)
            for seq in sequences:
                # 既知の例 (1487, 4817, 8147) を除外
                if seq != (1487, 4817, 8147):
                    # 12桁の数として連結
                    return int(f"{seq[0]}{seq[1]}{seq[2]}")

    return 0


def solve_optimized() -> int:
    """
    最適化解法: エラトステネスの篩を使って素数生成を高速化
    時間計算量: O(n log log n + m²)
    空間計算量: O(n)
    """

    # エラトステネスの篩で4桁の素数を効率的に生成
    is_prime_arr = sieve_of_eratosthenes(9999, "bool_array")

    # 4桁の素数のみ抽出
    primes = [n for n in range(1000, 10000) if is_prime_arr[n]]

    # 順列グループごとに分類
    permutation_groups: dict[str, list[int]] = {}
    for prime in primes:
        signature = get_digit_signature(prime)
        if signature not in permutation_groups:
            permutation_groups[signature] = []
        permutation_groups[signature].append(prime)

    # 各グループで算術数列を探す
    for _signature, group in permutation_groups.items():
        if len(group) >= 3:
            sequences = find_arithmetic_sequences(group)
            for seq in sequences:
                # 既知の例を除外
                if seq != (1487, 4817, 8147):
                    return int(f"{seq[0]}{seq[1]}{seq[2]}")

    return 0


def solve_mathematical() -> int:
    """
    数学的解法: 算術数列の性質を利用した最適化
    中間項から前後の項を計算することで効率化
    時間計算量: O(n log n)
    空間計算量: O(n)
    """

    # エラトステネスの篩で素数生成
    primes_list = sieve_of_eratosthenes(9999)
    primes = {n for n in primes_list if n >= 1000}

    # 順列グループを作成
    permutation_groups: dict[str, set[int]] = {}
    for prime in primes:
        signature = get_digit_signature(prime)
        if signature not in permutation_groups:
            permutation_groups[signature] = set()
        permutation_groups[signature].add(prime)

    # 3つ以上の順列を持つグループのみ処理
    for _signature, group in permutation_groups.items():
        if len(group) >= 3:
            group_list = sorted(group)

            # 中間項を基準に算術数列をチェック
            for i in range(len(group_list)):
                for j in range(i + 1, len(group_list)):
                    a, b = group_list[i], group_list[j]
                    diff = b - a
                    c = b + diff

                    if c in group:
                        sequence = (a, b, c)
                        # 既知の例を除外
                        if sequence != (1487, 4817, 8147):
                            return int(f"{a}{b}{c}")

    return 0
