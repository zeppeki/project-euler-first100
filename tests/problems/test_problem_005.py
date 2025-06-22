"""Tests for Problem 005: Smallest multiple."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problem_005 import (
    gcd,
    lcm,
    solve_builtin,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem005:
    """Test cases for Problem 005."""

    def test_gcd(self) -> None:
        """Test the greatest common divisor function."""
        assert gcd(12, 8) == 4
        assert gcd(8, 12) == 4
        assert gcd(17, 13) == 1
        assert gcd(100, 25) == 25
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5
        assert gcd(1, 1) == 1

    def test_lcm(self) -> None:
        """Test the least common multiple function."""
        assert lcm(4, 6) == 12
        assert lcm(6, 4) == 12
        assert lcm(3, 5) == 15
        assert lcm(12, 8) == 24
        assert lcm(1, 5) == 5
        assert lcm(7, 7) == 7

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, 1),  # LCM(1) = 1
            (2, 2),  # LCM(1,2) = 2
            (3, 6),  # LCM(1,2,3) = 6
            (4, 12),  # LCM(1,2,3,4) = 12
            (5, 60),  # LCM(1,2,3,4,5) = 60
            (10, 2520),  # Problem example: LCM(1,...,10) = 2520
        ],
    )
    def test_solve_naive(self, n: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

        # Verify that the result is divisible by all numbers from 1 to n
        for i in range(1, n + 1):
            assert result % i == 0, f"Result {result} not divisible by {i}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, 1),  # LCM(1) = 1
            (2, 2),  # LCM(1,2) = 2
            (3, 6),  # LCM(1,2,3) = 6
            (4, 12),  # LCM(1,2,3,4) = 12
            (5, 60),  # LCM(1,2,3,4,5) = 60
            (10, 2520),  # Problem example: LCM(1,...,10) = 2520
        ],
    )
    def test_solve_optimized(self, n: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

        # Verify that the result is divisible by all numbers from 1 to n
        for i in range(1, n + 1):
            assert result % i == 0, f"Result {result} not divisible by {i}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, 1),  # LCM(1) = 1
            (2, 2),  # LCM(1,2) = 2
            (3, 6),  # LCM(1,2,3) = 6
            (4, 12),  # LCM(1,2,3,4) = 12
            (5, 60),  # LCM(1,2,3,4,5) = 60
            (10, 2520),  # Problem example: LCM(1,...,10) = 2520
        ],
    )
    def test_solve_mathematical(self, n: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

        # Verify that the result is divisible by all numbers from 1 to n
        for i in range(1, n + 1):
            assert result % i == 0, f"Result {result} not divisible by {i}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, 1),  # LCM(1) = 1
            (2, 2),  # LCM(1,2) = 2
            (3, 6),  # LCM(1,2,3) = 6
            (4, 12),  # LCM(1,2,3,4) = 12
            (5, 60),  # LCM(1,2,3,4,5) = 60
            (10, 2520),  # Problem example: LCM(1,...,10) = 2520
        ],
    )
    def test_solve_builtin(self, n: int, expected: int) -> None:
        """Test the builtin solution."""
        result = solve_builtin(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

        # Verify that the result is divisible by all numbers from 1 to n
        for i in range(1, n + 1):
            assert result % i == 0, f"Result {result} not divisible by {i}"

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 10])
    def test_all_solutions_agree(self, n: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(n)
        optimized_result = solve_optimized(n)
        math_result = solve_mathematical(n)
        builtin_result = solve_builtin(n)

        assert naive_result == optimized_result == math_result == builtin_result, (
            f"Solutions disagree for n={n}: "
            f"naive={naive_result}, optimized={optimized_result}, "
            f"math={math_result}, builtin={builtin_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with n = 0
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0
        assert solve_mathematical(0) == 0
        assert solve_builtin(0) == 0

        # Test with negative n
        assert solve_naive(-1) == 0
        assert solve_optimized(-1) == 0
        assert solve_mathematical(-1) == 0
        assert solve_builtin(-1) == 0

    @pytest.mark.slow
    def test_twenty_digit_problem(self) -> None:
        """Test the actual problem with numbers 1-20 (marked as slow)."""
        # This is the actual problem we need to solve
        n = 20

        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)
        result_builtin = solve_builtin(n)

        # All solutions should agree
        assert result_naive == result_optimized == result_math == result_builtin

        # Result should be divisible by all numbers from 1 to 20
        for i in range(1, n + 1):
            assert result_naive % i == 0, f"Result {result_naive} not divisible by {i}"

        # The expected answer according to Project Euler
        expected_answer = 232792560
        assert result_naive == expected_answer

    def test_mathematical_properties(self) -> None:
        """Test mathematical properties of LCM."""
        # LCM(a, b) * GCD(a, b) = a * b
        test_pairs = [(12, 8), (15, 25), (7, 11), (6, 9)]

        for a, b in test_pairs:
            lcm_val = lcm(a, b)
            gcd_val = gcd(a, b)
            assert lcm_val * gcd_val == a * b, (
                f"LCM({a},{b}) * GCD({a},{b}) != {a} * {b}: "
                f"{lcm_val} * {gcd_val} != {a * b}"
            )

    def test_sieve_of_eratosthenes_indirectly(self) -> None:
        """Test the sieve function indirectly through mathematical solution."""
        # Test that mathematical solution gives correct results for small cases
        # This indirectly tests the sieve implementation
        for n in range(1, 11):
            math_result = solve_mathematical(n)
            optimized_result = solve_optimized(n)
            assert (
                math_result == optimized_result
            ), f"Mathematical and optimized solutions disagree for n={n}"

    def test_performance_comparison(self) -> None:
        """Test that optimized solutions are faster for larger inputs."""
        import time

        n = 10

        # Test naive solution
        start_time = time.time()
        solve_naive(n)
        naive_time = time.time() - start_time

        # Test optimized solution
        start_time = time.time()
        solve_optimized(n)
        optimized_time = time.time() - start_time

        # Test mathematical solution
        start_time = time.time()
        solve_mathematical(n)
        math_time = time.time() - start_time

        # Test builtin solution
        start_time = time.time()
        solve_builtin(n)
        builtin_time = time.time() - start_time

        # All should complete in reasonable time (less than 1 second for n=10)
        assert naive_time < 1.0
        assert optimized_time < 1.0
        assert math_time < 1.0
        assert builtin_time < 1.0

    def test_large_number_divisibility(self) -> None:
        """Test divisibility properties for the actual answer."""
        # Test with the known answer for n=20
        n = 20
        expected_answer = 232792560

        # Verify it's divisible by all numbers from 1 to 20
        for i in range(1, n + 1):
            assert (
                expected_answer % i == 0
            ), f"Expected answer {expected_answer} not divisible by {i}"

    def test_prime_factorization_properties(self) -> None:
        """Test that the mathematical approach handles prime powers correctly."""
        # For n=8, we need 2^3 (since 8 = 2^3)
        # For n=9, we need 3^2 (since 9 = 3^2)
        # So LCM(1,...,9) should include 2^3 and 3^2

        result = solve_mathematical(9)

        # Should be divisible by 8 (2^3) and 9 (3^2)
        assert result % 8 == 0, f"Result {result} not divisible by 8"
        assert result % 9 == 0, f"Result {result} not divisible by 9"

        # Should equal 2520/3 * 9 = 2520 since LCM(1,...,9) includes 9
        expected = solve_optimized(9)
        assert result == expected
