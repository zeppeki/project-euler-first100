#!/usr/bin/env python3
"""Tests for primes module."""

import pytest

from problems.lib.primes import (
    count_distinct_prime_factors,
    generate_primes,
    get_prime_factors,
    is_prime,
    is_prime_optimized,
    is_truncatable_prime,
    sieve_of_eratosthenes,
)


class TestIsPrime:
    """Test prime checking functions."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, False),
            (7, True),
            (8, False),
            (9, False),
            (10, False),
            (11, True),
            (13, True),
            (17, True),
            (19, True),
            (23, True),
            (25, False),
            (29, True),
            (31, True),
            (37, True),
            (41, True),
            (100, False),
            (101, True),
            (997, True),
            (1009, True),
        ],
    )
    def test_is_prime(self, n: int, expected: bool) -> None:
        """Test basic prime checking."""
        assert is_prime(n) == expected

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, False),
            (7, True),
            (8, False),
            (9, False),
            (10, False),
            (11, True),
            (13, True),
            (17, True),
            (19, True),
            (23, True),
            (25, False),
            (29, True),
            (31, True),
            (37, True),
            (41, True),
            (100, False),
            (101, True),
            (997, True),
            (1009, True),
        ],
    )
    def test_is_prime_optimized(self, n: int, expected: bool) -> None:
        """Test optimized prime checking."""
        assert is_prime_optimized(n) == expected

    def test_prime_functions_agree(self) -> None:
        """Test that both prime functions give same results."""
        for n in range(1, 100):
            assert is_prime(n) == is_prime_optimized(n)


class TestSieveOfEratosthenes:
    """Test sieve of Eratosthenes function."""

    def test_sieve_small_limit(self) -> None:
        """Test sieve with small limit."""
        result = sieve_of_eratosthenes(10)
        expected = [2, 3, 5, 7]
        assert result == expected

    def test_sieve_return_set(self) -> None:
        """Test sieve returning set."""
        result = sieve_of_eratosthenes(10, "set")
        expected = {2, 3, 5, 7}
        assert result == expected

    def test_sieve_return_bool_array(self) -> None:
        """Test sieve returning boolean array."""
        result = sieve_of_eratosthenes(10, "bool_array")
        # result[i] is True if i is prime
        assert result[2] is True
        assert result[3] is True
        assert result[4] is False
        assert result[5] is True
        assert result[6] is False
        assert result[7] is True


class TestGeneratePrimes:
    """Test prime generation."""

    def test_generate_primes_limit(self) -> None:
        """Test generating primes up to limit."""
        result = list(generate_primes(20))
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        assert result == expected

    def test_generate_primes_count(self) -> None:
        """Test generating first few primes."""
        result = list(generate_primes(15))
        expected = [2, 3, 5, 7, 11, 13]
        assert result == expected


class TestPrimeFactors:
    """Test prime factorization functions."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, {}),
            (2, {2: 1}),
            (4, {2: 2}),
            (8, {2: 3}),
            (12, {2: 2, 3: 1}),
            (60, {2: 2, 3: 1, 5: 1}),
            (100, {2: 2, 5: 2}),
        ],
    )
    def test_get_prime_factors(self, n: int, expected: dict[int, int]) -> None:
        """Test prime factorization."""
        result = get_prime_factors(n)
        # get_prime_factors returns a set, need to check differently for factorization
        # This is checking distinct prime factors, not full factorization
        assert result == set(expected.keys())

    @pytest.mark.parametrize(
        "n,expected", [(1, 0), (2, 1), (4, 1), (6, 2), (12, 2), (30, 3), (60, 3)]
    )
    def test_count_distinct_prime_factors(self, n: int, expected: int) -> None:
        """Test counting distinct prime factors."""
        assert count_distinct_prime_factors(n) == expected


class TestTruncatablePrimes:
    """Test truncatable prime checking."""

    def test_truncatable_primes_examples(self) -> None:
        """Test known truncatable primes."""
        # Known left-to-right truncatable primes
        assert is_truncatable_prime(2357)
        assert is_truncatable_prime(3797)

        # Non-truncatable primes
        assert not is_truncatable_prime(11)  # 1 is not prime
        assert not is_truncatable_prime(13)  # 3 -> 13 but 1 is not prime

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Single digit primes should not be considered truncatable
        for prime in [2, 3, 5, 7]:
            assert not is_truncatable_prime(prime)
