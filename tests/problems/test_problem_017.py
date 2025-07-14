#!/usr/bin/env python3
"""
Test for Problem 017: Number Letter Counts
"""

import pytest

from problems.problem_017 import (
    count_letters,
    number_to_words,
    solve_naive,
    solve_optimized,
)


class TestProblem017:
    """Problem 017のテストクラス"""

    def test_number_to_words_single_digits(self) -> None:
        """一桁の数字のテスト"""
        test_cases = [
            (1, "one"),
            (2, "two"),
            (3, "three"),
            (4, "four"),
            (5, "five"),
            (6, "six"),
            (7, "seven"),
            (8, "eight"),
            (9, "nine"),
        ]

        for num, expected in test_cases:
            assert number_to_words(num) == expected, f"Failed for {num}"

    def test_number_to_words_teens(self) -> None:
        """10代の数字のテスト"""
        test_cases = [
            (10, "ten"),
            (11, "eleven"),
            (12, "twelve"),
            (13, "thirteen"),
            (14, "fourteen"),
            (15, "fifteen"),
            (16, "sixteen"),
            (17, "seventeen"),
            (18, "eighteen"),
            (19, "nineteen"),
        ]

        for num, expected in test_cases:
            assert number_to_words(num) == expected, f"Failed for {num}"

    def test_number_to_words_tens(self) -> None:
        """10の倍数のテスト"""
        test_cases = [
            (20, "twenty"),
            (30, "thirty"),
            (40, "forty"),
            (50, "fifty"),
            (60, "sixty"),
            (70, "seventy"),
            (80, "eighty"),
            (90, "ninety"),
        ]

        for num, expected in test_cases:
            assert number_to_words(num) == expected, f"Failed for {num}"

    def test_number_to_words_compound_tens(self) -> None:
        """合成された10の位のテスト"""
        test_cases = [
            (21, "twenty one"),
            (35, "thirty five"),
            (42, "forty two"),
            (56, "fifty six"),
            (67, "sixty seven"),
            (78, "seventy eight"),
            (89, "eighty nine"),
            (99, "ninety nine"),
        ]

        for num, expected in test_cases:
            assert number_to_words(num) == expected, f"Failed for {num}"

    def test_number_to_words_hundreds(self) -> None:
        """100の位のテスト"""
        test_cases = [
            (100, "one hundred"),
            (200, "two hundred"),
            (500, "five hundred"),
            (900, "nine hundred"),
        ]

        for num, expected in test_cases:
            assert number_to_words(num) == expected, f"Failed for {num}"

    def test_number_to_words_hundreds_with_and(self) -> None:
        """100の位 + "and" のテスト"""
        test_cases = [
            (101, "one hundred and one"),
            (115, "one hundred and fifteen"),
            (342, "three hundred and forty two"),
            (999, "nine hundred and ninety nine"),
        ]

        for num, expected in test_cases:
            assert number_to_words(num) == expected, f"Failed for {num}"

    def test_number_to_words_thousand(self) -> None:
        """1000のテスト"""
        assert number_to_words(1000) == "one thousand"

    def test_number_to_words_edge_cases(self) -> None:
        """エッジケースのテスト"""
        # 境界値
        with pytest.raises(ValueError):
            number_to_words(0)

        with pytest.raises(ValueError):
            number_to_words(1001)

        with pytest.raises(ValueError):
            number_to_words(-1)

    def test_count_letters(self) -> None:
        """文字数カウントのテスト"""
        test_cases = [
            ("one", 3),
            ("twelve", 6),
            ("twenty one", 9),  # スペースは除外
            ("forty two", 8),  # スペースは除外
            ("one hundred and fifteen", 20),  # スペースは除外
            ("three hundred and forty two", 23),  # スペースは除外
            ("one thousand", 11),  # スペースは除外
        ]

        for text, expected in test_cases:
            assert count_letters(text) == expected, f"Failed for '{text}'"

    def test_solve_naive(self) -> None:
        """素直な解法のテスト"""
        test_cases = [
            (1, 3),  # "one" = 3
            (2, 6),  # "one" + "two" = 3 + 3 = 6
            (5, 19),  # "one" + "two" + "three" + "four" + "five" = 3+3+5+4+4 = 19
            (
                10,
                39,
            ),  # 1-5 + "six"(3) + "seven"(5) + "eight"(5) + "nine"(4) + "ten"(3) = 19+20 = 39
            (20, 112),  # 予想される値
        ]

        for limit, expected in test_cases:
            assert solve_naive(limit) == expected, f"Failed for limit {limit}"

    def test_solve_optimized(self) -> None:
        """最適化解法のテスト"""
        test_cases = [
            (1, 3),  # "one" = 3
            (2, 6),  # "one" + "two" = 3 + 3 = 6
            (5, 19),  # "one" + "two" + "three" + "four" + "five" = 3+3+5+4+4 = 19
            (10, 39),  # 計算される値
            (20, 112),  # 予想される値
        ]

        for limit, expected in test_cases:
            assert solve_optimized(limit) == expected, f"Failed for limit {limit}"

    def test_all_solutions_agree(self) -> None:
        """すべての解法が同じ結果を返すことを確認"""
        test_cases = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

        for limit in test_cases:
            result_naive = solve_naive(limit)
            result_optimized = solve_optimized(limit)

            assert result_naive == result_optimized, (
                f"Solutions disagree for limit {limit}: "
                f"naive={result_naive}, optimized={result_optimized}"
            )

    def test_edge_cases(self) -> None:
        """エッジケースのテスト"""
        # 最小値
        assert solve_naive(1) == 3
        assert solve_optimized(1) == 3

        # 最大値
        result_1000 = solve_naive(1000)
        assert solve_optimized(1000) == result_1000

    def test_specific_examples(self) -> None:
        """問題文の具体例のテスト"""
        # 1-5の例: one, two, three, four, five → 3+3+5+4+4 = 19
        assert solve_naive(5) == 19
        assert solve_optimized(5) == 19

        # 342 = "three hundred and forty two" = 23 letters
        assert count_letters(number_to_words(342)) == 23

        # 115 = "one hundred and fifteen" = 20 letters
        assert count_letters(number_to_words(115)) == 20

    def test_british_usage(self) -> None:
        """イギリス式表記のテスト"""
        # 100以上の数では "and" を使用
        assert "and" in number_to_words(101)
        assert "and" in number_to_words(115)
        assert "and" in number_to_words(342)
        assert "and" in number_to_words(999)

        # 100の倍数では "and" を使用しない
        assert "and" not in number_to_words(100)
        assert "and" not in number_to_words(200)
        assert "and" not in number_to_words(500)
        assert "and" not in number_to_words(900)

    def test_letter_count_validation(self) -> None:
        """文字数カウントの妥当性検証"""
        # 各数値の文字数が妥当であることを確認
        for i in range(1, 101):
            words = number_to_words(i)
            letters = count_letters(words)

            # 文字数は正の数
            assert letters > 0, f"Letter count for {i} should be positive"

            # 文字数は妥当な範囲内（最長でも50文字以内）
            assert letters <= 50, (
                f"Letter count for {i} is unexpectedly large: {letters}"
            )

    def test_cumulative_properties(self) -> None:
        """累積的性質のテスト"""
        # 範囲が拡大すると文字数も増加する
        results = []
        for limit in [1, 5, 10, 20, 50, 100]:
            result = solve_naive(limit)
            results.append(result)
            assert result > 0, (
                f"Total letter count should be positive for limit {limit}"
            )

        # 単調増加であることを確認
        for i in range(1, len(results)):
            assert results[i] > results[i - 1], (
                "Results should be monotonically increasing"
            )

    @pytest.mark.slow
    def test_performance(self) -> None:
        """パフォーマンステスト"""
        # 大きな数での実行時間テスト（機能検証ベース）
        limit = 1000

        # すべての解法が同じ結果を返すことを確認
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)

        assert result_naive == result_optimized
        assert result_naive > 0  # 正の数であることを確認
        assert result_naive < 100000  # 妥当な範囲内であることを確認

    def test_solution_consistency(self) -> None:
        """解答の一貫性テスト"""
        # 同じ入力に対して常に同じ結果を返すことを確認
        limit = 100

        result1 = solve_naive(limit)
        result2 = solve_naive(limit)
        result3 = solve_naive(limit)

        assert result1 == result2 == result3

    def test_word_formation_correctness(self) -> None:
        """単語形成の正確性テスト"""
        # 各範囲の代表的な数値で単語形成をテスト
        test_cases = [
            # 一桁
            (7, "seven"),
            # 10代
            (13, "thirteen"),
            # 10の倍数
            (40, "forty"),
            # 合成10の位
            (27, "twenty seven"),
            # 100の倍数
            (300, "three hundred"),
            # 100の位 + 一桁
            (105, "one hundred and five"),
            # 100の位 + 10代
            (116, "one hundred and sixteen"),
            # 100の位 + 10の倍数
            (150, "one hundred and fifty"),
            # 100の位 + 合成10の位
            (189, "one hundred and eighty nine"),
            # 1000
            (1000, "one thousand"),
        ]

        for num, expected in test_cases:
            actual = number_to_words(num)
            assert actual == expected, (
                f"Expected '{expected}', got '{actual}' for {num}"
            )

    def test_known_answer(self) -> None:
        """既知の解答のテスト"""
        # Problem 017の解答は21124
        result = solve_naive(1000)
        assert result == 21124, f"Expected 21124, got {result}"

        # 他の解法でも同じ結果が得られることを確認
        assert solve_optimized(1000) == 21124
