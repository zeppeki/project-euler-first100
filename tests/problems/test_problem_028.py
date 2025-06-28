#!/usr/bin/env python3
"""Tests for Problem 028"""

import pytest

from problems.problem_028 import solve_mathematical, solve_naive, solve_optimized


class TestProblem028:
    """Test cases for Problem 028"""

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        test_cases = [
            (1, 1),
            (3, 25),
            (5, 101),
            (7, 261),
        ]

        for size, expected in test_cases:
            result = solve_naive(size)
            assert result == expected, (
                f"Expected {expected}, got {result} for size {size}"
            )

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        test_cases = [
            (1, 1),
            (3, 25),
            (5, 101),
            (7, 261),
            (9, 537),
            (101, 692101),
        ]

        for size, expected in test_cases:
            result = solve_optimized(size)
            assert result == expected, (
                f"Expected {expected}, got {result} for size {size}"
            )

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution"""
        test_cases = [
            (1, 1),
            (3, 25),
            (5, 101),
            (7, 261),
            (9, 537),
            (101, 692101),
            (1001, 669171001),  # Main problem answer
        ]

        for size, expected in test_cases:
            result = solve_mathematical(size)
            assert result == expected, (
                f"Expected {expected}, got {result} for size {size}"
            )

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        test_sizes = [1, 3, 5, 7, 9, 11, 13, 15]

        for size in test_sizes:
            naive_result = solve_naive(size)
            optimized_result = solve_optimized(size)
            mathematical_result = solve_mathematical(size)

            assert naive_result == optimized_result == mathematical_result, (
                f"Solutions disagree for size {size}: "
                f"naive={naive_result}, optimized={optimized_result}, "
                f"mathematical={mathematical_result}"
            )

    def test_invalid_input(self) -> None:
        """Test error handling for invalid inputs"""
        # Test even sizes (should raise ValueError)
        with pytest.raises(ValueError):
            solve_naive(2)

        with pytest.raises(ValueError):
            solve_optimized(4)

        with pytest.raises(ValueError):
            solve_mathematical(6)

    def test_edge_cases(self) -> None:
        """Test edge cases"""
        # Test minimum valid size
        assert solve_naive(1) == 1
        assert solve_optimized(1) == 1
        assert solve_mathematical(1) == 1

    @pytest.mark.slow
    def test_large_input(self) -> None:
        """Test with large input"""
        # Test main problem size
        size = 1001
        result_optimized = solve_optimized(size)
        result_mathematical = solve_mathematical(size)

        assert result_optimized == result_mathematical == 669171001

    def test_pattern_verification(self) -> None:
        """Test the spiral diagonal pattern"""
        # Manually verify small spirals

        # 1x1 spiral: [1] -> diagonal sum = 1
        assert solve_naive(1) == 1

        # 3x3 spiral:
        # 7 8 9
        # 6 1 2
        # 5 4 3
        # Diagonals: 7, 1, 3, 5, 9 -> sum = 25
        assert solve_naive(3) == 25

        # 5x5 spiral (from problem description):
        # 21 22 23 24 25
        # 20  7  8  9 10
        # 19  6  1  2 11
        # 18  5  4  3 12
        # 17 16 15 14 13
        # Diagonals: 21, 7, 1, 3, 13, 17, 5, 9, 25 -> sum = 101
        assert solve_naive(5) == 101

    def test_performance_comparison(self) -> None:
        """Test performance characteristics"""
        import time

        size = 101

        # Test optimized solution
        start_time = time.time()
        result_optimized = solve_optimized(size)
        optimized_time = time.time() - start_time

        # Test mathematical solution
        start_time = time.time()
        result_mathematical = solve_mathematical(size)
        mathematical_time = time.time() - start_time

        # Results should be the same
        assert result_optimized == result_mathematical

        # Mathematical solution should be faster (though both are very fast)
        # This is more of a sanity check than a strict requirement
        assert mathematical_time <= optimized_time * 10  # Allow some variance
