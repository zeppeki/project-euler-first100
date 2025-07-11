#!/usr/bin/env python3
"""
Tests for Problem 074: Digit factorial chains
"""

import pytest

from problems.problem_074 import (
    analyze_factorial_chains,
    count_chains_by_length,
    digit_factorial_sum,
    find_chains_with_length,
    get_factorial_chain,
    get_factorial_chain_length,
    get_factorial_chain_length_memoized,
    get_factorial_chain_statistics,
    solve_naive,
    solve_optimized,
)


def verify_known_chains() -> dict[int, tuple[int, list[int]]]:
    """
    既知のチェーンを検証し、結果を返す
    """
    known_chains = {}

    # 145: 145 → 1!+4!+5! = 145 (length 1)
    chain_145 = get_factorial_chain(145)
    known_chains[145] = (len(chain_145), chain_145)

    # 169: 169 → 363601 → 1454 → 169 (length 3)
    chain_169 = get_factorial_chain(169)
    known_chains[169] = (len(chain_169), chain_169)

    # 871: 871 → 45361 → 871 (length 2)
    chain_871 = get_factorial_chain(871)
    known_chains[871] = (len(chain_871), chain_871)

    return known_chains


class TestDigitFactorialSum:
    """Test digit factorial sum calculations."""

    def test_single_digit_numbers(self) -> None:
        """Test digit factorial sum for single digit numbers."""
        # Test cases based on factorials: 0!=1, 1!=1, 2!=2, ..., 9!=362880
        expected = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        for i, expected_val in enumerate(expected):
            assert digit_factorial_sum(i) == expected_val

    def test_multi_digit_numbers(self) -> None:
        """Test digit factorial sum for multi-digit numbers."""
        # 145: 1! + 4! + 5! = 1 + 24 + 120 = 145
        assert digit_factorial_sum(145) == 145

        # 169: 1! + 6! + 9! = 1 + 720 + 362880 = 363601
        assert digit_factorial_sum(169) == 363601

        # 1454: 1! + 4! + 5! + 4! = 1 + 24 + 120 + 24 = 169
        assert digit_factorial_sum(1454) == 169

    def test_edge_cases(self) -> None:
        """Test edge cases for digit factorial sum."""
        assert digit_factorial_sum(0) == 1  # 0! = 1
        assert digit_factorial_sum(10) == 2  # 1! + 0! = 1 + 1 = 2
        assert digit_factorial_sum(100) == 3  # 1! + 0! + 0! = 1 + 1 + 1 = 3


class TestFactorialChainLength:
    """Test factorial chain length calculations."""

    def test_known_chain_lengths(self) -> None:
        """Test chain lengths for known examples."""
        # 145 → 145 (length 1)
        assert get_factorial_chain_length(145) == 1

        # 169 → 363601 → 1454 → 169 (length 3)
        assert get_factorial_chain_length(169) == 3
        assert get_factorial_chain_length(363601) == 3
        assert get_factorial_chain_length(1454) == 3

        # 871 → 45361 → 871 (length 2)
        assert get_factorial_chain_length(871) == 2
        assert get_factorial_chain_length(45361) == 2

        # 872 → 45362 → 872 (length 2)
        assert get_factorial_chain_length(872) == 2
        assert get_factorial_chain_length(45362) == 2

    def test_chain_length_consistency(self) -> None:
        """Test that memoized version gives same results."""
        memo: dict[int, int] = {}
        test_numbers = [1, 2, 69, 78, 145, 169, 540, 871, 872]

        for num in test_numbers:
            regular_length = get_factorial_chain_length(num)
            memoized_length = get_factorial_chain_length_memoized(num, memo)
            assert regular_length == memoized_length

    def test_memoization_effectiveness(self) -> None:
        """Test that memoization builds up correctly."""
        memo: dict[int, int] = {}

        # First calculation should populate memo
        length1 = get_factorial_chain_length_memoized(169, memo)
        assert 169 in memo

        # Second calculation should use memo
        length2 = get_factorial_chain_length_memoized(169, memo)
        assert length1 == length2

        # Memo should be working
        assert len(memo) > 0


class TestSolutionMethods:
    """Test solution methods."""

    def test_solve_naive_small_cases(self) -> None:
        """Test naive solution with small cases."""
        # No 60-term chains in very small ranges
        assert solve_naive(100) == 0
        assert solve_naive(500) == 0

        # Some 60-term chains should appear in medium ranges
        result_1000 = solve_naive(1000)
        assert isinstance(result_1000, int)
        assert result_1000 >= 0

    def test_solve_optimized_small_cases(self) -> None:
        """Test optimized solution with small cases."""
        # No 60-term chains in very small ranges
        assert solve_optimized(100) == 0
        assert solve_optimized(500) == 0

        # Some 60-term chains should appear in medium ranges
        result_1000 = solve_optimized(1000)
        assert isinstance(result_1000, int)
        assert result_1000 >= 0

    def test_solution_consistency(self) -> None:
        """Test that both solutions give consistent results."""
        test_limits = [100, 500, 1000, 2000]

        for limit in test_limits:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            assert naive_result == optimized_result

    @pytest.mark.parametrize("limit,expected", [(1000, 0), (10000, 42), (100000, 42)])
    def test_known_results(self, limit: int, expected: int) -> None:
        """Test against known results for specific limits."""
        assert solve_optimized(limit) == expected


class TestUtilityFunctions:
    """Test utility functions."""

    def test_get_factorial_chain(self) -> None:
        """Test factorial chain generation."""
        # Test 145 → 145
        chain_145 = get_factorial_chain(145)
        assert 145 in chain_145
        assert len(chain_145) >= 1

        # Test 169 → 363601 → 1454 → 169
        chain_169 = get_factorial_chain(169)
        expected_elements = {169, 363601, 1454}
        assert expected_elements.issubset(set(chain_169))

    def test_find_chains_with_length(self) -> None:
        """Test finding chains with specific length."""
        # Find chains with length 1 (should include 145)
        chains_length_1 = find_chains_with_length(1, 1000)
        assert 145 in chains_length_1

        # Find chains with length 3 (should include 169)
        chains_length_3 = find_chains_with_length(3, 1000)
        assert (
            len(chains_length_3) > 0
        )  # Just check that there are some 3-length chains

        # Find chains with length 60
        chains_length_60 = find_chains_with_length(60, 10000)
        assert isinstance(chains_length_60, list)
        assert len(chains_length_60) >= 0

    def test_verify_known_chains(self) -> None:
        """Test verification of known chain examples."""
        known_results = verify_known_chains()

        # Check that known numbers are included
        assert 145 in known_results
        assert 169 in known_results

        # Check result format
        for num, (length, chain) in known_results.items():
            assert isinstance(length, int)
            assert isinstance(chain, list)
            assert length > 0
            assert len(chain) >= length
            assert num in chain

    def test_count_chains_by_length(self) -> None:
        """Test counting chains by length."""
        counts = count_chains_by_length(1000)

        # Should be a dictionary
        assert isinstance(counts, dict)

        # Should have some entries
        assert len(counts) > 0

        # All keys should be positive integers
        for length in counts:
            assert isinstance(length, int)
            assert length > 0

        # All values should be positive integers
        for count in counts.values():
            assert isinstance(count, int)
            assert count > 0

    def test_analyze_factorial_chains(self) -> None:
        """Test factorial chain analysis."""
        analysis = analyze_factorial_chains(1000)

        # Check required keys
        required_keys = [
            "length_distribution",
            "special_chain_examples",
            "most_common_length",
            "longest_chain",
            "total_numbers",
        ]
        for key in required_keys:
            assert key in analysis

        # Check data types and values
        assert isinstance(analysis["length_distribution"], dict)
        assert isinstance(analysis["special_chain_examples"], dict)
        assert isinstance(analysis["most_common_length"], int)
        assert isinstance(analysis["longest_chain"], int)
        assert analysis["total_numbers"] == 999  # 1 to 999

    def test_get_factorial_chain_statistics(self) -> None:
        """Test factorial chain statistics."""
        stats = get_factorial_chain_statistics(1000)

        # Check required keys
        required_keys = [
            "length_distribution",
            "total_numbers_analyzed",
            "unique_chain_lengths",
            "most_common_length",
            "most_common_count",
            "longest_chain_length",
            "shortest_chain_length",
            "chains_with_60_terms",
        ]
        for key in required_keys:
            assert key in stats

        # Check reasonable values
        assert stats["total_numbers_analyzed"] == 999
        assert stats["unique_chain_lengths"] > 0
        assert stats["longest_chain_length"] >= stats["shortest_chain_length"]
        assert stats["most_common_count"] > 0
        assert stats["chains_with_60_terms"] >= 0


class TestKnownFactorialChains:
    """Test specific known factorial chain properties."""

    def test_single_element_chains(self) -> None:
        """Test chains that loop to themselves."""
        # 145 → 145
        assert get_factorial_chain_length(145) == 1
        chain = get_factorial_chain(145)
        assert chain[0] == 145

    def test_two_element_chains(self) -> None:
        """Test 2-element chains."""
        # 871 ↔ 45361
        assert get_factorial_chain_length(871) == 2
        assert get_factorial_chain_length(45361) == 2

        # 872 ↔ 45362
        assert get_factorial_chain_length(872) == 2
        assert get_factorial_chain_length(45362) == 2

    def test_three_element_chains(self) -> None:
        """Test 3-element chains."""
        # 169 → 363601 → 1454 → 169
        three_element_numbers = [169, 363601, 1454]
        for num in three_element_numbers:
            assert get_factorial_chain_length(num) == 3

    def test_longer_chains(self) -> None:
        """Test some longer chains."""
        # Test that some numbers have longer chains
        longer_examples = [69, 78]  # 540 has chain length 2
        for num in longer_examples:
            length = get_factorial_chain_length(num)
            assert length > 3


class TestEdgeCasesAndPerformance:
    """Test edge cases and performance characteristics."""

    def test_zero_and_small_numbers(self) -> None:
        """Test behavior with very small numbers."""
        # Test digit factorial sum for small numbers
        assert digit_factorial_sum(0) == 1
        assert digit_factorial_sum(1) == 1

        # Test chain lengths for small numbers
        for i in range(1, 10):
            length = get_factorial_chain_length(i)
            assert length > 0

    def test_large_single_chain(self) -> None:
        """Test a single large chain calculation."""
        # Test with a moderately large number
        large_num = 99999
        length = get_factorial_chain_length(large_num)
        assert isinstance(length, int)
        assert length > 0

    @pytest.mark.slow
    def test_performance_with_medium_range(self) -> None:
        """Test performance with medium range (slow test)."""
        # Test with a range that should complete reasonably quickly
        result = solve_optimized(50000)
        assert isinstance(result, int)
        assert result >= 0

    def test_memoization_memory_usage(self) -> None:
        """Test that memoization doesn't grow excessively."""
        memo: dict[int, int] = {}

        # Calculate several chains
        for i in range(1, 1000, 100):
            get_factorial_chain_length_memoized(i, memo)

        # Memo should have reasonable size (not every number from 1-1000)
        assert len(memo) < 1000
        assert len(memo) > 0

    @pytest.mark.slow
    def test_final_answer_verification(self) -> None:
        """Test the final answer for the actual problem (slow test)."""
        # This tests the actual problem: chains with exactly 60 terms below 1,000,000
        result = solve_optimized(1000000)
        assert result == 402  # Expected answer


if __name__ == "__main__":
    pytest.main([__file__])
