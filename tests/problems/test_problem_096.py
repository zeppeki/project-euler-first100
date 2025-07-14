#!/usr/bin/env python3
"""
Test for Problem 096: Su Doku
"""

import pytest

from problems.lib.constraint_solving import (
    find_empty_cell,
    is_valid_sudoku_move,
    load_sudoku_puzzles,
    solve_sudoku_backtrack,
)
from problems.problem_096 import (
    get_top_left_number,
    solve_naive,
    solve_optimized,
    sudoku_backtrack_optimized,
    sudoku_solver_single,
)


class TestUtilityFunctions:
    """Test utility functions for Sudoku solving."""

    def test_load_sudoku_puzzles(self) -> None:
        """Test loading sudoku puzzles from file."""
        puzzles = load_sudoku_puzzles()

        # Should load 50 puzzles
        assert len(puzzles) == 50

        # Each puzzle should be 9x9
        for puzzle in puzzles:
            assert len(puzzle) == 9
            for row in puzzle:
                assert len(row) == 9
                # All values should be 0-9
                for cell in row:
                    assert 0 <= cell <= 9

    def test_is_valid_sudoku_move(self) -> None:
        """Test sudoku move validation."""
        # Simple test grid
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        # Test row constraint
        assert not is_valid_sudoku_move(grid, 0, 2, 5)  # 5 already in row 0
        assert not is_valid_sudoku_move(grid, 0, 2, 3)  # 3 already in row 0

        # Test column constraint
        assert not is_valid_sudoku_move(grid, 0, 2, 6)  # 6 already in column 2

        # Test box constraint
        assert not is_valid_sudoku_move(grid, 0, 2, 9)  # 9 already in top-left box

        # Test valid move
        assert is_valid_sudoku_move(grid, 0, 2, 4)  # 4 should be valid
        assert is_valid_sudoku_move(grid, 0, 2, 1)  # 1 should be valid

    def test_find_empty_cell(self) -> None:
        """Test finding empty cells."""
        # Grid with empty cells
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        # Should find first empty cell (0, 2)
        empty = find_empty_cell(grid)
        assert empty == (0, 2)

        # Filled grid should return None
        filled_grid = [[1] * 9 for _ in range(9)]
        assert find_empty_cell(filled_grid) is None

    def test_get_top_left_number(self) -> None:
        """Test extracting top-left 3-digit number."""
        grid = [
            [4, 8, 3, 9, 2, 1, 6, 5, 7],
            [9, 6, 7, 3, 4, 5, 8, 2, 1],
            [2, 5, 1, 8, 7, 6, 4, 9, 3],
            [5, 4, 8, 1, 3, 2, 9, 7, 6],
            [7, 2, 9, 5, 6, 4, 1, 3, 8],
            [1, 3, 6, 7, 9, 8, 2, 4, 5],
            [3, 7, 2, 6, 8, 9, 5, 1, 4],
            [8, 1, 4, 2, 5, 3, 7, 6, 9],
            [6, 9, 5, 4, 1, 7, 3, 8, 2],
        ]

        # Top-left should be 483
        assert get_top_left_number(grid) == 483


class TestSudokuSolvers:
    """Test sudoku solving algorithms."""

    def test_solve_sudoku_backtrack(self) -> None:
        """Test basic backtracking solver."""
        # Simple solvable puzzle
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        original_grid = [row[:] for row in grid]
        assert solve_sudoku_backtrack(grid)

        # Check that solution is valid
        assert find_empty_cell(grid) is None  # No empty cells

        # Check that original filled cells are unchanged
        for i in range(9):
            for j in range(9):
                if original_grid[i][j] != 0:
                    assert grid[i][j] == original_grid[i][j]

    def test_solve_sudoku_optimized(self) -> None:
        """Test optimized sudoku solver."""
        # Same puzzle as above
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        original_grid = [row[:] for row in grid]
        assert sudoku_backtrack_optimized(grid)

        # Check that solution is valid
        assert find_empty_cell(grid) is None  # No empty cells

        # Check that original filled cells are unchanged
        for i in range(9):
            for j in range(9):
                if original_grid[i][j] != 0:
                    assert grid[i][j] == original_grid[i][j]

    def test_sudoku_solver_single(self) -> None:
        """Test solving a single puzzle."""
        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        solved = sudoku_solver_single(puzzle)

        # Original puzzle should be unchanged
        assert puzzle[0][2] == 0  # Still empty

        # Solution should be complete
        assert find_empty_cell(solved) is None

        # Solution should be valid
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    assert solved[i][j] == puzzle[i][j]


class TestSolutionMethods:
    """Test solution methods with file input."""

    def test_solution_consistency(self) -> None:
        """Test that all solution methods give the same results."""
        # Load a subset for faster testing
        puzzles = load_sudoku_puzzles()
        if len(puzzles) >= 3:
            # Test with first 3 puzzles only for speed
            test_puzzles = puzzles[:3]

            # Calculate expected result
            expected_result = 0
            for puzzle in test_puzzles:
                solved = sudoku_solver_single(puzzle)
                expected_result += get_top_left_number(solved)

            # Create test file with just these puzzles
            import os
            import tempfile

            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".txt", delete=False
            ) as f:
                for i, puzzle in enumerate(test_puzzles):
                    f.write(f"Grid {i + 1:02d}\n")
                    for row in puzzle:
                        f.write("".join(map(str, row)) + "\n")
                test_file = f.name

            try:
                # Move test file to data directory with expected name
                data_dir = os.path.join(
                    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data"
                )
                test_data_file = os.path.join(data_dir, "test_sudoku.txt")
                os.rename(test_file, test_data_file)

                # Test all methods
                naive_result = solve_naive("test_sudoku.txt")
                optimized_result = solve_optimized("test_sudoku.txt")

                assert naive_result == optimized_result == expected_result

            finally:
                # Clean up
                if os.path.exists(test_data_file):
                    os.remove(test_data_file)

    def test_known_puzzles(self) -> None:
        """Test with known puzzle solutions."""
        puzzles = load_sudoku_puzzles()

        # Test first puzzle
        if puzzles:
            first_puzzle = puzzles[0]
            solved = sudoku_solver_single(first_puzzle)
            top_left = get_top_left_number(solved)

            # The first puzzle should be solvable
            assert top_left > 0
            assert len(str(top_left)) <= 3  # Should be a valid 3-digit number (or less)

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Already solved puzzle
        solved_puzzle = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]

        # Should "solve" instantly (no changes needed)
        result = sudoku_solver_single(solved_puzzle)
        assert result == solved_puzzle

    @pytest.mark.slow
    def test_full_problem(self) -> None:
        """Test solving all 50 puzzles (marked as slow)."""
        result = solve_optimized()

        # Should be a positive number
        assert result > 0

        # Expected answer for Project Euler Problem 96 (all 50 puzzles)
        assert result == 24702

    def test_solver_properties(self) -> None:
        """Test properties of the solvers."""
        puzzles = load_sudoku_puzzles()

        if puzzles:
            # Test that all puzzles are solvable
            sample_puzzles = puzzles[:5]  # Test first 5 for speed

            for i, puzzle in enumerate(sample_puzzles):
                solved = sudoku_solver_single(puzzle)

                # Solution should be complete
                assert find_empty_cell(solved) is None, (
                    f"Puzzle {i + 1} not completely solved"
                )

                # Solution should preserve original clues
                for row in range(9):
                    for col in range(9):
                        if puzzle[row][col] != 0:
                            assert solved[row][col] == puzzle[row][col], (
                                f"Original clue changed in puzzle {i + 1}"
                            )

                # Solution should be valid
                for row in range(9):
                    for col in range(9):
                        num = solved[row][col]
                        # Temporarily remove the number to test validity
                        solved[row][col] = 0
                        assert is_valid_sudoku_move(solved, row, col, num), (
                            f"Invalid solution in puzzle {i + 1} at ({row},{col})"
                        )
                        solved[row][col] = num


class TestProblem096:
    """Test the main problem solution."""

    def test_file_loading(self) -> None:
        """Test that the sudoku file loads correctly."""
        puzzles = load_sudoku_puzzles()

        # Should have exactly 50 puzzles
        assert len(puzzles) == 50

        # Each puzzle should have at least some empty cells initially
        for i, puzzle in enumerate(puzzles):
            empty_count = sum(row.count(0) for row in puzzle)
            assert empty_count > 0, f"Puzzle {i + 1} has no empty cells"
            assert empty_count < 81, f"Puzzle {i + 1} is completely empty"

    def test_solution_format(self) -> None:
        """Test that solutions have correct format."""
        puzzles = load_sudoku_puzzles()

        if puzzles:
            # Test first puzzle
            solved = sudoku_solver_single(puzzles[0])

            # Should be 9x9
            assert len(solved) == 9
            for row in solved:
                assert len(row) == 9

            # All cells should be filled with 1-9
            for row in solved:
                for cell in row:
                    assert 1 <= cell <= 9

    def test_main_problem_result(self) -> None:
        """Test the main problem result."""
        # The expected answer for all 50 puzzles is 24702
        result = solve_optimized()
        assert result == 24702

    def test_performance_characteristics(self) -> None:
        """Test performance characteristics of different approaches."""
        puzzles = load_sudoku_puzzles()

        if puzzles:
            # Test that optimized solver can handle multiple puzzles
            sample_puzzles = puzzles[:3]  # Small sample

            import time

            start_time = time.time()
            for puzzle in sample_puzzles:
                sudoku_solver_single(puzzle)
            total_time = time.time() - start_time

            # Should solve 3 puzzles in reasonable time (< 10 seconds)
            assert total_time < 10.0, f"Took too long: {total_time:.2f}s for 3 puzzles"

    def test_top_left_extraction(self) -> None:
        """Test extraction of top-left 3-digit numbers."""
        puzzles = load_sudoku_puzzles()

        if puzzles:
            solved = sudoku_solver_single(puzzles[0])
            top_left = get_top_left_number(solved)

            # Should be a valid 3-digit representation
            assert 0 <= top_left <= 999

            # First three cells should match the calculation
            expected = solved[0][0] * 100 + solved[0][1] * 10 + solved[0][2]
            assert top_left == expected
