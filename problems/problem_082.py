"""
Problem 82: Path sum: three ways

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing
in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing an 80 by 80 matrix.

日本語：
左の列の任意のセルから開始し、右の列の任意のセルで終了し、上、下、右にのみ移動して、
5×5のマトリックスの最小パス合計を見つけます。80×80のマトリックスでこの問題を解きます。
"""


def load_matrix(filename: str = "data/p082_matrix.txt") -> list[list[int]]:
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
    素直な解法：再帰的にすべての可能なパスを探索
    時間計算量：O(3^(m*n)) - 各セルで最大3つの選択肢
    空間計算量：O(m*n) - 再帰スタック

    Args:
        matrix: 2次元配列の行列（Noneの場合はファイルから読み込み）

    Returns:
        左列から右列への最小経路の合計
    """
    if matrix is None:
        matrix = load_matrix()
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    min_sum = 10**18  # Large number instead of infinity

    def dfs(row: int, col: int, current_sum: int, visited: set) -> None:
        nonlocal min_sum

        # Add current cell to sum
        current_sum += matrix[row][col]

        # If we reached the rightmost column, update min_sum
        if col == cols - 1:
            min_sum = min(min_sum, current_sum)
            return

        # Early pruning
        if current_sum >= min_sum:
            return

        # Mark as visited
        visited.add((row, col))

        # Try moving right
        if col + 1 < cols and (row, col + 1) not in visited:
            dfs(row, col + 1, current_sum, visited)

        # Try moving up
        if row - 1 >= 0 and (row - 1, col) not in visited:
            dfs(row - 1, col, current_sum, visited)

        # Try moving down
        if row + 1 < rows and (row + 1, col) not in visited:
            dfs(row + 1, col, current_sum, visited)

        # Backtrack
        visited.remove((row, col))

    # Try starting from each cell in the first column
    for start_row in range(rows):
        dfs(start_row, 0, 0, set())

    return min_sum


def solve_optimized(matrix: list[list[int]] | None = None) -> int:
    """
    最適化解法：動的計画法を使用して効率的に解く
    時間計算量：O(m*n)
    空間計算量：O(m)

    Args:
        matrix: 2次元配列の行列（Noneの場合はファイルから読み込み）

    Returns:
        左列から右列への最小経路の合計
    """
    if matrix is None:
        matrix = load_matrix()
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    # dp[i] represents the minimum path sum to reach row i in the current column
    dp: list[int | float] = [matrix[i][0] for i in range(rows)]

    # Process each column from left to right
    for col in range(1, cols):
        new_dp = [float("inf")] * rows

        # For each row in the current column
        for row in range(rows):
            # Option 1: Come from the left (same row, previous column)
            new_dp[row] = dp[row] + matrix[row][col]

            # Option 2: Come from above (accumulate downward)
            temp_sum = new_dp[row]
            for r in range(row - 1, -1, -1):
                temp_sum += matrix[r][col]
                new_dp[r] = min(new_dp[r], temp_sum)

            # Option 3: Come from below (accumulate upward)
            temp_sum = new_dp[row]
            for r in range(row + 1, rows):
                temp_sum += matrix[r][col]
                new_dp[r] = min(new_dp[r], temp_sum)

        dp = new_dp

    # Return the minimum value in the last column
    return int(min(dp))
