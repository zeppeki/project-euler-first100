#!/usr/bin/env python3
"""
Problem 001 Runner: Execution and demonstration code for Problem 001.

This module handles the execution and demonstration of Problem 001 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_001 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem001Runner(BaseProblemRunner):
    """Runner for Problem 001: Multiples of 3 and 5."""

    def __init__(self) -> None:
        super().__init__("001", "Multiples of 3 and 5")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 001."""
        return [
            (10, 23),  # 3 + 5 + 6 + 9 = 23
            (20, 78),  # 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
            (100, 2318),  # Known result for limit 100
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 001."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (1000,)


def main() -> None:
    """Main entry point."""
    runner = Problem001Runner()
    runner.main()


if __name__ == "__main__":
    main()
