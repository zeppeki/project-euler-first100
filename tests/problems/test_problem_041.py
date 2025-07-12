#!/usr/bin/env python3
"""
Tests for Problem 041: Pandigital prime
"""

from collections.abc import Callable

import pytest

from problems.problem_041 import (
    is_pandigital,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem041:
    """Test cases for Problem 041"""

    def test_is_pandigital(self) -> None:
        """Test pandigital number detection"""
        # Valid pandigital numbers
        assert is_pandigital(1, 1)
        assert is_pandigital(12, 2)
        assert is_pandigital(21, 2)
        assert is_pandigital(123, 3)
        assert is_pandigital(321, 3)
        assert is_pandigital(1234, 4)
        assert is_pandigital(2143, 4)  # Example from problem
        assert is_pandigital(4321, 4)

        # Invalid pandigital numbers
        assert not is_pandigital(11, 2)  # Repeated digit
        assert not is_pandigital(102, 3)  # Contains 0
        assert not is_pandigital(1235, 4)  # Contains 5 instead of expected digits
        assert not is_pandigital(12, 3)  # Wrong length
        assert not is_pandigital(1234, 3)  # Wrong length

    def test_known_pandigital_primes(self) -> None:
        """Test with known pandigital primes"""
        from problems.lib.primes import is_prime

        # Example from problem statement
        assert is_pandigital(2143, 4)
        assert is_prime(2143)

        # Other known pandigital primes
        known_pandigital_primes = [2143, 4231]

        for prime in known_pandigital_primes:
            assert is_prime(prime), f"{prime} should be prime"
            # Check if it's pandigital for its digit count
            digit_count = len(str(prime))
            assert is_pandigital(prime, digit_count), (
                f"{prime} should be {digit_count}-digit pandigital"
            )

    def test_mathematical_insight(self) -> None:
        """Test the mathematical insight about 8 and 9 digit pandigital numbers"""
        # Sum of digits 1 through 8: 1+2+...+8 = 36 (divisible by 3)
        sum_8_digits = sum(range(1, 9))
        assert sum_8_digits == 36
        assert sum_8_digits % 3 == 0

        # Sum of digits 1 through 9: 1+2+...+9 = 45 (divisible by 3)
        sum_9_digits = sum(range(1, 10))
        assert sum_9_digits == 45
        assert sum_9_digits % 3 == 0

        # This means all 8-digit and 9-digit pandigital numbers are divisible by 3
        # and therefore cannot be prime (except 3 itself, but we're looking for larger)

    def test_solution_consistency(self) -> None:
        """Test that all solution methods return the same result"""
        result_naive = solve_naive()
        result_optimized = solve_optimized()
        result_mathematical = solve_mathematical()

        assert result_naive == result_optimized, (
            "Naive and optimized solutions should match"
        )
        assert result_optimized == result_mathematical, (
            "Optimized and mathematical solutions should match"
        )
        assert result_naive == result_mathematical, (
            "Naive and mathematical solutions should match"
        )

    def test_solution_properties(self) -> None:
        """Test properties of the solution"""
        from problems.lib.primes import is_prime

        result = solve_mathematical()  # Use most efficient method

        # Result should be positive
        assert result > 0, "Solution should be positive"

        # Result should be prime
        assert is_prime(result), "Solution should be prime"

        # Result should be pandigital for its digit count
        digit_count = len(str(result))
        assert is_pandigital(result, digit_count), (
            f"Solution should be {digit_count}-digit pandigital"
        )

        # Result should be at most 7 digits (due to mathematical insight)
        assert digit_count <= 7, "Solution should be at most 7 digits"

    @pytest.mark.parametrize(
        "solve_func", [solve_naive, solve_optimized, solve_mathematical]
    )
    def test_all_solutions(self, solve_func: Callable[[], int]) -> None:
        """Test each solution function individually"""
        from problems.lib.primes import is_prime

        result = solve_func()

        # Basic properties
        assert isinstance(result, int), "Result should be an integer"
        assert result > 0, "Result should be positive"

        # Mathematical properties
        assert is_prime(result), "Result should be prime"
        digit_count = len(str(result))
        assert is_pandigital(result, digit_count), (
            f"Result should be {digit_count}-digit pandigital"
        )

    def test_performance_benchmark(self) -> None:
        """Test that solutions complete within reasonable time"""
        import time

        # Each solution should complete within 10 seconds
        timeout = 10.0

        start_time = time.time()
        result_mathematical = solve_mathematical()
        mathematical_time = time.time() - start_time

        assert mathematical_time < timeout, (
            f"Mathematical solution took too long: {mathematical_time:.2f}s"
        )
        assert result_mathematical > 0, (
            "Mathematical solution should return valid result"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases"""
        from problems.lib.primes import is_prime

        # Test 1-digit pandigital prime
        assert is_pandigital(1, 1)
        assert not is_prime(1)  # 1 is not considered prime

        # Test 2-digit pandigital numbers
        assert is_pandigital(12, 2)
        assert not is_prime(12)
        assert is_pandigital(21, 2)
        assert not is_prime(21)

        # Test small primes that are also pandigital
        # Note: 2 is not 1-digit pandigital (doesn't contain digit 1)
        assert is_prime(2)
        assert not is_pandigital(2, 1)  # 2 doesn't contain digit 1

        # Note: 23 is not pandigital (doesn't contain digit 1)
        assert is_prime(23)
        assert not is_pandigital(23, 2)  # 23 doesn't contain digit 1

        # Only 12 and 21 are 2-digit pandigital, but neither is prime
        assert is_pandigital(12, 2) and not is_prime(12)
        assert is_pandigital(21, 2) and not is_prime(21)
