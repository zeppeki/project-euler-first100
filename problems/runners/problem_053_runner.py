#!/usr/bin/env python3
"""
Problem 053 Runner: Execution and demonstration code for Problem 053.

This module handles the execution and demonstration of Problem 053 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_053 import (
    analyze_combinatorial_values,
    combination_optimized,
    demonstrate_symmetry,
    find_first_exceeding_threshold,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem053Runner(BaseProblemRunner):
    """Runner for Problem 053: Combinatoric selections."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "053",
            "Combinatoric selections",
            4075,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 053."""
        return [
            (10, 1000000, 0),  # Small test case - no combinations > 1M for n ≤ 10
            (23, 1000000, 4),  # First threshold crossing at C(23,10)
            (25, 1000000, 21),  # More combinations above threshold
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 053."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (100, 1000000)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 053."""
        return [self._demonstrate_combinatorial_selections]

    def _demonstrate_combinatorial_selections(self) -> None:
        """組み合わせ選択の分析を表示"""
        print("組み合わせ選択の分析:")

        # Pascal's triangle demonstration
        print("\n1. パスカルの三角形（対称性の確認）:")
        symmetry_demo = demonstrate_symmetry()
        for n, row in symmetry_demo[:8]:  # Show first 8 rows
            print(f"  n={n}: {row}")

        # First value exceeding threshold
        print("\n2. 100万を最初に超える組み合わせ:")
        n, r, value = find_first_exceeding_threshold(1000000)
        if n != -1:
            print(f"  C({n},{r}) = {value:,}")
            print("  検証: 問題文では C(23,10) = 1,144,066 と記載")

        # Analysis of specific values around threshold
        print("\n3. 閾値周辺の値の分析:")
        test_values = [
            (22, 10),
            (22, 11),
            (22, 12),
            (23, 9),
            (23, 10),
            (23, 11),
            (23, 12),
            (24, 10),
            (24, 11),
            (24, 12),
        ]

        for n, r in test_values:
            value = combination_optimized(n, r)
            threshold_mark = "✓" if value > 1000000 else " "
            print(f"  C({n},{r}) = {value:8,} {threshold_mark}")

        # Overall analysis
        print("\n4. 全体分析 (n ≤ 100):")
        analysis = analyze_combinatorial_values(100)
        print(f"  総計算値数: {analysis['total_values']:,}")
        print(f"  最大値: C{analysis['max_position']} = {analysis['max_value']:,}")
        print(f"  100万超過: {analysis['threshold_count']:,} 個")

        # Distribution by n
        print("\n5. nごとの100万超過数の分布:")
        for n in range(20, 31):  # Show range around threshold
            count = 0
            above_threshold = []
            for r in range(n + 1):
                value = combination_optimized(n, r)
                if value > 1000000:
                    count += 1
                    above_threshold.append(r)

            if count > 0:
                print(f"  n={n}: {count}個 (r={above_threshold})")

        # Symmetry verification
        print("\n6. 対称性の検証:")
        n = 25
        print(f"  n={n}での対称性:")
        for r in range(6):
            value1 = combination_optimized(n, r)
            value2 = combination_optimized(n, n - r)
            print(f"    C({n},{r}) = {value1:,} = C({n},{n - r}) = {value2:,}")


def main() -> None:
    """メイン関数"""
    runner = Problem053Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem053Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
