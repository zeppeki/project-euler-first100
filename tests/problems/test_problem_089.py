"""Tests for Problem 089: Roman numerals."""

import importlib.util
import sys
import tempfile
from pathlib import Path

import pytest

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import the module
spec = importlib.util.spec_from_file_location(
    "problem_089", Path(__file__).parent.parent.parent / "problems" / "problem_089.py"
)
if spec and spec.loader:
    problem_089 = importlib.util.module_from_spec(spec)
    sys.modules["problem_089"] = problem_089
    spec.loader.exec_module(problem_089)
else:
    raise ImportError("Could not load problem_089 module")


class TestRomanNumeralConversion:
    """ローマ数字変換のテスト."""

    def test_roman_to_decimal_basic(self) -> None:
        """基本的なローマ数字から10進数への変換."""
        test_cases = [
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("L", 50),
            ("C", 100),
            ("D", 500),
            ("M", 1000),
        ]

        for roman, expected in test_cases:
            assert problem_089.roman_to_decimal(roman) == expected

    def test_roman_to_decimal_subtractive(self) -> None:
        """減算記法のローマ数字から10進数への変換."""
        test_cases = [
            ("IV", 4),
            ("IX", 9),
            ("XL", 40),
            ("XC", 90),
            ("CD", 400),
            ("CM", 900),
        ]

        for roman, expected in test_cases:
            assert problem_089.roman_to_decimal(roman) == expected

    def test_roman_to_decimal_complex(self) -> None:
        """複雑なローマ数字から10進数への変換."""
        test_cases = [
            ("XIV", 14),
            ("XXIV", 24),
            ("XLIV", 44),
            ("XLIX", 49),
            ("XCIV", 94),
            ("XCIX", 99),
            ("CDXLIV", 444),
            ("MCMXC", 1990),
            ("MMXXI", 2021),
            ("MMMCMXCIX", 3999),
        ]

        for roman, expected in test_cases:
            assert problem_089.roman_to_decimal(roman) == expected

    def test_roman_to_decimal_non_optimal(self) -> None:
        """非最適なローマ数字から10進数への変換."""
        test_cases = [
            ("IIII", 4),  # 通常はIV
            ("VIIII", 9),  # 通常はIX
            ("XIIII", 14),  # 通常はXIV
            ("XXXX", 40),  # 通常はXL
            ("LXXXX", 90),  # 通常はXC
            ("CCCC", 400),  # 通常はCD
            ("DCCCC", 900),  # 通常はCM
        ]

        for roman, expected in test_cases:
            assert problem_089.roman_to_decimal(roman) == expected

    def test_decimal_to_roman_basic(self) -> None:
        """基本的な10進数からローマ数字への変換."""
        test_cases = [
            (1, "I"),
            (5, "V"),
            (10, "X"),
            (50, "L"),
            (100, "C"),
            (500, "D"),
            (1000, "M"),
        ]

        for decimal, expected in test_cases:
            assert problem_089.decimal_to_roman(decimal) == expected

    def test_decimal_to_roman_subtractive(self) -> None:
        """減算記法を使う10進数からローマ数字への変換."""
        test_cases = [
            (4, "IV"),
            (9, "IX"),
            (40, "XL"),
            (90, "XC"),
            (400, "CD"),
            (900, "CM"),
        ]

        for decimal, expected in test_cases:
            assert problem_089.decimal_to_roman(decimal) == expected

    def test_decimal_to_roman_complex(self) -> None:
        """複雑な10進数からローマ数字への変換."""
        test_cases = [
            (14, "XIV"),
            (24, "XXIV"),
            (44, "XLIV"),
            (49, "XLIX"),
            (94, "XCIV"),
            (99, "XCIX"),
            (444, "CDXLIV"),
            (1990, "MCMXC"),
            (2021, "MMXXI"),
            (3999, "MMMCMXCIX"),
        ]

        for decimal, expected in test_cases:
            assert problem_089.decimal_to_roman(decimal) == expected

    def test_decimal_to_roman_edge_cases(self) -> None:
        """境界値のテスト."""
        # 有効な範囲
        assert problem_089.decimal_to_roman(1) == "I"
        assert problem_089.decimal_to_roman(3999) == "MMMCMXCIX"

        # 無効な値
        with pytest.raises(ValueError):
            problem_089.decimal_to_roman(0)

        with pytest.raises(ValueError):
            problem_089.decimal_to_roman(4000)

        with pytest.raises(ValueError):
            problem_089.decimal_to_roman(-1)

    def test_roundtrip_conversion(self) -> None:
        """ローマ数字 ↔ 10進数の相互変換テスト."""
        test_numbers = [
            1,
            4,
            5,
            9,
            10,
            14,
            40,
            49,
            50,
            90,
            99,
            100,
            400,
            444,
            500,
            900,
            999,
            1000,
            1990,
            2021,
            3999,
        ]

        for num in test_numbers:
            roman = problem_089.decimal_to_roman(num)
            converted_back = problem_089.roman_to_decimal(roman)
            assert converted_back == num, (
                f"Failed for {num}: {roman} → {converted_back}"
            )


class TestSolutionFunctions:
    """解法関数のテスト."""

    def create_test_file(self, content: list[str]) -> str:
        """テスト用のファイルを作成."""
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
            f.write("\n".join(content))
            return f.name

    def test_problem_examples(self) -> None:
        """問題文の例を検証."""
        # 非最適なローマ数字の例
        test_data = [
            "IIIIIIIII",  # 9 → IX (7文字節約)
            "VIIII",  # 9 → IX (3文字節約)
            "XIIII",  # 14 → XIV (2文字節約)
            "LXXXX",  # 90 → XC (3文字節約)
            "CCCC",  # 400 → CD (2文字節約)
        ]

        expected_savings = 7 + 3 + 2 + 3 + 2  # 17文字

        temp_file = self.create_test_file(test_data)
        try:
            assert problem_089.solve_naive(temp_file) == expected_savings
            assert problem_089.solve_optimized(temp_file) == expected_savings
            assert problem_089.solve_mathematical(temp_file) == expected_savings
        finally:
            import os

            os.unlink(temp_file)

    def test_small_dataset(self) -> None:
        """小さなデータセットでの結果を検証."""
        test_data = [
            "IV",  # 既に最適 (0文字節約)
            "IX",  # 既に最適 (0文字節約)
            "IIII",  # 4 → IV (2文字節約)
            "VIIII",  # 9 → IX (3文字節約)
        ]

        expected_savings = 0 + 0 + 2 + 3  # 5文字

        temp_file = self.create_test_file(test_data)
        try:
            assert problem_089.solve_naive(temp_file) == expected_savings
            assert problem_089.solve_optimized(temp_file) == expected_savings
            assert problem_089.solve_mathematical(temp_file) == expected_savings
        finally:
            import os

            os.unlink(temp_file)

    def test_empty_file(self) -> None:
        """空ファイルのテスト."""
        temp_file = self.create_test_file([])
        try:
            assert problem_089.solve_naive(temp_file) == 0
            assert problem_089.solve_optimized(temp_file) == 0
            assert problem_089.solve_mathematical(temp_file) == 0
        finally:
            import os

            os.unlink(temp_file)

    def test_consistency(self) -> None:
        """異なる解法の一致性を検証."""
        test_datasets = [
            ["IV", "IX", "XL", "XC", "CD", "CM"],  # 既に最適
            ["IIII", "VIIII", "XXXX", "LXXXX", "CCCC", "DCCCC"],  # 全て非最適
            ["XIV", "XIIII", "XL", "LXXXX"],  # 混在
        ]

        for test_data in test_datasets:
            temp_file = self.create_test_file(test_data)
            try:
                result_naive = problem_089.solve_naive(temp_file)
                result_optimized = problem_089.solve_optimized(temp_file)
                result_mathematical = problem_089.solve_mathematical(temp_file)

                assert result_naive == result_optimized == result_mathematical, (
                    f"Inconsistent results for {test_data}: "
                    f"naive={result_naive}, optimized={result_optimized}, mathematical={result_mathematical}"
                )
            finally:
                import os

                os.unlink(temp_file)

    def test_file_not_found(self) -> None:
        """存在しないファイルのテスト（フォールバック動作）."""
        # 存在しないファイルを指定した場合、内蔵のテストデータを使用
        result_naive = problem_089.solve_naive("nonexistent_file.txt")
        result_optimized = problem_089.solve_optimized("nonexistent_file.txt")
        result_mathematical = problem_089.solve_mathematical("nonexistent_file.txt")

        # フォールバックデータでの期待値
        expected = 7 + 3 + 2 + 3 + 2 + 2  # 19文字

        assert result_naive == expected
        assert result_optimized == expected
        assert result_mathematical == expected


class TestOptimizationPatterns:
    """最適化パターンのテスト."""

    def test_four_consecutive_same_characters(self) -> None:
        """4つの連続する同じ文字のパターン."""
        test_cases = [
            ("IIII", "IV", 2),  # 4文字 → 2文字 (2文字節約)
            ("XXXX", "XL", 2),  # 4文字 → 2文字 (2文字節約)
            ("CCCC", "CD", 2),  # 4文字 → 2文字 (2文字節約)
        ]

        for original, optimal, expected_savings in test_cases:
            decimal = problem_089.roman_to_decimal(original)
            computed_optimal = problem_089.decimal_to_roman(decimal)

            assert computed_optimal == optimal
            assert len(original) - len(optimal) == expected_savings

    def test_five_character_patterns(self) -> None:
        """5文字のパターン（V+4つの次の文字）."""
        test_cases = [
            ("VIIII", "IX", 3),  # 5文字 → 2文字 (3文字節約)
            ("LXXXX", "XC", 3),  # 5文字 → 2文字 (3文字節約)
            ("DCCCC", "CM", 3),  # 5文字 → 2文字 (3文字節約)
        ]

        for original, optimal, expected_savings in test_cases:
            decimal = problem_089.roman_to_decimal(original)
            computed_optimal = problem_089.decimal_to_roman(decimal)

            assert computed_optimal == optimal
            assert len(original) - len(optimal) == expected_savings

    def test_already_optimal(self) -> None:
        """既に最適なローマ数字のテスト."""
        optimal_numerals = [
            "I",
            "II",
            "III",
            "IV",
            "V",
            "VI",
            "VII",
            "VIII",
            "IX",
            "X",
            "XIV",
            "XV",
            "XIX",
            "XX",
            "XXIV",
            "XXV",
            "XXIX",
            "XXX",
            "XL",
            "XLV",
            "XLIX",
            "L",
            "XC",
            "XCV",
            "XCIX",
            "C",
            "CD",
            "D",
            "CM",
            "M",
            "MCMXC",
            "MM",
            "MMMCMXCIX",
        ]

        for roman in optimal_numerals:
            decimal = problem_089.roman_to_decimal(roman)
            computed_optimal = problem_089.decimal_to_roman(decimal)

            # 既に最適な場合、変換しても同じになるはず
            assert computed_optimal == roman


class TestEdgeCases:
    """エッジケースのテスト."""

    def test_large_numbers(self) -> None:
        """大きな数値のテスト."""
        large_test_cases = [
            (3000, "MMM"),
            (3900, "MMMCM"),
            (3999, "MMMCMXCIX"),  # 最大値
        ]

        for decimal, expected in large_test_cases:
            assert problem_089.decimal_to_roman(decimal) == expected
            assert problem_089.roman_to_decimal(expected) == decimal

    def test_mixed_patterns(self) -> None:
        """複数の最適化パターンが混在するテスト."""
        mixed_cases = [
            "MCCCCXXXXVIIII",  # M + CCCC + XXXX + VIIII → M + CD + XL + IX
        ]

        for original in mixed_cases:
            decimal = problem_089.roman_to_decimal(original)
            optimal = problem_089.decimal_to_roman(decimal)

            # 最適化により文字数が減ることを確認
            assert len(optimal) < len(original)

            # 変換後も同じ数値を表すことを確認
            assert problem_089.roman_to_decimal(optimal) == decimal

    def test_whitespace_and_empty_lines(self) -> None:
        """空白行や空文字列の処理."""
        test_data = [
            "",  # 空行
            "IV",  # 通常の行
            "",  # 空行
            "IIII",  # 非最適な行
            "",  # 空行
        ]

        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
            f.write("\n".join(test_data))
            temp_file = f.name

        try:
            # 空行は無視され、有効な行のみ処理される
            expected_savings = 0 + 2  # IV(0文字節約) + IIII→IV(2文字節約)

            result = problem_089.solve_naive(temp_file)
            assert result == expected_savings
        finally:
            import os

            os.unlink(temp_file)


class TestPerformance:
    """パフォーマンステスト."""

    def test_performance_difference(self) -> None:
        """最適化の効果を確認."""
        import time

        # 大きなテストデータセット
        test_data = ["IIII", "VIIII", "XXXX", "LXXXX", "CCCC", "DCCCC"] * 100

        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
            f.write("\n".join(test_data))
            temp_file = f.name

        try:
            # 素直な解法
            start = time.time()
            result_naive = problem_089.solve_naive(temp_file)
            time_naive = time.time() - start

            # 最適化解法
            start = time.time()
            result_optimized = problem_089.solve_optimized(temp_file)
            time_optimized = time.time() - start

            # 結果は一致すべき
            assert result_naive == result_optimized

            # パフォーマンス情報を出力
            print("\nPerformance comparison:")
            print(f"  Naive: {time_naive:.6f}s")
            print(f"  Optimized: {time_optimized:.6f}s")

        finally:
            import os

            os.unlink(temp_file)

    @pytest.mark.slow
    def test_large_dataset(self) -> None:
        """大きなデータセットでの動作を検証."""
        # 1000行のテストデータを生成
        large_data = []
        for i in range(1000):
            if i % 6 == 0:
                large_data.append("IIII")
            elif i % 6 == 1:
                large_data.append("VIIII")
            elif i % 6 == 2:
                large_data.append("XXXX")
            elif i % 6 == 3:
                large_data.append("LXXXX")
            elif i % 6 == 4:
                large_data.append("CCCC")
            else:
                large_data.append("DCCCC")

        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
            f.write("\n".join(large_data))
            temp_file = f.name

        try:
            result_naive = problem_089.solve_naive(temp_file)
            result_optimized = problem_089.solve_optimized(temp_file)
            result_mathematical = problem_089.solve_mathematical(temp_file)

            assert result_naive == result_optimized == result_mathematical
            assert result_naive > 0  # 何らかの節約があることを確認

        finally:
            import os

            os.unlink(temp_file)
