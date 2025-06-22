"""Tests for Problem 003: Largest prime factor."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problem_003 import solve_mathematical, solve_naive, solve_optimized  # noqa: E402


class TestProblem003:
    """Test cases for Problem 003."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (13195, 29),  # Example: 5, 7, 13, 29 → max is 29
            (100, 5),  # 100 = 2^2 × 5^2 → max is 5
            (84, 7),  # 84 = 2^2 × 3 × 7 → max is 7
        ],
    )
    def test_solve_naive(self, n: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (13195, 29),  # Example: 5, 7, 13, 29 → max is 29
            (100, 5),  # 100 = 2^2 × 5^2 → max is 5
            (84, 7),  # 84 = 2^2 × 3 × 7 → max is 7
        ],
    )
    def test_solve_optimized(self, n: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (13195, 29),  # Example: 5, 7, 13, 29 → max is 29
            (100, 5),  # 100 = 2^2 × 5^2 → max is 5
            (84, 7),  # 84 = 2^2 × 3 × 7 → max is 7
        ],
    )
    def test_solve_mathematical(self, n: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize("n", [13195, 100, 84, 17, 25])
    def test_all_solutions_agree(self, n: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(n)
        optimized_result = solve_optimized(n)
        math_result = solve_mathematical(n)

        assert naive_result == optimized_result == math_result, (
            f"Solutions disagree for n={n}: "
            f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with n = 1
        assert solve_naive(1) == 1
        assert solve_optimized(1) == 1
        assert solve_mathematical(1) == 1

        # Test with n = 2
        assert solve_naive(2) == 2
        assert solve_optimized(2) == 2
        assert solve_mathematical(2) == 2

        # Test with n = 0 (should handle gracefully)
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0
        assert solve_mathematical(0) == 0

    def test_negative_input(self) -> None:
        """Test with negative input (should handle gracefully)."""
        # All solutions should handle negative input gracefully
        assert solve_naive(-10) == 0
        assert solve_optimized(-10) == 0
        assert solve_mathematical(-10) == 0

    @pytest.mark.parametrize("prime", [17, 19, 23, 29, 31])
    def test_prime_numbers(self, prime: int) -> None:
        """Test with prime numbers."""
        assert solve_naive(prime) == prime
        assert solve_optimized(prime) == prime
        assert solve_mathematical(prime) == prime

    @pytest.mark.slow
    def test_large_number(self) -> None:
        """Test with a large number (marked as slow)."""
        # Test with the actual problem number
        n = 600851475143
        expected = 6857

        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)

        assert result_naive == expected
        assert result_optimized == expected
        assert result_math == expected
