#!/usr/bin/env python3
"""
Problem 021 Runner: Execution and demonstration code for Problem 021.

This module handles the execution and demonstration of Problem 021 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_021 import (
from problems.runners.base_runner import BaseProblemRunner


class Problem021Runner(BaseProblemRunner):
    """Runner for Problem 021: Amicable Numbers."""

    def __init__(self) -> None:
        super().__init__("021", "Amicable Numbers")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 021."""
        return []  # TODO: Add test cases

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 021."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical)
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (=="),)


def main() -> None:
    """メイン関数"""
    runner = Problem021Runner()
    runner.main()


if __name__ == "__main__":
    main()
