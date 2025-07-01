#!/usr/bin/env python3
"""
Problem 007 Runner: 10001st prime

実行・表示・パフォーマンス測定を担当
"""

import math
from collections.abc import Callable
from typing import Any

from problems.problem_007 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem007Runner(BaseProblemRunner):
    """Runner for Problem 007: 10001st prime."""

    def __init__(self) -> None:
        super().__init__("007", "10001st prime")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 007."""
        return [
            (1, 2),  # 1番目の素数は2
            (2, 3),  # 2番目の素数は3
            (3, 5),  # 3番目の素数は5
            (4, 7),  # 4番目の素数は7
            (5, 11),  # 5番目の素数は11
            (6, 13),  # 6番目の素数は13（問題例）
            (10, 29),  # 10番目の素数は29
            (25, 97),  # 25番目の素数は97
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 007."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (10001,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 007."""
        return [
            self._show_prime_sequence,
            self._show_approximation,
            self._show_algorithm_comparison,
        ]

    def _show_prime_sequence(self) -> None:
        """Show the first 10 primes."""
        print("=== 計算過程の詳細 ===")
        print("最初の10個の素数:")
        primes = []
        for i in range(1, 11):
            prime = solve_optimized(i)
            primes.append(prime)
            print(f"{i:2d}番目: {prime}")

        print(f"\n素数列: {', '.join(map(str, primes))}")

    def _show_approximation(self) -> None:
        """Show prime number theorem approximation."""
        n = self.get_main_parameters()[0]

        if n >= 6:
            approx = n * (math.log(n) + math.log(math.log(n)))
            print("=== 素数定理による近似 ===")
            print(f"{n}番目の素数の近似上限: {approx:.0f}")
            print("実際の値と比較することで精度を確認できます")

    def _show_algorithm_comparison(self) -> None:
        """Show algorithm comparison."""
        print("=== アルゴリズムの特徴 ===")
        print("1. 素直な解法: 各数を順次素数判定")
        print("2. 最適化解法: エラトステネスの篩で効率的に素数生成")
        print("3. 数学的解法: 6k±1の形の数のみをチェックして効率化")


def main() -> None:
    """Main entry point."""
    runner = Problem007Runner()
    runner.main()


if __name__ == "__main__":
    main()
