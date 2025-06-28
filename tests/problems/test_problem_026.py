#!/usr/bin/env python3
"""
Tests for Problem 026: Reciprocal cycles
"""

from collections.abc import Callable

import pytest

from problems.problem_026 import (
    get_cycle_length_naive,
    get_cycle_length_optimized,
    solve_naive,
    solve_optimized,
)


class TestCycleLengthFunctions:
    """Tests for cycle length calculation functions."""

    @pytest.mark.parametrize(
        "func", [get_cycle_length_naive, get_cycle_length_optimized]
    )
    def test_known_cycle_lengths(self, func: Callable[[int], int]) -> None:
        """Tests known cycle lengths from the problem description."""
        # Non-recurring decimals
        assert func(2) == 0  # 1/2 = 0.5
        assert func(4) == 0  # 1/4 = 0.25
        assert func(5) == 0  # 1/5 = 0.2
        assert func(8) == 0  # 1/8 = 0.125
        assert func(10) == 0  # 1/10 = 0.1

        # Recurring decimals
        assert func(3) == 1  # 1/3 = 0.(3)
        assert func(6) == 1  # 1/6 = 0.1(6)
        assert func(7) == 6  # 1/7 = 0.(142857)
        assert func(9) == 1  # 1/9 = 0.(1)

    @pytest.mark.parametrize(
        "func", [get_cycle_length_naive, get_cycle_length_optimized]
    )
    def test_more_cycle_lengths(self, func: Callable[[int], int]) -> None:
        """Tests additional cycle lengths."""
        assert func(11) == 2  # 1/11 = 0.(09)
        assert func(13) == 6  # 1/13 = 0.(076923)
        assert func(17) == 16  # 1/17 has cycle length 16

    @pytest.mark.parametrize(
        "func", [get_cycle_length_naive, get_cycle_length_optimized]
    )
    def test_edge_cases(self, func: Callable[[int], int]) -> None:
        """Tests edge cases."""
        assert func(0) == 0
        assert func(1) == 0

    def test_consistency_between_functions(self) -> None:
        """Tests that both cycle length functions give consistent results."""
        test_cases = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 19, 23]

        for d in test_cases:
            naive_result = get_cycle_length_naive(d)
            optimized_result = get_cycle_length_optimized(d)
            assert naive_result == optimized_result, (
                f"Mismatch for d={d}: naive={naive_result}, optimized={optimized_result}"
            )


@pytest.mark.parametrize("solver", [solve_naive, solve_optimized])
class TestProblem026:
    """Tests for Problem 026 solvers."""

    def test_small_limit(self, solver: Callable[[int], int]) -> None:
        """Tests with a small limit."""
        # For d < 10, the longest cycle is 1/7 with length 6
        assert solver(10) == 7

    def test_medium_limit(self, solver: Callable[[int], int]) -> None:
        """Tests with a medium limit."""
        # For d < 20, the longest cycle is 1/19 with length 18
        result = solver(20)
        assert result == 19

    @pytest.mark.slow
    def test_main_problem(self, solver: Callable[[int], int]) -> None:
        """Tests the main problem case (limit 1000)."""
        result = solver(1000)

        # Verify the result is reasonable
        assert 900 <= result < 1000

        # Verify that both solvers give the same answer
        naive_result = solve_naive(1000)
        optimized_result = solve_optimized(1000)
        assert naive_result == optimized_result

    def test_consistency_between_solvers(self, solver: Callable[[int], int]) -> None:
        """Tests that all solvers give consistent results."""
        test_limits = [10, 20, 50]

        for limit in test_limits:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            assert naive_result == optimized_result == solver(limit)
