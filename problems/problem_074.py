#!/usr/bin/env python3
"""
Problem 074: Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, for which it produces the longest chain of non-repeating terms:

169 → 363601 → 1454 → 169

It can be seen that 169 is an element of a three-element non-repeating chain.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

from typing import Any

# Pre-compute factorials for digits 0-9
DIGIT_FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def digit_factorial_sum(n: int) -> int:
    """
    桁の階乗の和を計算

    時間計算量: O(log n)
    空間計算量: O(1)

    Args:
        n: 計算対象の数値

    Returns:
        各桁の階乗の和
    """
    if n == 0:
        return DIGIT_FACTORIALS[0]  # 0! = 1

    total = 0
    while n > 0:
        digit = n % 10
        total += DIGIT_FACTORIALS[digit]
        n //= 10
    return total


def get_factorial_chain_length(n: int) -> int:
    """
    階乗チェーンの長さを計算（重複しない項の数）

    時間計算量: O(k) where k is chain length
    空間計算量: O(k)

    Args:
        n: 開始する数値

    Returns:
        チェーンの長さ（重複しない項の数）
    """
    seen = set()
    current = n

    while current not in seen:
        seen.add(current)
        current = digit_factorial_sum(current)

    return len(seen)


def solve_naive(limit: int) -> int:
    """
    素直な解法: 各数値のチェーンの長さを直接計算

    時間計算量: O(n × k) where k is average chain length
    空間計算量: O(k)

    Args:
        limit: 上限値（未満）

    Returns:
        ちょうど60の重複しない項を持つチェーンの数
    """
    count = 0
    target_length = 60

    for i in range(1, limit):
        if get_factorial_chain_length(i) == target_length:
            count += 1

    return count


def solve_optimized(limit: int) -> int:
    """
    最適化解法: メモ化を使用してチェーンの長さを効率的に計算

    時間計算量: O(n × k) with memoization speedup
    空間計算量: O(n)

    Args:
        limit: 上限値（未満）

    Returns:
        ちょうど60の重複しない項を持つチェーンの数
    """
    count = 0
    target_length = 60
    memo: dict[int, int] = {}

    for i in range(1, limit):
        length = get_factorial_chain_length_memoized(i, memo)
        if length == target_length:
            count += 1

    return count


def get_factorial_chain_length_memoized(n: int, memo: dict[int, int]) -> int:
    """
    メモ化を使用した階乗チェーンの長さ計算

    Args:
        n: 開始する数値
        memo: メモ化用の辞書

    Returns:
        チェーンの長さ
    """
    if n in memo:
        return memo[n]

    # 直接計算して結果をキャッシュ
    length = get_factorial_chain_length(n)
    memo[n] = length
    return length


def analyze_factorial_chains(limit: int) -> dict[str, Any]:
    """
    階乗チェーンの分析

    Args:
        limit: 分析する範囲の上限

    Returns:
        分析結果の辞書
    """
    length_counts: dict[int, int] = {}
    special_chains: dict[int, int] = {}
    memo: dict[int, int] = {}

    for i in range(1, limit):
        length = get_factorial_chain_length_memoized(i, memo)
        length_counts[length] = length_counts.get(length, 0) + 1

        # 特別なチェーンの例を収集
        if length not in special_chains:
            special_chains[length] = i

    return {
        "length_distribution": length_counts,
        "special_chain_examples": special_chains,
        "most_common_length": max(length_counts, key=lambda x: length_counts[x]),
        "longest_chain": max(length_counts.keys()),
        "total_numbers": limit - 1,
    }


def get_factorial_chain(n: int, max_length: int = 100) -> list[int]:
    """
    指定された数値から始まる階乗チェーンを取得

    Args:
        n: 開始する数値
        max_length: 最大チェーン長（無限ループ防止）

    Returns:
        チェーンのリスト（ループ検出まで）
    """
    chain: list[int] = []
    seen: set[int] = set()
    current = n

    while current not in seen and len(chain) < max_length:
        chain.append(current)
        seen.add(current)
        current = digit_factorial_sum(current)

    # ループの最初の要素も追加（ループを示すため）
    if current in seen:
        chain.append(current)

    return chain


def find_chains_with_length(target_length: int, limit: int) -> list[int]:
    """
    指定された長さのチェーンを持つ数値を検索

    Args:
        target_length: 目標とするチェーンの長さ
        limit: 検索範囲の上限

    Returns:
        指定された長さのチェーンを持つ数値のリスト
    """
    result: list[int] = []
    memo: dict[int, int] = {}

    for i in range(1, limit):
        if get_factorial_chain_length_memoized(i, memo) == target_length:
            result.append(i)

    return result


def verify_known_chains() -> dict[int, tuple[int, list[int]]]:
    """
    既知の特別なチェーンを検証

    Returns:
        数値をキーとし、(チェーン長, チェーン)をバリューとする辞書
    """
    known_cases = [145, 169, 363601, 1454, 871, 45361, 872, 45362, 69, 78, 540]
    results: dict[int, tuple[int, list[int]]] = {}

    for num in known_cases:
        chain = get_factorial_chain(num)
        length = get_factorial_chain_length(num)
        results[num] = (length, chain)

    return results


def count_chains_by_length(limit: int) -> dict[int, int]:
    """
    チェーンの長さ別に数をカウント

    Args:
        limit: 検索範囲の上限

    Returns:
        チェーン長をキー、その長さのチェーン数をバリューとする辞書
    """
    length_counts: dict[int, int] = {}
    memo: dict[int, int] = {}

    for i in range(1, limit):
        length = get_factorial_chain_length_memoized(i, memo)
        length_counts[length] = length_counts.get(length, 0) + 1

    return length_counts


def get_factorial_chain_statistics(limit: int) -> dict[str, Any]:
    """
    階乗チェーンの統計情報を取得

    Args:
        limit: 分析範囲の上限

    Returns:
        統計情報の辞書
    """
    length_counts = count_chains_by_length(limit)

    return {
        "length_distribution": dict(sorted(length_counts.items())),
        "total_numbers_analyzed": limit - 1,
        "unique_chain_lengths": len(length_counts),
        "most_common_length": max(length_counts, key=lambda x: length_counts[x]),
        "most_common_count": max(length_counts.values()),
        "longest_chain_length": max(length_counts.keys()),
        "shortest_chain_length": min(length_counts.keys()),
        "chains_with_60_terms": length_counts.get(60, 0),
    }
