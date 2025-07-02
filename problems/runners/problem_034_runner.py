#!/usr/bin/env python3
"""
Problem 034 Runner: Execution and demonstration code for Problem 034.

This module handles the execution and demonstration of Problem 034 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_034 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem034Runner(BaseProblemRunner):
    """Runner for Problem 034: Digit factorials."""

    def __init__(self) -> None:
        super().__init__("034", "Digit factorials")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 034."""
        return [
            (145, True),  # 例題: 1! + 4! + 5! = 1 + 24 + 120 = 145
            (1, False),  # 1! = 1 は和ではない
            (2, False),  # 2! = 2 は和ではない
            (123, False),  # 1! + 2! + 3! = 1 + 2 + 6 = 9 ≠ 123
            (40585, True),  # 実際の桁階乗数
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 034."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()  # TODO: Add parameters


def main() -> None:
    """メイン関数"""
    runner = Problem034Runner()
    runner.main()


if __name__ == "__main__":
    main()
