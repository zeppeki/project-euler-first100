#!/usr/bin/env python3
"""
Problem 071 Runner: Execution and demonstration code for Problem 071.

This module handles the execution and demonstration of Problem 071 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_071 import (
    analyze_fraction_sequence,
    find_fraction_left_of_target,
    solve_mathematical,
    solve_mediant,
    solve_optimized,
    verify_farey_neighbor,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem071Runner(BaseProblemRunner):
    """Runner for Problem 071: Ordered fractions."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "071",
            "Ordered fractions",
            428570,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 071."""
        return [
            (8, 2),  # d ≤ 8の場合、3/7のすぐ左は2/5
            (100, 29),  # d ≤ 100の場合の期待値
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 071."""
        return [
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
            ("メディアント法", solve_mediant),
            # 注意: solve_naiveは10^6まででは実用的でないため除外
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 071."""
        return [self._demonstrate_farey_sequence_analysis]

    def _demonstrate_farey_sequence_analysis(self) -> None:
        """ファレー数列の分析を表示"""
        print("Ordered Fractions (Farey Sequence) Analysis:")
        print("=" * 50)

        # 問題文の例の分析
        print("\n問題文の例（d ≤ 8）の分析:")
        small_limit = 8
        target_num, target_den = 3, 7

        # 小さな例での分析
        print(f"目標分数: {target_num}/{target_den}")
        left_num, left_den = find_fraction_left_of_target(
            target_num, target_den, small_limit
        )
        print(f"左側の分数: {left_num}/{left_den}")

        # 隣接関係の検証
        is_neighbor = verify_farey_neighbor(left_num, left_den, target_num, target_den)
        print(f"隣接関係の検証: {is_neighbor}")

        if is_neighbor:
            determinant = target_num * left_den - target_den * left_num
            print(f"行列式 (ad - bc): {determinant}")

        print("\nファレー数列の性質:")
        print("- 隣接する分数a/bとc/dに対して、ad - bc = 1")
        print("- メディアント (a+c)/(b+d) が次に挿入される分数")
        print("- 既約分数のみが含まれる")

        print("\n3/7付近の分数分析:")
        nearby_fractions = analyze_fraction_sequence(50)

        print("3/7に近い分数（d ≤ 50）:")
        print("分子/分母    | 分数値     | 3/7との差")
        print("-----------|-----------|-----------")

        target_val = 3 / 7
        for n, d, val in nearby_fractions:
            diff = val - target_val
            print(f"{n:2d}/{d:2d}      | {val:.6f} | {diff:+.6f}")
            if val >= target_val:
                break

        print("\n数学的洞察:")
        print("- 3/7のすぐ左の分数p/qは、3q - 7p = 1を満たす")
        print("- q = (7p + 1)/3の形で表現できる")
        print("- 最大のqを求めるには、(7p + 1)が3で割り切れる条件が必要")

        print("\nアルゴリズム比較:")
        print("- 素直な解法: O(n²) - 全ての既約分数を生成")
        print("- 最適化解法: O(n) - ファレー数列の性質を利用")
        print("- 数学的解法: O(1) - 直接計算")
        print("- メディアント法: O(log n) - 二分探索的手法")

        # 中規模での例
        print("\n中規模例（d ≤ 1000）:")
        medium_limit = 1000
        result_optimized = solve_optimized(medium_limit)
        result_mathematical = solve_mathematical(medium_limit)
        result_mediant = solve_mediant(medium_limit)

        print(f"最適化解法: {result_optimized}")
        print(f"数学的解法: {result_mathematical}")
        print(f"メディアント法: {result_mediant}")

        # 一貫性確認
        if result_optimized == result_mathematical == result_mediant:
            print("✓ 全ての解法が一致")
        else:
            print("✗ 解法間で結果が異なる")

        print("\n実際の問題（d ≤ 1,000,000）:")
        try:
            final_result = solve_mathematical(1000000)
            print(f"分子: {final_result}")

            # 対応する分母を計算
            if (7 * final_result + 1) % 3 == 0:
                final_denominator = (7 * final_result + 1) // 3
                print(f"分母: {final_denominator}")
                print(f"分数: {final_result}/{final_denominator}")
                print(f"分数値: {final_result / final_denominator:.10f}")
                print(f"3/7の値: {3 / 7:.10f}")
                print(f"差: {3 / 7 - final_result / final_denominator:.2e}")

        except Exception as e:
            print(f"計算エラー: {e}")

        print("\nメディアント法の動作例:")
        print("初期状態: 2/5 ... 3/7")

        # メディアント法のステップを表示
        a, b = 2, 5
        c, d = 3, 7
        step = 1

        print(f"Step {step}: {a}/{b} と {c}/{d}")

        while b + d <= 100:  # 小さな例で表示
            step += 1
            a = a + c
            b = b + d
            print(f"Step {step}: {a}/{b} と {c}/{d}")
            if step > 5:  # 表示制限
                break

        print("\n実用的な応用:")
        print("- 音楽理論での調律")
        print("- 近似分数の計算")
        print("- 連分数展開")
        print("- 数値解析での有理近似")

        print("\n学習ポイント:")
        print("- ファレー数列の性質と応用")
        print("- 既約分数の効率的な生成")
        print("- メディアント法による近似")
        print("- 数論的関数の実用的応用")


def main() -> None:
    """メイン関数"""
    runner = Problem071Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem071Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
