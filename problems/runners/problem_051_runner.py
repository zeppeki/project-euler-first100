#!/usr/bin/env python3
"""
Problem 051 Runner: Execution and demonstration code for Problem 051.

This module handles the execution and demonstration of Problem 051 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_051 import (
    get_prime_family_details,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem051Runner(BaseProblemRunner):
    """Runner for Problem 051: Prime digit replacements."""

    def __init__(self) -> None:
        super().__init__("051", "Prime digit replacements")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 051."""
        return [
            (6, 13),  # *3パターンで6個の素数族を作る最小の素数
            (7, 56003),  # 56**3パターンで7個の素数族を作る最小の素数
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 051."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (8,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 051."""
        return [self._demonstrate_prime_families]

    def _demonstrate_prime_families(self) -> None:
        """素数族の分析を表示"""
        print("素数族の例:")

        # *3パターンの例
        print("\n1. *3パターン（6個の素数族）:")
        family_details = get_prime_family_details(13, 6)
        if family_details:
            family, positions = family_details
            print("  基準数: 13")
            print(f"  置換位置: {positions}")
            print(f"  素数族: {family}")
            print(f"  族の数: {len(family)}")

        # 56**3パターンの例
        print("\n2. 56**3パターン（7個の素数族）:")
        family_details = get_prime_family_details(56003, 7)
        if family_details:
            family, positions = family_details
            print("  基準数: 56003")
            print(f"  置換位置: {positions}")
            print(f"  素数族: {family}")
            print(f"  族の数: {len(family)}")

        # メイン問題の結果
        print("\n3. 8個の素数族を作る最小の素数:")
        result = solve_optimized(8)
        if result != -1:
            family_details = get_prime_family_details(result, 8)
            if family_details:
                family, positions = family_details
                print(f"  基準数: {result}")
                print(f"  置換位置: {positions}")
                print(f"  素数族: {family}")
                print(f"  族の数: {len(family)}")

                # パターン分析
                pattern = str(result)
                pattern_display = list(pattern)
                for pos in positions:
                    if pos < len(pattern_display):
                        pattern_display[pos] = "*"
                print(f"  パターン: {''.join(pattern_display)}")
        else:
            print("  結果が見つかりませんでした")


def main() -> None:
    """メイン関数"""
    runner = Problem051Runner()
    runner.main()


if __name__ == "__main__":
    main()
