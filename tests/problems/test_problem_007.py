"""Tests for Problem 007: 10001st prime."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.lib import (
    is_prime,
    is_prime_optimized,
    sieve_of_eratosthenes,
)
from problems.problem_007 import (
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem007:
    """Test cases for Problem 007."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, 2),  # 1st prime is 2
            (2, 3),  # 2nd prime is 3
            (3, 5),  # 3rd prime is 5
            (4, 7),  # 4th prime is 7
            (5, 11),  # 5th prime is 11
            (6, 13),  # 6th prime is 13 (problem example)
            (10, 29),  # 10th prime is 29
            (25, 97),  # 25th prime is 97
            (100, 541),  # 100th prime is 541
        ],
    )
    def test_solve_naive(self, n: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, 2),  # 1st prime is 2
            (2, 3),  # 2nd prime is 3
            (3, 5),  # 3rd prime is 5
            (4, 7),  # 4th prime is 7
            (5, 11),  # 5th prime is 11
            (6, 13),  # 6th prime is 13 (problem example)
            (10, 29),  # 10th prime is 29
            (25, 97),  # 25th prime is 97
            (100, 541),  # 100th prime is 541
        ],
    )
    def test_solve_optimized(self, n: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, 2),  # 1st prime is 2
            (2, 3),  # 2nd prime is 3
            (3, 5),  # 3rd prime is 5
            (4, 7),  # 4th prime is 7
            (5, 11),  # 5th prime is 11
            (6, 13),  # 6th prime is 13 (problem example)
            (10, 29),  # 10th prime is 29
            (25, 97),  # 25th prime is 97
            (100, 541),  # 100th prime is 541
        ],
    )
    def test_solve_mathematical(self, n: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6, 10, 25, 100])
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
        # Test with n = 1 (first prime)
        assert solve_naive(1) == 2
        assert solve_optimized(1) == 2
        assert solve_mathematical(1) == 2

        # Test with n = 2 (second prime)
        assert solve_naive(2) == 3
        assert solve_optimized(2) == 3
        assert solve_mathematical(2) == 3

    def test_invalid_input(self) -> None:
        """Test with invalid input."""
        # All solutions should raise ValueError for non-positive n
        with pytest.raises(ValueError):
            solve_naive(0)
        with pytest.raises(ValueError):
            solve_optimized(0)
        with pytest.raises(ValueError):
            solve_mathematical(0)

        with pytest.raises(ValueError):
            solve_naive(-1)
        with pytest.raises(ValueError):
            solve_optimized(-1)
        with pytest.raises(ValueError):
            solve_mathematical(-1)

    @pytest.mark.slow
    def test_large_number(self) -> None:
        """Test with the actual problem number (marked as slow)."""
        # Test with the actual problem limit using fastest algorithm only
        n = 10001
        expected = 104743  # Known Project Euler answer

        # Test only mathematical solution for speed
        result_math = solve_mathematical(n)
        assert result_math == expected

    def test_prime_checking_functions(self) -> None:
        """Test the prime checking helper functions."""
        # Test known primes
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in primes:
            assert is_prime(prime), f"{prime} should be prime (naive)"
            assert is_prime_optimized(prime), f"{prime} should be prime (optimized)"

        # Test known composites
        composites = [
            4,
            6,
            8,
            9,
            10,
            12,
            14,
            15,
            16,
            18,
            20,
            21,
            22,
            24,
            25,
            26,
            27,
            28,
            30,
        ]
        for composite in composites:
            assert not is_prime(composite), f"{composite} should not be prime (naive)"
            assert not is_prime_optimized(composite), (
                f"{composite} should not be prime (optimized)"
            )

        # Test edge cases
        assert not is_prime(0)
        assert not is_prime(1)
        assert not is_prime_optimized(0)
        assert not is_prime_optimized(1)

    def test_sieve_of_eratosthenes(self) -> None:
        """Test the Sieve of Eratosthenes function."""
        # Test small range
        primes_10 = sieve_of_eratosthenes(10, "list")
        expected_10 = [2, 3, 5, 7]
        assert primes_10 == expected_10

        # Test medium range
        primes_30 = sieve_of_eratosthenes(30, "list")
        expected_30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        assert primes_30 == expected_30

        # Test edge cases
        assert sieve_of_eratosthenes(1, "list") == []
        assert sieve_of_eratosthenes(2, "list") == [2]
        assert sieve_of_eratosthenes(3, "list") == [2, 3]

    def test_manual_calculation_verification(self) -> None:
        """Test manual calculation verification for the first few primes."""
        # The first 10 primes are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
        expected_first_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        for i, expected_prime in enumerate(expected_first_10, 1):
            assert solve_naive(i) == expected_prime
            assert solve_optimized(i) == expected_prime
            assert solve_mathematical(i) == expected_prime

    def test_performance_comparison(self) -> None:
        """Test that all solutions work for moderate inputs."""
        # Simple functional test without timing overhead
        n = 50  # 50th prime is 229

        # Verify all solutions work
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)

        # All should give same result
        assert result_naive == result_optimized == result_math
        assert result_naive == 229  # 50th prime is 229

    def test_large_values_consistency(self) -> None:
        """Test consistency for larger values."""
        # Test larger values to ensure algorithms remain accurate
        test_values = [20, 50, 100, 200]
        expected_primes = [71, 229, 541, 1223]  # Known nth primes

        for n, expected in zip(test_values, expected_primes, strict=False):
            naive_result = solve_naive(n)
            optimized_result = solve_optimized(n)
            math_result = solve_mathematical(n)

            assert naive_result == optimized_result == math_result == expected, (
                f"Solutions disagree for n={n}: "
                f"naive={naive_result}, optimized={optimized_result}, math={math_result}, expected={expected}"
            )

    def test_prime_distribution_properties(self) -> None:
        """Test some basic properties of prime distribution."""
        # Test that primes are increasing
        for i in range(1, 20):
            prime_i = solve_optimized(i)
            prime_i_plus_1 = solve_optimized(i + 1)
            assert prime_i < prime_i_plus_1, (
                f"Prime {i} should be less than prime {i + 1}"
            )

        # Test that all found numbers are actually prime
        for i in range(1, 50):
            nth_prime = solve_optimized(i)
            assert is_prime_optimized(nth_prime), (
                f"The {i}th prime {nth_prime} should actually be prime"
            )

    def test_project_euler_example(self) -> None:
        """Test the specific Project Euler example."""
        # From the problem statement:
        # First 6 primes: 2, 3, 5, 7, 11, 13
        # 6th prime is 13

        n = 6
        expected = 13

        # Test all our solutions
        assert solve_naive(n) == expected
        assert solve_optimized(n) == expected
        assert solve_mathematical(n) == expected

        # Verify the first 6 primes manually
        first_6_primes = [solve_optimized(i) for i in range(1, 7)]
        expected_first_6 = [2, 3, 5, 7, 11, 13]
        assert first_6_primes == expected_first_6

    def test_mathematical_optimization_correctness(self) -> None:
        """Test that the 6k±1 optimization is correct."""
        # The mathematical solution uses the fact that all primes > 3
        # are of the form 6k±1. Test this property.

        # Generate primes using sieve for verification
        primes = sieve_of_eratosthenes(100, "list")

        # Check that all primes > 3 are of the form 6k±1
        for prime in primes:
            if prime <= 3:
                continue
            remainder = prime % 6
            assert remainder == 1 or remainder == 5, (
                f"Prime {prime} is not of the form 6k±1 (remainder={remainder})"
            )

    def test_sieve_upper_bound_estimation(self) -> None:
        """Test that the upper bound estimation for sieve works correctly."""
        # The optimized solution estimates upper bound using prime number theorem
        # Test that it finds enough primes for small n values

        for n in [10, 20, 50, 100]:
            result = solve_optimized(n)
            # Just verify it returns a valid prime
            assert is_prime_optimized(result), (
                f"Result {result} for n={n} should be prime"
            )

            # Verify it's actually the nth prime by checking with naive solution
            expected = solve_naive(n)
            assert result == expected, (
                f"Optimized solution disagrees with naive for n={n}"
            )

    def test_algorithm_specific_edge_cases(self) -> None:
        """Test algorithm-specific edge cases."""
        # Test the 6k±1 pattern starting from 5
        assert solve_mathematical(3) == 5  # First prime in the 6k±1 pattern
        assert solve_mathematical(4) == 7  # Next prime in the pattern

        # Test that the increment alternation works correctly
        # 5 (6*1-1), 7 (6*1+1), 11 (6*2-1), 13 (6*2+1), 17 (6*3-1), 19 (6*3+1), 23 (6*4-1)
        primes_in_pattern = [5, 7, 11, 13, 17, 19, 23]
        for i, expected_prime in enumerate(primes_in_pattern):
            actual_prime = solve_mathematical(
                i + 3
            )  # +3 because we start from the 3rd prime (5)
            assert actual_prime == expected_prime, (
                f"Expected {expected_prime}, got {actual_prime}"
            )
