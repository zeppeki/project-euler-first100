#!/usr/bin/env python3
"""
Problem 062: Cubic permutations

The cube, 41063625 (345³), can be permuted to produce two other cubes: 56623104 (384³) and 66430125 (405³).
Find the smallest cube for which exactly five permutations of its digits are also cubes.

Answer: Project Euler公式サイトで確認してください。
"""

from collections import defaultdict


def get_digit_signature(n: int) -> str:
    """
    Get the sorted digit signature of a number.

    Args:
        n: Number to get signature for

    Returns:
        String of sorted digits
    """
    return "".join(sorted(str(n)))


def solve_naive() -> int:
    """
    素直な解法: 立方数を順次生成し、桁の順列をチェックして5つの立方数を持つ最小値を探索
    時間計算量: O(n * log(n)) - n個の立方数を生成し、各数の桁をソート
    空間計算量: O(n) - 桁の順列をグループ化するためのハッシュマップ
    """
    # Dictionary to group cubes by their digit signature
    digit_groups: dict[str, list[int]] = defaultdict(list)

    n = 1
    while True:
        cube = n**3
        signature = get_digit_signature(cube)
        digit_groups[signature].append(cube)

        # Check if we found exactly 5 cubes with the same digit signature
        if len(digit_groups[signature]) == 5:
            # Return the smallest cube in this group
            return min(digit_groups[signature])

        n += 1

        # Safety check to prevent infinite loops
        if n > 10000:
            break

    return 0


def solve_optimized() -> int:
    """
    最適化解法: 素直な解法と同じアルゴリズムだが、早期終了条件を追加
    時間計算量: O(n * log(n)) - 最悪ケースは同じだが実用的には高速
    空間計算量: O(n) - 桁の順列をグループ化するためのハッシュマップ
    """
    # Dictionary to group cubes by their digit signature
    digit_groups: dict[str, list[int]] = defaultdict(list)
    found_groups: list[tuple[str, list[int]]] = []

    n = 1
    while True:
        cube = n**3
        signature = get_digit_signature(cube)
        digit_groups[signature].append(cube)

        # Check if we found exactly 5 cubes with the same digit signature
        if len(digit_groups[signature]) == 5:
            found_groups.append((signature, digit_groups[signature][:]))

            # Early termination: we can stop when we find the first group
            # because we're generating cubes in ascending order
            return min(digit_groups[signature])

        n += 1

        # Safety check to prevent infinite loops
        if n > 10000:
            break

    return 0
