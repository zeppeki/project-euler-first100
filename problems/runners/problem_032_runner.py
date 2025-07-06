#!/usr/bin/env python3
"""
Problem 032 Runner: Execution and demonstration code for Problem 032.

This module handles the execution and demonstration of Problem 032 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_032 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem032Runner(BaseProblemRunner):
    """Runner for Problem 032: Pandigital products."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "032",
            "Pandigital products",
            problem_answer=45228,  # Known answer for sum of all products with pandigital identity
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 032."""
        return [
            ("123456789", True),  # 正常な1-9パンデジタル
            ("987654321", True),  # 逆順の1-9パンデジタル
            ("123456788", False),  # 8が重複
            ("12345679", False),  # 8文字（不足）
            ("1234567890", False),  # 10文字（過多）
            ("023456789", False),  # 0を含む
            ("391867254", True),  # 例題の組み合わせ
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 032."""
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
    runner = Problem032Runner(enable_demonstrations=True)
    runner.main()


def run_with_all_features() -> None:
    """Run with all features enabled for demonstration."""
    print("=== 全機能有効 ===")
    runner = Problem032Runner(enable_performance_test=True, enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 032."""
    print("=== Problem 032 Performance Benchmark ===")
    runner = Problem032Runner(enable_performance_test=True, enable_demonstrations=False)
    # Skip tests and run only the performance benchmark
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
