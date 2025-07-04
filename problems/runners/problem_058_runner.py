#!/usr/bin/env python3
"""
Problem 058 Runner: Execution and demonstration code for Problem 058.

This module handles the execution and demonstration of Problem 058 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_058 import (
    analyze_spiral_pattern,
    calculate_prime_ratio,
    count_primes_in_diagonals,
    get_spiral_layer_info,
    solve_naive,
    solve_optimized,
    verify_example_spiral,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem058Runner(BaseProblemRunner):
    """Runner for Problem 058: Spiral primes."""

    def __init__(self) -> None:
        super().__init__("058", "Spiral primes")

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

        analysis = analyze_spiral_pattern(21)

        print(
            f"{'辺の長さ':>6} {'対角線数':>8} {'素数':>6} {'総数':>6} {'比率':>10} {'パーセント':>10}"
        )
        print("-" * 60)

        for data in analysis:
            side_length = data["side_length"]
            prime_count = data["prime_count"]
            total_count = data["total_count"]
            ratio = data["ratio"]
            percentage = data["percentage"]

            print(
                f"{side_length:>6} {len(data['diagonal_values']):>8} {prime_count:>6} {total_count:>6} {ratio:>10.4f} {percentage:>9.2f}%"
            )

    def _demonstrate_layer_analysis(self) -> None:
        """各層の詳細分析を表示"""
        print("\n各層の詳細分析:")
        print("=" * 50)

        for side_length in [3, 5, 7, 9, 11]:
            layer_info = get_spiral_layer_info(side_length)

            print(f"\n辺の長さ {side_length} (層 {layer_info['layer']}):")
            print(f"  対角線の値: {layer_info['diagonal_values']}")
            print(f"  素数: {layer_info['primes']}")
            print(f"  非素数: {layer_info['non_primes']}")
            print(f"  素数状態: {layer_info['prime_status']}")

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
        if verify_example_spiral():
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
    runner = Problem058Runner()
    runner.main()


if __name__ == "__main__":
    main()
