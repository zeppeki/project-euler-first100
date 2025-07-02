#!/usr/bin/env python3
"""
Problem 040 Runner: Execution and demonstration code for Problem 040.

This module handles the execution and demonstration of Problem 040 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_040 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem040Runner(BaseProblemRunner):
    """Runner for Problem 040: Champernowne's constant."""

    def __init__(self) -> None:
        super().__init__("040", "Champernowne's constant")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 040."""
        return []  # TODO: Add test cases

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 040."""
        return [("素直な解法", solve_naive), ("最適化解法", solve_optimized)]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()


def main() -> None:
    """メイン関数"""
    runner = Problem040Runner()
    runner.main()


if __name__ == "__main__":
    main()
