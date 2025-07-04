#!/usr/bin/env python3
"""
Tests for Problem 019: Counting Sundays
"""

import importlib.util
import sys
from pathlib import Path
from typing import Any

import pytest


def load_problem_module():  # type: ignore
    """動的にproblem_019モジュールをロード"""
    problem_path = Path(__file__).parent.parent.parent / "problems" / "problem_019.py"
    spec = importlib.util.spec_from_file_location("problem_019", problem_path)
    if spec is None:
        raise ImportError("Could not load problem module")
    module = importlib.util.module_from_spec(spec)
    sys.modules["problem_019"] = module
    if spec.loader is None:
        raise ImportError("Could not load problem module")
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def problem():  # type: ignore
    """problem_019モジュールのフィクスチャ"""
    return load_problem_module()


class TestLeapYearCalculation:
    """うるう年判定のテスト"""

    @pytest.mark.parametrize(
        "year,expected",
        [
            (1900, False),  # 世紀年で400で割り切れない
            (2000, True),  # 世紀年で400で割り切れる
            (1996, True),  # 4で割り切れる
            (1997, False),  # 4で割り切れない
            (1800, False),  # 世紀年で400で割り切れない
            (2004, True),  # 4で割り切れる
            (1600, True),  # 世紀年で400で割り切れる
            (1700, False),  # 世紀年で400で割り切れない
            (2100, False),  # 世紀年で400で割り切れない
            (2400, True),  # 世紀年で400で割り切れる
        ],
    )
    def test_is_leap_year(self, problem: Any, year: int, expected: bool) -> None:
        """うるう年判定のテスト"""
        assert problem.is_leap_year(year) == expected

    def test_leap_year_century_rule(self, problem: Any) -> None:
        """世紀年の特別ルールのテスト"""
        # 400で割り切れる世紀年はうるう年
        assert problem.is_leap_year(1600) is True
        assert problem.is_leap_year(2000) is True
        assert problem.is_leap_year(2400) is True

        # 100で割り切れるが400で割り切れない世紀年は平年
        assert problem.is_leap_year(1700) is False
        assert problem.is_leap_year(1800) is False
        assert problem.is_leap_year(1900) is False


class TestDaysInMonth:
    """月の日数計算のテスト"""

    def test_thirty_days_months(self, problem: Any) -> None:
        """30日の月のテスト"""
        for month in [4, 6, 9, 11]:  # April, June, September, November
            assert problem.days_in_month(2000, month) == 30

    def test_thirty_one_days_months(self, problem: Any) -> None:
        """31日の月のテスト"""
        for month in [1, 3, 5, 7, 8, 10, 12]:  # Jan, Mar, May, Jul, Aug, Oct, Dec
            assert problem.days_in_month(2000, month) == 31

    def test_february_leap_year(self, problem: Any) -> None:
        """うるう年の2月のテスト"""
        assert problem.days_in_month(2000, 2) == 29  # うるう年
        assert problem.days_in_month(2004, 2) == 29  # うるう年

    def test_february_regular_year(self, problem: Any) -> None:
        """平年の2月のテスト"""
        assert problem.days_in_month(1997, 2) == 28  # 平年
        assert problem.days_in_month(1900, 2) == 28  # 世紀年（平年）
        assert problem.days_in_month(2001, 2) == 28  # 平年

    @pytest.mark.parametrize(
        "year,month,expected",
        [
            (2000, 1, 31),  # January
            (2000, 2, 29),  # February (leap year)
            (1900, 2, 28),  # February (not leap year)
            (2000, 3, 31),  # March
            (2000, 4, 30),  # April
            (2000, 5, 31),  # May
            (2000, 6, 30),  # June
            (2000, 7, 31),  # July
            (2000, 8, 31),  # August
            (2000, 9, 30),  # September
            (2000, 10, 31),  # October
            (2000, 11, 30),  # November
            (2000, 12, 31),  # December
        ],
    )
    def test_all_months_days(
        self, problem: Any, year: int, month: int, expected: int
    ) -> None:
        """全月の日数テスト"""
        assert problem.days_in_month(year, month) == expected


class TestSolutionCorrectness:
    """解法の正解性テスト"""

    def test_small_range_consistency(self, problem: Any) -> None:
        """小範囲での全解法一致テスト"""
        test_ranges = [
            (1901, 1901),  # 1年だけ
            (1901, 1905),  # 5年
            (1901, 1910),  # 10年
            (1950, 1959),  # 1950年代
        ]

        for start_year, end_year in test_ranges:
            naive_result = problem.solve_naive(start_year, end_year)
            optimized_result = problem.solve_optimized(start_year, end_year)
            math_result = problem.solve_mathematical(start_year, end_year)

            assert naive_result == optimized_result, (
                f"Range {start_year}-{end_year}: naive vs optimized"
            )
            assert naive_result == math_result, (
                f"Range {start_year}-{end_year}: naive vs mathematical"
            )

    def test_single_year_cases(self, problem: Any) -> None:
        """特定年のテストケース"""
        # 2000年（うるう年）での検証
        result_2000_naive = problem.solve_naive(2000, 2000)
        result_2000_optimized = problem.solve_optimized(2000, 2000)
        result_2000_math = problem.solve_mathematical(2000, 2000)

        assert result_2000_naive == result_2000_optimized == result_2000_math

        # 1900年（世紀年、平年）での検証（ただし問題範囲外）
        # 範囲を1901年に調整してテスト
        result_1901_naive = problem.solve_naive(1901, 1901)
        result_1901_optimized = problem.solve_optimized(1901, 1901)
        result_1901_math = problem.solve_mathematical(1901, 1901)

        assert result_1901_naive == result_1901_optimized == result_1901_math


class TestSolutionConsistency:
    """解法間の一貫性テスト"""

    def test_all_solutions_agree_problem_range(self, problem: Any) -> None:
        """本問題の範囲で全解法が一致することを確認"""
        start_year, end_year = 1901, 2000

        naive_result = problem.solve_naive(start_year, end_year)
        optimized_result = problem.solve_optimized(start_year, end_year)
        math_result = problem.solve_mathematical(start_year, end_year)

        assert naive_result == optimized_result == math_result

    def test_partial_ranges_consistency(self, problem: Any) -> None:
        """部分範囲での一貫性テスト"""
        test_cases = [
            (1901, 1920),  # 20世紀前期
            (1921, 1950),  # 20世紀中期前半
            (1951, 1980),  # 20世紀中期後半
            (1981, 2000),  # 20世紀後期
        ]

        for start_year, end_year in test_cases:
            naive_result = problem.solve_naive(start_year, end_year)
            optimized_result = problem.solve_optimized(start_year, end_year)
            math_result = problem.solve_mathematical(start_year, end_year)

            assert naive_result == optimized_result == math_result


class TestEdgeCases:
    """エッジケースのテスト"""

    def test_single_year_range(self, problem: Any) -> None:
        """1年だけの範囲のテスト"""
        year = 1950
        naive_result = problem.solve_naive(year, year)
        optimized_result = problem.solve_optimized(year, year)
        math_result = problem.solve_mathematical(year, year)

        assert naive_result == optimized_result == math_result
        # 1年間では0〜12の範囲の値になるはず
        assert 0 <= naive_result <= 12

    def test_leap_year_boundary(self, problem: Any) -> None:
        """うるう年境界でのテスト"""
        # 1999-2000（世紀境界でうるう年）
        result_boundary = problem.solve_naive(1999, 2000)
        result_boundary_opt = problem.solve_optimized(1999, 2000)
        result_boundary_math = problem.solve_mathematical(1999, 2000)

        assert result_boundary == result_boundary_opt == result_boundary_math

    def test_century_boundary(self, problem: Any) -> None:
        """世紀境界でのテスト"""
        # 1900年は含まれないが、2000年は含まれる
        # 1999-2000で世紀境界をテスト
        naive_result = problem.solve_naive(1999, 2000)
        optimized_result = problem.solve_optimized(1999, 2000)
        math_result = problem.solve_mathematical(1999, 2000)

        assert naive_result == optimized_result == math_result


class TestResultBounds:
    """結果の境界テスト"""

    def test_result_reasonable_bounds(self, problem: Any) -> None:
        """結果が妥当な範囲内であることを確認"""
        # 100年間での結果をテスト
        result = problem.solve_naive(1901, 2000)

        # 100年 = 1200ヶ月
        # 理論的最小値: 0（すべての月初が日曜日以外）
        # 理論的最大値: 1200（すべての月初が日曜日）
        # 実際は確率的に1200/7 ≈ 171前後が期待値
        assert 0 <= result <= 1200
        assert 100 <= result <= 250  # より現実的な範囲

    def test_proportional_results(self, problem: Any) -> None:
        """期間に比例した結果が得られることを確認"""
        result_10_years = problem.solve_naive(1901, 1910)
        result_20_years = problem.solve_naive(1901, 1920)
        result_50_years = problem.solve_naive(1901, 1950)

        # 長期間の方が多くの日曜日があるはず
        assert result_10_years <= result_20_years <= result_50_years


if __name__ == "__main__":
    pytest.main([__file__])
