#!/usr/bin/env python3
"""
Problem 055 Runner: Lychrel numbers

This runner provides test cases, performance analysis, and demonstrations
for the Lychrel numbers problem.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_055 import (
    analyze_number_process,
    get_lychrel_statistics,
    solve_naive,
    solve_optimized,
    test_lychrel_examples,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem055Runner(BaseProblemRunner):
    """Runner for Problem 055: Lychrel numbers"""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "055",
            "Lychrel numbers",
            249,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Test cases for Lychrel numbers problem"""
        return [
            # Test with smaller limits to verify algorithm
            (100, 0),  # No Lychrel numbers below 100
            (200, 1),  # First Lychrel number is 196
            (1000, 13),  # Known count for first 1000 numbers
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for performance comparison"""
        return [
            ("solve_naive", solve_naive),
            ("solve_optimized", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Parameters for main problem execution"""
        return (10000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Demonstration functions for Lychrel numbers analysis"""
        return [
            self.demonstrate_lychrel_process,
            self.demonstrate_palindromic_lychrel,
            self.demonstrate_statistics,
        ]

    def demonstrate_lychrel_process(self) -> None:
        """Demonstrate the reverse-and-add process for various numbers"""
        print("=== Lychrel数の判定プロセス ===")

        # Test numbers from problem description
        test_numbers = [47, 349, 196, 4994]

        for number in test_numbers:
            print(f"\n数値 {number} の分析:")
            analysis = analyze_number_process(number, 10)  # Limit to 10 for display

            if analysis["is_lychrel"]:
                print("  結果: Lychrel数 (10回の反復では回文数にならない)")
            else:
                print(
                    f"  結果: 非Lychrel数 ({analysis['iterations_to_palindrome']}回で回文数 {analysis['final_palindrome']})"
                )

            # Show first few steps
            print("  プロセス:")
            for step in analysis["steps"][:5]:  # Show first 5 steps
                print(
                    f"    {step['iteration']}: {step['current']} + {step['reversed']} = {step['sum']}"
                )
                if step["is_palindrome"]:
                    print("      → 回文数発見!")
                    break

            if len(analysis["steps"]) > 5 and not analysis["is_lychrel"]:
                print("    ... (省略) ...")
                final_step = analysis["steps"][-1]
                print(
                    f"    {final_step['iteration']}: 最終回文数 = {final_step['sum']}"
                )

    def demonstrate_palindromic_lychrel(self) -> None:
        """Demonstrate palindromic Lychrel numbers"""
        print("=== 回文数のLychrel数 ===")

        # Find palindromic Lychrel numbers below 10000
        palindromic_lychrel = []
        for n in range(1, 10000):
            s = str(n)
            if s == s[::-1]:  # Is palindrome
                from problems.problem_055 import is_lychrel_number

                if is_lychrel_number(n):
                    palindromic_lychrel.append(n)
                    if len(palindromic_lychrel) >= 10:  # Show first 10
                        break

        print("回文数でありながらLychrel数である数 (最初の10個):")
        for i, num in enumerate(palindromic_lychrel[:10], 1):
            print(f"  {i:2d}. {num}")

        # Show analysis for 4994
        print("\n4994 の詳細分析:")
        analysis = analyze_number_process(4994, 10)
        print("  4994は回文数ですが、反転加算では回文数になりません")
        print("  プロセス (最初の5ステップ):")
        for step in analysis["steps"][:5]:
            print(
                f"    {step['iteration']}: {step['current']} + {step['reversed']} = {step['sum']}"
            )

    def demonstrate_statistics(self) -> None:
        """Show statistics about Lychrel numbers"""
        print("=== Lychrel数の統計 ===")

        # Get statistics for numbers below 1000 (for faster computation)
        stats = get_lychrel_statistics(1000)

        print(f"分析範囲: 1-{stats['total_numbers']}")
        print(f"Lychrel数の個数: {stats['lychrel_count']}")
        print(
            f"Lychrel数の割合: {stats['lychrel_count'] / stats['total_numbers'] * 100:.2f}%"
        )
        print(f"回文数のLychrel数: {stats['palindromic_lychrel_count']}")

        print("\nLychrel数の一覧 (最初の20個):")
        for i, num in enumerate(stats["lychrel_numbers"][:20], 1):
            print(f"  {i:2d}. {num}")

        if stats["palindromic_lychrel_numbers"]:
            print("\n回文数のLychrel数:")
            for i, num in enumerate(stats["palindromic_lychrel_numbers"], 1):
                print(f"  {i:2d}. {num}")

        # Show iteration distribution
        if stats["iteration_distribution"]:
            print("\n回文数到達までの反復回数分布:")
            for iterations in sorted(stats["iteration_distribution"].keys())[:10]:
                count = stats["iteration_distribution"][iterations]
                print(f"  {iterations:2d}回: {count:3d}個")


def main() -> None:
    """Main execution function"""
    # Verify examples first
    if not test_lychrel_examples():
        print("警告: 例題の検証に失敗しました")
        return

    # Run the problem
    runner = Problem055Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem055Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
