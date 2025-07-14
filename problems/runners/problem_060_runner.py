#!/usr/bin/env python3
"""
Problem 060 Runner: Prime pair sets

素数ペア集合の探索と分析を実行するランナーです。
"""

from collections.abc import Callable
from typing import Any

from problems.problem_060 import (
    demonstrate_example_set,
    find_prime_pair_sets_by_size,
    get_prime_pair_details,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem060Runner(BaseProblemRunner):
    """Problem 060: Prime pair sets のランナークラス"""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "060",
            "Prime pair sets",
            26033,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """
        テストケースを取得
        小さなサイズでの素数ペア集合のテストケースを提供
        """
        return [
            # (set_size, prime_limit, expected_minimum_result_type)
            (2, 50, int),  # サイズ2の集合、制限50
            (3, 100, int),  # サイズ3の集合、制限100
            (2, 20, int),  # より小さな制限でのテスト
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """解法関数を取得"""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """メイン問題のパラメータを取得"""
        return (5, 10000)  # サイズ5、制限10000

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """デモンストレーション関数を取得"""
        return [
            self._demonstrate_example_analysis,
            self._demonstrate_progressive_search,
            self._demonstrate_pair_analysis,
        ]

    def _demonstrate_example_analysis(self) -> None:
        """問題で与えられた例の詳細分析"""
        print("=== 問題例の詳細分析 ===")

        demo = demonstrate_example_set()
        print(f"例の素数集合: {demo['prime_set']}")
        print(f"集合の和: {demo['sum']}")
        print(f"集合サイズ: {demo['size']}")
        print(f"完全な素数ペア集合: {demo['is_valid_complete_set']}")
        print(f"総ペア数: {demo['total_pairs']}")
        print(f"有効ペア数: {demo['valid_pairs']}")

        print("\n各ペアの連結結果:")
        for pair_key, pair_info in demo["pair_analysis"].items():
            p1, p2 = pair_key.split(",")
            concat1, concat2 = pair_info["concatenations"]
            prime1, prime2 = pair_info["both_prime"]
            valid = pair_info["valid_pair"]

            print(
                f"  {p1} + {p2}: {concat1} ({'素数' if prime1 else '合成数'}), "
                f"{p2} + {p1}: {concat2} ({'素数' if prime2 else '合成数'}) "
                f"→ {'✓' if valid else '✗'}"
            )

    def _demonstrate_progressive_search(self) -> None:
        """段階的な探索のデモンストレーション"""
        print("=== 段階的な素数ペア集合探索 ===")

        # サイズ2から4まで探索
        results = find_prime_pair_sets_by_size(max_size=4, prime_limit=1000)

        for size, result in results.items():
            print(f"\nサイズ {size} の最小素数ペア集合:")
            print(f"  集合: {result['set']}")
            print(f"  和: {result['sum']}")
            print(f"  検証済み: {result['verified']}")

            # 詳細分析
            details = get_prime_pair_details(result["set"])
            print(f"  有効ペア率: {details['valid_pairs']}/{details['total_pairs']}")

    def _demonstrate_pair_analysis(self) -> None:
        """素数ペアの性質分析"""
        print("=== 素数ペアの性質分析 ===")

        # いくつかの小さな素数ペアの例を分析
        small_primes = [3, 7, 11, 13, 17, 19, 23, 29, 31]

        print("小さな素数での素数ペア関係:")
        pair_count = 0
        total_checked = 0

        for i in range(len(small_primes)):
            for j in range(i + 1, len(small_primes)):
                p1, p2 = small_primes[i], small_primes[j]

                # 連結結果を計算
                concat1 = int(str(p1) + str(p2))
                concat2 = int(str(p2) + str(p1))

                # 素数判定
                from problems.problem_060 import is_prime

                is_prime1 = is_prime(concat1)
                is_prime2 = is_prime(concat2)
                is_pair = is_prime1 and is_prime2

                total_checked += 1
                if is_pair:
                    pair_count += 1
                    print(
                        f"  {p1}, {p2}: {concat1} ({'P' if is_prime1 else 'C'}), "
                        f"{concat2} ({'P' if is_prime2 else 'C'}) ✓"
                    )

        print(
            f"\n素数ペア率: {pair_count}/{total_checked} "
            f"({100 * pair_count / total_checked:.1f}%)"
        )

        # 特殊な性質の分析
        print("\n特殊な性質:")
        print("- 連結順序に依存する対称性")
        print("- 桁数が異なる素数の組み合わせ効果")
        print("- 末尾桁が偶数の場合の制約（2を除く）")

    def run_problem(self) -> Any:
        """
        メイン問題を実行
        """
        print(f"=== Problem {self.problem_number}: {self.problem_title} ===")
        print()

        # 各解法の実行とパフォーマンス比較
        solution_functions = self.get_solution_functions()
        main_params = self.get_main_parameters()

        print(
            f"メイン問題: サイズ{main_params[0]}の素数ペア集合を探索（制限: {main_params[1]}）"
        )
        print()

        results = []
        for name, func in solution_functions:
            try:
                print(f"{name}を実行中...")
                result = func(*main_params)
                results.append(result)
                print(f"{name}: {result}")
            except Exception as e:
                print(f"{name}: エラー - {e}")
                results.append(0)

        # 結果の一致確認
        if results and len(set(results)) <= 1:
            print(f"\n✓ すべての解法が一致: {results[0]}")
            final_result = results[0]
        else:
            print(f"\n⚠ 解法間で結果が異なる: {results}")
            final_result = results[0] if results else 0

        print()

        # デモンストレーション実行
        demonstrations = self.get_demonstration_functions()
        if demonstrations:
            for demo_func in demonstrations:
                try:
                    demo_func()
                    print()
                except Exception as e:
                    print(f"デモンストレーションエラー: {e}")
                    print()

        return final_result

    def main(self) -> None:
        """メインエントリーポイント"""
        print(f"=== Problem {self.problem_number} Runner ===")
        print()

        # 基本テスト実行
        print("=== 基本機能テスト ===")
        test_cases = self.get_test_cases()
        solution_functions = self.get_solution_functions()

        all_passed = True
        for i, test_case in enumerate(test_cases):
            set_size, prime_limit, expected_type = test_case
            print(f"\nテスト {i + 1}: サイズ{set_size}, 制限{prime_limit}")

            for name, func in solution_functions:
                try:
                    result = func(set_size, prime_limit)
                    if isinstance(result, expected_type) and result > 0:
                        print(f"  {name}: ✓ ({result})")
                    else:
                        print(f"  {name}: ✗ 予期しない結果: {result}")
                        all_passed = False
                except Exception as e:
                    print(f"  {name}: ✗ エラー - {e}")
                    all_passed = False

        if all_passed:
            print("\n✓ 全ての基本テストが通過しました")
        else:
            print("\n✗ 一部のテストが失敗しました")

        print()

        # メイン問題実行
        self.run_problem()

        print("=== 実行完了 ===")


def main() -> None:
    """エントリーポイント"""
    runner = Problem060Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem060Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
