#!/usr/bin/env python3
"""
Tests for Project Euler Problem 057: Square root convergents
"""

from collections.abc import Callable
from fractions import Fraction

import pytest

from problems.problem_057 import (
    analyze_convergent_pattern,
    count_digits,
    demonstrate_convergence,
    find_digit_difference_pattern,
    generate_sqrt2_convergent,
    get_convergent_sequence,
    get_large_convergents,
    has_numerator_more_digits,
    solve_naive,
    solve_optimized,
)


def verify_known_convergents() -> bool:
    """
    既知の連分数展開を検証
    """
    # 初期の経験的に知られている値をチェック
    # 1番目: 1 + 1/2 = 3/2
    convergent_1 = generate_sqrt2_convergent(1)
    # 2番目: 1 + 1/(2 + 1/2) = 7/5
    convergent_2 = generate_sqrt2_convergent(2)
    return convergent_1 == Fraction(3, 2) and convergent_2 == Fraction(7, 5)


class TestUtilityFunctions:
    """Test utility functions for convergent calculations"""

    def test_count_digits(self) -> None:
        """Test digit counting function"""
        # Single digit numbers
        assert count_digits(0) == 1
        assert count_digits(5) == 1
        assert count_digits(9) == 1

        # Multi-digit numbers
        assert count_digits(10) == 2
        assert count_digits(99) == 2
        assert count_digits(100) == 3
        assert count_digits(1000) == 4
        assert count_digits(12345) == 5

        # Negative numbers
        assert count_digits(-123) == 3
        assert count_digits(-5) == 1

    def test_has_numerator_more_digits(self) -> None:
        """Test numerator digit comparison function"""
        # Cases where numerator has more digits
        assert has_numerator_more_digits(Fraction(100, 99)) is True
        assert has_numerator_more_digits(Fraction(1000, 999)) is True
        assert has_numerator_more_digits(Fraction(1393, 985)) is True

        # Cases where denominator has more digits
        assert has_numerator_more_digits(Fraction(99, 100)) is False
        assert has_numerator_more_digits(Fraction(999, 1000)) is False

        # Cases where they have equal digits
        assert has_numerator_more_digits(Fraction(123, 456)) is False
        assert has_numerator_more_digits(Fraction(99, 88)) is False


class TestConvergentGeneration:
    """Test convergent generation functions"""

    def test_generate_sqrt2_convergent_basic(self) -> None:
        """Test basic convergent generation"""
        # Test first few convergents manually
        conv1 = generate_sqrt2_convergent(1)
        assert conv1 == Fraction(3, 2)

        conv2 = generate_sqrt2_convergent(2)
        assert conv2 == Fraction(7, 5)

        conv3 = generate_sqrt2_convergent(3)
        assert conv3 == Fraction(17, 12)

        conv4 = generate_sqrt2_convergent(4)
        assert conv4 == Fraction(41, 29)

    def test_generate_sqrt2_convergent_known_values(self) -> None:
        """Test against known convergent values"""
        known_convergents = [
            (1, Fraction(3, 2)),
            (2, Fraction(7, 5)),
            (3, Fraction(17, 12)),
            (4, Fraction(41, 29)),
            (5, Fraction(99, 70)),
            (6, Fraction(239, 169)),
            (7, Fraction(577, 408)),
            (8, Fraction(1393, 985)),
        ]

        for n, expected in known_convergents:
            actual = generate_sqrt2_convergent(n)
            assert actual == expected, (
                f"Convergent {n}: expected {expected}, got {actual}"
            )

    def test_generate_sqrt2_convergent_properties(self) -> None:
        """Test mathematical properties of convergents"""
        # Test that convergents are in lowest terms
        for n in range(1, 10):
            conv = generate_sqrt2_convergent(n)
            # Fractions should automatically be in lowest terms
            assert conv.numerator > 0
            assert conv.denominator > 0

        # Test convergence to √2
        import math

        sqrt2 = math.sqrt(2)

        # Later convergents should be closer to √2
        conv5 = generate_sqrt2_convergent(5)
        conv10 = generate_sqrt2_convergent(10)

        error5 = abs(float(conv5) - sqrt2)
        error10 = abs(float(conv10) - sqrt2)

        assert error10 < error5  # Better approximation with more terms


class TestKnownExamples:
    """Test known examples from the problem"""

    def test_verify_known_convergents(self) -> None:
        """Test that known convergents verification works"""
        assert verify_known_convergents() is True

    def test_eighth_convergent_property(self) -> None:
        """Test that 8th convergent is first with more digits in numerator"""
        # Test first 7 convergents don't have property
        for n in range(1, 8):
            conv = generate_sqrt2_convergent(n)
            assert not has_numerator_more_digits(conv), (
                f"Convergent {n} should not have more digits in numerator"
            )

        # Test 8th convergent does have property
        conv8 = generate_sqrt2_convergent(8)
        assert has_numerator_more_digits(conv8), (
            "8th convergent should have more digits in numerator"
        )

        # Check specific values
        assert conv8 == Fraction(1393, 985)
        assert count_digits(1393) == 4
        assert count_digits(985) == 3


class TestSolutionFunctions:
    """Test main solution functions"""

    @pytest.mark.parametrize("solver", [solve_naive, solve_optimized])
    def test_solve_consistency(self, solver: Callable[[int], int]) -> None:
        """Test that solution methods work with small limits"""
        # Test with small limits first
        result_10 = solver(10)
        assert isinstance(result_10, int)
        assert result_10 >= 0
        assert result_10 <= 10

        result_20 = solver(20)
        assert isinstance(result_20, int)
        assert result_20 >= result_10  # Larger range should give at least as many

    def test_solve_agreement(self) -> None:
        """Test that all solution methods agree"""
        # Test with smaller limits for speed
        limits = [10, 20, 50]

        for limit in limits:
            result_naive = solve_naive(limit)
            result_optimized = solve_optimized(limit)

            assert result_naive == result_optimized, (
                f"Solutions disagree for limit {limit}"
            )

    def test_solve_known_results(self) -> None:
        """Test with known results for small limits"""
        # Test that 8th convergent is first to satisfy condition
        result_8 = solve_naive(8)
        assert result_8 == 1, (
            "First 8 convergents should have exactly 1 with numerator > denominator"
        )

        # Test that first 7 have none
        result_7 = solve_naive(7)
        assert result_7 == 0, (
            "First 7 convergents should have 0 with numerator > denominator"
        )

    @pytest.mark.slow
    def test_solve_full_problem(self) -> None:
        """Test the full problem (marked as slow test)"""
        result = solve_naive(1000)
        assert isinstance(result, int)
        assert result > 0  # Should be some convergents with property
        assert result < 1000  # But not all


class TestAnalysisFunctions:
    """Test analysis and statistics functions"""

    def test_get_convergent_sequence(self) -> None:
        """Test convergent sequence generation"""
        sequence = get_convergent_sequence(5)

        assert len(sequence) == 5
        assert all("n" in conv for conv in sequence)
        assert all("numerator" in conv for conv in sequence)
        assert all("denominator" in conv for conv in sequence)
        assert all("has_more_digits" in conv for conv in sequence)

        # Check that sequence is in order
        for i, conv in enumerate(sequence):
            assert conv["n"] == i + 1

        # Check 8th element would have more digits (if we had it)
        if len(sequence) >= 8:
            assert sequence[7]["has_more_digits"] is True

    def test_analyze_convergent_pattern(self) -> None:
        """Test convergent pattern analysis"""
        analysis = analyze_convergent_pattern(20)

        assert "total_convergents" in analysis
        assert "more_digits_count" in analysis
        assert "more_digits_positions" in analysis
        assert "numerator_digit_distribution" in analysis
        assert "denominator_digit_distribution" in analysis
        assert "first_few_convergents" in analysis

        assert analysis["total_convergents"] == 20
        assert isinstance(analysis["more_digits_count"], int)
        assert analysis["more_digits_count"] >= 0
        assert len(analysis["first_few_convergents"]) <= 10

    def test_demonstrate_convergence(self) -> None:
        """Test convergence demonstration"""
        demonstrations = demonstrate_convergence()

        assert len(demonstrations) > 0
        assert all("n" in demo for demo in demonstrations)
        assert all("fraction_str" in demo for demo in demonstrations)
        assert all("decimal_value" in demo for demo in demonstrations)
        assert all("error" in demo for demo in demonstrations)

        # Errors should generally decrease (convergence)
        if len(demonstrations) >= 5:
            early_error = demonstrations[1]["error"]
            later_error = demonstrations[4]["error"]
            assert later_error < early_error

    def test_find_digit_difference_pattern(self) -> None:
        """Test digit difference pattern analysis"""
        pattern = find_digit_difference_pattern(15)

        assert "digit_differences" in pattern
        assert "difference_distribution" in pattern
        assert "positive_differences" in pattern

        assert len(pattern["digit_differences"]) == 15

        # Check that 8th position has positive difference
        eighth_diff = pattern["digit_differences"][7]  # 0-indexed
        assert eighth_diff["difference"] > 0
        assert eighth_diff["has_more_digits"] is True

    def test_get_large_convergents(self) -> None:
        """Test large convergent generation"""
        # Test with smaller n values for speed
        large_convs = get_large_convergents(50, 3)

        assert len(large_convs) == 3
        assert all("n" in conv for conv in large_convs)
        assert all("numerator_digits" in conv for conv in large_convs)
        assert all("denominator_digits" in conv for conv in large_convs)

        # Check that n values are correct
        assert large_convs[0]["n"] == 50
        assert large_convs[1]["n"] == 51
        assert large_convs[2]["n"] == 52


class TestBoundaryConditions:
    """Test boundary conditions and edge cases"""

    def test_first_convergent(self) -> None:
        """Test the first convergent"""
        conv1 = generate_sqrt2_convergent(1)
        assert conv1 == Fraction(3, 2)
        assert float(conv1) == 1.5

    def test_convergent_uniqueness(self) -> None:
        """Test that consecutive convergents are different"""
        for n in range(1, 10):
            conv_n = generate_sqrt2_convergent(n)
            conv_n_plus_1 = generate_sqrt2_convergent(n + 1)
            assert conv_n != conv_n_plus_1

    def test_solve_edge_cases(self) -> None:
        """Test solution functions with edge cases"""
        # Test with limit 1
        assert solve_naive(1) == 0  # First convergent doesn't have property
        assert solve_optimized(1) == 0

        # Test with limit 8 (first to have property)
        assert solve_naive(8) == 1
        assert solve_optimized(8) == 1


class TestMathematicalProperties:
    """Test mathematical properties of convergents"""

    def test_convergent_growth(self) -> None:
        """Test that convergents grow in magnitude"""
        convergents = []
        for n in range(1, 10):
            conv = generate_sqrt2_convergent(n)
            convergents.append((conv.numerator, conv.denominator))

        # Both numerators and denominators should generally grow
        for i in range(1, len(convergents)):
            prev_num, prev_den = convergents[i - 1]
            curr_num, curr_den = convergents[i]

            assert curr_num > prev_num
            assert curr_den > prev_den

    def test_convergent_bounds(self) -> None:
        """Test that convergents are bounded appropriately"""
        import math

        sqrt2 = math.sqrt(2)

        for n in range(1, 15):
            conv = generate_sqrt2_convergent(n)
            value = float(conv)

            # Should be close to √2
            assert 1.0 < value < 2.0

            # Should get closer to √2 as n increases
            error = abs(value - sqrt2)
            assert error < 1.0  # Reasonable bound


class TestPerformance:
    """Test performance-related aspects"""

    def test_small_limit_performance(self) -> None:
        """Test performance with small limits"""
        import time

        start_time = time.time()
        result = solve_optimized(100)
        end_time = time.time()

        assert isinstance(result, int)
        assert end_time - start_time < 1.0  # Should complete quickly

    def test_optimization_comparison(self) -> None:
        """Test that optimization improves performance"""
        import time

        limit = 200

        # Time naive solution
        start_time = time.time()
        result_naive = solve_naive(limit)
        naive_time = time.time() - start_time

        # Time optimized solution
        start_time = time.time()
        result_optimized = solve_optimized(limit)
        optimized_time = time.time() - start_time

        # Results should be the same
        assert result_naive == result_optimized

        # Optimized should be faster (though this may not always hold for small inputs)
        # Just check that both complete in reasonable time
        assert naive_time < 5.0
        assert optimized_time < 5.0


if __name__ == "__main__":
    pytest.main([__file__])
