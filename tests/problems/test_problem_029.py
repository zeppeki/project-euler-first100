#!/usr/bin/env python3
"""
Tests for Problem 029: Distinct powers
"""

from collections.abc import Callable

import pytest

from problems.problem_029 import solve_naive


@pytest.mark.parametrize("solver", [solve_naive])
class TestProblem029:
    """Tests for Problem 029 solvers."""

    def test_example_case(self, solver: Callable[[int], int]) -> None:
        """Tests the example case from the problem description."""
        assert solver(5) == 15

    def test_main_problem(self, solver: Callable[[int], int]) -> None:
        """Tests the main problem case."""
        assert solver(100) == 9183
