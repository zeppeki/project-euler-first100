#!/usr/bin/env python3
"""
Test for Problem 093: Arithmetic expressions
"""

import pytest

from problems.problem_093 import (
    evaluate_expression,
    find_consecutive_length,
    generate_all_expressions,
    get_expression_details,
    solve_naive,
    solve_optimized,
)


class TestUtilityFunctions:
    """Test utility functions for arithmetic expressions."""

    def test_evaluate_expression(self) -> None:
        """Test arithmetic expression evaluation."""
        # Addition
        assert evaluate_expression(2, 3, "+") == 5
        assert evaluate_expression(1.5, 2.5, "+") == 4.0

        # Subtraction
        assert evaluate_expression(5, 3, "-") == 2
        assert evaluate_expression(1, 4, "-") == -3

        # Multiplication
        assert evaluate_expression(3, 4, "*") == 12
        assert evaluate_expression(2.5, 2, "*") == 5.0

        # Division
        assert evaluate_expression(6, 2, "/") == 3.0
        assert evaluate_expression(7, 4, "/") == 1.75

        # Division by zero
        assert evaluate_expression(5, 0, "/") is None

        # Invalid operation
        assert evaluate_expression(2, 3, "%") is None

    def test_find_consecutive_length(self) -> None:
        """Test consecutive length calculation."""
        # Perfect consecutive sequence from 1
        assert find_consecutive_length({1, 2, 3, 4, 5}) == 5

        # Consecutive sequence with gaps later
        assert find_consecutive_length({1, 2, 3, 5, 6, 7}) == 3

        # Empty set
        assert find_consecutive_length(set()) == 0

        # No consecutive sequence from 1
        assert find_consecutive_length({2, 3, 4, 5}) == 0

        # Single element starting from 1
        assert find_consecutive_length({1}) == 1

        # Large consecutive sequence
        numbers = set(range(1, 101))
        assert find_consecutive_length(numbers) == 100

    def test_generate_all_expressions(self) -> None:
        """Test expression generation for small cases."""
        # Test with invalid input
        with pytest.raises(ValueError):
            generate_all_expressions((1, 2))

        with pytest.raises(ValueError):
            generate_all_expressions((1, 2, 3))

        # Test with known case {1, 2, 3, 4}
        result = generate_all_expressions((1, 2, 3, 4))
        # Should be able to generate 1 to 28 consecutively
        consecutive_length = find_consecutive_length(result)
        assert consecutive_length == 28

        # Verify specific examples from problem statement
        assert 8 in result  # (4 * (1 + 3)) / 2
        assert 14 in result  # 4 * (3 + 1 / 2)
        assert 19 in result  # 4 * (2 + 3) - 1
        assert 36 in result  # 3 * 4 * (2 + 1)

    def test_get_expression_details(self) -> None:
        """Test expression details function."""
        digits = (1, 2, 3, 4)
        details = get_expression_details(digits)

        assert details["digits"] == digits
        assert isinstance(details["possible_numbers"], set)
        assert isinstance(details["consecutive_length"], int)
        assert details["consecutive_length"] == 28
        assert len(details["possible_numbers"]) > 28


class TestSolutionMethods:
    """Test solution methods with various inputs."""

    def test_solution_consistency(self) -> None:
        """Test that all solution methods give the same results."""
        naive_result = solve_naive()
        optimized_result = solve_optimized()

        # All methods should return the same result
        assert naive_result == optimized_result

        # Result should be a 4-digit string
        assert len(naive_result) == 4
        assert naive_result.isdigit()

        # Digits should be in ascending order
        digits = [int(d) for d in naive_result]
        assert digits == sorted(digits)

        # All digits should be different
        assert len(set(digits)) == 4

    def test_known_example(self) -> None:
        """Test with the known example from problem statement."""
        # {1, 2, 3, 4} should produce consecutive sequence 1-28
        details = get_expression_details((1, 2, 3, 4))
        assert details["consecutive_length"] == 28

        # Verify this is a valid combination
        result = solve_optimized()

        # The result should be a valid digit combination
        result_digits = tuple(int(d) for d in result)
        result_details = get_expression_details(result_digits)

        # The result should have at least as good performance as {1,2,3,4}
        assert isinstance(result_details["consecutive_length"], int)
        assert result_details["consecutive_length"] >= 28

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with small digit combinations
        small_cases = [
            (1, 2, 3, 4),
            (1, 2, 3, 5),
            (2, 3, 4, 5),
        ]

        for digits in small_cases:
            details = get_expression_details(digits)
            assert isinstance(details["consecutive_length"], int)
            assert details["consecutive_length"] >= 0
            assert isinstance(details["possible_numbers"], set)
            assert len(details["possible_numbers"]) > 0

    def test_result_format(self) -> None:
        """Test that results are properly formatted."""
        result = solve_optimized()

        # Should be exactly 4 digits
        assert len(result) == 4

        # Should be all digits
        assert result.isdigit()

        # Should be in ascending order
        digits = [int(d) for d in result]
        assert digits == sorted(digits)

        # Should not contain 0 (since we exclude it in optimized solution)
        assert "0" not in result

        # All digits should be unique
        assert len(set(result)) == 4

    def test_comprehensive_calculation(self) -> None:
        """Test comprehensive calculation for validation."""
        # Test the actual result
        result = solve_optimized()
        result_digits = tuple(int(d) for d in result)

        # Generate all expressions for the result
        possible_numbers = generate_all_expressions(result_digits)
        consecutive_length = find_consecutive_length(possible_numbers)

        # Verify the consecutive length is reasonable
        assert consecutive_length >= 28  # Should be at least as good as {1,2,3,4}

        # Verify all numbers from 1 to consecutive_length are present
        for i in range(1, consecutive_length + 1):
            assert i in possible_numbers

    def test_expression_generation_properties(self) -> None:
        """Test properties of expression generation."""
        # Test with {1, 2, 3, 4}
        result = generate_all_expressions((1, 2, 3, 4))

        # Should contain only positive integers
        assert all(isinstance(x, int) and x > 0 for x in result)

        # Should contain a significant number of results
        assert len(result) > 25  # Should generate many different numbers

        # Should be able to generate consecutive numbers starting from 1
        consecutive_count = 0
        for i in range(1, 100):
            if i in result:
                consecutive_count += 1
            else:
                break

        assert consecutive_count == 28  # Known result for {1,2,3,4}


class TestProblem093:
    """Test the main problem solution."""

    def test_final_result_validation(self) -> None:
        """Test that the final result is valid and optimal."""
        result = solve_optimized()

        # Convert to digits and verify
        digits = tuple(int(d) for d in result)
        details = get_expression_details(digits)

        # Should produce a good consecutive sequence
        assert isinstance(details["consecutive_length"], int)
        assert details["consecutive_length"] >= 28

        # Test a few other combinations to ensure this is indeed optimal
        test_combinations = [
            (1, 2, 3, 4),
            (1, 2, 5, 8),
            (2, 3, 4, 6),
            (1, 3, 5, 7),
        ]

        for test_digits in test_combinations:
            test_details = get_expression_details(test_digits)
            # The result should be at least as good as these alternatives
            assert isinstance(test_details["consecutive_length"], int)
            assert isinstance(details["consecutive_length"], int)
            assert details["consecutive_length"] >= test_details["consecutive_length"]

    def test_algorithm_correctness(self) -> None:
        """Test algorithm correctness with known cases."""
        # Test that we correctly identify {1,2,3,4} produces 1-28
        details = get_expression_details((1, 2, 3, 4))
        assert details["consecutive_length"] == 28

        # Test some specific expressions work
        expressions = generate_all_expressions((1, 2, 3, 4))

        # Known examples from problem statement should be present
        assert 8 in expressions
        assert 14 in expressions
        assert 19 in expressions
        assert 36 in expressions

        # Should have consecutive integers 1-28
        for i in range(1, 29):
            assert i in expressions

    @pytest.mark.slow
    def test_performance_validation(self) -> None:
        """Test that the solution completes in reasonable time."""
        # This test ensures the algorithm runs efficiently
        result = solve_optimized()

        # Should complete and return a valid result
        assert len(result) == 4
        assert result.isdigit()

        # Verify the result produces a good consecutive sequence
        digits = tuple(int(d) for d in result)
        details = get_expression_details(digits)
        assert isinstance(details["consecutive_length"], int)
        assert details["consecutive_length"] >= 28
