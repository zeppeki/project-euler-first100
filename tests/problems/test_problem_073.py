#!/usr/bin/env python3
"""
Test cases for Problem 073: Counting fractions in a range
"""

import pytest

from problems.problem_073 import (
    analyze_fraction_distribution,
    count_fractions_in_range,
    find_closest_fractions,
    get_fractions_by_denominator,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    verify_small_example,
)


class TestProblem073:
    """Test cases for Problem 073 solutions."""

    def test_verify_small_example(self) -> None:
        """Test the small example verification."""
        count, fractions = verify_small_example()
        assert count == 3
        assert len(fractions) == 3

        # Check that the fractions are 3/8, 2/5, 3/7
        expected = [(3, 8), (2, 5), (3, 7)]
        assert fractions == expected

        # Verify they are in ascending order
        values = [n / d for n, d in fractions]
        assert values == sorted(values)

        # Verify they are between 1/3 and 1/2
        for n, d in fractions:
            assert 1 / 3 < n / d < 1 / 2

    def test_solve_naive_basic(self) -> None:
        """Test solve_naive with basic cases."""
        assert solve_naive(8) == 3
        assert solve_naive(12) == 7
        assert solve_naive(1) == 0
        assert solve_naive(2) == 0

    def test_solve_optimized_basic(self) -> None:
        """Test solve_optimized with basic cases."""
        assert solve_optimized(8) == 3
        assert solve_optimized(12) == 7
        assert solve_optimized(1) == 0
        assert solve_optimized(2) == 0

    def test_solve_mathematical_basic(self) -> None:
        """Test solve_mathematical with basic cases."""
        assert solve_mathematical(8) == 3
        assert solve_mathematical(12) == 7
        assert solve_mathematical(1) == 0
        assert solve_mathematical(2) == 0

    def test_solutions_agree(self) -> None:
        """Test that all solutions produce the same results."""
        test_cases = [8, 12, 20, 50, 100]

        for limit in test_cases:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            mathematical_result = solve_mathematical(limit)

            assert naive_result == optimized_result
            assert optimized_result == mathematical_result
            assert naive_result == mathematical_result

    def test_count_fractions_in_range(self) -> None:
        """Test the general range counting function."""
        # Test with 1/3 and 1/2 range
        result = count_fractions_in_range(8, 1, 3, 1, 2)
        assert result == 3

        # Test with different range
        result = count_fractions_in_range(8, 1, 4, 1, 2)
        assert result >= 3  # Should include more fractions

    def test_get_fractions_by_denominator(self) -> None:
        """Test getting fractions grouped by denominator."""
        fractions_by_d = get_fractions_by_denominator(8)

        # Check that we have the expected denominators
        assert 5 in fractions_by_d
        assert 7 in fractions_by_d
        assert 8 in fractions_by_d

        # Check specific fractions
        assert (2, 5) in fractions_by_d[5]
        assert (3, 7) in fractions_by_d[7]
        assert (3, 8) in fractions_by_d[8]

    def test_find_closest_fractions(self) -> None:
        """Test finding fractions closest to 1/3 and 1/2."""
        closest_to_third, closest_to_half = find_closest_fractions(100)

        assert closest_to_third is not None
        assert closest_to_half is not None

        # Check that they are valid fractions
        n1, d1 = closest_to_third
        n2, d2 = closest_to_half

        assert 1 / 3 < n1 / d1 < 1 / 2
        assert 1 / 3 < n2 / d2 < 1 / 2

        # Check that they are close to the respective bounds
        assert abs(n1 / d1 - 1 / 3) < 0.01
        assert abs(n2 / d2 - 1 / 2) < 0.01

    def test_analyze_fraction_distribution(self) -> None:
        """Test fraction distribution analysis."""
        analysis = analyze_fraction_distribution(20)

        assert "total_count" in analysis
        assert "denominator_counts" in analysis
        assert "fraction_values" in analysis
        assert "min_value" in analysis
        assert "max_value" in analysis
        assert "avg_value" in analysis

        # Check that values are reasonable
        assert analysis["total_count"] > 0
        assert 1 / 3 < analysis["min_value"] < 1 / 2
        assert 1 / 3 < analysis["max_value"] < 1 / 2
        assert 1 / 3 < analysis["avg_value"] < 1 / 2

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with very small limits
        assert solve_naive(3) == 0
        assert solve_optimized(3) == 0
        assert solve_mathematical(3) == 0

        # Test with limit that gives exactly one fraction
        assert solve_naive(5) == 1
        assert solve_optimized(5) == 1
        assert solve_mathematical(5) == 1

    @pytest.mark.parametrize(
        "limit, expected",
        [
            (8, 3),
            (12, 7),
            (20, 21),
            (50, 129),
            (100, 505),
        ],
    )
    def test_parametrized_solutions(self, limit: int, expected: int) -> None:
        """Test solutions with parametrized inputs."""
        assert solve_naive(limit) == expected
        assert solve_optimized(limit) == expected
        assert solve_mathematical(limit) == expected

    @pytest.mark.slow
    def test_large_limit(self) -> None:
        """Test with large limit (slow test)."""
        # Test with the actual problem limit
        result = solve_mathematical(12000)
        assert result == 7295372  # Expected answer

    def test_fraction_validity(self) -> None:
        """Test that all found fractions are valid."""
        fractions_by_d = get_fractions_by_denominator(50)

        for d, fractions in fractions_by_d.items():
            for n, d_val in fractions:
                assert d == d_val
                assert n < d
                assert 1 / 3 < n / d < 1 / 2

                # Check that fraction is in reduced form
                from math import gcd

                assert gcd(n, d) == 1

    def test_increasing_count(self) -> None:
        """Test that count increases with limit."""
        prev_count = 0
        for limit in [5, 10, 20, 50, 100]:
            count = solve_mathematical(limit)
            assert count >= prev_count
            prev_count = count
