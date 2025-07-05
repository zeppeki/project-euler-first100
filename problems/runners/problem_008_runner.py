#!/usr/bin/env python3
"""
Problem 008 Runner: Execution and demonstration code for Problem 008.

This module handles the execution and demonstration of Problem 008 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_008 import (
    THOUSAND_DIGIT_NUMBER,
    get_max_product_sequence,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem008Runner(BaseProblemRunner):
    """Runner for Problem 008: Largest product in a series."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "008",
            "Largest product in a series",
            problem_answer=23514624000,  # Known answer for 13 consecutive digits
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 008."""
        return [
            (1, 9),  # Single digit max is 9
            (2, 81),  # Two digits: 9×9=81
            (3, 648),  # Three digits: 9×8×9=648
            (4, 5832),  # Four digits: 9×9×8×9=5832 (problem example)
            (5, 40824),  # Five digits: 9×9×8×7×9=40824
            (6, 285768),  # Six digits: 9×9×8×7×9×7=285768
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 008."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (13,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 008."""
        return [
            self._demonstrate_number_properties,
            self._demonstrate_sequence_analysis,
            self._demonstrate_optimization_effects,
        ]

    def _demonstrate_number_properties(self) -> None:
        """Demonstrate properties of the 1000-digit number."""
        print("=== 1000桁数の性質分析 ===")
        print(f"数字の長さ: {len(THOUSAND_DIGIT_NUMBER)} 桁")
        print(f"開始部分: {THOUSAND_DIGIT_NUMBER[:50]}...")
        print(f"終了部分: ...{THOUSAND_DIGIT_NUMBER[-50:]}")

        # Digit frequency analysis
        digit_counts = {}
        for digit in "0123456789":
            digit_counts[digit] = THOUSAND_DIGIT_NUMBER.count(digit)

        print("\n各桁の出現頻度:")
        for digit in "0123456789":
            count = digit_counts[digit]
            percentage = (count / 1000) * 100
            print(f"  桁 {digit}: {count:3d}回 ({percentage:5.1f}%)")

        zero_count = digit_counts["0"]
        print(f"\nゼロの出現: {zero_count}回 (最適化で重要)")

    def _demonstrate_sequence_analysis(self) -> None:
        """Demonstrate sequence analysis for different lengths."""
        print("=== 異なる隣接桁数での最大積分析 ===")

        test_lengths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f"{'桁数':>4} {'最大積':>12} {'最大シーケンス':>15}")
        print("-" * 35)

        for length in test_lengths:
            try:
                sequence, product = get_max_product_sequence(length)
                print(f"{length:4d} {product:12,d} {sequence:>15}")
            except (ValueError, IndexError):
                print(f"{length:4d} {'N/A':>12} {'N/A':>15}")

    def _demonstrate_optimization_effects(self) -> None:
        """Demonstrate the effects of optimization techniques."""
        print("=== 最適化技法の効果分析 ===")

        # Show how zero-skipping works
        print("ゼロスキップ最適化の例:")
        sample_start = 50  # Starting position with some zeros nearby
        sample_length = 20  # Length of sample to show

        sample = THOUSAND_DIGIT_NUMBER[sample_start : sample_start + sample_length]
        print(f"位置 {sample_start}-{sample_start + sample_length - 1}: {sample}")

        # Find zeros in the sample
        zero_positions = [i for i, digit in enumerate(sample) if digit == "0"]
        if zero_positions:
            print(f"ゼロの位置: {[sample_start + pos for pos in zero_positions]}")
            print("素直な解法: 全シーケンスを計算")
            print("最適化解法: ゼロを含むシーケンスをスキップ")
        else:
            print("この範囲にはゼロがありません")

        # Show actual computation for a few adjacent digits
        print("\n隣接4桁での計算例 (問題の例):")
        target_length = 4
        max_sequence, max_product = get_max_product_sequence(target_length)

        print(f"最大積シーケンス: {max_sequence}")
        print(f"計算: {' × '.join(max_sequence)} = {max_product}")

        # Verify this is indeed 9×9×8×9=5832 from the problem
        manual_product = 1
        for digit in max_sequence:
            manual_product *= int(digit)
        print(f"検証: {manual_product} (期待値: 5832)")


def main() -> None:
    """Main entry point."""
    runner = Problem008Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 008."""
    print("=== Problem 008 Performance Benchmark ===")
    runner = Problem008Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
