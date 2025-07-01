#!/usr/bin/env python3
"""
Problem 002 Runner: Execution and demonstration code for Problem 002.

This module handles the execution and demonstration of Problem 002 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_002 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem002Runner(BaseProblemRunner):
    """Runner for Problem 002: Even Fibonacci numbers."""

    def __init__(self) -> None:
        super().__init__("002", "Even Fibonacci numbers")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 002."""
        return [
            (10, 10),  # 2 + 8 = 10
            (50, 44),  # 2 + 8 + 34 = 44
            (100, 44),  # 2 + 8 + 34 = 44
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 002."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (4_000_000,)


def main() -> None:
    """Main entry point."""
    runner = Problem002Runner()
    runner.main()


if __name__ == "__main__":
    main()
