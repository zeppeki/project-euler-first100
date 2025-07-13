#!/usr/bin/env python3
"""
Problem 094 Runner: Execution and demonstration code for Problem 094.

This module handles the execution and demonstration of Problem 094 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_094 import (
    calculate_area,
    find_almost_equilateral_triangles,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem094Runner(BaseProblemRunner):
    """Runner for Problem 094: Almost equilateral triangles."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "094",
            "Almost equilateral triangles",
            518408346,  # Expected answer for perimeter limit 1,000,000,000
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 094."""
        return [
            (100, 60),  # Small test case
            (1000, 60),  # Medium test case
            (10000, 60),  # Larger test case
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 094."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000000000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 094."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_triangle_properties,
                self.demonstrate_area_calculation,
                self.demonstrate_solution_approaches,
                self.demonstrate_pell_equation,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 094の概要を説明"""
        print("=== Problem 094: Almost equilateral triangles ===")
        print()
        print("目標: 「ほぼ正三角形」の周長の和を求める")
        print()
        print("ほぼ正三角形の定義:")
        print("- 2つの辺が等しい")
        print("- 3つ目の辺が他の2つの辺と最大1だけ異なる")
        print("- 全ての辺の長さが整数")
        print("- 面積が整数")
        print()
        print("制約:")
        print("- 周長が1,000,000,000以下")
        print("- 正三角形（3つの辺が全て等しい）で整数の辺と面積を持つものは存在しない")
        print()
        print("例: 5-5-6の三角形は面積が12平方単位")
        print()

    def demonstrate_triangle_properties(self) -> None:
        """三角形の性質を説明"""
        print("=== 三角形の性質 ===")
        print()
        print("ほぼ正三角形の2つの形:")
        print("1. (a, a, a+1) - 3つ目の辺が1長い")
        print("2. (a, a, a-1) - 3つ目の辺が1短い")
        print()

        # 小さな例を示す
        small_triangles = find_almost_equilateral_triangles(100)
        print("周長100以下の例:")
        for triangle in small_triangles:
            a, b, c = triangle
            perimeter = a + b + c
            area = calculate_area(a, b, c)
            print(f"  {a}-{b}-{c}: 周長={perimeter}, 面積={area}")
        print()

        print("面積の計算:")
        print("ヘロンの公式: Area = sqrt(s(s-a)(s-b)(s-c))")
        print("where s = (a+b+c)/2 (半周長)")
        print()

    def demonstrate_area_calculation(self) -> None:
        """面積計算の詳細を説明"""
        print("=== 面積計算の詳細 ===")
        print()

        # 5-5-6の三角形の例
        a, b, c = 5, 5, 6
        s = (a + b + c) / 2
        print(f"例: {a}-{b}-{c}の三角形")
        print(f"半周長 s = ({a}+{b}+{c})/2 = {s}")
        print(f"面積 = sqrt({s}×({s}-{a})×({s}-{b})×({s}-{c}))")
        print(f"     = sqrt({s}×{s - a}×{s - b}×{s - c})")
        print(f"     = sqrt({s * s - a * s - b * s - c})")
        print(f"     = sqrt({s * (s - a) * (s - b) * (s - c)})")

        area = calculate_area(a, b, c)
        print(f"     = {area}")
        print()

        print("面積が整数になる条件:")
        print("- (a, a, a+1)の場合: (2a+1)² - 3 = 4k² (k≥1)")
        print("- (a, a, a-1)の場合: (2a-1)² - 3 = 4k² (k≥1)")
        print()

    def demonstrate_solution_approaches(self) -> None:
        """各解法のアプローチを説明"""
        print("=== 解法アプローチの比較 ===")
        print()

        print("1. 素直な解法:")
        print("   - 全ての可能な三角形を順次チェック")
        print("   - 時間計算量: O(n) where n is perimeter_limit")
        print("   - 実装が簡単だが、大きな制限では時間がかかる")
        print()

        print("2. 最適化解法:")
        print("   - ペル方程式の解を利用")
        print("   - 時間計算量: O(log n)")
        print("   - 数学的性質を活用した高速化")
        print()

        print("3. 数学的解法:")
        print("   - ペル方程式の解を直接利用")
        print("   - 時間計算量: O(log n)")
        print("   - 最も効率的な実装")
        print()

        # 小規模テストで比較
        test_limit = 10000
        print(f"テスト（周長制限: {test_limit}）:")

        triangles = find_almost_equilateral_triangles(test_limit)
        total = sum(sum(t) for t in triangles)

        print(f"  見つかった三角形の数: {len(triangles)}")
        print(f"  周長の合計: {total}")

        if triangles:
            print("  最初の3つの三角形:")
            for i, triangle in enumerate(triangles[:3]):
                a, b, c = triangle
                perimeter = a + b + c
                area = calculate_area(a, b, c)
                print(f"    {i + 1}. {a}-{b}-{c}: 周長={perimeter}, 面積={area}")
        print()

    def demonstrate_pell_equation(self) -> None:
        """ペル方程式の解説"""
        print("=== ペル方程式の応用 ===")
        print()

        print("問題の核心:")
        print("面積が整数になる条件を満たす三角形を効率的に見つける")
        print()

        print("数学的背景:")
        print("ペル方程式 x² - 3y² = 1 の解を利用")
        print("基本解: (x, y) = (2, 1)")
        print("一般解: x_{n+1} = 2x_n + 3y_n, y_{n+1} = x_n + 2y_n")
        print()

        print("解の生成:")
        x, y = 2, 1
        print("解の列:")
        for _ in range(5):
            print(f"  ({x}, {y})")
            x, y = 2 * x + 3 * y, x + 2 * y
        print("  ...")
        print()

        print("三角形への変換:")
        print("- (a, a, a+1)の場合: x = 2a+1, y = 2k")
        print("- (a, a, a-1)の場合: x = 2a-1, y = 2k")
        print("- 条件: x-1 または x+1 が偶数、y が偶数")
        print()

    def demonstrate_final_analysis(self) -> None:
        """最終的な分析結果を表示"""
        print("=== 最終分析 ===")
        print()

        print("アルゴリズムの特徴:")
        print("- 数論的問題（ペル方程式の応用）")
        print("- 指数的に増加する解の列")
        print("- 効率的な大数処理が必要")
        print()

        print("実装のポイント:")
        print("- ペル方程式の解の正確な生成")
        print("- 条件判定の効率化")
        print("- 大きな数値の処理")
        print("- 周長制限の適切なチェック")
        print()

        print("計算量の分析:")
        print("- 時間計算量: O(log n) - ペル方程式の解の数は対数的")
        print("- 空間計算量: O(1) - 定数空間で計算可能")
        print("- 実用的な計算時間で大きな制限も処理可能")
        print()

        print("最終結果:")
        result = solve_mathematical(1000000000)
        print(f"周長制限 1,000,000,000 での答え: {result:,}")
        print()

        print("検証:")
        # 中規模での検証
        test_limit = 100000
        triangles = find_almost_equilateral_triangles(test_limit)
        test_result = sum(sum(t) for t in triangles)
        print(f"周長制限 {test_limit:,} での三角形数: {len(triangles)}")
        print(f"周長制限 {test_limit:,} での周長合計: {test_result:,}")

        if triangles:
            print("最大の三角形:")
            largest = max(triangles, key=lambda t: sum(t))
            a, b, c = largest
            perimeter = a + b + c
            area = calculate_area(a, b, c)
            print(f"  {a}-{b}-{c}: 周長={perimeter:,}, 面積={area:,}")
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem094Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem094Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
