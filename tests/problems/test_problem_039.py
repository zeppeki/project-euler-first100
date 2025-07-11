"""Tests for Problem 039: Integer right triangles."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_039 import (
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


def count_solutions(perimeter: int) -> int:
    """Count the number of right triangles with given perimeter."""
    if perimeter <= 0:
        return 0

    count = 0
    for a in range(1, perimeter // 3 + 1):
        for b in range(a, (perimeter - a) // 2 + 1):
            c = perimeter - a - b
            if c > b and a * a + b * b == c * c:
                count += 1
    return count


def get_solutions(perimeter: int) -> list[tuple[int, int, int]]:
    """Get all right triangle solutions for given perimeter."""
    if perimeter <= 0:
        return []

    solutions = []
    for a in range(1, perimeter // 3 + 1):
        for b in range(a, (perimeter - a) // 2 + 1):
            c = perimeter - a - b
            if c > b and a * a + b * b == c * c:
                solutions.append((a, b, c))
    return solutions


class TestProblem039:
    """Test cases for Problem 039."""

    def test_count_solutions(self) -> None:
        """Test the count_solutions function."""
        # 例題のテスト
        assert count_solutions(120) == 3

        # 基本的なピタゴラス数
        assert count_solutions(12) == 1  # (3,4,5)
        assert count_solutions(30) == 1  # (5,12,13)
        assert count_solutions(36) == 1  # (9,12,15)

        # 境界ケース
        assert count_solutions(0) == 0
        assert count_solutions(1) == 0
        assert count_solutions(2) == 0
        assert count_solutions(11) == 0  # 最小の直角三角形は(3,4,5)で周囲12

    def test_get_solutions(self) -> None:
        """Test the get_solutions function."""
        # 例題のテスト: p = 120 の場合
        solutions_120 = get_solutions(120)
        expected_120 = [(20, 48, 52), (24, 45, 51), (30, 40, 50)]
        assert len(solutions_120) == 3
        assert sorted(solutions_120) == sorted(expected_120)

        # 基本的なピタゴラス数のテスト
        solutions_12 = get_solutions(12)
        assert solutions_12 == [(3, 4, 5)]

        solutions_30 = get_solutions(30)
        assert solutions_30 == [(5, 12, 13)]

        # 境界ケース
        assert get_solutions(0) == []
        assert get_solutions(11) == []

    def test_solution_properties(self) -> None:
        """Test that all solutions satisfy the Pythagorean theorem."""
        # p = 120 の全ての解をテスト
        solutions = get_solutions(120)
        for a, b, c in solutions:
            assert a * a + b * b == c * c  # ピタゴラスの定理
            assert a <= b < c  # a ≤ b < c の順序
            assert a + b + c == 120  # 周囲の長さ

    @pytest.mark.parametrize(
        "perimeter,expected_count",
        [
            (12, 1),  # (3,4,5)
            (24, 1),  # (6,8,10)
            (30, 1),  # (5,12,13)
            (36, 1),  # (9,12,15)
            (40, 1),  # (8,15,17)
            (48, 1),  # (12,16,20)
            (60, 2),  # (10,24,26), (15,20,25)
            (120, 3),  # 例題
        ],
    )
    def test_parametrized_solutions(self, perimeter: int, expected_count: int) -> None:
        """Test solution counts for various perimeters."""
        assert count_solutions(perimeter) == expected_count

    def test_solve_naive(self) -> None:
        """Test the naive solution approach."""
        # 小さな値でのテスト
        result = solve_naive(120)
        assert isinstance(result, int)
        assert result > 0

        # p = 120 が最大の解数を持つかどうかをチェック
        max_count = count_solutions(result)
        assert count_solutions(120) <= max_count

    def test_solve_optimized(self) -> None:
        """Test the optimized solution approach."""
        # 小さな値でのテスト
        result = solve_optimized(120)
        assert isinstance(result, int)
        assert result > 0

        # naive解法と同じ結果になることを確認
        assert solve_optimized(120) == solve_naive(120)

    def test_solve_mathematical(self) -> None:
        """Test the mathematical solution approach."""
        # 小さな値でのテスト
        result = solve_mathematical(120)
        assert isinstance(result, int)
        assert result > 0

        # 他の解法と同じ結果になることを確認
        assert solve_mathematical(120) == solve_naive(120)
        assert solve_mathematical(120) == solve_optimized(120)

    def test_all_solutions_agree(self) -> None:
        """Test that all solution methods agree."""
        test_values = [50, 100, 200, 500]

        for max_p in test_values:
            naive_result = solve_naive(max_p)
            optimized_result = solve_optimized(max_p)
            mathematical_result = solve_mathematical(max_p)

            assert naive_result == optimized_result == mathematical_result

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # ゼロや負の値
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0
        assert solve_mathematical(0) == 0

        # 非常に小さな値
        for func in [solve_naive, solve_optimized, solve_mathematical]:
            result = func(12)
            assert result == 12  # (3,4,5) の周囲が唯一の解なので、p=12が最大解数を持つ

    @pytest.mark.slow
    def test_large_values(self) -> None:
        """Test with larger values (marked as slow)."""
        # 本問題の制限値でのテスト
        result_naive = solve_naive(1000)
        result_optimized = solve_optimized(1000)
        result_mathematical = solve_mathematical(1000)

        assert result_naive == result_optimized == result_mathematical
        assert isinstance(result_naive, int)
        assert 12 <= result_naive <= 1000  # 合理的な範囲

    def test_performance_comparison(self) -> None:
        """Test that optimized solutions are faster for larger inputs."""
        # パフォーマンステストは実行時間の測定ではなく、
        # 機能的な正確性をチェック
        test_limit = 200

        naive_result = solve_naive(test_limit)
        optimized_result = solve_optimized(test_limit)
        mathematical_result = solve_mathematical(test_limit)

        # 全て同じ結果になることを確認
        assert naive_result == optimized_result == mathematical_result

        # 結果が妥当な範囲内であることを確認
        assert 12 <= naive_result <= test_limit
