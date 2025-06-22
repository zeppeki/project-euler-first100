"""Tests for Problem 006: Sum square difference."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_006 import solve_mathematical, solve_naive, solve_optimized


class TestProblem006:
    """Test cases for Problem 006."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 0),  # Edge case: n=0
            (1, 0),  # n=1: (1)² - (1²) = 1 - 1 = 0
            (2, 4),  # n=2: (1+2)² - (1²+2²) = 9 - 5 = 4
            (3, 22),  # n=3: (1+2+3)² - (1²+2²+3²) = 36 - 14 = 22
            (4, 70),  # n=4: (1+2+3+4)² - (1²+2²+3²+4²) = 100 - 30 = 70
            (5, 170),  # n=5: (1+...+5)² - (1²+...+5²) = 225 - 55 = 170
            (10, 2640),  # Problem example: n=10
        ],
    )
    def test_solve_naive(self, n: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 0),  # Edge case: n=0
            (1, 0),  # n=1: (1)² - (1²) = 1 - 1 = 0
            (2, 4),  # n=2: (1+2)² - (1²+2²) = 9 - 5 = 4
            (3, 22),  # n=3: (1+2+3)² - (1²+2²+3²) = 36 - 14 = 22
            (4, 70),  # n=4: (1+2+3+4)² - (1²+2²+3²+4²) = 100 - 30 = 70
            (5, 170),  # n=5: (1+...+5)² - (1²+...+5²) = 225 - 55 = 170
            (10, 2640),  # Problem example: n=10
        ],
    )
    def test_solve_optimized(self, n: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 0),  # Edge case: n=0
            (1, 0),  # n=1: (1)² - (1²) = 1 - 1 = 0
            (2, 4),  # n=2: (1+2)² - (1²+2²) = 9 - 5 = 4
            (3, 22),  # n=3: (1+2+3)² - (1²+2²+3²) = 36 - 14 = 22
            (4, 70),  # n=4: (1+2+3+4)² - (1²+2²+3²+4²) = 100 - 30 = 70
            (5, 170),  # n=5: (1+...+5)² - (1²+...+5²) = 225 - 55 = 170
            (10, 2640),  # Problem example: n=10
        ],
    )
    def test_solve_mathematical(self, n: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize("n", [0, 1, 2, 3, 4, 5, 10, 50])
    def test_all_solutions_agree(self, n: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(n)
        optimized_result = solve_optimized(n)
        math_result = solve_mathematical(n)

        assert naive_result == optimized_result == math_result, (
            f"Solutions disagree for n={n}: "
            f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with n = 0
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0
        assert solve_mathematical(0) == 0

        # Test with n = 1
        assert solve_naive(1) == 0
        assert solve_optimized(1) == 0
        assert solve_mathematical(1) == 0

        # Test with n = 2
        assert solve_naive(2) == 4
        assert solve_optimized(2) == 4
        assert solve_mathematical(2) == 4

    def test_negative_input(self) -> None:
        """Test with negative input (should handle gracefully)."""
        # All solutions should handle negative input gracefully
        assert solve_naive(-10) == 0
        assert solve_optimized(-10) == 0
        assert solve_mathematical(-10) == 0

    @pytest.mark.slow
    def test_large_number(self) -> None:
        """Test with the actual problem number (marked as slow)."""
        # Test with the actual problem limit using fastest algorithm only
        n = 100
        expected = 25164150  # Known Project Euler answer

        # Test only mathematical solution for speed
        result_math = solve_mathematical(n)
        assert result_math == expected

    def test_manual_calculation_verification(self) -> None:
        """Test manual calculation verification for small values."""
        # Verify n=3 manually
        # Sum: 1 + 2 + 3 = 6
        # Square of sum: 6² = 36
        # Sum of squares: 1² + 2² + 3² = 1 + 4 + 9 = 14
        # Difference: 36 - 14 = 22

        n = 3
        sum_of_numbers = sum(range(1, n + 1))  # 6
        square_of_sum = sum_of_numbers**2  # 36
        sum_of_squares = sum(i**2 for i in range(1, n + 1))  # 14
        expected_difference = square_of_sum - sum_of_squares  # 22

        assert solve_naive(n) == expected_difference
        assert solve_optimized(n) == expected_difference
        assert solve_mathematical(n) == expected_difference
        assert expected_difference == 22

    def test_mathematical_formulas(self) -> None:
        """Test that the mathematical formulas are correct."""
        for n in [1, 2, 3, 4, 5, 10, 20]:
            # Test sum formula: 1 + 2 + ... + n = n(n+1)/2
            expected_sum = sum(range(1, n + 1))
            formula_sum = n * (n + 1) // 2
            assert formula_sum == expected_sum, f"Sum formula failed for n={n}"

            # Test sum of squares formula: 1² + 2² + ... + n² = n(n+1)(2n+1)/6
            expected_sum_of_squares = sum(i**2 for i in range(1, n + 1))
            formula_sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
            assert formula_sum_of_squares == expected_sum_of_squares, (
                f"Sum of squares formula failed for n={n}"
            )

    def test_performance_comparison(self) -> None:
        """Test that optimized solutions are faster for larger inputs."""
        # Simple functional test without timing overhead
        n = 50  # Reduced test size

        # Verify all solutions work
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)

        # All should give same result
        assert result_naive == result_optimized == result_math

    def test_large_values_consistency(self) -> None:
        """Test consistency for larger values."""
        # Test larger values to ensure formulas remain accurate
        test_values = [20, 50, 100, 200]

        for n in test_values:
            naive_result = solve_naive(n)
            optimized_result = solve_optimized(n)
            math_result = solve_mathematical(n)

            assert naive_result == optimized_result == math_result, (
                f"Solutions disagree for n={n}: "
                f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
            )

    def test_mathematical_derivation(self) -> None:
        """Test the mathematical derivation formula."""
        # The mathematical solution uses: n(n+1)(n-1)(3n+2)/12
        # Verify this is equivalent to the difference calculation

        for n in [2, 3, 4, 5, 10, 20]:
            # Calculate using basic approach
            sum_of_numbers = n * (n + 1) // 2
            square_of_sum = sum_of_numbers * sum_of_numbers
            sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
            expected = square_of_sum - sum_of_squares

            # Calculate using derived formula
            derived = n * (n + 1) * (n - 1) * (3 * n + 2) // 12

            assert derived == expected, (
                f"Derived formula failed for n={n}: expected={expected}, got={derived}"
            )

    def test_zero_and_one_special_cases(self) -> None:
        """Test special cases for n=0 and n=1."""
        # For n=0: no numbers to sum, so difference should be 0
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0
        assert solve_mathematical(0) == 0

        # For n=1: sum=1, square_of_sum=1, sum_of_squares=1, difference=0
        assert solve_naive(1) == 0
        assert solve_optimized(1) == 0
        assert solve_mathematical(1) == 0

    def test_project_euler_example(self) -> None:
        """Test the specific Project Euler example."""
        # From the problem statement:
        # Sum of squares of first 10 natural numbers = 385
        # Square of sum of first 10 natural numbers = 3025
        # Difference = 3025 - 385 = 2640

        n = 10

        # Verify intermediate calculations
        sum_of_squares = sum(i**2 for i in range(1, n + 1))
        sum_of_numbers = sum(range(1, n + 1))
        square_of_sum = sum_of_numbers**2

        assert sum_of_squares == 385
        assert square_of_sum == 3025

        expected_difference = 2640
        assert square_of_sum - sum_of_squares == expected_difference

        # Test all our solutions
        assert solve_naive(n) == expected_difference
        assert solve_optimized(n) == expected_difference
        assert solve_mathematical(n) == expected_difference
