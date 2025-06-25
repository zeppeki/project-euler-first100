"""Tests for Problem 015: Lattice paths."""

import math
import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_015 import (
    solve_mathematical,
    solve_mathematical_factorial,
    solve_naive,
    solve_optimized,
)


class TestProblem015:
    """Test cases for Problem 015."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 1),  # 0×0 grid: 1 path (no movement)
            (1, 2),  # 1×1 grid: 2 paths (right-down or down-right)
            (2, 6),  # 2×2 grid: 6 paths (problem example)
            (3, 20),  # 3×3 grid: 20 paths
            (4, 70),  # 4×4 grid: 70 paths
            (5, 252),  # 5×5 grid: 252 paths
            (6, 924),  # 6×6 grid: 924 paths
            (7, 3432),  # 7×7 grid: 3432 paths
            (8, 12870),  # 8×8 grid: 12870 paths
            (9, 48620),  # 9×9 grid: 48620 paths
            (10, 184756),  # 10×10 grid: 184756 paths
        ],
    )
    def test_solve_naive(self, n: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 1),  # 0×0 grid: 1 path (no movement)
            (1, 2),  # 1×1 grid: 2 paths (right-down or down-right)
            (2, 6),  # 2×2 grid: 6 paths (problem example)
            (3, 20),  # 3×3 grid: 20 paths
            (4, 70),  # 4×4 grid: 70 paths
            (5, 252),  # 5×5 grid: 252 paths
            (6, 924),  # 6×6 grid: 924 paths
            (7, 3432),  # 7×7 grid: 3432 paths
            (8, 12870),  # 8×8 grid: 12870 paths
            (9, 48620),  # 9×9 grid: 48620 paths
            (10, 184756),  # 10×10 grid: 184756 paths
        ],
    )
    def test_solve_optimized(self, n: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 1),  # 0×0 grid: 1 path (no movement)
            (1, 2),  # 1×1 grid: 2 paths (right-down or down-right)
            (2, 6),  # 2×2 grid: 6 paths (problem example)
            (3, 20),  # 3×3 grid: 20 paths
            (4, 70),  # 4×4 grid: 70 paths
            (5, 252),  # 5×5 grid: 252 paths
            (6, 924),  # 6×6 grid: 924 paths
            (7, 3432),  # 7×7 grid: 3432 paths
            (8, 12870),  # 8×8 grid: 12870 paths
            (9, 48620),  # 9×9 grid: 48620 paths
            (10, 184756),  # 10×10 grid: 184756 paths
        ],
    )
    def test_solve_mathematical(self, n: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, 1),  # 0×0 grid: 1 path (no movement)
            (1, 2),  # 1×1 grid: 2 paths (right-down or down-right)
            (2, 6),  # 2×2 grid: 6 paths (problem example)
            (3, 20),  # 3×3 grid: 20 paths
            (4, 70),  # 4×4 grid: 70 paths
            (5, 252),  # 5×5 grid: 252 paths
            (6, 924),  # 6×6 grid: 924 paths
            (7, 3432),  # 7×7 grid: 3432 paths
            (8, 12870),  # 8×8 grid: 12870 paths
            (9, 48620),  # 9×9 grid: 48620 paths
            (10, 184756),  # 10×10 grid: 184756 paths
        ],
    )
    def test_solve_mathematical_factorial(self, n: int, expected: int) -> None:
        """Test the mathematical factorial solution."""
        result = solve_mathematical_factorial(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize("n", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_all_solutions_agree(self, n: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(n)
        optimized_result = solve_optimized(n)
        math_result = solve_mathematical(n)
        factorial_result = solve_mathematical_factorial(n)

        assert naive_result == optimized_result == math_result == factorial_result, (
            f"Solutions disagree for n={n}: "
            f"naive={naive_result}, optimized={optimized_result}, "
            f"math={math_result}, factorial={factorial_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with n = 0 (no movement)
        assert solve_naive(0) == 1
        assert solve_optimized(0) == 1
        assert solve_mathematical(0) == 1
        assert solve_mathematical_factorial(0) == 1

        # Test with n = 1 (1×1 grid)
        assert solve_naive(1) == 2
        assert solve_optimized(1) == 2
        assert solve_mathematical(1) == 2
        assert solve_mathematical_factorial(1) == 2

        # Test with n = 2 (problem example)
        assert solve_naive(2) == 6
        assert solve_optimized(2) == 6
        assert solve_mathematical(2) == 6
        assert solve_mathematical_factorial(2) == 6

    def test_invalid_input(self) -> None:
        """Test with invalid input."""
        # All solutions should raise ValueError for negative n
        with pytest.raises(ValueError):
            solve_naive(-1)
        with pytest.raises(ValueError):
            solve_optimized(-1)
        with pytest.raises(ValueError):
            solve_mathematical(-1)
        with pytest.raises(ValueError):
            solve_mathematical_factorial(-1)

    @pytest.mark.slow
    def test_large_number(self) -> None:
        """Test with the actual problem number (marked as slow)."""
        # Test with the actual problem limit using fastest algorithm only
        n = 20
        expected = 137846528820  # Known Project Euler answer for 20×20 grid

        # Test only mathematical solution for speed
        result_math = solve_mathematical(n)
        assert result_math == expected

        # Test factorial solution as well
        result_factorial = solve_mathematical_factorial(n)
        assert result_factorial == expected

    def test_combinatorics_formula(self) -> None:
        """Test that the combinatorics formula C(2n, n) is correct."""
        # For n×n grid, the number of paths is C(2n, n) = (2n)! / (n! * n!)
        test_cases = [
            (0, 1),
            (1, 2),
            (2, 6),
            (3, 20),
            (4, 70),
            (5, 252),
        ]

        for n, expected in test_cases:
            # Direct calculation using math.comb
            if hasattr(math, "comb"):  # Python 3.8+
                result_comb = math.comb(2 * n, n)
                assert result_comb == expected, f"math.comb failed for n={n}"

            # Manual calculation
            if n == 0:
                manual_result = 1
            else:
                manual_result = math.factorial(2 * n) // (
                    math.factorial(n) * math.factorial(n)
                )
            assert manual_result == expected, f"Manual calculation failed for n={n}"

    def test_problem_example_verification(self) -> None:
        """Test the specific Project Euler example."""
        # From the problem statement:
        # 2×2 grid has exactly 6 routes
        n = 2
        expected = 6

        # Test all our solutions
        assert solve_naive(n) == expected
        assert solve_optimized(n) == expected
        assert solve_mathematical(n) == expected
        assert solve_mathematical_factorial(n) == expected

        # Verify the paths manually for 2×2 grid:
        # Paths: RRDD, RDRD, RDDR, DRRD, DRDR, DDRR
        # Where R = right, D = down
        # This gives us 6 paths total

    def test_grid_path_properties(self) -> None:
        """Test mathematical properties of grid paths."""
        # Test that paths are monotonically increasing
        for n in range(1, 10):
            current_paths = solve_mathematical(n)
            next_paths = solve_mathematical(n + 1)
            assert current_paths < next_paths, (
                f"Paths should increase: {n}×{n} has {current_paths}, "
                f"{n + 1}×{n + 1} has {next_paths}"
            )

        # Test symmetry: paths from (0,0) to (n,n) equals paths from (n,n) to (0,0)
        # This is automatically satisfied by our formula, but let's verify
        for n in range(1, 8):
            paths = solve_mathematical(n)
            # The mathematical formula is symmetric, so this should always be true
            assert paths > 0, f"Should have positive paths for n={n}"

    def test_small_grid_manual_verification(self) -> None:
        """Manually verify small grids by counting paths."""
        # 1×1 grid: R-D, D-R → 2 paths
        assert solve_mathematical(1) == 2

        # 2×2 grid: RRDD, RDRD, RDDR, DRRD, DRDR, DDRR → 6 paths
        assert solve_mathematical(2) == 6

        # 3×3 grid: Choose 3 positions out of 6 for R moves → C(6,3) = 20
        assert solve_mathematical(3) == 20

    def test_dynamic_programming_correctness(self) -> None:
        """Test that the DP approach builds the grid correctly."""
        # For a 3×3 grid, manually verify the DP table
        # The DP table should look like:
        # 1  1  1  1
        # 1  2  3  4
        # 1  3  6  10
        # 1  4  10 20

        # Test some intermediate calculations
        n = 3
        result = solve_naive(n)
        assert result == 20

        # Test that the optimized DP gives the same result
        result_opt = solve_optimized(n)
        assert result_opt == 20

    def test_mathematical_efficiency(self) -> None:
        """Test that mathematical solutions are efficient for larger inputs."""
        # Test moderately large inputs
        test_values = [11, 12, 13, 14, 15]

        for n in test_values:
            # Mathematical solutions should work efficiently
            result_math = solve_mathematical(n)
            result_factorial = solve_mathematical_factorial(n)

            # Both should agree
            assert result_math == result_factorial, (
                f"Mathematical solutions disagree for n={n}: "
                f"efficient={result_math}, factorial={result_factorial}"
            )

            # Result should be positive
            assert result_math > 0, f"Should have positive result for n={n}"

    def test_overflow_protection(self) -> None:
        """Test that solutions handle large numbers correctly."""
        # Test with n=15 (fairly large but manageable)
        n = 15

        # All solutions should work without overflow
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)
        result_factorial = solve_mathematical_factorial(n)

        # All should agree
        assert result_naive == result_optimized == result_math == result_factorial

        # Result should be reasonable (C(30, 15) = 155,117,520)
        expected_15 = 155117520
        assert result_math == expected_15

    def test_performance_comparison(self) -> None:
        """Test that all solutions work for moderate inputs."""
        # Simple functional test without timing overhead
        n = 12

        # Verify all solutions work
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)
        result_factorial = solve_mathematical_factorial(n)

        # All should give same result
        assert result_naive == result_optimized == result_math == result_factorial

        # Should be C(24, 12) = 2,704,156
        expected_12 = 2704156
        assert result_math == expected_12

    def test_binomial_coefficient_properties(self) -> None:
        """Test properties of binomial coefficients."""
        # Test that C(2n, n) is always even for n > 0
        for n in range(1, 10):
            result = solve_mathematical(n)
            assert result % 2 == 0, f"C(2×{n}, {n}) should be even"

        # Test Pascal's triangle property: C(n,k) = C(n-1,k-1) + C(n-1,k)
        # For our case: C(2n, n) relates to smaller binomial coefficients
        # This is more complex to verify directly, but we can check some relationships

        # Test that C(2n, n) > C(2n-2, n-1) for n > 0
        for n in range(2, 8):
            current = solve_mathematical(n)
            previous = solve_mathematical(n - 1)
            assert current > previous, (
                f"C(2×{n}, {n}) should be greater than C(2×{n - 1}, {n - 1})"
            )

    def test_project_euler_final_answer(self) -> None:
        """Test the final Project Euler answer."""
        # The problem asks for paths through a 20×20 grid
        n = 20
        expected = 137846528820  # Known Project Euler answer

        # Test with mathematical solution (most efficient)
        result = solve_mathematical(n)
        assert result == expected, f"Expected {expected}, got {result}"

        # Verify with factorial solution as well
        result_factorial = solve_mathematical_factorial(n)
        assert result_factorial == expected, (
            f"Factorial method: expected {expected}, got {result_factorial}"
        )

    def test_mathematical_formula_verification(self) -> None:
        """Verify the mathematical formula step by step."""
        # For n=4, verify C(8,4) = 8!/(4!×4!) = 70
        n = 4

        # Step by step calculation
        numerator = 8 * 7 * 6 * 5  # 8×7×6×5
        denominator = 4 * 3 * 2 * 1  # 4!
        expected = numerator // denominator  # 70

        assert expected == 70
        assert solve_mathematical(n) == expected

        # Verify the efficient calculation matches
        # solve_mathematical uses: result = result * (2*n - i) // (i + 1)
        # For n=4:
        # i=0: result = 1 * 8 // 1 = 8
        # i=1: result = 8 * 7 // 2 = 28
        # i=2: result = 28 * 6 // 3 = 56
        # i=3: result = 56 * 5 // 4 = 70

        manual_result = 1
        for i in range(n):
            manual_result = manual_result * (2 * n - i) // (i + 1)

        assert manual_result == 70
        assert manual_result == solve_mathematical(n)

    def test_algorithm_specific_optimizations(self) -> None:
        """Test algorithm-specific optimizations."""
        # Test that the space-optimized DP uses O(n) space instead of O(n²)
        # This is more of a structural test - we verify it works correctly
        n = 6

        result_naive = solve_naive(n)  # Uses O(n²) space
        result_optimized = solve_optimized(n)  # Uses O(n) space

        assert result_naive == result_optimized

        # Test that mathematical approach avoids DP entirely
        result_math = solve_mathematical(n)
        assert result_math == result_naive

    def test_zero_grid_edge_case(self) -> None:
        """Test the special case of 0×0 grid."""
        # A 0×0 grid has exactly 1 path (the empty path)
        n = 0
        expected = 1

        assert solve_naive(n) == expected
        assert solve_optimized(n) == expected
        assert solve_mathematical(n) == expected
        assert solve_mathematical_factorial(n) == expected

        # Verify this makes sense mathematically: C(0, 0) = 1
        assert math.factorial(0) == 1  # 0! = 1
        if hasattr(math, "comb"):
            assert math.comb(0, 0) == 1
