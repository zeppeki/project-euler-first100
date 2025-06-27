#!/usr/bin/env python3
"""
Tests for Problem 024: Lexicographic permutations
"""

from collections.abc import Callable

import pytest

from problems.problem_024 import solve_naive, solve_optimized


@pytest.mark.parametrize("solver", [solve_naive, solve_optimized])
class TestProblem024:
    """Tests for Problem 024 solvers."""

    def test_example_case(self, solver: Callable[[str, int], str]) -> None:
        """Tests the example case from the problem description."""
        digits = "012"
        assert solver(digits, 1) == "012"
        assert solver(digits, 2) == "021"
        assert solver(digits, 3) == "102"
        assert solver(digits, 4) == "120"
        assert solver(digits, 5) == "201"
        assert solver(digits, 6) == "210"

    def test_main_problem(self, solver: Callable[[str, int], str]) -> None:
        """Tests the main problem case."""
        digits = "0123456789"
        n = 1_000_000
        expected = "2783915460"
        assert solver(digits, n) == expected

    def test_invalid_n(self, solver: Callable[[str, int], str]) -> None:
        """Tests for n that is out of bounds."""
        digits = "012"
        assert solver(digits, 0) == ""
        assert solver(digits, 7) == ""
