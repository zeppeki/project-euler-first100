#!/usr/bin/env python3
"""
Runner for Problem 005: Smallest multiple

This module contains the execution code for Problem 005, separated from the
algorithm implementations for better test coverage and code organization.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_005 import (
    prime_factorization,
    solve_builtin,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem005Runner(BaseProblemRunner):
    """Runner for Problem 005: Smallest multiple."""

    def __init__(self) -> None:
        super().__init__("005", "Smallest multiple")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 005."""
        return [
            (1, 1),  # LCM(1) = 1
            (2, 2),  # LCM(1,2) = 2
            (3, 6),  # LCM(1,2,3) = 6
            (4, 12),  # LCM(1,2,3,4) = 12
            (5, 60),  # LCM(1,2,3,4,5) = 60
            (10, 2520),  # 問題例: LCM(1,...,10) = 2520
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 005."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
            ("標準ライブラリ解法", solve_builtin),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (20,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 005."""
        return [self._demonstrate_factorization, self._demonstrate_divisibility]

    def _demonstrate_factorization(self) -> None:
        """Demonstrate prime factorization of the result."""
        n = self.get_main_parameters()[0]
        answer = solve_optimized(n)

        print("=== 素因数分解の確認 ===")
        print(f"結果: {answer:,}")

        factors = prime_factorization(answer)
        factor_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factors])
        print(f"素因数分解: {factor_str}")

    def _demonstrate_divisibility(self) -> None:
        """Demonstrate divisibility verification."""
        n = self.get_main_parameters()[0]
        answer = solve_optimized(n)

        print("=== 除数確認 ===")
        verification_failed = False
        for i in range(1, min(n + 1, 11)):  # 表示は最初の10個まで
            if answer % i == 0:
                print(f"{answer:,} ÷ {i} = {answer // i:,} ✓")
            else:
                print(f"{answer:,} ÷ {i} = 余り{answer % i} ✗")
                verification_failed = True

        if n > 10:
            print(f"... (11から{n}まで省略)")
            for i in range(11, n + 1):
                if answer % i != 0:
                    print(f"{answer:,} ÷ {i} = 余り{answer % i} ✗")
                    verification_failed = True

        if not verification_failed:
            print("全ての数で割り切れることを確認 ✓")


def main() -> None:
    """Main entry point."""
    runner = Problem005Runner()
    runner.main()


if __name__ == "__main__":
    main()
