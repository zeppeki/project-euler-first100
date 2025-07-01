#!/usr/bin/env python3
"""
Problem 006 Runner: Sum square difference

実行・表示・パフォーマンス測定を担当
"""

from collections.abc import Callable
from typing import Any

from problems.problem_006 import solve_mathematical, solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem006Runner(BaseProblemRunner):
    """Runner for Problem 006: Sum square difference."""

    def __init__(self) -> None:
        super().__init__("006", "Sum square difference")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 006."""
        return [
            (0, 0),  # n=0の場合
            (1, 0),  # n=1: 1² = 1, (1)² = 1, 差は0
            (2, 4),  # n=2: (1+2)² - (1²+2²) = 9 - 5 = 4
            (3, 22),  # n=3: (1+2+3)² - (1²+2²+3²) = 36 - 14 = 22
            (10, 2640),  # 問題例: n=10の場合
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 006."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (100,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 006."""
        return [self._show_calculation_details]

    def _show_calculation_details(self) -> None:
        """Show detailed calculation process."""
        print("=== 計算過程の詳細 ===")

        # n=10の例で詳細を表示
        example_n = 10
        print(f"例: n = {example_n}")

        # 平方の和
        sum_of_squares_example = sum(i * i for i in range(1, example_n + 1))
        print(f"平方の和: 1² + 2² + ... + {example_n}² = {sum_of_squares_example}")

        # 和の平方
        sum_of_numbers_example = sum(i for i in range(1, example_n + 1))
        square_of_sum_example = sum_of_numbers_example * sum_of_numbers_example
        print(
            f"和の平方: (1 + 2 + ... + {example_n})² = {sum_of_numbers_example}² = {square_of_sum_example}"
        )

        # 差
        difference_example = square_of_sum_example - sum_of_squares_example
        print(
            f"差: {square_of_sum_example} - {sum_of_squares_example} = {difference_example}"
        )

        # 公式の確認
        n = 100
        print(f"\n=== 公式の確認 (n={n}) ===")
        sum_formula = n * (n + 1) // 2
        sum_of_squares_formula = n * (n + 1) * (2 * n + 1) // 6
        print(f"1 + 2 + ... + {n} = {n}×{n + 1}/2 = {sum_formula}")
        print(
            f"1² + 2² + ... + {n}² = {n}×{n + 1}×{2 * n + 1}/6 = {sum_of_squares_formula}"
        )
        print(f"和の平方: {sum_formula}² = {sum_formula * sum_formula:,}")
        print(f"平方の和: {sum_of_squares_formula:,}")

        result = solve_optimized(n)
        print(
            f"差: {sum_formula * sum_formula:,} - {sum_of_squares_formula:,} = {result:,}"
        )


def main() -> None:
    """Main entry point."""
    runner = Problem006Runner()
    runner.main()


if __name__ == "__main__":
    main()
