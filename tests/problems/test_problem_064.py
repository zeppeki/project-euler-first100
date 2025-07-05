#!/usr/bin/env python3
"""Tests for Problem 064"""

import pytest

from problems.problem_064 import (
    get_continued_fraction_period,
    is_perfect_square,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem064:
    """Test cases for Problem 064"""

    def test_is_perfect_square(self) -> None:
        """Test perfect square detection"""
        # Test perfect squares
        assert is_perfect_square(1)
        assert is_perfect_square(4)
        assert is_perfect_square(9)
        assert is_perfect_square(16)
        assert is_perfect_square(25)
        assert is_perfect_square(100)

        # Test non-perfect squares
        assert not is_perfect_square(2)
        assert not is_perfect_square(3)
        assert not is_perfect_square(5)
        assert not is_perfect_square(6)
        assert not is_perfect_square(7)
        assert not is_perfect_square(8)
        assert not is_perfect_square(10)
        assert not is_perfect_square(23)

    def test_get_continued_fraction_period(self) -> None:
        """Test continued fraction period calculation"""
        # Perfect squares should have period 0
        assert get_continued_fraction_period(1) == 0
        assert get_continued_fraction_period(4) == 0
        assert get_continued_fraction_period(9) == 0
        assert get_continued_fraction_period(16) == 0

        # Known continued fraction periods
        # √2 = [1;(2)] - period 1
        assert get_continued_fraction_period(2) == 1

        # √3 = [1;(1,2)] - period 2
        assert get_continued_fraction_period(3) == 2

        # √5 = [2;(4)] - period 1
        assert get_continued_fraction_period(5) == 1

        # √6 = [2;(2,4)] - period 2
        assert get_continued_fraction_period(6) == 2

        # √7 = [2;(1,1,1,4)] - period 4
        assert get_continued_fraction_period(7) == 4

        # √8 = [2;(1,4)] - period 2
        assert get_continued_fraction_period(8) == 2

        # √10 = [3;(6)] - period 1
        assert get_continued_fraction_period(10) == 1

        # √23 = [4;(1,3,1,8)] - period 4
        assert get_continued_fraction_period(23) == 4

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        # The naive solution should work correctly
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        # The optimized solution should work correctly
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution"""
        # The mathematical solution should work correctly
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 0

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        # All solutions should return the same result
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert naive_result == optimized_result
        assert optimized_result == mathematical_result
        assert naive_result == mathematical_result

    @pytest.mark.parametrize(
        "n,expected_odd",
        [
            (2, True),  # period 1 (odd)
            (3, False),  # period 2 (even)
            (5, True),  # period 1 (odd)
            (6, False),  # period 2 (even)
            (7, False),  # period 4 (even)
            (8, False),  # period 2 (even)
            (10, True),  # period 1 (odd)
            (23, False),  # period 4 (even)
        ],
    )
    def test_odd_period_classification(self, n: int, expected_odd: bool) -> None:
        """Test classification of odd vs even periods"""
        period = get_continued_fraction_period(n)
        is_odd = period % 2 == 1
        assert is_odd == expected_odd, (
            f"√{n} has period {period}, expected odd={expected_odd}"
        )

    def test_small_range_count(self) -> None:
        """Test counting odd periods for small range"""
        # Count odd periods for N ≤ 13 (excluding perfect squares)
        count = 0
        for n in range(2, 14):
            if not is_perfect_square(n):
                period = get_continued_fraction_period(n)
                if period % 2 == 1:
                    count += 1

        # Expected odd periods: 2(1), 5(1), 10(1), 13(5) = 4 odd periods
        assert count == 4
