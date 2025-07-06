#!/usr/bin/env python3
"""
Problem 046 Runner: Execution and demonstration code for Problem 046.

This module handles the execution and demonstration of Problem 046 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_046 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem046Runner(BaseProblemRunner):
    """Runner for Problem 046: Goldbach's other conjecture."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "046",
            "Goldbach's other conjecture",
            5777,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 046."""
        return [
            (6000, 5777),  # 最初の反例が5777であることを確認
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 046."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (10000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 046."""
        from problems.problem_046 import (
            can_be_written_as_conjecture,
            generate_primes,
            is_perfect_square,
            is_prime,
        )

        def demonstrate_conjecture_examples() -> None:
            """ゴールドバッハの他の予想の例を表示"""
            print("ゴールドバッハの他の予想の例:")
            examples = [9, 15, 21, 25, 27, 33]
            primes = generate_primes(100)

            for num in examples:
                if num % 2 == 1 and not is_prime(num):
                    can_write = can_be_written_as_conjecture(num, primes)
                    status = "成り立つ" if can_write else "成り立たない"
                    print(f"{num}: {status}")

                    if can_write:
                        # 具体的な分解例を表示
                        for prime in primes:
                            if prime >= num:
                                break
                            remainder = num - prime
                            if remainder > 0 and remainder % 2 == 0:
                                k_squared = remainder // 2
                                if is_perfect_square(k_squared):
                                    import math

                                    k = int(math.sqrt(k_squared))
                                    print(f"  {num} = {prime} + 2×{k}²")
                                    break

        def demonstrate_prime_generation() -> None:
            """素数生成のデモンストレーション"""
            print("素数生成 (最初の20個):")
            primes = generate_primes(100)
            print(f"最初の20個の素数: {primes[:20]}")

        def demonstrate_perfect_squares() -> None:
            """完全平方数判定のデモンストレーション"""
            print("完全平方数判定:")
            test_numbers = [1, 4, 9, 16, 25, 30, 36, 49, 50, 64]
            for num in test_numbers:
                is_square = is_perfect_square(num)
                print(f"{num}: {'完全平方数' if is_square else '完全平方数ではない'}")

        return [
            demonstrate_conjecture_examples,
            demonstrate_prime_generation,
            demonstrate_perfect_squares,
        ]


def main() -> None:
    """メイン関数"""
    runner = Problem046Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem046Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
