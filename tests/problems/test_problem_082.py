"""Tests for Problem 082: Path sum: three ways"""

import pytest

from problems.problem_082 import solve_naive, solve_optimized


class TestProblem082:
    """Test suite for Problem 082 solutions."""

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
        # Best path is to start at row 0: 1
        assert solve_naive(matrix) == 1
        assert solve_optimized(matrix) == 1

    def test_2x2_matrix(self) -> None:
        """Test with 2x2 matrix."""
        matrix = [[1, 2], [3, 4]]
        # Best path: start at (0,0): 1 -> 2 = 3
        assert solve_naive(matrix) == 3
        assert solve_optimized(matrix) == 3

    def test_3x3_matrix(self) -> None:
        """Test with 3x3 matrix."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # Best path: start at (0,0): 1 -> 2 -> 3 = 6
        assert solve_naive(matrix) == 6
        assert solve_optimized(matrix) == 6

    def test_example_from_problem(self) -> None:
        """Test with example from problem statement."""
        matrix = [
            [131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331],
        ]
        assert solve_naive(matrix) == 994
        assert solve_optimized(matrix) == 994

    def test_diagonal_preference(self) -> None:
        """Test matrix where diagonal movement is preferred."""
        matrix = [[10, 1, 1, 100], [1, 10, 1, 100], [1, 1, 10, 100], [100, 100, 100, 1]]
        # Best path involves moving up/down to follow low values
        result_naive = solve_naive(matrix)
        result_optimized = solve_optimized(matrix)
        assert result_naive == result_optimized
        assert result_naive < 400  # Should find path better than straight across

    def test_all_ones(self) -> None:
        """Test matrix with all ones."""
        matrix = [[1] * 5 for _ in range(5)]
        # Any path from left to right has same cost = 5
        assert solve_naive(matrix) == 5
        assert solve_optimized(matrix) == 5

    def test_high_cost_barriers(self) -> None:
        """Test matrix with high cost barriers."""
        matrix = [[1, 1000, 1], [1, 1, 1], [1, 1000, 1]]
        # Best path: (1,0) -> (1,1) -> (1,2) = 3
        assert solve_naive(matrix) == 3
        assert solve_optimized(matrix) == 3

    def test_large_values(self) -> None:
        """Test with large values."""
        matrix = [[9999, 1, 9999], [1, 9999, 1], [9999, 1, 9999]]
        # Best path involves careful navigation
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
        # Create a matrix where optimal path is along the top row
        matrix = []
        for i in range(size):
            row = []
            for _ in range(size):
                if i == 0:
                    row.append(1)  # Top row has cost 1
                else:
                    row.append(100)  # Other rows have high cost
            matrix.append(row)

        # Optimal path is along top row: cost = size
        assert solve_naive(matrix) == size
        assert solve_optimized(matrix) == size

    def test_zigzag_optimal_path(self) -> None:
        """Test where optimal path requires zigzag movement."""
        matrix = [[1, 100, 100, 1], [1, 1, 1, 100], [100, 100, 1, 1], [1, 1, 1, 1]]
        # Optimal path requires moving up and down
        result_naive = solve_naive(matrix)
        result_optimized = solve_optimized(matrix)
        assert result_naive == result_optimized
        assert result_naive < 20  # Should find efficient zigzag path

    @pytest.mark.slow
    def test_performance_10x10(self) -> None:
        """Test performance with 10x10 matrix."""
        matrix = [[i + j for j in range(10)] for i in range(10)]
        result_optimized = solve_optimized(matrix)
        # Verify result is reasonable
        assert result_optimized > 0
        assert result_optimized < 1000
