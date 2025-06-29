#!/usr/bin/env python3
"""
Problem 018: Maximum Path Sum I

By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle of 15 rows below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67, is the same challenge with a
triangle containing one-hundred rows; it cannot be solved by brute force,
and requires a clever method! ;o)

Answer: 1074
"""


def parse_triangle(triangle_str: str) -> list[list[int]]:
    """
    三角形の文字列表現を数値の二次元リストに変換

    Args:
        triangle_str: 三角形の文字列表現

    Returns:
        数値の二次元リスト
    """
    lines = triangle_str.strip().split("\n")
    triangle = []

    for line in lines:
        row = [int(x) for x in line.split()]
        triangle.append(row)

    return triangle


def solve_naive(triangle: list[list[int]]) -> int:
    """
    素直な解法: 全経路を探索してブルートフォースで最大値を求める

    時間計算量: O(2^n) - 指数時間
    空間計算量: O(n) - 再帰スタック

    Args:
        triangle: 三角形の数値配列

    Returns:
        最大パス合計
    """

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


def solve_optimized(triangle: list[list[int]]) -> int:
    """
    最適化解法: 動的プログラミング（メモ化）で効率的に計算

    時間計算量: O(n^2)
    空間計算量: O(n^2)

    Args:
        triangle: 三角形の数値配列

    Returns:
        最大パス合計
    """
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


def solve_mathematical(triangle: list[list[int]]) -> int:
    """
    数学的解法: ボトムアップ動的プログラミングで最適化

    時間計算量: O(n^2)
    空間計算量: O(n) - インプレース更新

    Args:
        triangle: 三角形の数値配列

    Returns:
        最大パス合計
    """
    # 三角形をコピーして破壊的変更を避ける
    dp = [row[:] for row in triangle]

    # 底辺から上に向かって計算
    for i in range(len(dp) - 2, -1, -1):  # 下から2番目の行から上へ
        for j in range(len(dp[i])):
            # 現在位置の値 + 下の行の隣接する2つのうち大きい方
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]


def get_problem_triangle() -> list[list[int]]:
    """Problem 018の三角形データを取得"""
    triangle_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

    return parse_triangle(triangle_str)


def get_example_triangle() -> list[list[int]]:
    """例題の小さな三角形データを取得"""
    triangle_str = """3
7 4
2 4 6
8 5 9 3"""

    return parse_triangle(triangle_str)
