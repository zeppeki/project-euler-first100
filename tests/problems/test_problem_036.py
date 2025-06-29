#!/usr/bin/env python3
"""Tests for Problem 036"""

import pytest

from problems.problem_036 import is_palindrome, solve_naive, solve_optimized


class TestProblem036:
    """Test cases for Problem 036"""

    def test_is_palindrome(self) -> None:
        """Test palindrome check function"""
        assert is_palindrome("1") is True
        assert is_palindrome("121") is True
        assert is_palindrome("1221") is True
        assert is_palindrome("12321") is True
        assert is_palindrome("123") is False
        assert is_palindrome("1234") is False

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (
                10,
                25,
            ),  # 1, 3, 5, 7, 9 (single digits that are palindromes in both bases)
            (100, 157),  # Add 33, 99
            (1000, 1772),  # Add 313, 585, 717, 999
        ],
    )
    def test_solve_naive(self, limit: int, expected: int) -> None:
        """Test naive solution with various limits"""
        result = solve_naive(limit)
        assert result == expected

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (10, 25),  # 1, 3, 5, 7, 9
            (100, 157),  # Add 33, 99
            (1000, 1772),  # Add 313, 585, 717, 999
        ],
    )
    def test_solve_optimized(self, limit: int, expected: int) -> None:
        """Test optimized solution with various limits"""
        result = solve_optimized(limit)
        assert result == expected

    @pytest.mark.parametrize("limit", [10, 100, 1000, 10000])
    def test_solutions_agree(self, limit: int) -> None:
        """Test that all solutions agree"""
        naive_result = solve_naive(limit)
        optimized_result = solve_optimized(limit)
        assert naive_result == optimized_result

    def test_known_double_base_palindromes(self) -> None:
        """Test known double-base palindromes"""
        # Test individual known cases
        known_cases = [
            (1, "1", "1"),  # 1 in decimal = 1 in binary
            (3, "3", "11"),  # 3 in decimal = 11 in binary
            (5, "5", "101"),  # 5 in decimal = 101 in binary
            (7, "7", "111"),  # 7 in decimal = 111 in binary
            (9, "9", "1001"),  # 9 in decimal = 1001 in binary
            (33, "33", "100001"),  # 33 in decimal = 100001 in binary
            (99, "99", "1100011"),  # 99 in decimal = 1100011 in binary
            (313, "313", "100111001"),  # 313 in decimal = 100111001 in binary
            (585, "585", "1001001001"),  # 585 in decimal = 1001001001 in binary
        ]

        for num, dec_str, bin_str in known_cases:
            assert str(num) == dec_str
            assert bin(num)[2:] == bin_str
            assert is_palindrome(dec_str)
            assert is_palindrome(bin_str)

    @pytest.mark.slow
    def test_full_problem(self) -> None:
        """Test the full problem with limit 1000000"""
        naive_result = solve_naive(1000000)
        optimized_result = solve_optimized(1000000)
        assert naive_result == optimized_result
        assert naive_result > 0
