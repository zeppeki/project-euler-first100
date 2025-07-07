"""
Tests for Problem 76: Counting summations
"""

from collections.abc import Callable

import pytest

from problems.problem_076 import solve_naive, solve_optimized


class TestProblem076:
    """Problem 76のテストクラス"""

    @pytest.mark.parametrize("func", [solve_naive, solve_optimized])
    def test_basic_cases(self, func: Callable[[int], int]) -> None:
        """基本的なテストケース"""
        # 問題文の例: 5の分割
        assert func(5) == 6

        # 小さな値のテスト
        assert func(2) == 1  # 2 = 1 + 1
        assert func(3) == 2  # 3 = 2 + 1, 1 + 1 + 1
        assert func(4) == 4  # 4 = 3 + 1, 2 + 2, 2 + 1 + 1, 1 + 1 + 1 + 1

    @pytest.mark.parametrize("func", [solve_naive, solve_optimized])
    def test_edge_cases(self, func: Callable[[int], int]) -> None:
        """エッジケースのテスト"""
        # 最小値
        assert func(1) == 0  # 1は2つ以上の正の整数の和で表せない

    @pytest.mark.parametrize("func", [solve_naive, solve_optimized])
    def test_larger_values(self, func: Callable[[int], int]) -> None:
        """大きめの値でのテスト"""
        # 計算可能な範囲での確認
        assert func(10) == 41
        assert func(15) == 175
        assert func(20) == 626

    def test_solution_consistency(self) -> None:
        """異なる解法の結果が一致することを確認"""
        test_values = [5, 10, 15, 20, 25, 30]

        for n in test_values:
            naive_result = solve_naive(n)
            optimized_result = solve_optimized(n)
            assert naive_result == optimized_result, f"Solutions disagree for n={n}"

    @pytest.mark.slow
    def test_project_euler(self) -> None:
        """Project Eulerの問題を解く"""
        n = 100

        # 両方の解法を実行
        naive_result = solve_naive(n)
        optimized_result = solve_optimized(n)

        # 結果が一致することを確認
        assert naive_result == optimized_result

        # 結果が正の整数であることを確認
        assert isinstance(naive_result, int)
        assert naive_result > 0

        # Project Eulerの回答確認用（実際の値は表示しない）
        print(f"\nProblem 76 - n={n}の分割数: {naive_result}")
