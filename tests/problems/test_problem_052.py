#!/usr/bin/env python3
"""
Tests for Project Euler Problem 052: Permuted multiples
"""

from collections.abc import Callable

import pytest

from problems.problem_052 import (
    are_permutations,
    check_all_multiples_permuted,
    demonstrate_permutation_check,
    find_smallest_permuted_multiple_family,
    get_digit_signature,
    get_digit_signature_str,
    get_permuted_multiples_details,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestUtilityFunctions:
    """Test utility functions"""

    def test_get_digit_signature(self) -> None:
        """Test digit signature generation"""
        # Test simple cases
        assert get_digit_signature(123) == (0, 1, 1, 1, 0, 0, 0, 0, 0, 0)
        assert get_digit_signature(1223) == (0, 1, 2, 1, 0, 0, 0, 0, 0, 0)
        assert get_digit_signature(125874) == (0, 1, 1, 0, 1, 1, 0, 1, 1, 0)

        # Test edge cases
        assert get_digit_signature(0) == (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        assert get_digit_signature(1) == (0, 1, 0, 0, 0, 0, 0, 0, 0, 0)

    def test_get_digit_signature_str(self) -> None:
        """Test digit signature string generation"""
        assert get_digit_signature_str(123) == "123"
        assert get_digit_signature_str(321) == "123"
        assert get_digit_signature_str(125874) == "124578"
        assert get_digit_signature_str(251748) == "124578"

        # Test edge cases
        assert get_digit_signature_str(0) == "0"
        assert get_digit_signature_str(100) == "001"

    def test_are_permutations(self) -> None:
        """Test permutation checking"""
        # Known permutations
        assert are_permutations(125874, 251748)
        assert are_permutations(123, 321)
        assert are_permutations(1234, 4321)

        # Not permutations
        assert not are_permutations(123, 124)
        assert not are_permutations(125874, 125875)
        assert not are_permutations(123, 1234)

        # Same numbers
        assert are_permutations(123, 123)

    def test_check_all_multiples_permuted(self) -> None:
        """Test checking if all multiples are permutations"""
        # Test case from problem description
        assert check_all_multiples_permuted(125874, 2)

        # Test negative cases
        assert not check_all_multiples_permuted(123, 2)
        assert not check_all_multiples_permuted(125874, 6)  # Should fail for 6x


class TestSolutionFunctions:
    """Test main solution functions"""

    @pytest.mark.parametrize(
        "solver", [solve_naive, solve_optimized, solve_mathematical]
    )
    def test_solve_small_cases(self, solver: Callable[[int], int]) -> None:
        """Test solution functions with small test cases"""
        # Test case: 2x permutation
        result = solver(2)
        assert result == 125874
        assert check_all_multiples_permuted(result, 2)

    def test_solve_consistency(self) -> None:
        """Test that all solution methods give the same result for small cases"""
        target_multiples = [2, 3]

        for target in target_multiples:
            results = [
                solve_naive(target),
                solve_optimized(target),
                solve_mathematical(target),
            ]

            # All methods should return the same result
            assert len(set(results)) == 1, (
                f"Inconsistent results for target {target}: {results}"
            )

    def test_solve_main_problem(self) -> None:
        """Test the main problem (6x permutations)"""
        # Use fast algorithms only for regular tests
        result_optimized = solve_optimized(6)
        result_mathematical = solve_mathematical(6)

        # Both optimized methods should agree
        assert result_optimized == result_mathematical
        assert result_optimized > 0  # Should find a valid answer
        assert check_all_multiples_permuted(result_optimized, 6)


class TestAnalysisFunctions:
    """Test analysis and demonstration functions"""

    def test_get_permuted_multiples_details(self) -> None:
        """Test getting permuted multiples details"""
        # Test with known case
        details = get_permuted_multiples_details(125874, 2)
        assert len(details) == 2
        assert details[0] == (1, 125874)
        assert details[1] == (2, 251748)

        # Test with larger case
        details_3 = get_permuted_multiples_details(125874, 3)
        assert len(details_3) == 3
        assert details_3[0] == (1, 125874)
        assert details_3[1] == (2, 251748)
        assert details_3[2] == (3, 377622)

    def test_demonstrate_permutation_check(self) -> None:
        """Test permutation check demonstration"""
        # Test with known permutation
        demo = demonstrate_permutation_check(125874, 251748)
        assert demo["number1"] == 125874
        assert demo["number2"] == 251748
        assert demo["digits1_sorted"] == "124578"
        assert demo["digits2_sorted"] == "124578"
        assert demo["are_permutations"] is True

        # Test with non-permutation
        demo_false = demonstrate_permutation_check(123, 124)
        assert demo_false["are_permutations"] is False

    @pytest.mark.slow
    def test_find_smallest_permuted_multiple_family(self) -> None:
        """Test finding smallest permuted multiple families"""
        # Find families of size 2 or more
        families = find_smallest_permuted_multiple_family(2)
        assert len(families) > 0
        assert 125874 in families  # Should include the known case


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_single_digit_numbers(self) -> None:
        """Test single digit numbers"""
        # Single digits can't have meaningful multiples that are permutations
        for i in range(1, 10):
            assert not check_all_multiples_permuted(i, 2)

    def test_small_multiples(self) -> None:
        """Test behavior with small multiples"""
        # Test with just 1x (should always be true)
        assert check_all_multiples_permuted(123, 1)
        assert check_all_multiples_permuted(1, 1)

    def test_signature_consistency(self) -> None:
        """Test that different signature methods agree"""
        test_numbers = [125874, 251748, 123, 321, 1234, 4321]

        for num in test_numbers:
            # String-based and tuple-based signatures should be consistent
            str_sig = get_digit_signature_str(num)
            tuple_sig = get_digit_signature(num)

            # Convert tuple signature to string for comparison
            tuple_as_str = "".join(
                str(digit) * count for digit, count in enumerate(tuple_sig)
            )
            assert str_sig == tuple_as_str

    def test_mathematical_constraints(self) -> None:
        """Test mathematical constraints for valid solutions"""
        # For a number to have 6x as a permutation, it must start with 1
        # because if it starts with 2 or higher, 6x would have more digits
        result = solve_mathematical(6)
        assert str(result)[0] == "1", f"Result {result} should start with 1"

    def test_performance_bounds(self) -> None:
        """Test that solutions are found within reasonable bounds"""
        # The solution for 6x should be found relatively quickly
        # and should be a reasonable size number
        result = solve_optimized(6)
        assert result < 10**7, f"Result {result} seems too large"
        assert result > 10**5, f"Result {result} seems too small"


if __name__ == "__main__":
    pytest.main([__file__])
