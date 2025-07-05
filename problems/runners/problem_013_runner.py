#!/usr/bin/env python3
"""
Problem 013 Runner: Execution and demonstration code for Problem 013.

This module handles the execution and demonstration of Problem 013 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_013 import (
    get_fifty_digit_numbers,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem013Runner(BaseProblemRunner):
    """Runner for Problem 013: Large sum."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "013",
            "Large sum",
            problem_answer="5537376230",  # Known answer for first 10 digits of sum
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 013."""
        # テスト用の小さな数値リスト
        test_numbers = [
            "12345678901234567890123456789012345678901234567890",
            "98765432109876543210987654321098765432109876543210",
            "11111111111111111111111111111111111111111111111111",
        ]
        expected = str(sum(int(num) for num in test_numbers))[:10]
        return [
            (test_numbers, expected),
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 013."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 013."""
        return [self._demonstrate_large_numbers]

    def _demonstrate_large_numbers(self) -> None:
        """50桁数の分析を表示"""
        numbers = get_fifty_digit_numbers()
        total = sum(int(num) for num in numbers)

        print(f"50桁の数値の個数: {len(numbers)}")
        print(f"最初の数値: {numbers[0]}")
        print(f"最後の数値: {numbers[-1]}")
        print(f"全数値の合計: {total}")
        print(f"合計の桁数: {len(str(total))}")
        print(f"上位10桁: {str(total)[:10]}")


def main() -> None:
    """Main entry point."""
    runner = Problem013Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 013."""
    print("=== Problem 013 Performance Benchmark ===")
    runner = Problem013Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
