#!/usr/bin/env python3
"""Tests for Problem 040"""

from problems.problem_040 import solve_naive, solve_optimized


class TestProblem040:
    """Test cases for Problem 040"""

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        assert naive_result == optimized_result

    def test_individual_digits(self) -> None:
        """Test individual digit retrieval for known positions"""
        champernowne = "123456789101112131415161718192021222324252627282930"

        assert int(champernowne[0]) == 1  # d1
        assert int(champernowne[9]) == 1  # d10 (from "10")
        assert int(champernowne[11]) == 1  # d12 (from "12")

        def get_digit_at_position(pos: int) -> int:
            if pos <= 9:
                return pos

            length = 1
            count = 9
            start = 1

            while pos > length * count:
                pos -= length * count
                length += 1
                count *= 10
                start *= 10

            number = start + (pos - 1) // length
            digit_index = (pos - 1) % length

            return int(str(number)[digit_index])

        assert get_digit_at_position(1) == 1
        assert get_digit_at_position(10) == 1
        assert get_digit_at_position(12) == 1
