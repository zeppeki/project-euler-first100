#!/usr/bin/env python3
"""Tests for Problem 066"""

from problems.problem_066 import (
    find_pell_solution,
    get_continued_fraction_period,
    is_perfect_square,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem066:
    """Test cases for Problem 066"""

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
        assert not is_perfect_square(13)

    def test_get_continued_fraction_period(self) -> None:
        """Test continued fraction period calculation"""
        # Perfect squares should return empty period
        a0, period = get_continued_fraction_period(4)
        assert a0 == 2
        assert period == []

        a0, period = get_continued_fraction_period(9)
        assert a0 == 3
        assert period == []

        # Test some known continued fractions
        # √2 = [1; (2)]
        a0, period = get_continued_fraction_period(2)
        assert a0 == 1
        assert period == [2]

        # √3 = [1; (1, 2)]
        a0, period = get_continued_fraction_period(3)
        assert a0 == 1
        assert period == [1, 2]

    def test_solve_pell_equation(self) -> None:
        """Test Pell equation solutions"""
        # Test known solutions from problem description
        test_cases = [
            (2, (3, 2)),  # x=3, y=2 for D=2
            (3, (2, 1)),  # x=2, y=1 for D=3
            (5, (9, 4)),  # x=9, y=4 for D=5
            (6, (5, 2)),  # x=5, y=2 for D=6
            (7, (8, 3)),  # x=8, y=3 for D=7
            (13, (649, 180)),  # x=649, y=180 for D=13
        ]

        for d, (expected_x, expected_y) in test_cases:
            x, y = find_pell_solution(d)
            assert x == expected_x, f"D={d}: expected x={expected_x}, got x={x}"
            assert y == expected_y, f"D={d}: expected y={expected_y}, got y={y}"
            # Verify the Pell equation x² - dy² = 1
            assert x * x - d * y * y == 1, f"D={d}: Pell equation not satisfied"

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        # The naive solution should work correctly
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0
        assert result <= 1000

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        # The optimized solution should work correctly
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0
        assert result <= 1000

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution"""
        # The mathematical solution should work correctly
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 0
        assert result <= 1000

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        # All solutions should return the same result
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert naive_result == optimized_result
        assert optimized_result == mathematical_result
        assert naive_result == mathematical_result

    def test_pell_equation_verification(self) -> None:
        """Test that Pell equation solutions are correct for small D values"""
        # Test a few more D values to ensure our algorithm works
        for d in [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]:
            if not is_perfect_square(d):
                x, y = find_pell_solution(d)
                # Verify the equation x² - dy² = 1
                assert x * x - d * y * y == 1, (
                    f"D={d}: x={x}, y={y} doesn't satisfy Pell equation"
                )
                # Ensure we have positive solutions
                assert x > 0 and y > 0, f"D={d}: solutions must be positive"

    def test_perfect_square_exclusion(self) -> None:
        """Test that perfect squares are properly excluded"""
        # Perfect squares should return (0, 0) from find_pell_solution
        for perfect_square in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
            x, y = find_pell_solution(perfect_square)
            assert x == 0 and y == 0, (
                f"Perfect square {perfect_square} should have no solution"
            )
