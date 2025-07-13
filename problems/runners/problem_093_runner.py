#!/usr/bin/env python3
"""
Problem 093 Runner: Execution and demonstration code for Problem 093.

This module handles the execution and demonstration of Problem 093 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_093 import (
    get_expression_details,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem093Runner(BaseProblemRunner):
    """Runner for Problem 093: Arithmetic expressions."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "093",
            "Arithmetic expressions",
            "1258",  # Expected answer: the set of digits that produces the longest consecutive sequence
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 093."""
        # This problem doesn't have parametrized test cases
        return []

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 093."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 093."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_expression_generation,
                self.demonstrate_example_calculations,
                self.demonstrate_solution_approaches,
                self.demonstrate_performance_analysis,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 093の概要を説明"""
        print("=== Problem 093: Arithmetic expressions ===")
        print()
        print("目標: 4つの異なる数字を使って最も長い連続した正の整数列を生成")
        print()
        print("制約:")
        print("- 4つの異なる数字を1回ずつ使用")
        print("- 四則演算（+, -, *, /）と括弧を使用")
        print("- 数字の連結は不可（例: 12 + 34は無効）")
        print("- 正の整数のみを対象")
        print()
        print("例: {1, 2, 3, 4}の場合:")
        print("  8 = (4 * (1 + 3)) / 2")
        print("  14 = 4 * (3 + 1 / 2)")
        print("  19 = 4 * (2 + 3) - 1")
        print("  36 = 3 * 4 * (2 + 1)")
        print()
        print(
            "目標: 1からnまでの最も長い連続した正の整数列を生成する数字の組み合わせを見つける"
        )
        print()

    def demonstrate_expression_generation(self) -> None:
        """式の生成方法を説明"""
        print("=== 式の生成方法 ===")
        print()
        print("4つの数字から生成可能な式のパターン:")
        print()
        print("1. 数字の順列: 4! = 24通り")
        print("2. 演算子の組み合わせ: 4³ = 64通り（3つの演算子位置）")
        print("3. 括弧のパターン: 5通り")
        print()
        print("括弧のパターン:")
        print("  1) ((a op1 b) op2 c) op3 d")
        print("  2) (a op1 (b op2 c)) op3 d")
        print("  3) (a op1 b) op2 (c op3 d)")
        print("  4) a op1 ((b op2 c) op3 d)")
        print("  5) a op1 (b op2 (c op3 d))")
        print()
        print("総計算数: 24 × 64 × 5 = 7,680通り")
        print()

    def demonstrate_example_calculations(self) -> None:
        """具体的な計算例を示す"""
        print("=== 具体的な計算例 ===")
        print()

        # {1, 2, 3, 4}の例
        example_digits = (1, 2, 3, 4)
        print(f"数字の組み合わせ: {example_digits}")

        details = get_expression_details(example_digits)
        possible_numbers = details["possible_numbers"]
        consecutive_length = details["consecutive_length"]

        # Type assertions for mypy
        assert isinstance(possible_numbers, set)
        assert isinstance(consecutive_length, int)

        print(f"生成可能な数の個数: {len(possible_numbers)}")
        print(f"連続した長さ: 1から{consecutive_length}まで")
        print()

        # 最初の20個の数を表示
        sorted_numbers = sorted(possible_numbers)
        print("生成可能な数（最初の20個）:")
        for i, num in enumerate(sorted_numbers[:20]):
            if i % 10 == 0 and i > 0:
                print()
            print(f"{num:3d}", end=" ")
        print()
        print()

        # 連続性の確認
        print("連続性の確認:")
        consecutive_numbers = []
        current = 1
        while current in possible_numbers:
            consecutive_numbers.append(current)
            current += 1

        print(f"連続した数: {consecutive_numbers[:15]}...")
        print(f"最大連続長: {len(consecutive_numbers)}")
        print()

    def demonstrate_solution_approaches(self) -> None:
        """各解法のアプローチを説明"""
        print("=== 解法アプローチの比較 ===")
        print()

        print("1. 素直な解法:")
        print("   - 0-9の数字から4つの組み合わせを全て試す")
        print("   - 組み合わせ数: C(10,4) = 210")
        print("   - 0を含む場合も計算（割り算で問題になる可能性）")
        print("   - 時間計算量: O(210 × 7,680) = O(1,612,800)")
        print()

        print("2. 最適化解法:")
        print("   - 1-9の数字のみを使用（0を除外）")
        print("   - 組み合わせ数: C(9,4) = 126")
        print("   - 0による割り算エラーを回避")
        print("   - 時間計算量: O(126 × 7,680) = O(967,680)")
        print()

        print("3. 数学的解法:")
        print("   - この問題では最適化解法と同じ")
        print("   - 数学的ショートカットは存在しない")
        print("   - 全ての組み合わせを試す必要がある")
        print()

    def demonstrate_performance_analysis(self) -> None:
        """パフォーマンス分析を実行"""
        print("=== パフォーマンス分析 ===")
        print()

        # 小規模テストでパフォーマンスを測定
        print("小規模テスト（{1,2,3,4}の詳細分析）:")
        test_digits = (1, 2, 3, 4)
        details = get_expression_details(test_digits)

        print(f"数字組み合わせ: {test_digits}")
        assert isinstance(details["possible_numbers"], set)
        print(f"生成可能な数の個数: {len(details['possible_numbers'])}")
        print(f"連続した長さ: {details['consecutive_length']}")
        print()

        # 上位の数字組み合わせを表示
        print("上位の数字組み合わせ（例）:")

        test_combinations = [
            (1, 2, 3, 4),
            (1, 2, 5, 8),
            (2, 3, 4, 6),
            (1, 3, 5, 7),
            (2, 4, 6, 8),
        ]

        for digits in test_combinations:
            details = get_expression_details(digits)
            print(f"  {digits}: 連続長 {details['consecutive_length']}")

        print()
        print("最適解の探索:")
        print("- 全ての組み合わせを体系的に評価")
        print("- 最長の連続した正の整数列を生成する組み合わせを特定")
        print()

    def demonstrate_final_analysis(self) -> None:
        """最終的な分析結果を表示"""
        print("=== 最終分析 ===")
        print()

        print("アルゴリズムの特徴:")
        print("- 組み合わせ論的探索問題")
        print("- 全ての可能な式を体系的に評価")
        print("- 浮動小数点演算の精度に注意が必要")
        print("- 結果の正の整数判定に誤差考慮が重要")
        print()

        print("実装のポイント:")
        print("- 5つの括弧パターンを全て実装")
        print("- ゼロ除算エラーの適切な処理")
        print("- 浮動小数点誤差を考慮した整数判定")
        print("- 効率的な組み合わせ生成")
        print()

        print("計算量の分析:")
        print("- 時間計算量: O(C(9,4) × 4! × 4³ × 5) = O(967,680)")
        print("- 空間計算量: O(k) where k is number of unique results")
        print("- 実用的な計算時間で解決可能")
        print()

        print("最終結果:")
        result = solve_optimized()
        print(f"最長の連続した正の整数列を生成する数字の組み合わせ: {result}")

        # 最終結果の詳細
        result_digits = tuple(int(d) for d in result)
        details = get_expression_details(result_digits)
        print(f"連続した長さ: 1から{details['consecutive_length']}まで")
        assert isinstance(details["possible_numbers"], set)
        print(f"生成可能な数の総数: {len(details['possible_numbers'])}")
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem093Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem093Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
