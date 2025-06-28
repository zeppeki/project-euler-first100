#!/usr/bin/env python3
"""
Tests for Problem 030: Digit fifth powers
"""

from problems.problem_030 import solve


class TestProblem030:
    """Tests for Problem 030 solver."""

    def test_fourth_power(self) -> None:
        """Tests the case for the fourth power as described in the problem."""
        assert solve(4) == 19316

    def test_fifth_power(self) -> None:
        """Tests the main problem case for the fifth power."""
        assert solve(5) == 443839
