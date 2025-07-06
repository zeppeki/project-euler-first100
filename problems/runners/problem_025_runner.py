#!/usr/bin/env python3
"""
Problem 025 Runner: Execution and demonstration code for Problem 025.

This module handles the execution and demonstration of Problem 025 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_025 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem025Runner(BaseProblemRunner):
    """Runner for Problem 025: 1000-digit Fibonacci number."""

    def __init__(
        self,
        enable_performance_test: bool = True,
        enable_demonstrations: bool = True,
    ) -> None:
        super().__init__(
            "025",
            "1000-digit Fibonacci number",
            4782,
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 025."""
        return []  # TODO: Add test cases

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 025."""
        return [("素直な解法", solve_naive), ("最適化解法", solve_optimized)]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 025."""
        return None


def main() -> None:
    """メイン関数"""
    runner = Problem025Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run benchmark for Problem 025."""
    runner = Problem025Runner(enable_demonstrations=False)
    runner.run_problem()


if __name__ == "__main__":
    main()
