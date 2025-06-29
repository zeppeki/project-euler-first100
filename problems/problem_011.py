#!/usr/bin/env python3
"""
Problem 011: Largest product in a grid

In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?

Answer: 70600674
"""

# 20×20グリッドデータ
GRID_DATA = [
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48],
]

# 方向ベクトル（右、下、右下、左下）
DIRECTIONS = [
    (0, 1),  # 右
    (1, 0),  # 下
    (1, 1),  # 右下
    (1, -1),  # 左下
]


def is_valid_position(row: int, col: int, grid: list[list[int]]) -> bool:
    """位置がグリッド内かどうかをチェック"""
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def get_product_in_direction(
    grid: list[list[int]],
    start_row: int,
    start_col: int,
    direction: tuple[int, int],
    length: int,
) -> int:
    """指定された方向の積を計算"""
    dr, dc = direction
    product = 1

    for i in range(length):
        row = start_row + i * dr
        col = start_col + i * dc

        if not is_valid_position(row, col, grid):
            return 0

        product *= grid[row][col]

    return product


def solve_naive(grid: list[list[int]], length: int = 4) -> int:
    """
    素直な解法: 全方向の全位置から隣接する数の積をチェック
    時間計算量: O(rows × cols × directions × length)
    空間計算量: O(1)
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_product = 0

    # 各位置から各方向の積を計算
    for row in range(rows):
        for col in range(cols):
            for direction in DIRECTIONS:
                product = get_product_in_direction(grid, row, col, direction, length)
                max_product = max(max_product, product)

    return max_product


def solve_optimized(grid: list[list[int]], length: int = 4) -> int:
    """
    最適化解法: 境界チェックを最適化し、早期終了を活用
    時間計算量: O(rows × cols × directions × length)
    空間計算量: O(1)
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_product = 0

    # 各方向について、有効な開始位置のみをチェック
    for direction in DIRECTIONS:
        dr, dc = direction

        # この方向で有効な開始位置の範囲を計算
        start_rows = range(rows - (length - 1) * max(0, dr))
        start_cols = range(cols - (length - 1) * max(0, dc))

        for row in start_rows:
            for col in start_cols:
                product = 1
                valid = True

                # 4つの隣接する数をチェック
                for i in range(length):
                    r = row + i * dr
                    c = col + i * dc

                    if not is_valid_position(r, c, grid):
                        valid = False
                        break

                    product *= grid[r][c]

                if valid:
                    max_product = max(max_product, product)

    return max_product


def solve_mathematical(grid: list[list[int]], length: int = 4) -> int:
    """
    数学的解法: 方向ごとに最適化された探索
    各方向の特性を活用して効率的に探索
    時間計算量: O(rows × cols × directions)
    空間計算量: O(1)
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_product = 0

    # 方向ごとに最適化された探索
    directions_info = [
        # (dr, dc, row_range, col_range, description)
        (0, 1, range(rows), range(cols - length + 1), "水平方向"),
        (1, 0, range(rows - length + 1), range(cols), "垂直方向"),
        (1, 1, range(rows - length + 1), range(cols - length + 1), "右下対角線"),
        (1, -1, range(length - 1, rows), range(length - 1, cols), "左下対角線"),
    ]

    for dr, dc, row_range, col_range, _ in directions_info:
        for row in row_range:
            for col in col_range:
                product = 1

                for i in range(length):
                    r = row + i * dr
                    c = col + i * dc
                    # 行と列の両方の境界をチェック
                    if not (0 <= r < rows and 0 <= c < cols):
                        product = 0
                        break
                    product *= grid[r][c]

                max_product = max(max_product, product)

    return max_product


def find_max_product_sequence(
    grid: list[list[int]], length: int = 4
) -> tuple[int, list[int], str]:
    """
    最大積となるシーケンスとその方向を返すヘルパー関数
    """
    if not grid or not grid[0]:
        return 0, [], ""

    rows, cols = len(grid), len(grid[0])
    max_product = 0
    max_sequence = []
    max_direction = ""

    directions_info = [
        (0, 1, "水平方向"),
        (1, 0, "垂直方向"),
        (1, 1, "右下対角線"),
        (1, -1, "左下対角線"),
    ]

    for dr, dc, desc in directions_info:
        # この方向で有効な開始位置の範囲を計算
        if dr == 0:  # 水平方向
            row_range = range(rows)
            col_range = range(cols - length + 1)
        elif dc == 0:  # 垂直方向
            row_range = range(rows - length + 1)
            col_range = range(cols)
        elif dc > 0:  # 右下対角線
            row_range = range(rows - length + 1)
            col_range = range(cols - length + 1)
        else:  # 左下対角線
            row_range = range(length - 1, rows)
            col_range = range(length - 1, cols)

        for row in row_range:
            for col in col_range:
                sequence = []
                product = 1

                for i in range(length):
                    r = row + i * dr
                    c = col + i * dc
                    sequence.append(grid[r][c])
                    product *= grid[r][c]

                if product > max_product:
                    max_product = product
                    max_sequence = sequence
                    max_direction = desc

    return max_product, max_sequence, max_direction
