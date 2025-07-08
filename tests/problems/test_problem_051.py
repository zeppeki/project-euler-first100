#!/usr/bin/env python3
"""
Tests for Project Euler Problem 051: Prime digit replacements
"""

from collections.abc import Callable

import pytest

from problems.problem_051 import (
    count_prime_family,
    generate_replacements,
    get_prime_family_details,
    is_prime,
    sieve_of_eratosthenes,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestUtilityFunctions:
    """Test utility functions"""

    def test_is_prime(self) -> None:
        """Test prime checking function"""
        # Known primes
        assert is_prime(2)
        assert is_prime(3)
        assert is_prime(5)
        assert is_prime(7)
        assert is_prime(11)
        assert is_prime(13)
        assert is_prime(23)
        assert is_prime(43)
        assert is_prime(53)
        assert is_prime(73)
        assert is_prime(83)

        # Known non-primes
        assert not is_prime(0)
        assert not is_prime(1)
        assert not is_prime(4)
        assert not is_prime(6)
        assert not is_prime(8)
        assert not is_prime(9)
        assert not is_prime(10)
        assert not is_prime(12)

    def test_sieve_of_eratosthenes(self) -> None:
        """Test sieve of Eratosthenes implementation"""
        primes_up_to_20 = sieve_of_eratosthenes(20)

        # Check known primes up to 20
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for p in expected_primes:
            assert primes_up_to_20[p], f"{p} should be prime"

        # Check known non-primes
        expected_non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for n in expected_non_primes:
            assert not primes_up_to_20[n], f"{n} should not be prime"

    def test_generate_replacements(self) -> None:
        """Test digit replacement function"""
        # Test single position replacement
        assert generate_replacements(13, (0,), 2) == 23
        assert generate_replacements(13, (0,), 4) == 43
        assert generate_replacements(13, (0,), 5) == 53

        # Test multiple position replacement
        assert generate_replacements(56003, (2, 3), 1) == 56113
        assert generate_replacements(56003, (2, 3), 3) == 56333
        assert generate_replacements(56003, (2, 3), 4) == 56443

    def test_count_prime_family(self) -> None:
        """Test prime family counting"""
        # Create a prime set for testing
        primes_up_to_100 = sieve_of_eratosthenes(100)
        prime_set = {i for i in range(2, 101) if primes_up_to_100[i]}

        # Test *3 pattern (13 -> 13, 23, 43, 53, 73, 83)
        count = count_prime_family(13, (0,), prime_set)
        assert count == 6

        # Test **03 pattern should work with 56003
        primes_up_to_60000 = sieve_of_eratosthenes(60000)
        large_prime_set = {i for i in range(2, 60001) if primes_up_to_60000[i]}
        count_large = count_prime_family(56003, (2, 3), large_prime_set)
        assert count_large == 7


class TestSolutionFunctions:
    """Test main solution functions"""

    @pytest.mark.parametrize(
        "solver", [solve_naive, solve_optimized, solve_mathematical]
    )
    def test_solve_small_cases(self, solver: Callable[[int], int]) -> None:
        """Test solution functions with small test cases"""
        # Test case: 6 primes in family (*3 pattern)
        result = solver(6)
        assert result == 13

        # Test case: 7 primes in family (56**3 pattern)
        result = solver(7)
        assert result == 56003

    @pytest.mark.slow
    def test_solve_consistency(self) -> None:
        """Test that all solution methods give the same result"""
        target_sizes = [6, 7]

        for target_size in target_sizes:
            results = [
                solve_naive(target_size),
                solve_optimized(target_size),
                solve_mathematical(target_size),
            ]

            # All methods should return the same result
            assert len(set(results)) == 1, (
                f"Inconsistent results for target {target_size}: {results}"
            )

    @pytest.mark.slow
    def test_solve_main_problem(self) -> None:
        """Test the main problem (8 primes in family)"""
        # Use fast algorithms only for regular tests
        result_optimized = solve_optimized(8)
        result_mathematical = solve_mathematical(8)

        # Both optimized methods should agree
        assert result_optimized == result_mathematical
        assert result_optimized > 0  # Should find a valid answer


class TestPrimeFamilyDetails:
    """Test prime family analysis functions"""

    def test_get_prime_family_details(self) -> None:
        """Test detailed prime family analysis"""
        # Test *3 pattern (6 primes)
        result = get_prime_family_details(13, 6)
        assert result is not None
        family, positions = result
        assert len(family) == 6
        assert 13 in family
        assert 23 in family
        assert 43 in family
        assert 53 in family
        assert 73 in family
        assert 83 in family

        # Test 56**3 pattern (7 primes)
        result = get_prime_family_details(56003, 7)
        assert result is not None
        family, positions = result
        assert len(family) == 7
        assert 56003 in family

    def test_get_prime_family_details_invalid(self) -> None:
        """Test prime family analysis with invalid inputs"""
        # Test with a prime that doesn't form a large enough family
        result = get_prime_family_details(7, 8)  # 7 can't form 8-prime family
        assert result is None or len(result[0]) < 8


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_empty_or_invalid_inputs(self) -> None:
        """Test handling of invalid inputs"""
        # Test invalid prime checking
        assert not is_prime(-1)
        assert not is_prime(0)
        assert not is_prime(1)

    def test_single_digit_replacements(self) -> None:
        """Test single digit numbers"""
        primes_up_to_10 = sieve_of_eratosthenes(10)
        prime_set = {i for i in range(2, 11) if primes_up_to_10[i]}

        # Single digit numbers can't have meaningful replacements for families
        # This tests the edge case handling
        count = count_prime_family(7, (0,), prime_set)
        assert count >= 0  # Should handle gracefully

    def test_large_number_handling(self) -> None:
        """Test with larger numbers to ensure scalability"""
        # Test that the functions can handle reasonably large numbers
        assert is_prime(97)
        assert is_prime(101)

        primes_up_to_1000 = sieve_of_eratosthenes(1000)
        assert (
            len([i for i in range(2, 1001) if primes_up_to_1000[i]]) == 168
        )  # Known count of primes up to 1000


if __name__ == "__main__":
    pytest.main([__file__])
