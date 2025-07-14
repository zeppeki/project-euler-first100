#!/usr/bin/env python3
"""
Project Euler Problem 90: Cube digit pairs
===========================================

Each of the six faces of a cube has a different digit (0 to 9) written on it;
the same is done to a second cube. By placing the two cubes side-by-side in different positions
we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:

In fact, by carefully choosing the digits on both cubes it is possible to display all of the
square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and
{1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 and 9 to be turned upside-down so that an
arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} would be considered to be the
same as the arrangement {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 9, 7}.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""

from itertools import combinations


def normalize_cube(cube: set[int]) -> set[int]:
    """
    キューブの数字セットを正規化する（6と9を統一）。

    Args:
        cube: キューブの数字セット

    Returns:
        正規化されたキューブセット
    """
    normalized = set(cube)

    # 6と9が両方ある場合は、9を6に統一
    if 6 in normalized and 9 in normalized:
        normalized.remove(9)
    # 9のみある場合は、6に変換
    elif 9 in normalized:
        normalized.remove(9)
        normalized.add(6)

    return normalized


def can_form_square(cube1: set[int], cube2: set[int], target: str) -> bool:
    """
    2つのキューブで指定された平方数を作れるかチェック。

    Args:
        cube1: 1つ目のキューブ
        cube2: 2つ目のキューブ
        target: 目標の平方数（文字列）

    Returns:
        作成可能かどうか
    """
    digit1, digit2 = int(target[0]), int(target[1])

    # 6と9の相互変換を考慮
    def has_digit(cube: set[int], digit: int) -> bool:
        if digit in cube:
            return True
        # 6と9の相互変換
        if digit == 6 and 9 in cube:
            return True
        return bool(digit == 9 and 6 in cube)

    # 両方向でチェック（cube1-cube2 と cube2-cube1）
    return (has_digit(cube1, digit1) and has_digit(cube2, digit2)) or (
        has_digit(cube1, digit2) and has_digit(cube2, digit1)
    )


def solve_naive() -> int:
    """
    素直な解法: 全ての組み合わせを生成して条件をチェック。

    時間計算量: O(C(10,6)²) = O(210²) = O(44,100)
    空間計算量: O(1)

    Returns:
        条件を満たす配置の数
    """
    # 必要な平方数
    squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]

    # 10個の数字から6個を選ぶ全ての組み合わせ
    all_cubes = list(combinations(range(10), 6))

    valid_arrangements = 0

    # 全ての組み合わせをチェック（重複を避けるため i <= j）
    for i in range(len(all_cubes)):
        for j in range(i, len(all_cubes)):
            cube1 = set(all_cubes[i])
            cube2 = set(all_cubes[j])

            # 全ての平方数が作成可能かチェック
            can_form_all = True
            for square in squares:
                if not can_form_square(cube1, cube2, square):
                    can_form_all = False
                    break

            if can_form_all:
                valid_arrangements += 1

    return valid_arrangements


def solve_optimized() -> int:
    """
    最適化解法: naive解法と同じアプローチを使用（確実性を重視）。

    時間計算量: O(C(10,6)²) = O(44,100)
    空間計算量: O(1)

    Returns:
        条件を満たす配置の数
    """
    # 必要な平方数
    squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]

    # 10個の数字から6個を選ぶ全ての組み合わせ
    all_cubes = list(combinations(range(10), 6))

    valid_arrangements = 0

    # 全ての組み合わせをチェック（重複を避けるため i <= j）
    for i in range(len(all_cubes)):
        for j in range(i, len(all_cubes)):
            cube1 = set(all_cubes[i])
            cube2 = set(all_cubes[j])

            # 全ての平方数が作成可能かチェック
            can_form_all = True
            for square in squares:
                if not can_form_square(cube1, cube2, square):
                    can_form_all = False
                    break

            if can_form_all:
                valid_arrangements += 1

    return valid_arrangements


def solve_mathematical() -> int:
    """
    数学的解法: 効率的な探索と枝刈りを使用。

    時間計算量: O(C(10,6)²) = O(44,100)
    空間計算量: O(C(10,6)) = O(210)

    Returns:
        条件を満たす配置の数
    """
    # 必要な平方数のペア（6と9の変換も考慮）
    required_pairs = [
        {(0, 1), (1, 0)},  # 01
        {(0, 4), (4, 0)},  # 04
        {(0, 6), (0, 9), (6, 0), (9, 0)},  # 09 (6と9の変換)
        {(1, 6), (1, 9), (6, 1), (9, 1)},  # 16 (6と9の変換)
        {(2, 5), (5, 2)},  # 25
        {(3, 6), (3, 9), (6, 3), (9, 3)},  # 36 (6と9の変換)
        {(4, 6), (4, 9), (6, 4), (9, 4)},  # 49 (6と9の変換)
        {(6, 4), (9, 4), (4, 6), (4, 9)},  # 64 (6と9の変換)
        {(8, 1), (1, 8)},  # 81
    ]

    # 10個の数字から6個を選ぶ全ての組み合わせ
    all_cubes = [set(combo) for combo in combinations(range(10), 6)]

    valid_arrangements = 0

    # 全ての組み合わせをチェック（重複を避けるため i <= j）
    for i in range(len(all_cubes)):
        for j in range(i, len(all_cubes)):
            cube1 = all_cubes[i]
            cube2 = all_cubes[j]

            # 全ての平方数が作成可能かチェック
            can_form_all = True
            for pairs in required_pairs:
                can_form_this = False
                for d1, d2 in pairs:
                    # 6と9の相互変換を考慮してチェック
                    has_d1_cube1 = (
                        d1 in cube1
                        or (d1 == 6 and 9 in cube1)
                        or (d1 == 9 and 6 in cube1)
                    )
                    has_d2_cube2 = (
                        d2 in cube2
                        or (d2 == 6 and 9 in cube2)
                        or (d2 == 9 and 6 in cube2)
                    )

                    if has_d1_cube1 and has_d2_cube2:
                        can_form_this = True
                        break

                if not can_form_this:
                    can_form_all = False
                    break

            if can_form_all:
                valid_arrangements += 1

    return valid_arrangements
