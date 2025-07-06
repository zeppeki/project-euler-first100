#!/usr/bin/env python3
"""
Problem 057 Runner: Square root convergents

This runner provides test cases, performance analysis, and demonstrations
for the square root convergents problem.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_057 import (
    analyze_convergent_pattern,
    demonstrate_convergence,
    find_digit_difference_pattern,
    get_convergent_sequence,
    get_large_convergents,
    solve_naive,
    solve_optimized,
    verify_known_convergents,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem057Runner(BaseProblemRunner):
    """Runner for Problem 057: Square root convergents"""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "057",
            "Square root convergents",
            153,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Test cases for square root convergents problem"""
        return [
            # Test with smaller limits to verify algorithm
            (10, 1),  # First 10 convergents: only 8th has more digits in numerator
            (50, 7),  # First 50 convergents
            (100, 15),  # First 100 convergents
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for performance comparison"""
        return [
            ("solve_naive", solve_naive),
            ("solve_optimized", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Parameters for main problem execution"""
        return (1000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Demonstration functions for square root convergents analysis"""
        return [
            self.demonstrate_convergents,
            self.demonstrate_convergence_pattern,
            self.demonstrate_digit_patterns,
        ]

    def demonstrate_convergents(self) -> None:
        """Demonstrate the first few convergents of √2"""
        print("=== √2の近似分数のデモンストレーション ===")

        convergents = get_convergent_sequence(15)

        print("最初の15個の近似分数:")
        print("n  | 分数     | 小数値    | 分子桁数 | 分母桁数 | 分子>分母")
        print("---|----------|-----------|----------|----------|----------")

        for c in convergents:
            fraction_str = f"{c['numerator']}/{c['denominator']}"
            status = "✓" if c["has_more_digits"] else " "
            print(
                f"{c['n']:2d} | {fraction_str:8s} | {c['decimal_value']:.6f} | "
                f"{c['numerator_digits']:8d} | {c['denominator_digits']:8d} | {status:8s}"
            )

        # 8番目の近似分数が最初の例であることを強調
        print("\n第8近似分数 (1393/985) が分子の桁数が分母を上回る最初の例です")

    def demonstrate_convergence_pattern(self) -> None:
        """Demonstrate convergence to √2"""
        print("=== √2への収束パターン ===")

        demonstrations = demonstrate_convergence()

        import math

        sqrt2 = math.sqrt(2)
        print(f"√2の実際の値: {sqrt2:.10f}")
        print()

        print("近似分数と誤差:")
        print("n  | 分数表記   | 小数値      | 誤差        | 桁数比較")
        print("---|------------|-------------|-------------|----------")

        for demo in demonstrations[:10]:
            status = "分子>分母" if demo["has_more_digits"] else "分子≤分母"
            print(
                f"{demo['n']:2d} | {demo['fraction_str']:10s} | "
                f"{demo['decimal_value']:.8f} | {demo['error_scientific']:9s} | {status}"
            )

    def demonstrate_digit_patterns(self) -> None:
        """Demonstrate patterns in digit counts"""
        print("=== 桁数のパターン分析 ===")

        # 100個の近似分数を分析
        analysis = analyze_convergent_pattern(100)

        print("分析範囲: 最初の100個の近似分数")
        print(f"分子の桁数が分母を上回る個数: {analysis['more_digits_count']}")
        print(f"割合: {analysis['more_digits_count'] / 100 * 100:.1f}%")

        print("\n分子>分母となる位置 (最初の20個):")
        positions = analysis["more_digits_positions"][:20]
        for i, pos in enumerate(positions):
            if i > 0 and i % 10 == 0:
                print()
            print(f"{pos:3d}", end=" ")
        print()

        # 桁数の分布
        print("\n分子の桁数分布:")
        num_dist = analysis["numerator_digit_distribution"]
        for digits in sorted(num_dist.keys())[:10]:
            count = num_dist[digits]
            print(f"  {digits}桁: {count}個")

        # 桁数の差のパターン
        diff_analysis = find_digit_difference_pattern(50)
        print("\n桁数の差の分布 (分子桁数 - 分母桁数):")
        diff_dist = diff_analysis["difference_distribution"]
        for diff in sorted(diff_dist.keys()):
            count = diff_dist[diff]
            if diff > 0:
                print(f"  +{diff}: {count}個 (分子>分母)")
            elif diff == 0:
                print(f"   {diff}: {count}個 (分子=分母)")
            else:
                print(f"  {diff}: {count}個 (分子<分母)")

    def demonstrate_large_convergents(self) -> None:
        """Demonstrate large convergents (for very large n)"""
        print("=== 大きなnでの近似分数 ===")

        large_convergents = get_large_convergents(990, 10)

        print("n=990から999までの近似分数:")
        print("n   | 分子桁数 | 分母桁数 | 分子>分母")
        print("----|----------|----------|----------")

        for conv in large_convergents:
            status = "✓" if conv["has_more_digits"] else " "
            print(
                f"{conv['n']:3d} | {conv['numerator_digits']:8d} | "
                f"{conv['denominator_digits']:8d} | {status:8s}"
            )

        print("\n例: n=990の分子 (最初と最後の20桁):")
        example = large_convergents[0]
        print(f"    {example['numerator_display']}")
        print(f"    ({example['numerator_digits']}桁)")


def main() -> None:
    """Main execution function"""
    # Verify known convergents first
    if not verify_known_convergents():
        print("警告: 既知の近似分数の検証に失敗しました")
        return

    # Run the problem
    runner = Problem057Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem057Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
