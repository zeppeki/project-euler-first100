#!/usr/bin/env python3
"""
Problem 054 Runner: Execution and demonstration code for Problem 054.

This module handles the execution and demonstration of Problem 054 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_054 import (
    analyze_poker_data,
    demonstrate_hand_evaluation,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    test_example_hands,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem054Runner(BaseProblemRunner):
    """Runner for Problem 054: Poker hands."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "054", "Poker hands", 376, enable_performance_test, enable_demonstrations
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 054."""
        # Since we have external data file, we'll use the example verification
        # The actual test will verify the example hands work correctly
        return [
            # Test that example hands evaluate correctly
            # This is tested through the test_example_hands function
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 054."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()  # No parameters needed as functions read from file

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 054."""
        return [
            self._demonstrate_poker_hands,
            self._demonstrate_hand_evaluation_examples,
            self._demonstrate_poker_statistics,
        ]

    def run_tests(self) -> bool:
        """Run custom tests for poker hand evaluation."""
        print("=== ポーカーハンド評価テスト ===")

        # Test the example hands from problem description
        print("例題ハンドの検証...")
        if not test_example_hands():
            print("✗ 例題ハンドの評価が失敗しました")
            return False
        print("✓ 例題ハンドの評価が正しく動作しています")

        # Test that all solution functions return the same result
        print("\n解法一致性テスト...")
        try:
            result_naive = solve_naive()
            result_optimized = solve_optimized()
            result_mathematical = solve_mathematical()

            if result_naive == result_optimized == result_mathematical:
                print(f"✓ 全ての解法が一致: {result_naive}")
                return True
            print(
                f"✗ 解法が一致しません: naive={result_naive}, optimized={result_optimized}, mathematical={result_mathematical}"
            )
            return False
        except Exception as e:
            print(f"✗ テスト実行エラー: {e}")
            return False

    def _demonstrate_poker_hands(self) -> None:
        """ポーカーハンドの基本的な評価をデモンストレーション"""
        print("ポーカーハンド評価デモンストレーション:")

        examples = demonstrate_hand_evaluation()

        for hand_str, description, evaluation in examples:
            print(f"  {hand_str:<15} | {description:<25} | {evaluation}")

    def _demonstrate_hand_evaluation_examples(self) -> None:
        """問題文の例題ハンドを詳細に分析"""
        print("問題文例題の詳細分析:")

        from problems.problem_054 import PokerHand

        examples = [
            (
                "5H 5C 6S 7S KD",
                "2C 3S 8S 8D TD",
                "Player 2",
                "Pair of Eights beats Pair of Fives",
            ),
            (
                "5D 8C 9S JS AC",
                "2C 5C 7D 8S QH",
                "Player 1",
                "High card Ace beats High card Queen",
            ),
            (
                "2D 9C AS AH AC",
                "3D 6D 7D TD QD",
                "Player 2",
                "Flush beats Three of a Kind",
            ),
            (
                "4D 6S 9H QH QC",
                "3D 6D 7H QD QS",
                "Player 1",
                "Pair of Queens with Nine beats Pair of Queens with Seven",
            ),
            (
                "2H 2D 4C 4D 4S",
                "3C 3D 3S 9S 9D",
                "Player 1",
                "Full House with Three Fours beats Full House with Three Threes",
            ),
        ]

        for i, (player1_str, player2_str, expected_winner, explanation) in enumerate(
            examples, 1
        ):
            player1_hand = PokerHand.from_string(player1_str)
            player2_hand = PokerHand.from_string(player2_str)

            player1_wins = player1_hand.beats(player2_hand)
            actual_winner = "Player 1" if player1_wins else "Player 2"

            print(f"\n  例題 {i}: {explanation}")
            print(
                f"    Player 1: {player1_str} -> {player1_hand.evaluation.hand_rank.name.replace('_', ' ').title()}"
            )
            print(
                f"    Player 2: {player2_str} -> {player2_hand.evaluation.hand_rank.name.replace('_', ' ').title()}"
            )
            print(
                f"    勝者: {actual_winner} {'✓' if actual_winner == expected_winner else '✗'}"
            )

    def _demonstrate_poker_statistics(self) -> None:
        """ポーカーデータの統計分析"""
        print("ポーカーデータ統計分析:")

        stats = analyze_poker_data()

        if "error" in stats:
            print(f"  エラー: {stats['error']}")
            return

        print(f"  総ゲーム数: {stats['total_games']:,}")
        print(f"  Player 1勝利数: {stats['player1_wins']:,}")
        print(f"  Player 2勝利数: {stats['player2_wins']:,}")
        print(f"  Player 1勝率: {stats['player1_win_rate']:.1%}")

        print("\n  ハンドランク分布:")
        for rank_name, counts in stats["hand_rank_distribution"].items():
            total = counts["player1"] + counts["player2"]
            if total > 0:
                rank_display = rank_name.replace("_", " ").title()
                print(
                    f"    {rank_display:<20}: {total:>3} ({counts['player1']:>3} vs {counts['player2']:>3})"
                )

    def run_problem(self) -> Any:
        """
        Run the main problem with custom logic for poker hands.

        Override the base method to handle the no-parameter case properly.
        """
        from problems.utils.display import print_final_answer, print_solution_header
        from problems.utils.performance import compare_performance

        # Print problem header
        print_solution_header(
            self.problem_number, self.problem_title, "1000 poker hands"
        )

        # Get solution functions
        functions = self.get_solution_functions()
        if not functions:
            print("エラー: 解法関数が定義されていません")
            return None

        # Create wrapper functions that accept no parameters
        wrapped_functions = [(name, lambda f=func: f()) for name, func in functions]

        # Run performance comparison with no parameters
        performance_results = compare_performance(wrapped_functions)

        # Display performance results
        from problems.utils.display import print_performance_comparison

        print_performance_comparison(performance_results)

        # Verify all solutions agree
        results = [data["result"] for data in performance_results.values()]
        verified = len(set(results)) == 1

        # Display final answer
        final_result = results[0] if results else None
        print_final_answer(final_result, verified=verified)

        # Run demonstrations if available
        demonstrations = self.get_demonstration_functions()
        if demonstrations:
            print("\n=== 追加デモンストレーション ===")
            for demo_func in demonstrations:
                try:
                    demo_func()
                    print()
                except Exception as e:
                    print(f"デモンストレーションエラー: {e}")
                    print()

        return final_result


def main() -> None:
    """メイン関数"""
    runner = Problem054Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem054Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
