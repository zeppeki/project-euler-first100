#!/usr/bin/env python3
"""Tests for Problem 062"""

from problems.problem_062 import get_digit_signature, solve_naive, solve_optimized


class TestProblem062:
    """Test cases for Problem 062"""

    def test_get_digit_signature(self) -> None:
        """Test digit signature function"""
        # Test with known cube permutations
        assert get_digit_signature(41063625) == "01234566"  # 345³
        assert get_digit_signature(56623104) == "01234566"  # 384³
        assert get_digit_signature(66430125) == "01234566"  # 405³

        # Test that different permutations have the same signature
        assert get_digit_signature(123) == get_digit_signature(321)
        assert get_digit_signature(1234) == get_digit_signature(4321)

        # Test that different numbers have different signatures
        assert get_digit_signature(123) != get_digit_signature(456)

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0
        # The answer should be a cube number
        cube_root = round(result ** (1 / 3))
        assert cube_root**3 == result

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0
        # The answer should be a cube number
        cube_root = round(result ** (1 / 3))
        assert cube_root**3 == result

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        result_naive = solve_naive()
        result_optimized = solve_optimized()

        assert result_naive == result_optimized
        assert result_naive > 0
