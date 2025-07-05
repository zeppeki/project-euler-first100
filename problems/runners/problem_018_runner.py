#!/usr/bin/env python3
"""
Problem 018 Runner: Execution and demonstration code for Problem 018.

This module handles the execution and demonstration of Problem 018 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_018 import (
    get_example_triangle,
    get_problem_triangle,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem018Runner(BaseProblemRunner):
    """Runner for Problem 018: Maximum Path Sum I."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "018",
            "Maximum Path Sum I",
            problem_answer=1074,  # Known answer for maximum path sum
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 018."""
        example_triangle = get_example_triangle()
        return [
            (example_triangle, 23),  # 例題の三角形: 期待値 23
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 018."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (get_problem_triangle(),)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 018."""
        return [self._demonstrate_path_analysis]

    def _demonstrate_path_analysis(self) -> None:
        """三角形経路の動的計画法を表示"""
        example_triangle = get_example_triangle()
        problem_triangle = get_problem_triangle()

        print("例題三角形:")
        for row in example_triangle:
            print("  " + " ".join(f"{num:2d}" for num in row))

        example_result = solve_optimized(example_triangle)
        print(f"例題の最大経路和: {example_result}")

        print("\n本問題の三角形:")
        print(f"行数: {len(problem_triangle)}")
        print(f"最初の行: {problem_triangle[0]}")
        print(f"最後の行の要素数: {len(problem_triangle[-1])}")

        problem_result = solve_optimized(problem_triangle)
        print(f"本問題の最大経路和: {problem_result}")

        print("\n動的計画法の説明:")
        print("- 下から上へ計算")
        print("- 各位置で左下と右下の最大値を選択")
        print("- 時間計算量: O(n²), 空間計算量: O(n)")


def main() -> None:
    """Main entry point."""
    # デフォルト実行（パフォーマンステストのみ無効、デモンストレーションは有効）
    runner = Problem018Runner(enable_demonstrations=True)
    runner.main()


def run_with_all_features() -> None:
    """Run with all features enabled for demonstration."""
    print("=== 全機能有効 ===")
    runner = Problem018Runner(enable_performance_test=True, enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 018."""
    print("=== Problem 018 Performance Benchmark ===")
    runner = Problem018Runner(enable_performance_test=True, enable_demonstrations=False)
    # Skip tests and run only the performance benchmark
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
