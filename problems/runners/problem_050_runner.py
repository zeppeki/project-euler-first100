#!/usr/bin/env python3
"""
Problem 050 Runner: Execution and demonstration code for Problem 050.

This module handles the execution and demonstration of Problem 050 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_050 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem050Runner(BaseProblemRunner):
    """Runner for Problem 050: Consecutive prime sum."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "050",
            "Consecutive prime sum",
            997651,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 050."""
        return [
            (100, 41),  # Example from problem: sum of first 6 consecutive primes
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 050."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 050."""
        from problems.lib import generate_primes, is_prime

        def demonstrate_consecutive_prime_sums() -> None:
            """連続する素数の和の例を表示"""
            print("連続する素数の和の例:")
            primes = generate_primes(100)

            # 最初の数個の連続する素数の和を計算
            for length in range(2, 7):
                consecutive_sum = sum(primes[:length])
                is_prime_result = is_prime(consecutive_sum)
                prime_list = " + ".join(map(str, primes[:length]))
                status = "素数" if is_prime_result else "合成数"
                print(f"  {prime_list} = {consecutive_sum} ({status})")

        def demonstrate_problem_example() -> None:
            """問題の例を表示"""
            print("問題の例 (限界値100):")
            primes = generate_primes(100)

            # 41 = 2 + 3 + 5 + 7 + 11 + 13 (6つの連続する素数)
            example_primes = primes[:6]
            example_sum = sum(example_primes)
            prime_list = " + ".join(map(str, example_primes))

            print(f"  最長の連続する素数の和: {prime_list} = {example_sum}")
            print(f"  これは{len(example_primes)}個の連続する素数の和")

        def demonstrate_longer_sequences() -> None:
            """より長い連続する素数の和を表示"""
            print("より長い連続する素数の和:")
            primes = generate_primes(1000)

            # いくつかの長い連続する素数の和を計算
            test_lengths = [10, 20, 50]
            for length in test_lengths:
                if length <= len(primes):
                    consecutive_sum = sum(primes[:length])
                    is_prime_result = is_prime(consecutive_sum)
                    status = "素数" if is_prime_result else "合成数"
                    print(f"  最初の{length}個の素数の和: {consecutive_sum} ({status})")

        return [
            demonstrate_consecutive_prime_sums,
            demonstrate_problem_example,
            demonstrate_longer_sequences,
        ]


def main() -> None:
    """メイン関数"""
    runner = Problem050Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem050Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
