"""Tests for Problem 047: Distinct primes factors."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_047 import (
    count_distinct_prime_factors,
    count_distinct_prime_factors_cached,
    get_consecutive_with_factors,
    get_prime_factors,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem047:
    """Test cases for Problem 047."""

    @pytest.mark.parametrize(
        "target_factors,expected",
        [
            (2, 14),  # First two consecutive numbers with 2 distinct prime factors each
            (
                3,
                644,
            ),  # First three consecutive numbers with 3 distinct prime factors each
        ],
    )
    def test_solve_naive(self, target_factors: int, expected: int) -> None:
        """Test the naive solution."""
        result = solve_naive(target_factors)
        assert result == expected, (
            f"Expected {expected}, got {result} for target_factors={target_factors}"
        )

    @pytest.mark.parametrize(
        "target_factors,expected",
        [
            (2, 14),  # First two consecutive numbers with 2 distinct prime factors each
            (
                3,
                644,
            ),  # First three consecutive numbers with 3 distinct prime factors each
        ],
    )
    def test_solve_optimized(self, target_factors: int, expected: int) -> None:
        """Test the optimized solution."""
        result = solve_optimized(target_factors)
        assert result == expected, (
            f"Expected {expected}, got {result} for target_factors={target_factors}"
        )

    @pytest.mark.parametrize(
        "target_factors,expected",
        [
            (2, 14),  # First two consecutive numbers with 2 distinct prime factors each
            (
                3,
                644,
            ),  # First three consecutive numbers with 3 distinct prime factors each
        ],
    )
    def test_solve_mathematical(self, target_factors: int, expected: int) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(target_factors)
        assert result == expected, (
            f"Expected {expected}, got {result} for target_factors={target_factors}"
        )

    @pytest.mark.parametrize("target_factors", [2, 3])
    def test_all_solutions_agree(self, target_factors: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(target_factors)
        optimized_result = solve_optimized(target_factors)
        math_result = solve_mathematical(target_factors)

        assert naive_result == optimized_result == math_result, (
            f"Solutions disagree for target_factors={target_factors}: "
            f"naive={naive_result}, optimized={optimized_result}, "
            f"math={math_result}"
        )

    @pytest.mark.parametrize(
        "n,expected_factors",
        [
            (2, {2}),
            (3, {3}),
            (4, {2}),
            (5, {5}),
            (6, {2, 3}),
            (7, {7}),
            (8, {2}),
            (9, {3}),
            (10, {2, 5}),
            (12, {2, 3}),
            (14, {2, 7}),
            (15, {3, 5}),
            (30, {2, 3, 5}),
            (644, {2, 7, 23}),
            (645, {3, 5, 43}),
            (646, {2, 17, 19}),
        ],
    )
    def test_get_prime_factors(self, n: int, expected_factors: set[int]) -> None:
        """Test prime factor extraction."""
        result = get_prime_factors(n)
        assert result == expected_factors, (
            f"Expected {expected_factors}, got {result} for n={n}"
        )

    @pytest.mark.parametrize(
        "n,expected_count",
        [
            (2, 1),  # 2
            (3, 1),  # 3
            (4, 1),  # 2²
            (5, 1),  # 5
            (6, 2),  # 2×3
            (7, 1),  # 7
            (8, 1),  # 2³
            (9, 1),  # 3²
            (10, 2),  # 2×5
            (12, 2),  # 2²×3
            (14, 2),  # 2×7
            (15, 2),  # 3×5
            (30, 3),  # 2×3×5
            (210, 4),  # 2×3×5×7
            (644, 3),  # 2²×7×23
            (645, 3),  # 3×5×43
            (646, 3),  # 2×17×19
        ],
    )
    def test_count_distinct_prime_factors(self, n: int, expected_count: int) -> None:
        """Test distinct prime factor counting."""
        result = count_distinct_prime_factors(n)
        assert result == expected_count, (
            f"Expected {expected_count}, got {result} for n={n}"
        )

        # Test cached version gives same result
        cached_result = count_distinct_prime_factors_cached(n)
        assert cached_result == expected_count, f"Cached version failed for n={n}"

    def test_consecutive_verification(self) -> None:
        """Test verification of consecutive numbers with distinct prime factors."""
        # Test 2 consecutive numbers with 2 distinct prime factors each
        consecutive_2 = get_consecutive_with_factors(14, 2)
        assert len(consecutive_2) == 2
        assert consecutive_2[0] == (14, {2, 7})
        assert consecutive_2[1] == (15, {3, 5})

        # Test 3 consecutive numbers with 3 distinct prime factors each
        consecutive_3 = get_consecutive_with_factors(644, 3)
        assert len(consecutive_3) == 3
        assert consecutive_3[0] == (644, {2, 7, 23})
        assert consecutive_3[1] == (645, {3, 5, 43})
        assert consecutive_3[2] == (646, {2, 17, 19})

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with target_factors = 1 (numbers with exactly 1 prime factor)
        # These are prime powers: 2, 3, 4, 5, 7, 8, 9, ...
        # First consecutive pair: 8, 9 (2³, 3²)
        result = solve_naive(1)
        consecutive = get_consecutive_with_factors(result, 1)
        for num, factors in consecutive:
            assert len(factors) == 1, (
                f"Number {num} should have exactly 1 distinct prime factor"
            )

    def test_problem_examples(self) -> None:
        """Test the specific examples from the problem statement."""
        # Example 1: First two consecutive numbers with 2 distinct prime factors
        # 14 = 2 × 7, 15 = 3 × 5
        assert count_distinct_prime_factors(14) == 2
        assert count_distinct_prime_factors(15) == 2
        assert get_prime_factors(14) == {2, 7}
        assert get_prime_factors(15) == {3, 5}

        # Example 2: First three consecutive numbers with 3 distinct prime factors
        # 644 = 2² × 7 × 23, 645 = 3 × 5 × 43, 646 = 2 × 17 × 19
        assert count_distinct_prime_factors(644) == 3
        assert count_distinct_prime_factors(645) == 3
        assert count_distinct_prime_factors(646) == 3
        assert get_prime_factors(644) == {2, 7, 23}
        assert get_prime_factors(645) == {3, 5, 43}
        assert get_prime_factors(646) == {2, 17, 19}

    def test_prime_factor_properties(self) -> None:
        """Test properties of prime factor functions."""
        # Test that prime numbers have exactly 1 distinct prime factor
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for p in primes:
            assert count_distinct_prime_factors(p) == 1
            assert get_prime_factors(p) == {p}

        # Test that prime powers have exactly 1 distinct prime factor
        prime_powers = [4, 8, 9, 25, 27, 49, 121]  # 2², 2³, 3², 5², 3³, 7², 11²
        for pp in prime_powers:
            assert count_distinct_prime_factors(pp) == 1

        # Test that products of distinct primes have the correct count
        assert count_distinct_prime_factors(6) == 2  # 2×3
        assert count_distinct_prime_factors(30) == 3  # 2×3×5
        assert count_distinct_prime_factors(210) == 4  # 2×3×5×7

    def test_caching_efficiency(self) -> None:
        """Test that caching works correctly."""
        # Clear cache by creating a new test
        test_numbers = [100, 101, 102, 103, 104]

        # First calls (cache misses)
        results1 = [count_distinct_prime_factors_cached(n) for n in test_numbers]

        # Second calls (cache hits)
        results2 = [count_distinct_prime_factors_cached(n) for n in test_numbers]

        # Should get same results
        assert results1 == results2

        # Verify against non-cached version
        results_non_cached = [count_distinct_prime_factors(n) for n in test_numbers]
        assert results1 == results_non_cached

    @pytest.mark.slow
    def test_main_problem(self) -> None:
        """Test the main problem (marked as slow)."""
        # Test with target_factors = 4 (the actual problem)
        # This is marked as slow because it may take some time
        target_factors = 4

        # Test only the optimized solution for speed
        result = solve_optimized(target_factors)

        # Verify that the result gives 4 consecutive numbers with 4 distinct prime factors each
        consecutive = get_consecutive_with_factors(result, target_factors)
        assert len(consecutive) == target_factors

        for num, factors in consecutive:
            assert len(factors) == target_factors, (
                f"Number {num} should have exactly {target_factors} distinct prime factors, "
                f"but has {len(factors)}: {factors}"
            )

        # Verify these are truly consecutive
        for i in range(1, target_factors):
            assert consecutive[i][0] == consecutive[i - 1][0] + 1, (
                f"Numbers should be consecutive: {consecutive[i - 1][0]} and {consecutive[i][0]}"
            )

    def test_small_consecutive_sequences(self) -> None:
        """Test small consecutive sequences manually."""
        # Manually verify some small sequences

        # Numbers with exactly 2 distinct prime factors:
        # 6=2×3, 10=2×5, 12=2²×3, 14=2×7, 15=3×5, 18=2×3², 20=2²×5, 21=3×7, 22=2×11, ...
        # First consecutive pair: 14, 15

        numbers_with_2_factors = []
        for n in range(2, 50):
            if count_distinct_prime_factors(n) == 2:
                numbers_with_2_factors.append(n)

        # Find first consecutive pair
        for i in range(len(numbers_with_2_factors) - 1):
            if numbers_with_2_factors[i + 1] == numbers_with_2_factors[i] + 1:
                first_consecutive_2 = numbers_with_2_factors[i]
                break
        else:
            pytest.fail("Could not find consecutive pair with 2 distinct prime factors")

        assert first_consecutive_2 == 14

    def test_factorization_accuracy(self) -> None:
        """Test accuracy of factorization for known composite numbers."""
        test_cases = [
            (12, {2, 3}),  # 2² × 3
            (18, {2, 3}),  # 2 × 3²
            (20, {2, 5}),  # 2² × 5
            (24, {2, 3}),  # 2³ × 3
            (28, {2, 7}),  # 2² × 7
            (36, {2, 3}),  # 2² × 3²
            (40, {2, 5}),  # 2³ × 5
            (42, {2, 3, 7}),  # 2 × 3 × 7
            (60, {2, 3, 5}),  # 2² × 3 × 5
            (72, {2, 3}),  # 2³ × 3²
            (84, {2, 3, 7}),  # 2² × 3 × 7
            (90, {2, 3, 5}),  # 2 × 3² × 5
            (96, {2, 3}),  # 2⁵ × 3
            (100, {2, 5}),  # 2² × 5²
        ]

        for n, expected_factors in test_cases:
            actual_factors = get_prime_factors(n)
            assert actual_factors == expected_factors, (
                f"Factorization of {n}: expected {expected_factors}, got {actual_factors}"
            )

    def test_solution_verification(self) -> None:
        """Verify solutions by checking the consecutive property."""
        for target_factors in [2, 3]:
            result = solve_optimized(target_factors)

            # Check that we have target_factors consecutive numbers
            for i in range(target_factors):
                num = result + i
                factor_count = count_distinct_prime_factors(num)
                assert factor_count == target_factors, (
                    f"Number {num} (position {i}) should have {target_factors} "
                    f"distinct prime factors, but has {factor_count}"
                )

            # Check that the previous number doesn't satisfy the condition
            if result > 2:  # Avoid going below 2
                prev_num = result - 1
                prev_count = count_distinct_prime_factors(prev_num)
                # The previous number should either not have target_factors distinct prime factors,
                # or if it does, then result-target_factors+1 should not satisfy the condition
                if prev_count == target_factors:
                    # Check if this would make a longer sequence
                    check_num = result - target_factors
                    if check_num >= 2:
                        check_count = count_distinct_prime_factors(check_num)
                        assert check_count != target_factors, (
                            f"Found earlier sequence starting at {check_num}"
                        )

    def test_boundary_conditions(self) -> None:
        """Test boundary conditions and edge cases."""
        # Test very small numbers
        small_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for n in small_numbers[1:]:  # Skip 1 as it has no prime factors
            factors = get_prime_factors(n)
            count = count_distinct_prime_factors(n)

            assert len(factors) == count, (
                f"Count mismatch for {n}: {factors} vs {count}"
            )
            assert count >= 1, (
                f"Every number > 1 should have at least 1 prime factor: {n}"
            )

            # Verify factors are actually prime and divide n
            for factor in factors:
                assert n % factor == 0, f"{factor} should divide {n}"
                assert factor >= 2, f"Prime factors should be >= 2: {factor}"

                # Simple primality check for small factors
                if factor <= 100:
                    is_prime = factor > 1 and all(
                        factor % i != 0 for i in range(2, int(factor**0.5) + 1)
                    )
                    assert is_prime, f"{factor} should be prime"

    def test_performance_characteristics(self) -> None:
        """Test performance characteristics without timing."""
        # Test that solutions work for reasonable inputs
        target_factors_list = [1, 2, 3]

        for target_factors in target_factors_list:
            # All solutions should complete and agree
            result_naive = solve_naive(target_factors)
            result_optimized = solve_optimized(target_factors)
            result_mathematical = solve_mathematical(target_factors)

            assert result_naive == result_optimized == result_mathematical, (
                f"Solutions disagree for target_factors={target_factors}"
            )

            # Result should be reasonable (not too small)
            assert result_naive >= 2, (
                f"Result should be at least 2 for target_factors={target_factors}"
            )

    def test_mathematical_properties(self) -> None:
        """Test mathematical properties of the problem."""
        # Test that as target_factors increases, the first occurrence also increases
        results = []
        for target_factors in [1, 2, 3]:
            result = solve_optimized(target_factors)
            results.append(result)

        # Results should be in ascending order (more factors = later occurrence)
        for i in range(1, len(results)):
            assert results[i] > results[i - 1], (
                f"Results should increase: target_factors={i} gives {results[i - 1]}, "
                f"target_factors={i + 1} gives {results[i]}"
            )

    def test_correctness_verification(self) -> None:
        """Final correctness verification."""
        # Verify the known examples from Project Euler

        # Example 1: First two consecutive with 2 distinct prime factors
        result_2 = solve_optimized(2)
        assert result_2 == 14
        consecutive_2 = get_consecutive_with_factors(14, 2)
        assert consecutive_2 == [(14, {2, 7}), (15, {3, 5})]

        # Example 2: First three consecutive with 3 distinct prime factors
        result_3 = solve_optimized(3)
        assert result_3 == 644
        consecutive_3 = get_consecutive_with_factors(644, 3)
        assert consecutive_3 == [
            (644, {2, 7, 23}),
            (645, {3, 5, 43}),
            (646, {2, 17, 19}),
        ]

        # Verify all numbers in sequences have correct factor counts
        for _num, factors in consecutive_2:
            assert len(factors) == 2

        for _num, factors in consecutive_3:
            assert len(factors) == 3
