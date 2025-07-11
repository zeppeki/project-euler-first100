#!/usr/bin/env python3
"""
Test for Problem 097: Large non-Mersenne prime
"""

import pytest

from problems.problem_097 import (
    modular_exponentiation,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    verify_small_case,
)


class TestModularExponentiation:
    """Test modular exponentiation function."""

    def test_basic_cases(self) -> None:
        """Test basic modular exponentiation cases."""
        # Test basic cases
        assert (
            modular_exponentiation(2, 10, 1000) == 24
        )  # 2^10 = 1024, 1024 % 1000 = 24
        assert modular_exponentiation(3, 4, 100) == 81  # 3^4 = 81, 81 % 100 = 81
        assert modular_exponentiation(5, 3, 125) == 0  # 5^3 = 125, 125 % 125 = 0

        # Test with larger modulus
        assert modular_exponentiation(2, 10, 1000) == pow(2, 10, 1000)
        assert modular_exponentiation(3, 13, 1000) == pow(3, 13, 1000)
        assert modular_exponentiation(7, 15, 2000) == pow(7, 15, 2000)

    def test_edge_cases(self) -> None:
        """Test edge cases for modular exponentiation."""
        # Base = 0
        assert modular_exponentiation(0, 5, 100) == 0

        # Exponent = 0
        assert modular_exponentiation(5, 0, 100) == 1

        # Exponent = 1
        assert modular_exponentiation(5, 1, 100) == 5

        # Modulus = 1
        assert modular_exponentiation(5, 10, 1) == 0

    def test_large_numbers(self) -> None:
        """Test with large numbers."""
        # Test cases that would cause overflow in naive implementation
        base, exp, mod = 12345, 67890, 10**9
        expected = pow(base, exp, mod)
        result = modular_exponentiation(base, exp, mod)
        assert result == expected

        # Test very large exponent
        base, exp, mod = 2, 1000000, 10**10
        expected = pow(base, exp, mod)
        result = modular_exponentiation(base, exp, mod)
        assert result == expected

    def test_consistency_with_builtin(self) -> None:
        """Test consistency with Python's built-in pow function."""
        test_cases = [
            (2, 100, 10**6),
            (3, 200, 10**7),
            (5, 150, 10**8),
            (7, 300, 10**9),
            (11, 250, 10**10),
        ]

        for base, exp, mod in test_cases:
            expected = pow(base, exp, mod)
            result = modular_exponentiation(base, exp, mod)
            assert result == expected, f"Failed for {base}^{exp} mod {mod}"


class TestVerifySmallCase:
    """Test verification function for small cases."""

    def test_small_cases(self) -> None:
        """Test small case verification."""
        # Test cases that can be calculated directly
        assert verify_small_case(3, 5, 1) == 97  # 3 × 2^5 + 1 = 3 × 32 + 1 = 97
        assert verify_small_case(7, 4, 2) == 114  # 7 × 2^4 + 2 = 7 × 16 + 2 = 114
        assert verify_small_case(1, 10, 0) == 1024  # 1 × 2^10 + 0 = 1024

    def test_modular_behavior(self) -> None:
        """Test that function correctly applies modulo 10^10."""
        # Test with result that needs modulo
        mult, exp, add = 123456789, 10, 987654321
        result = verify_small_case(mult, exp, add)
        expected = (mult * (2**exp) + add) % (10**10)
        assert result == expected

    def test_large_exponent_rejection(self) -> None:
        """Test that function rejects large exponents."""
        with pytest.raises(ValueError):
            verify_small_case(2, 50, 1)  # Too large for direct calculation


class TestSolutionMethods:
    """Test solution methods."""

    def test_small_examples(self) -> None:
        """Test with small examples."""
        # Test case: 3 × 2^5 + 1 = 97
        mult, exp, add = 3, 5, 1
        expected = 97 % (10**10)  # Still 97 since it's small

        assert solve_naive(mult, exp, add) == expected
        assert solve_optimized(mult, exp, add) == expected
        assert solve_mathematical(mult, exp, add) == expected

    def test_medium_examples(self) -> None:
        """Test with medium-sized examples."""
        # Test case: 7 × 2^10 + 3 = 7171
        mult, exp, add = 7, 10, 3
        expected = 7171 % (10**10)  # Still 7171 since it's small

        assert solve_naive(mult, exp, add) == expected
        assert solve_optimized(mult, exp, add) == expected
        assert solve_mathematical(mult, exp, add) == expected

    def test_larger_examples(self) -> None:
        """Test with larger examples that require modular arithmetic."""
        # Test case that produces a large result
        mult, exp, add = 12345, 100, 6789

        result_naive = solve_naive(mult, exp, add)
        result_optimized = solve_optimized(mult, exp, add)
        result_mathematical = solve_mathematical(mult, exp, add)

        # All methods should give the same result
        assert result_naive == result_optimized == result_mathematical

        # Result should be within range [0, 10^10)
        assert 0 <= result_naive < 10**10

    def test_main_problem_consistency(self) -> None:
        """Test that all methods give the same result for main problem."""
        # Test with default parameters (main problem)
        result_naive = solve_naive()
        result_optimized = solve_optimized()
        result_mathematical = solve_mathematical()

        assert result_naive == result_optimized == result_mathematical

        # Result should be a valid 10-digit number (or less)
        assert 0 <= result_naive < 10**10

    def test_default_parameters(self) -> None:
        """Test that default parameters work correctly."""
        # All methods should work with no parameters
        result_naive = solve_naive()
        result_optimized = solve_optimized()
        result_mathematical = solve_mathematical()

        # Should all be equal
        assert result_naive == result_optimized == result_mathematical

        # Should be the expected answer for the main problem
        assert result_naive == 8739992577

    def test_parameter_variations(self) -> None:
        """Test with various parameter combinations."""
        test_cases = [
            (1, 20, 0),  # Simple case
            (28433, 100, 1),  # Smaller version of main problem
            (999, 50, 999),  # Various parameters
        ]

        for mult, exp, add in test_cases:
            result_naive = solve_naive(mult, exp, add)
            result_optimized = solve_optimized(mult, exp, add)
            result_mathematical = solve_mathematical(mult, exp, add)

            assert result_naive == result_optimized == result_mathematical


class TestProblem097:
    """Test the main problem solution."""

    def test_main_problem_result(self) -> None:
        """Test the main problem result."""
        # The expected answer for Problem 097
        expected_result = 8739992577

        result = solve_mathematical()
        assert result == expected_result

    def test_result_format(self) -> None:
        """Test that result has correct format."""
        result = solve_mathematical()

        # Should be a positive integer
        assert isinstance(result, int)
        assert result >= 0

        # Should be less than 10^10 (last 10 digits)
        assert result < 10**10

        # For the main problem, should be exactly 10 digits
        assert result == 8739992577  # Known answer

    def test_algorithm_properties(self) -> None:
        """Test properties of the algorithms."""
        # Test that modular exponentiation gives correct results
        # for the main problem components

        # Calculate 2^7830457 mod 10^10
        power_mod = modular_exponentiation(2, 7830457, 10**10)

        # Calculate full result
        result = (28433 * power_mod + 1) % (10**10)

        # Should match our solution functions
        assert result == solve_mathematical()

    def test_performance_characteristics(self) -> None:
        """Test performance characteristics."""
        import time

        # Test that main problem can be solved quickly
        start_time = time.time()
        result = solve_optimized()
        end_time = time.time()

        # Should complete very quickly (less than 1 second)
        assert end_time - start_time < 1.0

        # Should get correct result
        assert result == 8739992577

    def test_mathematical_verification(self) -> None:
        """Test mathematical properties of the solution."""
        # Verify using different approaches

        # Method 1: Direct calculation with our functions
        result1 = solve_mathematical()

        # Method 2: Step by step calculation
        modulus = 10**10
        power_of_two = pow(2, 7830457, modulus)
        result2 = (28433 * power_of_two + 1) % modulus

        # Method 3: Using our modular exponentiation
        power_of_two_custom = modular_exponentiation(2, 7830457, modulus)
        result3 = (28433 * power_of_two_custom + 1) % modulus

        # All should be equal
        assert result1 == result2 == result3 == 8739992577

    def test_edge_case_parameters(self) -> None:
        """Test edge cases with different parameters."""
        # Test with multiplier = 1
        result = solve_mathematical(1, 10, 0)
        expected = 2**10 % (10**10)  # 1024
        assert result == expected

        # Test with addend = 0
        result = solve_mathematical(5, 10, 0)
        expected = (5 * (2**10)) % (10**10)  # 5120
        assert result == expected

        # Test with exponent = 0
        result = solve_mathematical(123, 0, 456)
        expected = (123 * 1 + 456) % (10**10)  # 579
        assert result == expected


class TestIntegration:
    """Integration tests."""

    def test_all_functions_consistency(self) -> None:
        """Test that all functions work together consistently."""
        # Test multiple parameter combinations
        test_cases = [
            (),  # Default parameters
            (1, 5, 1),  # Small case
            (100, 20, 50),  # Medium case
            (28433, 1000, 1),  # Reduced main problem
        ]

        for params in test_cases:
            results = []
            results.append(solve_naive(*params))
            results.append(solve_optimized(*params))
            results.append(solve_mathematical(*params))

            # All results should be equal
            assert len(set(results)) == 1, (
                f"Inconsistent results for {params}: {results}"
            )

            # Results should be in valid range
            assert all(0 <= r < 10**10 for r in results)

    def test_small_case_verification(self) -> None:
        """Test against small cases that can be verified manually."""
        # Cases where we can verify the result manually
        verifiable_cases = [
            (3, 5, 1),  # 3 × 32 + 1 = 97
            (7, 4, 2),  # 7 × 16 + 2 = 114
            (1, 10, 0),  # 1 × 1024 + 0 = 1024
        ]

        for mult, exp, add in verifiable_cases:
            if exp <= 20:  # Safe for direct calculation
                expected = verify_small_case(mult, exp, add)
                result = solve_mathematical(mult, exp, add)
                assert result == expected, f"Failed for {mult} × 2^{exp} + {add}"
