#!/usr/bin/env python3
"""
Test for Problem 099: Largest exponential
"""

import math
import os
import tempfile

from problems.problem_099 import (
    compare_exponentials_logarithmic,
    compare_exponentials_naive,
    get_exponential_info,
    load_base_exp_data,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestUtilityFunctions:
    """Test utility functions for largest exponential."""

    def test_load_base_exp_data(self) -> None:
        """Test loading base-exponent data from file."""
        pairs = load_base_exp_data()

        # Should load many pairs
        assert len(pairs) > 900  # Expecting 1000 pairs

        # Check structure
        for base, exp in pairs[:10]:
            assert isinstance(base, int)
            assert isinstance(exp, int)
            assert base > 0
            assert exp > 0

    def test_load_base_exp_data_with_custom_file(self) -> None:
        """Test loading data with a custom test file."""
        # Create temporary test file
        test_data = "2,11\n3,7\n5,3\n"

        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write(test_data)
            temp_filename = os.path.basename(f.name)

        try:
            # Move to data directory for testing
            import shutil

            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(
                os.path.dirname(os.path.dirname(current_dir)), "data"
            )
            temp_path = os.path.join(data_dir, temp_filename)
            shutil.move(f.name, temp_path)

            pairs = load_base_exp_data(temp_filename)

            expected = [(2, 11), (3, 7), (5, 3)]
            assert pairs == expected

        finally:
            # Cleanup
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_compare_exponentials_naive(self) -> None:
        """Test naive exponential comparison for small numbers."""
        # 2^11 = 2048 vs 3^7 = 2187
        assert compare_exponentials_naive(2, 11, 3, 7) == -1  # 2^11 < 3^7
        assert compare_exponentials_naive(3, 7, 2, 11) == 1  # 3^7 > 2^11

        # Equal values
        assert compare_exponentials_naive(2, 3, 2, 3) == 0  # 2^3 = 2^3

        # More examples
        assert compare_exponentials_naive(5, 3, 2, 8) == -1  # 125 < 256
        assert compare_exponentials_naive(10, 2, 4, 3) == 1  # 100 > 64

    def test_compare_exponentials_logarithmic(self) -> None:
        """Test logarithmic exponential comparison."""
        # Same tests as naive for small numbers
        assert compare_exponentials_logarithmic(2, 11, 3, 7) == -1
        assert compare_exponentials_logarithmic(3, 7, 2, 11) == 1
        assert compare_exponentials_logarithmic(2, 3, 2, 3) == 0

        # Test with larger numbers (where naive would be impractical)
        assert (
            compare_exponentials_logarithmic(1000, 1000, 999, 1001) == -1
        )  # 999^1001 > 1000^1000
        assert compare_exponentials_logarithmic(2, 1000, 3, 700) == -1

    def test_naive_vs_logarithmic_consistency(self) -> None:
        """Test that naive and logarithmic methods give same results for small numbers."""
        test_cases = [
            (2, 3, 4, 2),  # 8 vs 16
            (3, 4, 5, 3),  # 81 vs 125
            (7, 2, 6, 2),  # 49 vs 36
            (10, 3, 8, 3),  # 1000 vs 512
        ]

        for base1, exp1, base2, exp2 in test_cases:
            naive_result = compare_exponentials_naive(base1, exp1, base2, exp2)
            log_result = compare_exponentials_logarithmic(base1, exp1, base2, exp2)
            assert naive_result == log_result

    def test_get_exponential_info(self) -> None:
        """Test exponential information calculation."""
        # Test with known values
        info = get_exponential_info(10, 3)
        assert info["base"] == 10
        assert info["exponent"] == 3
        assert info["estimated_digits"] == 4  # 10^3 = 1000 has 4 digits

        # Test with 2^10 = 1024
        info = get_exponential_info(2, 10)
        assert info["base"] == 2
        assert info["exponent"] == 10
        assert info["estimated_digits"] == 4  # 1024 has 4 digits

        # Check that log value is positive
        assert info["log_value"] > 0
        assert info["base_log"] > 0


class TestSolutionMethods:
    """Test solution methods."""

    def test_solution_consistency(self) -> None:
        """Test that all solution methods give the same results."""
        # Test with main data file
        result_naive = solve_naive()
        result_optimized = solve_optimized()
        result_mathematical = solve_mathematical()

        assert result_naive == result_optimized == result_mathematical

    def test_main_problem_result(self) -> None:
        """Test the main problem result."""
        # The expected answer for Problem 099
        expected_result = 709

        result = solve_mathematical()
        assert result == expected_result

    def test_result_properties(self) -> None:
        """Test properties of the result."""
        result = solve_mathematical()

        # Should be a positive integer
        assert isinstance(result, int)
        assert result > 0

        # Should be within the range of lines in the file
        pairs = load_base_exp_data()
        assert 1 <= result <= len(pairs)

    def test_with_small_custom_dataset(self) -> None:
        """Test with a small custom dataset."""
        # Create test data where we know the answer
        test_data = "2,11\n3,7\n5,4\n"  # 2048, 2187, 625

        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write(test_data)
            temp_filename = os.path.basename(f.name)

        try:
            # Move to data directory
            import shutil

            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(
                os.path.dirname(os.path.dirname(current_dir)), "data"
            )
            temp_path = os.path.join(data_dir, temp_filename)
            shutil.move(f.name, temp_path)

            # 3^7 = 2187 is the largest
            result = solve_optimized(temp_filename)
            assert result == 2  # Second line (3^7)

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_edge_cases(self) -> None:
        """Test edge cases and error handling."""
        # Test with minimal data
        test_data = "2,3\n"

        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write(test_data)
            temp_filename = os.path.basename(f.name)

        try:
            import shutil

            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(
                os.path.dirname(os.path.dirname(current_dir)), "data"
            )
            temp_path = os.path.join(data_dir, temp_filename)
            shutil.move(f.name, temp_path)

            result = solve_optimized(temp_filename)
            assert result == 1  # Only one line

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


class TestPerformanceAndIntegration:
    """Test performance characteristics and integration."""

    def test_algorithm_efficiency(self) -> None:
        """Test that algorithms complete in reasonable time."""
        import time

        # Test with main problem
        start_time = time.time()
        result = solve_optimized()
        end_time = time.time()

        # Should complete quickly (less than 1 second)
        assert end_time - start_time < 1.0

        # Should get correct result
        assert result == 709

    def test_data_integrity(self) -> None:
        """Test data file integrity."""
        pairs = load_base_exp_data()

        # Should have approximately 1000 pairs
        assert 900 < len(pairs) < 1100

        # All pairs should be valid
        for base, exp in pairs:
            assert isinstance(base, int)
            assert isinstance(exp, int)
            assert base > 0
            assert exp > 0

            # Should be reasonable ranges
            assert base < 10**7  # Base shouldn't be too large
            assert exp < 10**7  # Exponent shouldn't be too large

    def test_mathematical_properties(self) -> None:
        """Test mathematical properties of the solution."""
        pairs = load_base_exp_data()
        result = solve_mathematical()

        # Get the winning pair
        winning_base, winning_exp = pairs[result - 1]
        winning_log = winning_exp * math.log(winning_base)

        # Verify it's actually the maximum
        for i, (base, exp) in enumerate(pairs):
            log_value = exp * math.log(base)
            if i + 1 != result:
                assert log_value <= winning_log, (
                    f"Line {i + 1} has larger log value than winner"
                )

    def test_logarithmic_precision(self) -> None:
        """Test precision of logarithmic calculations."""
        # Test cases where precision matters

        # Very close values
        log1 = 1000 * math.log(2.0001)
        log2 = 1000 * math.log(2.0000)
        assert log1 > log2  # Should distinguish small differences

        # Large numbers - test that we can handle without overflow
        _ = 500000 * math.log(10000)
        _ = 500001 * math.log(9999)

    def test_consistency_across_methods(self) -> None:
        """Test consistency across all solution methods."""
        # All methods should give the same result
        results = [solve_naive(), solve_optimized(), solve_mathematical()]

        # All results should be identical
        assert all(r == results[0] for r in results)

    def test_robustness(self) -> None:
        """Test robustness of the solution."""
        pairs = load_base_exp_data()

        # Test with different orderings shouldn't matter for mathematical solution
        # (since it processes sequentially)
        result = solve_mathematical()

        # Verify the result is valid
        assert 1 <= result <= len(pairs)

        # Verify the winning pair exists
        winning_base, winning_exp = pairs[result - 1]
        assert winning_base > 0
        assert winning_exp > 0

    def test_known_examples(self) -> None:
        """Test with known examples from problem statement."""
        # 2^11 vs 3^7: 2048 vs 2187, so 3^7 is larger
        assert compare_exponentials_logarithmic(2, 11, 3, 7) == -1
        assert compare_exponentials_logarithmic(3, 7, 2, 11) == 1

        # The problem mentions 632382^518061 > 519432^525806
        # These are the first two lines in the file
        pairs = load_base_exp_data()
        if len(pairs) >= 2:
            base1, exp1 = pairs[0]  # 519432, 525806
            base2, exp2 = pairs[1]  # 632382, 518061

            # According to problem, line 2 should be larger than line 1
            result = compare_exponentials_logarithmic(base2, exp2, base1, exp1)
            assert result == 1, (
                "Second line should be larger than first according to problem statement"
            )
