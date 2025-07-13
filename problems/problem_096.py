#!/usr/bin/env python3
"""
Problem 096: Su Doku

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a
similar, and much more difficult, puzzle idea called Latin Squares. The objective of
Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in
such that each row, column, and 3 by 3 box contains each of the digits 1 to 9.

Below, I include an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
although it may be necessary to employ "guess and test" methods in order to eliminate
options (there is much contested opinion over this). The complexity of the search
determines the difficulty of the puzzle; the example above is considered Easy because
it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt, contains fifty different Su Doku puzzles ranging in
difficulty, but all with unique solutions.

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top
left corner of each solution grid.
"""

from problems.lib.constraint_solving import (
    is_valid_sudoku_move,
    load_sudoku_puzzles,
    solve_sudoku_backtrack as sudoku_backtrack,
)


def sudoku_backtrack_optimized(grid: list[list[int]]) -> bool:
    """
    最適化されたバックトラッキング解法（最小残可能値ヒューリスティック）
    時間計算量: O(9^(n*n)) but typically much faster
    空間計算量: O(n*n)
    """

    def get_possible_values(row: int, col: int) -> set[int]:
        """指定されたセルに配置可能な値を取得"""
        possible = set(range(1, 10))

        # Remove values in same row
        for j in range(9):
            possible.discard(grid[row][j])

        # Remove values in same column
        for i in range(9):
            possible.discard(grid[i][col])

        # Remove values in same 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                possible.discard(grid[i][j])

        return possible

    def find_best_cell() -> tuple[int, int, set[int]] | None:
        """最小残可能値を持つ空のセルを見つける"""
        best_cell = None
        min_possibilities = 10

        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    possible = get_possible_values(i, j)
                    if len(possible) < min_possibilities:
                        min_possibilities = len(possible)
                        best_cell = (i, j, possible)
                        if min_possibilities == 0:
                            return best_cell  # Impossible to fill

        return best_cell

    cell_info = find_best_cell()
    if cell_info is None:
        return True  # All cells filled

    row, col, possible_values = cell_info
    if not possible_values:
        return False  # No valid values

    for num in possible_values:
        if is_valid_sudoku_move(grid, row, col, num):
            grid[row][col] = num

            if sudoku_backtrack_optimized(grid):
                return True

            # Backtrack
            grid[row][col] = 0

    return False


def get_top_left_number(grid: list[list[int]]) -> int:
    """
    グリッドの左上3桁の数字を取得
    時間計算量: O(1)
    空間計算量: O(1)
    """
    return grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]


def solve_naive(filename: str = "p096_sudoku.txt") -> int:
    """
    素直な解法: 基本的なバックトラッキング
    時間計算量: O(k * 9^(n*n)) where k is number of puzzles
    空間計算量: O(n*n)
    """
    puzzles = load_sudoku_puzzles(filename)
    total_sum = 0

    for i, puzzle in enumerate(puzzles):
        # Create a copy to avoid modifying original
        grid = [row[:] for row in puzzle]

        if sudoku_backtrack(grid):
            total_sum += get_top_left_number(grid)
        else:
            raise ValueError(f"Puzzle {i + 1} has no solution")

    return total_sum


def solve_optimized(filename: str = "p096_sudoku.txt") -> int:
    """
    最適化解法: 最小残可能値ヒューリスティック
    時間計算量: O(k * 9^(n*n)) but typically much faster
    空間計算量: O(n*n)
    """
    puzzles = load_sudoku_puzzles(filename)
    total_sum = 0

    for i, puzzle in enumerate(puzzles):
        # Create a copy to avoid modifying original
        grid = [row[:] for row in puzzle]

        if sudoku_backtrack_optimized(grid):
            total_sum += get_top_left_number(grid)
        else:
            raise ValueError(f"Puzzle {i + 1} has no solution")

    return total_sum


def solve_mathematical(filename: str = "p096_sudoku.txt") -> int:
    """
    数学的解法: この問題では最適化解法と同じ（数独は組み合わせ問題）
    時間計算量: O(k * 9^(n*n)) but typically much faster
    空間計算量: O(n*n)
    """
    return solve_optimized(filename)


def sudoku_solver_single(puzzle: list[list[int]]) -> list[list[int]]:
    """
    単一の数独パズルを解く（テスト用）
    時間計算量: O(9^(n*n))
    空間計算量: O(n*n)
    """
    grid = [row[:] for row in puzzle]
    if sudoku_backtrack_optimized(grid):
        return grid
    raise ValueError("Puzzle has no solution")


def main() -> None:
    """メイン実行関数"""
    import time

    # Small example with first few puzzles
    puzzles = load_sudoku_puzzles()
    print(f"Loaded {len(puzzles)} puzzles")

    # Solve first puzzle as example
    if puzzles:
        print("\nFirst puzzle:")
        for row in puzzles[0]:
            print("".join(map(str, row)))

        solved = sudoku_solver_single(puzzles[0])
        print("\nSolved:")
        for row in solved:
            print("".join(map(str, row)))

        top_left = get_top_left_number(solved)
        print(f"\nTop-left 3-digit number: {top_left}")

    # Solve all puzzles
    print("\nSolving all 50 puzzles...")
    start_time = time.time()
    result = solve_optimized()
    print(f"Sum of all top-left 3-digit numbers: {result}")
    print(f"Time: {time.time() - start_time:.3f}s")


if __name__ == "__main__":
    main()
