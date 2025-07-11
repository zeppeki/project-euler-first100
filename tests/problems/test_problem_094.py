#!/usr/bin/env python3
"""
Test for Problem 094: Almost equilateral triangles
"""

import pytest

from problems.problem_094 import (
    calculate_area,
    find_almost_equilateral_triangles,
    is_integral_area,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestUtilityFunctions:
    """Test utility functions for almost equilateral triangles."""

    def test_is_integral_area(self) -> None:
        """Test integral area calculation."""
        # Known example from problem statement
        assert is_integral_area(5, 5, 6) is True

        # Other valid almost equilateral triangles
        assert is_integral_area(17, 17, 16) is True
        assert is_integral_area(65, 65, 66) is True
        assert is_integral_area(241, 241, 240) is True

        # Invalid triangles (not integral area)
        assert is_integral_area(5, 5, 4) is False
        assert is_integral_area(13, 13, 14) is False
        assert is_integral_area(13, 13, 12) is False
        assert is_integral_area(3, 3, 4) is False
        assert is_integral_area(3, 3, 2) is False
        assert is_integral_area(4, 4, 5) is False

        # Degenerate triangles
        assert is_integral_area(1, 1, 2) is False  # Not a valid triangle
        assert is_integral_area(1, 1, 3) is False  # Not a valid triangle

    def test_calculate_area(self) -> None:
        """Test area calculation for valid triangles."""
        # Known example
        assert calculate_area(5, 5, 6) == 12

        # Other valid cases
        assert calculate_area(17, 17, 16) == 120
        assert calculate_area(65, 65, 66) == 1848
        assert calculate_area(241, 241, 240) == 25080

    def test_find_almost_equilateral_triangles(self) -> None:
        """Test finding almost equilateral triangles."""
        # Small limit
        triangles = find_almost_equilateral_triangles(100)
        assert len(triangles) >= 1  # Should find at least (5,5,6)

        # Check that all triangles are valid
        for triangle in triangles:
            a, b, c = triangle
            assert a == b  # Two sides equal
            assert abs(c - a) == 1  # Third side differs by 1
            assert is_integral_area(a, b, c)  # Integral area
            assert a + b + c <= 100  # Within perimeter limit

        # Check known triangles are included
        assert (5, 5, 6) in triangles
        assert (17, 17, 16) in triangles

        # Triangles should be sorted by perimeter
        perimeters = [sum(t) for t in triangles]
        assert perimeters == sorted(perimeters)

    def test_triangle_properties(self) -> None:
        """Test properties of almost equilateral triangles."""
        triangles = find_almost_equilateral_triangles(1000)

        for triangle in triangles:
            a, b, c = triangle

            # Properties check
            assert a == b  # Two sides equal
            assert abs(c - a) == 1  # Third side differs by 1
            assert a > 0 and b > 0 and c > 0  # Positive sides
            assert is_integral_area(a, b, c)  # Integral area

            # Triangle inequality
            assert a + b > c
            assert a + c > b
            assert b + c > a


class TestSolutionMethods:
    """Test solution methods with various inputs."""

    def test_small_cases(self) -> None:
        """Test solutions with small input values."""
        # Very small cases
        assert solve_naive(15) == 0  # No triangles with perimeter ≤ 15
        assert solve_optimized(15) == 0
        assert solve_mathematical(15) == 0

        # Case with known triangles
        result_100 = solve_naive(100)
        # (5,5,6) has perimeter 16, (17,17,16) has perimeter 50
        # So the sum should be 16 + 50 = 66
        triangles = find_almost_equilateral_triangles(100)
        expected = sum(sum(t) for t in triangles)
        assert result_100 == expected
        assert result_100 == 66

    def test_solution_consistency(self) -> None:
        """Test that all solution methods give the same results."""
        test_limits = [100, 500, 1000, 10000]

        for limit in test_limits:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            mathematical_result = solve_mathematical(limit)

            assert naive_result == optimized_result, (
                f"Naive vs Optimized mismatch at limit {limit}: "
                f"{naive_result} != {optimized_result}"
            )
            assert naive_result == mathematical_result, (
                f"Naive vs Mathematical mismatch at limit {limit}: "
                f"{naive_result} != {mathematical_result}"
            )

    def test_known_triangles(self) -> None:
        """Test with known almost equilateral triangles."""
        # Find triangles up to a reasonable limit
        triangles = find_almost_equilateral_triangles(1000)

        # Check that known triangles are present
        known_triangles = [(5, 5, 6), (17, 17, 16), (65, 65, 66), (241, 241, 240)]
        for triangle in known_triangles:
            assert triangle in triangles, f"Missing known triangle: {triangle}"

        # Verify their properties
        for triangle in known_triangles:
            a, b, c = triangle
            assert is_integral_area(a, b, c)
            area = calculate_area(a, b, c)
            assert area > 0
            assert isinstance(area, int)

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Very small limits
        assert solve_naive(1) == 0
        assert solve_optimized(1) == 0
        assert solve_mathematical(1) == 0

        # Limits that exclude all triangles
        assert solve_naive(10) == 0
        assert solve_optimized(10) == 0
        assert solve_mathematical(10) == 0

        # Minimum limit to include smallest triangle
        # Smallest triangle is (5,5,6) with perimeter 16
        assert solve_naive(16) == 16
        assert solve_optimized(16) == 16
        assert solve_mathematical(16) == 16

        # Include next triangle (17,17,16) with perimeter 50
        result_50 = solve_naive(50)
        assert result_50 == 16 + 50  # Both triangles included
        assert solve_optimized(50) == result_50
        assert solve_mathematical(50) == result_50

    @pytest.mark.slow
    def test_large_case(self) -> None:
        """Test with larger input (marked as slow)."""
        # Test with moderately large limit
        limit = 100000
        result_optimized = solve_optimized(limit)
        result_mathematical = solve_mathematical(limit)

        assert result_optimized == result_mathematical
        assert result_optimized > 0

        # Verify by checking actual triangles
        triangles = find_almost_equilateral_triangles(limit)
        expected = sum(sum(t) for t in triangles)
        assert result_optimized == expected

    def test_result_properties(self) -> None:
        """Test properties of the results."""
        # Results should be positive for reasonable limits
        assert solve_optimized(100) > 0
        assert solve_mathematical(100) > 0

        # Results should increase with larger limits
        result_100 = solve_optimized(100)
        result_1000 = solve_optimized(1000)
        result_10000 = solve_optimized(10000)

        assert result_1000 >= result_100
        assert result_10000 >= result_1000


class TestProblem094:
    """Test the main problem solution."""

    def test_pell_equation_solutions(self) -> None:
        """Test that Pell equation solutions work correctly."""
        # Test the sequence generation
        x, y = 2, 1
        solutions = [(x, y)]

        for _ in range(5):
            x, y = 2 * x + 3 * y, x + 2 * y
            solutions.append((x, y))

        # Verify that solutions satisfy x² - 3y² = 1
        for x, y in solutions:
            assert x * x - 3 * y * y == 1

        # Check that solutions grow exponentially
        for i in range(1, len(solutions)):
            assert solutions[i][0] > solutions[i - 1][0]
            assert solutions[i][1] > solutions[i - 1][1]

    def test_triangle_generation_from_pell(self) -> None:
        """Test triangle generation from Pell equation solutions."""
        triangles = find_almost_equilateral_triangles(1000)

        # All triangles should be valid
        for triangle in triangles:
            a, b, c = triangle
            assert a == b
            assert abs(c - a) == 1
            assert is_integral_area(a, b, c)

        # Check that we get the expected small triangles
        small_triangles = [t for t in triangles if sum(t) <= 100]
        assert len(small_triangles) >= 2

    def test_algorithm_correctness(self) -> None:
        """Test algorithm correctness with known cases."""
        # Test specific cases
        limit = 1000
        triangles = find_almost_equilateral_triangles(limit)
        total_perimeter = sum(sum(t) for t in triangles)

        # All three methods should give the same result
        assert solve_naive(limit) == total_perimeter
        assert solve_optimized(limit) == total_perimeter
        assert solve_mathematical(limit) == total_perimeter

        # Check some specific triangles
        assert (5, 5, 6) in triangles
        assert (17, 17, 16) in triangles

        # Areas should be correct
        assert calculate_area(5, 5, 6) == 12
        assert calculate_area(17, 17, 16) == 120

    def test_performance_characteristics(self) -> None:
        """Test performance characteristics of different approaches."""
        # Mathematical approach should handle large limits efficiently
        limit = 1000000
        result = solve_mathematical(limit)
        assert result > 0

        # Should be much larger than small limit results
        small_result = solve_mathematical(1000)
        assert result > small_result

    def test_triangle_distribution(self) -> None:
        """Test distribution of triangles."""
        triangles = find_almost_equilateral_triangles(10000)

        # Should have both types: (a,a,a+1) and (a,a,a-1)
        type1 = [t for t in triangles if t[2] == t[0] + 1]  # (a,a,a+1)
        type2 = [t for t in triangles if t[2] == t[0] - 1]  # (a,a,a-1)

        assert len(type1) > 0
        assert len(type2) > 0

        # Both types should contribute to the total
        total_type1 = sum(sum(t) for t in type1)
        total_type2 = sum(sum(t) for t in type2)

        assert total_type1 > 0
        assert total_type2 > 0

        # Total should match
        expected_total = total_type1 + total_type2
        actual_total = solve_mathematical(10000)
        assert actual_total == expected_total
