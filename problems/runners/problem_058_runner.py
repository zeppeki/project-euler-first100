#!/usr/bin/env python3
"""
Problem 058 Runner: Spiral primes

This runner provides test cases, performance analysis, and demonstrations
for the spiral primes problem.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_058 import (
    analyze_spiral_pattern,
    get_diagonal_values,
    get_spiral_layer_info,
    is_prime,
    solve_naive,
    solve_optimized,
    verify_example_spiral,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem058Runner(BaseProblemRunner):
    """Runner for Problem 058: Spiral primes"""

    def __init__(self) -> None:
        super().__init__("058", "Spiral primes")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Test cases for spiral primes problem"""
        return [
            # Test with higher target ratios for faster execution
            (0.7, 3),  # Side length 3 has ratio 60% < 70%
            (0.5, 11),  # Side length 11 has ratio 47.62% < 50%
            (0.35, 35),  # Use a higher ratio for faster test
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for performance comparison"""
        return [
            ("solve_naive", solve_naive),
            ("solve_optimized", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Parameters for main problem execution"""
        return (0.1,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Demonstration functions for spiral primes analysis"""
        return [
            self.demonstrate_spiral_construction,
            self.demonstrate_diagonal_analysis,
            self.demonstrate_prime_ratio_progression,
        ]

    def demonstrate_spiral_construction(self) -> None:
        """Demonstrate how the spiral is constructed and diagonal values calculated"""
        print("=== スパイラルの構築と対角線の値 ===")

        # 例の検証
        print("問題文の例（辺の長さ7のスパイラル）の検証:")
        if verify_example_spiral():
            print("✓ 検証成功")
        else:
            print("✗ 検証失敗")

        print("\n小さなスパイラルの対角線の値:")
        print("辺の長さ | 対角線の値")
        print("---------|---------------------------")

        for side_length in range(1, 12, 2):
            diagonal_values = get_diagonal_values(side_length)
            if side_length == 1:
                diagonal_values = [1]  # 特別なケース

            values_str = ", ".join(map(str, diagonal_values))
            print(f"{side_length:8d} | {values_str}")

        print("\n対角線の値の計算式:")
        print("辺の長さ n のスパイラルにおいて、最外層の対角線の値は:")
        print("- 右下: n²")
        print("- 右上: n² - (n-1)")
        print("- 左上: n² - 2(n-1)")
        print("- 左下: n² - 3(n-1)")

    def demonstrate_diagonal_analysis(self) -> None:
        """Demonstrate diagonal value analysis"""
        print("=== 対角線の値の分析 ===")

        # 各層の詳細情報
        print("各層の対角線の値と素数の状態:")
        print("辺の長さ | 層 | 対角線の値 | 素数 | 合成数")
        print("---------|----|-----------|----- |------")

        for side_length in range(1, 14, 2):
            layer_info = get_spiral_layer_info(side_length)

            diagonal_str = ", ".join(map(str, layer_info["diagonal_values"]))
            primes_str = (
                ", ".join(map(str, layer_info["primes"]))
                if layer_info["primes"]
                else "なし"
            )
            non_primes_str = (
                ", ".join(map(str, layer_info["non_primes"]))
                if layer_info["non_primes"]
                else "なし"
            )

            print(
                f"{side_length:8d} | {layer_info['layer']:2d} | {diagonal_str:9s} | {primes_str:4s} | {non_primes_str}"
            )

        print("\n素数の判定:")
        sample_values = [3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]
        for value in sample_values:
            status = "素数" if is_prime(value) else "合成数"
            print(f"  {value:2d}: {status}")

    def demonstrate_prime_ratio_progression(self) -> None:
        """Demonstrate how prime ratio changes as spiral grows"""
        print("=== 素数の割合の変化 ===")

        # 素数の割合の変化を追跡
        analysis = analyze_spiral_pattern(31)

        print("辺の長さ | 対角線の数 | 素数の数 | 割合 | パーセンテージ")
        print("---------|------------|----------|------|-------------")

        for data in analysis:
            side_length = data["side_length"]
            total_count = data["total_count"]
            prime_count = data["prime_count"]
            ratio = data["ratio"]
            percentage = data["percentage"]

            print(
                f"{side_length:8d} | {total_count:10d} | {prime_count:8d} | {ratio:.4f} | {percentage:10.2f}%"
            )

        print("\n10%を下回る最初の辺の長さを探す:")
        target_ratio = 0.1

        for data in analysis:
            if data["ratio"] < target_ratio:
                print(
                    f"辺の長さ {data['side_length']} で初めて10%を下回る: {data['percentage']:.2f}%"
                )
                break
        else:
            print("この範囲では10%を下回る辺の長さは見つかりませんでした")

        print("\n割合の傾向:")
        print("- 初期は素数の割合が高い")
        print("- 辺の長さが増すにつれて素数の割合は減少")
        print("- これは対角線の値が大きくなり、素数の密度が低下するため")

    def demonstrate_performance_comparison(self) -> None:
        """Compare performance between different approaches"""
        print("=== パフォーマンス比較 ===")

        import time

        # 異なる目標比率でのパフォーマンス比較
        test_ratios = [0.3, 0.2, 0.15]

        print("目標比率 | 素直な解法 | 最適化解法 | 結果")
        print("---------|------------|------------|-----")

        for ratio in test_ratios:
            # 素直な解法
            start_time = time.time()
            result_naive = solve_naive(ratio)
            naive_time = time.time() - start_time

            # 最適化解法
            start_time = time.time()
            result_optimized = solve_optimized(ratio)
            optimized_time = time.time() - start_time

            print(
                f"{ratio:8.2f} | {naive_time:10.6f}s | {optimized_time:10.6f}s | {result_naive}"
            )

            # 結果の一致確認
            assert result_naive == result_optimized, (
                f"Results disagree for ratio {ratio}"
            )

        print("\n最適化の効果:")
        print("- 最適化解法は各層の対角線の値を段階的に計算")
        print("- 素直な解法は毎回全ての対角線の値を再計算")
        print("- 大きな目標比率では差は小さいが、小さな目標比率では差が顕著")

    def demonstrate_mathematical_properties(self) -> None:
        """Demonstrate mathematical properties of the spiral"""
        print("=== スパイラルの数学的性質 ===")

        print("対角線の値の性質:")
        print("1. 右下の対角線: 奇数の平方数 (1, 9, 25, 49, ...)")
        print("2. 他の対角線: 平方数から一定の間隔で減少")
        print("3. 各層で4つの新しい対角線の値が追加される")

        print("\n対角線の値の計算:")
        print("辺の長さ n (n は奇数) において:")
        print("- 右下: n²")
        print("- 右上: n² - (n-1)")
        print("- 左上: n² - 2(n-1)")
        print("- 左下: n² - 3(n-1)")

        print("\n具体例（辺の長さ 5）:")
        side_length = 5
        diagonal_values = get_diagonal_values(side_length)
        n = side_length

        print(f"- 右下: {n}² = {n**2}")
        print(f"- 右上: {n}² - ({n}-1) = {n**2} - {n - 1} = {n**2 - (n - 1)}")
        print(
            f"- 左上: {n}² - 2({n}-1) = {n**2} - {2 * (n - 1)} = {n**2 - 2 * (n - 1)}"
        )
        print(
            f"- 左下: {n}² - 3({n}-1) = {n**2} - {3 * (n - 1)} = {n**2 - 3 * (n - 1)}"
        )
        print(f"実際の値: {diagonal_values}")

        print("\n素数の分布:")
        print("- 大きな数になるほど素数の密度は低下")
        print("- 素数定理により、n周辺の素数の密度は約1/ln(n)")
        print("- 対角線の値が大きくなるにつれて素数の割合は減少")


def main() -> None:
    """Main execution function"""
    # Verify example spiral first
    if not verify_example_spiral():
        print("警告: 例のスパイラルの検証に失敗しました")
        return

    # Run the problem
    runner = Problem058Runner()
    runner.main()


if __name__ == "__main__":
    main()
