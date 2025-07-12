#!/usr/bin/env python3
"""
Problem 022 Runner: Execution and demonstration code for Problem 022.

This module handles the execution and demonstration of Problem 022 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_022 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem022Runner(BaseProblemRunner):
    """Runner for Problem 022: Names Scores."""

    def __init__(
        self,
        enable_performance_test: bool = False,
        enable_demonstrations: bool = False,
    ) -> None:
        super().__init__(
            "022",
            "Names Scores",
            871198282,
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 022."""
        # Simple test case with sample names
        sample_names = ["MARY", "PATRICIA", "LINDA", "BARBARA", "COLIN"]
        return [
            # Test case 1: Small sample for testing
            (sample_names,),
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 022."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        # Load names from data file for main problem
        from problems.lib.file_io import load_names_file

        names = load_names_file("p022_names.txt")
        return (names,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 022."""
        return None


def main() -> None:
    """メイン関数"""
    runner = Problem022Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 022."""
    print("=== Problem 022 Performance Benchmark ===")
    runner = Problem022Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
