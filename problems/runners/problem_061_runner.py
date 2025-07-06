#!/usr/bin/env python3
"""
Problem 061 Runner: Execution and demonstration code for Problem 061.

This module handles the execution and demonstration of Problem 061 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_061 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem061Runner(BaseProblemRunner):
    """Runner for Problem 061: Cyclical figurate numbers."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "061",
            "Cyclical figurate numbers",
            28684,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 061."""
        # Skip runner tests as they are covered by unit tests
        return []

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 061."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()


def main() -> None:
    """メイン関数"""
    runner = Problem061Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem061Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
