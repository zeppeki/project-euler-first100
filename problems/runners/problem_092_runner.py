#!/usr/bin/env python3
"""
Problem 092 Runner: Execution and demonstration code for Problem 092.

This module handles the execution and demonstration of Problem 092 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_092 import (
    get_chain_destination,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    square_digit_sum,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem092Runner(BaseProblemRunner):
    """Runner for Problem 092: Square digit chains."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "092",
            "Square digit chains",
            8581146,  # Expected answer for numbers below 10 million
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 092."""
        return [
            (100, 80),  # Below 100: 80 numbers arrive at 89
            (1000, 857),  # Below 1000: 857 numbers arrive at 89
            (10000, 8558),  # Below 10000: 8558 numbers arrive at 89
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 092."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (10000000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 092."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_chain_examples,
                self.demonstrate_square_digit_sum,
                self.demonstrate_solution_approaches,
                self.demonstrate_mathematical_insights,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 092の概要を説明"""
        print("=== Problem 092: Square digit chains ===")
        print()
        print("目標: 1000万未満の数のうち、89に到達する数の個数を求める")
        print()
        print("数字チェーンのルール:")
        print("- 各桁の二乗の和を繰り返し計算")
        print("- 最終的に1または89に到達する")
        print("- 全ての数は必ず1か89のどちらかに到達する")
        print()
        print("例:")
        print("  44 → 32 → 13 → 10 → 1 → 1")
        print("  85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89")
        print()

    def demonstrate_chain_examples(self) -> None:
        """チェーンの例を実演"""
        print("=== チェーンの例 ===")
        print()

        examples = [44, 85, 23, 145, 32]

        for num in examples:
            print(f"数値 {num} のチェーン:")
            current = num
            chain = [current]

            while current != 1 and current != 89:
                current = square_digit_sum(current)
                chain.append(current)
                if len(chain) > 20:  # 無限ループ防止
                    break

            chain_str = " → ".join(map(str, chain))
            destination = get_chain_destination(num)
            print(f"  {chain_str}")
            print(f"  最終到達点: {destination}")
            print()

    def demonstrate_square_digit_sum(self) -> None:
        """桁の二乗和の計算を説明"""
        print("=== 桁の二乗和の計算 ===")
        print()

        examples = [44, 85, 145, 32, 13]

        for num in examples:
            digits = [int(d) for d in str(num)]
            squares = [d * d for d in digits]
            total = sum(squares)

            digit_str = " + ".join(f"{d}²" for d in digits)
            square_str = " + ".join(map(str, squares))

            print(f"{num}: {digit_str} = {square_str} = {total}")
        print()

    def demonstrate_solution_approaches(self) -> None:
        """各解法のアプローチを説明"""
        print("=== 解法アプローチの比較 ===")
        print()

        test_limit = 10000
        print(f"テスト範囲: 1 から {test_limit:,}")
        print()

        print("1. 素直な解法:")
        print("   各数字について個別にチェーンをたどる")
        print("   時間計算量: O(n × k × log d)")
        result_naive = solve_naive(test_limit)
        print(f"   結果: {result_naive} 個の数が89に到達")
        print()

        print("2. 最適化解法:")
        print("   メモ化を使用して計算済みの結果を再利用")
        print("   時間計算量: O(n + k × log d)")
        result_optimized = solve_optimized(test_limit)
        print(f"   結果: {result_optimized} 個の数が89に到達")
        print()

        print("3. 数学的解法:")
        print("   桁の二乗和の可能な値は限られることを利用")
        print("   時間計算量: O(s + n)")
        result_mathematical = solve_mathematical(test_limit)
        print(f"   結果: {result_mathematical} 個の数が89に到達")
        print()

        if result_naive == result_optimized == result_mathematical:
            print("✓ 全ての解法が同じ結果を生成")
        else:
            print("✗ 解法間で結果が異なる")
        print()

    def demonstrate_mathematical_insights(self) -> None:
        """数学的洞察を説明"""
        print("=== 数学的洞察 ===")
        print()

        print("1. 問題の性質:")
        print("   - 全ての正の整数は最終的に1または89に到達する")
        print("   - チェーンの長さは比較的短い")
        print("   - 桁の二乗和は元の数より小さくなることが多い")
        print()

        print("2. 最適化のポイント:")
        print("   - 桁の二乗和の最大値は限られている")
        print("   - 7桁の数の場合: 最大 7 × 9² = 567")
        print("   - 多くの異なる数が同じ二乗和を持つ")
        print()

        print("3. 分布の分析:")
        # 小規模での分析
        ones_count = 0
        eighty_nines_count = 0

        for i in range(1, 1000):
            if get_chain_destination(i) == 1:
                ones_count += 1
            else:
                eighty_nines_count += 1

        print("   1000未満の数について:")
        print(f"   - 1に到達: {ones_count} 個 ({ones_count / 999 * 100:.1f}%)")
        print(
            f"   - 89に到達: {eighty_nines_count} 個 ({eighty_nines_count / 999 * 100:.1f}%)"
        )
        print()

    def demonstrate_final_analysis(self) -> None:
        """最終的な分析結果を表示"""
        print("=== 最終分析 ===")
        print()

        print("チェーンの長さ分析:")
        chain_lengths = {}
        sample_size = 1000

        for i in range(1, sample_size + 1):
            current = i
            length = 0
            while current != 1 and current != 89:
                current = square_digit_sum(current)
                length += 1
                if length > 50:  # 安全装置
                    break

            if length not in chain_lengths:
                chain_lengths[length] = 0
            chain_lengths[length] += 1

        print(f"サンプル {sample_size} 個の分析:")
        for length in sorted(chain_lengths.keys()):
            count = chain_lengths[length]
            print(f"  チェーン長 {length}: {count} 個")
        print()

        print("1000万未満での最終計算:")
        final_count = solve_mathematical(10000000)
        print(f"結果: {final_count:,} 個の数が89に到達")
        print(f"割合: {final_count / 9999999 * 100:.2f}%")
        print()

        print("アルゴリズム考察:")
        print("- メモ化により大幅な高速化を実現")
        print("- 桁の二乗和の性質を利用した効率的な計算")
        print("- 約858万の数が89に到達（約85.8%）")
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem092Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem092Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
