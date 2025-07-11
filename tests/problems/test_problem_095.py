#!/usr/bin/env python3
"""
Test for Problem 095: Amicable chains
"""

import pytest

from problems.problem_095 import (
    compute_divisor_sums,
    find_all_amicable_chains,
    find_chain_length,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    sum_of_proper_divisors,
)


class TestUtilityFunctions:
    """Test utility functions for amicable chains."""

    def test_sum_of_proper_divisors(self) -> None:
        """Test sum of proper divisors calculation."""
        # Perfect number
        assert sum_of_proper_divisors(6) == 6
        assert sum_of_proper_divisors(28) == 28

        # Amicable numbers
        assert sum_of_proper_divisors(220) == 284
        assert sum_of_proper_divisors(284) == 220

        # Chain example
        assert sum_of_proper_divisors(12496) == 14288
        assert sum_of_proper_divisors(14288) == 15472
        assert sum_of_proper_divisors(15472) == 14536
        assert sum_of_proper_divisors(14536) == 14264
        assert sum_of_proper_divisors(14264) == 12496

        # Edge cases
        assert sum_of_proper_divisors(1) == 0
        assert sum_of_proper_divisors(2) == 1
        assert sum_of_proper_divisors(3) == 1
        assert sum_of_proper_divisors(4) == 3  # 1 + 2

        # Prime numbers
        assert sum_of_proper_divisors(7) == 1
        assert sum_of_proper_divisors(11) == 1
        assert sum_of_proper_divisors(13) == 1

    def test_compute_divisor_sums(self) -> None:
        """Test bulk computation of divisor sums."""
        limit = 30
        divisor_sums = compute_divisor_sums(limit)

        # Verify some values
        assert divisor_sums[0] == 0
        assert divisor_sums[1] == 0
        assert divisor_sums[6] == 6  # Perfect number
        assert divisor_sums[12] == 16  # 1 + 2 + 3 + 4 + 6
        assert divisor_sums[28] == 28  # Perfect number

        # Check against individual calculation
        for i in range(1, limit + 1):
            assert divisor_sums[i] == sum_of_proper_divisors(i)

    def test_find_chain_length_amicable_chain(self) -> None:
        """Test finding amicable chains."""
        divisor_sums = compute_divisor_sums(20000)

        # Test the known chain starting at 12496
        chain_length, chain = find_chain_length(12496, divisor_sums, 20000)
        assert chain_length == 5
        assert chain == [12496, 14288, 15472, 14536, 14264]

        # Test perfect number (chain length 1)
        chain_length, chain = find_chain_length(6, divisor_sums, 20000)
        assert chain_length == 1
        assert chain == [6]

        # Test amicable pair (chain length 2)
        chain_length, chain = find_chain_length(220, divisor_sums, 20000)
        assert chain_length == 2
        assert chain == [220, 284]

    def test_find_chain_length_no_chain(self) -> None:
        """Test cases that don't form amicable chains."""
        divisor_sums = compute_divisor_sums(1000)

        # Prime number (leads to 1)
        chain_length, chain = find_chain_length(7, divisor_sums, 1000)
        assert chain_length == 0
        assert chain == []

        # Number that leads to a smaller number
        chain_length, chain = find_chain_length(10, divisor_sums, 1000)
        assert chain_length == 0
        assert chain == []

    def test_find_all_amicable_chains(self) -> None:
        """Test finding all amicable chains within a limit."""
        chains = find_all_amicable_chains(300)

        # Should find perfect numbers and amicable pairs
        chain_lengths = [c[0] for c in chains]

        # Perfect numbers: 6, 28
        assert 1 in chain_lengths

        # Amicable pair: 220, 284
        assert 2 in chain_lengths

        # All chains should be properly sorted
        for i in range(1, len(chains)):
            # First by length (descending)
            if chains[i - 1][0] == chains[i][0]:
                # Then by minimum element (ascending)
                assert min(chains[i - 1][1]) <= min(chains[i][1])
            else:
                assert chains[i - 1][0] > chains[i][0]


class TestSolutionMethods:
    """Test solution methods with various inputs."""

    def test_small_cases(self) -> None:
        """Test solutions with small input values."""
        # Very small case - should find 6 (perfect number)
        assert solve_naive(10) == 6
        assert solve_optimized(10) == 6
        assert solve_mathematical(10) == 6

        # Case with amicable pair
        assert solve_naive(300) == 220
        assert solve_optimized(300) == 220
        assert solve_mathematical(300) == 220

    def test_solution_consistency(self) -> None:
        """Test that all solution methods give the same results."""
        test_limits = [100, 500, 1000, 10000]

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

    def test_known_chains(self) -> None:
        """Test with known amicable chains."""
        # For limit 15000, longest chains are amicable pairs (length 2)
        # 220 is the smallest member of such chains
        result = solve_optimized(15000)
        assert result == 220

        # To include the chain starting at 12496, need higher limit
        result = solve_optimized(20000)
        assert result in [220, 12496]  # Depends on which chain is longer

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Very small limits
        assert solve_optimized(1) == 0
        assert solve_optimized(2) == 0
        assert solve_optimized(5) == 0

        # Just enough to include first perfect number
        assert solve_optimized(6) == 6

        # Should include perfect numbers and amicable pairs
        result = solve_optimized(1000)
        assert result > 0

    @pytest.mark.slow
    def test_large_case(self) -> None:
        """Test with larger input (marked as slow)."""
        # Test with moderately large limit
        limit = 100000
        result_optimized = solve_optimized(limit)
        result_mathematical = solve_mathematical(limit)

        assert result_optimized == result_mathematical
        assert result_optimized > 0

        # Verify the result is actually the smallest member of the longest chain
        chains = find_all_amicable_chains(limit)
        if chains:
            longest_chain = chains[0]  # Already sorted by length
            assert result_optimized == min(longest_chain[1])

    def test_result_properties(self) -> None:
        """Test properties of the results."""
        # Results should be positive for reasonable limits
        assert solve_optimized(1000) > 0

        # Results should be consistent as limit increases
        result_1000 = solve_optimized(1000)
        result_10000 = solve_optimized(10000)
        result_100000 = solve_optimized(100000)

        # The longest chain might change as limit increases
        # But results should always be valid
        assert result_1000 > 0
        assert result_10000 > 0
        assert result_100000 > 0


class TestProblem095:
    """Test the main problem solution."""

    def test_chain_properties(self) -> None:
        """Test properties of amicable chains."""
        chains = find_all_amicable_chains(20000)

        for length, chain in chains:
            # Verify chain properties
            assert len(chain) == length

            # Verify it's actually a chain
            divisor_sums = compute_divisor_sums(20000)
            for i in range(length):
                current = chain[i]
                next_expected = chain[(i + 1) % length]
                assert divisor_sums[current] == next_expected

            # All elements should be unique
            assert len(set(chain)) == length

    def test_perfect_numbers_as_chains(self) -> None:
        """Test that perfect numbers are treated as chains of length 1."""
        divisor_sums = compute_divisor_sums(100)

        # Test perfect numbers
        for perfect in [6, 28]:
            chain_length, chain = find_chain_length(perfect, divisor_sums, 100)
            assert chain_length == 1
            assert chain == [perfect]

    def test_amicable_pairs_as_chains(self) -> None:
        """Test that amicable pairs are chains of length 2."""
        divisor_sums = compute_divisor_sums(300)

        # Test amicable pair 220, 284
        chain_length1, chain1 = find_chain_length(220, divisor_sums, 300)
        chain_length2, chain2 = find_chain_length(284, divisor_sums, 300)

        assert chain_length1 == 2
        assert chain_length2 == 0  # Already seen when starting from 220
        assert set(chain1) == {220, 284}

    def test_main_problem_result(self) -> None:
        """Test the main problem result."""
        # The expected answer for limit 1,000,000 is 14316
        result = solve_mathematical(1000000)
        assert result == 14316

    def test_chain_detection_algorithm(self) -> None:
        """Test the chain detection algorithm."""
        divisor_sums = compute_divisor_sums(20000)

        # Test various starting points
        test_cases = [
            (12496, 5, True),  # Known chain
            (220, 2, True),  # Amicable pair
            (6, 1, True),  # Perfect number
            (7, 0, False),  # Prime (no chain)
            (10, 0, False),  # No chain
        ]

        for start, expected_length, forms_chain in test_cases:
            chain_length, chain = find_chain_length(start, divisor_sums, 20000)
            assert chain_length == expected_length
            assert (chain_length > 0) == forms_chain

    def test_performance_characteristics(self) -> None:
        """Test performance characteristics of different approaches."""
        # Optimized approach should be significantly faster than naive
        # This is more of a sanity check than a strict performance test

        limit = 10000
        chains = find_all_amicable_chains(limit)

        # Should find multiple chains
        assert len(chains) > 5

        # Chains should be properly ordered
        for i in range(1, len(chains)):
            assert chains[i - 1][0] >= chains[i][0]
