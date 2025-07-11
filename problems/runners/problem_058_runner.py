#!/usr/bin/env python3
"""
Problem 058 Runner: Execution and demonstration code for Problem 058.

This module handles the execution and demonstration of Problem 058 solutions,
separated from the core algorithm implementations.
"""

import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from problems.problem_058 import (
    calculate_prime_ratio,
    count_primes_in_diagonals,
    get_all_diagonal_values,
    get_diagonal_values,
    is_prime,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem058Runner(BaseProblemRunner):
    """Runner for Problem 058: Spiral primes."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "058", "Spiral primes", 0, enable_performance_test, enable_demonstrations
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 058."""
        return [
            (0.5, 5),  # 辺の長さ5で素数比率が50%未満
            (0.3, 9),  # 辺の長さ9で素数比率が30%未満
            (0.2, 11),  # 辺の長さ11で素数比率が20%未満
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 058."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (0.1,)  # 10%未満の比率を探す

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 058."""
        return [
            self._demonstrate_spiral_pattern,
            self._demonstrate_layer_analysis,
            self._demonstrate_example_verification,
        ]

    def _demonstrate_spiral_pattern(self) -> None:
        """スパイラルパターンの分析を表示"""
        print("スパイラルパターンの分析 (辺の長さ 1-21):")
        print("=" * 60)

        print(
            f"{'辺の長さ':>6} {'対角線数':>8} {'素数':>6} {'総数':>6} {'比率':>10} {'パーセント':>10}"
        )
        print("-" * 60)

        for side_length in range(1, 22, 2):
            diagonal_values = get_all_diagonal_values(side_length)
            prime_count, total_count = count_primes_in_diagonals(side_length)
            ratio = prime_count / total_count if total_count > 0 else 0.0
            percentage = ratio * 100

            print(
                f"{side_length:>6} {len(diagonal_values):>8} {prime_count:>6} {total_count:>6} {ratio:>10.4f} {percentage:>9.2f}%"
            )

    def _demonstrate_layer_analysis(self) -> None:
        """各層の詳細分析を表示"""
        print("\n各層の詳細分析:")
        print("=" * 50)

        for side_length in [3, 5, 7, 9, 11]:
            if side_length == 1:
                diagonal_values = [1]
                primes = []
                non_primes = [1]
                prime_status = [False]
                layer = 0
            else:
                diagonal_values = get_diagonal_values(side_length)
                prime_status = [is_prime(value) for value in diagonal_values]
                primes = [value for value in diagonal_values if is_prime(value)]
                non_primes = [value for value in diagonal_values if not is_prime(value)]
                layer = (side_length - 1) // 2

            print(f"\n辺の長さ {side_length} (層 {layer}):")
            print(f"  対角線の値: {diagonal_values}")
            print(f"  素数: {primes}")
            print(f"  非素数: {non_primes}")
            print(f"  素数状態: {prime_status}")

            # 現在の辺の長さまでの総比率
            prime_count, total_count = count_primes_in_diagonals(side_length)
            ratio = calculate_prime_ratio(side_length)
            print(
                f"  累積比率: {prime_count}/{total_count} = {ratio:.4f} ({ratio * 100:.2f}%)"
            )

    def _demonstrate_example_verification(self) -> None:
        """問題例の検証を表示"""
        print("\n問題例の検証:")
        print("=" * 30)

        # 辺の長さ7のスパイラルを検証
        side_length = 7
        diagonal_values = get_all_diagonal_values(side_length)

        # 素数の数をカウント
        prime_count = sum(
            1 for value in diagonal_values if value > 1 and is_prime(value)
        )
        expected_prime_count = 8  # 問題文では8個の素数

        if prime_count == expected_prime_count:
            print("✓ 辺の長さ7のスパイラル検証: 成功")

            # 詳細を表示
            prime_count, total_count = count_primes_in_diagonals(7)
            ratio = calculate_prime_ratio(7)

            print(f"  対角線上の素数: {prime_count}個")
            print(f"  対角線上の総数: {total_count}個")
            print(f"  素数比率: {ratio:.4f} ({ratio * 100:.2f}%)")

            # 問題文の例: 8/13 ≈ 62%
            expected_ratio = 8 / 13
            print(f"  期待比率: {expected_ratio:.4f} ({expected_ratio * 100:.2f}%)")

            if abs(ratio - expected_ratio) < 0.001:
                print("  ✓ 問題文の例と一致")
            else:
                print("  ✗ 問題文の例と不一致")
        else:
            print("✗ 辺の長さ7のスパイラル検証: 失敗")


def main() -> None:
    """メイン関数"""
    runner = Problem058Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem058Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
