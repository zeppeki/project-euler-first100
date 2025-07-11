"""Tests for Problem 091: Right triangles with integer coordinates"""

import pytest

from problems.problem_091 import (
    gcd,
    is_right_triangle,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem091:
    """Test cases for Problem 091 solutions"""

    def test_is_right_triangle_basic(self) -> None:
        """Test basic right triangle detection"""
        # Simple right triangle at origin
        assert is_right_triangle(1, 0, 0, 1) is True

        # Not a triangle (same point)
        assert is_right_triangle(1, 1, 1, 1) is False

        # Not a triangle (point at origin)
        assert is_right_triangle(0, 0, 1, 1) is False

        # 3-4-5 right triangle
        assert is_right_triangle(3, 0, 0, 4) is True

        # Not a right triangle
        assert is_right_triangle(1, 1, 2, 2) is False

    def test_is_right_triangle_examples(self) -> None:
        """Test with examples from problem statement"""
        # From the 2x2 grid examples
        assert is_right_triangle(1, 0, 0, 1) is True
        assert is_right_triangle(2, 0, 0, 1) is True
        assert is_right_triangle(2, 0, 0, 2) is True
        assert is_right_triangle(1, 0, 1, 1) is True
        assert is_right_triangle(2, 0, 2, 1) is True
        assert is_right_triangle(2, 0, 2, 2) is True

    def test_is_right_triangle_symmetry(self) -> None:
        """Test that P and Q order doesn't matter"""
        # Same triangle, different order
        assert is_right_triangle(1, 0, 0, 1) == is_right_triangle(0, 1, 1, 0)
        assert is_right_triangle(2, 0, 1, 1) == is_right_triangle(1, 1, 2, 0)

    def test_gcd(self) -> None:
        """Test greatest common divisor function"""
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5
        assert gcd(12, 8) == 4
        assert gcd(17, 19) == 1
        assert gcd(100, 50) == 50

    def test_small_grid(self) -> None:
        """Test with small grid (2x2)"""
        # Problem states there are 14 right triangles in 2x2 grid
        assert solve_naive(2) == 14
        assert solve_optimized(2) == 14
        assert solve_mathematical(2) == 14

    def test_trivial_cases(self) -> None:
        """Test edge cases"""
        # 0x0 grid - no triangles possible
        assert solve_naive(0) == 0
        assert solve_optimized(0) == 0
        assert solve_mathematical(0) == 0

        # 1x1 grid - only 3 triangles possible
        # (1,0), (0,1) and (1,1), (1,0) and (1,1), (0,1)
        assert solve_naive(1) == 3
        assert solve_optimized(1) == 3
        assert solve_mathematical(1) == 3

    def test_solutions_consistency(self) -> None:
        """Test that all solutions give same result for various inputs"""
        test_limits = [2, 3, 5, 10]

        for limit in test_limits:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            mathematical_result = solve_mathematical(limit)

            assert naive_result == optimized_result == mathematical_result, (
                f"Solutions differ for limit={limit}: "
                f"naive={naive_result}, optimized={optimized_result}, "
                f"mathematical={mathematical_result}"
            )

    def test_known_values(self) -> None:
        """Test against known values"""
        # Known values for small grids
        known_values = {
            0: 0,
            1: 3,
            2: 14,
            3: 33,
            5: 101,  # Corrected value
            10: 448,
        }

        for limit, expected in known_values.items():
            assert solve_optimized(limit) == expected, (
                f"Wrong result for limit={limit}: expected {expected}"
            )

    @pytest.mark.slow
    def test_large_grid(self) -> None:
        """Test with larger grid (slower test)"""
        # Test that solution works for larger inputs
        result = solve_optimized(20)
        assert result > 0
        assert isinstance(result, int)

        # Verify consistency between methods for medium size
        assert solve_naive(15) == solve_optimized(15)

    def test_right_triangle_at_different_vertices(self) -> None:
        """Test triangles with right angles at different vertices"""
        # Right angle at origin
        assert is_right_triangle(1, 0, 0, 1) is True

        # Right angle at P
        assert is_right_triangle(1, 0, 1, 1) is True

        # Right angle at Q
        assert is_right_triangle(0, 1, 1, 1) is True

    def test_collinear_points(self) -> None:
        """Test that collinear points don't form triangles"""
        # Points on x-axis
        assert is_right_triangle(1, 0, 2, 0) is False

        # Points on y-axis
        assert is_right_triangle(0, 1, 0, 2) is False

        # Points on diagonal
        assert is_right_triangle(1, 1, 2, 2) is False

    def test_performance_characteristics(self) -> None:
        """Test that optimized solution is faster than naive"""
        import time

        limit = 15

        # Time naive solution
        start = time.time()
        naive_result = solve_naive(limit)
        naive_time = time.time() - start

        # Time optimized solution
        start = time.time()
        optimized_result = solve_optimized(limit)
        optimized_time = time.time() - start

        # Results should match
        assert naive_result == optimized_result

        # Optimized should not be significantly slower
        # (allowing some variance in timing)
        assert optimized_time <= naive_time * 1.5
