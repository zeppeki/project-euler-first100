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

import heapq
from collections import deque


def load_matrix(filename: str = "data/p083_matrix.txt") -> list[list[int]]:
    """Load matrix from file."""
    from pathlib import Path

    file_path = Path(__file__).parent.parent / filename
    matrix = []
    with open(file_path) as f:
        for line in f:
            row = [int(x) for x in line.strip().split(",")]
            matrix.append(row)
    return matrix


def solve_naive(matrix: list[list[int]] | None = None) -> int:
    """
    素直な解法：BFSを使用してすべての可能なパスを探索
    時間計算量：O(4^(m*n)) - 最悪の場合
    空間計算量：O(m*n)

    Args:
        matrix: 2次元配列の行列（Noneの場合はファイルから読み込み）

    Returns:
        左上から右下への最小経路の合計
    """
    if matrix is None:
        matrix = load_matrix()
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    # BFS with distance tracking
    queue = deque([(0, 0, matrix[0][0])])  # (row, col, distance)
    visited = {(0, 0): matrix[0][0]}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while queue:
        row, col, dist = queue.popleft()

        # If we reached the destination
        if row == rows - 1 and col == cols - 1:
            continue

        # Try all four directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                new_dist = dist + matrix[new_row][new_col]

                # If we found a shorter path to this cell
                if (new_row, new_col) not in visited or new_dist < visited[
                    (new_row, new_col)
                ]:
                    visited[(new_row, new_col)] = new_dist
                    queue.append((new_row, new_col, new_dist))

    return visited.get((rows - 1, cols - 1), 0)


def solve_optimized(matrix: list[list[int]] | None = None) -> int:
    """
    最適化解法：ダイクストラ法を使用した最短経路探索
    時間計算量：O(m*n*log(m*n))
    空間計算量：O(m*n)

    Args:
        matrix: 2次元配列の行列（Noneの場合はファイルから読み込み）

    Returns:
        左上から右下への最小経路の合計
    """
    if matrix is None:
        matrix = load_matrix()
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    # Priority queue: (distance, row, col)
    pq = [(matrix[0][0], 0, 0)]
    distances = {(0, 0): matrix[0][0]}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while pq:
        current_dist, row, col = heapq.heappop(pq)

        # If we reached the destination
        if row == rows - 1 and col == cols - 1:
            return current_dist

        # Skip if we've already found a better path
        if current_dist > distances.get((row, col), float("inf")):
            continue

        # Try all four directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                new_dist = current_dist + matrix[new_row][new_col]

                # If we found a shorter path
                if new_dist < distances.get((new_row, new_col), float("inf")):
                    distances[(new_row, new_col)] = new_dist
                    heapq.heappush(pq, (new_dist, new_row, new_col))

    return distances.get((rows - 1, cols - 1), 0)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    # Example from problem statement
    test_matrix = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]

    naive_result = solve_naive(test_matrix)
    optimized_result = solve_optimized(test_matrix)

    print(f"Test matrix result (naive): {naive_result}")
    print(f"Test matrix result (optimized): {optimized_result}")
    assert naive_result == optimized_result == 2297, (
        f"Test failed: expected 2297, got {naive_result}/{optimized_result}"
    )
    print("✓ Test passed!")


def main() -> None:
    """メイン関数"""
    import time

    # Run test cases
    print("Running test cases...")
    test_solutions()
    print()

    # Load the actual problem data
    try:
        matrix = load_matrix("data/p083_matrix.txt")
        print(f"Loaded {len(matrix)}x{len(matrix[0])} matrix")

        # Solve with optimized method (naive would be too slow for 80x80)
        print("\nSolving with optimized method...")
        start = time.time()
        result = solve_optimized(matrix)
        elapsed = time.time() - start

        print(f"Result: {result}")
        print(f"Time: {elapsed:.4f} seconds")

    except FileNotFoundError:
        print("Matrix file not found. Please ensure data/p083_matrix.txt exists.")
        print("Running with example data only.")


if __name__ == "__main__":
    main()
