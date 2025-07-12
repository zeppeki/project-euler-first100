#!/usr/bin/env python3
"""
Problem 021 Runner: Execution and demonstration code for Problem 021.

This module handles the execution and demonstration of Problem 021 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_021 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem021Runner(BaseProblemRunner):
    """Runner for Problem 021: Amicable Numbers."""

    def __init__(
        self,
        enable_performance_test: bool = False,
        enable_demonstrations: bool = False,
    ) -> None:
        super().__init__(
            "021",
            "Amicable Numbers",
            31626,
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 021."""
        return [
            # Test case 1: Small limit that includes the known amicable pair (220, 284)
            (300,),
            # Test case 2: Larger test case
            (1000,),
            # Test case 3: Main problem
            (10000,),
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 021."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (10000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 021."""
        return None


def main() -> None:
    """メイン関数"""
    runner = Problem021Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 021."""
    print("=== Problem 021 Performance Benchmark ===")
    runner = Problem021Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
