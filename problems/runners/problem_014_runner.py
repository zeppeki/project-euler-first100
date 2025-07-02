#!/usr/bin/env python3
"""
Problem 014 Runner: Execution and demonstration code for Problem 014.

This module handles the execution and demonstration of Problem 014 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_014 import (
    collatz_length_simple,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem014Runner(BaseProblemRunner):
    """Runner for Problem 014: Longest Collatz sequence."""

    def __init__(self) -> None:
        super().__init__("014", "Longest Collatz sequence")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 014."""
        return [
            (2, 1),  # 1のみ
            (3, 2),  # 1, 2
            (5, 3),  # 1, 2, 3, 4 -> 3が最長(8ステップ)
            (10, 9),  # 9が最長(20ステップ)
            (14, 9),  # 13も9も同じ長さだが9の方が小さい番号
            (20, 18),  # 18が最長(21ステップ) - 18と19は同じ長さだが18が小さい
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 014."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000000,)

    def get_demonstration_functions(self) -> list[tuple[str, Callable[[], None]]]:
        """Get demonstration functions for Problem 014."""
        return [("コラッツ数列の分析", self._demonstrate_collatz_analysis)]

    def _demonstrate_collatz_analysis(self) -> None:
        """コラッツ数列の分析を表示"""
        longest_num = solve_optimized(1000000)
        chain_length = collatz_length_simple(longest_num)

        print(f"最長チェーンの開始数: {longest_num:,}")
        print(f"チェーンの長さ: {chain_length}")

        print("\n最初の20個の数のチェーン長:")
        for i in range(1, 21):
            length = collatz_length_simple(i)
            print(f"{i}: {length}")

        print("\n特別な例 - 13の完全なチェーン:")
        n = 13
        sequence = []
        while n != 1:
            sequence.append(n)
            n = n * 3 + 1 if n % 2 == 1 else n // 2
        sequence.append(1)
        print(f"13 → {'→ '.join(map(str, sequence[:10]))}... (長さ: {len(sequence)})")


def main() -> None:
    """メイン関数"""
    runner = Problem014Runner()
    runner.main()


if __name__ == "__main__":
    main()
