#!/usr/bin/env python3
"""
Problem 095 Runner: Execution and demonstration code for Problem 095.

This module handles the execution and demonstration of Problem 095 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_095 import (
    compute_divisor_sums,
    find_all_amicable_chains,
    find_chain_length,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    sum_of_proper_divisors,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem095Runner(BaseProblemRunner):
    """Runner for Problem 095: Amicable chains."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "095",
            "Amicable chains",
            14316,  # Expected answer for limit 1,000,000
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 095."""
        return [
            (1000, 220),  # Small test case
            (10000, 220),  # Medium test case
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 095."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 095."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_divisor_sums,
                self.demonstrate_amicable_chains,
                self.demonstrate_chain_building,
                self.demonstrate_solution_approaches,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 095の概要を説明"""
        print("=== Problem 095: Amicable chains ===")
        print()
        print("目標: 最長の友愛連鎖の最小メンバーを見つける")
        print()
        print("定義:")
        print("- 真の約数: ある数の約数のうち、その数自身を除いたもの")
        print("- 完全数: 真の約数の和が自分自身と等しい数（例: 28 = 1+2+4+7+14）")
        print("- 友愛数: 互いに相手の真の約数の和になる数のペア（例: 220と284）")
        print("- 友愛連鎖: 真の約数の和を繰り返し計算することで元の数に戻る連鎖")
        print()
        print("例: 12496 → 14288 → 15472 → 14536 → 14264 → 12496")
        print("これは長さ5の友愛連鎖")
        print()
        print("制約: 連鎖の要素は100万を超えない")
        print()

    def demonstrate_divisor_sums(self) -> None:
        """約数の和の計算を説明"""
        print("=== 約数の和の計算 ===")
        print()

        # 個別の例
        test_numbers = [28, 220, 284, 12496]
        print("個別の例:")
        for n in test_numbers:
            sum_div = sum_of_proper_divisors(n)
            print(f"  sum_of_proper_divisors({n}) = {sum_div}")

            # 約数を表示
            divisors = []
            for i in range(1, n):
                if n % i == 0:
                    divisors.append(i)
            print(f"    約数: {divisors}")
        print()

        # 効率的な計算方法
        print("効率的な計算方法:")
        print("- 個別計算: O(√n) - 平方根までチェック")
        print("- 一括計算: O(n log n) - ふるい法的アプローチ")
        print()

        # 一括計算の例
        limit = 30
        divisor_sums = compute_divisor_sums(limit)
        print(f"1から{limit}までの約数和（一括計算）:")
        for i in range(1, min(11, limit + 1)):
            print(f"  divisor_sum[{i}] = {divisor_sums[i]}")
        print("  ...")
        print()

    def demonstrate_amicable_chains(self) -> None:
        """友愛連鎖の例を説明"""
        print("=== 友愛連鎖の例 ===")
        print()

        # 異なる長さの連鎖
        examples = [
            (6, "完全数（長さ1の連鎖）"),
            (220, "友愛数（長さ2の連鎖）"),
            (12496, "長さ5の連鎖"),
        ]

        divisor_sums = compute_divisor_sums(100000)

        for start, description in examples:
            print(f"{description} - {start}から開始:")
            chain: list[int] = []
            current = start
            seen: set[int] = set()

            while current not in seen and len(chain) < 10:
                chain.append(current)
                seen.add(current)
                if current < len(divisor_sums):
                    current = divisor_sums[current]
                else:
                    break

            # 連鎖を表示
            chain_str = " → ".join(map(str, chain[:6]))
            if len(chain) > 6:
                chain_str += " → ..."
            if current == start:
                chain_str += f" → {start}"
            print(f"  {chain_str}")

            if current == start:
                print(f"  長さ: {len(chain)}")
            else:
                print("  連鎖にならない")
            print()

    def demonstrate_chain_building(self) -> None:
        """連鎖構築アルゴリズムを説明"""
        print("=== 連鎖構築アルゴリズム ===")
        print()

        divisor_sums = compute_divisor_sums(20000)

        # 12496から連鎖を構築
        start = 12496
        print(f"{start}から連鎖を構築:")
        chain_length, chain = find_chain_length(start, divisor_sums, 20000)

        if chain_length > 0:
            print(f"  連鎖: {chain}")
            print(f"  長さ: {chain_length}")
            print(f"  最小要素: {min(chain)}")
        print()

        # 連鎖構築の終了条件
        print("連鎖構築の終了条件:")
        print("1. 開始数に戻る → 友愛連鎖発見")
        print("2. 開始数より小さい数に到達 → 既に処理済みの連鎖")
        print("3. 制限を超える数に到達 → 無効な連鎖")
        print("4. 既に訪問した数に到達（開始数以外）→ ループだが友愛連鎖ではない")
        print("5. 0または1に到達 → 連鎖終了")
        print()

    def demonstrate_solution_approaches(self) -> None:
        """各解法のアプローチを説明"""
        print("=== 解法アプローチの比較 ===")
        print()

        print("1. 素直な解法:")
        print("   - 各数について約数和を個別に計算")
        print("   - 時間計算量: O(n * √n)")
        print("   - 実装が簡単だが、大きな制限では遅い")
        print()

        print("2. 最適化解法:")
        print("   - 約数和を事前に一括計算")
        print("   - ふるい法的アプローチで効率化")
        print("   - 時間計算量: O(n log n)")
        print("   - メモリを使うが大幅に高速化")
        print()

        print("3. 数学的解法:")
        print("   - この問題では特別な数学的ショートカットはない")
        print("   - 最適化解法と同じアプローチ")
        print()

        # 小規模テストで比較
        test_limit = 10000
        print(f"テスト（制限: {test_limit}）:")

        chains = find_all_amicable_chains(test_limit)
        print(f"  見つかった連鎖の数: {len(chains)}")

        if chains:
            max_chain = chains[0]  # Already sorted by length
            print("  最長連鎖:")
            print(f"    長さ: {max_chain[0]}")
            print(f"    最小要素: {min(max_chain[1])}")
            print(f"    連鎖の最初の5要素: {max_chain[1][:5]}...")
        print()

    def demonstrate_final_analysis(self) -> None:
        """最終的な分析結果を表示"""
        print("=== 最終分析 ===")
        print()

        print("アルゴリズムの特徴:")
        print("- 約数和の効率的な計算が鍵")
        print("- 既に処理した連鎖を記録して重複を避ける")
        print("- 連鎖の終了条件を正確に判定")
        print()

        print("実装のポイント:")
        print("- ふるい法による約数和の一括計算")
        print("- 効率的な連鎖追跡アルゴリズム")
        print("- メモリと計算時間のトレードオフ")
        print()

        print("計算量の分析:")
        print("- 時間計算量: O(n log n) - 約数和の計算が支配的")
        print("- 空間計算量: O(n) - 約数和の配列")
        print("- 実用的な計算時間で100万までの制限も処理可能")
        print()

        print("最終結果:")
        result = solve_mathematical(1000000)
        print(f"100万以下の最長友愛連鎖の最小メンバー: {result}")
        print()

        # 中規模での検証
        test_limit = 100000
        chains = find_all_amicable_chains(test_limit)
        print(f"検証（制限 {test_limit}）:")
        print(f"  見つかった連鎖数: {len(chains)}")

        if chains and len(chains) >= 3:
            print("  上位3つの連鎖:")
            for i, (length, chain) in enumerate(chains[:3]):
                print(
                    f"    {i + 1}. 長さ{length}, 最小要素{min(chain)}: {chain[:4]}..."
                )
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem095Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem095Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
