#!/usr/bin/env python3
"""
Problem 075 Runner: Execution and demonstration code for Problem 075.

This module handles the execution and demonstration of Problem 075 solutions,
separated from the core algorithm implementations.
"""

import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from collections.abc import Callable
from typing import Any

from problems.problem_075 import (
    analyze_perimeter_distribution,
    find_triangles_with_perimeter,
    get_examples_by_triangle_count,
    solve_naive,
    solve_optimized,
)


def verify_small_examples() -> dict[int, list[tuple[int, int, int]]]:
    """
    小さな例での検証
    返り値: 周長ごとの三角形リスト
    """
    examples = {}

    # テストケースを追加
    test_perimeters = [12, 30, 120]

    for perimeter in test_perimeters:
        examples[perimeter] = find_triangles_with_perimeter(perimeter)

    return examples


from problems.runners.base_runner import BaseProblemRunner


class Problem075Runner(BaseProblemRunner):
    """Runner for Problem 075: Singular integer right triangles."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "075",
            "Singular integer right triangles",
            161667,  # Expected answer: 161667 perimeters with exactly one triangle
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 075."""
        return [
            (48, 6),  # Small test: 6 singular perimeters ≤ 48
            (120, 13),  # Medium test: 13 singular perimeters ≤ 120
            (1000, 112),  # Larger test: 112 singular perimeters ≤ 1000
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 075."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1500000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 075."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_pythagorean_triples,
                self.demonstrate_small_examples,
                self.demonstrate_perimeter_analysis,
                self.demonstrate_solution_approaches,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 075の概要を説明"""
        print("=== Problem 075: Singular integer right triangles ===")
        print()
        print("目標: ちょうど1つの整数辺直角三角形を形成できる周長の数を求める")
        print("範囲: 1,500,000以下の周長")
        print()
        print("「Singular」の意味:")
        print("- その周長で形成できる直角三角形がただ1つだけ")
        print("- 例: 12cm → (3,4,5) のみ")
        print("- 対照: 36cm → (9,12,15) と (12,16,20) の2つ")
        print()
        print("数学的基礎:")
        print("- ピタゴラス三角形: a² + b² = c²")
        print("- ユークリッドの公式による生成")
        print("- 周長 P = a + b + c")
        print()

    def demonstrate_pythagorean_triples(self) -> None:
        """ピタゴラス三角形の基本概念を説明"""
        print("=== ピタゴラス三角形の基本概念 ===")
        print()

        print("ユークリッドの公式 (m > n > 0):")
        print("  a = m² - n²")
        print("  b = 2mn")
        print("  c = m² + n²")
        print("  周長 P = a + b + c = 2m(m + n)")
        print()

        print("原始三角形の条件:")
        print("- gcd(m, n) = 1 (互いに素)")
        print("- m と n の一方が偶数、他方が奇数")
        print()

        print("具体例:")
        examples = [
            (2, 1, "(3, 4, 5)"),
            (3, 2, "(5, 12, 13)"),
            (4, 1, "(15, 8, 17)"),
            (4, 3, "(7, 24, 25)"),
        ]

        for m, n, _triple in examples:
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            perimeter = a + b + c
            if a > b:
                a, b = b, a
            print(f"  m={m}, n={n} → ({a}, {b}, {c}), 周長={perimeter}")
        print()

    def demonstrate_small_examples(self) -> None:
        """問題文の小例を検証"""
        print("=== 問題文の例の検証 ===")
        print()

        examples = verify_small_examples()

        for perimeter in sorted(examples.keys()):
            triangles = examples[perimeter]
            print(f"周長 {perimeter}cm:")

            if not triangles:
                print("  → 整数辺直角三角形なし")
            else:
                for i, (a, b, c) in enumerate(triangles, 1):
                    print(f"  {i}. ({a}, {b}, {c})")
                    # 検証
                    assert a * a + b * b == c * c, (
                        f"ピタゴラスの定理が成り立たない: {a}² + {b}² ≠ {c}²"
                    )
                    assert a + b + c == perimeter, (
                        f"周長が一致しない: {a} + {b} + {c} ≠ {perimeter}"
                    )

                count = len(triangles)
                if count == 1:
                    print("  → Singular (1つのみ)")
                else:
                    print(f"  → Multiple ({count}個)")
            print()

    def demonstrate_perimeter_analysis(self) -> None:
        """周長分析を実演"""
        print("=== 周長分析 ===")
        print()

        # 小規模での分析
        print("小規模分析 (周長 ≤ 1000):")
        analysis = analyze_perimeter_distribution(1000)

        print(f"  有効周長数: {analysis['total_valid_perimeters']:,}")
        print(f"  Singular周長: {analysis['singular_perimeters']:,}")
        print(f"  Multiple周長: {analysis['multiple_solution_perimeters']:,}")
        print(f"  最大三角形数: {analysis['max_triangles_per_perimeter']}")
        print(f"  平均三角形数: {analysis['avg_triangles_per_perimeter']:.2f}")
        print()

        print("三角形数分布 (上位10):")
        distribution = analysis["count_distribution"]
        sorted_items = sorted(distribution.items(), key=lambda x: x[1], reverse=True)[
            :10
        ]
        for count, freq in sorted_items:
            print(f"  {count}個の三角形: {freq:,} 周長")
        print()

    def demonstrate_solution_approaches(self) -> None:
        """各解法のアプローチを説明"""
        print("=== 解法アプローチの比較 ===")
        print()

        test_limit = 1000
        print(f"テスト範囲: 周長 ≤ {test_limit:,}")
        print()

        print("1. 素直な解法:")
        print("   辞書で各周長の三角形数をカウント")
        print("   時間計算量: O(√limit × log(limit))")
        print("   空間計算量: O(limit)")
        result_naive = solve_naive(test_limit)
        print(f"   結果: {result_naive} 個のsingular周長")
        print()

        print("2. 最適化解法:")
        print("   配列で効率的にカウント")
        print("   時間計算量: O(√limit × log(limit))")
        print("   空間計算量: O(limit)")
        result_optimized = solve_optimized(test_limit)
        print(f"   結果: {result_optimized} 個のsingular周長")
        print()

        if result_naive == result_optimized:
            print("✓ 両解法の結果が一致")
        else:
            print("✗ 解法間で結果が異なる")
        print()

    def demonstrate_final_analysis(self) -> None:
        """最終的な分析結果を表示"""
        print("=== 最終分析 ===")
        print()

        print("Singular三角形の例:")
        singular_examples = get_examples_by_triangle_count(200, 1, 5)
        print("ちょうど1つの三角形を持つ周長の例:")
        for perimeter, triangles in singular_examples:
            if triangles:
                a, b, c = triangles[0]
                print(f"  周長 {perimeter}: ({a}, {b}, {c})")
        print()

        print("Multiple三角形の例:")
        multiple_examples = get_examples_by_triangle_count(200, 2, 3)
        print("2つの三角形を持つ周長の例:")
        for perimeter, triangles in multiple_examples:
            print(f"  周長 {perimeter}:")
            for i, (a, b, c) in enumerate(triangles, 1):
                print(f"    {i}. ({a}, {b}, {c})")
        print()

        print("1,500,000以下での最終計算:")
        final_count = solve_optimized(1500000)
        print(f"結果: {final_count:,} 個のsingular周長")
        print()

        print("アルゴリズム考察:")
        print("- ユークリッドの公式による効率的な三角形生成")
        print("- 原始三角形とスケール三角形の系統的な探索")
        print("- O(√N)の時間計算量で大規模データに対応")
        print("- 約16万の singular 周長が存在")
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem075Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem075Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
