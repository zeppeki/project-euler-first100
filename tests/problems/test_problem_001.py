"""Tests for Problem 001: Multiples of 3 and 5."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_001 import solve_naive, solve_optimized


class TestProblem001:
    """Test cases for Problem 001."""

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (10, 23),  # 3 + 5 + 6 + 9 = 23
            (20, 78),  # 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
            (100, 2318),  # Known result for limit 100
        ],
    )
    def test_solve_naive(self, limit: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit {limit}"
        )

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (10, 23),  # 3 + 5 + 6 + 9 = 23
            (20, 78),  # 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
            (100, 2318),  # Known result for limit 100
        ],
    )
    def test_solve_optimized(self, limit: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit {limit}"
        )

    @pytest.mark.parametrize("limit", [10, 20, 50, 100])
    def test_all_solutions_agree(self, limit: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(limit)
        optimized_result = solve_optimized(limit)
        assert naive_result == optimized_result, (
            f"Solutions disagree for limit {limit}: "
            f"naive={naive_result}, optimized={optimized_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with limit 0
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0

        # Test with limit 1
        assert solve_naive(1) == 0
        assert solve_optimized(1) == 0

        # Test with limit 2
        assert solve_naive(2) == 0
        assert solve_optimized(2) == 0

    def test_negative_input(self) -> None:
        """Test with negative input (should handle gracefully)."""
        # All solutions should handle negative input gracefully
        assert solve_naive(-10) == 0
        assert solve_optimized(-10) == 0

    def test_problem_answer(self) -> None:
        """Test with the actual problem limit (optimized for speed)."""
        # Test with the actual problem limit
        limit = 1000
        expected = 233168

        # Only test optimized solution for speed, then verify naive agrees
        result_optimized = solve_optimized(limit)
        assert result_optimized == expected

        # Verify both solutions agree (quick check)
        result_naive = solve_naive(limit)
        assert result_naive == result_optimized
