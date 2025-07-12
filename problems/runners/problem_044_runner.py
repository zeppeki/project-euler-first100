#!/usr/bin/env python3
"""
Problem 044 Runner: Execution and demonstration code for Problem 044.

This module handles the execution and demonstration of Problem 044 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_044 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem044Runner(BaseProblemRunner):
    """Runner for Problem 044: Pentagon numbers."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "044",
            "Pentagon numbers",
            5482660,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 044."""
                return [
            # Test case: Main problem parameters
            ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 044."""
        from problems.problem_044 import generate_pentagonal, is_pentagonal

        def demonstrate_pentagonal_numbers() -> None:
            """五角数の生成とテスト"""
            print("五角数の生成と検証:")
            print("最初の10個の五角数:")
            for i in range(1, 11):
                pent = generate_pentagonal(i)
                print(f"  P{i,
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 044."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 044."""
        from problems.problem_044 import generate_pentagonal, is_pentagonal

        def demonstrate_pentagonal_numbers() -> None:
            """五角数の生成とテスト"""
            print("五角数の生成と検証:")
            print("最初の10個の五角数:")
            for i in range(1, 11):
                pent = generate_pentagonal(i)
                print(f"  P{i} = {pent}")

            print("\n五角数判定テスト:")
            test_numbers = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 2, 6, 13, 23, 36]
            for num in test_numbers:
                is_pent = is_pentagonal(num)
                print(f"  {num}: {'五角数' if is_pent else '五角数ではない'}")

        def demonstrate_problem_example() -> None:
            """問題の例を表示"""
            print("\n問題の例:")
            p4, p7, p8 = 22, 70, 92
            print(f"P4 = {p4}, P7 = {p7}, P8 = {p8}")
            print(f"P4 + P7 = {p4 + p7} = {p8} (P8と一致)")
            print(f"P7 - P4 = {p7 - p4} = 48")
            print(f"48は五角数？: {is_pentagonal(48)}")

        return [demonstrate_pentagonal_numbers, demonstrate_problem_example]


def main() -> None:
    """メイン関数"""
    runner = Problem044Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem044Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
