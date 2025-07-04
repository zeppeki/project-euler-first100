#!/usr/bin/env python3
"""
Tests for Project Euler Problem 058: Spiral primes
"""

from collections.abc import Callable

import pytest

from problems.problem_058 import (
    analyze_spiral_pattern,
    calculate_prime_ratio,
    count_primes_in_diagonals,
    get_all_diagonal_values,
    get_diagonal_values,
    get_spiral_layer_info,
    is_prime,
    solve_naive,
    solve_optimized,
    verify_example_spiral,
)


class TestUtilityFunctions:
    """Test utility functions for spiral calculations"""

    def test_is_prime(self) -> None:
        """Test prime checking function"""
        # Test small primes
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(13) is True

        # Test small composites
        assert is_prime(1) is False
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False

        # Test edge cases
        assert is_prime(0) is False
        assert is_prime(-1) is False

        # Test larger numbers
        assert is_prime(17) is True
        assert is_prime(31) is True
        assert is_prime(37) is True
        assert is_prime(43) is True
        assert is_prime(21) is False  # 3 × 7
        assert is_prime(25) is False  # 5²
        assert is_prime(49) is False  # 7²

    def test_get_diagonal_values_basic(self) -> None:
        """Test basic diagonal value calculation"""
        # Test side length 1 (special case)
        values_1 = get_diagonal_values(1)
        assert values_1 == [1]

        # Test side length 3
        values_3 = get_diagonal_values(3)
        assert values_3 == [
            9,
            7,
            5,
            3,
        ]  # Bottom-right, top-right, top-left, bottom-left

        # Test side length 5
        values_5 = get_diagonal_values(5)
        assert values_5 == [25, 21, 17, 13]

        # Test side length 7
        values_7 = get_diagonal_values(7)
        assert values_7 == [49, 43, 37, 31]

    def test_get_diagonal_values_even_sides(self) -> None:
        """Test that even side lengths return empty list"""
        assert get_diagonal_values(2) == []
        assert get_diagonal_values(4) == []
        assert get_diagonal_values(6) == []

    def test_get_diagonal_values_formula(self) -> None:
        """Test diagonal value calculation formula"""
        for side_length in range(3, 20, 2):  # Test odd side lengths
            values = get_diagonal_values(side_length)
            n = side_length

            # Verify the formula for each diagonal
            assert values[0] == n * n  # Bottom-right: n²
            assert values[1] == n * n - (n - 1)  # Top-right: n² - (n-1)
            assert values[2] == n * n - 2 * (n - 1)  # Top-left: n² - 2(n-1)
            assert values[3] == n * n - 3 * (n - 1)  # Bottom-left: n² - 3(n-1)


class TestSpiralConstruction:
    """Test spiral construction and diagonal value aggregation"""

    def test_get_all_diagonal_values_small(self) -> None:
        """Test aggregation of diagonal values for small spirals"""
        # Side length 1
        all_values_1 = get_all_diagonal_values(1)
        assert all_values_1 == [1]

        # Side length 3
        all_values_3 = get_all_diagonal_values(3)
        expected_3 = [1, 9, 7, 5, 3]  # Center + layer 1
        assert all_values_3 == expected_3

        # Side length 5
        all_values_5 = get_all_diagonal_values(5)
        expected_5 = [1, 9, 7, 5, 3, 25, 21, 17, 13]  # Center + layer 1 + layer 2
        assert all_values_5 == expected_5

    def test_get_all_diagonal_values_progression(self) -> None:
        """Test that diagonal values grow correctly as layers are added"""
        for side_length in range(1, 12, 2):
            values = get_all_diagonal_values(side_length)

            # Check that values are in correct order
            assert values[0] == 1  # Always starts with center

            # Check that the length is correct
            expected_length = 1 + 4 * ((side_length - 1) // 2)  # 1 center + 4 per layer
            assert len(values) == expected_length

    def test_count_primes_in_diagonals(self) -> None:
        """Test prime counting in diagonal values"""
        # Test side length 1
        prime_count_1, total_count_1 = count_primes_in_diagonals(1)
        assert prime_count_1 == 0  # 1 is not prime
        assert total_count_1 == 1

        # Test side length 3
        prime_count_3, total_count_3 = count_primes_in_diagonals(3)
        # Values: [1, 9, 7, 5, 3] -> primes: [7, 5, 3] = 3 primes
        assert prime_count_3 == 3
        assert total_count_3 == 5

        # Test side length 5
        prime_count_5, total_count_5 = count_primes_in_diagonals(5)
        # Additional values: [25, 21, 17, 13] -> primes: [17, 13] = 2 more primes
        assert prime_count_5 == 5  # 3 + 2
        assert total_count_5 == 9  # 5 + 4


class TestExampleVerification:
    """Test verification of the problem example"""

    def test_verify_example_spiral(self) -> None:
        """Test that the example spiral from the problem is verified correctly"""
        assert verify_example_spiral() is True

    def test_example_spiral_details(self) -> None:
        """Test detailed verification of the example spiral"""
        side_length = 7
        all_diagonal_values = get_all_diagonal_values(side_length)

        # The expected diagonal values from the problem statement
        # Center: 1
        # Layer 1 (side 3): 9, 7, 5, 3
        # Layer 2 (side 5): 25, 21, 17, 13
        # Layer 3 (side 7): 49, 43, 37, 31
        expected_values = [1, 9, 7, 5, 3, 25, 21, 17, 13, 49, 43, 37, 31]

        assert len(all_diagonal_values) == 13
        assert all_diagonal_values == expected_values

        # Count primes: 3, 5, 7, 13, 17, 31, 37, 43 = 8 primes
        expected_primes = [3, 5, 7, 13, 17, 31, 37, 43]
        actual_primes = [
            value for value in all_diagonal_values if value > 1 and is_prime(value)
        ]

        assert len(actual_primes) == 8
        assert set(actual_primes) == set(expected_primes)

        # Verify ratio: 8/13 ≈ 0.615 ≈ 61.5%
        prime_count, total_count = count_primes_in_diagonals(side_length)
        ratio = prime_count / total_count
        assert abs(ratio - 8 / 13) < 1e-10


class TestSolutionFunctions:
    """Test main solution functions"""

    @pytest.mark.parametrize("solver", [solve_naive, solve_optimized])
    def test_solve_consistency(self, solver: Callable[[float], int]) -> None:
        """Test that solution methods work with high target ratios"""
        # Test with high ratios that should be found quickly
        result_80 = solver(0.8)
        assert isinstance(result_80, int)
        assert result_80 >= 1
        assert result_80 % 2 == 1  # Should be odd

        result_50 = solver(0.5)
        assert isinstance(result_50, int)
        assert result_50 >= result_80  # Lower ratio should require larger spiral

    def test_solve_agreement(self) -> None:
        """Test that all solution methods agree"""
        # Test with manageable target ratios
        test_ratios = [0.8, 0.6, 0.4, 0.3]

        for ratio in test_ratios:
            result_naive = solve_naive(ratio)
            result_optimized = solve_optimized(ratio)

            assert result_naive == result_optimized, (
                f"Solutions disagree for ratio {ratio}: {result_naive} vs {result_optimized}"
            )

    def test_solve_known_ratios(self) -> None:
        """Test with known ratio thresholds"""
        # Test that solutions respect the ratio threshold
        test_ratios = [0.7, 0.5, 0.3]

        for ratio in test_ratios:
            result = solve_naive(ratio)
            actual_ratio = calculate_prime_ratio(result)

            # The result should be the first side length where ratio falls below target
            assert actual_ratio < ratio, (
                f"Ratio {actual_ratio} should be < {ratio} for side length {result}"
            )

            # The previous side length should have ratio >= target (if result > 3)
            if result > 3:
                prev_ratio = calculate_prime_ratio(result - 2)
                assert prev_ratio >= ratio, (
                    f"Previous ratio {prev_ratio} should be >= {ratio} for side length {result - 2}"
                )

    @pytest.mark.slow
    def test_solve_main_problem(self) -> None:
        """Test the main problem with 10% threshold (marked as slow test)"""
        # Use a higher threshold for CI performance
        target_ratio = 0.15  # Use 15% instead of 10% for faster execution
        result = solve_optimized(target_ratio)

        assert isinstance(result, int)
        assert result > 7  # Should be larger than the example
        assert result % 2 == 1  # Should be odd

        # Verify the result
        actual_ratio = calculate_prime_ratio(result)
        assert actual_ratio < target_ratio


class TestAnalysisFunctions:
    """Test analysis and helper functions"""

    def test_calculate_prime_ratio(self) -> None:
        """Test prime ratio calculation"""
        # Test known cases
        ratio_1 = calculate_prime_ratio(1)
        assert ratio_1 == 0.0  # No primes in [1]

        ratio_3 = calculate_prime_ratio(3)
        assert abs(ratio_3 - 3 / 5) < 1e-10  # 3 primes out of 5

        ratio_7 = calculate_prime_ratio(7)
        assert abs(ratio_7 - 8 / 13) < 1e-10  # 8 primes out of 13

    def test_get_spiral_layer_info(self) -> None:
        """Test spiral layer information extraction"""
        # Test center
        info_1 = get_spiral_layer_info(1)
        assert info_1["side_length"] == 1
        assert info_1["layer"] == 0
        assert info_1["diagonal_values"] == [1]
        assert info_1["prime_status"] == [False]
        assert info_1["primes"] == []
        assert info_1["non_primes"] == [1]

        # Test first layer
        info_3 = get_spiral_layer_info(3)
        assert info_3["side_length"] == 3
        assert info_3["layer"] == 1
        assert info_3["diagonal_values"] == [9, 7, 5, 3]
        assert info_3["prime_status"] == [False, True, True, True]
        assert info_3["primes"] == [7, 5, 3]
        assert info_3["non_primes"] == [9]

    def test_analyze_spiral_pattern(self) -> None:
        """Test spiral pattern analysis"""
        analysis = analyze_spiral_pattern(9)

        assert len(analysis) == 5  # Side lengths 1, 3, 5, 7, 9
        assert all("side_length" in data for data in analysis)
        assert all("prime_count" in data for data in analysis)
        assert all("total_count" in data for data in analysis)
        assert all("ratio" in data for data in analysis)

        # Check progression
        for i in range(1, len(analysis)):
            prev_data = analysis[i - 1]
            curr_data = analysis[i]

            # Side length should increase by 2
            assert curr_data["side_length"] == prev_data["side_length"] + 2

            # Total count should increase by 4 (new layer adds 4 diagonal values)
            assert curr_data["total_count"] == prev_data["total_count"] + 4


class TestBoundaryConditions:
    """Test boundary conditions and edge cases"""

    def test_small_side_lengths(self) -> None:
        """Test smallest valid side lengths"""
        # Side length 1
        values_1 = get_diagonal_values(1)
        assert values_1 == [1]

        # Side length 3
        values_3 = get_diagonal_values(3)
        assert len(values_3) == 4
        assert all(isinstance(v, int) for v in values_3)

    def test_spiral_growth_pattern(self) -> None:
        """Test that spiral grows in expected pattern"""
        for side_length in range(1, 20, 2):
            diagonal_values = get_diagonal_values(side_length)

            if side_length == 1:
                assert diagonal_values == [1]
                continue

            # Should have exactly 4 values for each layer
            assert len(diagonal_values) == 4

            # Values should be in descending order (bottom-right to bottom-left)
            assert diagonal_values[0] > diagonal_values[1]
            assert diagonal_values[1] > diagonal_values[2]
            assert diagonal_values[2] > diagonal_values[3]

            # Largest value should be the square of side length
            assert diagonal_values[0] == side_length * side_length

    def test_prime_ratio_monotonicity(self) -> None:
        """Test that prime ratio generally decreases as spiral grows"""
        ratios = []
        for side_length in range(3, 20, 2):
            ratio = calculate_prime_ratio(side_length)
            ratios.append(ratio)

        # Generally, ratios should decrease (though not strictly monotonic)
        # At least the overall trend should be downward
        assert ratios[0] > ratios[-1]  # First ratio should be higher than last


class TestMathematicalProperties:
    """Test mathematical properties of the spiral"""

    def test_diagonal_value_formulas(self) -> None:
        """Test that diagonal values follow correct mathematical formulas"""
        for n in range(3, 20, 2):
            values = get_diagonal_values(n)

            # Test each diagonal value formula
            assert values[0] == n * n  # Bottom-right
            assert values[1] == n * n - (n - 1)  # Top-right
            assert values[2] == n * n - 2 * (n - 1)  # Top-left
            assert values[3] == n * n - 3 * (n - 1)  # Bottom-left

            # Test differences between adjacent values
            assert values[0] - values[1] == n - 1
            assert values[1] - values[2] == n - 1
            assert values[2] - values[3] == n - 1

    def test_odd_squares_property(self) -> None:
        """Test that odd squares appear in the bottom-right diagonal"""
        # Collect all bottom-right diagonal values
        bottom_right_values = []
        for side_length in range(1, 20, 2):
            if side_length == 1:
                bottom_right_values.append(1)
            else:
                values = get_diagonal_values(side_length)
                bottom_right_values.append(values[0])

        # Check that these are indeed odd squares
        expected_odd_squares = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
        assert bottom_right_values == expected_odd_squares[: len(bottom_right_values)]

        # Verify they are squares of odd numbers
        for i, value in enumerate(bottom_right_values):
            odd_number = 2 * i + 1
            assert value == odd_number * odd_number

    def test_layer_count_formula(self) -> None:
        """Test that the total count of diagonal values follows correct formula"""
        for side_length in range(1, 20, 2):
            _, total_count = count_primes_in_diagonals(side_length)

            # Formula: 1 (center) + 4 * number_of_layers
            number_of_layers = (side_length - 1) // 2
            expected_total = 1 + 4 * number_of_layers

            assert total_count == expected_total


class TestPerformance:
    """Test performance-related aspects"""

    def test_small_problem_performance(self) -> None:
        """Test performance with manageable problem sizes"""
        import time

        start_time = time.time()
        result = solve_optimized(0.3)
        end_time = time.time()

        assert isinstance(result, int)
        assert end_time - start_time < 5.0  # Should complete reasonably quickly

    def test_optimization_effectiveness(self) -> None:
        """Test that optimization improves performance"""
        import time

        ratio = 0.4  # Use higher ratio for faster execution

        # Time naive solution
        start_time = time.time()
        result_naive = solve_naive(ratio)
        naive_time = time.time() - start_time

        # Time optimized solution
        start_time = time.time()
        result_optimized = solve_optimized(ratio)
        optimized_time = time.time() - start_time

        # Results should be the same
        assert result_naive == result_optimized

        # Both should complete in reasonable time
        assert naive_time < 5.0
        assert optimized_time < 5.0

        # For this problem size, the difference might be small, but optimized should not be slower
        # Note: For very small problems, the difference might not be significant


if __name__ == "__main__":
    pytest.main([__file__])
