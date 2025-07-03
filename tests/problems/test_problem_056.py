#!/usr/bin/env python3
"""
Tests for Project Euler Problem 056: Powerful digit sum
"""

from collections.abc import Callable

import pytest

from problems.problem_056 import (
    analyze_digit_sum_patterns,
    demonstrate_special_cases,
    digit_sum,
    find_high_digit_sum_examples,
    find_max_digit_sum_with_details,
    get_digit_sum_statistics,
    solve_naive,
    solve_optimized,
    verify_examples,
)


class TestUtilityFunctions:
    """Test utility functions for digit sum calculation"""

    def test_digit_sum(self) -> None:
        """Test digit sum calculation"""
        # Single digit numbers
        assert digit_sum(0) == 0
        assert digit_sum(5) == 5
        assert digit_sum(9) == 9

        # Multi-digit numbers
        assert digit_sum(12) == 3
        assert digit_sum(123) == 6
        assert digit_sum(999) == 27
        assert digit_sum(1234) == 10

        # Large numbers
        assert digit_sum(10**100) == 1  # Googol
        assert digit_sum(999999999) == 81

    def test_digit_sum_powers(self) -> None:
        """Test digit sum with power calculations"""
        # Small powers
        assert digit_sum(2**3) == digit_sum(8) == 8
        assert digit_sum(3**3) == digit_sum(27) == 9
        assert digit_sum(9**2) == digit_sum(81) == 9

        # Known examples
        assert digit_sum(9**9) == 45  # 387420489 -> 3+8+7+4+2+0+4+8+9 = 45


class TestExamplesVerification:
    """Test the example verification function"""

    def test_verify_examples(self) -> None:
        """Test that the examples verification function works"""
        assert verify_examples() is True

    def test_googol_digit_sum(self) -> None:
        """Test that googol (10^100) has digit sum 1"""
        googol = 10**100
        assert digit_sum(googol) == 1

    def test_hundred_power_hundred(self) -> None:
        """Test that 100^100 has a reasonable digit sum"""
        # 100^100 is very large but starts with 1 followed by many 0s
        result = 100**100
        ds = digit_sum(result)

        # Should be much smaller than the number of digits
        assert ds < 1000  # Reasonable upper bound
        assert ds > 0  # Should be positive


class TestSolutionFunctions:
    """Test main solution functions"""

    @pytest.mark.parametrize("solver", [solve_naive, solve_optimized])
    def test_solve_consistency(self, solver: Callable[[int, int], int]) -> None:
        """Test that solution methods work with small limits"""
        # Test with small limits first
        result_5 = solver(5, 5)
        assert isinstance(result_5, int)
        assert result_5 > 0

        result_10 = solver(10, 10)
        assert isinstance(result_10, int)
        assert (
            result_10 >= result_5
        )  # Larger range should give at least as large result

    def test_solve_agreement(self) -> None:
        """Test that all solution methods agree"""
        # Test with smaller limits for speed
        limit = 20
        result_naive = solve_naive(limit, limit)
        result_optimized = solve_optimized(limit, limit)

        assert result_naive == result_optimized

    def test_solve_known_results(self) -> None:
        """Test with known results for small limits"""
        # Test with very small limit where we can manually verify
        result_5 = solve_naive(5, 5)
        assert result_5 > 0

        # 9^9 = 387420489 has digit sum 45, which should be high for small ranges
        result_10 = solve_naive(10, 10)
        assert result_10 >= 45  # Should include 9^9

    @pytest.mark.slow
    def test_solve_full_problem(self) -> None:
        """Test the full problem (marked as slow test)"""
        result = solve_naive(100, 100)
        assert isinstance(result, int)
        assert result > 500  # Should be reasonably high
        assert result < 1000  # Reasonable upper bound


class TestAnalysisFunctions:
    """Test analysis and statistics functions"""

    def test_find_max_digit_sum_with_details(self) -> None:
        """Test detailed max digit sum finding"""
        details = find_max_digit_sum_with_details(10, 10)

        assert "max_digit_sum" in details
        assert "best_a" in details
        assert "best_b" in details
        assert "best_power" in details
        assert "power_length" in details

        assert details["max_digit_sum"] > 0
        assert 1 <= details["best_a"] < 10
        assert 1 <= details["best_b"] < 10
        assert details["best_power"] == details["best_a"] ** details["best_b"]
        assert details["power_length"] == len(str(details["best_power"]))

    def test_analyze_digit_sum_patterns(self) -> None:
        """Test digit sum pattern analysis"""
        analysis = analyze_digit_sum_patterns(5, 5)

        assert "all_results" in analysis
        assert "top_10" in analysis
        assert "digit_sum_frequency" in analysis
        assert "total_combinations" in analysis

        assert analysis["total_combinations"] == 4 * 4  # (1-4) x (1-4)
        assert len(analysis["all_results"]) == 16
        assert len(analysis["top_10"]) <= 10

        # Results should be sorted by digit sum
        top_results = analysis["top_10"]
        for i in range(len(top_results) - 1):
            assert top_results[i]["digit_sum"] >= top_results[i + 1]["digit_sum"]

    def test_find_high_digit_sum_examples(self) -> None:
        """Test finding high digit sum examples"""
        # Test with low threshold
        examples = find_high_digit_sum_examples(10, 10, 10)

        assert isinstance(examples, list)
        assert len(examples) > 0

        # All examples should have digit sum >= threshold
        for example in examples:
            assert example["digit_sum"] >= 10
            assert "a" in example
            assert "b" in example
            assert "power" in example
            assert "power_length" in example
            assert example["power"] == example["a"] ** example["b"]

    def test_demonstrate_special_cases(self) -> None:
        """Test special cases demonstration"""
        special_cases = demonstrate_special_cases()

        assert isinstance(special_cases, list)
        assert len(special_cases) > 0

        # Check that googol case is included
        googol_case = next(
            (case for case in special_cases if case["a"] == 10 and case["b"] == 100),
            None,
        )
        assert googol_case is not None
        assert googol_case["digit_sum"] == 1

    def test_get_digit_sum_statistics(self) -> None:
        """Test digit sum statistics"""
        stats = get_digit_sum_statistics(5, 5)

        assert "max_digit_sum" in stats
        assert "min_digit_sum" in stats
        assert "average_digit_sum" in stats
        assert "total_combinations" in stats
        assert "digit_sum_distribution" in stats
        assert "unique_digit_sums" in stats

        assert stats["total_combinations"] == 4 * 4  # (1-4) x (1-4)
        assert stats["max_digit_sum"] >= stats["min_digit_sum"]
        assert stats["min_digit_sum"] > 0
        assert stats["average_digit_sum"] > 0
        assert len(stats["digit_sum_distribution"]) == stats["unique_digit_sums"]


class TestBoundaryConditions:
    """Test boundary conditions and edge cases"""

    def test_limit_one(self) -> None:
        """Test with limit of 1 (no valid combinations)"""
        result = solve_naive(1, 1)
        assert result == 0  # No combinations with a,b < 1

    def test_limit_two(self) -> None:
        """Test with limit of 2 (only 1^1)"""
        result = solve_naive(2, 2)
        assert result == 1  # Only 1^1 = 1, digit sum = 1

    def test_limit_three(self) -> None:
        """Test with limit of 3"""
        result = solve_naive(3, 3)
        # Possible: 1^1=1(1), 1^2=1(1), 2^1=2(2), 2^2=4(4)
        assert result == 4  # 2^2 = 4 has highest digit sum

    def test_asymmetric_limits(self) -> None:
        """Test with different limits for a and b"""
        result1 = solve_naive(5, 10)
        result2 = solve_naive(10, 5)

        assert isinstance(result1, int)
        assert isinstance(result2, int)
        assert result1 > 0
        assert result2 > 0


class TestPerformance:
    """Test performance-related aspects"""

    def test_small_limit_performance(self) -> None:
        """Test performance with small limits"""
        import time

        start_time = time.time()
        result = solve_naive(20, 20)
        end_time = time.time()

        assert isinstance(result, int)
        assert end_time - start_time < 1.0  # Should complete in less than 1 second

    def test_optimization_comparison(self) -> None:
        """Test that optimization doesn't hurt correctness"""
        # Test with moderate limit
        limit = 15
        result_naive = solve_naive(limit, limit)
        result_optimized = solve_optimized(limit, limit)

        assert result_naive == result_optimized


class TestSpecialCases:
    """Test special cases and mathematical properties"""

    def test_power_of_ten(self) -> None:
        """Test powers of 10 have low digit sums"""
        # 10^n always has digit sum 1
        for n in range(1, 10):
            power_of_ten = 10**n
            assert digit_sum(power_of_ten) == 1

    def test_power_of_one(self) -> None:
        """Test that 1^n always equals 1"""
        for n in range(1, 100):
            assert 1**n == 1
            assert digit_sum(1**n) == 1

    def test_large_base_small_exponent(self) -> None:
        """Test large base with small exponent"""
        # 99^1 = 99, digit sum = 18
        assert digit_sum(99**1) == 18

        # 99^2 = 9801, digit sum = 18
        assert digit_sum(99**2) == 18

    def test_small_base_large_exponent(self) -> None:
        """Test small base with large exponent"""
        # 2^10 = 1024, digit sum = 7
        assert digit_sum(2**10) == 7

        # 3^10 = 59049, digit sum = 27
        assert digit_sum(3**10) == 27

    def test_nine_powers(self) -> None:
        """Test powers of 9 (often have high digit sums)"""
        # 9^2 = 81, digit sum = 9
        assert digit_sum(9**2) == 9

        # 9^3 = 729, digit sum = 18
        assert digit_sum(9**3) == 18

        # 9^4 = 6561, digit sum = 18
        assert digit_sum(9**4) == 18


class TestMathematicalProperties:
    """Test mathematical properties of digit sums"""

    def test_digit_sum_bounds(self) -> None:
        """Test that digit sums are bounded reasonably"""
        # For a^b where a,b < 100, the maximum possible digit sum
        # should be much less than 9 * number_of_digits
        max_details = find_max_digit_sum_with_details(20, 20)
        max_possible = 9 * max_details["power_length"]

        assert max_details["max_digit_sum"] <= max_possible
        assert max_details["max_digit_sum"] > 0

    def test_digit_sum_monotonicity(self) -> None:
        """Test some monotonicity properties"""
        # Adding more digits can only increase the maximum possible digit sum
        result_5 = solve_naive(5, 5)
        result_10 = solve_naive(10, 10)

        assert result_10 >= result_5


if __name__ == "__main__":
    pytest.main([__file__])
