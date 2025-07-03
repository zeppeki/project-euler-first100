#!/usr/bin/env python3
"""
Tests for Project Euler Problem 053: Combinatoric selections
"""

from collections.abc import Callable

import pytest

from problems.problem_053 import (
    analyze_combinatorial_values,
    combination_formula,
    combination_math_lib,
    combination_optimized,
    demonstrate_symmetry,
    factorial,
    find_first_exceeding_threshold,
    get_combinations_above_threshold,
    pascal_triangle_row,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestUtilityFunctions:
    """Test utility functions"""

    def test_factorial(self) -> None:
        """Test factorial function"""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
        assert factorial(10) == 3628800

        # Test error case
        with pytest.raises(ValueError):
            factorial(-1)

    def test_combination_formula(self) -> None:
        """Test combination calculation using factorial formula"""
        # Basic combinations
        assert combination_formula(5, 3) == 10
        assert combination_formula(10, 3) == 120
        assert combination_formula(23, 10) == 1144066

        # Edge cases
        assert combination_formula(5, 0) == 1
        assert combination_formula(5, 5) == 1
        assert combination_formula(5, 1) == 5

        # Invalid cases
        assert combination_formula(3, 5) == 0
        assert combination_formula(5, -1) == 0
        assert combination_formula(-1, 2) == 0

    def test_combination_optimized(self) -> None:
        """Test optimized combination calculation"""
        # Same results as formula method
        assert combination_optimized(5, 3) == 10
        assert combination_optimized(10, 3) == 120
        assert combination_optimized(23, 10) == 1144066

        # Edge cases
        assert combination_optimized(5, 0) == 1
        assert combination_optimized(5, 5) == 1
        assert combination_optimized(5, 1) == 5

        # Test symmetry C(n,r) = C(n,n-r)
        assert combination_optimized(10, 3) == combination_optimized(10, 7)
        assert combination_optimized(15, 5) == combination_optimized(15, 10)

        # Invalid cases
        assert combination_optimized(3, 5) == 0
        assert combination_optimized(5, -1) == 0
        assert combination_optimized(-1, 2) == 0

    def test_combination_math_lib(self) -> None:
        """Test math library combination function"""
        # Same results as other methods
        assert combination_math_lib(5, 3) == 10
        assert combination_math_lib(10, 3) == 120
        assert combination_math_lib(23, 10) == 1144066

        # Edge cases
        assert combination_math_lib(5, 0) == 1
        assert combination_math_lib(5, 5) == 1

        # Invalid cases
        assert combination_math_lib(3, 5) == 0
        assert combination_math_lib(5, -1) == 0
        assert combination_math_lib(-1, 2) == 0

    def test_combination_consistency(self) -> None:
        """Test that all combination methods give same results"""
        test_cases = [(0, 0), (1, 0), (1, 1), (5, 3), (10, 5), (15, 7), (20, 10)]

        for n, r in test_cases:
            formula_result = combination_formula(n, r)
            optimized_result = combination_optimized(n, r)
            math_lib_result = combination_math_lib(n, r)

            assert formula_result == optimized_result == math_lib_result, (
                f"Inconsistent results for C({n},{r}): "
                f"formula={formula_result}, optimized={optimized_result}, "
                f"math_lib={math_lib_result}"
            )


class TestSolutionFunctions:
    """Test main solution functions"""

    @pytest.mark.parametrize(
        "solver", [solve_naive, solve_optimized, solve_mathematical]
    )
    def test_solve_small_cases(self, solver: Callable[[int, int], int]) -> None:
        """Test solution functions with small test cases"""
        # Test case: no values > 1M for n ≤ 10
        result = solver(10, 1000000)
        assert result == 0

        # Test case: first threshold crossing at n=23
        result = solver(23, 1000000)
        assert result == 4  # C(23,10), C(23,11), C(23,12), C(23,13)

    def test_solve_consistency(self) -> None:
        """Test that all solution methods give the same result"""
        test_parameters = [(10, 1000000), (20, 1000000), (25, 1000000)]

        for max_n, threshold in test_parameters:
            results = [
                solve_naive(max_n, threshold),
                solve_optimized(max_n, threshold),
                solve_mathematical(max_n, threshold),
            ]

            # All methods should return the same result
            assert len(set(results)) == 1, (
                f"Inconsistent results for max_n={max_n}, threshold={threshold}: {results}"
            )

    @pytest.mark.slow
    def test_solve_main_problem(self) -> None:
        """Test the main problem (n ≤ 100, threshold = 1,000,000)"""
        # This test is marked as slow since it may take longer
        result_optimized = solve_optimized(100, 1000000)
        result_mathematical = solve_mathematical(100, 1000000)

        # Both optimized methods should agree
        assert result_optimized == result_mathematical
        assert result_optimized > 0  # Should find valid answers


class TestAnalysisFunctions:
    """Test analysis and utility functions"""

    def test_find_first_exceeding_threshold(self) -> None:
        """Test finding first combination exceeding threshold"""
        n, r, value = find_first_exceeding_threshold(1000000)

        # Should find C(23,10) = 1,144,066
        assert n == 23
        assert r == 10
        assert value == 1144066
        assert value > 1000000

    def test_get_combinations_above_threshold(self) -> None:
        """Test getting all combinations above threshold"""
        # Test with small range
        results = get_combinations_above_threshold(25, 1000000)

        # Should have multiple results
        assert len(results) > 0

        # All results should be above threshold
        for n, r, value in results:
            assert value > 1000000
            assert 1 <= n <= 25
            assert 0 <= r <= n

    def test_analyze_combinatorial_values(self) -> None:
        """Test combinatorial values analysis"""
        analysis = analyze_combinatorial_values(30)

        # Check structure
        assert "total_values" in analysis
        assert "max_value" in analysis
        assert "max_position" in analysis
        assert "threshold_count" in analysis

        # Check values
        assert analysis["total_values"] > 0
        assert analysis["max_value"] > 0
        assert analysis["threshold_count"] >= 0

    def test_pascal_triangle_row(self) -> None:
        """Test Pascal's triangle row generation"""
        # Test known rows
        assert pascal_triangle_row(0) == [1]
        assert pascal_triangle_row(1) == [1, 1]
        assert pascal_triangle_row(2) == [1, 2, 1]
        assert pascal_triangle_row(3) == [1, 3, 3, 1]
        assert pascal_triangle_row(4) == [1, 4, 6, 4, 1]
        assert pascal_triangle_row(5) == [1, 5, 10, 10, 5, 1]

        # Test empty case
        assert pascal_triangle_row(-1) == []

    def test_demonstrate_symmetry(self) -> None:
        """Test symmetry demonstration"""
        results = demonstrate_symmetry()

        # Should have results for n=0 to n=10
        assert len(results) == 11

        # Check structure
        for n, row in results:
            assert isinstance(n, int)
            assert isinstance(row, list)
            assert len(row) == n + 1

            # Check symmetry
            for i in range(len(row)):
                assert row[i] == row[-(i + 1)]


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_combination_symmetry(self) -> None:
        """Test combination symmetry property"""
        test_cases = [(5, 2), (10, 3), (15, 7), (20, 8)]

        for n, r in test_cases:
            assert combination_optimized(n, r) == combination_optimized(n, n - r)

    def test_large_combinations(self) -> None:
        """Test with larger combination values"""
        # Test some larger values that should work
        large_cases = [(50, 25), (60, 30), (70, 35)]

        for n, r in large_cases:
            result = combination_optimized(n, r)
            assert result > 0
            assert result == combination_math_lib(n, r)

    def test_threshold_boundary(self) -> None:
        """Test values around the threshold boundary"""
        threshold = 1000000

        # Test known boundary cases
        assert combination_optimized(22, 10) < threshold  # Should be under
        assert combination_optimized(23, 10) > threshold  # Should be over

        # Test symmetry at boundary
        assert combination_optimized(23, 10) == combination_optimized(23, 13)

    def test_performance_bounds(self) -> None:
        """Test that calculations complete within reasonable bounds"""
        # Test that we can calculate the main problem efficiently
        result = solve_optimized(100, 1000000)
        assert isinstance(result, int)
        assert result > 0


class TestMathematicalProperties:
    """Test mathematical properties of combinations"""

    def test_pascals_identity(self) -> None:
        """Test Pascal's identity: C(n,r) = C(n-1,r-1) + C(n-1,r)"""
        test_cases = [(5, 2), (10, 5), (15, 7)]

        for n, r in test_cases:
            if n > 0 and r > 0:
                left = combination_optimized(n, r)
                right = combination_optimized(n - 1, r - 1) + combination_optimized(
                    n - 1, r
                )
                assert left == right

    def test_combination_bounds(self) -> None:
        """Test combination bounds and properties"""
        n = 10

        # C(n,0) = C(n,n) = 1
        assert combination_optimized(n, 0) == 1
        assert combination_optimized(n, n) == 1

        # C(n,1) = C(n,n-1) = n
        assert combination_optimized(n, 1) == n
        assert combination_optimized(n, n - 1) == n

        # Maximum is at middle
        max_value = max(combination_optimized(n, r) for r in range(n + 1))
        middle_r = n // 2
        assert combination_optimized(n, middle_r) == max_value


if __name__ == "__main__":
    pytest.main([__file__])
