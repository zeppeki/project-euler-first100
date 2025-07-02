#!/usr/bin/env python3
"""
Problem 011 Runner: Execution and demonstration code for Problem 011.

This module handles the execution and demonstration of Problem 011 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_011 import (
    GRID_DATA,
    find_max_product_sequence,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem011Runner(BaseProblemRunner):
    """Runner for Problem 011: Largest product in a grid."""

    def __init__(self) -> None:
        super().__init__("011", "Largest product in a grid")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 011."""
        # 小さなテストグリッド
        test_grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        return [
            (test_grid, 4, 43680),  # 13×14×15×16 = 43680
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 011."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (GRID_DATA, 4)

    def get_demonstration_functions(self) -> list[tuple[str, Callable[[], None]]]:
        """Get demonstration functions for Problem 011."""
        return [("最大積のシーケンス詳細", self._demonstrate_max_sequence)]

    def _demonstrate_max_sequence(self) -> None:
        """最大積のシーケンスの詳細を表示"""
        length = 4
        max_product, sequence, direction = find_max_product_sequence(GRID_DATA, length)
        print(f"最大積のシーケンス: {sequence}")
        print(f"方向: {direction}")
        print(f"積: {max_product:,}")
        print(f"Grid size: {len(GRID_DATA)}×{len(GRID_DATA[0])}")


def main() -> None:
    """メイン関数"""
    runner = Problem011Runner()
    runner.main()


if __name__ == "__main__":
    main()
