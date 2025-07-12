#!/usr/bin/env python3
"""
Problem 076 Runner: Execution and demonstration code for Problem 076.

This module handles the execution and demonstration of Problem 076 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_076 import solve_naive, solve_optimized
from problems.runners.base_runner import BaseProblemRunner


class Problem076Runner(BaseProblemRunner):
    """Runner for Problem 076: Counting summations."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "076",
            "Counting summations",
            190569291,  # Expected answer for n=100
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 076."""
        return [
            # Test case 1: Example from problem statement (5 partitions)
            (5,),
            # Test case 2: Small values
            (2,),
            (3,),
            (4,),
            # Test case 3: Larger values for consistency
            (10,),
            (20,),
            # Test case 4: Main problem
            (100,),
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 076."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (100,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 076."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_partition_examples,
                self.demonstrate_dynamic_programming_approach,
                self.demonstrate_optimization_comparison,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 076の概要を説明"""
        print("=== Problem 076: Counting summations ===")
        print()
        print("目標: 100を2つ以上の正の整数の和で表す方法の数を求める")
        print()
        print("例: 5を2つ以上の正の整数の和で表す方法:")
        print("  5 = 4 + 1")
        print("  5 = 3 + 2")
        print("  5 = 3 + 1 + 1")
        print("  5 = 2 + 2 + 1")
        print("  5 = 2 + 1 + 1 + 1")
        print("  5 = 1 + 1 + 1 + 1 + 1")
        print("  → 合計6通り")
        print()
        print("これは「整数分割」問題として知られています。")
        print()

    def demonstrate_partition_examples(self) -> None:
        """小さな数での分割例を表示"""
        print("=== 小さな数での分割例 ===")
        print()
        examples = [
            (2, ["1+1"]),
            (3, ["2+1", "1+1+1"]),
            (4, ["3+1", "2+2", "2+1+1", "1+1+1+1"]),
            (5, ["4+1", "3+2", "3+1+1", "2+2+1", "2+1+1+1", "1+1+1+1+1"]),
        ]

        for n, partitions in examples:
            result = solve_optimized(n)
            print(f"n = {n}: {result}通り")
            for i, partition in enumerate(partitions, 1):
                print(f"  {i}. {n} = {partition}")
            print()

    def demonstrate_dynamic_programming_approach(self) -> None:
        """動的計画法のアプローチを説明"""
        print("=== 動的計画法のアプローチ ===")
        print()
        print("アルゴリズムの考え方:")
        print("dp[i][j] = iをj以下の整数の和で表す方法の数")
        print()
        print("漸化式:")
        print("dp[i][j] = dp[i][j-1] + dp[i-j][j]")
        print("  - dp[i][j-1]: jを使わない場合")
        print("  - dp[i-j][j]: jを少なくとも1回使う場合")
        print()

        # 小さな例での計算過程を表示
        print("例: n=5の計算過程")
        n = 5
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # 初期化
        for j in range(n + 1):
            dp[0][j] = 1

        print("\n初期状態:")
        print("dp[0][j] = 1 (0は空の和で表現)")

        # 計算過程を表示
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i < j:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - j][j]

        print(f"\n最終結果: dp[{n}][{n - 1}] = {dp[n][n - 1]} (n未満の数のみ使用)")
        print()

    def demonstrate_optimization_comparison(self) -> None:
        """最適化の比較を説明"""
        print("=== 素直な解法 vs 最適化解法 ===")
        print()
        print("素直な解法 (2次元DP):")
        print("- 時間計算量: O(n²)")
        print("- 空間計算量: O(n²)")
        print("- メモリ使用量: n×nの2次元配列")
        print()
        print("最適化解法 (1次元DP):")
        print("- 時間計算量: O(n²)")
        print("- 空間計算量: O(n)")
        print("- メモリ使用量: nの1次元配列")
        print()
        print("最適化のポイント:")
        print("- 前の行のデータのみ必要なため、1次元配列で十分")
        print("- メモリ効率が大幅に改善される")
        print("- 大きなnに対してより実用的")
        print()

        # 実際の性能比較
        print("実際の性能差:")
        test_values = [50, 100]

        for n in test_values:
            print(f"\nn = {n}:")

            import time

            # 素直な解法
            start = time.perf_counter()
            result1 = solve_naive(n)
            time1 = time.perf_counter() - start

            # 最適化解法
            start = time.perf_counter()
            result2 = solve_optimized(n)
            time2 = time.perf_counter() - start

            print(f"  素直な解法:    {time1:.6f}秒 → {result1:,}")
            print(f"  最適化解法:    {time2:.6f}秒 → {result2:,}")
            if time1 > 0:
                speedup = time1 / time2
                print(f"  高速化率:      {speedup:.2f}倍")


def main() -> None:
    """メイン関数"""
    runner = Problem076Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 076."""
    print("=== Problem 076 Performance Benchmark ===")
    runner = Problem076Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
