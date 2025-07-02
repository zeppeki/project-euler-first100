#!/usr/bin/env python3
"""
Problem 016 Runner: Execution and demonstration code for Problem 016.

This module handles the execution and demonstration of Problem 016 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_016 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem016Runner(BaseProblemRunner):
    """Runner for Problem 016: Power Digit Sum."""

    def __init__(self) -> None:
        super().__init__("016", "Power Digit Sum")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 016."""
        return [
            (15, 26),  # 2^15 = 32768 → 3+2+7+6+8 = 26
            (10, 7),  # 2^10 = 1024 → 1+0+2+4 = 7
            (5, 5),  # 2^5 = 32 → 3+2 = 5
            (0, 1),  # 2^0 = 1 → 1 = 1
            (1, 2),  # 2^1 = 2 → 2 = 2
            (2, 4),  # 2^2 = 4 → 4 = 4
            (3, 8),  # 2^3 = 8 → 8 = 8
            (4, 7),  # 2^4 = 16 → 1+6 = 7
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 016."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000,)

    def get_demonstration_functions(self) -> list[tuple[str, Callable[[], None]]]:
        """Get demonstration functions for Problem 016."""
        return [("2の冪乗の桁数分析", self._demonstrate_power_analysis)]

    def _demonstrate_power_analysis(self) -> None:
        """2の冪乗の桁数分析を表示"""
        power = 1000
        result = solve_optimized(power)

        print(f"2^{power} の桁の和: {result}")

        print("\n2の小さな冪乗の桁数と桁の和:")
        for i in range(1, 21):
            value = 2**i
            digit_sum = sum(int(digit) for digit in str(value))
            print(
                f"2^{i:2d} = {value:>6} → 桁数: {len(str(value)):2d}, 桁の和: {digit_sum:2d}"
            )

        print(f"\n2^{power} の詳細:")
        large_value = 2**power
        print(f"桁数: {len(str(large_value))}")
        print(f"最初の20桁: {str(large_value)[:20]}...")
        print(f"最後の20桁: ...{str(large_value)[-20:]}")


def main() -> None:
    """メイン関数"""
    runner = Problem016Runner()
    runner.main()


if __name__ == "__main__":
    main()
