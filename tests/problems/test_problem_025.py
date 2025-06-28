#!/usr/bin/env python3
"""
Tests for Problem 025: 1000-digit Fibonacci number
"""

from collections.abc import Callable

import pytest

from problems.problem_025 import solve_naive, solve_optimized


@pytest.mark.parametrize("solver", [solve_naive, solve_optimized])
class TestProblem025:
    """Tests for Problem 025 solvers."""

    def test_small_cases(self, solver: Callable[[int], int]) -> None:
        """Tests small cases with known answers."""
        # F_1 = 1 (1 digit)
        assert solver(1) == 1

        # F_7 = 13 (2 digits)
        assert solver(2) == 7

        # F_12 = 144 (3 digits) - from problem description
        assert solver(3) == 12

    def test_edge_cases(self, solver: Callable[[int], int]) -> None:
        """Tests edge cases."""
        assert solver(0) == 0
        assert solver(-1) == 0

    def test_medium_cases(self, solver: Callable[[int], int]) -> None:
        """Tests medium-sized cases."""
        # F_17 = 1597 (4 digits)
        assert solver(4) == 17

        # F_21 = 10946 (5 digits)
        assert solver(5) == 21

    @pytest.mark.slow
    def test_main_problem(self, solver: Callable[[int], int]) -> None:
        """Tests the main problem case (1000 digits)."""
        target_digits = 1000
        result = solver(target_digits)

        # Verify the result is reasonable (should be around 4782)
        assert 4700 <= result <= 4800

        # Verify that both solvers give the same answer
        naive_result = solve_naive(target_digits)
        optimized_result = solve_optimized(target_digits)
        assert naive_result == optimized_result

    def test_consistency_between_solvers(self, solver: Callable[[int], int]) -> None:
        """Tests that all solvers give consistent results."""
        test_cases = [1, 2, 3, 4, 5, 10]

        for digits in test_cases:
            naive_result = solve_naive(digits)
            optimized_result = solve_optimized(digits)
            assert naive_result == optimized_result == solver(digits)
