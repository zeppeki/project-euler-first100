#!/usr/bin/env python3
"""
Problem 038 Runner: Execution and demonstration code for Problem 038.

This module handles the execution and demonstration of Problem 038 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_038 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem038Runner(BaseProblemRunner):
    """Runner for Problem 038: Pandigital multiples."""

    def __init__(self) -> None:
        super().__init__("038", "Pandigital multiples")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 038."""
        return []  # TODO: Add test cases

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 038."""
        return [("素直な解法", solve_naive), ("最適化解法", solve_optimized)]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()


def main() -> None:
    """メイン関数"""
    runner = Problem038Runner()
    runner.main()


if __name__ == "__main__":
    main()
