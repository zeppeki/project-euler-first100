#!/usr/bin/env python3
"""
Problem 069 Runner: Execution and demonstration code for Problem 069.

This module handles the execution and demonstration of Problem 069 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_069 import (
    analyze_totient_pattern,
    get_totient_ratio,
    solve_mathematical,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem069Runner(BaseProblemRunner):
    """Runner for Problem 069: Totient maximum."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "069",
            "Totient maximum",
            510510,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 069."""
        return [
            (10, 6),  # 小さな例: n≤10でn/φ(n)が最大となるのは6
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 069."""
        return [
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
            # 注意: solve_naiveは1,000,000まででは実用的でないため除外
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 069."""
        return [self._demonstrate_totient_analysis]

    def _demonstrate_totient_analysis(self) -> None:
        """オイラーのφ関数とn/φ(n)比率の分析を表示"""
        print("Euler's Totient Function Analysis:")
        print("=" * 50)

        # 小さな例での分析
        print("\nn ≤ 20 でのφ(n)とn/φ(n)の値:")
        print("n  | φ(n) | n/φ(n) | 素因数")
        print("---|------|--------|--------")

        pattern_data = analyze_totient_pattern(20)
        from problems.lib.primes import get_prime_factors

        for n, phi_n, ratio in pattern_data:
            factors = sorted(get_prime_factors(n))
            factors_str = "×".join(map(str, factors)) if factors else "1"
            print(f"{n:2d} | {phi_n:4d} | {ratio:6.3f} | {factors_str}")

        # 最大比率の数値を特定
        max_ratio_data = max(pattern_data, key=lambda x: x[2])
        print(
            f"\nn ≤ 20 で最大比率: n={max_ratio_data[0]}, ratio={max_ratio_data[2]:.3f}"
        )

        print("\nオイラーのφ関数の性質:")
        print("- φ(n) = nと互いに素な数（≤n）の個数")
        print("- 素数pの場合: φ(p) = p - 1")
        print("- 素数の積の場合: φ(p₁×p₂×...×pₖ) = (p₁-1)×(p₂-1)×...×(pₖ-1)")
        print("- 一般式: φ(n) = n × ∏(1 - 1/p) for all prime factors p")

        print("\nn/φ(n)比率の最大化:")
        print("- n/φ(n)が大きい ⟺ φ(n)が小さい")
        print("- φ(n)が小さい ⟺ nが多くの異なる小さな素因数を持つ")
        print("- 最適解: n = 2×3×5×7×11×... (小さな素数の積)")

        # 素数の積による分析
        print("\n小さな素数の積による分析:")
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        product = 1

        for _i, p in enumerate(primes):
            product *= p
            if product <= 1000000:
                ratio = get_totient_ratio(product)
                print(f"2×3×...×{p} = {product:6d}, ratio = {ratio:.6f}")
            else:
                print(f"2×3×...×{p} = {product:6d} > 1,000,000")
                break

        print("\nアルゴリズム比較:")
        print("- 素直な解法: O(n²log n) - 各数値についてGCDベースでφ(n)計算")
        print("- 最適化解法: O(n√n) - 素因数分解ベースでφ(n)計算")
        print("- 数学的解法: O(π(√n)) - 素数の積による直接計算")

        print("\n数学的洞察:")
        print("- n/φ(n) = ∏(p/(p-1)) for all prime factors p")
        print("- 小さな素因数ほど比率への寄与が大きい")
        print("- 例: 2/(2-1) = 2.0, 3/(3-1) = 1.5, 5/(5-1) = 1.25")
        print("- 最大値は連続する小さな素数の積で達成される")

        # 実際の問題の解を計算
        print("\n実際の問題（n ≤ 1,000,000）:")
        try:
            result = solve_mathematical(1000000)
            ratio = get_totient_ratio(result)
            factors = sorted(get_prime_factors(result))
            print(f"最大比率を持つn: {result}")
            print(f"比率 n/φ(n): {ratio:.6f}")
            print(f"素因数: {' × '.join(map(str, factors))}")
        except Exception as e:
            print(f"計算エラー: {e}")

        print("\n学習ポイント:")
        print("- 数論関数の性質と最適化")
        print("- 素因数分解の応用")
        print("- 数学的洞察による計算量削減")
        print("- 組み合わせ最適化問題への数学的アプローチ")


def main() -> None:
    """メイン関数"""
    runner = Problem069Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem069Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
