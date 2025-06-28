#!/usr/bin/env python3
"""Tests for Problem 035"""

import pytest

from problems.problem_035 import solve_naive, solve_optimized


class TestProblem035:
    """Test cases for Problem 035"""

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        # Test cases with known results
        assert solve_naive(10) == 4  # 2, 3, 5, 7
        assert solve_naive(100) == 13  # Given in problem statement

        # Edge cases
        assert solve_naive(2) == 0  # No primes below 2
        assert solve_naive(3) == 1  # Only 2 is circular prime below 3

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        # Test cases with known results
        assert solve_optimized(10) == 4  # 2, 3, 5, 7
        assert solve_optimized(100) == 13  # Given in problem statement

        # Edge cases
        assert solve_optimized(2) == 0  # No primes below 2
        assert solve_optimized(3) == 1  # Only 2 is circular prime below 3

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        # Test on smaller inputs to ensure solutions agree
        test_cases = [10, 50, 100, 1000]

        for limit in test_cases:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)

            assert naive_result == optimized_result, (
                f"Solutions disagree for limit {limit}: naive={naive_result}, optimized={optimized_result}"
            )

    @pytest.mark.slow
    def test_final_answer(self) -> None:
        """Test the final answer for the problem"""
        # This is the actual problem: circular primes below 1,000,000
        result = solve_optimized(1000000)
        assert result == 55  # Expected answer

        # Verify naive solution agrees (but only test on smaller input for speed)
        assert solve_naive(10000) == solve_optimized(10000)
