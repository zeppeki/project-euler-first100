#!/usr/bin/env python3
"""
Problem 039 Runner: Execution and demonstration code for Problem 039.

This module handles the execution and demonstration of Problem 039 solutions,
separated from the core algorithm implementations.
"""

import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from problems.runners.base_runner import BaseProblemRunner


class Problem039Runner(BaseProblemRunner):
    """Runner for Problem 039: Integer right triangles."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "039",
            "Integer right triangles",
            problem_answer=840,  # Known answer for value of p ≤ 1000 with maximum number of solutions
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

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

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get optional demonstration functions for complex analysis."""
        return None


def main() -> None:
    """Main entry point."""
    # デフォルト実行（パフォーマンステストのみ無効、デモンストレーションは有効）
    runner = Problem039Runner(enable_demonstrations=True)
    runner.main()


def run_with_all_features() -> None:
    """Run with all features enabled for demonstration."""
    print("=== 全機能有効 ===")
    runner = Problem039Runner(enable_performance_test=True, enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 039."""
    print("=== Problem 039 Performance Benchmark ===")
    runner = Problem039Runner(enable_performance_test=True, enable_demonstrations=False)
    # Skip tests and run only the performance benchmark
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
