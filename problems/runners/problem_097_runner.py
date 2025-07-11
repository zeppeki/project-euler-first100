#!/usr/bin/env python3
"""
Problem 097 Runner: Execution and demonstration code for Problem 097.

This module handles the execution and demonstration of Problem 097 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_097 import (
    modular_exponentiation,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    verify_small_case,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem097Runner(BaseProblemRunner):
    """Runner for Problem 097: Large non-Mersenne prime."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "097",
            "Large non-Mersenne prime",
            8739992577,  # Expected answer for 28433 × 2^7830457 + 1 mod 10^10
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 097."""
        return [
            # Test with default parameters (main problem)
            (),
            # Test with small custom parameters
            (3, 5, 1),  # 3 × 2^5 + 1 = 97
            (7, 10, 3),  # 7 × 2^10 + 3 = 7171
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 097."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()  # Use default parameters

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 097."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_modular_arithmetic,
                self.demonstrate_modular_exponentiation,
                self.demonstrate_large_numbers,
                self.demonstrate_algorithm_comparison,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 097の概要を説明"""
        print("=== Problem 097: Large non-Mersenne prime ===")
        print()
        print("目標: 非Mersenne素数 28433 × 2^7830457 + 1 の末尾10桁を求める")
        print()
        print("背景:")
        print("- 2004年に発見された2,357,207桁の巨大な非Mersenne素数")
        print("- Mersenne素数: 2^p - 1 の形の素数")
        print("- 非Mersenne素数: それ以外の形の素数")
        print()
        print("問題の特徴:")
        print("- 非常に大きな数の計算（2^7830457は約236万桁）")
        print("- 直接計算は不可能、モジュラー算術が必要")
        print("- 末尾10桁のみを求める（mod 10^10）")
        print()

    def demonstrate_modular_arithmetic(self) -> None:
        """モジュラー算術の基本を説明"""
        print("=== モジュラー算術の基本 ===")
        print()
        print("基本性質:")
        print("(a + b) mod m = ((a mod m) + (b mod m)) mod m")
        print("(a × b) mod m = ((a mod m) × (b mod m)) mod m")
        print("(a^b) mod m は特別なアルゴリズムが必要")
        print()

        # Simple examples
        print("例:")
        a, b, m = 123, 456, 100
        print(f"({a} + {b}) mod {m} = {(a + b) % m}")
        print(f"({a} × {b}) mod {m} = {(a * b) % m}")
        print()

        # Why modular arithmetic is needed
        print("なぜモジュラー算術が必要か:")
        print("- 28433 × 2^7830457 + 1 は約236万桁の巨大な数")
        print("- メモリ上で直接計算することは不可能")
        print("- 末尾10桁のみが必要なので、mod 10^10 で計算")
        print()

    def demonstrate_modular_exponentiation(self) -> None:
        """モジュラー冪乗アルゴリズムを説明"""
        print("=== モジュラー冪乗アルゴリズム ===")
        print()
        print("問題: a^b mod m を効率的に計算する")
        print("素直な方法: a^b を計算してから mod m → 指数が大きいと不可能")
        print("効率的な方法: バイナリ指数法（Binary Exponentiation）")
        print()

        print("バイナリ指数法の原理:")
        print("- 指数を2進数で表現")
        print("- 各ビットに対して、結果を2乗して更新")
        print("- ビットが1の場合、ベースを掛ける")
        print()

        # Demonstrate with small example
        base, exp, mod = 3, 13, 1000
        print(f"例: {base}^{exp} mod {mod}")
        print(f"{exp} = 1101₂ (2進数)")
        print()

        # Step by step calculation
        result = 1
        current_base = base
        current_exp = exp
        step = 1

        print("計算ステップ:")
        while current_exp > 0:
            if current_exp % 2 == 1:
                result = (result * current_base) % mod
                print(f"ステップ{step}: 指数が奇数, result = {result}")
            else:
                print(f"ステップ{step}: 指数が偶数, resultは変更なし")
            current_exp //= 2
            current_base = (current_base * current_base) % mod
            step += 1

        print(f"最終結果: {result}")

        # Verify with our implementation
        our_result = modular_exponentiation(base, exp, mod)
        builtin_result = pow(base, exp, mod)
        print(f"自作関数: {our_result}")
        print(f"組み込み関数: {builtin_result}")
        print(f"一致: {result == our_result == builtin_result}")
        print()

    def demonstrate_large_numbers(self) -> None:
        """大きな数の処理を説明"""
        print("=== 大きな数の処理 ===")
        print()
        print("メイン問題の規模:")
        print("- 指数: 7,830,457")
        print("- 2^7830457 の桁数: 約2,357,207桁")
        print("- 全体の数値: 約236万桁")
        print()

        # Calculate some properties
        import math

        exp = 7830457
        digits = int(exp * math.log10(2)) + 1
        print(f"2^{exp} の概算桁数: {digits:,}")
        print(f"この数をテキストファイルで保存すると約 {digits / (1024 * 1024):.1f} MB")
        print()

        print("計算時間の比較:")
        print("- 直接計算: 不可能（メモリ不足）")
        print("- モジュラー冪乗: O(log 指数) = O(log 7830457) ≈ 23ステップ")
        print()

        # Demonstrate performance with smaller examples
        print("性能デモ（小さな例）:")
        test_cases = [
            (2, 100, 10**10),
            (2, 1000, 10**10),
            (2, 10000, 10**10),
        ]

        import time

        for base, exp_test, mod in test_cases:
            start_time = time.time()
            result = modular_exponentiation(base, exp_test, mod)
            end_time = time.time()
            print(
                f"  {base}^{exp_test} mod {mod} = {result} ({end_time - start_time:.6f}秒)"
            )
        print()

    def demonstrate_algorithm_comparison(self) -> None:
        """アルゴリズム比較を説明"""
        print("=== アルゴリズム比較 ===")
        print()

        print("3つの解法の比較:")
        print("1. 素直な解法 (solve_naive):")
        print("   - Python組み込みのpow()関数を使用")
        print("   - pow(a, b, m)は内部的に高速なアルゴリズムを使用")
        print("   - 最も簡潔だが内部動作は見えない")
        print()

        print("2. 最適化解法 (solve_optimized):")
        print("   - 自作のモジュラー冪乗関数を使用")
        print("   - アルゴリズムの動作が明確")
        print("   - 教育的価値が高い")
        print()

        print("3. 数学的解法 (solve_mathematical):")
        print("   - この問題では最適化解法と同一")
        print("   - モジュラー冪乗が最も数学的に効率的")
        print()

        # Performance comparison with small cases
        print("性能比較（小さなテストケース）:")
        test_mult, test_exp, test_add = 123, 1000, 7

        import time

        start_time = time.time()
        result1 = solve_naive(test_mult, test_exp, test_add)
        time1 = time.time() - start_time

        start_time = time.time()
        result2 = solve_optimized(test_mult, test_exp, test_add)
        time2 = time.time() - start_time

        start_time = time.time()
        result3 = solve_mathematical(test_mult, test_exp, test_add)
        time3 = time.time() - start_time

        print(f"  素直な解法: {result1} ({time1:.6f}秒)")
        print(f"  最適化解法: {result2} ({time2:.6f}秒)")
        print(f"  数学的解法: {result3} ({time3:.6f}秒)")
        print(f"  結果一致: {result1 == result2 == result3}")
        print()

    def demonstrate_final_analysis(self) -> None:
        """最終的な分析結果を表示"""
        print("=== 最終分析 ===")
        print()

        print("アルゴリズムの特徴:")
        print("- 数論・モジュラー算術の応用")
        print("- バイナリ指数法による効率化")
        print("- 大きな数の処理技術")
        print()

        print("実装のポイント:")
        print("- モジュラー算術の性質の活用")
        print("- オーバーフローの回避")
        print("- 効率的なビット操作")
        print()

        print("計算量の分析:")
        print("- 時間計算量: O(log 指数)")
        print("- 空間計算量: O(1)")
        print("- 実際の計算時間: 1ミリ秒未満")
        print()

        # Solve the main problem
        print("メイン問題の解答:")
        import time

        start_time = time.time()
        result = solve_mathematical()
        end_time = time.time()

        print(f"28433 × 2^7830457 + 1 の末尾10桁: {result}")
        print(f"計算時間: {end_time - start_time:.6f}秒")
        print()

        print("結果の検証:")
        result_naive = solve_naive()
        result_optimized = solve_optimized()
        print(f"素直な解法: {result_naive}")
        print(f"最適化解法: {result_optimized}")
        print(f"数学的解法: {result}")
        print(f"全解法一致: {result_naive == result_optimized == result}")
        print()

        # Additional verification with small cases
        print("小さな例での検証:")
        small_cases = [
            (3, 5, 1),  # 3 × 2^5 + 1 = 97
            (7, 10, 3),  # 7 × 2^10 + 3 = 7171
        ]

        for mult, exp, add in small_cases:
            expected = verify_small_case(mult, exp, add)
            calculated = solve_mathematical(mult, exp, add)
            print(
                f"  {mult} × 2^{exp} + {add}: 期待値={expected}, 計算値={calculated}, 一致={expected == calculated}"
            )
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem097Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem097Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
