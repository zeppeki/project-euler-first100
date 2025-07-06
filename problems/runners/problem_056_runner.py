#!/usr/bin/env python3
"""
Problem 056 Runner: Powerful digit sum

This runner provides test cases, performance analysis, and demonstrations
for the powerful digit sum problem.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_056 import (
    analyze_digit_sum_patterns,
    demonstrate_special_cases,
    find_high_digit_sum_examples,
    get_digit_sum_statistics,
    solve_naive,
    solve_optimized,
    verify_examples,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem056Runner(BaseProblemRunner):
    """Runner for Problem 056: Powerful digit sum"""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "056",
            "Powerful digit sum",
            972,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Test cases for powerful digit sum problem"""
        return [
            # Test with smaller limits to verify algorithm
            (10, 10, 45),  # Known max for a,b < 10: 9^7 gives digit sum 45
            (20, 20, 127),  # Known max for a,b < 20: 19^19 gives digit sum 127
            (50, 50, 406),  # Known max for a,b < 50
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for performance comparison"""
        return [
            ("solve_naive", solve_naive),
            ("solve_optimized", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Parameters for main problem execution"""
        return (100, 100)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Demonstration functions for powerful digit sum analysis"""
        return [
            self.demonstrate_special_cases,
            self.demonstrate_high_digit_sums,
            self.demonstrate_statistics,
        ]

    def demonstrate_special_cases(self) -> None:
        """Demonstrate special cases from the problem"""
        print("=== 特別なケースのデモンストレーション ===")

        special_cases = demonstrate_special_cases()

        for case in special_cases:
            print(f"\n{case['description']}: {case['a']}^{case['b']}")
            print(f"  桁数: {case['power_length']:,}")
            print(f"  桁数の合計: {case['digit_sum']}")
            print(f"  数値: {case['power_display']}")

    def demonstrate_high_digit_sums(self) -> None:
        """Demonstrate numbers with high digit sums"""
        print("=== 高い桁数の合計を持つ例 ===")

        # Find examples with digit sum >= 800
        high_examples = find_high_digit_sum_examples(100, 100, 800)

        print(f"桁数の合計が800以上の組み合わせ: {len(high_examples)}個")
        print("\n最高の10例:")

        for i, example in enumerate(high_examples[:10], 1):
            print(
                f"  {i:2d}. {example['a']}^{example['b']} = 桁数の合計 {example['digit_sum']}"
            )
            print(f"       桁数: {example['power_length']:,}")

        # Show the best one in detail
        if high_examples:
            best = high_examples[0]
            print("\n最高の例の詳細:")
            print(f"  a = {best['a']}, b = {best['b']}")
            print(f"  {best['a']}^{best['b']} の桁数: {best['power_length']:,}")
            print(f"  桁数の合計: {best['digit_sum']}")

            # Show first and last few digits
            power_str = str(best["power"])
            if len(power_str) > 100:
                print(f"  数値: {power_str[:50]}...{power_str[-50:]}")
            else:
                print(f"  数値: {power_str}")

    def demonstrate_statistics(self) -> None:
        """Show statistics about digit sums"""
        print("=== 桁数の合計の統計 ===")

        # Get statistics for smaller range for faster computation
        stats = get_digit_sum_statistics(50, 50)

        print("分析範囲: a,b < 50")
        print(f"総組み合わせ数: {stats['total_combinations']:,}")
        print(f"最大桁数の合計: {stats['max_digit_sum']}")
        print(f"最小桁数の合計: {stats['min_digit_sum']}")
        print(f"平均桁数の合計: {stats['average_digit_sum']:.2f}")
        print(f"異なる桁数の合計の種類: {stats['unique_digit_sums']}")

        # Show distribution of top digit sums
        distribution = stats["digit_sum_distribution"]
        sorted_sums = sorted(distribution.keys(), reverse=True)

        print("\n桁数の合計の分布 (上位10位):")
        for i, digit_sum in enumerate(sorted_sums[:10], 1):
            count = distribution[digit_sum]
            print(f"  {i:2d}. 桁数の合計 {digit_sum}: {count}回")

    def demonstrate_patterns(self) -> None:
        """Demonstrate patterns in digit sums"""
        print("=== 桁数の合計のパターン分析 ===")

        # Analyze patterns for smaller range
        analysis = analyze_digit_sum_patterns(20, 20)

        print("分析範囲: a,b < 20")
        print(f"総組み合わせ数: {analysis['total_combinations']}")

        print("\n桁数の合計トップ10:")
        for i, result in enumerate(analysis["top_10"], 1):
            print(
                f"  {i:2d}. {result['a']}^{result['b']} = {result['digit_sum']} (桁数: {result['power_length']})"
            )


def main() -> None:
    """Main execution function"""
    # Verify examples first
    if not verify_examples():
        print("警告: 例題の検証に失敗しました")
        return

    # Run the problem
    runner = Problem056Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem056Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
