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

    def __init__(self) -> None:
        super().__init__("004", "Largest palindrome product")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 004."""
        return [
            (1, 1, (9, 3, 3)),  # 1桁の場合: 3 * 3 = 9
            (2, 2, (9009, 91, 99)),  # 2桁の場合: 91 * 99 = 9009
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

    def run_tests(self) -> bool:
        """Run custom test cases for Problem 004."""
        test_cases = self.get_test_cases()
        functions = self.get_solution_functions()

        if not test_cases or not functions:
            print("警告: テストケースまたは解法関数が定義されていません")
            return False

        print("=== テストケース ===")
        all_passed = True

        for test_case in test_cases:
            min_digits, max_digits, expected = test_case
            expected_palindrome, expected_factor1, expected_factor2 = expected

            print(f"Digits: {min_digits}-{max_digits}")
            print(
                f"  Expected: {expected_palindrome} = "
                f"{expected_factor1} × {expected_factor2}"
            )

            for name, func in functions:
                try:
                    result = func(min_digits, max_digits)
                    palindrome = result[0]
                    status = "✓" if palindrome == expected_palindrome else "✗"
                    print(f"  {name}: {result[0]} = {result[1]} × {result[2]} {status}")
                    if palindrome != expected_palindrome:
                        all_passed = False
                except Exception as e:
                    print(f"  {name}: エラー - {e}")
                    all_passed = False

            print()

        return all_passed


def main() -> None:
    """Main entry point."""
    runner = Problem004Runner()
    runner.main()


if __name__ == "__main__":
    main()
