#!/usr/bin/env python3
"""
Tests for Problem 075: Singular integer right triangles
"""

import pytest

from problems.problem_075 import (
    analyze_perimeter_distribution,
    count_triangles_by_perimeter,
    find_triangles_with_perimeter,
    gcd,
    generate_primitive_pythagorean_triples,
    get_examples_by_triangle_count,
    solve_naive,
    solve_optimized,
    verify_small_examples,
)


class TestUtilityFunctions:
    """Test utility functions."""

    def test_gcd(self) -> None:
        """Test greatest common divisor calculation."""
        assert gcd(12, 8) == 4
        assert gcd(15, 25) == 5
        assert gcd(17, 13) == 1
        assert gcd(100, 50) == 50
        assert gcd(0, 5) == 5
        assert gcd(7, 0) == 7

    def test_gcd_commutative(self) -> None:
        """Test that gcd is commutative."""
        test_pairs = [(12, 8), (15, 25), (17, 13), (100, 50)]
        for a, b in test_pairs:
            assert gcd(a, b) == gcd(b, a)


class TestPythagoreanTripleGeneration:
    """Test Pythagorean triple generation."""

    def test_generate_primitive_pythagorean_triples_small(self) -> None:
        """Test primitive triple generation with small limit."""
        triples = generate_primitive_pythagorean_triples(30)

        # Should include (3,4,5) and (5,12,13)
        assert (3, 4, 5) in triples
        assert (5, 12, 13) in triples

        # Check that all are primitive (gcd = 1)
        for a, b, c in triples:
            assert gcd(gcd(a, b), c) == 1

        # Check Pythagorean theorem
        for a, b, c in triples:
            assert a * a + b * b == c * c

        # Check perimeter constraint
        for a, b, c in triples:
            assert a + b + c <= 30

    def test_generate_primitive_pythagorean_triples_properties(self) -> None:
        """Test properties of generated primitive triples."""
        triples = generate_primitive_pythagorean_triples(100)

        for a, b, c in triples:
            # Check Pythagorean theorem
            assert a * a + b * b == c * c

            # Check ordering: a ≤ b < c
            assert a <= b < c

            # Check primitivity
            assert gcd(gcd(a, b), c) == 1

            # Check perimeter constraint
            assert a + b + c <= 100

    def test_known_primitive_triples(self) -> None:
        """Test that known primitive triples are generated."""
        triples = generate_primitive_pythagorean_triples(200)

        known_triples = [
            (3, 4, 5),  # m=2, n=1
            (5, 12, 13),  # m=3, n=2
            (8, 15, 17),  # m=4, n=1
            (7, 24, 25),  # m=4, n=3
            (20, 21, 29),  # m=5, n=2
            (9, 40, 41),  # m=5, n=4
        ]

        for triple in known_triples:
            assert triple in triples or (triple[1], triple[0], triple[2]) in triples


class TestTriangleCountingByPerimeter:
    """Test triangle counting by perimeter."""

    def test_count_triangles_by_perimeter_small(self) -> None:
        """Test triangle counting with small perimeters."""
        counts = count_triangles_by_perimeter(50)

        # Known cases from problem statement
        assert counts.get(12, 0) == 1  # (3,4,5) only
        assert counts.get(24, 0) == 1  # (6,8,10) only
        assert counts.get(30, 0) == 1  # (5,12,13) only

        # Should have no count for 20 (no integer triangle)
        assert counts.get(20, 0) == 0

    def test_count_triangles_by_perimeter_consistency(self) -> None:
        """Test consistency of triangle counting."""
        counts = count_triangles_by_perimeter(100)

        # All counts should be non-negative
        for perimeter, count in counts.items():
            assert count > 0
            assert perimeter <= 100


class TestSolutionMethods:
    """Test solution methods."""

    def test_solve_naive_small_cases(self) -> None:
        """Test naive solution with small cases."""
        # Very small cases
        assert solve_naive(10) == 0  # No triangles possible
        assert solve_naive(15) >= 1  # Should include perimeter 12

        # Known case
        result_48 = solve_naive(48)
        assert isinstance(result_48, int)
        assert result_48 >= 0

    def test_solve_optimized_small_cases(self) -> None:
        """Test optimized solution with small cases."""
        # Very small cases
        assert solve_optimized(10) == 0  # No triangles possible
        assert solve_optimized(15) >= 1  # Should include perimeter 12

        # Known case
        result_48 = solve_optimized(48)
        assert isinstance(result_48, int)
        assert result_48 >= 0

    def test_solution_consistency(self) -> None:
        """Test that both solutions give consistent results."""
        test_limits = [48, 100, 200, 500]

        for limit in test_limits:
            naive_result = solve_naive(limit)
            optimized_result = solve_optimized(limit)
            assert naive_result == optimized_result

    @pytest.mark.parametrize(
        "limit,expected",
        [
            (48, 6),
            (120, 13),  # 実際の計算値に修正
            (1000, 112),
        ],
    )
    def test_known_results(self, limit: int, expected: int) -> None:
        """Test against known results for specific limits."""
        assert solve_optimized(limit) == expected


class TestTriangleSearching:
    """Test triangle searching functions."""

    def test_find_triangles_with_perimeter(self) -> None:
        """Test finding triangles with specific perimeter."""
        # Test known cases
        triangles_12 = find_triangles_with_perimeter(12)
        assert len(triangles_12) == 1
        assert (3, 4, 5) in triangles_12

        triangles_30 = find_triangles_with_perimeter(30)
        assert len(triangles_30) == 1
        assert (5, 12, 13) in triangles_30

        # Test case with no solutions
        triangles_20 = find_triangles_with_perimeter(20)
        assert len(triangles_20) == 0

    def test_find_triangles_multiple_solutions(self) -> None:
        """Test finding triangles with multiple solutions."""
        # Cases with multiple solutions - test with known multiple solution case
        triangles_120 = find_triangles_with_perimeter(120)
        assert len(triangles_120) >= 2

        # Verify all found triangles
        for a, b, c in triangles_120:
            assert a * a + b * b == c * c
            assert a + b + c == 120
            assert a <= b < c

    def test_triangle_validation(self) -> None:
        """Test that all found triangles are valid."""
        test_perimeters = [12, 24, 30, 36, 40, 48, 60]

        for perimeter in test_perimeters:
            triangles = find_triangles_with_perimeter(perimeter)
            for a, b, c in triangles:
                # Check Pythagorean theorem
                assert a * a + b * b == c * c

                # Check perimeter
                assert a + b + c == perimeter

                # Check ordering
                assert a <= b < c

                # Check positive integers
                assert a > 0 and b > 0 and c > 0


class TestAnalysisFunctions:
    """Test analysis functions."""

    def test_analyze_perimeter_distribution(self) -> None:
        """Test perimeter distribution analysis."""
        analysis = analyze_perimeter_distribution(200)

        # Check required keys
        required_keys = [
            "total_valid_perimeters",
            "singular_perimeters",
            "multiple_solution_perimeters",
            "count_distribution",
            "max_triangles_per_perimeter",
            "avg_triangles_per_perimeter",
        ]
        for key in required_keys:
            assert key in analysis

        # Check reasonable values
        assert analysis["total_valid_perimeters"] > 0
        assert analysis["singular_perimeters"] >= 0
        assert analysis["multiple_solution_perimeters"] >= 0
        assert analysis["max_triangles_per_perimeter"] >= 1
        assert analysis["avg_triangles_per_perimeter"] >= 1.0

    def test_get_examples_by_triangle_count(self) -> None:
        """Test getting examples by triangle count."""
        # Get singular examples
        singular_examples = get_examples_by_triangle_count(100, 1, 3)
        assert len(singular_examples) <= 3

        for perimeter, triangles in singular_examples:
            assert len(triangles) == 1
            a, b, c = triangles[0]
            assert a * a + b * b == c * c
            assert a + b + c == perimeter

        # Get multiple examples
        multiple_examples = get_examples_by_triangle_count(100, 2, 3)
        assert len(multiple_examples) <= 3

        for perimeter, triangles in multiple_examples:
            assert len(triangles) == 2
            for a, b, c in triangles:
                assert a * a + b * b == c * c
                assert a + b + c == perimeter

    def test_verify_small_examples(self) -> None:
        """Test verification of small examples from problem statement."""
        examples = verify_small_examples()

        # Check that key perimeters are included
        expected_perimeters = [12, 24, 30, 36, 40, 48, 120]
        for perimeter in expected_perimeters:
            assert perimeter in examples

        # Verify specific cases
        assert len(examples[12]) == 1  # Singular
        assert len(examples[30]) == 1  # Singular
        assert len(examples[36]) == 1  # Actually singular based on our calculation
        assert len(examples[120]) >= 3  # Multiple (exactly 3 mentioned in problem)

        # Verify triangle validity
        for perimeter, triangles in examples.items():
            for a, b, c in triangles:
                assert a * a + b * b == c * c
                assert a + b + c == perimeter


class TestEdgeCasesAndPerformance:
    """Test edge cases and performance characteristics."""

    def test_small_limits(self) -> None:
        """Test behavior with very small limits."""
        assert solve_naive(5) == 0
        assert solve_optimized(5) == 0
        assert solve_naive(11) == 0
        assert solve_optimized(11) == 0

    def test_increasing_counts(self) -> None:
        """Test that singular count increases with limit."""
        prev_count = 0
        test_limits = [50, 100, 200, 500]

        for limit in test_limits:
            count = solve_optimized(limit)
            assert count >= prev_count
            prev_count = count

    @pytest.mark.slow
    def test_performance_medium_range(self) -> None:
        """Test performance with medium range (slow test)."""
        # Test with a range that should complete reasonably quickly
        result = solve_optimized(10000)
        assert isinstance(result, int)
        assert result > 0

    def test_perimeter_boundary_cases(self) -> None:
        """Test perimeter boundary cases."""
        # Test exact boundary
        result_1000 = solve_optimized(1000)
        result_1001 = solve_optimized(1001)

        # Should be non-decreasing
        assert result_1001 >= result_1000

    @pytest.mark.slow
    def test_final_answer_verification(self) -> None:
        """Test the final answer for the actual problem (slow test)."""
        # This tests the actual problem: singular triangles with perimeter ≤ 1,500,000
        result = solve_optimized(1500000)
        assert result == 161667  # Expected answer


class TestMathematicalProperties:
    """Test mathematical properties and invariants."""

    def test_primitive_triple_coverage(self) -> None:
        """Test that primitive triples cover expected range."""
        triples = generate_primitive_pythagorean_triples(500)

        # Should have reasonable number of triples
        assert len(triples) >= 20

        # Check no duplicates
        triple_set = set(triples)
        assert len(triple_set) == len(triples)

    def test_scaling_property(self) -> None:
        """Test that scaling property works correctly."""
        # If (a,b,c) has perimeter P and forms 1 triangle,
        # then (2a,2b,2c) has perimeter 2P
        base_triangles = find_triangles_with_perimeter(12)
        assert len(base_triangles) == 1
        a, b, c = base_triangles[0]

        scaled_triangles = find_triangles_with_perimeter(24)
        # Should include (2a, 2b, 2c)
        scaled_expected = (2 * a, 2 * b, 2 * c)
        assert scaled_expected in scaled_triangles

    def test_perimeter_divisibility(self) -> None:
        """Test properties of perimeters that can form triangles."""
        counts = count_triangles_by_perimeter(100)

        # All perimeters should be even (property of Pythagorean triples)
        for perimeter in counts:
            assert perimeter % 2 == 0


if __name__ == "__main__":
    pytest.main([__file__])
