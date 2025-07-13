#!/usr/bin/env python3
"""
Problem 100 Runner: Execution and demonstration code for Problem 100.

This module handles the execution and demonstration of Problem 100 solutions,
separated from the core algorithm implementations.
"""

import math
from collections.abc import Callable
from typing import Any

from problems.problem_100 import (
    find_next_arrangement,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    verify_arrangement,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem100Runner(BaseProblemRunner):
    """Runner for Problem 100: Arranged probability."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "100",
            "Arranged probability",
            756872327473,  # Expected answer for the problem
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 100."""
        return [
            # Test with main problem limit
            (10**12,),
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 100."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (10**12,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 100."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_probability_theory,
                self.demonstrate_mathematical_approach,
                self.demonstrate_pell_equation,
                self.demonstrate_solution_sequence,
                self.demonstrate_final_calculation,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 100の概要を説明"""
        print("=== Problem 100: Arranged probability ===")
        print()
        print("目標: 2つの青いディスクを引く確率が正確に50%となる配置を見つける")
        print()
        print("問題の設定:")
        print("- 箱に青と赤のディスクが入っている")
        print("- 2つのディスクを連続で引く（戻さない）")
        print("- P(青, 青) = (青の数/全体) × (青の数-1)/(全体-1) = 1/2")
        print("- 全体のディスク数が10^12を超える最初の配置を求める")
        print()
        print("既知の例:")
        print("- 21個中15個が青: P(青,青) = (15/21) × (14/20) = 1/2")
        print("- 120個中85個が青: P(青,青) = (85/120) × (84/119) = 1/2")
        print()

    def demonstrate_probability_theory(self) -> None:
        """確率論的アプローチを説明"""
        print("=== 確率論的アプローチ ===")
        print()
        print("数学的定式化:")
        print("b = 青いディスクの数, n = 全体のディスク数とすると")
        print()
        print("P(青, 青) = b/n × (b-1)/(n-1) = 1/2")
        print()
        print("これを整理すると:")
        print("2b(b-1) = n(n-1)")
        print()

        # 実際の例で確認
        print("既知の解での検証:")
        examples = [(15, 21), (85, 120)]

        for blue, total in examples:
            info = verify_arrangement(blue, total)
            red = total - blue
            print(f"  青: {blue}, 赤: {red}, 全体: {total}")
            print(
                f"  確率計算: ({blue}/{total}) × ({blue - 1}/{total - 1}) = {info['prob_both_blue']:.10f}"
            )
            print(
                f"  数式検証: 2×{blue}×{blue - 1} = {2 * blue * (blue - 1)}, {total}×{total - 1} = {total * (total - 1)}"
            )
            print(f"  一致: {info['formula_valid']}")
            print()

    def demonstrate_mathematical_approach(self) -> None:
        """数学的変換を説明"""
        print("=== 数学的変換 ===")
        print()
        print("方程式 2b(b-1) = n(n-1) をPell方程式に変換:")
        print()
        print("1. 方程式を展開:")
        print("   2b² - 2b = n² - n")
        print()
        print("2. 平方完成を行う:")
        print("   2b² - 2b + 1/2 = n² - n + 1/2")
        print("   (2b - 1)² - 1/2 = n² - n + 1/2")
        print()
        print("3. 変数置換: x = 2b - 1, y = 2n - 1")
        print("   y² - 2x² = -1")
        print()
        print("これはPell方程式の標準形!")
        print()

        # 座標変換の例
        print("座標変換の例:")
        examples = [(15, 21), (85, 120)]

        for blue, total in examples:
            x = 2 * blue - 1
            y = 2 * total - 1
            print(f"  (b={blue}, n={total}) → (x={x}, y={y})")
            print(f"  検証: {y}² - 2×{x}² = {y * y - 2 * x * x}")
            print()

    def demonstrate_pell_equation(self) -> None:
        """Pell方程式の解法を説明"""
        print("=== Pell方程式 y² - 2x² = -1 の解法 ===")
        print()
        print("特徴:")
        print("- 基本解: (x₁, y₁) = (1, 1)")
        print("- 漸化式: (xₖ₊₁, yₖ₊₁) = (2yₖ + 3xₖ, 3yₖ + 4xₖ)")
        print()

        print("解の生成:")
        x, y = 1, 1
        solutions = []

        for i in range(5):
            # 座標を元に戻す
            if x % 2 == 1 and y % 2 == 1:  # 奇数の場合のみ有効
                b = (x + 1) // 2
                n = (y + 1) // 2
                if b > 0 and n > 0:
                    solutions.append((x, y, b, n))

            print(f"  解{i + 1}: (x={x}, y={y})", end="")
            if x % 2 == 1 and y % 2 == 1:
                b = (x + 1) // 2
                n = (y + 1) // 2
                if b > 0 and n > 0:
                    print(f" → (b={b}, n={n})")
                    # 検証
                    check = y * y - 2 * x * x
                    print(f"        検証: {y}² - 2×{x}² = {check}")
                else:
                    print(" → 無効")
            else:
                print(" → 無効（偶数）")

            # 次の解を計算
            x_new = 2 * y + 3 * x
            y_new = 3 * y + 4 * x
            x, y = x_new, y_new

        print()

    def demonstrate_solution_sequence(self) -> None:
        """解の系列を生成・表示"""
        print("=== 有効な解の系列 ===")
        print()

        # 最初の有効解から開始
        blue, total = 15, 21
        solutions = []

        print("配置の系列:")
        for i in range(6):
            info = verify_arrangement(blue, total)
            solutions.append((blue, total))

            print(f"  解{i + 1}: 青={blue:,}, 全体={total:,}")
            print(f"        確率={info['prob_both_blue']:.15f}")
            print(f"        10^12を超過: {'Yes' if total > 10**12 else 'No'}")

            if total > 10**12:
                print("        → これが答え！")
                break

            # 次の解を計算
            blue, total = find_next_arrangement(blue, total)
            print()

        print()
        print("パターンの分析:")
        if len(solutions) >= 3:
            for i in range(1, min(4, len(solutions))):
                b_ratio = solutions[i][0] / solutions[i - 1][0]
                n_ratio = solutions[i][1] / solutions[i - 1][1]
                print(
                    f"  解{i + 1}/解{i}: 青の比={b_ratio:.6f}, 全体の比={n_ratio:.6f}"
                )

    def demonstrate_final_calculation(self) -> None:
        """最終的な計算結果を表示"""
        print("=== 最終計算 ===")
        print()

        print("問題の制約:")
        print(f"- 全体のディスク数 > {10**12:,}")
        print("- P(青, 青) = 正確に 1/2")
        print()

        # メイン問題を解く
        print("計算実行:")
        import time

        start_time = time.time()
        blue_result = solve_mathematical(10**12)
        end_time = time.time()

        # totalを逆算
        discriminant = 1 + 8 * blue_result * (blue_result - 1)
        total_result = int((1 + math.sqrt(discriminant)) / 2)

        info = verify_arrangement(blue_result, total_result)

        print(f"計算時間: {end_time - start_time:.6f}秒")
        print()

        print("結果:")
        print(f"  青いディスクの数: {blue_result:,}")
        print(f"  全体のディスク数: {total_result:,}")
        print(f"  赤いディスクの数: {info['red']:,}")
        print()

        print("検証:")
        print(f"  確率: {info['prob_both_blue']:.20f}")
        print(f"  正確に1/2: {info['is_exactly_half']}")
        print(
            f"  数式検証: 2×{blue_result}×{blue_result - 1} = {info['formula_left']:,}"
        )
        print(
            f"             {total_result}×{total_result - 1} = {info['formula_right']:,}"
        )
        print(f"  数式一致: {info['formula_valid']}")
        print(f"  制約充足: {total_result > 10**12}")
        print()

        # 最適性の確認
        if total_result > 10**12:
            # 前の解も表示
            print("前の解との比較:")
            prev_x = 2 * blue_result - 1
            prev_y = 2 * total_result - 1

            # 逆算で前の解を求める
            # (x', y') = (3x + 4y, 2x + 3y) の逆は
            # x = 3x' - 4y', y = -2x' + 3y'
            x_prev = 3 * prev_x - 4 * prev_y
            y_prev = -2 * prev_x + 3 * prev_y

            # 符号の調整が必要な場合がある
            if x_prev < 0:
                x_prev = -x_prev
                y_prev = -y_prev

            blue_prev = (x_prev + 1) // 2
            total_prev = (y_prev + 1) // 2

            if blue_prev > 0 and total_prev > 0:
                print(f"  前の解: 青={blue_prev:,}, 全体={total_prev:,}")
                print(f"  制約充足: {total_prev > 10**12}")


def main() -> None:
    """メイン関数"""
    runner = Problem100Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem100Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
