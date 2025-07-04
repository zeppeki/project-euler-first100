#!/usr/bin/env python3
"""Tests for Problem 048"""

from problems.problem_048 import (
    calculate_self_powers_sum,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem048:
    """Test cases for Problem 048"""

    def test_individual_self_powers(self) -> None:
        """Test individual self power calculations"""
        test_cases = [
            (1, 1),  # 1^1 = 1
            (2, 4),  # 2^2 = 4
            (3, 27),  # 3^3 = 27
            (4, 256),  # 4^4 = 256
            (5, 3125),  # 5^5 = 3125
            (6, 46656),  # 6^6 = 46656
            (7, 823543),  # 7^7 = 823543
        ]

        for base, expected in test_cases:
            result = pow(base, base)
            assert result == expected, (
                f"{base}^{base} should equal {expected}, got {result}"
            )

    def test_small_sums(self) -> None:
        """Test sums for small limits"""
        # Test cases calculated manually
        test_cases = [
            (1, 1),  # 1^1 = 1
            (2, 5),  # 1^1 + 2^2 = 1 + 4 = 5
            (3, 32),  # 1^1 + 2^2 + 3^3 = 1 + 4 + 27 = 32
            (4, 288),  # 1^1 + 2^2 + 3^3 + 4^4 = 1 + 4 + 27 + 256 = 288
            (5, 3413),  # 1^1 + 2^2 + 3^3 + 4^4 + 5^5 = 1 + 4 + 27 + 256 + 3125 = 3413
        ]

        for limit, expected in test_cases:
            # Use helper function for full calculation
            full_result = calculate_self_powers_sum(limit)
            assert full_result == expected, (
                f"Full calculation: limit {limit} should give {expected}, got {full_result}"
            )

            # Test that the modular versions agree with each other
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            mathematical_result = solve_mathematical(limit)

            expected_mod = expected % (10**10)
            assert naive_result == expected_mod, (
                f"Naive: limit {limit} should give {expected_mod}, got {naive_result}"
            )
            assert optimized_result == expected_mod, (
                f"Optimized: limit {limit} should give {expected_mod}, got {optimized_result}"
            )
            assert mathematical_result == expected_mod, (
                f"Mathematical: limit {limit} should give {expected_mod}, got {mathematical_result}"
            )

    def test_problem_example(self) -> None:
        """Test the example from the problem statement"""
        # 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
        limit = 10
        expected = 10405071317

        # Test full calculation
        full_result = calculate_self_powers_sum(limit)
        assert full_result == expected, (
            f"Full calculation should give {expected}, got {full_result}"
        )

        # Test modular calculations (should all agree with each other)
        naive_result = solve_naive(limit)
        optimized_result = solve_optimized(limit)
        mathematical_result = solve_mathematical(limit)

        expected_mod = expected % (10**10)
        assert naive_result == expected_mod, (
            f"Naive: example should give {expected_mod}, got {naive_result}"
        )
        assert optimized_result == expected_mod, (
            f"Optimized: example should give {expected_mod}, got {optimized_result}"
        )
        assert mathematical_result == expected_mod, (
            f"Mathematical: example should give {expected_mod}, got {mathematical_result}"
        )

    def test_modular_arithmetic_correctness(self) -> None:
        """Test that modular arithmetic gives correct last 10 digits"""
        # Test with different limits
        test_limits = [10, 20, 50, 100]

        for limit in test_limits:
            # Calculate using helper function (full calculation)
            total = calculate_self_powers_sum(limit)
            expected_last_10 = total % (10**10)

            # Test all methods
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            mathematical_result = solve_mathematical(limit)

            assert naive_result == expected_last_10, (
                f"Naive failed for limit {limit}: expected {expected_last_10}, got {naive_result}"
            )
            assert optimized_result == expected_last_10, (
                f"Optimized failed for limit {limit}: expected {expected_last_10}, got {optimized_result}"
            )
            assert mathematical_result == expected_last_10, (
                f"Mathematical failed for limit {limit}: expected {expected_last_10}, got {mathematical_result}"
            )

    def test_large_number_handling(self) -> None:
        """Test handling of very large numbers"""
        # Test with limit 100 - numbers get very large
        limit = 100

        naive_result = solve_naive(limit)
        optimized_result = solve_optimized(limit)
        mathematical_result = solve_mathematical(limit)

        # All should be valid 10-digit numbers (or less)
        assert 0 <= naive_result < 10**10, (
            f"Naive result should be < 10^10, got {naive_result}"
        )
        assert 0 <= optimized_result < 10**10, (
            f"Optimized result should be < 10^10, got {optimized_result}"
        )
        assert 0 <= mathematical_result < 10**10, (
            f"Mathematical result should be < 10^10, got {mathematical_result}"
        )

        # All should give the same result
        assert naive_result == optimized_result, (
            f"Naive != Optimized: {naive_result} != {optimized_result}"
        )
        assert naive_result == mathematical_result, (
            f"Naive != Mathematical: {naive_result} != {mathematical_result}"
        )

    def test_multiples_of_ten_behavior(self) -> None:
        """Test behavior with multiples of 10"""
        # Test that multiples of 10 are handled correctly
        for i in [10, 20, 30, 40, 50]:
            # i^i where i is multiple of 10 should have specific behavior
            power = pow(i, i, 10**10)  # Last 10 digits of i^i

            # For large multiples of 10, i^i mod 10^10 should be 0
            # since i^i contains factor 10^i where i >= 10
            if i >= 10:
                assert power == 0, f"{i}^{i} mod 10^10 should be 0, got {power}"

    def test_edge_cases(self) -> None:
        """Test edge cases"""
        # Test with limit 1
        assert solve_naive(1) == 1
        assert solve_optimized(1) == 1
        assert solve_mathematical(1) == 1

        # Test with limit 0 (edge case)
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0
        assert solve_mathematical(0) == 0

    def test_consistency_across_methods(self) -> None:
        """Test that all three methods give consistent results"""
        test_limits = [1, 5, 10, 25, 50, 100]

        for limit in test_limits:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            mathematical_result = solve_mathematical(limit)

            assert naive_result == optimized_result, (
                f"Naive != Optimized for limit {limit}: {naive_result} != {optimized_result}"
            )
            assert naive_result == mathematical_result, (
                f"Naive != Mathematical for limit {limit}: {naive_result} != {mathematical_result}"
            )
            assert optimized_result == mathematical_result, (
                f"Optimized != Mathematical for limit {limit}: {optimized_result} != {mathematical_result}"
            )

    def test_solve_naive(self) -> None:
        """Test naive solution with default parameters"""
        result = solve_naive()
        assert isinstance(result, int)
        assert 0 <= result < 10**10, "Result should be last 10 digits"

    def test_solve_optimized(self) -> None:
        """Test optimized solution with default parameters"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert 0 <= result < 10**10, "Result should be last 10 digits"

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution with default parameters"""
        result = solve_mathematical()
        assert isinstance(result, int)
        assert 0 <= result < 10**10, "Result should be last 10 digits"

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree on the main problem"""
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

    def test_mathematical_properties(self) -> None:
        """Test mathematical properties of self powers"""
        # Test that full sum is always non-negative and increasing
        prev_sum = 0
        for limit in range(1, 21):
            current_sum = calculate_self_powers_sum(limit)
            assert current_sum >= prev_sum, (
                f"Full sum should be increasing: {prev_sum} -> {current_sum}"
            )
            prev_sum = current_sum

        # Test that individual terms contribute correctly (using full calculation)
        sum_5 = calculate_self_powers_sum(5)
        sum_4 = calculate_self_powers_sum(4)
        fifth_term = pow(5, 5)

        expected_diff = fifth_term
        actual_diff = sum_5 - sum_4

        assert actual_diff == expected_diff, (
            f"Fifth term should contribute {expected_diff}, but difference is {actual_diff}"
        )

        # Test modular properties
        sum_5_mod = solve_naive(5)
        sum_4_mod = solve_naive(4)
        fifth_term_mod = pow(5, 5) % (10**10)

        expected_diff_mod = fifth_term_mod
        actual_diff_mod = (sum_5_mod - sum_4_mod) % (10**10)

        assert actual_diff_mod == expected_diff_mod, (
            f"Fifth term (mod) should contribute {expected_diff_mod}, but difference is {actual_diff_mod}"
        )

    def test_return_types(self) -> None:
        """Test that all functions return proper integer types"""
        methods = [solve_naive, solve_optimized, solve_mathematical]

        for method in methods:
            result = method(10)
            assert isinstance(result, int), (
                f"{method.__name__} should return int, got {type(result)}"
            )
            assert result >= 0, (
                f"{method.__name__} should return non-negative integer, got {result}"
            )
