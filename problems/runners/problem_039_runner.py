#!/usr/bin/env python3
"""
Problem 039 Runner: Execution and demonstration code for Problem 039.

This module handles the execution and demonstration of Problem 039 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.runners.base_runner import BaseProblemRunner


class Problem039Runner(BaseProblemRunner):
    """Runner for Problem 039: Integer right triangles."""

    def __init__(self) -> None:
        super().__init__("039", "Integer right triangles")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 039."""
        return [
            (12, 12),  # (3,4,5) の周囲が唯一の解
            (30, 12),  # p≤30の範囲では p=12 が最大解数
            (60, 60),  # p=60 が2つの解を持ち最大
            (120, 120),  # p=120 が3つの解を持ち最大
            (200, 120),  # p≤200の範囲では p=120 が最大
            (500, 420),  # p≤500の範囲では p=420 が最大
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 039."""
        from problems.problem_039 import solve_naive, solve_optimized

        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000,)


def main() -> None:
    """メイン関数"""
    runner = Problem039Runner()
    runner.main()


if __name__ == "__main__":
    main()
