#!/usr/bin/env python3
"""
Problem 028 Runner: Execution and demonstration code for Problem 028.

This module handles the execution and demonstration of Problem 028 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_028 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem028Runner(BaseProblemRunner):
    """Runner for Problem 028: Number spiral diagonals ===."""

    def __init__(
        self,
        enable_performance_test: bool = True,
        enable_demonstrations: bool = True,
    ) -> None:
        super().__init__(
            "028",
            "Number spiral diagonals ===",
            669171001,
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 028."""
        return [
            (1, 1),
            (3, 25),  # 1 + 3 + 5 + 7 + 9 = 25
            (5, 101),  # 問題文の例
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 028."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1001,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 028."""
        return None


def main() -> None:
    """メイン関数"""
    runner = Problem028Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run benchmark for Problem 028."""
    runner = Problem028Runner(enable_demonstrations=False)
    runner.run_problem()


if __name__ == "__main__":
    main()
