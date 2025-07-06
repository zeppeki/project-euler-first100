#!/usr/bin/env python3
"""
Problem 041 Runner: Execution and demonstration code for Problem 041.

This module handles the execution and demonstration of Problem 041 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_041 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem041Runner(BaseProblemRunner):
    """Runner for Problem 041: Pandigital prime."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "041",
            "Pandigital prime",
            7652413,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 041."""
        return [
            (4, 4231),  # Largest 4-digit pandigital prime
            (7, 7652413),  # Largest 7-digit pandigital prime
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 041."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (9,)


def main() -> None:
    """メイン関数"""
    runner = Problem041Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem041Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
