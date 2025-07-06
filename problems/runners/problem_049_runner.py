#!/usr/bin/env python3
"""
Problem 049 Runner: Execution and demonstration code for Problem 049.

This module handles the execution and demonstration of Problem 049 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_049 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem049Runner(BaseProblemRunner):
    """Runner for Problem 049: Prime permutations."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "049",
            "Prime permutations",
            296962999629,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 049."""
        return []  # No specific test cases for this problem

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 049."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 049."""
        from problems.lib import get_digit_signature, is_prime

        def demonstrate_known_example() -> None:
            """既知の例を表示"""
            print("既知の算術数列:")
            sequence = [1487, 4817, 8147]
            print(f"数列: {sequence}")

            # 素数チェック
            all_prime = all(is_prime(x) for x in sequence)
            print(f"全て素数: {'✓' if all_prime else '✗'}")

            # 算術数列チェック
            diff1 = sequence[1] - sequence[0]
            diff2 = sequence[2] - sequence[1]
            is_arithmetic = diff1 == diff2
            print(f"算術数列 (差: {diff1}): {'✓' if is_arithmetic else '✗'}")

            # 順列チェック
            signatures = [get_digit_signature(x) for x in sequence]
            are_permutations = len(set(signatures)) == 1
            print(f"相互の順列: {'✓' if are_permutations else '✗'}")

        def demonstrate_prime_checking() -> None:
            """素数判定のデモンストレーション"""
            print("素数判定テスト:")
            test_numbers = [1487, 4817, 8147, 1000, 1009, 9999]
            for num in test_numbers:
                is_prime_result = is_prime(num)
                print(f"  {num}: {'素数' if is_prime_result else '合成数'}")

        def demonstrate_digit_signatures() -> None:
            """桁の署名のデモンストレーション"""
            print("桁の署名 (順列判定):")
            test_pairs = [
                (1487, 4817),
                (4817, 8147),
                (1487, 8147),
                (1234, 4321),
                (1234, 5678),
            ]
            for a, b in test_pairs:
                sig_a = get_digit_signature(a)
                sig_b = get_digit_signature(b)
                are_permutations = sig_a == sig_b
                print(f"  {a} と {b}: {'順列' if are_permutations else '順列ではない'}")

        return [
            demonstrate_known_example,
            demonstrate_prime_checking,
            demonstrate_digit_signatures,
        ]


def main() -> None:
    """メイン関数"""
    runner = Problem049Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem049Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
