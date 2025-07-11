#!/usr/bin/env python3
"""
Problem 098 Runner: Execution and demonstration code for Problem 098.

This module handles the execution and demonstration of Problem 098 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_098 import (
    apply_mapping,
    find_anagram_pairs,
    find_square_anagram_pairs,
    get_letter_mapping,
    get_sorted_letters,
    is_perfect_square,
    load_words,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem098Runner(BaseProblemRunner):
    """Runner for Problem 098: Anagramic squares."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "098",
            "Anagramic squares",
            18769,  # Expected answer for the problem
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 098."""
        return [
            # Test with data file name
            ("p098_words.txt",),
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 098."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ("p098_words.txt",)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 098."""
        if self.enable_demonstrations:
            return [
                self.demonstrate_problem_overview,
                self.demonstrate_anagram_detection,
                self.demonstrate_square_mapping,
                self.demonstrate_constraint_checking,
                self.demonstrate_algorithm_optimization,
                self.demonstrate_final_analysis,
            ]
        return None

    def demonstrate_problem_overview(self) -> None:
        """Problem 098の概要を説明"""
        print("=== Problem 098: Anagramic squares ===")
        print()
        print("目標: アナグラムペアの単語を平方数に変換して、最大の平方数を見つける")
        print()
        print("問題の特徴:")
        print("- 同じ文字で構成される単語のペア（アナグラム）")
        print("- 各文字を数字に置き換えて平方数を作る")
        print("- 同じ置き換えルールで両方の単語が平方数になる")
        print("- 先頭が0になってはいけない")
        print("- 各文字は異なる数字に対応する")
        print()
        print("例: CARE と RACE")
        print("C=1, A=2, R=9, E=6 とすると")
        print("CARE = 1296 = 36²")
        print("RACE = 9216 = 96²")
        print()

    def demonstrate_anagram_detection(self) -> None:
        """アナグラム検出を説明"""
        print("=== アナグラム検出 ===")
        print()

        # Load sample words
        words = load_words()
        print(f"単語数: {len(words)}")
        print()

        # Show anagram detection process
        print("アナグラム検出の仕組み:")
        print("1. 各単語の文字をアルファベット順にソート")
        print("2. 同じソート結果を持つ単語をグループ化")
        print("3. 2つ以上の単語があるグループからペアを作成")
        print()

        # Demonstrate with examples
        example_words = ["CARE", "RACE", "ACRE", "SILENT", "LISTEN", "ENLIST"]
        print("例:")
        for word in example_words:
            sorted_letters = get_sorted_letters(word)
            print(f"  {word} → {sorted_letters}")
        print()

        # Find actual anagram pairs
        pairs = find_anagram_pairs(words)
        print(f"発見されたアナグラムペア数: {len(pairs)}")
        print()

        print("いくつかのアナグラムペア:")
        for i, (word1, word2) in enumerate(pairs):
            if i >= 10:
                break
            print(f"  {word1} ↔ {word2}")

        if len(pairs) > 10:
            print(f"  ... 他に{len(pairs) - 10}ペア")
        print()

    def demonstrate_square_mapping(self) -> None:
        """平方数マッピングを説明"""
        print("=== 平方数マッピング ===")
        print()

        print("文字→数字マッピングの制約:")
        print("1. 各文字は異なる数字に対応")
        print("2. 数字の先頭は0であってはいけない")
        print("3. 両方の単語が平方数になる")
        print()

        # Manual example
        print("手動例: CARE と RACE")
        print("試行: C=1, A=2, R=9, E=6")
        print("CARE → 1296 = 36² ✓")
        print("RACE → 9216 = 96² ✓")
        print()

        # Show mapping validation
        word1, word2 = "CARE", "RACE"
        square1, square2 = 1296, 9216

        print("マッピング検証:")
        mapping = get_letter_mapping(word1, word2, square1, square2)
        if mapping:
            print("マッピング:")
            for letter, digit in sorted(mapping.items()):
                print(f"  {letter} → {digit}")

            # Apply mapping
            mapped1 = apply_mapping(word1, mapping)
            mapped2 = apply_mapping(word2, mapping)
            if mapped1 is not None and mapped2 is not None:
                print(f"{word1} → {mapped1} (√{mapped1} = {int(mapped1**0.5)})")
                print(f"{word2} → {mapped2} (√{mapped2} = {int(mapped2**0.5)})")
                print(
                    f"両方とも平方数: {is_perfect_square(mapped1) and is_perfect_square(mapped2)}"
                )
        print()

    def demonstrate_constraint_checking(self) -> None:
        """制約チェックを説明"""
        print("=== 制約チェック ===")
        print()

        print("無効な例:")
        print()

        # Example 1: Leading zero
        print("1. 先頭0の例:")
        print("   WORD → 0123 (無効: 先頭が0)")
        print()

        # Example 2: Duplicate mapping
        print("2. 重複マッピングの例:")
        print("   A=1, B=1 (無効: 同じ数字に複数の文字)")
        print()

        # Example 3: Non-square result
        print("3. 非平方数の例:")
        print("   WORD → 1234 (無効: 1234は平方数ではない)")
        print()

        # Show validation process
        print("検証プロセス:")
        print("1. 文字数が一致するかチェック")
        print("2. 先頭文字が0にならないかチェック")
        print("3. 文字→数字マッピングが一意かチェック")
        print("4. 結果が平方数かチェック")
        print()

        # Demonstrate with real examples
        test_cases = [
            ("AB", "BA", 16, 61),  # Valid
            ("AB", "BA", 10, 1),  # Invalid: would create leading zero
            ("AB", "CD", 16, 25),  # Valid if letters don't conflict
        ]

        print("テストケース:")
        for word1, word2, num1, num2 in test_cases:
            mapping = get_letter_mapping(word1, word2, num1, num2)
            valid = mapping is not None
            print(f"  {word1}={num1}, {word2}={num2}: {'有効' if valid else '無効'}")
        print()

    def demonstrate_algorithm_optimization(self) -> None:
        """アルゴリズム最適化を説明"""
        print("=== アルゴリズム最適化 ===")
        print()

        print("最適化戦略:")
        print()

        print("1. 文字数別グループ化:")
        print("   - 同じ文字数の単語のみをペアで考慮")
        print("   - 異なる文字数の平方数は無視")
        print()

        print("2. 平方数の事前生成:")
        print("   - 各文字数に対して可能な平方数を事前計算")
        print("   - 範囲: 10^(n-1) ≤ square < 10^n")
        print()

        print("3. 早期終了:")
        print("   - 無効なマッピングを早期検出")
        print("   - 制約違反時の即座リターン")
        print()

        # Demonstrate range calculation
        print("文字数別平方数範囲:")
        for length in range(2, 6):
            min_val = 10 ** (length - 1)
            max_val = 10**length - 1
            min_root = int(min_val**0.5)
            max_root = int(max_val**0.5) + 1

            squares = []
            for root in range(min_root, max_root + 1):
                square = root * root
                if min_val <= square <= max_val:
                    squares.append(square)

            print(f"  {length}文字: {len(squares)}個の平方数 (例: {squares[:3]}...)")
        print()

        # Performance comparison
        print("計算量比較:")
        print("素直な解法: O(n × m × s²)")
        print("最適化解法: O(n × m × s)")
        print("ここで n=単語ペア数, m=文字数, s=平方数")
        print()

    def demonstrate_final_analysis(self) -> None:
        """最終的な分析結果を表示"""
        print("=== 最終分析 ===")
        print()

        print("アルゴリズムの特徴:")
        print("- 組み合わせ最適化問題")
        print("- 制約満足問題の要素")
        print("- 文字列処理とのハイブリッド")
        print()

        print("実装のポイント:")
        print("- 効率的なアナグラム検出")
        print("- 制約チェックの最適化")
        print("- メモリ効率的な平方数生成")
        print()

        print("計算量の分析:")
        print("- アナグラム検出: O(n × m log m)")
        print("- 平方数マッピング: O(n × m × s)")
        print("- 全体: O(n × m × s)")
        print()

        # Solve main problem
        print("メイン問題の解答:")
        import time

        start_time = time.time()
        result = solve_mathematical()
        end_time = time.time()

        print(f"最大の平方数: {result}")
        print(f"計算時間: {end_time - start_time:.3f}秒")
        print()

        # Show some examples
        words = load_words()
        pairs = find_anagram_pairs(words)
        square_pairs = find_square_anagram_pairs(words[:100])  # Limited for demo

        print("発見された平方数アナグラムペア例:")
        if square_pairs:
            for word1, word2, square1, square2 in square_pairs[:3]:
                print(f"  {word1}={square1} (√{square1}={int(square1**0.5)})")
                print(f"  {word2}={square2} (√{square2}={int(square2**0.5)})")
                print()
        else:
            print("  (最初の100単語では見つからず)")
        print()

        print("統計:")
        print(f"- 総単語数: {len(words)}")
        print(f"- アナグラムペア数: {len(pairs)}")
        print(f"- 平方数ペア数: {len(square_pairs)} (限定データ)")
        print()


def main() -> None:
    """メイン関数"""
    runner = Problem098Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem098Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
