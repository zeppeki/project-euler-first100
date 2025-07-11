#!/usr/bin/env python3
"""Tests for Problem 090: Cube digit pairs."""

import importlib.util
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import the module
spec = importlib.util.spec_from_file_location(
    "problem_090", Path(__file__).parent.parent.parent / "problems" / "problem_090.py"
)
if spec and spec.loader:
    problem_090 = importlib.util.module_from_spec(spec)
    sys.modules["problem_090"] = problem_090
    spec.loader.exec_module(problem_090)
else:
    raise ImportError("Could not load problem_090 module")


class TestCubeDigitPairs:
    """キューブの数字ペアのテスト."""

    def test_can_form_square_basic(self) -> None:
        """基本的な平方数の生成テスト."""
        cube1 = {0, 1, 2, 3, 4, 5}
        cube2 = {6, 7, 8, 9, 0, 1}

        # 01 が作れるかテスト
        assert problem_090.can_form_square(cube1, cube2, "01")

        # 10 が作れるかテスト（逆順）
        assert problem_090.can_form_square(cube1, cube2, "10")

    def test_can_form_square_with_6_9_conversion(self) -> None:
        """6と9の変換を含む平方数の生成テスト."""
        cube1 = {0, 1, 2, 3, 4, 6}  # 6を含む
        cube2 = {5, 7, 8, 9, 0, 1}  # 9を含む

        # 09 が作れるかテスト（0と6→9の変換）
        assert problem_090.can_form_square(cube1, cube2, "09")

        # 16 が作れるかテスト（1と6→9の変換）
        assert problem_090.can_form_square(cube1, cube2, "16")

        # 96 が作れるかテスト（9→6の変換）
        assert problem_090.can_form_square(cube1, cube2, "96")

    def test_normalize_cube(self) -> None:
        """キューブの正規化テスト."""
        # 6と9両方を含む場合
        cube1 = {0, 1, 2, 6, 9, 5}
        normalized1 = problem_090.normalize_cube(cube1)
        assert 9 not in normalized1
        assert 6 in normalized1

        # 9のみを含む場合
        cube2 = {0, 1, 2, 3, 9, 5}
        normalized2 = problem_090.normalize_cube(cube2)
        assert 9 not in normalized2
        assert 6 in normalized2

        # 6のみを含む場合
        cube3 = {0, 1, 2, 3, 6, 5}
        normalized3 = problem_090.normalize_cube(cube3)
        assert normalized3 == cube3

    def test_example_cubes(self) -> None:
        """問題文の例のキューブをテスト."""
        cube1 = {0, 5, 6, 7, 8, 9}
        cube2 = {1, 2, 3, 4, 8, 9}

        # 必要な全ての平方数が作れることを確認
        required_squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]

        for square in required_squares:
            assert problem_090.can_form_square(cube1, cube2, square), (
                f"Cannot form {square} with example cubes"
            )

    def test_specific_squares(self) -> None:
        """特定の平方数の詳細テスト."""
        # 01 をテスト
        cube1 = {0, 2, 3, 4, 5, 6}
        cube2 = {1, 7, 8, 9, 0, 2}
        assert problem_090.can_form_square(cube1, cube2, "01")

        # 25 をテスト
        cube3 = {2, 3, 4, 6, 7, 8}
        cube4 = {5, 1, 9, 0, 2, 3}
        assert problem_090.can_form_square(cube3, cube4, "25")

        # 64 をテスト（6と4）
        cube5 = {6, 1, 2, 3, 7, 8}
        cube6 = {4, 5, 9, 0, 1, 2}
        assert problem_090.can_form_square(cube5, cube6, "64")

    def test_impossible_squares(self) -> None:
        """作成不可能な平方数のテスト."""
        # 0と1を含まないキューブで01を作ろうとする
        cube1 = {2, 3, 4, 5, 6, 7}
        cube2 = {8, 9, 2, 3, 4, 5}
        assert not problem_090.can_form_square(cube1, cube2, "01")

        # 必要な数字が不足しているケース
        cube3 = {0, 1, 2, 3, 4, 5}
        cube4 = {0, 1, 2, 3, 4, 5}  # 8がない
        assert not problem_090.can_form_square(cube3, cube4, "81")


class TestSolutionFunctions:
    """解法関数のテスト."""

    def test_solution_consistency(self) -> None:
        """全ての解法が同じ結果を返すことを確認."""
        result_naive = problem_090.solve_naive()
        result_optimized = problem_090.solve_optimized()
        result_mathematical = problem_090.solve_mathematical()

        assert result_naive == result_optimized, (
            f"Naive and optimized solutions differ: {result_naive} vs {result_optimized}"
        )
        assert result_optimized == result_mathematical, (
            f"Optimized and mathematical solutions differ: {result_optimized} vs {result_mathematical}"
        )

    def test_solution_bounds(self) -> None:
        """解の妥当性をチェック."""
        result = problem_090.solve_naive()

        # 結果は正の整数であるべき
        assert isinstance(result, int)
        assert result > 0

        # 理論的上限をチェック（C(10,6) * C(10,6) = 210 * 210 = 44,100）
        max_possible = 210 * 210
        assert result <= max_possible

        # 現実的な下限をチェック（少なくとも1つは存在するはず）
        assert result >= 1

    def test_solution_performance(self) -> None:
        """パフォーマンステスト（軽量）."""
        import time

        # naive解法のテスト
        start = time.time()
        result_naive = problem_090.solve_naive()
        time_naive = time.time() - start

        # optimized解法のテスト
        start = time.time()
        result_optimized = problem_090.solve_optimized()
        time_optimized = time.time() - start

        # 結果が一致することを確認
        assert result_naive == result_optimized

        # 実行時間の情報を出力（アサートはしない）
        print("\nPerformance test:")
        print(f"  Naive: {time_naive:.4f}s")
        print(f"  Optimized: {time_optimized:.4f}s")


class TestEdgeCases:
    """エッジケースのテスト."""

    def test_minimum_squares(self) -> None:
        """最小限の平方数セットのテスト."""
        # 各平方数に必要な数字を確認
        required_digits = set()
        squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]

        for square in squares:
            for digit_char in square:
                digit = int(digit_char)
                required_digits.add(digit)
                # 6と9の相互変換を考慮
                if digit == 6:
                    required_digits.add(9)
                elif digit == 9:
                    required_digits.add(6)

        # 必要な数字が10個以下であることを確認
        assert len(required_digits) <= 10

    def test_cube_constraints(self) -> None:
        """キューブの制約テスト."""
        from itertools import combinations

        # 10個から6個を選ぶ組み合わせ数が正しいことを確認
        all_combinations = list(combinations(range(10), 6))
        assert len(all_combinations) == 210  # C(10,6) = 210

    def test_6_9_equivalence(self) -> None:
        """6と9の等価性テスト."""
        # 6を含むキューブと9を含むキューブが同等に扱われることを確認
        cube_with_6 = {0, 1, 2, 3, 4, 6}
        cube_with_9 = {0, 1, 2, 3, 4, 9}

        other_cube = {5, 7, 8, 9, 1, 2}  # 9を含む方のキューブ

        # どちらでも09が作れることを確認
        assert problem_090.can_form_square(cube_with_6, other_cube, "09")
        assert problem_090.can_form_square(cube_with_9, other_cube, "09")

        # 69が作れることを確認（6と9の相互変換）
        assert problem_090.can_form_square(cube_with_6, other_cube, "69")
        assert problem_090.can_form_square(cube_with_9, other_cube, "69")


class TestMathematicalProperties:
    """数学的性質のテスト."""

    def test_symmetry(self) -> None:
        """対称性のテスト."""
        # cube1とcube2を入れ替えても結果は同じであるべき
        cube1 = {0, 1, 2, 3, 4, 5}
        cube2 = {6, 7, 8, 9, 0, 1}

        for square in ["01", "16", "25", "64", "81"]:
            result1 = problem_090.can_form_square(cube1, cube2, square)
            result2 = problem_090.can_form_square(cube2, cube1, square)
            assert result1 == result2, f"Asymmetry found for {square}"

    def test_square_completeness(self) -> None:
        """平方数の完全性テスト."""
        # 1桁から2桁の完全平方数が正しく列挙されていることを確認
        expected_squares = []
        for i in range(1, 10):
            square = i * i
            if square < 100:
                expected_squares.append(f"{square:02d}")

        assert expected_squares == [
            "01",
            "04",
            "09",
            "16",
            "25",
            "36",
            "49",
            "64",
            "81",
        ]

    def test_digit_frequency(self) -> None:
        """数字の使用頻度分析."""
        squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]
        digit_count: dict[int, int] = {}

        for square in squares:
            for digit_char in square:
                digit = int(digit_char)
                digit_count[digit] = digit_count.get(digit, 0) + 1

        # 最も使用頻度の高い数字を確認
        most_common_digit = max(digit_count, key=lambda x: digit_count[x])
        print("\nDigit frequency analysis:")
        for digit in sorted(digit_count.keys()):
            print(f"  {digit}: {digit_count[digit]} times")
        print(f"  Most common: {most_common_digit}")
