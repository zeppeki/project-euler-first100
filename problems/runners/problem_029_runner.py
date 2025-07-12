#!/usr/bin/env python3
"""
Problem 029 Runner: Execution and demonstration code for Problem 029.

This module handles the execution and demonstration of Problem 029 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_029 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem029Runner(BaseProblemRunner):
    """Runner for Problem 029: Distinct powers."""

    def __init__(
        self,
        enable_performance_test: bool = False,
        enable_demonstrations: bool = False,
    ) -> None:
        super().__init__(
            "029",
            "Distinct powers",
            9183,
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 029."""
        return [
            (5, 15),  # a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5
            (10, 69),  # Known result for a, b ≤ 10
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 029."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (100,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 029."""
        return None


def main() -> None:
    """メイン関数"""
    runner = Problem029Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run benchmark for Problem 029."""
    runner = Problem029Runner(enable_demonstrations=False)
    runner.run_problem()


if __name__ == "__main__":
    main()
