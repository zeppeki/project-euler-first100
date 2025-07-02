#!/usr/bin/env python3
"""
Problem 019 Runner: Execution and demonstration code for Problem 019.

This module handles the execution and demonstration of Problem 019 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_019 import (
    solve_mathematical,
    solve_naive,
    solve_optimized,
    validate_days_in_month_calculation,
    validate_leap_year_calculation,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem019Runner(BaseProblemRunner):
    """Runner for Problem 019: Counting Sundays."""

    def __init__(self) -> None:
        super().__init__("019", "Counting Sundays")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 019."""
        return [
            ((1901, 1), (1901, 12), 2),  # 1901年の1年間
            ((1900, 1), (1900, 12), 2),  # 1900年の1年間（うるう年ではない）
            ((2000, 1), (2000, 12), 2),  # 2000年の1年間（うるう年）
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 019."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ((1901, 1), (2000, 12))

    def get_demonstration_functions(self) -> list[tuple[str, Callable[[], None]]]:
        """Get demonstration functions for Problem 019."""
        return [("カレンダー計算の検証", self._demonstrate_calendar_validation)]

    def _demonstrate_calendar_validation(self) -> None:
        """カレンダー計算の検証を表示"""
        print("=== 基本検証 ===")
        validate_leap_year_calculation()
        validate_days_in_month_calculation()

        result = solve_optimized(((1901, 1), (2000, 12)))
        print(f"\n20世紀中の月初日曜日数: {result}")

        print("\n各年代別の分析:")
        decades = [
            (1901, 1910, "1900年代"),
            (1911, 1920, "1910年代"),
            (1921, 1930, "1920年代"),
            (1931, 1940, "1930年代"),
            (1941, 1950, "1940年代"),
            (1951, 1960, "1950年代"),
            (1961, 1970, "1960年代"),
            (1971, 1980, "1970年代"),
            (1981, 1990, "1980年代"),
            (1991, 2000, "1990年代"),
        ]

        for start_year, end_year, description in decades:
            count = solve_optimized(((start_year, 1), (end_year, 12)))
            print(f"{description} ({start_year}-{end_year}): {count}回")

        print("\nうるう年の分析:")
        leap_years = [
            year
            for year in range(1901, 2001)
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        ]
        print(f"期間内のうるう年: {leap_years}")
        print(f"うるう年の数: {len(leap_years)}")


def main() -> None:
    """メイン関数"""
    runner = Problem019Runner()
    runner.main()


if __name__ == "__main__":
    main()
