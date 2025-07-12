#!/usr/bin/env python3
"""Tests for Problem 049"""

import pytest

# Import functions from common library
from problems.lib import (
    get_digit_signature,
)
from problems.lib import (
    get_permutations_4digit as get_permutations,
)
from problems.lib.primes import is_prime
from problems.problem_049 import (
    find_arithmetic_sequences,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem049:
    """Test cases for Problem 049"""

    def test_get_digit_signature(self) -> None:
        """Test digit signature function"""
        test_cases = [
            (1487, "1478"),
            (4817, "1478"),
            (8147, "1478"),
            (1234, "1234"),
            (4321, "1234"),
            (1000, "0001"),
            (9876, "6789"),
            (1111, "1111"),
        ]

        for num, expected in test_cases:
            result = get_digit_signature(num)
            assert result == expected, (
                f"get_digit_signature({num}) should return '{expected}', got '{result}'"
            )

    def test_get_permutations(self) -> None:
        """Test permutation generation"""
        # Test with 1487
        perms_1487 = get_permutations(1487)

        # Should include the known permutations
        known_perms = [1487, 4817, 8147]
        for perm in known_perms:
            assert perm in perms_1487, f"{perm} should be in permutations of 1487"

        # All should be 4-digit numbers
        for perm in perms_1487:
            assert 1000 <= perm <= 9999, f"{perm} should be a 4-digit number"

        # All should have the same digit signature
        signature = get_digit_signature(1487)
        for perm in perms_1487:
            assert get_digit_signature(perm) == signature, (
                f"{perm} should have same signature as 1487"
            )

        # Test with number containing 0
        perms_1037 = get_permutations(1037)
        # Should not include numbers starting with 0
        for perm in perms_1037:
            assert perm >= 1000, f"{perm} should not start with 0"

        # All permutations should be unique
        assert len(perms_1487) == len(set(perms_1487)), "Permutations should be unique"

    def test_find_arithmetic_sequences(self) -> None:
        """Test arithmetic sequence finding"""
        # Test with known example
        numbers = [1487, 4817, 8147]
        sequences = find_arithmetic_sequences(numbers)
        expected = (1487, 4817, 8147)
        assert expected in sequences, f"Should find sequence {expected}"

        # Test with unsorted input
        numbers_unsorted = [8147, 1487, 4817]
        sequences_unsorted = find_arithmetic_sequences(numbers_unsorted)
        assert expected in sequences_unsorted, (
            f"Should find sequence {expected} even with unsorted input"
        )

        # Test with no arithmetic sequence
        numbers_no_seq = [1000, 2000, 5000]
        sequences_no_seq = find_arithmetic_sequences(numbers_no_seq)
        assert len(sequences_no_seq) == 0, (
            "Should find no sequences in non-arithmetic numbers"
        )

        # Test with multiple sequences
        numbers_multi = [1, 2, 3, 4, 5, 6]  # Contains multiple arithmetic subsequences
        sequences_multi = find_arithmetic_sequences(numbers_multi)
        assert len(sequences_multi) > 0, "Should find arithmetic sequences"

        # Verify all found sequences are actually arithmetic
        for seq in sequences_multi:
            diff1 = seq[1] - seq[0]
            diff2 = seq[2] - seq[1]
            assert diff1 == diff2, f"Sequence {seq} should be arithmetic"

        # Test with duplicates (should handle gracefully)
        numbers_dup = [1, 2, 2, 3]
        find_arithmetic_sequences(numbers_dup)
        # Should still work correctly

    def test_known_example_properties(self) -> None:
        """Test properties of the known example sequence"""
        known_sequence = [1487, 4817, 8147]

        # All should be prime
        for num in known_sequence:
            assert is_prime(num), f"{num} should be prime"

        # All should have same digit signature
        signatures = [get_digit_signature(num) for num in known_sequence]
        assert len(set(signatures)) == 1, "All numbers should have same digit signature"

        # Should form arithmetic sequence
        diff1 = known_sequence[1] - known_sequence[0]
        diff2 = known_sequence[2] - known_sequence[1]
        assert diff1 == diff2, "Should form arithmetic sequence"
        assert diff1 == 3330, "Difference should be 3330"

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        assert isinstance(result, int), "Result should be an integer"
        assert result > 0, "Result should be positive"

        # Should be 12 digits (concatenation of three 4-digit numbers)
        result_str = str(result)
        assert len(result_str) == 12, (
            f"Result should be 12 digits, got {len(result_str)}"
        )

        # Extract the three numbers
        a = int(result_str[0:4])
        b = int(result_str[4:8])
        c = int(result_str[8:12])

        # Verify properties
        assert all(is_prime(x) for x in [a, b, c]), "All three numbers should be prime"
        assert b - a == c - b, "Should form arithmetic sequence"

        signature_a = get_digit_signature(a)
        signature_b = get_digit_signature(b)
        signature_c = get_digit_signature(c)
        assert signature_a == signature_b == signature_c, "All should be permutations"

        # Should not be the known example
        assert (a, b, c) != (1487, 4817, 8147), "Should not be the known example"

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int), "Result should be an integer"
        assert result > 0, "Result should be positive"

        # Should be 12 digits
        result_str = str(result)
        assert len(result_str) == 12, (
            f"Result should be 12 digits, got {len(result_str)}"
        )

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution"""
        result = solve_mathematical()
        assert isinstance(result, int), "Result should be an integer"
        assert result > 0, "Result should be positive"

        # Should be 12 digits
        result_str = str(result)
        assert len(result_str) == 12, (
            f"Result should be 12 digits, got {len(result_str)}"
        )

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert naive_result == optimized_result, (
            f"Naive and optimized disagree: {naive_result} != {optimized_result}"
        )
        assert naive_result == mathematical_result, (
            f"Naive and mathematical disagree: {naive_result} != {mathematical_result}"
        )
        assert optimized_result == mathematical_result, (
            f"Optimized and mathematical disagree: {optimized_result} != {mathematical_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases"""
        # Test get_permutations with edge cases
        perms_1000 = get_permutations(1000)
        # Should not include numbers with leading zeros as 4-digit numbers
        for perm in perms_1000:
            assert perm >= 1000, f"Permutation {perm} should be >= 1000"

        # Test find_arithmetic_sequences with edge cases
        empty_sequences = find_arithmetic_sequences([])
        assert len(empty_sequences) == 0, "Empty list should produce no sequences"

        single_sequences = find_arithmetic_sequences([1487])
        assert len(single_sequences) == 0, "Single number should produce no sequences"

        two_sequences = find_arithmetic_sequences([1487, 4817])
        assert len(two_sequences) == 0, "Two numbers should produce no sequences"

    def test_permutation_properties(self) -> None:
        """Test properties of permutation generation"""
        # Test with various 4-digit numbers
        test_numbers = [1234, 5678, 9876, 1023, 4567]

        for num in test_numbers:
            perms = get_permutations(num)

            # All permutations should be 4-digit numbers
            for perm in perms:
                assert 1000 <= perm <= 9999, f"Permutation {perm} should be 4-digit"

            # Original number should be included
            assert num in perms, f"Original number {num} should be in its permutations"

            # All should have same digit signature
            original_sig = get_digit_signature(num)
            for perm in perms:
                assert get_digit_signature(perm) == original_sig, (
                    f"Permutation {perm} should have same signature"
                )

    def test_arithmetic_sequence_properties(self) -> None:
        """Test properties of arithmetic sequence finding"""
        # Test with known arithmetic progressions
        test_cases = [
            [1, 3, 5],  # diff = 2
            [10, 20, 30],  # diff = 10
            [100, 150, 200],  # diff = 50
        ]

        for numbers in test_cases:
            sequences = find_arithmetic_sequences(numbers)
            assert len(sequences) >= 1, (
                f"Should find at least one sequence in {numbers}"
            )

            # Verify the found sequence
            for seq in sequences:
                diff1 = seq[1] - seq[0]
                diff2 = seq[2] - seq[1]
                assert diff1 == diff2, f"Sequence {seq} should be arithmetic"
                assert diff1 > 0, f"Difference should be positive in {seq}"

    @pytest.mark.slow
    def test_performance_comparison(self) -> None:
        """Test performance of different methods (marked as slow)"""
        import time

        methods = [
            ("Naive", solve_naive),
            ("Optimized", solve_optimized),
            ("Mathematical", solve_mathematical),
        ]

        results = {}
        for name, method in methods:
            start_time = time.time()
            result = method()
            end_time = time.time()

            results[name] = {"result": result, "time": end_time - start_time}

        # All methods should give the same result
        result_values = [data["result"] for data in results.values()]
        assert len(set(result_values)) == 1, f"Methods disagree: {result_values}"

        # All methods should complete successfully
        for name, data in results.items():
            assert data["time"] >= 0, f"{name} method should complete"
            assert data["result"] > 0, f"{name} method should return positive result"

    def test_return_types(self) -> None:
        """Test that all functions return proper types"""
        # Test utility functions
        assert isinstance(is_prime(1487), bool), "is_prime should return bool"
        assert isinstance(get_digit_signature(1487), str), (
            "get_digit_signature should return str"
        )
        assert isinstance(get_permutations(1487), list), (
            "get_permutations should return list"
        )
        assert isinstance(find_arithmetic_sequences([1, 2, 3]), list), (
            "find_arithmetic_sequences should return list"
        )

        # Test solution functions
        methods = [solve_naive, solve_optimized, solve_mathematical]
        for method in methods:
            result = method()
            assert isinstance(result, int), f"{method.__name__} should return int"
            assert result >= 0, f"{method.__name__} should return non-negative integer"
