#!/usr/bin/env python3
"""
Runner for Problem 003: Largest prime factor

This module contains the execution code for Problem 003, separated from the
algorithm implementations for better test coverage and code organization.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_003 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem003Runner(BaseProblemRunner):
    """Runner for Problem 003: Largest prime factor."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "003",
            "Largest prime factor",
            problem_answer=6857,  # Known answer for number 600851475143
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 003."""
        return [
            (13195, 29),  # Example: 5, 7, 13, 29 → max is 29
            (100, 5),  # 100 = 2^2 × 5^2 → max is 5
            (84, 7),  # 84 = 2^2 × 3 × 7 → max is 7
            (17, 17),  # 素数 → 最大は17
            (25, 5),  # 25 = 5^2 → 最大は5
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 003."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (600851475143,)


def main() -> None:
    """Main entry point."""
    # デフォルト実行（パフォーマンステストのみ無効、デモンストレーションは有効）
    runner = Problem003Runner(enable_demonstrations=True)
    runner.main()


def run_with_all_features() -> None:
    """Run with all features enabled for demonstration."""
    print("=== 全機能有効 ===")
    runner = Problem003Runner(enable_performance_test=True, enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 003."""
    print("=== Problem 003 Performance Benchmark ===")
    runner = Problem003Runner(enable_performance_test=True, enable_demonstrations=False)
    # Skip tests and run only the performance benchmark
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
