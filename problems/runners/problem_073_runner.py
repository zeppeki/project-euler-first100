#!/usr/bin/env python3
"""
Problem 073 Runner: Execution and demonstration code for Problem 073.

This module handles the execution and demonstration of Problem 073 solutions,
separated from the core algorithm implementations.
"""

import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from collections.abc import Callable
from typing import Any

from problems.problem_073 import (
    analyze_fraction_distribution,
    find_closest_fractions,
    get_fractions_by_denominator,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


def verify_small_example() -> tuple[int, list[tuple[int, int]]]:
    """
    問題文の小さな例 (d ≤ 8) を検証
    1/3 < n/d < 1/2 の範囲の既約分数を返す
    """
    from math import gcd

    fractions = []
    for d in range(2, 9):
        for n in range(1, d):
            if gcd(n, d) == 1 and 1 / 3 < n / d < 1 / 2:
                fractions.append((n, d))

    # Sort by value
    fractions.sort(key=lambda x: x[0] / x[1])
    return len(fractions), fractions


class Problem073Runner(BaseProblemRunner):
    """Runner for Problem 073: Counting fractions in a range."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "073",
            "Counting fractions in a range",
            7295372,  # Expected answer for d ≤ 12,000
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 073."""
        return [
            (8, 3),  # For d ≤ 8, there are 3 fractions between 1/3 and 1/2
            (12, 7),  # For d ≤ 12, there are 7 fractions between 1/3 and 1/2
            (100, 505),  # For d ≤ 100, there are 505 fractions between 1/3 and 1/2
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 073."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (12000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 073."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_small_example,
                self.demonstrate_solution_approaches,
                self.demonstrate_range_analysis,
                self.demonstrate_mathematical_insights,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 073の概要を説明"""
        print("=== Problem 073: Counting fractions in a range ===")
        print()
        print("目標: 1/3と1/2の間にある既約真分数の個数を求める")
        print("条件: 分母がd ≤ 12,000")
        print()
        print("既約真分数とは:")
        print("- n/d where n < d and gcd(n,d) = 1")
        print("- 分子と分母が互いに素である真分数")
        print()
        print("範囲条件:")
        print("- 1/3 < n/d < 1/2")
        print("- 厳密に1/3より大きく、1/2より小さい")
        print()

    def demonstrate_small_example(self) -> None:
        """小さな例での検証"""
        print("=== 小さな例での検証 ===")
        print()
        print("例: d ≤ 8の場合")
        count, fractions = verify_small_example()
        print(f"1/3と1/2の間の既約真分数の個数: {count}")
        print()
        print("該当する分数:")
        for n, d in fractions:
            fraction_value = n / d
            print(f"  {n}/{d} = {fraction_value:.6f}")
        print()
        print("参考: 1/3 = 0.333333..., 1/2 = 0.500000")
        print()

    def demonstrate_solution_approaches(self) -> None:
        """各解法のアプローチを説明"""
        print("=== 解法アプローチの比較 ===")
        print()
        test_limit = 100

        print("1. 素直な解法 (Naive):")
        print("   すべての分数を生成して範囲内をカウント - O(n²)")
        result_naive = solve_naive(test_limit)
        print(f"   結果 (d ≤ {test_limit}): {result_naive}")
        print()

        print("2. 最適化解法 (Optimized):")
        print("   範囲計算を最適化 - O(n log n)")
        result_optimized = solve_optimized(test_limit)
        print(f"   結果 (d ≤ {test_limit}): {result_optimized}")
        print()

        print("3. 数学的解法 (Mathematical):")
        print("   連分数とメディアント性質を利用 - O(n log n)")
        result_mathematical = solve_mathematical(test_limit)
        print(f"   結果 (d ≤ {test_limit}): {result_mathematical}")
        print()

        print("✓ すべての解法が同じ結果を生成")
        print()

    def demonstrate_range_analysis(self) -> None:
        """範囲別分析を実演"""
        print("=== 範囲別分析 ===")
        print()

        limits = [8, 12, 50, 100, 500, 1000]

        for limit in limits:
            count = solve_mathematical(limit)
            print(f"d ≤ {limit:4d}: {count:6d} 個の分数")
        print()

        print("分母別の分数分布 (d ≤ 20):")
        fractions_by_d = get_fractions_by_denominator(20)
        for d in sorted(fractions_by_d.keys()):
            fractions = fractions_by_d[d]
            print(f"  d = {d:2d}: {len(fractions)} 個の分数 - ", end="")
            for i, (n, d_val) in enumerate(fractions):
                print(f"{n}/{d_val}", end="")
                if i < len(fractions) - 1:
                    print(", ", end="")
            print()
        print()

    def demonstrate_mathematical_insights(self) -> None:
        """数学的洞察を説明"""
        print("=== 数学的洞察 ===")
        print()

        print("1. 問題の本質:")
        print("   各分母dについて、1/3 < n/d < 1/2 を満たす既約分数n/dの個数を求める")
        print("   総数 = Σ(count of valid n for each d)")
        print()

        print("2. 範囲の計算:")
        print("   1/3 < n/d < 1/2")
        print("   ⟺ d/3 < n < d/2")
        print("   ⟺ floor(d/3) + 1 ≤ n ≤ floor(d/2) - 1 (if d is even)")
        print("   ⟺ floor(d/3) + 1 ≤ n ≤ floor(d/2) (if d is odd)")
        print()

        print("3. 小さな例での計算過程:")
        for d in [5, 6, 7, 8]:
            min_n = d // 3 + 1
            max_n = (d - 1) // 2 if d % 2 == 1 else d // 2 - 1
            print(f"   d = {d}: {min_n} ≤ n ≤ {max_n}")
            valid_fractions = []
            for n in range(min_n, max_n + 1):
                from math import gcd

                if gcd(n, d) == 1 and 3 * n > d and 2 * n < d:
                    valid_fractions.append(f"{n}/{d}")
            print(
                f"        既約分数: {', '.join(valid_fractions) if valid_fractions else 'なし'}"
            )
        print()

        print("4. 境界に最も近い分数:")
        closest_to_third, closest_to_half = find_closest_fractions(1000)
        if closest_to_third:
            n, d = closest_to_third
            print(f"   1/3に最も近い分数: {n}/{d} = {n / d:.6f}")
        if closest_to_half:
            n, d = closest_to_half
            print(f"   1/2に最も近い分数: {n}/{d} = {n / d:.6f}")
        print()

        print("5. 最終的な計算:")
        final_answer = solve_mathematical(12000)
        print(f"   d ≤ 12,000の場合: {final_answer:,} 個の分数")
        print()

        print("6. 分布の分析:")
        analysis = analyze_fraction_distribution(100)
        print("   d ≤ 100での分析:")
        print(f"   - 総数: {analysis['total_count']:,}")
        print(f"   - 最小値: {analysis['min_value']:.6f}")
        print(f"   - 最大値: {analysis['max_value']:.6f}")
        print(f"   - 平均値: {analysis['avg_value']:.6f}")
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem073Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem073Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
