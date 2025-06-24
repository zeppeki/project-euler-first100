"""Tests for Problem 011: Largest product in a grid."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

from problems.problem_011 import (
    GRID_DATA,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


def test_small_grid() -> None:
    """小さな4x4グリッドでの正答検証"""
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    expected = 13 * 14 * 15 * 16  # 43680
    assert solve_naive(grid, 4) == expected
    assert solve_optimized(grid, 4) == expected
    assert solve_mathematical(grid, 4) == expected


def test_all_solutions_agree_on_main_grid() -> None:
    """20x20グリッドで全解法が一致することを検証"""
    result_naive = solve_naive(GRID_DATA, 4)
    result_optimized = solve_optimized(GRID_DATA, 4)
    result_math = solve_mathematical(GRID_DATA, 4)
    assert result_naive == result_optimized == result_math
    assert result_naive > 0


def test_edge_cases() -> None:
    """エッジケースの検証（空グリッドや長さ1など）"""
    assert solve_naive([], 4) == 0
    assert solve_optimized([], 4) == 0
    assert solve_mathematical([], 4) == 0
    grid = [[1]]
    assert solve_naive(grid, 1) == 1
    assert solve_optimized(grid, 1) == 1
    assert solve_mathematical(grid, 1) == 1


@pytest.mark.slow
def test_performance_on_main_grid() -> None:
    """20x20グリッドでのパフォーマンステスト（遅いのでslowマーク）"""
    result = solve_mathematical(GRID_DATA, 4)
    assert result > 0
