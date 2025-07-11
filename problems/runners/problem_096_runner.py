#!/usr/bin/env python3
"""
Problem 096 Runner: Execution and demonstration code for Problem 096.

This module handles the execution and demonstration of Problem 096 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_096 import (
    get_top_left_number,
    is_valid_move,
    load_sudoku_puzzles,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    solve_single_puzzle,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem096Runner(BaseProblemRunner):
    """Runner for Problem 096: Su Doku."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "096",
            "Su Doku",
            24702,  # Expected answer for all 50 puzzles (corrected data)
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 096."""
        return [
            # Test with data file name
            ("p096_sudoku.txt",),
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 096."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ("p096_sudoku.txt",)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 096."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_sudoku_rules,
                self.demonstrate_solving_algorithm,
                self.demonstrate_backtracking,
                self.demonstrate_optimization,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 096の概要を説明"""
        print("=== Problem 096: Su Doku ===")
        print()
        print("目標: 50個の数独パズルを解き、各解の左上3桁の数字の合計を求める")
        print()
        print("数独のルール:")
        print("- 9×9のグリッドを数字1-9で埋める")
        print("- 各行に1-9が一度ずつ")
        print("- 各列に1-9が一度ずつ")
        print("- 各3×3ボックスに1-9が一度ずつ")
        print()
        print("制約:")
        print("- すべてのパズルは一意解を持つ")
        print("- 初期値として一部のセルが埋められている")
        print("- 0は空のセルを表す")
        print()

    def demonstrate_sudoku_rules(self) -> None:
        """数独のルールと検証を説明"""
        print("=== 数独のルールと検証 ===")
        print()

        # Load puzzles for demonstration
        puzzles = load_sudoku_puzzles()
        if not puzzles:
            print("パズルが読み込めませんでした")
            return

        first_puzzle = puzzles[0]
        print("最初のパズル:")
        for row in first_puzzle:
            print("  " + " ".join(str(cell) if cell != 0 else "." for cell in row))
        print()

        print("ルール検証の例:")
        # Try placing a number and check validity
        test_cases = [
            (0, 0, 4, "行に4が既にある"),
            (0, 0, 1, "列に1が既にある"),
            (0, 0, 7, "3×3ボックスに7が既にある"),
            (0, 0, 5, "配置可能"),
        ]

        for test_row, test_col, test_num, description in test_cases:
            if first_puzzle[test_row][test_col] == 0:  # Only test empty cells
                valid = is_valid_move(first_puzzle, test_row, test_col, test_num)
                print(
                    f"  位置({test_row},{test_col})に{test_num}を配置: {'可能' if valid else '不可能'} - {description}"
                )
        print()

    def demonstrate_solving_algorithm(self) -> None:
        """解法アルゴリズムを説明"""
        print("=== 解法アルゴリズム ===")
        print()

        puzzles = load_sudoku_puzzles()
        if not puzzles:
            return

        # Solve first puzzle step by step
        first_puzzle = puzzles[0]
        print("解法のデモンストレーション:")
        print("元のパズル:")
        for row in first_puzzle:
            print("  " + " ".join(str(cell) if cell != 0 else "." for cell in row))
        print()

        try:
            solved_puzzle = solve_single_puzzle(first_puzzle)
            print("解答:")
            for row in solved_puzzle:
                print("  " + " ".join(str(cell) for cell in row))
            print()

            top_left = get_top_left_number(solved_puzzle)
            print(f"左上3桁の数字: {top_left}")
            print()

        except ValueError as e:
            print(f"解けませんでした: {e}")
            print()

    def demonstrate_backtracking(self) -> None:
        """バックトラッキングアルゴリズムを説明"""
        print("=== バックトラッキングアルゴリズム ===")
        print()

        print("バックトラッキングの基本流れ:")
        print("1. 空のセルを見つける")
        print("2. 1から9まで順番に試す")
        print("3. 配置が有効なら次のセルへ進む")
        print("4. すべてのセルが埋まったら完了")
        print("5. 行き詰まったら前のセルに戻って別の数字を試す")
        print()

        print("効率化のポイント:")
        print("- 各セルで配置可能な数字のみを試行")
        print("- 行・列・ボックスの制約を同時チェック")
        print("- 最小残可能値ヒューリスティック（制約の多いセルから処理）")
        print()

        # Show complexity analysis
        print("計算量分析:")
        print("- 最悪時間計算量: O(9^(n×n)) where n=9")
        print("- 実際はヒューリスティックにより大幅に高速化")
        print("- 空間計算量: O(n×n) 再帰スタック用")
        print()

    def demonstrate_optimization(self) -> None:
        """最適化手法を説明"""
        print("=== 最適化手法 ===")
        print()

        print("1. 基本的なバックトラッキング（素直な解法）:")
        print("   - 左上から順番にセルを処理")
        print("   - 1から9まで順番に試行")
        print("   - 実装が単純だが効率は劣る")
        print()

        print("2. 最小残可能値ヒューリスティック（最適化解法）:")
        print("   - 最も制約の厳しいセルから処理")
        print("   - 早期に矛盾を発見して枝刈り")
        print("   - 大幅な高速化が期待できる")
        print()

        print("3. その他の最適化技法:")
        print("   - 制約伝播（Constraint Propagation）")
        print("   - 隠れた単一候補（Hidden Singles）")
        print("   - 裸の組み合わせ（Naked Pairs/Triples）")
        print("   - X-Wing、Swordfish等の高度な論理推論")
        print()

        # Performance comparison
        puzzles = load_sudoku_puzzles()
        if puzzles and len(puzzles) >= 3:
            print("パフォーマンス比較（最初の3パズル）:")
            import time

            # Test first 3 puzzles for comparison
            test_puzzles = puzzles[:3]

            start_time = time.time()
            count = 0
            for puzzle in test_puzzles:
                try:
                    solve_single_puzzle(puzzle)
                    count += 1
                except ValueError:
                    pass
            optimized_time = time.time() - start_time

            print(f"  最適化解法: {count}パズル解答, {optimized_time:.4f}秒")
            print(f"  平均: {optimized_time / max(count, 1):.4f}秒/パズル")
        print()

    def demonstrate_final_analysis(self) -> None:
        """最終的な分析結果を表示"""
        print("=== 最終分析 ===")
        print()

        print("アルゴリズムの特徴:")
        print("- 組み合わせ最適化問題")
        print("- バックトラッキングによる全探索")
        print("- ヒューリスティックによる効率化")
        print()

        print("実装のポイント:")
        print("- 制約チェックの効率化")
        print("- 再帰の深さ管理")
        print("- メモリ使用量の最適化")
        print("- 数独特有の構造の活用")
        print()

        print("計算量の分析:")
        print("- 理論的時間計算量: O(9^81) = O(9^(n×n))")
        print("- 実際はヒューリスティックで大幅高速化")
        print("- 空間計算量: O(81) = O(n×n) 再帰スタック")
        print("- ほとんどのパズルは1秒以内で解ける")
        print()

        print("最終結果:")
        puzzles = load_sudoku_puzzles()
        print(f"パズル数: {len(puzzles)}")

        try:
            result = solve_mathematical()
            print(f"全50パズルの左上3桁数字の合計: {result}")
        except Exception as e:
            print(f"解答中にエラー: {e}")
        print()

        # Show some solved examples
        if puzzles:
            print("解答例（最初の3パズル）:")
            for i, puzzle in enumerate(puzzles[:3]):
                try:
                    solved = solve_single_puzzle(puzzle)
                    top_left = get_top_left_number(solved)
                    print(f"  パズル{i + 1}: 左上3桁 = {top_left}")
                except ValueError:
                    print(f"  パズル{i + 1}: 解けませんでした")
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem096Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem096Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
