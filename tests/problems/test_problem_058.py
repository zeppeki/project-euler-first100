"""Tests for Problem 058: Spiral primes."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
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


class TestProblem058:
    """Test cases for Problem 058."""

    @pytest.mark.parametrize(
        "target_ratio,expected",
        [
            (0.5, 5),  # 辺の長さ5で素数比率が50%未満
            (0.3, 9),  # 辺の長さ9で素数比率が30%未満
            (0.2, 11),  # 辺の長さ11で素数比率が20%未満
        ],
    )
    def test_solve_naive(self, target_ratio: float, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(target_ratio)
        assert result == expected, (
            f"Expected {expected}, got {result} for target_ratio={target_ratio}"
        )

    @pytest.mark.parametrize(
        "target_ratio,expected",
        [
            (0.5, 5),  # 辺の長さ5で素数比率が50%未満
            (0.3, 9),  # 辺の長さ9で素数比率が30%未満
            (0.2, 11),  # 辺の長さ11で素数比率が20%未満
        ],
    )
    def test_solve_optimized(self, target_ratio: float, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(target_ratio)
        assert result == expected, (
            f"Expected {expected}, got {result} for target_ratio={target_ratio}"
        )

    @pytest.mark.parametrize("target_ratio", [0.5, 0.3, 0.2])
    def test_all_solutions_agree(self, target_ratio: float) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(target_ratio)
        optimized_result = solve_optimized(target_ratio)

        assert naive_result == optimized_result, (
            f"Solutions disagree for target_ratio={target_ratio}: "
            f"naive={naive_result}, optimized={optimized_result}"
        )

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, False),  # 1は素数ではない
            (2, True),  # 2は素数
            (3, True),  # 3は素数
            (4, False),  # 4は合成数
            (5, True),  # 5は素数
            (6, False),  # 6は合成数
            (7, True),  # 7は素数
            (8, False),  # 8は合成数
            (9, False),  # 9は合成数
            (10, False),  # 10は合成数
            (11, True),  # 11は素数
            (13, True),  # 13は素数
            (17, True),  # 17は素数
            (19, True),  # 19は素数
            (23, True),  # 23は素数
            (25, False),  # 25は合成数
            (29, True),  # 29は素数
            (31, True),  # 31は素数
            (37, True),  # 37は素数
            (41, True),  # 41は素数
            (43, True),  # 43は素数
            (47, True),  # 47は素数
            (49, False),  # 49は合成数
            (100, False),  # 100は合成数
        ],
    )
    def test_is_prime(self, n: int, expected: bool) -> None:
        """Test prime checking function."""
        result = is_prime(n)
        assert result == expected, f"Expected {expected}, got {result} for n={n}"

    @pytest.mark.parametrize(
        "side_length,expected",
        [
            (1, [1]),
            (3, [9, 7, 5, 3]),  # 3² = 9, 9-2=7, 9-4=5, 9-6=3
            (5, [25, 21, 17, 13]),  # 5² = 25, 25-4=21, 25-8=17, 25-12=13
            (7, [49, 43, 37, 31]),  # 7² = 49, 49-6=43, 49-12=37, 49-18=31
            (2, []),  # 偶数の辺の長さは無効
            (4, []),  # 偶数の辺の長さは無効
        ],
    )
    def test_get_diagonal_values(self, side_length: int, expected: list[int]) -> None:
        """Test diagonal value calculation for a specific side length."""
        result = get_diagonal_values(side_length)
        assert result == expected, (
            f"Expected {expected}, got {result} for side_length={side_length}"
        )

    @pytest.mark.parametrize(
        "side_length,expected",
        [
            (1, [1]),
            (3, [1, 9, 7, 5, 3]),
            (5, [1, 9, 7, 5, 3, 25, 21, 17, 13]),
            (7, [1, 9, 7, 5, 3, 25, 21, 17, 13, 49, 43, 37, 31]),
        ],
    )
    def test_get_all_diagonal_values(
        self, side_length: int, expected: list[int]
    ) -> None:
        """Test all diagonal values up to a given side length."""
        result = get_all_diagonal_values(side_length)
        assert result == expected, (
            f"Expected {expected}, got {result} for side_length={side_length}"
        )

    @pytest.mark.parametrize(
        "side_length,expected_prime_count,expected_total_count",
        [
            (1, 0, 1),  # [1] - 1は素数ではない
            (3, 3, 5),  # [1, 9, 7, 5, 3] - 素数は7, 5, 3
            (5, 5, 9),  # [1, 9, 7, 5, 3, 25, 21, 17, 13] - 素数は7, 5, 3, 17, 13
            (7, 8, 13),  # 問題文の例: 8個の素数
        ],
    )
    def test_count_primes_in_diagonals(
        self, side_length: int, expected_prime_count: int, expected_total_count: int
    ) -> None:
        """Test counting primes in diagonal values."""
        prime_count, total_count = count_primes_in_diagonals(side_length)
        assert prime_count == expected_prime_count, (
            f"Expected {expected_prime_count} primes, got {prime_count} for side_length={side_length}"
        )
        assert total_count == expected_total_count, (
            f"Expected {expected_total_count} total, got {total_count} for side_length={side_length}"
        )

    @pytest.mark.parametrize(
        "side_length,expected_ratio",
        [
            (1, 0.0),  # 0/1 = 0.0
            (3, 0.6),  # 3/5 = 0.6
            (5, 5 / 9),  # 5/9 ≈ 0.556
            (7, 8 / 13),  # 8/13 ≈ 0.615 (問題文の例)
        ],
    )
    def test_calculate_prime_ratio(
        self, side_length: int, expected_ratio: float
    ) -> None:
        """Test prime ratio calculation."""
        result = calculate_prime_ratio(side_length)
        assert abs(result - expected_ratio) < 0.001, (
            f"Expected {expected_ratio}, got {result} for side_length={side_length}"
        )

    def test_verify_example_spiral(self) -> None:
        """Test the example spiral verification."""
        result = verify_example_spiral()
        assert result is True, "Example spiral verification should pass"

    def test_spiral_layer_info(self) -> None:
        """Test spiral layer information extraction."""
        # Test side length 1
        layer_info = get_spiral_layer_info(1)
        assert layer_info["side_length"] == 1
        assert layer_info["layer"] == 0
        assert layer_info["diagonal_values"] == [1]
        assert layer_info["prime_status"] == [False]
        assert layer_info["primes"] == []
        assert layer_info["non_primes"] == [1]

        # Test side length 3
        layer_info = get_spiral_layer_info(3)
        assert layer_info["side_length"] == 3
        assert layer_info["layer"] == 1
        assert layer_info["diagonal_values"] == [9, 7, 5, 3]
        assert layer_info["prime_status"] == [False, True, True, True]
        assert layer_info["primes"] == [7, 5, 3]
        assert layer_info["non_primes"] == [9]

        # Test side length 5
        layer_info = get_spiral_layer_info(5)
        assert layer_info["side_length"] == 5
        assert layer_info["layer"] == 2
        assert layer_info["diagonal_values"] == [25, 21, 17, 13]
        assert layer_info["prime_status"] == [False, False, True, True]
        assert layer_info["primes"] == [17, 13]
        assert layer_info["non_primes"] == [25, 21]

    def test_analyze_spiral_pattern(self) -> None:
        """Test spiral pattern analysis."""
        analysis = analyze_spiral_pattern(7)

        assert len(analysis) == 4  # side lengths 1, 3, 5, 7

        # Check side length 1
        assert analysis[0]["side_length"] == 1
        assert analysis[0]["prime_count"] == 0
        assert analysis[0]["total_count"] == 1
        assert analysis[0]["ratio"] == 0.0

        # Check side length 3
        assert analysis[1]["side_length"] == 3
        assert analysis[1]["prime_count"] == 3
        assert analysis[1]["total_count"] == 5
        assert analysis[1]["ratio"] == 0.6

        # Check side length 7 (example from problem)
        assert analysis[3]["side_length"] == 7
        assert analysis[3]["prime_count"] == 8
        assert analysis[3]["total_count"] == 13
        assert abs(analysis[3]["ratio"] - 8 / 13) < 0.001

    def test_diagonal_value_formulas(self) -> None:
        """Test diagonal value formulas for specific cases."""
        # For side length n, the diagonal values should be:
        # Bottom right: n²
        # Top right: n² - (n-1)
        # Top left: n² - 2*(n-1)
        # Bottom left: n² - 3*(n-1)

        # Test side length 3
        diagonal_values = get_diagonal_values(3)
        assert diagonal_values[0] == 9  # 3² = 9
        assert diagonal_values[1] == 7  # 9 - 2 = 7
        assert diagonal_values[2] == 5  # 9 - 4 = 5
        assert diagonal_values[3] == 3  # 9 - 6 = 3

        # Test side length 5
        diagonal_values = get_diagonal_values(5)
        assert diagonal_values[0] == 25  # 5² = 25
        assert diagonal_values[1] == 21  # 25 - 4 = 21
        assert diagonal_values[2] == 17  # 25 - 8 = 17
        assert diagonal_values[3] == 13  # 25 - 12 = 13

        # Test side length 7
        diagonal_values = get_diagonal_values(7)
        assert diagonal_values[0] == 49  # 7² = 49
        assert diagonal_values[1] == 43  # 49 - 6 = 43
        assert diagonal_values[2] == 37  # 49 - 12 = 37
        assert diagonal_values[3] == 31  # 49 - 18 = 31

    def test_prime_ratio_decreases(self) -> None:
        """Test that prime ratio generally decreases as side length increases."""
        ratios = []
        for side_length in [3, 5, 7, 9, 11, 13]:
            ratio = calculate_prime_ratio(side_length)
            ratios.append(ratio)

        # The ratio should generally decrease (though not strictly monotonic)
        # At least verify that the ratio at side length 13 is less than at side length 3
        assert ratios[-1] < ratios[0], "Prime ratio should decrease over time"

    def test_solution_verification(self) -> None:
        """Verify solutions by checking the prime ratios."""
        # Test with known target ratios
        target_ratios = [0.5, 0.3, 0.2]

        for target_ratio in target_ratios:
            result = solve_optimized(target_ratio)

            # Check that the ratio at the result is below the target
            actual_ratio = calculate_prime_ratio(result)
            assert actual_ratio < target_ratio, (
                f"Ratio {actual_ratio} should be below target {target_ratio} at side length {result}"
            )

            # Check that the previous side length (if >= 3) has ratio >= target
            if result > 3:
                prev_side_length = result - 2
                prev_ratio = calculate_prime_ratio(prev_side_length)
                assert prev_ratio >= target_ratio, (
                    f"Previous ratio {prev_ratio} should be >= target {target_ratio} at side length {prev_side_length}"
                )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with very high target ratio (should return 3)
        result = solve_naive(0.9)
        assert result == 3, "High target ratio should return side length 3"

        # Test with very low target ratio (should find a solution)
        result = solve_naive(0.05)
        assert result >= 3, "Low target ratio should find a valid solution"
        assert result % 2 == 1, "Result should be odd (valid side length)"

    def test_problem_examples(self) -> None:
        """Test the specific examples from the problem statement."""
        # Example from problem: side length 7 has 8 primes out of 13 diagonals
        prime_count, total_count = count_primes_in_diagonals(7)
        assert prime_count == 8, f"Expected 8 primes, got {prime_count}"
        assert total_count == 13, f"Expected 13 total, got {total_count}"

        # The ratio should be 8/13 ≈ 0.615
        ratio = calculate_prime_ratio(7)
        expected_ratio = 8 / 13
        assert abs(ratio - expected_ratio) < 0.001, (
            f"Expected ratio {expected_ratio}, got {ratio}"
        )

    def test_diagonal_sequence_properties(self) -> None:
        """Test properties of the diagonal sequence."""
        # Test that diagonal values are in descending order for each layer
        for side_length in [3, 5, 7, 9, 11]:
            diagonal_values = get_diagonal_values(side_length)
            for i in range(1, len(diagonal_values)):
                assert diagonal_values[i] < diagonal_values[i - 1], (
                    f"Diagonal values should be in descending order for side length {side_length}"
                )

    def test_performance_characteristics(self) -> None:
        """Test performance characteristics without timing."""
        # Test that solutions work for reasonable inputs
        target_ratios = [0.5, 0.3, 0.2, 0.15]

        for target_ratio in target_ratios:
            # Both solutions should complete and agree
            result_naive = solve_naive(target_ratio)
            result_optimized = solve_optimized(target_ratio)

            assert result_naive == result_optimized, (
                f"Solutions disagree for target_ratio={target_ratio}"
            )

            # Result should be reasonable (odd, >= 3)
            assert result_naive >= 3, (
                f"Result should be at least 3 for target_ratio={target_ratio}"
            )
            assert result_naive % 2 == 1, (
                f"Result should be odd for target_ratio={target_ratio}"
            )

    @pytest.mark.slow
    def test_main_problem(self) -> None:
        """Test the main problem (marked as slow)."""
        # Test with target_ratio = 0.1 (the actual problem)
        # This is marked as slow because it may take some time
        target_ratio = 0.1

        # Test only the optimized solution for speed
        result = solve_optimized(target_ratio)

        # Verify that the ratio is below the target
        actual_ratio = calculate_prime_ratio(result)
        assert actual_ratio < target_ratio, (
            f"Ratio {actual_ratio} should be below target {target_ratio}"
        )

        # Verify that the result is a valid odd side length
        assert result >= 3, "Result should be at least 3"
        assert result % 2 == 1, "Result should be odd"

        # Verify that the previous side length has ratio >= target
        if result > 3:
            prev_ratio = calculate_prime_ratio(result - 2)
            assert prev_ratio >= target_ratio, (
                f"Previous ratio {prev_ratio} should be >= target {target_ratio}"
            )

    def test_mathematical_properties(self) -> None:
        """Test mathematical properties of the spiral."""
        # Test that the center value is always 1
        all_diagonals = get_all_diagonal_values(13)
        assert all_diagonals[0] == 1, "Center value should always be 1"

        # Test that each layer adds exactly 4 diagonal values (except center)
        for side_length in [3, 5, 7, 9, 11]:
            diagonal_values = get_diagonal_values(side_length)
            assert len(diagonal_values) == 4, (
                f"Each layer should have 4 diagonal values, got {len(diagonal_values)} for side length {side_length}"
            )

        # Test that the total number of diagonal values follows the pattern
        for side_length in [3, 5, 7, 9, 11]:
            all_diagonals = get_all_diagonal_values(side_length)
            layers = (side_length - 1) // 2
            expected_count = 1 + 4 * layers  # 1 center + 4 values per layer
            assert len(all_diagonals) == expected_count, (
                f"Expected {expected_count} diagonal values, got {len(all_diagonals)} for side length {side_length}"
            )

    def test_correctness_verification(self) -> None:
        """Final correctness verification."""
        # Verify the example from the problem statement
        assert verify_example_spiral(), "Example spiral verification should pass"

        # Verify specific known ratios
        test_cases = [
            (7, 8 / 13),  # Example from problem
            (3, 3 / 5),  # First non-trivial case
            (5, 5 / 9),  # Second case
        ]

        for side_length, expected_ratio in test_cases:
            actual_ratio = calculate_prime_ratio(side_length)
            assert abs(actual_ratio - expected_ratio) < 0.001, (
                f"Ratio mismatch for side length {side_length}: expected {expected_ratio}, got {actual_ratio}"
            )

        # Verify that solutions find the correct answer for known cases
        known_cases = [
            (0.5, 5),
            (0.3, 9),
            (0.2, 11),
        ]

        for target_ratio, expected_side_length in known_cases:
            result = solve_optimized(target_ratio)
            assert result == expected_side_length, (
                f"Expected side length {expected_side_length} for target ratio {target_ratio}, got {result}"
            )
