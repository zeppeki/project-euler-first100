#!/usr/bin/env python3
"""
Runner for Problem 004: Largest palindrome product

This module contains the execution code for Problem 004, separated from the
algorithm implementations for better test coverage and code organization.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_004 import (
    is_palindrome,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem004Runner(BaseProblemRunner):
    """Runner for Problem 004: Largest palindrome product."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "004",
            "Largest palindrome product",
            problem_answer=906609,  # Known answer for 3-digit numbers
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 004."""
        return [
            (1, 1, (9, 9, 1)),  # 1桁の場合: 9 * 1 = 9
            (2, 2, (9009, 99, 91)),  # 2桁の場合: 99 * 91 = 9009
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 004."""
        return [
            ("素直な解法", lambda min_d, max_d: solve_naive(min_d, max_d)),
            ("最適化解法", lambda min_d, max_d: solve_optimized(min_d, max_d)),
            ("数学的解法", lambda min_d, max_d: solve_mathematical(min_d, max_d)),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (3, 3)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 004."""
        return [self._demonstrate_palindrome_verification]

    def _demonstrate_palindrome_verification(self) -> None:
        """Demonstrate palindrome verification for the solution."""
        min_digits, max_digits = self.get_main_parameters()
        result = solve_optimized(min_digits, max_digits)
        palindrome, factor1, factor2 = result

        print("=== 回文の検証 ===")
        print(f"数値: {palindrome}")
        print(f"文字列: {palindrome!s}")
        print(f"逆順: {str(palindrome)[::-1]}")
        print(f"回文: {'✓' if is_palindrome(palindrome) else '✗'}")
        print(f"因子: {factor1} × {factor2} = {palindrome}")


def main() -> None:
    """Main entry point."""
    runner = Problem004Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 004."""
    print("=== Problem 004 Performance Benchmark ===")
    runner = Problem004Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
