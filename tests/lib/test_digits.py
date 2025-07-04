#!/usr/bin/env python3
"""Tests for digits module."""

import pytest

from problems.lib.digits import (
    are_permutations,
    concatenated_product,
    count_digits,
    digit_factorial_sum,
    digit_power_sum,
    get_digit_at_position,
    get_digit_signature,
    get_digit_signature_tuple,
    get_permutations_4digit,
    get_rotations,
    has_substring_divisibility,
    is_circular_prime_candidate,
    is_pandigital,
    is_pandigital_0_to_9,
    is_pandigital_1_to_9,
    reverse_number,
    sum_of_digits,
)


class TestDigitSignatures:
    """Test digit signature functions."""

    @pytest.mark.parametrize(
        "n,expected", [(123, "123"), (321, "123"), (1234, "1234"), (4321, "1234")]
    )
    def test_get_digit_signature(self, n: int, expected: str) -> None:
        """Test digit signature string."""
        assert get_digit_signature(n) == expected

    @pytest.mark.parametrize(
        "n,expected",
        [(123, (0, 1, 1, 1, 0, 0, 0, 0, 0, 0)), (1223, (0, 1, 2, 1, 0, 0, 0, 0, 0, 0))],
    )
    def test_get_digit_signature_tuple(self, n: int, expected: tuple) -> None:
        """Test digit signature tuple."""
        assert get_digit_signature_tuple(n) == expected


class TestPandigital:
    """Test pandigital checking functions."""

    def test_is_pandigital_1_to_9(self) -> None:
        """Test 1-9 pandigital checking."""
        assert is_pandigital_1_to_9("123456789")
        assert not is_pandigital_1_to_9("123456788")
        assert not is_pandigital_1_to_9("1234567890")

    def test_is_pandigital_0_to_9(self) -> None:
        """Test 0-9 pandigital checking."""
        assert is_pandigital_0_to_9("1234567890")
        assert not is_pandigital_0_to_9("123456789")

    @pytest.mark.parametrize(
        "n,start,end,expected",
        [(123, 1, 3, True), (124, 1, 3, False), (9876543210, 0, 9, True)],
    )
    def test_is_pandigital_general(
        self, n: int, start: int, end: int, expected: bool
    ) -> None:
        """Test general pandigital checking."""
        assert is_pandigital(n, start, end) == expected


class TestNumberManipulation:
    """Test number manipulation functions."""

    @pytest.mark.parametrize("n,expected", [(123, 321), (1000, 1), (12340, 4321)])
    def test_reverse_number(self, n: int, expected: int) -> None:
        """Test number reversal."""
        assert reverse_number(n) == expected

    def test_get_rotations(self) -> None:
        """Test getting rotations of a number."""
        rotations = get_rotations(1234)
        expected = [1234, 2341, 3412, 4123]
        assert sorted(rotations) == sorted(expected)

    def test_get_permutations_4digit(self) -> None:
        """Test getting 4-digit permutations."""
        perms = get_permutations_4digit(1234)
        assert 1234 in perms
        assert 4321 in perms
        assert len(perms) == 24  # 4! permutations

    @pytest.mark.parametrize(
        "n1,n2,expected", [(123, 321, True), (123, 124, False), (1234, 4321, True)]
    )
    def test_are_permutations(self, n1: int, n2: int, expected: bool) -> None:
        """Test permutation checking."""
        assert are_permutations(n1, n2) == expected


class TestDigitCalculations:
    """Test digit calculation functions."""

    def test_digit_factorial_sum(self) -> None:
        """Test digit factorial sum."""
        # 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
        assert digit_factorial_sum(145) == 145

    @pytest.mark.parametrize(
        "n,p,expected",
        [
            (153, 3, 153),  # 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
            (9474, 4, 9474),  # 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474
        ],
    )
    def test_digit_power_sum(self, n: int, p: int, expected: int) -> None:
        """Test digit power sum."""
        assert digit_power_sum(n, p) == expected

    @pytest.mark.parametrize("n,expected", [(123, 3), (1000, 4), (99, 2)])
    def test_count_digits(self, n: int, expected: int) -> None:
        """Test digit counting."""
        assert count_digits(n) == expected

    @pytest.mark.parametrize("n,expected", [(123, 6), (999, 27), (1000, 1)])
    def test_sum_of_digits(self, n: int, expected: int) -> None:
        """Test digit sum."""
        assert sum_of_digits(n) == expected


class TestSpecialFunctions:
    """Test special digit functions."""

    def test_concatenated_product(self) -> None:
        """Test concatenated product."""
        # 192 * (1,2,3) = 192384576
        assert concatenated_product(192, 3) == "192384576"

    @pytest.mark.parametrize("pos,expected", [(1, 1), (10, 1), (12, 1), (15, 2)])
    def test_get_digit_at_position(self, pos: int, expected: int) -> None:
        """Test getting digit at position in Champernowne's constant."""
        assert get_digit_at_position(pos) == expected

    def test_has_substring_divisibility(self) -> None:
        """Test substring divisibility property."""
        # This is specific to problem 043
        assert has_substring_divisibility("1406357289")

    def test_is_circular_prime_candidate(self) -> None:
        """Test circular prime candidate checking."""
        assert is_circular_prime_candidate(197)  # No even digits
        assert not is_circular_prime_candidate(123)  # Contains 2
