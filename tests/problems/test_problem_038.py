#!/usr/bin/env python3
"""Tests for Problem 038"""

from problems.problem_038 import (
    concatenated_product,
    is_pandigital,
    solve_naive,
    solve_optimized,
)


class TestProblem038:
    """Test cases for Problem 038"""

    def test_is_pandigital(self) -> None:
        """Test pandigital number detection"""
        assert is_pandigital("123456789") is True
        assert is_pandigital("192384576") is True
        assert is_pandigital("918273645") is True
        assert is_pandigital("123456788") is False  # missing 9
        assert is_pandigital("123456780") is False  # has 0
        assert is_pandigital("12345678") is False  # too short
        assert is_pandigital("1234567890") is False  # too long

    def test_concatenated_product(self) -> None:
        """Test concatenated product generation"""
        assert concatenated_product(192, 3) == "192384576"
        assert concatenated_product(9, 5) == "918273645"
        assert concatenated_product(1, 9) == "123456789"
        assert concatenated_product(12, 4) == "12243648"

    def test_known_examples(self) -> None:
        """Test with known examples from problem description"""
        # Example 1: 192 × (1,2,3) = 192384576
        result = concatenated_product(192, 3)
        assert result == "192384576"
        assert is_pandigital(result) is True

        # Example 2: 9 × (1,2,3,4,5) = 918273645
        result = concatenated_product(9, 5)
        assert result == "918273645"
        assert is_pandigital(result) is True

    def test_solve_naive(self) -> None:
        """Test naive solution returns correct result"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0
        assert len(str(result)) == 9
        assert is_pandigital(str(result)) is True

    def test_solve_optimized(self) -> None:
        """Test optimized solution returns correct result"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0
        assert len(str(result)) == 9
        assert is_pandigital(str(result)) is True

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        assert naive_result == optimized_result

    def test_result_larger_than_examples(self) -> None:
        """Test that result is larger than known examples"""
        result = solve_naive()
        assert result > 918273645  # Larger than 9×(1,2,3,4,5)
        assert result > 192384576  # Larger than 192×(1,2,3)
