"""Tests for Problem 009: Special Pythagorean triplet."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_009 import (
    find_pythagorean_triplet,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem009:
    """Test cases for Problem 009."""

    @pytest.mark.parametrize(
        "target_sum,expected",
        [
            (12, 60),  # (3, 4, 5): 3+4+5=12, 3*4*5=60
            (30, 780),  # (5, 12, 13): 5+12+13=30, 5*12*13=780
            (24, 480),  # (6, 8, 10): 6+8+10=24, 6*8*10=480
            (36, 1620),  # (9, 12, 15): 9+12+15=36, 9*12*15=1620
            (60, 6240),  # (10, 24, 26): 10+24+26=60, 10*24*26=6240
        ],
    )
    def test_solve_naive(self, target_sum: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(target_sum)
        assert result == expected, (
            f"Expected {expected}, got {result} for sum {target_sum}"
        )

    @pytest.mark.parametrize(
        "target_sum,expected",
        [
            (12, 60),  # (3, 4, 5): 3+4+5=12, 3*4*5=60
            (30, 780),  # (5, 12, 13): 5+12+13=30, 5*12*13=780
            (24, 480),  # (6, 8, 10): 6+8+10=24, 6*8*10=480
            (36, 1620),  # (9, 12, 15): 9+12+15=36, 9*12*15=1620
            (60, 6240),  # (10, 24, 26): 10+24+26=60, 10*24*26=6240
        ],
    )
    def test_solve_optimized(self, target_sum: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(target_sum)
        assert result == expected, (
            f"Expected {expected}, got {result} for sum {target_sum}"
        )

    @pytest.mark.parametrize(
        "target_sum",
        [12, 24, 30, 36, 60, 84, 120],
    )
    def test_solve_mathematical(self, target_sum: int) -> None:
        """Test the mathematical solution returns valid results."""
        result = solve_mathematical(target_sum)

        # Verify that the result is valid by checking if it comes from a valid triplet
        assert result > 0, (
            f"Mathematical solution should return positive result for sum {target_sum}"
        )

        # Find the triplet that produces this result
        found_valid = False
        for a in range(1, target_sum // 3):
            for b in range(a + 1, (target_sum - a + 1) // 2):
                c = target_sum - a - b
                if b >= c:
                    continue
                if a * a + b * b == c * c and a * b * c == result:
                    found_valid = True
                    break
            if found_valid:
                break
        assert found_valid, (
            f"Mathematical result {result} is not valid for sum {target_sum}"
        )

    @pytest.mark.parametrize(
        "target_sum", [12, 24, 30, 36]
    )  # Test smaller values where algorithms agree
    def test_all_solutions_agree(self, target_sum: int) -> None:
        """Test that all solutions give the same result for small values."""
        naive_result = solve_naive(target_sum)
        optimized_result = solve_optimized(target_sum)
        math_result = solve_mathematical(target_sum)

        assert naive_result == optimized_result == math_result, (
            f"Solutions disagree for sum {target_sum}: "
            f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with minimum possible sum (3+4+5=12)
        assert solve_naive(12) == 60
        assert solve_optimized(12) == 60
        assert solve_mathematical(12) == 60

        # Test cases where no solution exists
        no_solution_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        for case in no_solution_cases:
            assert solve_naive(case) == 0
            assert solve_optimized(case) == 0
            assert solve_mathematical(case) == 0

    def test_invalid_input(self) -> None:
        """Test with invalid input."""
        # All solutions should raise ValueError for non-positive target_sum
        with pytest.raises(ValueError, match="target_sum must be positive"):
            solve_naive(0)
        with pytest.raises(ValueError, match="target_sum must be positive"):
            solve_optimized(0)
        with pytest.raises(ValueError, match="target_sum must be positive"):
            solve_mathematical(0)

        with pytest.raises(ValueError, match="target_sum must be positive"):
            solve_naive(-1)
        with pytest.raises(ValueError, match="target_sum must be positive"):
            solve_optimized(-1)
        with pytest.raises(ValueError, match="target_sum must be positive"):
            solve_mathematical(-1)

    @pytest.mark.slow
    def test_project_euler_answer(self) -> None:
        """Test with the actual Project Euler answer (marked as slow)."""
        target_sum = 1000
        expected = 31875000  # Known Project Euler answer

        # Test only mathematical solution for speed
        result_math = solve_mathematical(target_sum)
        assert result_math == expected

        # Verify the triplet exists and has correct properties
        triplet = find_pythagorean_triplet(target_sum)
        assert triplet is not None
        a, b, c = triplet

        # Verify Pythagorean theorem
        assert a * a + b * b == c * c

        # Verify sum
        assert a + b + c == target_sum

        # Verify ordering
        assert a < b < c

        # Verify product
        assert a * b * c == expected

    def test_find_pythagorean_triplet_helper(self) -> None:
        """Test the helper function for finding Pythagorean triplets."""
        # Test known cases
        triplet = find_pythagorean_triplet(12)
        assert triplet == (3, 4, 5)

        triplet = find_pythagorean_triplet(30)
        assert triplet == (5, 12, 13)

        triplet = find_pythagorean_triplet(24)
        assert triplet == (6, 8, 10)

        # Test case with no solution
        triplet = find_pythagorean_triplet(11)
        assert triplet is None

    def test_manual_calculation_verification(self) -> None:
        """Test manual calculation verification for small cases."""
        # Verify the classic 3-4-5 triangle
        assert 3 * 3 + 4 * 4 == 5 * 5  # 9 + 16 = 25
        assert 3 + 4 + 5 == 12
        assert 3 * 4 * 5 == 60

        # Verify the 5-12-13 triangle
        assert 5 * 5 + 12 * 12 == 13 * 13  # 25 + 144 = 169
        assert 5 + 12 + 13 == 30
        assert 5 * 12 * 13 == 780

        # Verify solutions for these cases
        assert solve_naive(12) == 60
        assert solve_naive(30) == 780

    def test_pythagorean_theorem_verification(self) -> None:
        """Test that found triplets actually satisfy Pythagorean theorem."""
        test_sums = [12, 24, 30, 36, 60, 84, 120]

        for target_sum in test_sums:
            triplet = find_pythagorean_triplet(target_sum)
            if triplet:
                a, b, c = triplet

                # Verify Pythagorean theorem
                assert a * a + b * b == c * c, (
                    f"Pythagorean theorem failed for ({a}, {b}, {c}): "
                    f"{a}² + {b}² = {a * a} + {b * b} = {a * a + b * b} ≠ {c * c} = {c}²"
                )

                # Verify sum
                assert a + b + c == target_sum, (
                    f"Sum failed for ({a}, {b}, {c}): "
                    f"{a} + {b} + {c} = {a + b + c} ≠ {target_sum}"
                )

                # Verify ordering
                assert a < b < c, (
                    f"Ordering failed for ({a}, {b}, {c}): Should have a < b < c"
                )

    def test_performance_comparison(self) -> None:
        """Test that all solutions work for moderate inputs."""
        # Simple functional test without timing overhead
        target_sum = 120

        # Verify all solutions work
        result_naive = solve_naive(target_sum)
        result_optimized = solve_optimized(target_sum)
        result_math = solve_mathematical(target_sum)

        # At least naive and optimized should give same result
        assert result_naive == result_optimized

        # All results should be positive for valid input
        assert result_naive > 0
        assert result_optimized > 0
        assert result_math > 0

    def test_mathematical_properties(self) -> None:
        """Test mathematical properties of Pythagorean triplets."""
        # Test that primitive Pythagorean triplets follow known patterns
        known_primitives = [
            (3, 4, 5),  # m=2, n=1
            (5, 12, 13),  # m=3, n=2
            (8, 15, 17),  # m=4, n=1
            (7, 24, 25),  # m=4, n=3
            (20, 21, 29),  # m=5, n=2
            (9, 40, 41),  # m=5, n=4
        ]

        for a, b, c in known_primitives:
            # Verify they are Pythagorean triplets
            assert a * a + b * b == c * c

            # Test if our algorithm can find valid triplets for these sums
            target_sum = a + b + c
            triplet = find_pythagorean_triplet(target_sum)
            if triplet:
                found_a, found_b, found_c = triplet
                # Verify the found triplet is valid (may not be exactly the same as expected)
                assert found_a * found_a + found_b * found_b == found_c * found_c
                assert found_a + found_b + found_c == target_sum
                assert found_a < found_b < found_c

    def test_scaling_properties(self) -> None:
        """Test that solutions handle scaled Pythagorean triplets correctly."""
        # Base triplet (3, 4, 5)
        base_a, base_b, base_c = 3, 4, 5
        base_sum = base_a + base_b + base_c  # 12
        base_product = base_a * base_b * base_c  # 60

        # Test specific scales where (3,4,5) is guaranteed to be the first solution
        test_scales = [1, 2, 3, 4]  # Exclude 5 as sum=60 has multiple solutions
        for scale in test_scales:
            scaled_sum = scale * base_sum
            expected_product = (scale**3) * base_product

            result = solve_optimized(scaled_sum)
            assert result == expected_product, (
                f"Scale {scale}: expected {expected_product}, got {result}"
            )

    def test_no_solution_cases(self) -> None:
        """Test cases where no Pythagorean triplet exists."""
        # Most small numbers don't have solutions
        no_solution_cases = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
        ]

        for case in no_solution_cases:
            assert solve_naive(case) == 0
            assert solve_optimized(case) == 0
            assert solve_mathematical(case) == 0
            assert find_pythagorean_triplet(case) is None

    def test_solution_uniqueness(self) -> None:
        """Test that the problem statement's claim of uniqueness holds for sum=1000."""
        # For sum=1000, there should be exactly one solution
        target_sum = 1000

        # Find all possible triplets (should be only one)
        solutions = []
        for a in range(1, target_sum // 3):
            for b in range(a + 1, (target_sum - a) // 2):
                c = target_sum - a - b
                if a * a + b * b == c * c:
                    solutions.append((a, b, c))

        # Should have exactly one solution
        assert len(solutions) == 1, (
            f"Expected 1 solution, found {len(solutions)}: {solutions}"
        )

    def test_input_validation_helper(self) -> None:
        """Test input validation for helper functions."""
        with pytest.raises(ValueError, match="target_sum must be positive"):
            find_pythagorean_triplet(0)
        with pytest.raises(ValueError, match="target_sum must be positive"):
            find_pythagorean_triplet(-1)

    def test_boundary_conditions(self) -> None:
        """Test boundary conditions for the algorithms."""
        # Test very small valid case
        assert solve_naive(12) == 60

        # Test moderately large case
        result_120 = solve_optimized(120)
        assert result_120 > 0

        # Verify the result for sum=120
        triplet_120 = find_pythagorean_triplet(120)
        if triplet_120:
            a, b, c = triplet_120
            assert a * b * c == result_120

    def test_algorithm_correctness(self) -> None:
        """Test algorithmic correctness with known mathematical results."""
        # Test a few more known cases beyond the basic ones
        test_cases = [
            (84, 15540),  # (12, 35, 37) - expected result from naive/optimized
            (156, 131820),  # (39, 52, 65) - expected result from naive/optimized
            (180, 118080),  # (18, 80, 82) - expected result from naive/optimized
        ]

        for target_sum, expected_product in test_cases:
            # Test that naive and optimized algorithms agree
            assert solve_naive(target_sum) == expected_product
            assert solve_optimized(target_sum) == expected_product

            # Test that mathematical algorithm returns a valid result (may be different)
            math_result = solve_mathematical(target_sum)
            assert math_result > 0

            # Verify the triplet from find_pythagorean_triplet
            triplet = find_pythagorean_triplet(target_sum)
            assert triplet is not None
            a, b, c = triplet
            assert a * b * c == expected_product
            assert a + b + c == target_sum
            assert a * a + b * b == c * c

    def test_euclid_formula_verification(self) -> None:
        """Test that our mathematical solution correctly implements Euclid's formula."""
        # Euclid's formula generates all primitive Pythagorean triplets
        # a = m² - n², b = 2mn, c = m² + n²
        # where m > n > 0, gcd(m,n) = 1, and exactly one of m,n is even

        # Test case: m=2, n=1 gives (3, 4, 5)
        # Sum = 3 + 4 + 5 = 12, Product = 60
        assert solve_mathematical(12) == 60

        # Test case: m=3, n=2 gives (5, 12, 13)
        # Sum = 5 + 12 + 13 = 30, Product = 780
        assert solve_mathematical(30) == 780

        # Test case: m=4, n=1 gives (15, 8, 17) -> sorted (8, 15, 17)
        # Sum = 8 + 15 + 17 = 40, Product = 2040
        assert solve_mathematical(40) == 2040

    def test_large_values_consistency(self) -> None:
        """Test that all algorithms find valid solutions for larger values."""
        # Test larger values to ensure algorithms remain accurate
        test_values = [84, 156, 180, 240, 360, 420]  # Values known to have solutions

        for target_sum in test_values:
            naive_result = solve_naive(target_sum)
            optimized_result = solve_optimized(target_sum)
            math_result = solve_mathematical(target_sum)

            # Verify that all algorithms find valid solutions (may not be the same)
            assert naive_result > 0, f"Naive algorithm failed for sum {target_sum}"
            assert optimized_result > 0, (
                f"Optimized algorithm failed for sum {target_sum}"
            )
            assert math_result > 0, (
                f"Mathematical algorithm failed for sum {target_sum}"
            )

            # Verify the solutions are actually correct by finding the triplets
            for result in [naive_result, optimized_result, math_result]:
                # Find the triplet that produces this result
                found_valid = False
                for a in range(1, target_sum // 3):
                    for b in range(a + 1, (target_sum - a + 1) // 2):
                        c = target_sum - a - b
                        if b >= c:
                            continue
                        if a * a + b * b == c * c and a * b * c == result:
                            found_valid = True
                            break
                    if found_valid:
                        break
                assert found_valid, (
                    f"Result {result} is not a valid product for sum {target_sum}"
                )
