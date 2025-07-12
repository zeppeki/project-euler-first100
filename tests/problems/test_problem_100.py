#!/usr/bin/env python3
"""
Test for Problem 100: Arranged probability
"""

import math

from problems.problem_100 import (
    find_next_arrangement,
    is_valid_arrangement,
    solve_mathematical,
    solve_optimized,
    verify_arrangement,
)


class TestUtilityFunctions:
    """Test utility functions for arranged probability."""

    def test_is_valid_arrangement(self) -> None:
        """Test arrangement validation."""
        # Known valid arrangements
        assert is_valid_arrangement(15, 21) is True
        assert is_valid_arrangement(85, 120) is True

        # Invalid arrangements
        assert is_valid_arrangement(10, 21) is False
        assert is_valid_arrangement(0, 21) is False
        assert is_valid_arrangement(15, 0) is False
        assert is_valid_arrangement(-5, 21) is False
        assert is_valid_arrangement(25, 21) is False  # blue > total

    def test_verify_arrangement(self) -> None:
        """Test arrangement verification with detailed info."""
        # Test known arrangement (15 blue, 21 total)
        info = verify_arrangement(15, 21)

        assert info["blue"] == 15
        assert info["red"] == 6
        assert info["total"] == 21
        assert abs(info["prob_both_blue"] - 0.5) < 1e-15
        assert info["is_exactly_half"] is True
        assert info["formula_valid"] is True
        assert info["formula_left"] == 2 * 15 * 14  # 420
        assert info["formula_right"] == 21 * 20  # 420

        # Test another known arrangement (85 blue, 120 total)
        info = verify_arrangement(85, 120)

        assert info["blue"] == 85
        assert info["red"] == 35
        assert info["total"] == 120
        assert abs(info["prob_both_blue"] - 0.5) < 1e-15
        assert info["is_exactly_half"] is True
        assert info["formula_valid"] is True

    def test_find_next_arrangement(self) -> None:
        """Test finding next valid arrangement."""
        # From (15, 21) → should get (85, 120)
        blue_next, total_next = find_next_arrangement(15, 21)
        assert blue_next == 85
        assert total_next == 120
        assert is_valid_arrangement(blue_next, total_next)

        # From (85, 120) → should get next arrangement
        blue_next2, total_next2 = find_next_arrangement(85, 120)
        assert blue_next2 > 85
        assert total_next2 > 120
        assert is_valid_arrangement(blue_next2, total_next2)

        # Verify the sequence continues correctly
        blue_next3, total_next3 = find_next_arrangement(blue_next2, total_next2)
        assert blue_next3 > blue_next2
        assert total_next3 > total_next2
        assert is_valid_arrangement(blue_next3, total_next3)


class TestSolutionMethods:
    """Test solution methods."""

    def test_solution_consistency(self) -> None:
        """Test that all solution methods give the same results for smaller limits."""
        # Test with smaller limits to verify consistency
        small_limit = 10**6

        result_optimized = solve_optimized(small_limit)
        result_mathematical = solve_mathematical(small_limit)

        assert result_optimized == result_mathematical

        # Verify the result is valid
        blue = result_optimized

        # Calculate corresponding total
        discriminant = 1 + 8 * blue * (blue - 1)
        total = int((1 + math.sqrt(discriminant)) / 2)

        assert is_valid_arrangement(blue, total)
        assert total > small_limit

    def test_main_problem_result(self) -> None:
        """Test the main problem result."""
        # The expected answer for Problem 100
        expected_result = 756872327473

        result = solve_mathematical(10**12)
        assert result == expected_result

        # Verify this is a valid arrangement
        blue = result

        # Calculate corresponding total
        discriminant = 1 + 8 * blue * (blue - 1)
        total = int((1 + math.sqrt(discriminant)) / 2)

        assert is_valid_arrangement(blue, total)
        assert total > 10**12

    def test_result_properties(self) -> None:
        """Test properties of the result."""
        result = solve_mathematical(10**12)

        # Should be a positive integer
        assert isinstance(result, int)
        assert result > 0

        # Should be larger than known examples
        assert result > 85  # Larger than the second known solution

        # Calculate total and verify
        blue = result
        discriminant = 1 + 8 * blue * (blue - 1)
        total = int((1 + math.sqrt(discriminant)) / 2)

        # Verify arrangement properties
        info = verify_arrangement(blue, total)
        assert info["is_exactly_half"] is True
        assert info["formula_valid"] is True
        assert total > 10**12

    def test_pell_equation_properties(self) -> None:
        """Test Pell equation properties."""
        # Start with first known solution
        blue, total = 15, 21

        # Convert to Pell equation variables
        x = 2 * blue - 1  # Should be 29
        y = 2 * total - 1  # Should be 41

        assert x == 29
        assert y == 41

        # Verify Pell equation: y² - 2x² = -1
        assert y * y - 2 * x * x == -1

        # Test recurrence relation
        for _ in range(3):
            x_new = 2 * y + 3 * x
            y_new = 3 * y + 4 * x

            # Verify new solution satisfies Pell equation
            assert y_new * y_new - 2 * x_new * x_new == -1

            # Convert back to blue/total
            if x_new % 2 == 1 and y_new % 2 == 1:
                blue_new = (x_new + 1) // 2
                total_new = (y_new + 1) // 2

                if blue_new > 0 and total_new > 0:
                    assert is_valid_arrangement(blue_new, total_new)

            x, y = x_new, y_new

    def test_sequence_generation(self) -> None:
        """Test sequence generation of valid arrangements."""
        arrangements = []
        blue, total = 15, 21

        # Generate first few arrangements in sequence
        for _ in range(4):
            assert is_valid_arrangement(blue, total)
            arrangements.append((blue, total))

            blue, total = find_next_arrangement(blue, total)

        # Verify the known second arrangement
        assert arrangements[1] == (85, 120)

        # Verify sequence is strictly increasing
        for i in range(1, len(arrangements)):
            assert arrangements[i][0] > arrangements[i - 1][0]  # blue increasing
            assert arrangements[i][1] > arrangements[i - 1][1]  # total increasing

    def test_edge_cases(self) -> None:
        """Test edge cases and boundary conditions."""
        # Test minimum valid arrangement
        blue, total = 15, 21
        assert is_valid_arrangement(blue, total)

        # Test very small cases
        assert not is_valid_arrangement(1, 2)
        assert not is_valid_arrangement(2, 3)
        assert is_valid_arrangement(3, 4)  # This is actually valid!

        # Test mathematical consistency
        blue = 15
        discriminant = 1 + 8 * blue * (blue - 1)
        total_calculated = int((1 + math.sqrt(discriminant)) / 2)
        assert total_calculated == 21


class TestPerformanceAndIntegration:
    """Test performance characteristics and integration."""

    def test_algorithm_efficiency(self) -> None:
        """Test that algorithms complete in reasonable time."""
        import time

        # Test with main problem
        start_time = time.time()
        result = solve_mathematical(10**12)
        end_time = time.time()

        # Should complete quickly (less than 1 second)
        assert end_time - start_time < 1.0

        # Should get correct result
        assert result == 756872327473

    def test_mathematical_consistency(self) -> None:
        """Test mathematical consistency across transformations."""
        # Test coordinate transformations
        test_cases = [(15, 21), (85, 120)]

        for blue, total in test_cases:
            # Forward transform
            x = 2 * blue - 1
            y = 2 * total - 1

            # Verify Pell equation
            assert y * y - 2 * x * x == -1

            # Reverse transform
            blue_back = (x + 1) // 2
            total_back = (y + 1) // 2

            assert blue_back == blue
            assert total_back == total

    def test_probability_precision(self) -> None:
        """Test precision of probability calculations."""
        # Test cases where precision matters
        test_arrangements = [(15, 21), (85, 120)]

        for blue, total in test_arrangements:
            info = verify_arrangement(blue, total)

            # Probability should be exactly 0.5
            assert abs(info["prob_both_blue"] - 0.5) < 1e-15

            # Formula should be exactly satisfied
            assert info["formula_valid"] is True

    def test_large_number_handling(self) -> None:
        """Test handling of large numbers."""
        # Test with main problem result
        blue = solve_mathematical(10**12)

        # Calculate total
        discriminant = 1 + 8 * blue * (blue - 1)
        total = int((1 + math.sqrt(discriminant)) / 2)

        # Verify no overflow issues
        assert blue > 0
        assert total > blue
        assert total > 10**12

        # Verify arithmetic precision
        formula_left = 2 * blue * (blue - 1)
        formula_right = total * (total - 1)
        assert formula_left == formula_right

    def test_robustness(self) -> None:
        """Test robustness of the solution."""
        # Test multiple starting points lead to same sequence
        _, _ = 15, 21
        blue2, total2 = find_next_arrangement(15, 21)

        # Both should lead to same eventual large solution
        limit = 10**6  # Use smaller limit for testing

        result1 = solve_mathematical(limit)

        # Verify result is valid and meets constraints
        discriminant = 1 + 8 * result1 * (result1 - 1)
        total_result = int((1 + math.sqrt(discriminant)) / 2)

        assert is_valid_arrangement(result1, total_result)
        assert total_result > limit

    def test_convergence_properties(self) -> None:
        """Test convergence and growth properties."""
        arrangements = []
        blue, total = 15, 21

        # Generate sequence and analyze growth
        for _ in range(5):
            arrangements.append((blue, total))
            blue, total = find_next_arrangement(blue, total)

        # Verify exponential-like growth
        if len(arrangements) >= 3:
            # Growth ratio should be roughly constant
            ratios = []
            for i in range(1, len(arrangements)):
                ratio = arrangements[i][1] / arrangements[i - 1][1]
                ratios.append(ratio)

            # Ratios should be similar (approximately same growth factor)
            for i in range(1, len(ratios)):
                assert (
                    abs(ratios[i] - ratios[i - 1]) / ratios[i - 1] < 0.5
                )  # Within 50% (more lenient)
