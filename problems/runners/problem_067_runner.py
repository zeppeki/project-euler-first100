#!/usr/bin/env python3
"""
Problem 067 Runner: Execution and demonstration code for Problem 067.

This module handles the execution and demonstration of Problem 067 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_067 import (
    get_problem_triangle,
    solve_mathematical,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem067Runner(BaseProblemRunner):
    """Runner for Problem 067: Maximum Path Sum II."""

    def __init__(self) -> None:
        super().__init__("067", "Maximum Path Sum II")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 067."""
        # 小さなテストケース（実際の問題は100行で大きすぎるため）
        small_triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        return [
            (small_triangle, 23),  # 小さな三角形: 期待値 23
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 067."""
        return [
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
            # 注意: solve_naiveは100行の三角形では実用的でないため除外
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (get_problem_triangle(),)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 067."""
        return [self._demonstrate_path_analysis]

    def _demonstrate_path_analysis(self) -> None:
        """三角形経路の動的計画法を表示"""
        small_triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        problem_triangle = get_problem_triangle()

        print("小さな例題三角形:")
        for row in small_triangle:
            print("  " + " ".join(f"{num:2d}" for num in row))

        small_result = solve_optimized(small_triangle)
        print(f"小さな例題の最大経路和: {small_result}")

        print("\nProblem 067の三角形:")
        print(f"行数: {len(problem_triangle)}")
        print(f"最初の行: {problem_triangle[0]}")
        print(f"最後の行の要素数: {len(problem_triangle[-1])}")

        problem_result = solve_optimized(problem_triangle)
        print(f"Problem 067の最大経路和: {problem_result}")

        print("\n動的計画法の説明:")
        print("- 下から上へ計算")
        print("- 各位置で左下と右下の最大値を選択")
        print("- 時間計算量: O(n²), 空間計算量: O(n)")
        print("- 2^99通りの経路を効率的に処理")

        print("\nアルゴリズムの効率性:")
        print("- ブルートフォース: 2^99 ≈ 6.3×10^29 通り")
        print("- 動的計画法: 100×101/2 = 5050 計算")
        print("- 劇的な効率化により実用的な時間で解決")


def main() -> None:
    """メイン関数"""
    runner = Problem067Runner()
    runner.main()


if __name__ == "__main__":
    main()
