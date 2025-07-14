"""
Problem 83: Path sum: four ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt,
a 31K text file containing an 80 by 80 matrix.

日本語：
左上から右下まで、左、右、上、下に移動して、最小パス合計を見つけます。
この問題は四方向への移動が可能なため、最短経路問題として解きます。
"""

from problems.lib.graph_algorithms import dijkstra_shortest_path
from problems.lib.matrix_utils import load_matrix


def solve_naive(matrix: list[list[int]] | None = None) -> int:
    """
    素直な解法：ライブラリのダイクストラ法を使用
    時間計算量：O(m*n*log(m*n))
    空間計算量：O(m*n)

    Args:
        matrix: 2次元配列の行列（Noneの場合はファイルから読み込み）

    Returns:
        左上から右下への最小経路の合計
    """
    if matrix is None:
        matrix = load_matrix("p083_matrix.txt")
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    distance, _ = dijkstra_shortest_path(
        matrix, (0, 0), (rows - 1, cols - 1), directions
    )
    return int(distance) if distance != float("inf") else 0


def solve_optimized(matrix: list[list[int]] | None = None) -> int:
    """
    最適化解法：ライブラリのダイクストラ法を使用（同じ実装）
    時間計算量：O(m*n*log(m*n))
    空間計算量：O(m*n)

    Args:
        matrix: 2次元配列の行列（Noneの場合はファイルから読み込み）

    Returns:
        左上から右下への最小経路の合計
    """
    if matrix is None:
        matrix = load_matrix("p083_matrix.txt")
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    distance, _ = dijkstra_shortest_path(
        matrix, (0, 0), (rows - 1, cols - 1), directions
    )
    return int(distance) if distance != float("inf") else 0
