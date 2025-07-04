#!/usr/bin/env python3
"""Tests for combinatorics module."""

import pytest

from problems.lib.combinatorics import (
    combination_formula,
    get_combinations,
    get_combinations_with_replacement,
    get_permutations,
    get_permutations_with_replacement,
    multinomial_coefficient,
    permutation_formula,
)


class TestCombinations:
    """Test combination functions."""

    @pytest.mark.parametrize(
        "n,r,expected",
        [
            (5, 0, 1),
            (5, 1, 5),
            (5, 2, 10),
            (5, 3, 10),
            (5, 4, 5),
            (5, 5, 1),
            (10, 3, 120),
            (0, 0, 1),
            (5, -1, 0),
            (5, 6, 0),
        ],
    )
    def test_combination_formula(self, n: int, r: int, expected: int) -> None:
        """Test combination calculation."""
        assert combination_formula(n, r) == expected

    def test_combination_edge_cases(self) -> None:
        """Test combination edge cases."""
        assert combination_formula(-1, 2) == 0
        assert combination_formula(5, -1) == 0


class TestPermutations:
    """Test permutation functions."""

    @pytest.mark.parametrize(
        "n,r,expected",
        [
            (5, 0, 1),
            (5, 1, 5),
            (5, 2, 20),
            (5, 3, 60),
            (5, 4, 120),
            (5, 5, 120),
            (0, 0, 1),
            (5, -1, 0),
            (5, 6, 0),
        ],
    )
    def test_permutation_formula(self, n: int, r: int, expected: int) -> None:
        """Test permutation calculation."""
        assert permutation_formula(n, r) == expected


class TestGenerators:
    """Test combination and permutation generators."""

    def test_get_combinations(self) -> None:
        """Test combination generation."""
        result = list(get_combinations([1, 2, 3], 2))
        expected = [(1, 2), (1, 3), (2, 3)]
        assert result == expected

    def test_get_permutations(self) -> None:
        """Test permutation generation."""
        result = list(get_permutations([1, 2, 3], 2))
        expected_count = 6  # P(3,2) = 6
        assert len(result) == expected_count
        assert (1, 2) in result
        assert (2, 1) in result
        assert (3, 2) in result

    def test_get_combinations_with_replacement(self) -> None:
        """Test combinations with replacement."""
        result = list(get_combinations_with_replacement([1, 2], 2))
        expected = [(1, 1), (1, 2), (2, 2)]
        assert result == expected

    def test_get_permutations_with_replacement(self) -> None:
        """Test permutations with replacement."""
        result = list(get_permutations_with_replacement([1, 2], 2))
        expected = [(1, 1), (1, 2), (2, 1), (2, 2)]
        assert sorted(result) == sorted(expected)


class TestMultinomial:
    """Test multinomial coefficient."""

    def test_multinomial_coefficient(self) -> None:
        """Test multinomial coefficient calculation."""
        # multinomial(4; 2,1,1) = 4!/(2!*1!*1!) = 12
        assert multinomial_coefficient(2, 1, 1) == 12

        # multinomial(6; 2,2,2) = 6!/(2!*2!*2!) = 90
        assert multinomial_coefficient(2, 2, 2) == 90

        # Edge case: single argument
        assert multinomial_coefficient(5) == 1

    def test_multinomial_edge_cases(self) -> None:
        """Test multinomial edge cases."""
        assert multinomial_coefficient() == 1  # Empty case
        assert multinomial_coefficient(0, 0, 0) == 1  # All zeros
