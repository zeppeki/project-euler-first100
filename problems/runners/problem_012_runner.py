#!/usr/bin/env python3
"""
Problem 012 Runner: Execution and demonstration code for Problem 012.

This module handles the execution and demonstration of Problem 012 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_012 import (
    count_divisors_optimized,
    get_divisors,
    get_triangular_number,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem012Runner(BaseProblemRunner):
    """Runner for Problem 012: Highly divisible triangular number."""

    def __init__(self) -> None:
        super().__init__("012", "Highly divisible triangular number")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 012."""
        return [
            (0, 1),  # 0個より多い約数を持つ最初の三角数は1
            (1, 3),  # 1個より多い約数を持つ最初の三角数は3
            (2, 6),  # 2個より多い約数を持つ最初の三角数は6
            (3, 6),  # 3個より多い約数を持つ最初の三角数は6
            (4, 28),  # 4個より多い約数を持つ最初の三角数は28
            (5, 28),  # 5個より多い約数を持つ最初の三角数は28（問題例）
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 012."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (500,)

    def get_demonstration_functions(self) -> list[tuple[str, Callable[[], None]]]:
        """Get demonstration functions for Problem 012."""
        return [("三角数と約数の分析", self._demonstrate_triangular_analysis)]

    def _demonstrate_triangular_analysis(self) -> None:
        """三角数と約数の分析を表示"""
        triangular_num = solve_optimized(500)
        n = 1
        while get_triangular_number(n) != triangular_num:
            n += 1

        divisor_count = count_divisors_optimized(triangular_num)
        print(f"{n}番目の三角数: {triangular_num:,}")
        print(f"約数の個数: {divisor_count}")
        print(f"三角数公式検証: {n} * ({n} + 1) / 2 = {n * (n + 1) // 2:,}")

        print("\n最初の10個の三角数と約数の個数:")
        for i in range(1, 11):
            triangular = get_triangular_number(i)
            divisor_count = count_divisors_optimized(triangular)
            divisors = get_divisors(triangular)
            print(f"T_{i} = {triangular}, divisors: {len(divisors)} {divisors}")


def main() -> None:
    """メイン関数"""
    runner = Problem012Runner()
    runner.main()


if __name__ == "__main__":
    main()
