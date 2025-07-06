#!/usr/bin/env python3
"""
Problem 062 Runner: Execution and demonstration code for Problem 062.

This module handles the execution and demonstration of Problem 062 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_062 import get_digit_signature, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem062Runner(BaseProblemRunner):
    """Runner for Problem 062: Cubic permutations."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "062",
            "Cubic permutations",
            127035954683,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 062."""
        # Test the digit signature function with known examples
        test_signature_1 = get_digit_signature(41063625)  # 345³
        test_signature_2 = get_digit_signature(56623104)  # 384³
        test_signature_3 = get_digit_signature(66430125)  # 405³

        # These should all have the same signature since they're permutations
        assert test_signature_1 == test_signature_2 == test_signature_3
        print("桁順列の検証テストが完了しました")
        return []

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 062."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()


def main() -> None:
    """メイン関数"""
    runner = Problem062Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem062Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
