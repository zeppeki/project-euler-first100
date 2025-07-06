#!/usr/bin/env python3
"""
Problem 043 Runner: Execution and demonstration code for Problem 043.

This module handles the execution and demonstration of Problem 043 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_043 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem043Runner(BaseProblemRunner):
    """Runner for Problem 043: Sub-string divisibility."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "043",
            "Sub-string divisibility",
            16695334890,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 043."""
        return []  # TODO: Add test cases

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 043."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()


def main() -> None:
    """メイン関数"""
    runner = Problem043Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem043Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
