#!/usr/bin/env python3
"""
Project Euler Problem 060: Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result is always prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, is the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

from itertools import combinations
from typing import Any


def sieve_of_eratosthenes(limit: int) -> list[bool]:
    """
    エラトステネスの篩で素数表を作成

    Args:
        limit: 上限値

    Returns:
        インデックスが素数かどうかのブール配列

    時間計算量: O(n log log n)
    空間計算量: O(n)
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return is_prime


def is_prime(n: int) -> bool:
    """
    素数判定

    Args:
        n: 判定する正の整数

    Returns:
        素数の場合True、そうでなければFalse

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


def concatenate_numbers(a: int, b: int) -> int:
    """
    2つの数値を連結する

    Args:
        a: 最初の数値
        b: 2番目の数値

    Returns:
        連結された数値

    時間計算量: O(log b)
    空間計算量: O(1)
    """
    return int(str(a) + str(b))


def are_prime_pair(p1: int, p2: int) -> bool:
    """
    2つの素数が素数ペアかどうかを判定

    Args:
        p1: 最初の素数
        p2: 2番目の素数

    Returns:
        素数ペアの場合True、そうでなければFalse

    時間計算量: O(√(max(concat)))
    空間計算量: O(1)
    """
    concat1 = concatenate_numbers(p1, p2)
    concat2 = concatenate_numbers(p2, p1)

    return is_prime(concat1) and is_prime(concat2)


def find_prime_pairs(primes: list[int], target_prime: int) -> list[int]:
    """
    指定した素数と素数ペアを形成する素数のリストを返す

    Args:
        primes: 素数のリスト
        target_prime: 対象の素数

    Returns:
        target_primeと素数ペアを形成する素数のリスト

    時間計算量: O(n × √(max(concat)))
    空間計算量: O(k) - kは結果の素数の数
    """
    pairs = []
    for prime in primes:
        if prime != target_prime and are_prime_pair(prime, target_prime):
            pairs.append(prime)
    return pairs


def can_form_complete_set(primes: list[int], set_size: int) -> bool:
    """
    指定した素数リストが完全な素数ペア集合を形成できるかチェック

    Args:
        primes: 素数のリスト
        set_size: 目標とする集合のサイズ

    Returns:
        完全な集合を形成できる場合True、そうでなければFalse

    時間計算量: O(n^2 × √(max(concat)))
    空間計算量: O(1)
    """
    if len(primes) != set_size:
        return False

    # 全ての素数のペアが素数ペアであることを確認
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if not are_prime_pair(primes[i], primes[j]):
                return False

    return True


def solve_naive(set_size: int = 5, prime_limit: int = 10000) -> int:
    """
    素直な解法: 全ての素数の組み合わせをチェック

    Args:
        set_size: 素数集合のサイズ
        prime_limit: 素数の上限

    Returns:
        条件を満たす素数集合の最小の和

    時間計算量: O(C(n,k) × k^2 × √(max(concat)))
    空間計算量: O(n)
    """
    # 素数を生成
    is_prime_array = sieve_of_eratosthenes(prime_limit)
    primes = [i for i in range(2, prime_limit + 1) if is_prime_array[i]]

    min_sum = float("inf")

    # 全ての組み合わせをチェック
    for prime_set in combinations(primes, set_size):
        if can_form_complete_set(list(prime_set), set_size):
            current_sum = sum(prime_set)
            min_sum = min(min_sum, current_sum)

    return int(min_sum) if min_sum != float("inf") else -1


def solve_optimized(set_size: int = 5, prime_limit: int = 10000) -> int:
    """
    最適化解法: 段階的に素数ペア集合を構築

    Args:
        set_size: 素数集合のサイズ
        prime_limit: 素数の上限

    Returns:
        条件を満たす素数集合の最小の和

    時間計算量: O(n^k × √(max(concat)))
    空間計算量: O(n)
    """
    # 素数を生成
    is_prime_array = sieve_of_eratosthenes(prime_limit)
    primes = [i for i in range(2, prime_limit + 1) if is_prime_array[i]]

    min_sum = float("inf")

    def build_set(
        current_set: list[int], remaining_primes: list[int], target_size: int
    ) -> None:
        nonlocal min_sum

        if len(current_set) == target_size:
            current_sum = sum(current_set)
            min_sum = min(min_sum, current_sum)
            return

        # 現在の合計がすでに最小値を超えている場合は枝刈り
        if sum(current_set) >= min_sum:
            return

        for i, prime in enumerate(remaining_primes):
            # 現在の集合の全ての素数とペアを形成できるかチェック
            if all(are_prime_pair(prime, p) for p in current_set):
                build_set([*current_set, prime], remaining_primes[i + 1 :], target_size)

    build_set([], primes, set_size)
    return int(min_sum) if min_sum != float("inf") else -1


def solve_mathematical(set_size: int = 5, prime_limit: int = 10000) -> int:
    """
    数学的解法: グラフ理論を用いた効率的な探索

    Args:
        set_size: 素数集合のサイズ
        prime_limit: 素数の上限

    Returns:
        条件を満たす素数集合の最小の和

    時間計算量: O(n^2 + n^k)
    空間計算量: O(n^2)
    """
    # 素数を生成
    is_prime_array = sieve_of_eratosthenes(prime_limit)
    primes = [i for i in range(2, prime_limit + 1) if is_prime_array[i]]

    # 素数ペアの隣接行列を構築
    n = len(primes)
    adjacency = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if are_prime_pair(primes[i], primes[j]):
                adjacency[i][j] = True
                adjacency[j][i] = True

    min_sum = float("inf")

    def find_clique(
        current_indices: list[int], candidates: list[int], target_size: int
    ) -> None:
        nonlocal min_sum

        if len(current_indices) == target_size:
            current_sum = sum(primes[i] for i in current_indices)
            min_sum = min(min_sum, current_sum)
            return

        # 現在の合計がすでに最小値を超えている場合は枝刈り
        current_sum = sum(primes[i] for i in current_indices)
        if current_sum >= min_sum:
            return

        for i, candidate in enumerate(candidates):
            # 現在の全ての頂点と隣接しているかチェック
            if all(adjacency[candidate][idx] for idx in current_indices):
                # 新しい候補リストは現在の候補と隣接している頂点のみ
                new_candidates = [
                    c for c in candidates[i + 1 :] if adjacency[candidate][c]
                ]
                find_clique([*current_indices, candidate], new_candidates, target_size)

    find_clique([], list(range(n)), set_size)
    return int(min_sum) if min_sum != float("inf") else -1


def find_prime_pair_sets_by_size(
    max_size: int = 5, prime_limit: int = 10000
) -> dict[int, Any]:
    """
    指定されたサイズまでの素数ペア集合を探索

    Args:
        max_size: 最大の集合サイズ
        prime_limit: 素数の上限

    Returns:
        各サイズの最小の素数集合の情報

    時間計算量: O(n^max_size × √(max(concat)))
    空間計算量: O(n)
    """
    # 素数を生成
    is_prime_array = sieve_of_eratosthenes(prime_limit)
    primes = [i for i in range(2, prime_limit + 1) if is_prime_array[i]]

    results = {}

    for size in range(2, max_size + 1):
        min_sum = float("inf")
        best_set = None

        def build_set(
            current_set: list[int], remaining_primes: list[int], target_size: int
        ) -> None:
            nonlocal min_sum, best_set

            if len(current_set) == target_size:
                current_sum = sum(current_set)
                if current_sum < min_sum:
                    min_sum = current_sum
                    best_set = current_set.copy()
                return

            if sum(current_set) >= min_sum:
                return

            for i, prime in enumerate(remaining_primes):
                if all(are_prime_pair(prime, p) for p in current_set):
                    build_set(
                        [*current_set, prime], remaining_primes[i + 1 :], target_size
                    )

        build_set([], primes, size)

        if best_set:
            results[size] = {
                "set": best_set,
                "sum": min_sum,
                "verified": can_form_complete_set(best_set, size),
            }

    return results


def get_prime_pair_details(prime_set: list[int]) -> dict[str, Any]:
    """
    素数集合の詳細な情報を取得

    Args:
        prime_set: 素数の集合

    Returns:
        素数集合の詳細情報
    """
    if not prime_set:
        return {"error": "Empty prime set"}

    # 全てのペアの連結結果を計算
    pair_results = {}
    for i in range(len(prime_set)):
        for j in range(i + 1, len(prime_set)):
            p1, p2 = prime_set[i], prime_set[j]
            concat1 = concatenate_numbers(p1, p2)
            concat2 = concatenate_numbers(p2, p1)

            pair_results[f"{p1},{p2}"] = {
                "concatenations": [concat1, concat2],
                "both_prime": [is_prime(concat1), is_prime(concat2)],
                "valid_pair": is_prime(concat1) and is_prime(concat2),
            }

    return {
        "prime_set": prime_set,
        "sum": sum(prime_set),
        "size": len(prime_set),
        "is_valid_complete_set": can_form_complete_set(prime_set, len(prime_set)),
        "pair_analysis": pair_results,
        "total_pairs": len(pair_results),
        "valid_pairs": sum(1 for info in pair_results.values() if info["valid_pair"]),
    }


def demonstrate_example_set() -> dict[str, Any]:
    """
    問題で与えられた例（3, 7, 109, 673）の詳細を示す

    Returns:
        例の詳細分析結果
    """
    example_set = [3, 7, 109, 673]
    return get_prime_pair_details(example_set)
