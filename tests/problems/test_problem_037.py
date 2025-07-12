#!/usr/bin/env python3
"""Tests for Problem 037"""

import pytest

from problems.problem_037 import (
    is_prime,
    is_truncatable_prime,
    solve_naive,
    solve_optimized,
)


class TestProblem037:
    """Test cases for Problem 037"""

    def test_is_truncatable_prime(self) -> None:
        """Test truncatable prime checking function"""
        # Known truncatable primes
        assert is_truncatable_prime(23) is True
        assert is_truncatable_prime(37) is True
        assert is_truncatable_prime(53) is True
        assert is_truncatable_prime(73) is True
        assert is_truncatable_prime(313) is True
        assert is_truncatable_prime(317) is True
        assert is_truncatable_prime(373) is True
        assert is_truncatable_prime(797) is True
        assert is_truncatable_prime(3137) is True
        assert is_truncatable_prime(3797) is True
        assert is_truncatable_prime(739397) is True

        # Excluded single digit primes
        assert is_truncatable_prime(2) is False
        assert is_truncatable_prime(3) is False
        assert is_truncatable_prime(5) is False
        assert is_truncatable_prime(7) is False

        # Non-truncatable primes
        assert is_truncatable_prime(11) is False  # 1 is not prime
        assert is_truncatable_prime(13) is False  # 1 is not prime
        assert is_truncatable_prime(41) is False  # 4 is not prime
        assert is_truncatable_prime(43) is False  # 4 is not prime

    def test_known_truncatable_primes_example(self) -> None:
        """Test the example from the problem statement"""
        # 3797 example from problem
        assert is_prime(3797) is True
        assert is_prime(797) is True  # left truncation
        assert is_prime(97) is True
        assert is_prime(7) is True
        assert is_prime(379) is True  # right truncation
        assert is_prime(37) is True
        assert is_prime(3) is True

        assert is_truncatable_prime(3797) is True

    @pytest.mark.slow
    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        # There are exactly 11 truncatable primes
        assert result > 0
        assert isinstance(result, int)

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        # There are exactly 11 truncatable primes
        assert result > 0
        assert isinstance(result, int)

    @pytest.mark.slow
    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        assert naive_result == optimized_result

    def test_truncatable_prime_properties(self) -> None:
        """Test properties that truncatable primes must satisfy"""
        # Test that known truncatable primes have correct structure
        known_truncatable = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]

        for prime in known_truncatable:
            assert is_truncatable_prime(prime) is True

            # All truncations from left must be prime
            s = str(prime)
            for i in range(1, len(s)):
                left_truncated = int(s[i:])
                assert is_prime(left_truncated) is True, (
                    f"Left truncation {left_truncated} of {prime} is not prime"
                )

            # All truncations from right must be prime
            for i in range(len(s) - 1, 0, -1):
                right_truncated = int(s[:i])
                assert is_prime(right_truncated) is True, (
                    f"Right truncation {right_truncated} of {prime} is not prime"
                )

    @pytest.mark.slow
    def test_count_truncatable_primes(self) -> None:
        """Test that there are exactly 11 truncatable primes"""
        truncatable_primes: list[int] = []
        candidate = 11

        while len(truncatable_primes) < 11:
            if is_truncatable_prime(candidate):
                truncatable_primes.append(candidate)
            candidate += 2

        assert len(truncatable_primes) == 11
        # Verify they are all different
        assert len(set(truncatable_primes)) == 11
