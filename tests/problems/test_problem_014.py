"""Tests for Problem 014: Longest Collatz sequence."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_014 import (
    collatz_length_memoized,
    collatz_length_simple,
    solve_naive,
    solve_optimized,
)


class TestProblem014:
    """Test cases for Problem 014."""

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (2, 1),  # Only 1 -> 1 is the longest (and only) sequence
            (3, 2),  # 1: 1 step, 2: 2 steps -> 2 is longest
            (5, 3),  # 3 has 8 steps: 3→10→5→16→8→4→2→1
            (10, 9),  # 9 has 20 steps, longest under 10
            (14, 9),  # 9 still longest under 14 (13 also has 10 steps)
            (20, 18),  # 18 has 21 steps (18 and 19 both have 21, but 18 is smaller)
            (100, 97),  # 97 has 119 steps
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
            (2, 1),  # Only 1 -> 1 is the longest (and only) sequence
            (3, 2),  # 1: 1 step, 2: 2 steps -> 2 is longest
            (5, 3),  # 3 has 8 steps: 3→10→5→16→8→4→2→1
            (10, 9),  # 9 has 20 steps, longest under 10
            (14, 9),  # 9 still longest under 14 (13 also has 10 steps)
            (20, 18),  # 18 has 21 steps (18 and 19 both have 21, but 18 is smaller)
            (100, 97),  # 97 has 119 steps
            (1000, 871),  # 871 has 179 steps
        ],
    )
    def test_solve_optimized(self, limit: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit={limit}"
        )

    @pytest.mark.parametrize("limit", [2, 3, 5, 10, 14, 20, 100])
    def test_all_solutions_agree(self, limit: int) -> None:
        """Test that naive and optimized solutions give the same result."""
        naive_result = solve_naive(limit)
        optimized_result = solve_optimized(limit)

        assert naive_result == optimized_result, (
            f"Solutions disagree for limit={limit}: "
            f"naive={naive_result}, optimized={optimized_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with limit = 2 (only 1 available)
        assert solve_naive(2) == 1
        assert solve_optimized(2) == 1

        # Test with limit = 3 (1 and 2 available)
        assert solve_naive(3) == 2
        assert solve_optimized(3) == 2

    def test_invalid_input(self) -> None:
        """Test with invalid input."""
        # Both solutions should raise ValueError for limit <= 1
        with pytest.raises(ValueError):
            solve_naive(1)
        with pytest.raises(ValueError):
            solve_optimized(1)

        with pytest.raises(ValueError):
            solve_naive(0)
        with pytest.raises(ValueError):
            solve_optimized(0)

        with pytest.raises(ValueError):
            solve_naive(-1)
        with pytest.raises(ValueError):
            solve_optimized(-1)

    @pytest.mark.slow
    def test_large_number(self) -> None:
        """Test with the actual problem number (marked as slow)."""
        # Test with the actual problem limit using fastest algorithm only
        limit = 1000000
        expected = 837799  # Known Project Euler answer

        # Test optimized solution for speed
        result_optimized = solve_optimized(limit)

        assert result_optimized == expected

    def test_collatz_length_functions(self) -> None:
        """Test the Collatz length calculation helper functions."""
        # Test known sequences
        test_cases = [
            (1, 1),  # 1 -> 1 step
            (2, 2),  # 2 -> 1 (2 steps)
            (3, 8),  # 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (8 steps)
            (4, 3),  # 4 -> 2 -> 1 (3 steps)
            (5, 6),  # 5 -> 16 -> 8 -> 4 -> 2 -> 1 (6 steps)
            (6, 9),  # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (9 steps)
            (
                7,
                17,
            ),  # 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (17 steps)
            (8, 4),  # 8 -> 4 -> 2 -> 1 (4 steps)
            (9, 20),  # 9 -> 28 -> 14 -> 7 -> ... (20 steps total)
            (10, 7),  # 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (7 steps)
            (13, 10),  # 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (10 steps)
        ]

        for n, expected_length in test_cases:
            # Test simple version
            simple_length = collatz_length_simple(n)
            assert simple_length == expected_length, (
                f"Simple: Expected length {expected_length} for n={n}, got {simple_length}"
            )

            # Test memoized version
            memo: dict[int, int] = {}
            memoized_length = collatz_length_memoized(n, memo)
            assert memoized_length == expected_length, (
                f"Memoized: Expected length {expected_length} for n={n}, got {memoized_length}"
            )

    def test_collatz_sequence_properties(self) -> None:
        """Test basic properties of Collatz sequences."""
        # Test that all numbers eventually reach 1
        for n in range(1, 100):
            length = collatz_length_simple(n)
            assert length >= 1, f"Length should be at least 1 for n={n}"

        # Test specific known sequences
        # The sequence from 13: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
        sequence_13 = []
        n = 13
        while n != 1:
            sequence_13.append(n)
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
        sequence_13.append(1)

        expected_13 = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        assert sequence_13 == expected_13, f"Expected {expected_13}, got {sequence_13}"
        assert len(sequence_13) == 10, f"Expected length 10, got {len(sequence_13)}"

    def test_memoization_effectiveness(self) -> None:
        """Test that memoization works correctly."""
        memo: dict[int, int] = {}

        # Calculate for several numbers
        lengths = []
        for n in range(1, 20):
            length = collatz_length_memoized(n, memo)
            lengths.append(length)

        # Verify memo has entries
        assert len(memo) > 0, "Memo should have entries after calculations"

        # Verify memo entries are correct
        for n, expected_length in memo.items():
            if n <= 19:  # Only check numbers we calculated
                actual_length = collatz_length_simple(n)
                assert actual_length == expected_length, (
                    f"Memo entry for {n} is incorrect: expected {actual_length}, got {expected_length}"
                )

    def test_project_euler_example(self) -> None:
        """Test the specific Project Euler example."""
        # From the problem statement:
        # Starting with 13: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
        # This sequence has 10 terms.

        n = 13
        expected_length = 10

        # Test length calculation methods
        assert collatz_length_simple(n) == expected_length
        assert collatz_length_memoized(n, {}) == expected_length

        # Build the actual sequence to verify
        sequence = []
        current = n
        while current != 1:
            sequence.append(current)
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
        sequence.append(1)

        expected_sequence = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        assert sequence == expected_sequence

    def test_performance_comparison(self) -> None:
        """Test that both solutions work for moderate inputs."""
        # Simple functional test without timing overhead
        limit = 100

        # Verify both solutions work
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)

        # Both should give same result
        assert result_naive == result_optimized
        assert result_naive == 97  # Known result for limit=100

    def test_large_values_consistency(self) -> None:
        """Test consistency for larger values."""
        # Test larger values to ensure algorithms remain accurate
        test_limits = [50, 100, 500, 1000]
        expected_results = [27, 97, 327, 871]  # Known results

        for limit, expected in zip(test_limits, expected_results, strict=False):
            if limit <= 100:
                # Test both for smaller limits
                naive_result = solve_naive(limit)
                optimized_result = solve_optimized(limit)

                assert naive_result == optimized_result == expected, (
                    f"Solutions disagree for limit={limit}: "
                    f"naive={naive_result}, optimized={optimized_result}, expected={expected}"
                )
            else:
                # Test only optimized algorithm for larger limits
                optimized_result = solve_optimized(limit)

                assert optimized_result == expected, (
                    f"Optimized solution disagrees for limit={limit}: "
                    f"optimized={optimized_result}, expected={expected}"
                )

    def test_chain_length_ordering(self) -> None:
        """Test some properties of chain length ordering."""
        # Generate lengths for first 20 numbers
        lengths = []
        for n in range(1, 21):
            length = collatz_length_simple(n)
            lengths.append((n, length))

        # Verify specific known patterns
        # 1 has length 1
        assert lengths[0] == (1, 1)

        # Powers of 2 have predictable lengths
        assert collatz_length_simple(2) == 2  # 2 -> 1
        assert collatz_length_simple(4) == 3  # 4 -> 2 -> 1
        assert collatz_length_simple(8) == 4  # 8 -> 4 -> 2 -> 1
        assert collatz_length_simple(16) == 5  # 16 -> 8 -> 4 -> 2 -> 1

    def test_memoization_optimization_correctness(self) -> None:
        """Test that the memoized optimization produces correct results."""
        # Test that memoized version produces the same results as the simple method
        memo: dict[int, int] = {}

        for n in range(1, 100):
            simple_result = collatz_length_simple(n)
            memoized_result = collatz_length_memoized(n, memo)

            assert simple_result == memoized_result, (
                f"Memoized optimization failed for n={n}: "
                f"simple={simple_result}, memoized={memoized_result}"
            )

    def test_algorithm_specific_edge_cases(self) -> None:
        """Test algorithm-specific edge cases."""
        # Test that memoized version handles edge cases correctly
        # Test odd numbers specifically
        odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

        memo: dict[int, int] = {}
        for n in odd_numbers:
            simple_length = collatz_length_simple(n)
            memoized_length = collatz_length_memoized(n, memo)

            assert simple_length == memoized_length, (
                f"Memoized version failed for odd number {n}: "
                f"simple={simple_length}, memoized={memoized_length}"
            )

    def test_boundary_conditions(self) -> None:
        """Test boundary conditions for the problem."""
        # Test numbers near common boundaries
        boundary_tests = [
            (10, 9),  # Single digit boundary
            (100, 97),  # Two digit boundary
            (1000, 871),  # Three digit boundary
        ]

        for limit, expected in boundary_tests:
            result_opt = solve_optimized(limit)

            assert result_opt == expected, (
                f"Boundary test failed for limit={limit}: "
                f"optimized={result_opt}, expected={expected}"
            )

    def test_sequence_generation_accuracy(self) -> None:
        """Test that sequence generation follows Collatz rules correctly."""
        # Test the rules: n/2 (even), 3n+1 (odd)

        # Test even numbers
        assert 6 // 2 == 3
        assert 8 // 2 == 4
        assert 10 // 2 == 5

        # Test odd numbers
        assert 3 * 3 + 1 == 10
        assert 3 * 5 + 1 == 16
        assert 3 * 7 + 1 == 22

        # Test a full sequence manually
        n = 7
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            sequence.append(n)

        # 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
        expected_7 = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        assert sequence == expected_7
        assert len(sequence) == 17  # Should match collatz_length_simple(7)
        assert collatz_length_simple(7) == 17
