#!/usr/bin/env python3
"""Tests for math_utils module."""

import pytest

from problems.lib.math_utils import (
    count_divisors,
    factorial,
    factorial_builtin,
    fibonacci,
    gcd,
    get_divisors,
    get_hexagonal_number,
    get_pentagonal_number,
    get_proper_divisors_sum,
    get_triangular_number,
    is_abundant,
    is_palindrome,
    lcm,
    prime_factorization,
)


class TestBasicMath:
    """Test basic mathematical functions."""

    @pytest.mark.parametrize(
        "a,b,expected", [(12, 8, 4), (15, 10, 5), (7, 13, 1), (0, 5, 5), (5, 0, 5)]
    )
    def test_gcd(self, a: int, b: int, expected: int) -> None:
        """Test greatest common divisor."""
        assert gcd(a, b) == expected

    @pytest.mark.parametrize(
        "a,b,expected", [(12, 8, 24), (15, 10, 30), (7, 13, 91), (0, 5, 0), (5, 0, 0)]
    )
    def test_lcm(self, a: int, b: int, expected: int) -> None:
        """Test least common multiple."""
        assert lcm(a, b) == expected

    @pytest.mark.parametrize(
        "n,expected", [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720)]
    )
    def test_factorial(self, n: int, expected: int) -> None:
        """Test factorial calculation."""
        assert factorial(n) == expected
        assert factorial_builtin(n) == expected


class TestDivisors:
    """Test divisor functions."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, [1]),
            (6, [1, 2, 3, 6]),
            (12, [1, 2, 3, 4, 6, 12]),
            (28, [1, 2, 4, 7, 14, 28]),
        ],
    )
    def test_get_divisors(self, n: int, expected: list[int]) -> None:
        """Test getting all divisors."""
        result = get_divisors(n)
        assert sorted(result) == sorted(expected)

    @pytest.mark.parametrize("n,expected", [(1, 1), (6, 4), (12, 6), (28, 6), (100, 9)])
    def test_count_divisors(self, n: int, expected: int) -> None:
        """Test counting divisors."""
        assert count_divisors(n) == expected

    @pytest.mark.parametrize(
        "n,expected", [(1, 0), (6, 6), (12, 16), (28, 28), (220, 284), (284, 220)]
    )
    def test_get_proper_divisors_sum(self, n: int, expected: int) -> None:
        """Test sum of proper divisors."""
        assert get_proper_divisors_sum(n) == expected

    @pytest.mark.parametrize(
        "n,expected",
        [(1, False), (6, False), (12, True), (18, True), (20, True), (28, False)],
    )
    def test_is_abundant(self, n: int, expected: bool) -> None:
        """Test abundant number checking."""
        assert is_abundant(n) == expected


class TestPalindrome:
    """Test palindrome functions."""

    @pytest.mark.parametrize(
        "value,expected",
        [(121, True), (123, False), (1221, True), ("aba", True), ("abc", False)],
    )
    def test_is_palindrome(self, value: int | str, expected: bool) -> None:
        """Test palindrome checking."""
        assert is_palindrome(value) == expected


class TestSequences:
    """Test sequence functions."""

    @pytest.mark.parametrize(
        "n,expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (10, 55)]
    )
    def test_fibonacci(self, n: int, expected: int) -> None:
        """Test Fibonacci sequence."""
        assert fibonacci(n) == expected

    @pytest.mark.parametrize(
        "n,expected", [(1, 1), (2, 3), (3, 6), (4, 10), (5, 15), (10, 55)]
    )
    def test_triangular_number(self, n: int, expected: int) -> None:
        """Test triangular numbers."""
        assert get_triangular_number(n) == expected

    @pytest.mark.parametrize("n,expected", [(1, 1), (2, 5), (3, 12), (4, 22), (5, 35)])
    def test_pentagonal_number(self, n: int, expected: int) -> None:
        """Test pentagonal numbers."""
        assert get_pentagonal_number(n) == expected

    @pytest.mark.parametrize("n,expected", [(1, 1), (2, 6), (3, 15), (4, 28), (5, 45)])
    def test_hexagonal_number(self, n: int, expected: int) -> None:
        """Test hexagonal numbers."""
        assert get_hexagonal_number(n) == expected


class TestPrimeFactorization:
    """Test prime factorization in math_utils."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (1, {}),
            (2, {2: 1}),
            (4, {2: 2}),
            (12, {2: 2, 3: 1}),
            (60, {2: 2, 3: 1, 5: 1}),
        ],
    )
    def test_prime_factorization(self, n: int, expected: dict[int, int]) -> None:
        """Test prime factorization function."""
        result = prime_factorization(n)
        assert dict(result) == expected
