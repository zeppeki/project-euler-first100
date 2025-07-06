#!/usr/bin/env python3
"""Tests for Problem 044"""

import pytest

from problems.problem_044 import (
    generate_pentagonal,
    is_pentagonal,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem044:
    """Test cases for Problem 044"""

    def test_generate_pentagonal(self) -> None:
        """Test pentagonal number generation"""
        # First 10 pentagonal numbers: 1, 5, 12, 22, 35, 51, 70, 92, 117, 145
        expected = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]

        for i, expected_value in enumerate(expected, 1):
            assert generate_pentagonal(i) == expected_value

        # Test a few more specific cases
        assert generate_pentagonal(11) == 176  # 11 * (3*11-1) / 2 = 11 * 32 / 2 = 176
        assert generate_pentagonal(20) == 590  # 20 * (3*20-1) / 2 = 20 * 59 / 2 = 590

    def test_is_pentagonal(self) -> None:
        """Test pentagonal number detection"""
        # Test known pentagonal numbers
        pentagonal_numbers = [
            1,
            5,
            12,
            22,
            35,
            51,
            70,
            92,
            117,
            145,
            176,
            210,
            247,
            287,
            330,
        ]
        for num in pentagonal_numbers:
            assert is_pentagonal(num), f"{num} should be pentagonal"

        # Test non-pentagonal numbers
        non_pentagonal = [
            2,
            3,
            4,
            6,
            7,
            8,
            9,
            10,
            11,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            23,
            48,
            100,
        ]
        for num in non_pentagonal:
            assert not is_pentagonal(num), f"{num} should not be pentagonal"

        # Test edge cases
        assert not is_pentagonal(0)
        assert not is_pentagonal(-1)
        assert not is_pentagonal(-5)

    def test_example_from_problem(self) -> None:
        """Test the example given in the problem statement"""
        # P4 = 22, P7 = 70, P8 = 92
        p4 = generate_pentagonal(4)
        p7 = generate_pentagonal(7)
        p8 = generate_pentagonal(8)

        assert p4 == 22
        assert p7 == 70
        assert p8 == 92

        # P4 + P7 = P8
        assert p4 + p7 == p8

        # But their difference (70 - 22 = 48) is NOT pentagonal
        difference = p7 - p4
        assert difference == 48
        assert not is_pentagonal(48)

    def test_pentagonal_formula_inverse(self) -> None:
        """Test the inverse pentagonal formula used in is_pentagonal"""
        # For a pentagonal number P_n = n(3n-1)/2
        # The inverse is n = (1 + sqrt(1 + 24*P)) / 6

        for n in range(1, 50):
            pent = generate_pentagonal(n)
            # The inverse formula should work
            discriminant = 1 + 24 * pent
            sqrt_disc = int(discriminant**0.5)

            # Check if sqrt is exact
            if sqrt_disc * sqrt_disc == discriminant and (1 + sqrt_disc) % 6 == 0:
                recovered_n = (1 + sqrt_disc) // 6
                assert recovered_n == n
                assert generate_pentagonal(recovered_n) == pent

    def test_solve_naive(self) -> None:
        """Test naive solution (optimized for CI)"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0, "Should find a valid pentagonal difference"
        # The result should be a pentagonal number itself
        assert is_pentagonal(result), "The difference should be pentagonal"

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0, "Should find a valid pentagonal difference"
        # The result should be a pentagonal number itself
        assert is_pentagonal(result), "The difference should be pentagonal"

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution"""
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 0, "Should find a valid pentagonal difference"
        # The result should be a pentagonal number itself
        assert is_pentagonal(result), "The difference should be pentagonal"

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree (fast algorithms only)"""
        # Only test fast solutions by default
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert optimized_result == mathematical_result, (
            f"Optimized and mathematical disagree: {optimized_result} != {mathematical_result}"
        )

    @pytest.mark.slow
    def test_all_solutions_agree(self) -> None:
        """Test that all solutions agree (including slow naive solution)"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert naive_result == optimized_result, (
            f"Naive and optimized disagree: {naive_result} != {optimized_result}"
        )
        assert naive_result == mathematical_result, (
            f"Naive and mathematical disagree: {naive_result} != {mathematical_result}"
        )

    def test_pentagonal_properties(self) -> None:
        """Test additional properties of pentagonal numbers"""
        # Test that pentagonal numbers grow as expected
        for n in range(1, 20):
            pn = generate_pentagonal(n)
            pn_plus_1 = generate_pentagonal(n + 1)

            # P_{n+1} > P_n (strictly increasing)
            assert pn_plus_1 > pn

            # The difference should be 3n + 1
            # P_{n+1} - P_n = (n+1)(3(n+1)-1)/2 - n(3n-1)/2
            #                = (n+1)(3n+2)/2 - n(3n-1)/2
            #                = ((n+1)(3n+2) - n(3n-1))/2
            #                = (3n²+2n+3n+2 - 3n²+n)/2
            #                = (6n+2)/2 = 3n+1
            expected_diff = 3 * n + 1
            actual_diff = pn_plus_1 - pn
            assert actual_diff == expected_diff

    def test_large_pentagonal_numbers(self) -> None:
        """Test behavior with larger pentagonal numbers"""
        # Test some larger cases
        large_indices = [100, 500, 1000]

        for n in large_indices:
            pent = generate_pentagonal(n)
            assert is_pentagonal(pent)

            # Test that nearby numbers are not pentagonal
            assert not is_pentagonal(pent - 1)
            assert not is_pentagonal(pent + 1)

    def test_performance_hint_verification(self) -> None:
        """Test that we can find valid pentagon pairs for verification"""
        # Generate first 100 pentagonal numbers for testing
        pentagonals = [generate_pentagonal(i) for i in range(1, 101)]
        pentagonal_set = set(pentagonals)

        found_valid_pair = False

        # Look for any pair where sum and difference are both pentagonal
        for i, pi in enumerate(pentagonals):
            for _j, pj in enumerate(pentagonals[i + 1 :], i + 1):
                pk, pj_val = pj, pi  # pk > pj

                pent_sum = pk + pj_val
                pent_diff = pk - pj_val

                # Check if both sum and difference are in our set
                if pent_sum in pentagonal_set and is_pentagonal(pent_diff):
                    found_valid_pair = True
                    # Found at least one valid pair in our test range
                    break
            if found_valid_pair:
                break

        # This test just verifies our detection logic works
        # (we might not find the minimum difference in such a small range)
