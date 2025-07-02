#!/usr/bin/env python3
"""
Problem 033 Runner: Execution and demonstration code for Problem 033.

This module handles the execution and demonstration of Problem 033 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_033 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem033Runner(BaseProblemRunner):
    """Runner for Problem 033: Digit cancelling fractions."""

    def __init__(self) -> None:
        super().__init__("033", "Digit cancelling fractions")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 033."""
        return [
            (49, 98, True),  # 例題: 49/98 = 4/8
            (16, 64, True),  # 16/64 = 1/4
            (26, 65, True),  # 26/65 = 2/5
            (19, 95, True),  # 19/95 = 1/5
            (30, 50, False),  # 自明な例
            (12, 21, False),  # 桁キャンセルできるが結果が異なる
            (11, 22, False),  # 同じ桁だが桁キャンセルの結果が異なる
            (12, 34, False),  # 共通桁なし
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 033."""
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
    runner = Problem033Runner()
    runner.main()


if __name__ == "__main__":
    main()
