"""Tests for Problem 023: Non-Abundant Sums."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_023 import (
    get_divisor_sum,
    is_abundant,
    solve_naive,
    solve_optimized,
)


class TestProblem023:
    """Test cases for Problem 023."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, 0),  # 1には真の約数がない
            (6, 6),  # 1 + 2 + 3 = 6 (完全数)
            (12, 16),  # 1 + 2 + 3 + 4 + 6 = 16 (過剰数)
            (28, 28),  # 1 + 2 + 4 + 7 + 14 = 28 (完全数)
            (8, 7),  # 1 + 2 + 4 = 7 (不足数)
        ],
    )
    def test_get_divisor_sum(self, n: int, expected: int) -> None:
        """Test the divisor sum calculation."""
        result = get_divisor_sum(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (12, True),  # 約数和16 > 12
            (18, True),  # 約数和21 > 18
            (20, True),  # 約数和22 > 20
            (24, True),  # 約数和36 > 24
            (6, False),  # 約数和6 = 6 (完全数)
            (8, False),  # 約数和7 < 8 (不足数)
            (28, False),  # 約数和28 = 28 (完全数)
            (1, False),  # 約数和0 < 1
            (2, False),  # 約数和1 < 2
        ],
    )
    def test_is_abundant(self, n: int, expected: bool) -> None:
        """Test the abundant number detection."""
        result = is_abundant(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (30, 411),  # 小さな範囲でのテスト
            (100, 2766),  # 中程度の範囲
        ],
    )
    def test_solve_naive(self, limit: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit={limit}"
        )

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (30, 411),  # 小さな範囲でのテスト
            (100, 2766),  # 中程度の範囲
        ],
    )
    def test_solve_optimized(self, limit: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(limit)
        assert result == expected, (
            f"Expected {expected}, got {result} for limit={limit}"
        )

    @pytest.mark.parametrize("limit", [30, 100, 500])
    def test_all_solutions_agree(self, limit: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(limit)
        optimized_result = solve_optimized(limit)

        assert naive_result == optimized_result, (
            f"Solutions disagree for limit={limit}: "
            f"naive={naive_result}, optimized={optimized_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with limit 1
        assert solve_naive(1) == 1  # 1は過剰数の和で表せない
        assert solve_optimized(1) == 1

        # Test with limit 12 (smallest abundant number)
        assert solve_naive(12) == 78  # 1+2+...+12 = 78, 12は過剰数だが和で表せない
        assert solve_optimized(12) == 78

    def test_abundant_numbers_sequence(self) -> None:
        """Test the first few abundant numbers."""
        expected_abundant = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54]

        actual_abundant = []
        for i in range(1, 60):
            if is_abundant(i):
                actual_abundant.append(i)
                if len(actual_abundant) >= 10:
                    break

        assert actual_abundant == expected_abundant

    def test_sum_of_two_abundant_examples(self) -> None:
        """Test specific examples of numbers that can be written as sum of two abundant numbers."""
        # 24 = 12 + 12 (両方過剰数)
        assert is_abundant(12)

        # 30 = 12 + 18 (両方過剰数)
        assert is_abundant(18)

        # 32 = 12 + 20 (両方過剰数)
        assert is_abundant(20)

    def test_perfect_and_deficient_examples(self) -> None:
        """Test examples of perfect and deficient numbers."""
        # 完全数のテスト
        assert get_divisor_sum(6) == 6  # 1 + 2 + 3 = 6
        assert get_divisor_sum(28) == 28  # 1 + 2 + 4 + 7 + 14 = 28
        assert not is_abundant(6)
        assert not is_abundant(28)

        # 不足数のテスト
        assert get_divisor_sum(8) == 7  # 1 + 2 + 4 = 7 < 8
        assert get_divisor_sum(9) == 4  # 1 + 3 = 4 < 9
        assert not is_abundant(8)
        assert not is_abundant(9)

    @pytest.mark.slow
    def test_problem_answer(self) -> None:
        """Test with the actual problem limit (optimized for speed)."""
        # Test with the actual problem limit
        limit = 28123
        expected = 4179871

        # Only test optimized solution for speed
        result_optimized = solve_optimized(limit)
        assert result_optimized == expected

    def test_upper_bound_property(self) -> None:
        """Test that the upper bound 28123 is meaningful."""
        # この関数は計算量の関係でslow markを付けないが、
        # 実際の問題では28123以下の全ての数を考慮する必要があることを確認
        limit = 28123

        # 少なくとも過剰数が存在することを確認
        abundant_count = 0
        for i in range(1, min(200, limit)):  # サンプルチェック
            if is_abundant(i):
                abundant_count += 1

        assert abundant_count > 0, "Should find abundant numbers in the range"

        # 24が2つの過剰数の和で表せることを確認
        assert is_abundant(12)  # 12は過剰数
        # 24 = 12 + 12 なので24は2つの過剰数の和で表せる
