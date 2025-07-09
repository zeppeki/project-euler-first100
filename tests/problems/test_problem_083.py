"""Tests for Problem 083: Path sum: four ways"""

import pytest

from problems.problem_083 import solve_naive, solve_optimized


class TestProblem083:
    """Test suite for Problem 083 solutions."""

    def test_single_cell(self) -> None:
        """Test with single cell."""
        matrix = [[5]]
        assert solve_naive(matrix) == 5
        assert solve_optimized(matrix) == 5

    def test_single_row(self) -> None:
        """Test with single row."""
        matrix = [[1, 2, 3, 4]]
        # Path: 1 -> 2 -> 3 -> 4 = 10
        assert solve_naive(matrix) == 10
        assert solve_optimized(matrix) == 10

    def test_single_column(self) -> None:
        """Test with single column."""
        matrix = [[1], [2], [3], [4]]
        # Path: 1 -> 2 -> 3 -> 4 = 10
        assert solve_naive(matrix) == 10
        assert solve_optimized(matrix) == 10

    def test_2x2_matrix(self) -> None:
        """Test with 2x2 matrix."""
        matrix = [[1, 2], [3, 4]]
        # Best path: 1 -> 2 -> 4 = 7
        assert solve_naive(matrix) == 7
        assert solve_optimized(matrix) == 7

    def test_3x3_matrix(self) -> None:
        """Test with 3x3 matrix."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # Best path: 1 -> 2 -> 3 -> 6 -> 9 = 21
        assert solve_naive(matrix) == 21
        assert solve_optimized(matrix) == 21

    def test_example_from_problem(self) -> None:
        """Test with example from problem statement."""
        matrix = [
            [131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331],
        ]
        assert solve_naive(matrix) == 2297
        assert solve_optimized(matrix) == 2297

    def test_all_ones(self) -> None:
        """Test matrix with all ones."""
        matrix = [[1] * 5 for _ in range(5)]
        # Shortest path from top-left to bottom-right = 9 cells
        assert solve_naive(matrix) == 9
        assert solve_optimized(matrix) == 9

    def test_high_cost_barriers(self) -> None:
        """Test matrix with high cost barriers."""
        matrix = [[1, 1000, 1], [1, 1, 1], [1, 1000, 1]]
        # Best path avoids high cost cells
        assert solve_naive(matrix) == 5
        assert solve_optimized(matrix) == 5

    def test_zigzag_path(self) -> None:
        """Test where optimal path requires zigzag movement."""
        matrix = [[1, 10, 10, 10], [1, 1, 1, 10], [10, 10, 1, 1], [10, 10, 10, 1]]
        # Optimal path zigzags through 1s
        result_naive = solve_naive(matrix)
        result_optimized = solve_optimized(matrix)
        assert result_naive == result_optimized
        assert result_naive == 7  # Path of seven 1s

    def test_large_values(self) -> None:
        """Test with large values."""
        matrix = [[9999, 1, 9999], [1, 9999, 1], [9999, 1, 9999]]
        # Best path avoids large values
        result_naive = solve_naive(matrix)
        result_optimized = solve_optimized(matrix)
        assert result_naive == result_optimized

    def test_empty_matrix(self) -> None:
        """Test with empty matrix."""
        assert solve_naive([]) == 0
        assert solve_optimized([]) == 0
        assert solve_naive([[]]) == 0
        assert solve_optimized([[]]) == 0

    @pytest.mark.parametrize("size", [4, 5, 6])
    def test_various_sizes(self, size: int) -> None:
        """Test with various matrix sizes."""
        # Create a matrix where diagonal path is optimal
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(1)  # Diagonal has cost 1
                else:
                    row.append(100)  # Other cells have high cost
            matrix.append(row)

        # Optimal path follows diagonal
        result_naive = solve_naive(matrix)
        result_optimized = solve_optimized(matrix)
        assert result_naive == result_optimized
        # Diagonal path has 'size' cells, but we can't always follow diagonal
        # due to four-way movement constraints

    def test_optimal_requires_backtrack(self) -> None:
        """Test case where optimal path requires moving backwards."""
        matrix = [[1, 100, 1, 1], [1, 100, 100, 1], [1, 1, 1, 1], [100, 100, 100, 1]]
        # Optimal path may need to go down first then across
        result_naive = solve_naive(matrix)
        result_optimized = solve_optimized(matrix)
        assert result_naive == result_optimized
        assert result_naive < 400  # Should find efficient path

    @pytest.mark.slow
    def test_performance_10x10(self) -> None:
        """Test performance with 10x10 matrix."""
        matrix = [[i + j for j in range(10)] for i in range(10)]
        result_optimized = solve_optimized(matrix)
        # Verify result is reasonable
        assert result_optimized > 0
        assert result_optimized < 1000
