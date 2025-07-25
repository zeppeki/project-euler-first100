#!/usr/bin/env python3
"""
Problem 067: Maximum Path Sum II

By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 2^99 altogether! If you
could check one trillion (10^12) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it. ;o)

The triangle contains 100 rows and is available in the file triangle.txt.
"""

from problems.lib.dynamic_programming import max_path_sum_triangle, parse_triangle
from problems.lib.file_io import load_triangle_data


def solve_naive(triangle: list[list[int]] | None = None) -> int:
    """
    素直な解法: 全経路を探索してブルートフォースで最大値を求める

    注意: 100行の三角形では実用的でない（2^99通りの経路）

    時間計算量: O(2^n) - 指数時間
    空間計算量: O(n) - 再帰スタック

    Args:
        triangle: 三角形の数値配列（Noneの場合はファイルから読み込み）

    Returns:
        最大パス合計
    """
    if triangle is None:
        triangle = load_triangle()

    def max_path_from(row: int, col: int) -> int:
        """指定位置から底辺までの最大パス合計を再帰的に計算"""
        if row >= len(triangle):
            return 0

        current = triangle[row][col]

        # 最後の行の場合
        if row == len(triangle) - 1:
            return current

        # 下の2つの経路のうち最大値を取る
        left = max_path_from(row + 1, col)
        right = max_path_from(row + 1, col + 1)

        return current + max(left, right)

    return max_path_from(0, 0)


def solve_optimized(triangle: list[list[int]] | None = None) -> int:
    """
    最適化解法: 動的プログラミング（メモ化）で効率的に計算

    時間計算量: O(n^2)
    空間計算量: O(n^2)

    Args:
        triangle: 三角形の数値配列（Noneの場合はファイルから読み込み）

    Returns:
        最大パス合計
    """
    if triangle is None:
        triangle = load_triangle()
    n = len(triangle)
    memo: dict[tuple[int, int], int] = {}

    def max_path_from(row: int, col: int) -> int:
        """メモ化を使用した最大パス計算"""
        if row >= n:
            return 0

        if (row, col) in memo:
            return memo[(row, col)]

        current = triangle[row][col]

        # 最後の行の場合
        if row == n - 1:
            memo[(row, col)] = current
            return current

        # 下の2つの経路のうち最大値を取る
        left = max_path_from(row + 1, col)
        right = max_path_from(row + 1, col + 1)

        result = current + max(left, right)
        memo[(row, col)] = result
        return result

    return max_path_from(0, 0)


def solve_mathematical(triangle: list[list[int]] | None = None) -> int:
    """
    数学的解法: ライブラリのmax_path_sum_triangle関数を使用

    時間計算量: O(n^2)
    空間計算量: O(n)

    Args:
        triangle: 三角形の数値配列（Noneの場合はファイルから読み込み）

    Returns:
        最大パス合計
    """
    if triangle is None:
        triangle = load_triangle()

    return max_path_sum_triangle(triangle)


def get_problem_triangle() -> list[list[int]]:
    """Problem 067の三角形データを取得"""
    return load_triangle_data("0067_triangle.txt")


def get_example_triangle() -> list[list[int]]:
    """例題の小さな三角形データを取得"""
    triangle_str = """3
7 4
2 4 6
8 5 9 3"""

    return parse_triangle(triangle_str)


def load_triangle() -> list[list[int]]:
    """デフォルトでProblem 067の三角形データを読み込み"""
    return get_problem_triangle()
