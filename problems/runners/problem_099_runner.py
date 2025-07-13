#!/usr/bin/env python3
"""
Problem 099 Runner: Execution and demonstration code for Problem 099.

This module handles the execution and demonstration of Problem 099 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_099 import (
    compare_exponentials_logarithmic,
    compare_exponentials_naive,
    get_exponential_info,
    load_base_exp_data,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem099Runner(BaseProblemRunner):
    """Runner for Problem 099: Largest exponential."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "099",
            "Largest exponential",
            709,  # Expected answer for the problem
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 099."""
        return [
            # Test with main data file
            ("p099_base_exp.txt",),
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 099."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ("p099_base_exp.txt",)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 099."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_exponential_comparison,
                self.demonstrate_logarithmic_approach,
                self.demonstrate_data_analysis,
                self.demonstrate_algorithm_optimization,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 099の概要を説明"""
        print("=== Problem 099: Largest exponential ===")
        print()
        print("目標: 1000個の base^exponent ペアから最大値を持つ行番号を見つける")
        print()
        print("問題の特徴:")
        print("- 巨大な指数（300万桁以上）")
        print("- 直接計算は不可能")
        print("- 対数を使った比較が必要")
        print("- 精度とパフォーマンスの両立")
        print()
        print("例:")
        print("2^11 = 2048 vs 3^7 = 2187")
        print("632382^518061 vs 519432^525806 (どちらも300万桁以上)")
        print()

    def demonstrate_exponential_comparison(self) -> None:
        """指数比較を説明"""
        print("=== 指数比較の課題 ===")
        print()

        # 小さな例での比較
        print("小さな例での比較:")
        examples = [
            (2, 11, 3, 7),
            (5, 3, 2, 8),
            (10, 5, 6, 7),
        ]

        for base1, exp1, base2, exp2 in examples:
            naive_result = compare_exponentials_naive(base1, exp1, base2, exp2)
            log_result = compare_exponentials_logarithmic(base1, exp1, base2, exp2)

            val1 = base1**exp1
            val2 = base2**exp2

            print(f"  {base1}^{exp1} = {val1} vs {base2}^{exp2} = {val2}")
            print(f"    素直な比較: {naive_result}")
            print(f"    対数比較: {log_result}")
            print(
                f"    実際の大小: {'>' if val1 > val2 else '<' if val1 < val2 else '='}"
            )
            print()

        print("大きな例の課題:")
        # ファイルから最初の2つを読み込み
        try:
            pairs = load_base_exp_data()
            if len(pairs) >= 2:
                base1, exp1 = pairs[0]
                base2, exp2 = pairs[1]

                info1 = get_exponential_info(base1, exp1)
                info2 = get_exponential_info(base2, exp2)

                print(f"  {base1}^{exp1} (~{info1['estimated_digits']:,} digits)")
                print(f"  {base2}^{exp2} (~{info2['estimated_digits']:,} digits)")
                print("  → 直接計算は不可能！")
                print()
        except Exception as e:
            print(f"  データファイル読み込みエラー: {e}")
            print()

    def demonstrate_logarithmic_approach(self) -> None:
        """対数アプローチを説明"""
        print("=== 対数を使った解法 ===")
        print()

        print("数学的原理:")
        print("a^b vs c^d を比較したい場合")
        print("→ log(a^b) vs log(c^d) を比較")
        print("→ b*log(a) vs d*log(c) を比較")
        print()

        print("利点:")
        print("1. 計算量が大幅に削減 O(1)")
        print("2. オーバーフローしない")
        print("3. 高精度な比較が可能")
        print()

        # 実際の例で説明
        print("具体例:")
        try:
            pairs = load_base_exp_data()
            if len(pairs) >= 5:
                for i in range(5):
                    base, exp = pairs[i]
                    info = get_exponential_info(base, exp)
                    print(f"  Line {i + 1}: {base}^{exp}")
                    print(
                        f"    log value = {exp} * log({base}) = {info['log_value']:.6f}"
                    )
                    print(f"    推定桁数: {info['estimated_digits']:,}")
                    print()
        except Exception as e:
            print(f"  データ解析エラー: {e}")

    def demonstrate_data_analysis(self) -> None:
        """データ分析を説明"""
        print("=== データ分析 ===")
        print()

        try:
            pairs = load_base_exp_data()
            print(f"総データ数: {len(pairs)} ペア")
            print()

            # 統計情報
            bases = [base for base, exp in pairs]
            exponents = [exp for base, exp in pairs]

            print("統計情報:")
            print(f"  Base範囲: {min(bases):,} - {max(bases):,}")
            print(f"  Exponent範囲: {min(exponents):,} - {max(exponents):,}")
            print(f"  Base平均: {sum(bases) / len(bases):.0f}")
            print(f"  Exponent平均: {sum(exponents) / len(exponents):.0f}")
            print()

            # 最大・最小の推定桁数
            log_values = []
            estimated_digits = []

            for base, exp in pairs:
                info = get_exponential_info(base, exp)
                log_values.append(info["log_value"])
                estimated_digits.append(info["estimated_digits"])

            print("推定桁数分析:")
            print(f"  最小桁数: {min(estimated_digits):,}")
            print(f"  最大桁数: {max(estimated_digits):,}")
            print(f"  平均桁数: {sum(estimated_digits) / len(estimated_digits):.0f}")
            print()

            # トップ5を表示
            import math

            sorted_pairs = sorted(
                enumerate(pairs, 1),
                key=lambda x: x[1][1] * math.log(x[1][0]),
                reverse=True,
            )

            print("上位5つの指数 (log値順):")
            for i, (line_num, (base, exp)) in enumerate(sorted_pairs[:5]):
                info = get_exponential_info(base, exp)
                print(
                    f"  {i + 1}. Line {line_num}: {base}^{exp} "
                    f"(log={info['log_value']:.6f})"
                )
            print()

        except Exception as e:
            print(f"データ分析エラー: {e}")

    def demonstrate_algorithm_optimization(self) -> None:
        """アルゴリズム最適化を説明"""
        print("=== アルゴリズム最適化 ===")
        print()

        print("最適化戦略:")
        print()

        print("1. 対数比較の利用:")
        print("   - 直接計算: O(exp) → 対数計算: O(1)")
        print("   - メモリ使用量の削減")
        print()

        print("2. ストリーミング処理:")
        print("   - 全データをメモリに保持しない")
        print("   - ファイルを1行ずつ処理")
        print("   - 空間計算量: O(n) → O(1)")
        print()

        print("3. 早期終了:")
        print("   - 現在の最大値より明らかに小さい場合の最適化")
        print("   - ただし、対数計算が十分高速なので効果は限定的")
        print()

        # パフォーマンス比較
        print("計算量比較:")
        print("素直な解法: O(n * max_exp) - 実用不可")
        print("最適化解法: O(n) - 実用的")
        print("数学的解法: O(n) + ストリーミング - 最適")
        print()

    def demonstrate_final_analysis(self) -> None:
        """最終的な分析結果を表示"""
        print("=== 最終分析 ===")
        print()

        print("アルゴリズムの特徴:")
        print("- 対数変換による大数処理")
        print("- 線形時間での最大値検索")
        print("- メモリ効率的な実装")
        print()

        print("実装のポイント:")
        print("- math.log()の精度を活用")
        print("- ファイルI/Oの最適化")
        print("- エラーハンドリング")
        print()

        # メイン問題を解く
        print("メイン問題の解答:")
        import time

        start_time = time.time()
        result = solve_mathematical()
        end_time = time.time()

        print(f"最大指数の行番号: {result}")
        print(f"計算時間: {end_time - start_time:.6f}秒")
        print()

        # 結果の詳細分析
        try:
            pairs = load_base_exp_data()
            if result > 0 and result <= len(pairs):
                base, exp = pairs[result - 1]
                info = get_exponential_info(base, exp)

                print("最大指数の詳細:")
                print(f"  Line {result}: {base}^{exp}")
                print(f"  Log値: {info['log_value']:.10f}")
                print(f"  推定桁数: {info['estimated_digits']:,}")
                print(f"  Base log: {info['base_log']:.10f}")
                print()

                # 近隣との比較
                print("近隣行との比較:")
                for offset in [-2, -1, 0, 1, 2]:
                    idx = result - 1 + offset
                    if 0 <= idx < len(pairs):
                        b, e = pairs[idx]
                        info = get_exponential_info(b, e)
                        marker = " ← 最大" if offset == 0 else ""
                        print(
                            f"  Line {idx + 1}: {b}^{e} "
                            f"(log={info['log_value']:.6f}){marker}"
                        )

        except Exception as e:
            print(f"結果分析エラー: {e}")


def main() -> None:
    """メイン関数"""
    runner = Problem099Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem099Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
