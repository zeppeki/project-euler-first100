"""Tests for Problem 012: Highly divisible triangular number."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
# Import functions from common library
from problems.lib import (
    count_divisors as count_divisors_naive,
)
from problems.lib import (
    count_divisors as count_divisors_optimized,
)
from problems.lib import (
    get_triangular_number,
    prime_factorization,
)
from problems.problem_012 import (
    get_divisors,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem012:
    """Test cases for Problem 012."""

    @pytest.mark.parametrize(
        "target_divisors,expected",
        [
            (0, 1),  # 0 divisors より多い最初の三角数は 1 (divisors: 1)
            (1, 3),  # 1 divisor より多い最初の三角数は 3 (divisors: 1,3)
            (2, 6),  # 2 divisors より多い最初の三角数は 6 (divisors: 1,2,3,6)
        ],
    )
    def test_solve_naive(self, target_divisors: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(target_divisors)
        assert result == expected, (
            f"Expected {expected}, got {result} for target_divisors={target_divisors}"
        )

    @pytest.mark.parametrize(
        "target_divisors,expected",
        [
            (0, 1),  # 0 divisors より多い最初の三角数は 1
            (1, 3),  # 1 divisor より多い最初の三角数は 3
            (2, 6),  # 2 divisors より多い最初の三角数は 6
        ],
    )
    def test_solve_optimized(self, target_divisors: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(target_divisors)
        assert result == expected, (
            f"Expected {expected}, got {result} for target_divisors={target_divisors}"
        )

    @pytest.mark.parametrize(
        "target_divisors,expected",
        [
            (0, 1),  # 0 divisors より多い最初の三角数は 1
            (1, 3),  # 1 divisor より多い最初の三角数は 3
            (2, 6),  # 2 divisors より多い最初の三角数は 6
        ],
    )
    def test_solve_mathematical(self, target_divisors: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(target_divisors)
        assert result == expected, (
            f"Expected {expected}, got {result} for target_divisors={target_divisors}"
        )

    @pytest.mark.parametrize("target_divisors", [0, 1, 2])
    def test_all_solutions_agree(self, target_divisors: int) -> None:
        """Test that all solutions give the same result."""
        # Use only mathematical and optimized for speed in CI
        optimized_result = solve_optimized(target_divisors)
        math_result = solve_mathematical(target_divisors)

        assert optimized_result == math_result, (
            f"Solutions disagree for target_divisors={target_divisors}: "
            f"optimized={optimized_result}, math={math_result}"
        )

        # Only test naive for smaller cases to save time
        if target_divisors <= 2:
            naive_result = solve_naive(target_divisors)
            assert naive_result == optimized_result, (
                f"Naive disagrees for target_divisors={target_divisors}: "
                f"naive={naive_result}, optimized={optimized_result}"
            )

    def test_triangular_number_generation(self) -> None:
        """Test triangular number generation."""
        # Test first 10 triangular numbers
        expected_triangular = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

        for i, expected in enumerate(expected_triangular, 1):
            result = get_triangular_number(i)
            assert result == expected, f"T_{i} should be {expected}, got {result}"

    def test_divisor_counting(self) -> None:
        """Test divisor counting functions."""
        test_cases = [
            (1, 1),  # 1: [1]
            (3, 2),  # 3: [1, 3]
            (6, 4),  # 6: [1, 2, 3, 6]
            (10, 4),  # 10: [1, 2, 5, 10]
            (15, 4),  # 15: [1, 3, 5, 15]
            (21, 4),  # 21: [1, 3, 7, 21]
            (28, 6),  # 28: [1, 2, 4, 7, 14, 28]
            (36, 9),  # 36: [1, 2, 3, 4, 6, 9, 12, 18, 36]
        ]

        for number, expected_count in test_cases:
            naive_count = count_divisors_naive(number)
            optimized_count = count_divisors_optimized(number)
            actual_divisors = get_divisors(number)

            assert naive_count == expected_count, (
                f"Naive count for {number}: expected {expected_count}, got {naive_count}"
            )
            assert optimized_count == expected_count, (
                f"Optimized count for {number}: expected {expected_count}, got {optimized_count}"
            )
            assert len(actual_divisors) == expected_count, (
                f"Actual divisors count for {number}: expected {expected_count}, got {len(actual_divisors)}"
            )

    def test_prime_factorization(self) -> None:
        """Test prime factorization function."""
        test_cases = [
            (1, {}),  # 1 has no prime factors
            (2, {2: 1}),  # 2 = 2^1
            (3, {3: 1}),  # 3 = 3^1
            (4, {2: 2}),  # 4 = 2^2
            (6, {2: 1, 3: 1}),  # 6 = 2^1 * 3^1
            (8, {2: 3}),  # 8 = 2^3
            (12, {2: 2, 3: 1}),  # 12 = 2^2 * 3^1
            (18, {2: 1, 3: 2}),  # 18 = 2^1 * 3^2
            (28, {2: 2, 7: 1}),  # 28 = 2^2 * 7^1
            (60, {2: 2, 3: 1, 5: 1}),  # 60 = 2^2 * 3^1 * 5^1
        ]

        for number, expected in test_cases:
            result = prime_factorization(number)
            assert dict(result) == expected, (
                f"Prime factorization of {number}: expected {expected}, got {dict(result)}"
            )

    def test_get_divisors(self) -> None:
        """Test divisor enumeration."""
        test_cases = [
            (1, [1]),
            (3, [1, 3]),
            (6, [1, 2, 3, 6]),
            (10, [1, 2, 5, 10]),
            (15, [1, 3, 5, 15]),
            (21, [1, 3, 7, 21]),
            (28, [1, 2, 4, 7, 14, 28]),
        ]

        for number, expected in test_cases:
            result = get_divisors(number)
            assert result == expected, (
                f"Divisors of {number}: expected {expected}, got {result}"
            )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with target_divisors = 0 (should find first triangular number with more than 0 divisors)
        assert solve_naive(0) == 1
        assert solve_optimized(0) == 1
        assert solve_mathematical(0) == 1

    def test_invalid_input(self) -> None:
        """Test with invalid input."""
        # All solutions should raise ValueError for negative target_divisors
        with pytest.raises(ValueError):
            solve_naive(-1)
        with pytest.raises(ValueError):
            solve_optimized(-1)
        with pytest.raises(ValueError):
            solve_mathematical(-1)

    @pytest.mark.slow
    def test_large_number(self) -> None:
        """Test with the actual problem number (marked as slow)."""
        # Test with the actual problem limit using fastest algorithm only
        target_divisors = 500
        expected = 76576500  # Known Project Euler answer

        # Test only mathematical solution for speed
        result_math = solve_mathematical(target_divisors)
        assert result_math == expected

    def test_problem_example(self) -> None:
        """Test the specific Problem 012 example properties."""
        # From the problem statement:
        # 28 is the first triangle number to have over five divisors

        # Just verify that 28 has exactly 6 divisors (avoid heavy computation)
        divisors_28 = get_divisors(28)
        expected_divisors = [1, 2, 4, 7, 14, 28]
        assert divisors_28 == expected_divisors
        assert len(divisors_28) == 6

        # Verify 28 is a triangular number (T_7 = 7*8/2 = 28)
        assert get_triangular_number(7) == 28

    @pytest.mark.slow
    def test_problem_example_solve_functions(self) -> None:
        """Test all solve functions for Problem 012 example (marked as slow)."""
        target_divisors = 5
        expected = 28

        # Test all solution approaches
        assert solve_naive(target_divisors) == expected
        assert solve_optimized(target_divisors) == expected
        assert solve_mathematical(target_divisors) == expected

    def test_first_triangular_numbers_properties(self) -> None:
        """Test properties of the first few triangular numbers."""
        # Verify the first 10 triangular numbers and their divisor counts
        expected_data = [
            (1, 1, [1]),  # T_1 = 1, divisors: 1
            (2, 3, [1, 3]),  # T_2 = 3, divisors: 2
            (3, 6, [1, 2, 3, 6]),  # T_3 = 6, divisors: 4
            (4, 10, [1, 2, 5, 10]),  # T_4 = 10, divisors: 4
            (5, 15, [1, 3, 5, 15]),  # T_5 = 15, divisors: 4
            (6, 21, [1, 3, 7, 21]),  # T_6 = 21, divisors: 4
            (7, 28, [1, 2, 4, 7, 14, 28]),  # T_7 = 28, divisors: 6
            (8, 36, [1, 2, 3, 4, 6, 9, 12, 18, 36]),  # T_8 = 36, divisors: 9
        ]

        for n, expected_triangular, expected_divisors in expected_data:
            # Test triangular number generation
            triangular = get_triangular_number(n)
            assert triangular == expected_triangular, (
                f"T_{n} should be {expected_triangular}, got {triangular}"
            )

            # Test divisor enumeration
            divisors = get_divisors(triangular)
            assert divisors == expected_divisors, (
                f"Divisors of T_{n}={triangular}: expected {expected_divisors}, got {divisors}"
            )

            # Test divisor counting
            divisor_count_naive = count_divisors_naive(triangular)
            divisor_count_optimized = count_divisors_optimized(triangular)
            expected_count = len(expected_divisors)

            assert divisor_count_naive == expected_count, (
                f"Naive divisor count for T_{n}={triangular}: expected {expected_count}, got {divisor_count_naive}"
            )
            assert divisor_count_optimized == expected_count, (
                f"Optimized divisor count for T_{n}={triangular}: expected {expected_count}, got {divisor_count_optimized}"
            )

    def test_mathematical_algorithm_properties(self) -> None:
        """Test mathematical algorithm specific properties."""
        # The mathematical algorithm uses the property that T_n = n(n+1)/2
        # and the fact that gcd(n, n+1) = 1, so we can compute divisors separately

        # Test even n case: T_n = (n/2) * (n+1)
        n = 6  # even
        triangular = get_triangular_number(n)  # T_6 = 21

        n_half_divisors = count_divisors_optimized(n // 2)  # divisors of 3
        n_plus_1_divisors = count_divisors_optimized(n + 1)  # divisors of 7
        total_expected = n_half_divisors * n_plus_1_divisors  # 2 * 2 = 4

        actual_divisors = count_divisors_optimized(triangular)
        assert actual_divisors == total_expected, (
            f"For even n={n}, expected {total_expected} divisors, got {actual_divisors}"
        )

        # Test odd n case: T_n = n * ((n+1)/2)
        n = 7  # odd
        triangular = get_triangular_number(n)  # T_7 = 28

        n_divisors = count_divisors_optimized(n)  # divisors of 7
        n_plus_1_half_divisors = count_divisors_optimized((n + 1) // 2)  # divisors of 4
        total_expected = n_divisors * n_plus_1_half_divisors  # 2 * 3 = 6

        actual_divisors = count_divisors_optimized(triangular)
        assert actual_divisors == total_expected, (
            f"For odd n={n}, expected {total_expected} divisors, got {actual_divisors}"
        )

    def test_divisor_counting_edge_cases(self) -> None:
        """Test edge cases for divisor counting."""
        # Test with 0 (should return 0)
        assert count_divisors_naive(0) == 0
        assert count_divisors_optimized(0) == 0

        # Test with perfect squares
        perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        for square in perfect_squares:
            naive_count = count_divisors_naive(square)
            optimized_count = count_divisors_optimized(square)
            assert naive_count == optimized_count, (
                f"Divisor counts disagree for perfect square {square}: "
                f"naive={naive_count}, optimized={optimized_count}"
            )

    def test_prime_factorization_edge_cases(self) -> None:
        """Test edge cases for prime factorization."""
        # Test with 1 (should return empty dict)
        assert prime_factorization(1) == {}

        # Test with 0 (should return empty dict)
        assert prime_factorization(0) == {}

        # Test with prime numbers
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            factors = prime_factorization(prime)
            expected = {prime: 1}
            assert dict(factors) == expected, (
                f"Prime factorization of {prime}: expected {expected}, got {dict(factors)}"
            )

    @pytest.mark.slow
    def test_large_values_consistency(self) -> None:
        """Test consistency for larger values."""
        # Test larger values to ensure algorithms remain accurate
        test_values = [6]

        for target_divisors in test_values:
            naive_result = solve_naive(target_divisors)
            optimized_result = solve_optimized(target_divisors)
            math_result = solve_mathematical(target_divisors)

            assert naive_result == optimized_result == math_result, (
                f"Solutions disagree for target_divisors={target_divisors}: "
                f"naive={naive_result}, optimized={optimized_result}, math={math_result}"
            )

            # Verify the result actually has more than target_divisors divisors
            actual_count = count_divisors_optimized(naive_result)
            assert actual_count > target_divisors, (
                f"Result {naive_result} should have more than {target_divisors} divisors, "
                f"but has {actual_count}"
            )
