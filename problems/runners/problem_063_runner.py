#!/usr/bin/env python3
"""
Problem 063 Runner: Execution and demonstration code for Problem 063.

This module handles the execution and demonstration of Problem 063 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_063 import (
    count_digits,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem063Runner(BaseProblemRunner):
    """Runner for Problem 063: Powerful digit counts."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "063",
            "Powerful digit counts",
            49,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 063."""
        # Test known examples from the problem statement
        assert count_digits(16807) == 5  # 7^5 is a 5-digit number
        assert count_digits(134217728) == 9  # 8^9 is a 9-digit number

        # Verify the examples are indeed powers
        assert 7**5 == 16807
        assert 8**9 == 134217728

        print("基本的な桁数計算と累乗の検証テストが完了しました")
        return []

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 063."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()


def main() -> None:
    """メイン関数"""
    runner = Problem063Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem063Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
