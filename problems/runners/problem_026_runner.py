#!/usr/bin/env python3
"""
Problem 026 Runner: Execution and demonstration code for Problem 026.

This module handles the execution and demonstration of Problem 026 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_026 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem026Runner(BaseProblemRunner):
    """Runner for Problem 026: Reciprocal cycles."""

    def __init__(
        self,
        enable_performance_test: bool = False,
        enable_demonstrations: bool = False,
    ) -> None:
        super().__init__(
            "026",
            "Reciprocal cycles",
            983,
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 026."""
        return [
            (10, 7),  # 1/7 has the longest recurring cycle for d < 10
            (100, 97),  # Known result for d < 100
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 026."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 026."""
        return None


def main() -> None:
    """メイン関数"""
    runner = Problem026Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run benchmark for Problem 026."""
    runner = Problem026Runner(enable_demonstrations=False)
    runner.run_problem()


if __name__ == "__main__":
    main()
