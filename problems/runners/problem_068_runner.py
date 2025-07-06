#!/usr/bin/env python3
"""
Problem 068 Runner: Execution and demonstration code for Problem 068.

This module handles the execution and demonstration of Problem 068 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_068 import (
    get_example_3gon,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem068Runner(BaseProblemRunner):
    """Runner for Problem 068: Magic 5-gon ring."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "068",
            "Magic 5-gon ring",
            "6531031914842725",
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 068."""
        # 3-gonの例題をテストケースとして使用
        # 実際の5-gonは複雑すぎるため、アルゴリズムの正確性をテスト
        return [
            # 小さな例題のテストは関数レベルで実装
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 068."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()  # No parameters needed for magic 5-gon

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 068."""
        return [self._demonstrate_magic_gon_analysis]

    def _demonstrate_magic_gon_analysis(self) -> None:
        """Magic n-gon ringの分析を表示"""
        print("Magic 5-gon Ring 分析:")
        print("=" * 50)

        # 3-gon例題の説明
        lines_3gon, expected_3gon = get_example_3gon()
        print("\n3-gon Ring 例題:")
        print("配置: 4,3,2; 6,2,1; 5,1,3")
        print("各ライン合計: 9")
        print(f"文字列表現: {expected_3gon}")

        print("\n5-gon Ring の制約:")
        print("- 数字1-10を一度ずつ使用")
        print("- 5つのラインの合計が全て同じ")
        print("- 16桁文字列として表現")
        print("- 最小外部ノードから時計回りに開始")

        print("\n数学的分析:")
        total_sum = sum(range(1, 11))
        print(f"総和: 1+2+...+10 = {total_sum}")
        print("内部ノードは2回カウントされる")
        print("5 × ライン合計 = 外部合計 + 2 × 内部合計")
        print("ライン合計 = (55 + 内部合計) / 5")

        print("\n16桁制約:")
        print("- 数字10が内部にあると17桁になる")
        print("- よって10は外部ノードに配置必須")

        print("\nアルゴリズム比較:")
        print("- 素直な解法: 10! = 3,628,800 通りの全順列")
        print("- 最適化解法: 9! = 362,880 通り (10を固定)")
        print("- 数学的解法: C(9,5) × 5! × 4! ≈ 30,240 通り")

        print("\n探索空間削減:")
        print("1. 対称性の利用 (回転で同じ配置)")
        print("2. 16桁制約 (10の位置固定)")
        print("3. ライン合計制約 (数学的事前計算)")

        # 実際の解を計算
        print("\n解の計算:")
        try:
            result = solve_optimized()
            print(f"最大16桁文字列: {result}")
            print(f"文字列長: {len(result)}")
        except Exception as e:
            print(f"計算エラー: {e}")

        print("\n学習ポイント:")
        print("- 組み合わせ問題における制約の活用")
        print("- 対称性を利用した探索空間削減")
        print("- 数学的制約による事前フィルタリング")
        print("- 順列・組み合わせの効率的な生成")


def main() -> None:
    """メイン関数"""
    runner = Problem068Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem068Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
