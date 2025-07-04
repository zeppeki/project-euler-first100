#!/usr/bin/env python3
"""
Tests for Problem 020: Factorial digit sum
"""

import pytest

from problems.problem_020 import (
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestSolveNaive:
    """solve_naiveのテスト"""

    def test_example(self) -> None:
        """例題のテスト"""
        assert solve_naive(10) == 27

    def test_small_numbers(self) -> None:
        """小さい数のテスト"""
        assert solve_naive(1) == 1
        assert solve_naive(2) == 2
        assert solve_naive(3) == 6
        assert solve_naive(4) == 6
        assert solve_naive(5) == 3

    def test_problem_case(self) -> None:
        """問題のケース"""
        assert solve_naive(100) == 648


class TestSolveOptimized:
    """solve_optimizedのテスト"""

    def test_example(self) -> None:
        """例題のテスト"""
        assert solve_optimized(10) == 27

    def test_small_numbers(self) -> None:
        """小さい数のテスト"""
        assert solve_optimized(1) == 1
        assert solve_optimized(2) == 2
        assert solve_optimized(3) == 6
        assert solve_optimized(4) == 6
        assert solve_optimized(5) == 3

    def test_problem_case(self) -> None:
        """問題のケース"""
        assert solve_optimized(100) == 648


class TestSolveMathematical:
    """solve_mathematicalのテスト"""

    def test_example(self) -> None:
        """例題のテスト"""
        assert solve_mathematical(10) == 27

    def test_small_numbers(self) -> None:
        """小さい数のテスト"""
        assert solve_mathematical(1) == 1
        assert solve_mathematical(2) == 2
        assert solve_mathematical(3) == 6
        assert solve_mathematical(4) == 6
        assert solve_mathematical(5) == 3

    def test_problem_case(self) -> None:
        """問題のケース"""
        assert solve_mathematical(100) == 648


class TestSolutionConsistency:
    """解法間の一貫性テスト"""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 10, 20, 50])
    def test_all_methods_consistency(self, n: int) -> None:
        """全ての解法の結果が一致することを確認"""
        naive_result = solve_naive(n)
        optimized_result = solve_optimized(n)
        mathematical_result = solve_mathematical(n)

        assert naive_result == optimized_result == mathematical_result

    def test_problem_case_consistency(self) -> None:
        """問題のケース（100!）で全解法が一致することを確認"""
        naive_result = solve_naive(100)
        optimized_result = solve_optimized(100)
        mathematical_result = solve_mathematical(100)

        assert naive_result == optimized_result == mathematical_result == 648


class TestEdgeCases:
    """エッジケースのテスト"""

    def test_zero_and_one_factorial(self) -> None:
        """0!と1!のテスト"""
        # 0! = 1, 1! = 1なので桁和は1
        assert solve_naive(0) == 1
        assert solve_naive(1) == 1
        assert solve_optimized(0) == 1
        assert solve_optimized(1) == 1
        assert solve_mathematical(0) == 1
        assert solve_mathematical(1) == 1

    def test_known_factorials(self) -> None:
        """既知の階乗値のテスト"""
        # 4! = 24, 桁和 = 2+4 = 6
        assert solve_naive(4) == 6
        assert solve_optimized(4) == 6
        assert solve_mathematical(4) == 6

        # 5! = 120, 桁和 = 1+2+0 = 3
        assert solve_naive(5) == 3
        assert solve_optimized(5) == 3
        assert solve_mathematical(5) == 3
