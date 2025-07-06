#!/usr/bin/env python3
"""
Problem 030 Runner: Execution and demonstration code for Problem 030.

This module handles the execution and demonstration of Problem 030 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_030 import solve
from problems.runners.base_runner import BaseProblemRunner


class Problem030Runner(BaseProblemRunner):
    """Runner for Problem 030: Digit fifth powers."""

    def __init__(
        self,
        enable_performance_test: bool = True,
        enable_demonstrations: bool = True,
    ) -> None:
        super().__init__(
            "030",
            "Digit fifth powers",
            443839,
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 030."""
        return [
            (4, 19316),  # Fourth powers: 1634 + 8208 + 9474 = 19316
            (5, 443839),  # Fifth powers (actual problem)
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 030."""
        return [
            ("解法", solve),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (5,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 030."""
        return None


def main() -> None:
    """メイン関数"""
    runner = Problem030Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run benchmark for Problem 030."""
    runner = Problem030Runner(enable_demonstrations=False)
    runner.run_problem()


if __name__ == "__main__":
    main()
