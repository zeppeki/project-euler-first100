#!/usr/bin/env python3
"""
Problem 048 Runner: Execution and demonstration code for Problem 048.

This module handles the execution and demonstration of Problem 048 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_048 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem048Runner(BaseProblemRunner):
    """Runner for Problem 048: Self powers."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "048",
            "Self powers",
            9110846700,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 048."""
        return [
            (1, 1),  # 1^1 = 1 (mod 10^10)
            (2, 5),  # 1^1 + 2^2 = 5 (mod 10^10)
            (3, 32),  # 1^1 + 2^2 + 3^3 = 32 (mod 10^10)
            (4, 288),  # 1^1 + 2^2 + 3^3 + 4^4 = 288 (mod 10^10)
            (10, 405071317),  # Example from problem statement
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 048."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 048."""
        from problems.problem_048 import calculate_self_powers_sum

        def demonstrate_self_powers() -> None:
            """自己累乗の計算例を表示"""
            print("自己累乗の例:")
            for i in range(1, 11):
                self_power = pow(i, i)
                print(f"  {i}^{i} = {self_power:,}")

        def demonstrate_modular_arithmetic() -> None:
            """モジュラー算術の例を表示"""
            print("モジュラー算術 (下10桁の計算):")

            print("小さな例:")
            for limit in [5, 10]:
                full_sum = calculate_self_powers_sum(limit)
                mod_sum = solve_optimized(limit)
                print(f"  limit={limit}: 完全計算={full_sum:,}, mod計算={mod_sum}")

        def demonstrate_large_numbers() -> None:
            """大きな数の例を表示"""
            print("大きな自己累乗数の例:")
            examples = [10, 50, 100]

            for base in examples:
                # 自己累乗が非常に大きくなることを示す
                if base <= 20:  # 計算可能な範囲
                    result = pow(base, base)
                    digits = len(str(result))
                    print(f"  {base}^{base} = {result:,} ({digits}桁)")
                else:
                    # 桁数のみ推定
                    import math

                    digits = int(base * math.log10(base)) + 1
                    print(f"  {base}^{base} は約{digits}桁の数")

        return [
            demonstrate_self_powers,
            demonstrate_modular_arithmetic,
            demonstrate_large_numbers,
        ]


def main() -> None:
    """メイン関数"""
    runner = Problem048Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem048Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
