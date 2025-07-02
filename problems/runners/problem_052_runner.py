#!/usr/bin/env python3
"""
Problem 052 Runner: Execution and demonstration code for Problem 052.

This module handles the execution and demonstration of Problem 052 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_052 import (
    demonstrate_permutation_check,
    get_permuted_multiples_details,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem052Runner(BaseProblemRunner):
    """Runner for Problem 052: Permuted multiples."""

    def __init__(self) -> None:
        super().__init__("052", "Permuted multiples")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 052."""
        # Test smaller cases that we can verify manually
        return [
            (2, 125874),  # First number where x and 2x are permutations
            (3, 142857),  # First number where x, 2x, 3x are permutations
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 052."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (6,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 052."""
        return [self._demonstrate_permuted_multiples]

    def _demonstrate_permuted_multiples(self) -> None:
        """順列倍数の分析を表示"""
        print("順列倍数の例:")

        # Example from problem description
        print("\n1. 問題例（125874とその2倍）:")
        demo = demonstrate_permutation_check(125874, 251748)
        print(f"  数値1: {demo['number1']}")
        print(f"  数値2: {demo['number2']}")
        print(f"  ソート済み桁1: {demo['digits1_sorted']}")
        print(f"  ソート済み桁2: {demo['digits2_sorted']}")
        print(f"  順列かどうか: {demo['are_permutations']}")

        # Show solution for 2x case
        print("\n2. 2倍が順列になる最小の数:")
        result_2x = solve_optimized(2)
        details_2x = get_permuted_multiples_details(result_2x, 2)
        print(f"  基準数: {result_2x}")
        for multiple, value in details_2x:
            print(f"    {multiple}x = {value}")

        # Show solution for 3x case
        print("\n3. 3倍まで順列になる最小の数:")
        result_3x = solve_optimized(3)
        details_3x = get_permuted_multiples_details(result_3x, 3)
        print(f"  基準数: {result_3x}")
        for multiple, value in details_3x:
            print(f"    {multiple}x = {value}")

        # Main problem solution
        print("\n4. 6倍まで順列になる最小の数:")
        result_6x = solve_optimized(6)
        details_6x = get_permuted_multiples_details(result_6x, 6)
        print(f"  基準数: {result_6x}")
        for multiple, value in details_6x:
            sorted_digits = "".join(sorted(str(value)))
            print(f"    {multiple}x = {value} (桁ソート: {sorted_digits})")

        # Verify all have same digits
        base_digits = "".join(sorted(str(result_6x)))
        print(f"\n  検証: 全ての倍数の桁ソート = {base_digits}")
        all_same = all(
            "".join(sorted(str(value))) == base_digits for _, value in details_6x
        )
        print(f"  全て同じ桁: {all_same}")


def main() -> None:
    """メイン関数"""
    runner = Problem052Runner()
    runner.main()


if __name__ == "__main__":
    main()
