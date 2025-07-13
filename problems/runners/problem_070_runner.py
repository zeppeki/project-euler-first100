#!/usr/bin/env python3
"""
Problem 070 Runner: Execution and demonstration code for Problem 070.

This module handles the execution and demonstration of Problem 070 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_070 import (
    analyze_totient_permutation_example,
    euler_totient,
    find_totient_permutations,
    is_permutation,
    solve_mathematical,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem070Runner(BaseProblemRunner):
    """Runner for Problem 070: Totient permutation."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "070",
            "Totient permutation",
            8319823,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 070."""
        return [
            (100, 21),  # 小さな例: n<100でφ(n)がnの順列となる最小比率のn
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 070."""
        return [
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
            # 注意: solve_naiveは10^7まででは実用的でないため除外
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (10000000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 070."""
        return [self._demonstrate_totient_permutation_analysis]

    def _demonstrate_totient_permutation_analysis(self) -> None:
        """トーシェント順列の分析を表示"""
        print("Totient Permutation Analysis:")
        print("=" * 50)

        # 問題文の例の分析
        print("\n問題文の例（87109）の分析:")
        n_example, phi_example, ratio_example = analyze_totient_permutation_example()
        print(f"n = {n_example}")
        print(f"φ(n) = {phi_example}")
        print(f"順列確認: {is_permutation(n_example, phi_example)}")
        print(f"比率 n/φ(n) = {ratio_example:.6f}")

        print("\nトーシェント順列の特徴:")
        print("- φ(n)とnが同じ桁の並び替えになる")
        print("- 比率 n/φ(n) を最小化する")
        print("- 範囲: 1 < n < 10^7")

        print("\n数学的洞察:")
        print("- n/φ(n)を最小化するには、nが2つの近い素数の積である必要がある")
        print("- p, qが素数の場合: φ(p×q) = (p-1)×(q-1)")
        print("- p ≈ q ≈ √n の時、n/φ(n) ≈ n/((√n-1)²) が最小")

        # 小規模な例での分析
        print("\n小規模範囲での分析（n < 10000）:")
        small_results = find_totient_permutations(10000, max_results=5)

        if small_results:
            print("上位5つの結果:")
            print("n      | φ(n)   | n/φ(n)  | 素因数")
            print("-------|--------|---------|--------")

            from problems.lib.primes import get_prime_factors

            for n, phi_n, ratio in small_results:
                factors = sorted(get_prime_factors(n))
                factors_str = "×".join(map(str, factors))
                print(f"{n:6d} | {phi_n:6d} | {ratio:7.4f} | {factors_str}")
        else:
            print("小規模範囲では該当する例が見つかりません")

        print("\n素数ペアによる最適化:")
        print("- √10^7 ≈ 3162 付近の素数に焦点")
        print("- 近い素数ペア (p, q) で p×q < 10^7 を探索")
        print("- φ(p×q) = (p-1)×(q-1) を直接計算")

        # 理論的な最小比率の分析
        sqrt_limit = int(10000000**0.5)
        print(f"\n理論的分析（√10^7 ≈ {sqrt_limit}）:")
        print(f"- p ≈ q ≈ {sqrt_limit} の場合")
        print(f"- n ≈ {sqrt_limit}² = {sqrt_limit**2}")
        print(f"- φ(n) ≈ ({sqrt_limit}-1)² = {(sqrt_limit - 1) ** 2}")
        print(f"- 理論的最小比率 ≈ {sqrt_limit**2 / (sqrt_limit - 1) ** 2:.6f}")

        print("\nアルゴリズム比較:")
        print("- 素直な解法: O(n√n) - 10^7まで全探索（実用的でない）")
        print("- 最適化解法: O(π(√n)²) - 素数ペアの組み合わせ")
        print("- 数学的解法: O(π(√n)²) - √n付近に焦点を絞った探索")

        print("\n探索戦略:")
        print("1. √limit付近の素数を生成")
        print("2. 素数ペア (p, q) で p×q < limit を探索")
        print("3. φ(p×q) = (p-1)×(q-1) を計算")
        print("4. 順列チェックと最小比率更新")

        # 実際の問題の解を計算（時間がかかる可能性があるため注意）
        print("\n実際の問題の解（n < 10^7）:")
        try:
            # 小さめの範囲でテスト
            test_result = solve_mathematical(100000)
            if test_result > 0:
                phi_test = euler_totient(test_result)
                ratio_test = test_result / phi_test
                print("テスト範囲（n < 100,000）の結果:")
                print(f"n = {test_result}")
                print(f"φ(n) = {phi_test}")
                print(f"比率 = {ratio_test:.6f}")
            else:
                print("テスト範囲では該当する値が見つかりません")
        except Exception as e:
            print(f"計算エラー: {e}")

        print("\n学習ポイント:")
        print("- トーシェント関数の応用")
        print("- 数値の桁並び替え判定")
        print("- 素数ペアによる最適化")
        print("- 大規模探索における効率化技法")


def main() -> None:
    """メイン関数"""
    runner = Problem070Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem070Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
