#!/usr/bin/env python3
"""
Tests for Problem 020: Factorial digit sum
"""

import importlib.util
import sys
from pathlib import Path
from typing import Any

import pytest


def load_problem_module():  # type: ignore
    """動的にproblem_020モジュールをロード"""
    problem_path = Path(__file__).parent.parent.parent / "problems" / "problem_020.py"
    spec = importlib.util.spec_from_file_location("problem_020", problem_path)
    if spec is None:
        raise ImportError("Could not load problem module")
    module = importlib.util.module_from_spec(spec)
    sys.modules["problem_020"] = module
    if spec.loader is None:
        raise ImportError("Could not load problem module")
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def problem():  # type: ignore
    """problem_020モジュールのフィクスチャ"""
    return load_problem_module()


class TestSolveNaive:
    """solve_naiveのテスト"""

    def test_example(self, problem: Any) -> None:
        """例題のテスト"""
        assert problem.solve_naive(10) == 27

    def test_small_numbers(self, problem: Any) -> None:
        """小さい数のテスト"""
        assert problem.solve_naive(1) == 1
        assert problem.solve_naive(2) == 2
        assert problem.solve_naive(3) == 6
        assert problem.solve_naive(4) == 6
        assert problem.solve_naive(5) == 3

    def test_problem_case(self, problem: Any) -> None:
        """問題のケース"""
        assert problem.solve_naive(100) == 648


class TestSolveOptimized:
    """solve_optimizedのテスト"""

    def test_example(self, problem: Any) -> None:
        """例題のテスト"""
        assert problem.solve_optimized(10) == 27

    def test_small_numbers(self, problem: Any) -> None:
        """小さい数のテスト"""
        assert problem.solve_optimized(1) == 1
        assert problem.solve_optimized(2) == 2
        assert problem.solve_optimized(3) == 6
        assert problem.solve_optimized(4) == 6
        assert problem.solve_optimized(5) == 3

    def test_problem_case(self, problem: Any) -> None:
        """問題のケース"""
        assert problem.solve_optimized(100) == 648


class TestSolveMathematical:
    """solve_mathematicalのテスト"""

    def test_example(self, problem: Any) -> None:
        """例題のテスト"""
        assert problem.solve_mathematical(10) == 27

    def test_small_numbers(self, problem: Any) -> None:
        """小さい数のテスト"""
        assert problem.solve_mathematical(1) == 1
        assert problem.solve_mathematical(2) == 2
        assert problem.solve_mathematical(3) == 6
        assert problem.solve_mathematical(4) == 6
        assert problem.solve_mathematical(5) == 3

    def test_problem_case(self, problem: Any) -> None:
        """問題のケース"""
        assert problem.solve_mathematical(100) == 648


class TestSolutionConsistency:
    """解法間の一貫性テスト"""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 10, 20, 50])
    def test_all_methods_consistency(self, problem: Any, n: int) -> None:
        """全ての解法の結果が一致することを確認"""
        naive_result = problem.solve_naive(n)
        optimized_result = problem.solve_optimized(n)
        mathematical_result = problem.solve_mathematical(n)

        assert naive_result == optimized_result == mathematical_result

    def test_problem_case_consistency(self, problem: Any) -> None:
        """問題のケース（100!）で全解法が一致することを確認"""
        naive_result = problem.solve_naive(100)
        optimized_result = problem.solve_optimized(100)
        mathematical_result = problem.solve_mathematical(100)

        assert naive_result == optimized_result == mathematical_result == 648


class TestEdgeCases:
    """エッジケースのテスト"""

    def test_zero_and_one_factorial(self, problem: Any) -> None:
        """0!と1!のテスト"""
        # 0! = 1, 1! = 1なので桁和は1
        assert problem.solve_naive(0) == 1
        assert problem.solve_naive(1) == 1
        assert problem.solve_optimized(0) == 1
        assert problem.solve_optimized(1) == 1
        assert problem.solve_mathematical(0) == 1
        assert problem.solve_mathematical(1) == 1

    def test_known_factorials(self, problem: Any) -> None:
        """既知の階乗値でのテスト"""
        # 計算できる範囲での検証
        test_cases = [
            (4, 6),  # 4! = 24, 2+4 = 6
            (5, 3),  # 5! = 120, 1+2+0 = 3
            (6, 9),  # 6! = 720, 7+2+0 = 9
            (7, 9),  # 7! = 5040, 5+0+4+0 = 9
        ]

        for n, expected in test_cases:
            assert problem.solve_naive(n) == expected
            assert problem.solve_optimized(n) == expected
            assert problem.solve_mathematical(n) == expected


if __name__ == "__main__":
    pytest.main([__file__])
