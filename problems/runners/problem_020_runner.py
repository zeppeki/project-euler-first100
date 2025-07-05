#!/usr/bin/env python3
"""
Problem 020 Runner: Execution and demonstration code for Problem 020.

This module handles the execution and demonstration of Problem 020 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_020 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem020Runner(BaseProblemRunner):
    """Runner for Problem 020: Factorial digit sum."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "020",
            "Factorial digit sum",
            problem_answer=648,  # Known answer for 100! digit sum
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 020."""
        return [
            (0, 1),  # 0! = 1 → 1
            (1, 1),  # 1! = 1 → 1
            (5, 3),  # 5! = 120 → 1+2+0 = 3
            (10, 27),  # 10! = 3628800 → 3+6+2+8+8+0+0 = 27
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 020."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (100,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 020."""
        return [self._demonstrate_factorial_analysis]

    def _demonstrate_factorial_analysis(self) -> None:
        """階乗の桁数分析を表示"""
        import math

        n = 100
        result = solve_optimized(n)
        factorial_100 = math.factorial(n)

        print(f"{n}! の桁の和: {result}")
        print(f"{n}! の桁数: {len(str(factorial_100))}")
        print(f"{n}! の最初の20桁: {str(factorial_100)[:20]}...")
        print(f"{n}! の最後の20桁: ...{str(factorial_100)[-20:]}")

        print("\n小さな階乗の桁数と桁の和:")
        for i in range(1, 21):
            factorial = math.factorial(i)
            digit_sum = sum(int(digit) for digit in str(factorial))
            print(
                f"{i:2d}! = {factorial:>15} → 桁数: {len(str(factorial)):2d}, 桁の和: {digit_sum:2d}"
            )

        print("\n階乗の成長:")
        milestones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        for milestone in milestones:
            factorial = math.factorial(milestone)
            digit_count = len(str(factorial))
            digit_sum = sum(int(digit) for digit in str(factorial))
            print(f"{milestone:3d}! → 桁数: {digit_count:3d}, 桁の和: {digit_sum:4d}")


def main() -> None:
    """Main entry point."""
    # デフォルト実行（パフォーマンステストのみ無効、デモンストレーションは有効）
    runner = Problem020Runner(enable_demonstrations=True)
    runner.main()


def run_with_all_features() -> None:
    """Run with all features enabled for demonstration."""
    print("=== 全機能有効 ===")
    runner = Problem020Runner(enable_performance_test=True, enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 020."""
    print("=== Problem 020 Performance Benchmark ===")
    runner = Problem020Runner(enable_performance_test=True, enable_demonstrations=False)
    # Skip tests and run only the performance benchmark
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
