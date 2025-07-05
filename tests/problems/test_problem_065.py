#!/usr/bin/env python3
"""Tests for Problem 065"""

from problems.problem_065 import (
    compute_convergent,
    get_e_continued_fraction_coefficient,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    sum_of_digits,
)


class TestProblem065:
    """Test cases for Problem 065"""

    def test_get_e_continued_fraction_coefficient(self) -> None:
        """Test e continued fraction coefficient generation"""
        # Test the pattern [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
        assert get_e_continued_fraction_coefficient(0) == 2
        assert get_e_continued_fraction_coefficient(1) == 1
        assert get_e_continued_fraction_coefficient(2) == 2
        assert get_e_continued_fraction_coefficient(3) == 1
        assert get_e_continued_fraction_coefficient(4) == 1
        assert get_e_continued_fraction_coefficient(5) == 4
        assert get_e_continued_fraction_coefficient(6) == 1
        assert get_e_continued_fraction_coefficient(7) == 1
        assert get_e_continued_fraction_coefficient(8) == 6
        assert get_e_continued_fraction_coefficient(9) == 1
        assert get_e_continued_fraction_coefficient(10) == 1
        assert get_e_continued_fraction_coefficient(11) == 8
        assert get_e_continued_fraction_coefficient(12) == 1
        assert get_e_continued_fraction_coefficient(13) == 1
        assert get_e_continued_fraction_coefficient(14) == 10

    def test_sum_of_digits(self) -> None:
        """Test digit sum calculation"""
        assert sum_of_digits(123) == 6
        assert sum_of_digits(1457) == 17  # From problem example
        assert sum_of_digits(0) == 0
        assert sum_of_digits(999) == 27

    def test_compute_convergent(self) -> None:
        """Test convergent computation"""
        # Test known convergents from problem description
        convergents = [
            (2, 1),  # 0th: 2
            (3, 1),  # 1st: 3
            (8, 3),  # 2nd: 8/3
            (11, 4),  # 3rd: 11/4
            (19, 7),  # 4th: 19/7
            (87, 32),  # 5th: 87/32
            (106, 39),  # 6th: 106/39
            (193, 71),  # 7th: 193/71
            (1264, 465),  # 8th: 1264/465
            (1457, 536),  # 9th: 1457/536
        ]

        for i, (expected_num, expected_den) in enumerate(convergents):
            num, den = compute_convergent(i)
            assert num == expected_num, (
                f"Convergent {i}: expected numerator {expected_num}, got {num}"
            )
            assert den == expected_den, (
                f"Convergent {i}: expected denominator {expected_den}, got {den}"
            )

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

    def test_tenth_convergent_example(self) -> None:
        """Test the specific example given in the problem"""
        # The 10th convergent (index 9) should be 1457/536
        num, den = compute_convergent(9)
        assert num == 1457
        assert den == 536

        # Sum of digits in numerator should be 17
        digit_sum = sum_of_digits(num)
        assert digit_sum == 17
