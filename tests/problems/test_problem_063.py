#!/usr/bin/env python3
"""Tests for Problem 063"""

from problems.problem_063 import (
    count_digits,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem063:
    """Test cases for Problem 063"""

    def test_count_digits(self) -> None:
        """Test digit counting function"""
        assert count_digits(0) == 1
        assert count_digits(9) == 1
        assert count_digits(10) == 2
        assert count_digits(99) == 2
        assert count_digits(100) == 3
        assert count_digits(16807) == 5  # 7^5
        assert count_digits(134217728) == 9  # 8^9

    def test_known_examples(self) -> None:
        """Test known examples from problem statement"""
        # 7^5 = 16807 is a 5-digit number
        assert 7**5 == 16807
        assert count_digits(16807) == 5

        # 8^9 = 134217728 is a 9-digit number
        assert 8**9 == 134217728
        assert count_digits(134217728) == 9

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0
        # We expect a reasonable number of powerful digit counts
        assert result < 1000  # Upper bound check

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0
        assert result < 1000  # Upper bound check

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution"""
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 0
        assert result < 1000  # Upper bound check

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        result_naive = solve_naive()
        result_optimized = solve_optimized()
        result_mathematical = solve_mathematical()

        assert result_naive == result_optimized == result_mathematical
        assert result_naive > 0
