"""Tests for Problem 010: Summation of primes."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.lib import is_prime, sieve_of_eratosthenes
from problems.problem_010 import (
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem010:
    """Test cases for Problem 010."""

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (2, 0),  # No primes below 2
            (3, 2),  # Only 2 is below 3
            (10, 17),  # Problem example: 2 + 3 + 5 + 7 = 17
            (11, 17),  # Same as above, 11 is not included
            (30, 129),  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 = 129
            (100, 1060),  # Sum of primes below 100
        ],
    )
    def test_solve_naive(self, limit: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit={limit}"
        )

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (2, 0),  # No primes below 2
            (3, 2),  # Only 2 is below 3
            (10, 17),  # Problem example: 2 + 3 + 5 + 7 = 17
            (11, 17),  # Same as above, 11 is not included
            (30, 129),  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 = 129
            (100, 1060),  # Sum of primes below 100
        ],
    )
    def test_solve_optimized(self, limit: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit={limit}"
        )

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (2, 0),  # No primes below 2
            (3, 2),  # Only 2 is below 3
            (10, 17),  # Problem example: 2 + 3 + 5 + 7 = 17
            (11, 17),  # Same as above, 11 is not included
            (30, 129),  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 = 129
            (100, 1060),  # Sum of primes below 100
        ],
    )
    def test_solve_mathematical(self, limit: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit={limit}"
        )

    @pytest.mark.parametrize("limit", [2, 3, 10, 11, 30, 100, 200])
    def test_all_solutions_agree(self, limit: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(limit)
        optimized_result = solve_optimized(limit)
        math_result = solve_mathematical(limit)

        assert naive_result == optimized_result == math_result, (
            f"Solutions disagree for limit={limit}: "
            f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with limit = 2 (no primes below 2)
        assert solve_naive(2) == 0
        assert solve_optimized(2) == 0
        assert solve_mathematical(2) == 0

        # Test with limit = 3 (only 2 is below 3)
        assert solve_naive(3) == 2
        assert solve_optimized(3) == 2
        assert solve_mathematical(3) == 2

        # Test with limit = 1 (no primes below 1)
        assert solve_naive(1) == 0
        assert solve_optimized(1) == 0
        assert solve_mathematical(1) == 0

    @pytest.mark.slow
    def test_large_number(self) -> None:
        """Test with the actual problem number (marked as slow)."""
        # Test with the actual problem limit using fastest algorithm only
        limit = 2000000
        expected = 142913828922  # Known Project Euler answer

        # Test only mathematical solution for speed
        result_math = solve_mathematical(limit)
        assert result_math == expected

    def test_prime_checking_function(self) -> None:
        """Test the prime checking helper function."""
        # Test known primes
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in primes:
            assert is_prime(prime), f"{prime} should be prime"

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
            assert not is_prime(composite), f"{composite} should not be prime"

        # Test edge cases
        assert not is_prime(0)
        assert not is_prime(1)

    def test_sieve_of_eratosthenes(self) -> None:
        """Test the Sieve of Eratosthenes function."""
        # Test small range
        primes_10 = sieve_of_eratosthenes(9, "list")  # primes up to 9
        expected_10 = [2, 3, 5, 7]
        assert primes_10 == expected_10

        # Test medium range
        primes_30 = sieve_of_eratosthenes(29, "list")  # primes up to 29
        expected_30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        assert primes_30 == expected_30

        # Test edge cases
        assert sieve_of_eratosthenes(1, "list") == []
        assert sieve_of_eratosthenes(2, "list") == [2]
        assert sieve_of_eratosthenes(3, "list") == [2, 3]

    def test_manual_calculation_verification(self) -> None:
        """Test manual calculation verification for small ranges."""
        # Verify the example from the problem: sum of primes below 10
        # Primes below 10: 2, 3, 5, 7
        # Sum: 2 + 3 + 5 + 7 = 17

        limit = 10
        expected_sum = 17
        expected_primes = [2, 3, 5, 7]

        # Get primes below 10
        primes = sieve_of_eratosthenes(limit - 1, "list")
        assert primes == expected_primes
        assert sum(primes) == expected_sum

        # Test all solutions
        assert solve_naive(limit) == expected_sum
        assert solve_optimized(limit) == expected_sum
        assert solve_mathematical(limit) == expected_sum

    def test_sum_calculation_correctness(self) -> None:
        """Test that sum calculations are correct."""
        # Test small ranges manually
        test_cases = [
            (5, [2, 3], 5),  # Primes below 5: 2, 3
            (8, [2, 3, 5, 7], 17),  # Primes below 8: 2, 3, 5, 7
            (12, [2, 3, 5, 7, 11], 28),  # Primes below 12: 2, 3, 5, 7, 11
        ]

        for limit, expected_primes, expected_sum in test_cases:
            primes = sieve_of_eratosthenes(limit - 1, "list")
            assert primes == expected_primes
            assert sum(primes) == expected_sum

            # Test all solutions
            assert solve_naive(limit) == expected_sum
            assert solve_optimized(limit) == expected_sum
            assert solve_mathematical(limit) == expected_sum

    def test_large_values_consistency(self) -> None:
        """Test consistency for larger values (optimized for speed)."""
        # Test larger values to ensure algorithms remain accurate
        test_limits = [50, 100, 500, 1000]

        for limit in test_limits:
            # Use fastest methods for large values
            if limit <= 100:
                # For smaller values, test all solutions
                naive_result = solve_naive(limit)
                optimized_result = solve_optimized(limit)
                math_result = solve_mathematical(limit)
                assert naive_result == optimized_result == math_result
            else:
                # For larger values, use optimized solutions only
                optimized_result = solve_optimized(limit)
                math_result = solve_mathematical(limit)
                assert optimized_result == math_result

    def test_prime_sum_properties(self) -> None:
        """Test some basic properties of prime sums."""
        # Test that sums are increasing
        for limit in range(10, 100, 10):
            sum_current = solve_optimized(limit)
            sum_next = solve_optimized(limit + 10)
            assert sum_current <= sum_next, (
                f"Sum for limit {limit} should be <= sum for limit {limit + 10}"
            )

        # Test that sum includes all primes below limit
        limit = 30
        primes = sieve_of_eratosthenes(limit - 1)
        expected_sum = sum(primes)

        # Verify each prime is actually below the limit
        for prime in primes:
            assert prime < limit, f"Prime {prime} should be below limit {limit}"

        # Verify our solutions match the expected sum
        assert solve_optimized(limit) == expected_sum

    def test_project_euler_example(self) -> None:
        """Test the specific Project Euler example."""
        # From the problem statement:
        # "The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17"

        limit = 10
        expected = 17

        # Test all our solutions
        assert solve_naive(limit) == expected
        assert solve_optimized(limit) == expected
        assert solve_mathematical(limit) == expected

        # Verify the primes manually
        primes_below_10 = sieve_of_eratosthenes(9)
        expected_primes = [2, 3, 5, 7]
        assert primes_below_10 == expected_primes
        assert sum(primes_below_10) == expected

    def test_mathematical_optimization_correctness(self) -> None:
        """Test that the memory-optimized sieve is correct."""
        # Compare the mathematical solution (odd-only sieve) with standard sieve
        for limit in [50, 100, 200]:
            standard_result = solve_optimized(limit)
            optimized_result = solve_mathematical(limit)
            assert standard_result == optimized_result, (
                f"Optimized sieve disagrees with standard sieve for limit={limit}"
            )

    def test_boundary_conditions(self) -> None:
        """Test boundary conditions carefully."""
        # Test that primes exactly at the limit are not included
        # Prime 11 should not be included when limit is 11
        limit = 11
        primes = sieve_of_eratosthenes(limit - 1)  # up to 10
        expected_primes = [2, 3, 5, 7]  # 11 should not be included
        assert primes == expected_primes

        # Test the next boundary
        limit = 12
        primes = sieve_of_eratosthenes(limit - 1)  # up to 11
        expected_primes = [2, 3, 5, 7, 11]  # now 11 should be included
        assert primes == expected_primes

    def test_sieve_implementation_details(self) -> None:
        """Test specific implementation details of the sieve."""
        # Test that sieve correctly marks composites
        limit = 50
        primes = sieve_of_eratosthenes(limit, "list")

        # Verify all returned numbers are actually prime
        for prime in primes:
            assert is_prime(prime), f"{prime} should be prime"

        # Verify no primes are missing (check against naive prime checking)
        expected_primes = [i for i in range(2, limit + 1) if is_prime(i)]
        assert primes == expected_primes

    def test_memory_optimization_verification(self) -> None:
        """Test that the memory-optimized version works correctly."""
        # The mathematical solution uses an odd-only sieve
        # Verify it produces the same results as the full sieve

        for limit in [30, 100, 500]:
            # Get result from standard optimized solution
            standard_sum = solve_optimized(limit)

            # Get result from memory-optimized solution
            optimized_sum = solve_mathematical(limit)

            assert standard_sum == optimized_sum, (
                f"Memory optimization produces different result for limit={limit}: "
                f"standard={standard_sum}, optimized={optimized_sum}"
            )

    def test_incremental_sums(self) -> None:
        """Test that sums increase correctly as limit increases."""
        previous_sum = 0
        primes_found = []

        # Test that adding each prime increases the sum correctly
        for limit in range(3, 31):  # Test limits 3 to 30
            current_sum = solve_optimized(limit)

            # Sum should never decrease
            assert current_sum >= previous_sum, (
                f"Sum decreased from {previous_sum} to {current_sum} at limit {limit}"
            )

            # If sum increased, we found a new prime
            if current_sum > previous_sum:
                new_prime = current_sum - previous_sum
                primes_found.append(new_prime)
                # Verify the new prime is actually prime and below limit
                assert is_prime(new_prime), (
                    f"New prime {new_prime} is not actually prime"
                )
                assert new_prime < limit, (
                    f"New prime {new_prime} is not below limit {limit}"
                )

            previous_sum = current_sum

        # Verify we found the expected primes
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        assert primes_found == expected_primes
