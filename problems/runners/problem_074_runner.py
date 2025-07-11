#!/usr/bin/env python3
"""
Problem 074 Runner: Execution and demonstration code for Problem 074.

This module handles the execution and demonstration of Problem 074 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_074 import (
    count_chains_by_length,
    find_chains_with_length,
    get_factorial_chain,
    get_factorial_chain_statistics,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


def verify_known_chains() -> dict[int, tuple[int, list[int]]]:
    """
    既知のチェーンを検証し、結果を返す
    """
    known_chains = {}

    # 145: 145 → 1!+4!+5! = 145 (length 1)
    chain_145 = get_factorial_chain(145)
    known_chains[145] = (len(chain_145), chain_145)

    # 169: 169 → 363601 → 1454 → 169 (length 3)
    chain_169 = get_factorial_chain(169)
    known_chains[169] = (len(chain_169), chain_169)

    # 871: 871 → 45361 → 871 (length 2)
    chain_871 = get_factorial_chain(871)
    known_chains[871] = (len(chain_871), chain_871)

    return known_chains


class Problem074Runner(BaseProblemRunner):
    """Runner for Problem 074: Digit factorial chains."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "074",
            "Digit factorial chains",
            402,  # Expected answer: 402 chains with exactly 60 non-repeating terms
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 074."""
        return [
            (1000, 0),  # No 60-term chains below 1000
            (10000, 42),  # 42 chains with 60 terms below 10000
            (100000, 42),  # 42 chains with 60 terms below 100000
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 074."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 074."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_factorial_chains,
                self.demonstrate_known_examples,
                self.demonstrate_chain_analysis,
                self.demonstrate_solution_approaches,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 074の概要を説明"""
        print("=== Problem 074: Digit factorial chains ===")
        print()
        print("目標: ちょうど60の重複しない項を持つ階乗チェーンの数を求める")
        print("範囲: 100万未満の開始数値")
        print()
        print("階乗チェーンとは:")
        print("- 各桁の階乗の和を次の項とする数列")
        print("- 例: 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145")
        print("- 最終的にループに入る")
        print()
        print("重複しない項の数:")
        print("- ループが始まるまでの異なる項の個数")
        print("- 目標: ちょうど60項")
        print()

    def demonstrate_factorial_chains(self) -> None:
        """階乗チェーンの基本概念を説明"""
        print("=== 階乗チェーンの基本概念 ===")
        print()

        # 桁の階乗の事前計算を表示
        print("桁の階乗（0! から 9!）:")
        factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        for i, f in enumerate(factorials):
            print(f"  {i}! = {f:,}")
        print()

        # 基本的なチェーンの例
        print("基本的なチェーンの例:")
        examples = [69, 78, 145]
        for num in examples:
            chain = get_factorial_chain(num, 10)
            print(f"  {num} → ", end="")
            for i, val in enumerate(chain[:-1]):
                if i > 0:
                    print(" → ", end="")
                print(val, end="")
            if len(chain) > 1 and chain[-1] in chain[:-1]:
                print(f" → {chain[-1]} (ループ)")
            else:
                print()
        print()

    def demonstrate_known_examples(self) -> None:
        """既知の特別な例を説明"""
        print("=== 既知の特別な例 ===")
        print()

        known_results = verify_known_chains()
        interesting_cases = [145, 169, 871, 872, 69]

        for num in interesting_cases:
            if num in known_results:
                length, chain = known_results[num]
                print(f"数値 {num}:")
                print(f"  チェーン長: {length}")
                print("  チェーン: ", end="")
                for i, val in enumerate(chain[:5]):  # 最初の5項のみ表示
                    if i > 0:
                        print(" → ", end="")
                    print(val, end="")
                if len(chain) > 5:
                    print(" → ...")
                elif len(chain) > 1 and chain[-1] in chain[:-1]:
                    print(f" → {chain[-1]} (ループ)")
                print()
        print()

    def demonstrate_chain_analysis(self) -> None:
        """チェーンの分析を実演"""
        print("=== チェーン分析 ===")
        print()

        # 小規模での統計
        print("小規模分析 (1-1000):")
        stats = get_factorial_chain_statistics(1000)
        print(f"  分析対象数: {stats['total_numbers_analyzed']:,}")
        print(f"  異なるチェーン長: {stats['unique_chain_lengths']}")
        print(f"  最短チェーン長: {stats['shortest_chain_length']}")
        print(f"  最長チェーン長: {stats['longest_chain_length']}")
        print(
            f"  最頻チェーン長: {stats['most_common_length']} ({stats['most_common_count']} 個)"
        )
        print()

        # チェーン長分布
        print("チェーン長分布 (1-10000):")
        length_counts = count_chains_by_length(10000)
        sorted_lengths = sorted(length_counts.items())
        for length, count in sorted_lengths:
            if count > 50 or length >= 55:  # 重要なもののみ表示
                print(f"  長さ {length:2d}: {count:4d} 個")
        print()

    def demonstrate_solution_approaches(self) -> None:
        """各解法のアプローチを説明"""
        print("=== 解法アプローチの比較 ===")
        print()

        test_limit = 10000
        print(f"テスト範囲: 1 から {test_limit:,}")
        print()

        print("1. 素直な解法:")
        print("   各数値のチェーン長を直接計算")
        print("   時間計算量: O(n × k) where k is average chain length")
        result_naive = solve_naive(test_limit)
        print(f"   結果: {result_naive} 個のチェーン")
        print()

        print("2. 最適化解法:")
        print("   メモ化を使用して効率化")
        print("   時間計算量: O(n × k) with memoization speedup")
        result_optimized = solve_optimized(test_limit)
        print(f"   結果: {result_optimized} 個のチェーン")
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

        print("60項チェーンの検索:")
        print("目標: ちょうど60の重複しない項を持つチェーンの数")
        print()

        # 段階的に範囲を拡大
        test_ranges = [1000, 10000, 100000]
        for limit in test_ranges:
            count = len(find_chains_with_length(60, limit))
            print(f"1 から {limit:,} の範囲: {count} 個のチェーン")

        print()
        print("100万未満での最終計算:")
        final_count = solve_optimized(1000000)
        print(f"結果: {final_count} 個のチェーン")
        print()

        print("60項チェーンの特徴:")
        sixty_term_examples = find_chains_with_length(60, 100000)[:5]
        print("最初の5つの例:")
        for i, num in enumerate(sixty_term_examples, 1):
            print(f"  {i}. {num:,}")

        print()
        print("パフォーマンス考察:")
        print("- メモ化により大幅な高速化を実現")
        print("- 100万の範囲でも実用的な速度")
        print("- 60項チェーンは比較的まれ（約0.04%）")
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem074Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem074Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
