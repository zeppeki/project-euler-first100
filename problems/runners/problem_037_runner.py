#!/usr/bin/env python3
"""
Problem 037 Runner: Execution and demonstration code for Problem 037.

This module handles the execution and demonstration of Problem 037 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_037 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem037Runner(BaseProblemRunner):
    """Runner for Problem 037: Truncatable primes."""

    def __init__(
        self,
        enable_performance_test: bool = False,
        enable_demonstrations: bool = False,
    ) -> None:
        super().__init__(
            "037",
            "Truncatable primes",
            748317,
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 037."""
        return [
            # Add appropriate test cases based on problem requirements
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 037."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()  # Add appropriate parameters

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 037."""
        return None


def main() -> None:
    """メイン関数"""
    runner = Problem037Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 037."""
    print("=== Problem 037 Performance Benchmark ===")
    runner = Problem037Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
