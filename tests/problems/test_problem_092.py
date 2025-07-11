#!/usr/bin/env python3
"""
Test for Problem 092: Square digit chains
"""

import pytest

from problems.problem_092 import (
    get_chain_destination,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    square_digit_sum,
)


class TestUtilityFunctions:
    """Test utility functions for square digit chains."""

    def test_square_digit_sum(self) -> None:
        """Test square digit sum calculation."""
        # Single digit
        assert square_digit_sum(4) == 16
        assert square_digit_sum(9) == 81

        # Multiple digits
        assert square_digit_sum(44) == 32  # 4² + 4² = 16 + 16 = 32
        assert square_digit_sum(85) == 89  # 8² + 5² = 64 + 25 = 89
        assert square_digit_sum(145) == 42  # 1² + 4² + 5² = 1 + 16 + 25 = 42
        assert square_digit_sum(32) == 13  # 3² + 2² = 9 + 4 = 13
        assert square_digit_sum(13) == 10  # 1² + 3² = 1 + 9 = 10
        assert square_digit_sum(10) == 1  # 1² + 0² = 1 + 0 = 1

        # Edge cases
        assert square_digit_sum(0) == 0
        assert square_digit_sum(1) == 1
        assert square_digit_sum(100) == 1  # 1² + 0² + 0² = 1

    def test_get_chain_destination(self) -> None:
        """Test chain destination calculation."""
        # Known examples from problem statement
        assert get_chain_destination(44) == 1  # 44 → 32 → 13 → 10 → 1
        assert get_chain_destination(85) == 89  # 85 → 89 → ...

        # Direct cases
        assert get_chain_destination(1) == 1
        assert get_chain_destination(89) == 89

        # Other test cases
        assert get_chain_destination(23) == 1  # 23 → 13 → 10 → 1
        assert get_chain_destination(145) == 89
        assert get_chain_destination(2) == 89
        assert get_chain_destination(3) == 89
        assert get_chain_destination(7) == 1
        assert get_chain_destination(10) == 1


class TestSolutionMethods:
    """Test solution methods with various inputs."""

    def test_small_cases(self) -> None:
        """Test solutions with small input values."""
        # Very small cases
        assert solve_naive(10) == 7  # Numbers 2,3,4,5,6,8,9 lead to 89
        assert solve_optimized(10) == 7
        assert solve_mathematical(10) == 7

        # Medium cases
        assert solve_naive(100) == 80
        assert solve_optimized(100) == 80
        assert solve_mathematical(100) == 80

    def test_solution_consistency(self) -> None:
        """Test that all solution methods give the same results."""
        test_limits = [50, 100, 500, 1000]

        for limit in test_limits:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            mathematical_result = solve_mathematical(limit)

            assert naive_result == optimized_result, (
                f"Naive vs Optimized mismatch at limit {limit}: "
                f"{naive_result} != {optimized_result}"
            )
            assert naive_result == mathematical_result, (
                f"Naive vs Mathematical mismatch at limit {limit}: "
                f"{naive_result} != {mathematical_result}"
            )

    @pytest.mark.slow
    def test_large_case(self) -> None:
        """Test with larger input (marked as slow)."""
        # Test with larger limit (this should be relatively fast with optimized solutions)
        result_optimized = solve_optimized(10000)
        result_mathematical = solve_mathematical(10000)

        assert result_optimized == result_mathematical
        assert result_optimized == 8558  # Expected value for limit 10000

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Limit of 1 (no numbers to check)
        assert solve_naive(1) == 0
        assert solve_optimized(1) == 0
        assert solve_mathematical(1) == 0

        # Limit of 2 (only number 1, which goes to 1, not 89)
        assert solve_naive(2) == 0
        assert solve_optimized(2) == 0
        assert solve_mathematical(2) == 0


class TestProblem092:
    """Test the main problem solution."""

    def test_known_values(self) -> None:
        """Test with known intermediate values."""
        # Test cases based on the problem examples and smaller limits
        test_cases = [
            (100, 80),  # 80 numbers below 100 arrive at 89
            (1000, 857),  # 857 numbers below 1000 arrive at 89
        ]

        for limit, expected in test_cases:
            # Test all methods
            assert solve_naive(limit) == expected
            assert solve_optimized(limit) == expected
            assert solve_mathematical(limit) == expected

    def test_individual_numbers(self) -> None:
        """Test specific numbers and their destinations."""
        # Numbers that should lead to 1
        ones_numbers = [1, 7, 10, 13, 19, 23, 44]

        # Numbers that should lead to 89
        eighty_nine_numbers = [
            2,
            3,
            4,
            5,
            6,
            8,
            9,
            11,
            12,
            14,
            15,
            16,
            17,
            18,
            20,
            85,
            89,
            145,
        ]

        for num in ones_numbers:
            assert get_chain_destination(num) == 1, f"Number {num} should lead to 1"

        for num in eighty_nine_numbers:
            assert get_chain_destination(num) == 89, f"Number {num} should lead to 89"

    def test_chain_properties(self) -> None:
        """Test properties of the chains."""
        # Test that every number eventually reaches 1 or 89
        for i in range(1, 1000):
            destination = get_chain_destination(i)
            assert destination in [1, 89], (
                f"Number {i} led to {destination}, not 1 or 89"
            )

    def test_square_sum_properties(self) -> None:
        """Test properties of square digit sums."""
        # Test that square digit sum is always positive for positive numbers
        for i in range(1, 100):
            assert square_digit_sum(i) > 0

        # Test that large numbers can have relatively small square digit sums
        assert square_digit_sum(1000000) == 1  # 1² + 0⁶ = 1
        assert square_digit_sum(9999999) == 567  # 7 × 9² = 7 × 81 = 567

        # Test specific values
        assert square_digit_sum(123) == 14  # 1² + 2² + 3² = 1 + 4 + 9 = 14
        assert square_digit_sum(999) == 243  # 3 × 9² = 3 × 81 = 243
