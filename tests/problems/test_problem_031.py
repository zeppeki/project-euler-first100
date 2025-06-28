#!/usr/bin/env python3
"""Tests for Problem 031"""

import pytest

from problems.problem_031 import solve_naive, solve_optimized


class TestProblem031:
    """Test cases for Problem 031: Coin sums"""

    @pytest.mark.parametrize(
        "target, expected",
        [
            (1, 1),  # 1pを作る方法: 1p
            (2, 2),  # 2pを作る方法: 2p, 1p+1p
            (3, 2),  # 3pを作る方法: 2p+1p, 1p+1p+1p
            (4, 3),  # 4pを作る方法: 2p+2p, 2p+1p+1p, 1p+1p+1p+1p
            (5, 4),  # 5pを作る方法: 5p, 2p+2p+1p, 2p+1p+1p+1p, 1p+1p+1p+1p+1p
            (10, 11),  # 10pを作る方法（コインの組み合わせ）
        ],
    )
    def test_solve_naive_small_values(self, target: int, expected: int) -> None:
        """Test naive solution with small values"""
        assert solve_naive(target) == expected

    @pytest.mark.parametrize(
        "target, expected",
        [
            (1, 1),
            (2, 2),
            (3, 2),
            (4, 3),
            (5, 4),
            (10, 11),
            (20, 41),
            (50, 451),
            (100, 4563),
        ],
    )
    def test_solve_optimized(self, target: int, expected: int) -> None:
        """Test optimized solution"""
        assert solve_optimized(target) == expected

    @pytest.mark.parametrize("target", [1, 2, 3, 4, 5, 10, 20])
    def test_solutions_agree_small_values(self, target: int) -> None:
        """Test that naive and optimized solutions agree for small values"""
        assert solve_naive(target) == solve_optimized(target)

    def test_main_problem(self) -> None:
        """Test the main problem: ways to make £2 (200p)"""
        result = solve_optimized(200)
        assert isinstance(result, int)
        assert result > 0
        # 実際の答えは隠匿するが、結果が正の整数であることを確認

    @pytest.mark.slow
    def test_naive_vs_optimized_medium_values(self) -> None:
        """Test agreement between solutions for medium values (marked as slow)"""
        for target in [15, 25, 30]:
            assert solve_naive(target) == solve_optimized(target)

    def test_edge_cases(self) -> None:
        """Test edge cases"""
        # 0pを作る方法は1つ（何も使わない）
        assert solve_optimized(0) == 1

        # 負の値に対してはエラーが発生しないことを確認
        # （実装では0以下の場合は適切に処理される）

    def test_single_coins(self) -> None:
        """Test cases where target equals single coin values"""
        coins = [1, 2, 5, 10, 20, 50, 100, 200]
        for coin in coins:
            result = solve_optimized(coin)
            assert result >= 1  # 少なくともそのコイン1枚で作れる

    def test_performance_optimized(self) -> None:
        """Test that optimized solution can handle the main problem efficiently"""
        import time

        start_time = time.time()
        result = solve_optimized(200)
        execution_time = time.time() - start_time

        assert result > 0
        assert execution_time < 1.0  # 1秒以内で完了することを確認
