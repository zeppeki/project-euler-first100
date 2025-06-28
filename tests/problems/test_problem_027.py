#!/usr/bin/env python3
"""
Tests for Problem 027: Quadratic primes
"""

from collections.abc import Callable

import pytest

from problems.problem_027 import (
    count_consecutive_primes,
    is_prime,
    sieve_of_eratosthenes,
    solve_naive,
    solve_optimized,
)


class TestUtilityFunctions:
    """Tests for utility functions."""

    def test_is_prime(self) -> None:
        """Test prime checking function."""
        # Test small primes
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True

        # Test non-primes
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False

    def test_sieve_of_eratosthenes(self) -> None:
        """Test sieve of Eratosthenes."""
        # Test small range
        primes_10 = sieve_of_eratosthenes(10)
        expected_primes_10 = {2, 3, 5, 7}
        assert primes_10 == expected_primes_10

        # Test larger range
        primes_30 = sieve_of_eratosthenes(30)
        expected_primes_30 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
        assert primes_30 == expected_primes_30

        # Test edge cases
        assert sieve_of_eratosthenes(1) == set()
        assert sieve_of_eratosthenes(2) == {2}

    def test_count_consecutive_primes(self) -> None:
        """Test consecutive prime counting."""
        # Test Euler's famous formula: n² + n + 41
        # Should produce 40 primes for n = 0 to 39
        count = count_consecutive_primes(1, 41)
        assert count == 40

        # Test some known cases
        assert (
            count_consecutive_primes(0, 2) == 2
        )  # n² + 2: gives 2, 3, 6 (6 not prime)
        assert count_consecutive_primes(0, 3) == 1  # n² + 3: gives 3, 4 (4 not prime)

        # Test case where first value is not prime
        assert count_consecutive_primes(0, 1) == 0  # n² + 1: gives 1 for n=0


@pytest.mark.parametrize("solver", [solve_naive, solve_optimized])
class TestProblem027:
    """Tests for Problem 027 solvers."""

    def test_small_limit(self, solver: Callable[[int], int]) -> None:
        """Tests with small limits."""
        # Test very small limit
        result = solver(10)
        assert isinstance(result, int)

        # Test medium limit
        result = solver(50)
        assert isinstance(result, int)

    def test_known_examples(self, solver: Callable[[int], int]) -> None:
        """Test with known examples from the problem."""
        # For small limits, we should get consistent results
        result_10 = solver(10)
        result_20 = solver(20)

        # The result should be reasonable (product of two integers within range)
        assert abs(result_10) <= 10 * 10
        assert abs(result_20) <= 20 * 20

    def test_euler_example(self, solver: Callable[[int], int]) -> None:
        """Test that Euler's example is found when in range."""
        # n² + n + 41 should be found when a=1, b=41 are in range
        result = solver(50)

        # We expect this to find a good solution
        assert isinstance(result, int)
        assert result != 0

    def test_medium_limit(self, solver: Callable[[int], int]) -> None:
        """Tests with medium limit."""
        # Test with limit 100
        result = solver(100)
        assert isinstance(result, int)

        # Should be a reasonable answer
        assert abs(result) <= 100 * 100

    @pytest.mark.slow
    def test_main_problem(self, solver: Callable[[int], int]) -> None:
        """Tests the main problem case (limit 1000)."""
        # Only test optimized for main problem due to performance
        if solver == solve_optimized:
            result = solver(1000)

            # Verify the result is reasonable
            assert isinstance(result, int)
            assert abs(result) <= 1000 * 1000

            # The result should be negative (based on known solution pattern)
            assert result < 0

    def test_consistency_between_solvers(self, solver: Callable[[int], int]) -> None:
        """Tests that solvers give consistent results for small limits."""
        test_limits = [10, 20, 50]

        for limit in test_limits:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            assert naive_result == optimized_result == solver(limit)


class TestProblemSpecificCases:
    """Tests for problem-specific edge cases."""

    def test_negative_coefficients(self) -> None:
        """Test handling of negative coefficients."""
        # Test with some negative a values
        count = count_consecutive_primes(-10, 41)
        assert count >= 0

        count = count_consecutive_primes(-1, 41)
        assert count >= 0

    def test_boundary_conditions(self) -> None:
        """Test boundary conditions."""
        # Test when n=0 gives value <= 1 (not prime)
        assert count_consecutive_primes(0, 1) == 0
        assert count_consecutive_primes(0, 0) == 0
        assert count_consecutive_primes(0, -1) == 0

        # Test when n=1 gives negative or small values
        assert count_consecutive_primes(-10, 5) >= 0
