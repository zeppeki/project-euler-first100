#!/usr/bin/env python3
"""Tests for Problem 080"""

import pytest

from problems.problem_080 import (
    calculate_sqrt_digital_sum_naive,
    calculate_sqrt_digital_sum_optimized,
    get_irrational_square_roots,
    is_perfect_square,
    solve_naive,
    solve_optimized,
    validate_sqrt_calculation,
)


class TestUtilityFunctions:
    """Test utility functions"""

    def test_is_perfect_square(self) -> None:
        """Test perfect square detection"""
        # Perfect squares
        assert is_perfect_square(0)
        assert is_perfect_square(1)
        assert is_perfect_square(4)
        assert is_perfect_square(9)
        assert is_perfect_square(16)
        assert is_perfect_square(25)
        assert is_perfect_square(36)
        assert is_perfect_square(49)
        assert is_perfect_square(64)
        assert is_perfect_square(81)
        assert is_perfect_square(100)

        # Non-perfect squares
        assert not is_perfect_square(2)
        assert not is_perfect_square(3)
        assert not is_perfect_square(5)
        assert not is_perfect_square(6)
        assert not is_perfect_square(7)
        assert not is_perfect_square(8)
        assert not is_perfect_square(10)
        assert not is_perfect_square(15)
        assert not is_perfect_square(20)

        # Negative numbers
        assert not is_perfect_square(-1)
        assert not is_perfect_square(-4)

    def test_get_irrational_square_roots(self) -> None:
        """Test irrational square root identification"""
        # Test small range
        result = get_irrational_square_roots(10)
        expected = [2, 3, 5, 6, 7, 8, 10]  # Excluding 1, 4, 9
        assert result == expected

        # Test larger range
        result = get_irrational_square_roots(25)
        perfect_squares_up_to_25 = {1, 4, 9, 16, 25}
        expected = [i for i in range(1, 26) if i not in perfect_squares_up_to_25]
        assert result == expected

        # Test edge cases
        assert get_irrational_square_roots(1) == []
        assert get_irrational_square_roots(2) == [2]
        assert get_irrational_square_roots(3) == [2, 3]

    def test_validate_sqrt_calculation(self) -> None:
        """Test square root calculation validation"""
        # Test perfect squares (should return True)
        assert validate_sqrt_calculation(1)
        assert validate_sqrt_calculation(4)
        assert validate_sqrt_calculation(9)
        assert validate_sqrt_calculation(16)

        # Test irrational numbers (should return True for valid calculations)
        assert validate_sqrt_calculation(2)
        assert validate_sqrt_calculation(3)
        assert validate_sqrt_calculation(5)
        assert validate_sqrt_calculation(10)


class TestDigitalSumCalculation:
    """Test digital sum calculation functions"""

    def test_calculate_sqrt_digital_sum_naive_perfect_squares(self) -> None:
        """Test digital sum calculation for perfect squares"""
        # Perfect squares should return 0
        assert calculate_sqrt_digital_sum_naive(1, 10) == 0
        assert calculate_sqrt_digital_sum_naive(4, 10) == 0
        assert calculate_sqrt_digital_sum_naive(9, 10) == 0
        assert calculate_sqrt_digital_sum_naive(16, 10) == 0

    def test_calculate_sqrt_digital_sum_optimized_perfect_squares(self) -> None:
        """Test optimized digital sum calculation for perfect squares"""
        # Perfect squares should return 0
        assert calculate_sqrt_digital_sum_optimized(1, 10) == 0
        assert calculate_sqrt_digital_sum_optimized(4, 10) == 0
        assert calculate_sqrt_digital_sum_optimized(9, 10) == 0
        assert calculate_sqrt_digital_sum_optimized(16, 10) == 0

    def test_calculate_sqrt_digital_sum_naive_irrational(self) -> None:
        """Test digital sum calculation for irrational numbers"""
        # Test √2 with small precision
        result_2 = calculate_sqrt_digital_sum_naive(2, 5)
        assert isinstance(result_2, int)
        assert result_2 > 0

        # Test √3 with small precision
        result_3 = calculate_sqrt_digital_sum_naive(3, 5)
        assert isinstance(result_3, int)
        assert result_3 > 0

        # Results should be different for different numbers
        assert result_2 != result_3

    def test_calculate_sqrt_digital_sum_optimized_irrational(self) -> None:
        """Test optimized digital sum calculation for irrational numbers"""
        # Test √2 with small precision
        result_2 = calculate_sqrt_digital_sum_optimized(2, 5)
        assert isinstance(result_2, int)
        assert result_2 > 0

        # Test √3 with small precision
        result_3 = calculate_sqrt_digital_sum_optimized(3, 5)
        assert isinstance(result_3, int)
        assert result_3 > 0

        # Results should be different for different numbers
        assert result_2 != result_3

    def test_digital_sum_methods_agree(self) -> None:
        """Test that both digital sum methods agree"""
        test_numbers = [2, 3, 5, 7, 8, 10]
        precision = 10

        for n in test_numbers:
            naive_result = calculate_sqrt_digital_sum_naive(n, precision)
            optimized_result = calculate_sqrt_digital_sum_optimized(n, precision)
            assert naive_result == optimized_result, (
                f"Methods disagree for √{n}: {naive_result} != {optimized_result}"
            )

    @pytest.mark.slow
    def test_sqrt_2_known_value(self) -> None:
        """Test √2 with higher precision (known example)"""
        # √2 = 1.41421356237309504880...
        # With precision=10: 1414213562 → digital sum = 1+4+1+4+2+1+3+5+6+2 = 29
        result = calculate_sqrt_digital_sum_naive(2, 10)
        expected = 29
        assert result == expected

        # Test optimized method agrees
        result_opt = calculate_sqrt_digital_sum_optimized(2, 10)
        assert result_opt == expected


class TestSolutionFunctions:
    """Test main solution functions"""

    def test_solve_naive_small_cases(self) -> None:
        """Test naive solution with small test cases"""
        # Test with limit=10, precision=5
        result = solve_naive(10, 5)
        assert isinstance(result, int)
        assert result > 0

        # Test with limit=4 (only √2 and √3)
        result = solve_naive(4, 5)
        assert isinstance(result, int)
        assert result > 0

    def test_solve_optimized_small_cases(self) -> None:
        """Test optimized solution with small test cases"""
        # Test with limit=10, precision=5
        result = solve_optimized(10, 5)
        assert isinstance(result, int)
        assert result > 0

        # Test with limit=4 (only √2 and √3)
        result = solve_optimized(4, 5)
        assert isinstance(result, int)
        assert result > 0

    def test_solutions_agree_small_cases(self) -> None:
        """Test that solutions agree on small cases"""
        test_cases = [
            (4, 5),  # √2, √3 with 5 digits
            (10, 5),  # First 10 numbers with 5 digits
            (16, 3),  # Up to 16 with 3 digits
        ]

        for limit, precision in test_cases:
            naive_result = solve_naive(limit, precision)
            optimized_result = solve_optimized(limit, precision)
            assert naive_result == optimized_result, (
                f"Solutions disagree for limit={limit}, precision={precision}: "
                f"{naive_result} != {optimized_result}"
            )

    @pytest.mark.slow
    def test_solve_naive_full_problem(self) -> None:
        """Test naive solution with full problem parameters"""
        result = solve_naive(100, 100)
        assert isinstance(result, int)
        assert result > 0
        # The result should be a reasonable large number
        assert result > 10000

    @pytest.mark.slow
    def test_solve_optimized_full_problem(self) -> None:
        """Test optimized solution with full problem parameters"""
        result = solve_optimized(100, 100)
        assert isinstance(result, int)
        assert result > 0
        # The result should be a reasonable large number
        assert result > 10000

    @pytest.mark.slow
    def test_solutions_agree_full_problem(self) -> None:
        """Test that all solutions agree on the full problem"""
        naive_result = solve_naive(100, 100)
        optimized_result = solve_optimized(100, 100)

        assert naive_result == optimized_result, (
            f"Naive and optimized disagree: {naive_result} != {optimized_result}"
        )


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_precision_one(self) -> None:
        """Test with precision=1"""
        result = solve_naive(10, 1)
        assert isinstance(result, int)
        assert result >= 0

        result_opt = solve_optimized(10, 1)
        assert result == result_opt

    def test_limit_one(self) -> None:
        """Test with limit=1 (only perfect square)"""
        result = solve_naive(1, 5)
        assert result == 0  # Only 1, which is a perfect square

        result_opt = solve_optimized(1, 5)
        assert result_opt == 0

    def test_limit_two(self) -> None:
        """Test with limit=2 (only √2)"""
        result = solve_naive(2, 5)
        expected = calculate_sqrt_digital_sum_naive(2, 5)
        assert result == expected

        result_opt = solve_optimized(2, 5)
        assert result_opt == expected

    def test_empty_range(self) -> None:
        """Test with no irrational numbers (only perfect squares)"""
        # Range containing only perfect squares
        # For this test, we'd need a custom range, but our function starts from 1
        # So we test with very small limits
        result = solve_naive(1, 5)  # Only 1
        assert result == 0

    def test_large_precision_small_limit(self) -> None:
        """Test with large precision but small limit"""
        result = solve_naive(4, 50)  # √2, √3 with 50 digits
        assert isinstance(result, int)
        assert result > 0

        result_opt = solve_optimized(4, 50)
        assert result == result_opt


class TestComplexScenarios:
    """Test complex scenarios"""

    def test_known_calculation_example(self) -> None:
        """Test with a known calculation example"""
        # Test that √2 with 5 digits gives expected result
        # √2 = 1.4142... → first 5 digits: 14142 → sum = 1+4+1+4+2 = 12
        result = calculate_sqrt_digital_sum_naive(2, 5)
        expected = 12
        assert result == expected

        result_opt = calculate_sqrt_digital_sum_optimized(2, 5)
        assert result_opt == expected

    def test_perfect_squares_filtering(self) -> None:
        """Test that perfect squares are properly filtered out"""
        # Test range that includes many perfect squares
        irrational_roots = get_irrational_square_roots(100)
        perfect_squares = {
            i * i for i in range(1, 11)
        }  # 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

        for square in perfect_squares:
            if square <= 100:
                assert square not in irrational_roots

        # Ensure we have the right count
        expected_count = 100 - len([s for s in perfect_squares if s <= 100])
        assert len(irrational_roots) == expected_count

    def test_consistency_across_runs(self) -> None:
        """Test that results are consistent across multiple runs"""
        # Small test case
        limit, precision = 10, 5

        # Run multiple times
        results = []
        for _ in range(3):
            result = solve_naive(limit, precision)
            results.append(result)

        # All results should be the same
        assert len(set(results)) == 1

        # Test optimized method
        results_opt = []
        for _ in range(3):
            result = solve_optimized(limit, precision)
            results_opt.append(result)

        assert len(set(results_opt)) == 1
        assert results[0] == results_opt[0]

    def test_incremental_limits(self) -> None:
        """Test that increasing limits gives increasing results"""
        precision = 5
        prev_result = 0

        for limit in [4, 9, 16, 25]:
            result = solve_naive(limit, precision)
            assert result >= prev_result  # Should be non-decreasing
            prev_result = result

    @pytest.mark.slow
    def test_precision_scaling(self) -> None:
        """Test that higher precision gives different (usually higher) results"""
        limit = 10
        results = []

        for precision in [5, 10, 20]:
            result = solve_naive(limit, precision)
            results.append(result)

        # Results should generally increase with precision
        # (more digits means higher digital sums)
        assert results[1] >= results[0]  # 10 >= 5
        assert results[2] >= results[1]  # 20 >= 10
