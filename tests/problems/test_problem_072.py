#!/usr/bin/env python3
"""
Tests for Problem 072: Counting fractions
"""

from math import gcd

import pytest

from problems.problem_072 import (
    analyze_totient_distribution,
    count_reduced_fractions_range,
    euler_totient_individual,
    euler_totient_prime_factorization,
    euler_totient_sieve,
    get_mathematical_properties,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    solve_sieve_optimized,
)


def verify_small_example() -> tuple[int, list[tuple[int, int]]]:
    """
    問題文の小さな例 (d ≤ 8) を検証
    返り値: (count, fractions)
    """
    fractions = []
    for d in range(2, 9):
        for n in range(1, d):
            if gcd(n, d) == 1:
                fractions.append((n, d))
    return len(fractions), fractions


class TestEulerTotientFunctions:
    """Test Euler's totient function implementations"""

    def test_euler_totient_individual_basic(self) -> None:
        """Test individual totient function with basic cases"""
        assert euler_totient_individual(1) == 1
        assert euler_totient_individual(2) == 1
        assert euler_totient_individual(3) == 2
        assert euler_totient_individual(4) == 2
        assert euler_totient_individual(5) == 4
        assert euler_totient_individual(6) == 2

    def test_euler_totient_individual_primes(self) -> None:
        """Test individual totient function with prime numbers"""
        primes = [7, 11, 13, 17, 19, 23]
        for p in primes:
            assert euler_totient_individual(p) == p - 1

    def test_euler_totient_individual_prime_powers(self) -> None:
        """Test individual totient function with prime powers"""
        # φ(p^k) = p^(k-1)(p-1)
        assert euler_totient_individual(4) == 2  # 2^2, φ(4) = 2^1 * 1 = 2
        assert euler_totient_individual(8) == 4  # 2^3, φ(8) = 2^2 * 1 = 4
        assert euler_totient_individual(9) == 6  # 3^2, φ(9) = 3^1 * 2 = 6
        assert euler_totient_individual(25) == 20  # 5^2, φ(25) = 5^1 * 4 = 20

    def test_euler_totient_prime_factorization_basic(self) -> None:
        """Test prime factorization-based totient function"""
        assert euler_totient_prime_factorization(1) == 1
        assert euler_totient_prime_factorization(2) == 1
        assert euler_totient_prime_factorization(3) == 2
        assert euler_totient_prime_factorization(4) == 2
        assert euler_totient_prime_factorization(5) == 4
        assert euler_totient_prime_factorization(6) == 2

    def test_euler_totient_prime_factorization_larger(self) -> None:
        """Test prime factorization-based totient function with larger numbers"""
        assert euler_totient_prime_factorization(12) == 4  # 12 = 2^2 * 3
        assert euler_totient_prime_factorization(15) == 8  # 15 = 3 * 5
        assert euler_totient_prime_factorization(16) == 8  # 16 = 2^4
        assert euler_totient_prime_factorization(18) == 6  # 18 = 2 * 3^2
        assert euler_totient_prime_factorization(20) == 8  # 20 = 2^2 * 5

    def test_totient_functions_consistency(self) -> None:
        """Test that both totient implementations give same results"""
        for n in range(1, 31):
            individual = euler_totient_individual(n)
            factorization = euler_totient_prime_factorization(n)
            assert individual == factorization, (
                f"Mismatch for n={n}: {individual} vs {factorization}"
            )

    def test_euler_totient_sieve_basic(self) -> None:
        """Test sieve-based totient function computation"""
        limit = 20
        phi_values = euler_totient_sieve(limit)

        # Check specific values
        assert phi_values[1] == 1
        assert phi_values[2] == 1
        assert phi_values[3] == 2
        assert phi_values[4] == 2
        assert phi_values[5] == 4
        assert phi_values[6] == 2
        assert phi_values[7] == 6
        assert phi_values[8] == 4
        assert phi_values[9] == 6
        assert phi_values[10] == 4

    def test_euler_totient_sieve_consistency(self) -> None:
        """Test that sieve method matches individual computation"""
        limit = 50
        phi_values = euler_totient_sieve(limit)

        for n in range(1, limit + 1):
            individual = euler_totient_prime_factorization(n)
            assert phi_values[n] == individual, (
                f"Mismatch for n={n}: {phi_values[n]} vs {individual}"
            )


class TestSolutionMethods:
    """Test all solution methods"""

    def test_small_example_verification(self) -> None:
        """Test the small example from the problem statement"""
        count, fractions = verify_small_example()
        assert count == 21

        # Check that all fractions are in reduced form
        for n, d in fractions:
            assert gcd(n, d) == 1, f"Fraction {n}/{d} is not reduced"
            assert n < d, f"Fraction {n}/{d} is not proper"

    def test_solve_naive_small(self) -> None:
        """Test naive solution with small inputs"""
        assert solve_naive(2) == 1  # Only 1/2
        assert solve_naive(3) == 3  # 1/2, 1/3, 2/3
        assert solve_naive(4) == 5  # 1/2, 1/3, 2/3, 1/4, 3/4
        assert solve_naive(8) == 21  # As per problem statement

    def test_solve_optimized_small(self) -> None:
        """Test optimized solution with small inputs"""
        assert solve_optimized(2) == 1
        assert solve_optimized(3) == 3
        assert solve_optimized(4) == 5
        assert solve_optimized(8) == 21

    def test_solve_mathematical_small(self) -> None:
        """Test mathematical solution with small inputs"""
        assert solve_mathematical(2) == 1
        assert solve_mathematical(3) == 3
        assert solve_mathematical(4) == 5
        assert solve_mathematical(8) == 21

    def test_solve_sieve_optimized_small(self) -> None:
        """Test sieve optimized solution with small inputs"""
        assert solve_sieve_optimized(2) == 1
        assert solve_sieve_optimized(3) == 3
        assert solve_sieve_optimized(4) == 5
        assert solve_sieve_optimized(8) == 21

    def test_all_solutions_consistent(self) -> None:
        """Test that all solution methods give consistent results"""
        test_limits = [10, 20, 50, 100]

        for limit in test_limits:
            naive = solve_naive(limit)
            optimized = solve_optimized(limit)
            mathematical = solve_mathematical(limit)
            sieve_opt = solve_sieve_optimized(limit)

            assert naive == optimized == mathematical == sieve_opt, (
                f"Inconsistent results for limit={limit}: {naive}, {optimized}, {mathematical}, {sieve_opt}"
            )

    def test_solution_edge_cases(self) -> None:
        """Test solution methods with edge cases"""
        # Test with limit < 2
        assert solve_naive(1) == 0
        assert solve_optimized(1) == 0
        assert solve_mathematical(1) == 0
        assert solve_sieve_optimized(1) == 0

        # Test with limit = 0
        assert solve_mathematical(0) == 0
        assert solve_sieve_optimized(0) == 0


class TestUtilityFunctions:
    """Test utility functions"""

    def test_count_reduced_fractions_range(self) -> None:
        """Test counting reduced fractions in a range"""
        # Test single denominator
        assert count_reduced_fractions_range(2, 2) == 1  # Only 1/2
        assert count_reduced_fractions_range(3, 3) == 2  # 1/3, 2/3
        assert count_reduced_fractions_range(4, 4) == 2  # 1/4, 3/4

        # Test ranges
        assert count_reduced_fractions_range(2, 4) == 5  # 1/2, 1/3, 2/3, 1/4, 3/4
        assert (
            count_reduced_fractions_range(5, 8) == 16
        )  # φ(5) + φ(6) + φ(7) + φ(8) = 4 + 2 + 6 + 4

    def test_count_reduced_fractions_range_edge_cases(self) -> None:
        """Test range counting with edge cases"""
        # Invalid range
        assert count_reduced_fractions_range(5, 3) == 0

        # Range starting below 2
        assert count_reduced_fractions_range(0, 3) == 3
        assert count_reduced_fractions_range(1, 3) == 3

    def test_analyze_totient_distribution(self) -> None:
        """Test totient distribution analysis"""
        analysis = analyze_totient_distribution(20)

        assert "total_count" in analysis
        assert "max_phi" in analysis
        assert "min_phi" in analysis
        assert "average_phi" in analysis

        # Check that total_count matches direct calculation
        expected_total = solve_mathematical(20)
        assert analysis["total_count"] == expected_total

        # Check that min_phi is 1 (φ(2) = 1)
        assert analysis["min_phi"] == 1

    def test_get_mathematical_properties(self) -> None:
        """Test mathematical properties extraction"""
        # Test with prime number
        props_7 = get_mathematical_properties(7)
        assert props_7["n"] == 7
        assert props_7["phi_n"] == 6
        assert props_7["prime_factors"] == [7]
        assert props_7["is_prime"] is True
        assert props_7["is_prime_power"] is True

        # Test with composite number
        props_12 = get_mathematical_properties(12)
        assert props_12["n"] == 12
        assert props_12["phi_n"] == 4
        assert set(props_12["prime_factors"]) == {2, 3}
        assert props_12["is_prime"] is False
        assert props_12["is_prime_power"] is False

        # Test with prime power
        props_8 = get_mathematical_properties(8)
        assert props_8["n"] == 8
        assert props_8["phi_n"] == 4
        assert props_8["prime_factors"] == [2]
        assert props_8["is_prime"] is False
        assert props_8["is_prime_power"] is True


class TestTotientProperties:
    """Test mathematical properties of totient function"""

    def test_totient_prime_property(self) -> None:
        """Test φ(p) = p - 1 for primes"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for p in primes:
            assert euler_totient_prime_factorization(p) == p - 1

    def test_totient_prime_power_property(self) -> None:
        """Test φ(p^k) = p^(k-1)(p-1) for prime powers"""
        test_cases = [
            (2, 2, 2),  # φ(4) = 2
            (2, 3, 4),  # φ(8) = 4
            (2, 4, 8),  # φ(16) = 8
            (3, 2, 6),  # φ(9) = 6
            (3, 3, 18),  # φ(27) = 18
            (5, 2, 20),  # φ(25) = 20
        ]

        for p, k, expected in test_cases:
            n = p**k
            result = euler_totient_prime_factorization(n)
            assert result == expected, (
                f"φ({p}^{k}) = φ({n}) should be {expected}, got {result}"
            )

    def test_totient_multiplicative_property(self) -> None:
        """Test φ(mn) = φ(m)φ(n) when gcd(m,n) = 1"""
        test_pairs = [
            (3, 5),  # φ(15) = φ(3)φ(5) = 2 * 4 = 8
            (4, 9),  # φ(36) = φ(4)φ(9) = 2 * 6 = 12
            (7, 8),  # φ(56) = φ(7)φ(8) = 6 * 4 = 24
            (9, 16),  # φ(144) = φ(9)φ(16) = 6 * 8 = 48
        ]

        for m, n in test_pairs:
            if gcd(m, n) == 1:
                mn = m * n
                phi_m = euler_totient_prime_factorization(m)
                phi_n = euler_totient_prime_factorization(n)
                phi_mn = euler_totient_prime_factorization(mn)

                assert phi_mn == phi_m * phi_n, (
                    f"φ({m}×{n}) = φ({mn}) should be {phi_m}×{phi_n} = {phi_m * phi_n}, got {phi_mn}"
                )

    def test_totient_sum_property(self) -> None:
        """Test sum of φ(d) for d|n equals n"""
        # For small numbers, sum of φ(d) over all divisors d of n equals n
        test_numbers = [6, 12, 18, 24, 30]

        for n in test_numbers:
            # Find all divisors of n
            divisors = []
            for i in range(1, n + 1):
                if n % i == 0:
                    divisors.append(i)

            # Sum φ(d) for all divisors d
            total = sum(euler_totient_prime_factorization(d) for d in divisors)
            assert total == n, (
                f"Sum of φ(d) for divisors of {n} should be {n}, got {total}"
            )


class TestPerformanceAndScaling:
    """Test performance characteristics and scaling"""

    def test_sieve_vs_individual_medium(self) -> None:
        """Test sieve method vs individual computation for medium range"""
        limit = 1000

        # Compute using sieve
        phi_sieve = euler_totient_sieve(limit)
        sieve_total = sum(phi_sieve[2 : limit + 1])

        # Compute using mathematical solution
        math_total = solve_mathematical(limit)

        assert sieve_total == math_total

    @pytest.mark.slow
    def test_final_answer_verification(self) -> None:
        """Test the final answer for the actual problem"""
        # This tests the actual problem: d ≤ 1,000,000
        result = solve_mathematical(1000000)
        assert result == 303963552391

    def test_scaling_behavior(self) -> None:
        """Test that results scale appropriately"""
        limits = [10, 100, 1000]
        results = []

        for limit in limits:
            result = solve_mathematical(limit)
            results.append(result)

        # Results should be increasing
        assert results[0] < results[1] < results[2]

        # Growth should be reasonable (roughly quadratic)
        # This is a rough check, not exact
        ratio1 = results[1] / results[0]
        ratio2 = results[2] / results[1]
        assert ratio1 > 5  # Should grow significantly
        assert ratio2 > 5  # Should continue growing


class TestErrorHandling:
    """Test error handling and edge cases"""

    def test_zero_and_negative_inputs(self) -> None:
        """Test handling of zero and negative inputs"""
        # Mathematical solution should handle these gracefully
        assert solve_mathematical(0) == 0
        assert solve_sieve_optimized(0) == 0

        # Totient function edge cases
        assert euler_totient_prime_factorization(0) == 0
        assert euler_totient_prime_factorization(1) == 1

    def test_large_prime_totient(self) -> None:
        """Test totient function with larger primes"""
        large_primes = [97, 101, 103, 107, 109, 113]
        for p in large_primes:
            assert euler_totient_prime_factorization(p) == p - 1

    def test_boundary_conditions(self) -> None:
        """Test boundary conditions for all functions"""
        # Test with limit = 2 (minimum meaningful case)
        assert solve_mathematical(2) == 1
        assert solve_sieve_optimized(2) == 1

        # Test range functions with boundary values
        assert count_reduced_fractions_range(2, 2) == 1
        assert count_reduced_fractions_range(1, 1) == 0  # No proper fractions with d=1
