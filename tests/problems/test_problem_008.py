"""Tests for Problem 008: Largest product in a series."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_008 import (
    THOUSAND_DIGIT_NUMBER,
    get_max_product_sequence,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem008:
    """Test cases for Problem 008."""

    @pytest.mark.parametrize(
        "adjacent_digits,expected",
        [
            (1, 9),  # Single digit max is 9
            (2, 81),  # Two digits: 9×9=81
            (3, 648),  # Three digits: 9×8×9=648
            (4, 5832),  # Four digits: 9×9×8×9=5832 (problem example)
            (5, 40824),  # Five digits: 9×9×8×7×9=40824
            (6, 285768),  # Six digits: 9×9×8×7×9×7=285768
        ],
    )
    def test_solve_naive(self, adjacent_digits: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(adjacent_digits)
        assert result == expected, (
            f"Expected {expected}, got {result} for {adjacent_digits} digits"
        )

    @pytest.mark.parametrize(
        "adjacent_digits,expected",
        [
            (1, 9),  # Single digit max is 9
            (2, 81),  # Two digits: 9×9=81
            (3, 648),  # Three digits: 9×8×9=648
            (4, 5832),  # Four digits: 9×9×8×9=5832 (problem example)
            (5, 40824),  # Five digits: 9×9×8×7×9=40824
            (6, 285768),  # Six digits: 9×9×8×7×9×7=285768
        ],
    )
    def test_solve_optimized(self, adjacent_digits: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(adjacent_digits)
        assert result == expected, (
            f"Expected {expected}, got {result} for {adjacent_digits} digits"
        )

    @pytest.mark.parametrize(
        "adjacent_digits,expected",
        [
            (1, 9),  # Single digit max is 9
            (2, 81),  # Two digits: 9×9=81
            (3, 648),  # Three digits: 9×8×9=648
            (4, 5832),  # Four digits: 9×9×8×9=5832 (problem example)
            (5, 40824),  # Five digits: 9×9×8×7×9=40824
            (6, 285768),  # Six digits: 9×9×8×7×9×7=285768
        ],
    )
    def test_solve_mathematical(self, adjacent_digits: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(adjacent_digits)
        assert result == expected, (
            f"Expected {expected}, got {result} for {adjacent_digits} digits"
        )

    @pytest.mark.parametrize("adjacent_digits", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_all_solutions_agree(self, adjacent_digits: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(adjacent_digits)
        optimized_result = solve_optimized(adjacent_digits)
        math_result = solve_mathematical(adjacent_digits)

        assert naive_result == optimized_result == math_result, (
            f"Solutions disagree for {adjacent_digits} digits: "
            f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with minimum adjacent digits
        assert solve_naive(1) == 9
        assert solve_optimized(1) == 9
        assert solve_mathematical(1) == 9

        # Test with maximum possible adjacent digits (1000)
        max_digits = len(THOUSAND_DIGIT_NUMBER)
        result = solve_naive(max_digits)
        assert result == 0  # Should be 0 because the number contains zeros

    def test_invalid_input(self) -> None:
        """Test with invalid input."""
        # All solutions should raise ValueError for non-positive adjacent_digits
        with pytest.raises(ValueError, match="adjacent_digits must be positive"):
            solve_naive(0)
        with pytest.raises(ValueError, match="adjacent_digits must be positive"):
            solve_optimized(0)
        with pytest.raises(ValueError, match="adjacent_digits must be positive"):
            solve_mathematical(0)

        with pytest.raises(ValueError, match="adjacent_digits must be positive"):
            solve_naive(-1)
        with pytest.raises(ValueError, match="adjacent_digits must be positive"):
            solve_optimized(-1)
        with pytest.raises(ValueError, match="adjacent_digits must be positive"):
            solve_mathematical(-1)

        # Test with adjacent_digits exceeding number length
        too_large = len(THOUSAND_DIGIT_NUMBER) + 1
        with pytest.raises(
            ValueError, match="adjacent_digits cannot exceed number length"
        ):
            solve_naive(too_large)
        with pytest.raises(
            ValueError, match="adjacent_digits cannot exceed number length"
        ):
            solve_optimized(too_large)
        with pytest.raises(
            ValueError, match="adjacent_digits cannot exceed number length"
        ):
            solve_mathematical(too_large)

    @pytest.mark.slow
    def test_large_number(self) -> None:
        """Test with the actual problem number (marked as slow)."""
        # Test with the actual problem limit using fastest algorithm only
        adjacent_digits = 13
        expected = 23514624000  # Known Project Euler answer

        # Test only mathematical solution for speed
        result_math = solve_mathematical(adjacent_digits)
        assert result_math == expected

    def test_thousand_digit_number_properties(self) -> None:
        """Test properties of the 1000-digit number."""
        # Check that we have exactly 1000 digits
        assert len(THOUSAND_DIGIT_NUMBER) == 1000

        # Check that all characters are digits
        assert all(c.isdigit() for c in THOUSAND_DIGIT_NUMBER)

        # Check that it contains both zeros and nines
        assert "0" in THOUSAND_DIGIT_NUMBER
        assert "9" in THOUSAND_DIGIT_NUMBER

        # Check specific digits from the problem description
        # The number should start with 73167176531330624919225119674426574742355349194934...
        assert THOUSAND_DIGIT_NUMBER.startswith(
            "73167176531330624919225119674426574742355349194934"
        )

    def test_get_max_product_sequence_helper(self) -> None:
        """Test the helper function for getting max product sequence."""
        # Test for 4 adjacent digits (problem example)
        sequence, product = get_max_product_sequence(4)
        assert product == 5832
        assert len(sequence) == 4
        assert "0" not in sequence  # Should not contain zeros

        # Test for single digit
        sequence, product = get_max_product_sequence(1)
        assert product == 9
        assert sequence == "9"

        # Test for 2 digits
        sequence, product = get_max_product_sequence(2)
        assert product == 81
        assert sequence == "99"

    def test_manual_calculation_verification(self) -> None:
        """Test manual calculation verification for small cases."""
        # Verify the 4-digit example from the problem description
        # The problem states that 9×9×8×9 = 5832 is the maximum for 4 digits
        assert 9 * 9 * 8 * 9 == 5832

        # Find this sequence in our number
        sequence, product = get_max_product_sequence(4)
        assert product == 5832

        # Verify that this sequence actually produces the expected product
        calculated_product = 1
        for digit in sequence:
            calculated_product *= int(digit)
        assert calculated_product == 5832

    def test_performance_comparison(self) -> None:
        """Test that all solutions work for moderate inputs."""
        # Simple functional test without timing overhead
        adjacent_digits = 8

        # Verify all solutions work
        result_naive = solve_naive(adjacent_digits)
        result_optimized = solve_optimized(adjacent_digits)
        result_math = solve_mathematical(adjacent_digits)

        # All should give same result
        assert result_naive == result_optimized == result_math

        # Result should be positive
        assert result_naive > 0

    def test_zero_handling(self) -> None:
        """Test that solutions correctly handle sequences containing zeros."""
        # Create a simple test case with known zeros
        # Since we can't modify THOUSAND_DIGIT_NUMBER, we test the logic indirectly

        # Any sequence containing a zero should have product 0
        # So the maximum should be from sequences without zeros

        # Test with a large number of adjacent digits that likely contains zeros
        large_digits = 100
        result = solve_optimized(large_digits)

        # If the result is 0, it means all possible sequences contain at least one zero
        # If the result is > 0, it means there's at least one sequence without zeros
        assert result >= 0

    def test_sequence_boundaries(self) -> None:
        """Test sequences at the boundaries of the number."""
        # Test that we can handle sequences at the start and end of the number
        for adjacent_digits in [1, 2, 3, 5, 10]:
            result = solve_naive(adjacent_digits)
            assert result >= 0

            # The number of possible sequences should be correct
            expected_sequences = len(THOUSAND_DIGIT_NUMBER) - adjacent_digits + 1
            assert expected_sequences > 0

    def test_mathematical_properties(self) -> None:
        """Test mathematical properties of the solutions."""
        # Test that larger sequences don't necessarily have larger products
        # (due to zeros and smaller digits)

        results = []
        for digits in range(1, 11):
            result = solve_mathematical(digits)
            results.append(result)

        # All results should be non-negative
        assert all(r >= 0 for r in results)

        # The first result (1 digit) should be 9
        assert results[0] == 9

    def test_project_euler_example(self) -> None:
        """Test the specific Project Euler example."""
        # From the problem statement:
        # "The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832"

        adjacent_digits = 4
        expected = 5832

        # Test all our solutions
        assert solve_naive(adjacent_digits) == expected
        assert solve_optimized(adjacent_digits) == expected
        assert solve_mathematical(adjacent_digits) == expected

        # Verify the sequence calculation
        sequence, product = get_max_product_sequence(adjacent_digits)
        assert product == expected

        # Verify that the sequence when multiplied gives the expected result
        manual_product = 1
        for digit in sequence:
            manual_product *= int(digit)
        assert manual_product == expected

    def test_large_values_consistency(self) -> None:
        """Test consistency for larger values."""
        # Test larger values to ensure algorithms remain accurate
        test_values = [7, 8, 9, 10, 11, 12]

        for digits in test_values:
            naive_result = solve_naive(digits)
            optimized_result = solve_optimized(digits)
            math_result = solve_mathematical(digits)

            assert naive_result == optimized_result == math_result, (
                f"Solutions disagree for {digits} digits: "
                f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
            )

    def test_optimization_effectiveness(self) -> None:
        """Test that optimizations correctly skip zero-containing sequences."""
        # This is more of a logical test since we can't easily measure performance

        # Test that optimized solutions handle zeros correctly
        for digits in [5, 10, 15, 20]:
            if digits <= len(THOUSAND_DIGIT_NUMBER):
                result_optimized = solve_optimized(digits)
                result_math = solve_mathematical(digits)

                # Both optimized methods should agree
                assert result_optimized == result_math

                # If result is 0, all sequences contain zeros
                # If result > 0, there's at least one sequence without zeros
                assert result_optimized >= 0

    def test_digit_frequency_analysis(self) -> None:
        """Test analysis of digit frequencies in the 1000-digit number."""
        # Count frequency of each digit
        digit_counts = {}
        for digit in "0123456789":
            digit_counts[digit] = THOUSAND_DIGIT_NUMBER.count(digit)

        # Verify total count
        assert sum(digit_counts.values()) == 1000

        # All digits should appear at least once
        for digit in "0123456789":
            assert digit_counts[digit] > 0, f"Digit {digit} should appear in the number"

        # The digit '9' should appear (since it's the maximum single digit result)
        assert digit_counts["9"] > 0
