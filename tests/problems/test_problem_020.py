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
        assert problem.solve_mathematical(10) == 9  # 27 % 9 = 0, so 9

    def test_small_numbers(self, problem: Any) -> None:
        """小さい数のテスト"""
        assert problem.solve_mathematical(1) == 1
        assert problem.solve_mathematical(2) == 2
        assert problem.solve_mathematical(3) == 6
        assert problem.solve_mathematical(4) == 6
        assert problem.solve_mathematical(5) == 3

    def test_problem_case(self, problem: Any) -> None:
        """問題のケース"""
        assert problem.solve_mathematical(100) == 9  # 648 % 9 = 0, so 9


class TestSolutionConsistency:
    """解法間の一貫性テスト"""

    @pytest.mark.parametrize("n", [10, 20, 50])
    def test_consistency(self, problem: Any, n: int) -> None:
        """各解法の結果が一致することを確認"""
        naive_result = problem.solve_naive(n)
        optimized_result = problem.solve_optimized(n)
        assert naive_result == optimized_result


if __name__ == "__main__":
    pytest.main([__file__])
