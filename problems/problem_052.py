#!/usr/bin/env python3
"""
Project Euler Problem 052: Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from typing import Any


def get_digit_signature(n: int) -> tuple[int, ...]:
    """
    数値の各桁の出現回数を取得

    Args:
        n: 正の整数

    Returns:
        各桁(0-9)の出現回数のタプル

    時間計算量: O(log n)
    空間計算量: O(1)
    """
    if n == 0:
        return (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    digits = [0] * 10
    while n > 0:
        digits[n % 10] += 1
        n //= 10
    return tuple(digits)


def get_digit_signature_str(n: int) -> str:
    """
    数値の各桁をソート済み文字列として取得

    Args:
        n: 正の整数

    Returns:
        各桁をソートした文字列

    時間計算量: O(log n * log log n)
    空間計算量: O(log n)
    """
    return "".join(sorted(str(n)))


def are_permutations(n1: int, n2: int) -> bool:
    """
    2つの数が同じ桁の順列かチェック

    Args:
        n1: 最初の数
        n2: 2番目の数

    Returns:
        同じ桁の順列の場合True、そうでなければFalse

    時間計算量: O(log max(n1, n2))
    空間計算量: O(log max(n1, n2))
    """
    return get_digit_signature_str(n1) == get_digit_signature_str(n2)


def check_all_multiples_permuted(x: int, max_multiple: int = 6) -> bool:
    """
    xとその倍数(2x, 3x, ..., max_multiple*x)が全て同じ桁を持つかチェック

    Args:
        x: 元の数
        max_multiple: チェックする最大の倍数

    Returns:
        全ての倍数が同じ桁を持つ場合True、そうでなければFalse

    時間計算量: O(max_multiple * log x)
    空間計算量: O(log x)
    """
    base_signature = get_digit_signature(x)

    for multiple in range(2, max_multiple + 1):
        if get_digit_signature(x * multiple) != base_signature:
            return False

    return True


def solve_naive(max_multiple: int = 6) -> int:
    """
    素直な解法: 1から順番にチェック

    Args:
        max_multiple: チェックする最大の倍数

    Returns:
        条件を満たす最小の数

    時間計算量: O(n * max_multiple * log n)
    空間計算量: O(log n)
    """
    x = 1
    while True:
        if check_all_multiples_permuted(x, max_multiple):
            return x
        x += 1


def solve_optimized(max_multiple: int = 6) -> int:
    """
    最適化解法: 桁数による制約を利用

    Args:
        max_multiple: チェックする最大の倍数

    Returns:
        条件を満たす最小の数

    時間計算量: O(n * max_multiple * log n)
    空間計算量: O(log n)
    """
    # x * max_multiple が x と同じ桁数を持つためには、
    # x は 10^(d-1) から 10^d / max_multiple の範囲にある必要がある

    digits = 1
    while True:
        # d桁の数の範囲
        start = 10 ** (digits - 1)
        # max_multiple倍しても桁数が変わらない上限
        end = 10**digits // max_multiple

        if start > end:
            # この桁数では不可能、次の桁数へ
            digits += 1
            continue

        for x in range(start, end + 1):
            if check_all_multiples_permuted(x, max_multiple):
                return x

        digits += 1


def solve_mathematical(max_multiple: int = 6) -> int:
    """
    数学的解法: 数学的制約を活用した効率的な探索

    Args:
        max_multiple: チェックする最大の倍数

    Returns:
        条件を満たす最小の数

    時間計算量: O(n * max_multiple * log n)
    空間計算量: O(log n)
    """
    # 数学的洞察:
    # 1. x と 6x が同じ桁数を持つためには、x は 10^(d-1) から 10^d/6 の範囲
    # 2. 6x が x と同じ桁数を持つということは、x の最初の桁は1である必要がある
    # 3. なぜなら、2以上だと6倍すると桁数が増える可能性が高い

    digits = 1
    while True:
        # d桁の数で最初の桁が1の範囲
        start = 10 ** (digits - 1)
        end = min(2 * 10 ** (digits - 1) - 1, 10**digits // max_multiple)

        if start > end:
            digits += 1
            continue

        # 最初の桁が1の数のみをチェック
        for x in range(start, end + 1):
            # 最初の桁が1でない場合はスキップ
            if str(x)[0] != "1":
                continue

            if check_all_multiples_permuted(x, max_multiple):
                return x

        digits += 1


def get_permuted_multiples_details(
    x: int, max_multiple: int = 6
) -> list[tuple[int, int]]:
    """
    指定した数の順列倍数の詳細を取得

    Args:
        x: 元の数
        max_multiple: チェックする最大の倍数

    Returns:
        (倍数, x*倍数) のリスト
    """
    return [(multiple, x * multiple) for multiple in range(1, max_multiple + 1)]


def demonstrate_permutation_check(n1: int, n2: int) -> dict[str, Any]:
    """
    2つの数の順列チェックのデモンストレーション

    Args:
        n1: 最初の数
        n2: 2番目の数

    Returns:
        デモンストレーション結果の辞書
    """
    return {
        "number1": n1,
        "number2": n2,
        "digits1_sorted": get_digit_signature_str(n1),
        "digits2_sorted": get_digit_signature_str(n2),
        "signature1": get_digit_signature(n1),
        "signature2": get_digit_signature(n2),
        "are_permutations": are_permutations(n1, n2),
    }


def find_smallest_permuted_multiple_family(min_family_size: int = 2) -> list[int]:
    """
    指定されたサイズ以上の順列倍数族を持つ最小の数を探す

    Args:
        min_family_size: 最小の族のサイズ

    Returns:
        条件を満たす数のリスト
    """
    results: list[int] = []
    x = 1

    while len(results) < 10:  # 最初の10個を見つける
        max_multiple = 2
        while max_multiple <= 10:
            if (
                check_all_multiples_permuted(x, max_multiple)
                and max_multiple >= min_family_size
            ):
                results.append(x)
                break
            max_multiple += 1
        x += 1

    return results
