#!/usr/bin/env python3
"""
Problem 045 Runner: Execution and demonstration code for Problem 045.

This module handles the execution and demonstration of Problem 045 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_045 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem045Runner(BaseProblemRunner):
    """Runner for Problem 045: Triangular, pentagonal, and hexagonal."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "045",
            "Triangular, pentagonal, and hexagonal",
            1533776805,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 045."""
        return []  # No specific test cases for this problem

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 045."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 045."""
        from problems.lib import generate_pentagonal
        from problems.problem_045 import (
            generate_hexagonal,
            generate_triangle,
            is_hexagonal,
            is_pentagonal,
            is_triangle,
        )

        def demonstrate_number_generation() -> None:
            """各数列の生成を表示"""
            print("数列の生成:")
            print("最初の10個の三角数:")
            for i in range(1, 11):
                tri = generate_triangle(i)
                print(f"  T{i} = {tri}")

            print("\n最初の10個の五角数:")
            for i in range(1, 11):
                pent = generate_pentagonal(i)
                print(f"  P{i} = {pent}")

            print("\n最初の10個の六角数:")
            for i in range(1, 11):
                hex_num = generate_hexagonal(i)
                print(f"  H{i} = {hex_num}")

        def demonstrate_number_detection() -> None:
            """数の判定を表示"""
            print("\n数の判定テスト:")
            test_numbers = [1, 3, 6, 10, 15, 28, 36, 45, 40755]
            for num in test_numbers:
                is_tri = is_triangle(num)
                is_pent = is_pentagonal(num)
                is_hex = is_hexagonal(num)
                types = []
                if is_tri:
                    types.append("三角数")
                if is_pent:
                    types.append("五角数")
                if is_hex:
                    types.append("六角数")

                type_str = ", ".join(types) if types else "どれでもない"
                print(f"  {num}: {type_str}")

        def demonstrate_known_example() -> None:
            """既知の例を表示"""
            print("\n既知の例 (40755):")
            print(f"T285 = {generate_triangle(285)}")
            print(f"P165 = {generate_pentagonal(165)}")
            print(f"H143 = {generate_hexagonal(143)}")
            print("すべて40755と一致することを確認")

        return [
            demonstrate_number_generation,
            demonstrate_number_detection,
            demonstrate_known_example,
        ]


def main() -> None:
    """メイン関数"""
    runner = Problem045Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem045Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
