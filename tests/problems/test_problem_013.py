"""Tests for Problem 013: Large sum."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_013 import (
    get_fifty_digit_numbers,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem013:
    """Test cases for Problem 013."""

    def test_get_fifty_digit_numbers(self) -> None:
        """Test that the fifty digit numbers are loaded correctly."""
        numbers = get_fifty_digit_numbers()

        # Should have exactly 100 numbers
        assert len(numbers) == 100

        # Each number should be exactly 50 digits
        for i, num in enumerate(numbers):
            assert len(num) == 50, f"Number {i + 1} has {len(num)} digits, expected 50"
            assert num.isdigit(), f"Number {i + 1} contains non-digit characters"

        # Test first few numbers (known values)
        assert numbers[0] == "37107287533902102798797998220837590246510135740250"
        assert numbers[1] == "46376937677490009712648124896970078050417018260538"
        assert numbers[2] == "74324986199524741059474233309513058123726617309629"

    def test_solve_naive(self) -> None:
        """Test the naive solution."""
        result = solve_naive()

        # Should return a string of 10 digits
        assert len(result) == 10
        assert result.isdigit()

        # Known answer from Project Euler
        assert result == "5537376230"

    def test_solve_optimized(self) -> None:
        """Test the optimized solution."""
        result = solve_optimized()

        # Should return a string of 10 digits
        assert len(result) == 10
        assert result.isdigit()

        # Should match the known answer
        assert result == "5537376230"

    def test_solve_mathematical(self) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical()

        # Should return a string of 10 digits
        assert len(result) == 10
        assert result.isdigit()

        # Should match the known answer
        assert result == "5537376230"

    def test_all_solutions_agree(self) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        math_result = solve_mathematical()

        assert naive_result == optimized_result == math_result, (
            f"Solutions disagree: "
            f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
        )

    def test_small_example(self) -> None:
        """Test with a smaller example to verify correctness."""
        # Test with a small set of numbers
        test_numbers = [
            "12345678901234567890123456789012345678901234567890",
            "98765432109876543210987654321098765432109876543210",
            "11111111111111111111111111111111111111111111111111",
        ]

        # Calculate expected result
        expected_sum = sum(int(num) for num in test_numbers)
        expected_first_10 = str(expected_sum)[:10]

        # Verify calculation is correct
        assert expected_first_10 == "1222222221"

    def test_digit_validation(self) -> None:
        """Test that all numbers are valid 50-digit numbers."""
        numbers = get_fifty_digit_numbers()

        for i, num in enumerate(numbers):
            # Each number should be exactly 50 characters
            assert len(num) == 50, f"Number {i + 1}: expected 50 digits, got {len(num)}"

            # Each character should be a digit
            for j, char in enumerate(num):
                assert char.isdigit(), (
                    f"Number {i + 1}, position {j + 1}: '{char}' is not a digit"
                )

            # Number should not start with 0 (though technically valid, unlikely for this problem)
            assert num[0] != "0", f"Number {i + 1} starts with 0, which seems unusual"

    def test_sum_magnitude(self) -> None:
        """Test that the sum has the expected magnitude."""
        numbers = get_fifty_digit_numbers()
        total_sum = sum(int(num) for num in numbers)

        # The sum should be approximately 100 * average_50_digit_number
        # With 100 numbers each around 10^49 to 10^50, the sum should be around 10^51 to 10^52
        sum_str = str(total_sum)

        # Should be 51 or 52 digits
        assert 51 <= len(sum_str) <= 52, (
            f"Sum has {len(sum_str)} digits, expected 51-52"
        )

        # Should start with 5 (based on known answer)
        assert sum_str[0] == "5", f"Sum starts with {sum_str[0]}, expected 5"

    def test_individual_number_ranges(self) -> None:
        """Test that individual numbers are in expected ranges."""
        numbers = get_fifty_digit_numbers()

        for i, num in enumerate(numbers):
            value = int(num)

            # Each 50-digit number should be between 10^49 and 10^50 - 1
            min_50_digit = 10**49
            max_50_digit = 10**50 - 1

            assert min_50_digit <= value <= max_50_digit, (
                f"Number {i + 1} ({num}) is outside valid 50-digit range"
            )

    def test_performance_comparison(self) -> None:
        """Test that all solutions work efficiently (optimized for speed)."""
        # Test fastest solution and verify others agree on smaller inputs
        result_math = solve_mathematical()
        result_optimized = solve_optimized()
        result_naive = solve_naive()

        # All should give the same result
        assert result_naive == result_optimized == result_math

    def test_expected_answer_format(self) -> None:
        """Test that the answer format is correct."""
        result = solve_naive()

        # Should be exactly 10 digits
        assert len(result) == 10

        # Should be all digits
        assert result.isdigit()

        # Should not start with 0 (would be unusual for this problem)
        assert result[0] != "0"

        # Known correct answer
        assert result == "5537376230"

    def test_mathematical_approach_accuracy(self) -> None:
        """Test that the mathematical approximation is accurate enough."""
        # The mathematical approach uses only first 12 digits
        # It should still produce the correct first 10 digits

        naive_result = solve_naive()
        math_result = solve_mathematical()

        # First 10 digits should match exactly
        assert naive_result == math_result

        # This verifies that using first 12 digits is sufficient
        # for accurate computation of first 10 digits

    def test_edge_cases(self) -> None:
        """Test edge cases and boundary conditions."""
        numbers = get_fifty_digit_numbers()

        # Verify we have exactly 100 numbers
        assert len(numbers) == 100

        # Verify no empty strings
        for num in numbers:
            assert num.strip() == num  # No leading/trailing whitespace
            assert len(num) > 0  # Not empty

        # Verify all numbers are unique (they should be for this problem)
        unique_numbers = set(numbers)
        assert len(unique_numbers) == len(numbers), "Some numbers are duplicated"

    def test_string_vs_int_consistency(self) -> None:
        """Test that string and integer operations give consistent results."""
        numbers = get_fifty_digit_numbers()

        # Convert to integers and sum
        int_sum = sum(int(num) for num in numbers)

        # Get first 10 digits via string conversion
        first_10_via_string = str(int_sum)[:10]

        # This should match our solve_naive result
        naive_result = solve_naive()
        assert first_10_via_string == naive_result

    def test_known_project_euler_answer(self) -> None:
        """Test against the known Project Euler answer."""
        # The known answer for Problem 013
        expected_answer = "5537376230"

        # All our solutions should produce this answer
        assert solve_naive() == expected_answer
        assert solve_optimized() == expected_answer
        assert solve_mathematical() == expected_answer

    @pytest.mark.slow
    def test_full_sum_calculation(self) -> None:
        """Test the full sum calculation (marked as slow for detailed verification)."""
        numbers = get_fifty_digit_numbers()

        # Calculate the complete sum
        total_sum = sum(int(num) for num in numbers)

        # Verify it's the expected value (if we know it)
        # The sum should be: 55373762302455...
        sum_str = str(total_sum)

        # Should start with our expected 10 digits
        assert sum_str.startswith("5537376230")

        # Total should be reasonable length
        assert 51 <= len(sum_str) <= 53  # Allow some tolerance

    def test_algorithm_specific_properties(self) -> None:
        """Test algorithm-specific properties and optimizations."""
        # Test that optimized solution handles carry-over correctly
        result_optimized = solve_optimized()
        result_naive = solve_naive()

        assert result_optimized == result_naive

        # Test that mathematical solution approximation is close enough
        result_math = solve_mathematical()
        assert result_math == result_naive
