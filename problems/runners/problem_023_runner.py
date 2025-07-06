#!/usr/bin/env python3
"""
Problem 023 Runner: Execution and demonstration code for Problem 023.

This module handles the execution and demonstration of Problem 023 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_023 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem023Runner(BaseProblemRunner):
    """Runner for Problem 023: Non-Abundant Sums."""

    def __init__(
        self,
        enable_performance_test: bool = True,
        enable_demonstrations: bool = True,
    ) -> None:
        super().__init__(
            "023",
            "Non-Abundant Sums",
            4179871,
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 023."""
        return [
            # 小さな値でのテスト
            (30, 230),  # 1+2+...+23+25+26+27+29 = 230 (24は12+12, 28は12+16で表せる)
            (100, 1574),  # 既知の結果
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 023."""
        return [("素直な解法", solve_naive), ("最適化解法", solve_optimized)]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (28123,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 023."""
        return None


def main() -> None:
    """メイン関数"""
    runner = Problem023Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run benchmark for Problem 023."""
    runner = Problem023Runner(enable_demonstrations=False)
    runner.run_problem()


if __name__ == "__main__":
    main()
