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

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "034",
            "Digit factorials",
            problem_answer=40730,  # Known answer for sum of all numbers equal to sum of factorial of their digits
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

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
        return ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get optional demonstration functions for complex analysis."""
        return None


def main() -> None:
    """Main entry point."""
    # デフォルト実行（パフォーマンステストのみ無効、デモンストレーションは有効）
    runner = Problem034Runner(enable_demonstrations=True)
    runner.main()


def run_with_all_features() -> None:
    """Run with all features enabled for demonstration."""
    print("=== 全機能有効 ===")
    runner = Problem034Runner(enable_performance_test=True, enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 034."""
    print("=== Problem 034 Performance Benchmark ===")
    runner = Problem034Runner(enable_performance_test=True, enable_demonstrations=False)
    # Skip tests and run only the performance benchmark
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
