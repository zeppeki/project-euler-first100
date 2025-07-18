#!/usr/bin/env python3
"""
Problem 047 Runner: Execution and demonstration code for Problem 047.

This module handles the execution and demonstration of Problem 047 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_047 import (
    get_prime_factors,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem047Runner(BaseProblemRunner):
    """Runner for Problem 047: Distinct primes factors."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "047",
            "Distinct primes factors",
            134043,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 047."""
        return [
            (2, 14),  # 最初の2つの連続数で2つの異なる素因数
            (3, 644),  # 最初の3つの連続数で3つの異なる素因数
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 047."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (4,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 047."""
        return [self._demonstrate_consecutive_factors]

    def _demonstrate_consecutive_factors(self) -> None:
        """連続数の素因数分析を表示"""
        target_factors = 4
        result = solve_optimized(target_factors)

        print(
            f"最初の{target_factors}つの連続整数（各数が{target_factors}つの異なる素因数を持つ）:"
        )
        print(f"開始数: {result}")

        # Show consecutive numbers with their factors
        for i in range(target_factors):
            num = result + i
            factors = get_prime_factors(num)
            factors_str = " × ".join(map(str, sorted(factors)))
            print(f"  {num} = {factors_str} ({len(factors)} distinct prime factors)")

        print("\n検証例 - 2つの異なる素因数を持つ最初の連続数:")
        for i in range(2):
            num = 14 + i
            factors = get_prime_factors(num)
            factors_str = " × ".join(map(str, sorted(factors)))
            print(f"  {num} = {factors_str} ({len(factors)} distinct prime factors)")

        print("\n検証例 - 3つの異なる素因数を持つ最初の連続数:")
        for i in range(3):
            num = 644 + i
            factors = get_prime_factors(num)
            factors_str = " × ".join(map(str, sorted(factors)))
            print(f"  {num} = {factors_str} ({len(factors)} distinct prime factors)")


def main() -> None:
    """メイン関数"""
    runner = Problem047Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem047Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
