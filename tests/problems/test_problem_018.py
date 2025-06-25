#!/usr/bin/env python3
"""
Tests for Problem 018: Maximum Path Sum I
"""

import importlib.util
import sys
from pathlib import Path
from typing import Any

import pytest


def load_problem_module():  # type: ignore
    """動的にproblem_018モジュールをロード"""
    problem_path = Path(__file__).parent.parent.parent / "problems" / "problem_018.py"
    spec = importlib.util.spec_from_file_location("problem_018", problem_path)
    if spec is None:
        raise ImportError("Could not load problem module")
    module = importlib.util.module_from_spec(spec)
    sys.modules["problem_018"] = module
    if spec.loader is None:
        raise ImportError("Could not load problem module")
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def problem():  # type: ignore
    """problem_018モジュールのフィクスチャ"""
    return load_problem_module()


class TestTriangleParsing:
    """三角形データの解析テスト"""

    def test_parse_triangle_single_element(self, problem: Any) -> None:
        """単一要素の三角形"""
        triangle_str = "5"
        expected = [[5]]
        result = problem.parse_triangle(triangle_str)
        assert result == expected

    def test_parse_triangle_two_rows(self, problem: Any) -> None:
        """2行の三角形"""
        triangle_str = "1\n2 3"
        expected = [[1], [2, 3]]
        result = problem.parse_triangle(triangle_str)
        assert result == expected

    def test_parse_triangle_example(self, problem: Any) -> None:
        """例題の三角形"""
        triangle_str = "3\n7 4\n2 4 6\n8 5 9 3"
        expected = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        result = problem.parse_triangle(triangle_str)
        assert result == expected

    def test_parse_triangle_with_leading_zeros(self, problem: Any) -> None:
        """先頭ゼロありの数値を含む三角形"""
        triangle_str = "01\n02 03\n04 05 06"
        expected = [[1], [2, 3], [4, 5, 6]]
        result = problem.parse_triangle(triangle_str)
        assert result == expected


class TestHelperFunctions:
    """ヘルパー関数のテスト"""

    def test_get_example_triangle(self, problem: Any) -> None:
        """例題三角形の取得"""
        result = problem.get_example_triangle()
        expected = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        assert result == expected

    def test_get_problem_triangle(self, problem: Any) -> None:
        """本問題三角形の取得"""
        result = problem.get_problem_triangle()
        assert len(result) == 15  # 15行
        assert len(result[0]) == 1  # 最上行は1要素
        assert len(result[-1]) == 15  # 最下行は15要素
        assert result[0][0] == 75  # 最上位の値


class TestSolutionCorrectness:
    """解法の正解性テスト"""

    @pytest.mark.parametrize(
        "triangle,expected",
        [
            ([[5]], 5),
            ([[1], [2, 3]], 4),  # 1 + 3 = 4
            ([[1], [2, 3], [4, 5, 6]], 10),  # 1 + 3 + 6 = 10
        ],
    )
    def test_small_triangles(self, problem: Any, triangle: Any, expected: Any) -> None:
        """小さな三角形での全解法テスト"""
        assert problem.solve_naive(triangle) == expected
        assert problem.solve_optimized(triangle) == expected
        assert problem.solve_mathematical(triangle) == expected

    def test_example_triangle(self, problem: Any) -> None:
        """例題での全解法テスト"""
        triangle = problem.get_example_triangle()
        expected = 23

        assert problem.solve_naive(triangle) == expected
        assert problem.solve_optimized(triangle) == expected
        assert problem.solve_mathematical(triangle) == expected


class TestSolutionConsistency:
    """解法間の一貫性テスト"""

    def test_all_solutions_agree_small(self, problem: Any) -> None:
        """小さな三角形で全解法が一致することを確認"""
        test_triangles = [
            [[1]],
            [[1], [2, 3]],
            [[5], [1, 2], [3, 4, 5]],
        ]

        for triangle in test_triangles:
            naive_result = problem.solve_naive(triangle)
            optimized_result = problem.solve_optimized(triangle)
            math_result = problem.solve_mathematical(triangle)

            assert naive_result == optimized_result == math_result

    def test_all_solutions_agree_example(self, problem: Any) -> None:
        """例題で全解法が一致することを確認"""
        triangle = problem.get_example_triangle()

        naive_result = problem.solve_naive(triangle)
        optimized_result = problem.solve_optimized(triangle)
        math_result = problem.solve_mathematical(triangle)

        assert naive_result == optimized_result == math_result

    def test_all_solutions_agree_problem(self, problem: Any) -> None:
        """本問題で全解法が一致することを確認"""
        triangle = problem.get_problem_triangle()

        naive_result = problem.solve_naive(triangle)
        optimized_result = problem.solve_optimized(triangle)
        math_result = problem.solve_mathematical(triangle)

        assert naive_result == optimized_result == math_result


class TestEdgeCases:
    """エッジケースのテスト"""

    def test_single_element_triangle(self, problem: Any) -> None:
        """単一要素の三角形"""
        triangle = [[42]]
        expected = 42

        assert problem.solve_naive(triangle) == expected
        assert problem.solve_optimized(triangle) == expected
        assert problem.solve_mathematical(triangle) == expected

    def test_two_row_triangle(self, problem: Any) -> None:
        """2行の三角形での最適パス選択"""
        triangle = [[5], [1, 9]]  # 5 + 9 = 14が最大
        expected = 14

        assert problem.solve_naive(triangle) == expected
        assert problem.solve_optimized(triangle) == expected
        assert problem.solve_mathematical(triangle) == expected

    def test_negative_numbers(self, problem: Any) -> None:
        """負の数を含む三角形"""
        triangle = [[1], [-2, 3], [4, -5, 6]]  # 1 + 3 + 6 = 10が最大
        expected = 10

        assert problem.solve_naive(triangle) == expected
        assert problem.solve_optimized(triangle) == expected
        assert problem.solve_mathematical(triangle) == expected


class TestPerformance:
    """パフォーマンステスト"""

    @pytest.mark.slow
    def test_large_triangle_performance(self, problem: Any) -> None:
        """大きな三角形でのパフォーマンステスト（スロー）"""
        import time

        triangle = problem.get_problem_triangle()

        # 最適化解法と数学的解法は十分高速であることを確認
        start = time.time()
        result_optimized = problem.solve_optimized(triangle)
        optimized_time = time.time() - start

        start = time.time()
        result_math = problem.solve_mathematical(triangle)
        math_time = time.time() - start

        # 結果が一致することを確認
        assert result_optimized == result_math

        # 実行時間が妥当であることを確認（1秒以内）
        assert optimized_time < 1.0
        assert math_time < 1.0


class TestMainFunction:
    """メイン関数のテスト"""

    def test_main_function_exists(self, problem: Any) -> None:
        """main関数が存在することを確認"""
        assert hasattr(problem, "main")
        assert callable(problem.main)

    def test_test_solutions_function_exists(self, problem: Any) -> None:
        """test_solutions関数が存在することを確認"""
        assert hasattr(problem, "test_solutions")
        assert callable(problem.test_solutions)


if __name__ == "__main__":
    pytest.main([__file__])
