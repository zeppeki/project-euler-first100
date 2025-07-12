#!/usr/bin/env python3
"""
Problem 040 Runner: Execution and demonstration code for Problem 040.

This module handles the execution and demonstration of Problem 040 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_040 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem040Runner(BaseProblemRunner):
    """Runner for Problem 040: Champernowne's constant."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "040",
            "Champernowne's constant",
            problem_answer=210,  # Known answer for product of d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 040."""
                return [
            # Test case: Main problem parameters
            ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get optional demonstration functions for complex analysis."""
        return None


def main() -> None:
    """Main entry point."""
    # デフォルト実行（パフォーマンステストのみ無効、デモンストレーションは有効）
    runner = Problem040Runner(enable_demonstrations=True)
    runner.main()


def run_with_all_features() -> None:
    """Run with all features enabled for demonstration."""
    print("=== 全機能有効 ===")
    runner = Problem040Runner(enable_performance_test=True, enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 040."""
    print("=== Problem 040 Performance Benchmark ===")
    runner = Problem040Runner(enable_performance_test=True, enable_demonstrations=False)
    # Skip tests and run only the performance benchmark
    result = runner.run_problem()
    print(f"Benchmark result: {result,
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 040."""
        return [("素直な解法", solve_naive), ("最適化解法", solve_optimized)]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get optional demonstration functions for complex analysis."""
        return None


def main() -> None:
    """Main entry point."""
    # デフォルト実行（パフォーマンステストのみ無効、デモンストレーションは有効）
    runner = Problem040Runner(enable_demonstrations=True)
    runner.main()


def run_with_all_features() -> None:
    """Run with all features enabled for demonstration."""
    print("=== 全機能有効 ===")
    runner = Problem040Runner(enable_performance_test=True, enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 040."""
    print("=== Problem 040 Performance Benchmark ===")
    runner = Problem040Runner(enable_performance_test=True, enable_demonstrations=False)
    # Skip tests and run only the performance benchmark
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
