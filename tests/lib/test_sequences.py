#!/usr/bin/env python3
"""Tests for sequences module."""

import pytest

from problems.lib.sequences import (
    fibonacci_generator,
    generate_heptagonal,
    generate_hexagonal,
    generate_octagonal,
    generate_pentagonal,
    generate_square,
    generate_triangle,
    hexagonal_generator,
    is_hexagonal_number,
    is_pentagonal_number,
    is_triangle_number,
    pentagonal_generator,
    triangle_generator,
)


class TestPolygonalNumbers:
    """Test polygonal number generation."""

    @pytest.mark.parametrize(
        "n,expected", [(1, 1), (2, 3), (3, 6), (4, 10), (5, 15), (10, 55)]
    )
    def test_generate_triangle(self, n: int, expected: int) -> None:
        """Test triangular number generation."""
        assert generate_triangle(n) == expected

    @pytest.mark.parametrize("n,expected", [(1, 1), (2, 5), (3, 12), (4, 22), (5, 35)])
    def test_generate_pentagonal(self, n: int, expected: int) -> None:
        """Test pentagonal number generation."""
        assert generate_pentagonal(n) == expected

    @pytest.mark.parametrize("n,expected", [(1, 1), (2, 6), (3, 15), (4, 28), (5, 45)])
    def test_generate_hexagonal(self, n: int, expected: int) -> None:
        """Test hexagonal number generation."""
        assert generate_hexagonal(n) == expected

    @pytest.mark.parametrize("n,expected", [(1, 1), (2, 8), (3, 21), (4, 40), (5, 65)])
    def test_generate_octagonal(self, n: int, expected: int) -> None:
        """Test octagonal number generation."""
        assert generate_octagonal(n) == expected

    @pytest.mark.parametrize("n,expected", [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
    def test_generate_square(self, n: int, expected: int) -> None:
        """Test square number generation."""
        assert generate_square(n) == expected

    @pytest.mark.parametrize("n,expected", [(1, 1), (2, 7), (3, 18), (4, 34), (5, 55)])
    def test_generate_heptagonal(self, n: int, expected: int) -> None:
        """Test heptagonal number generation."""
        assert generate_heptagonal(n) == expected


class TestSequenceGenerators:
    """Test sequence generators."""

    def test_fibonacci_generator(self) -> None:
        """Test Fibonacci sequence generator."""
        fib_sequence = list(fibonacci_generator(20))
        expected = [1, 1, 2, 3, 5, 8, 13]
        assert fib_sequence == expected

    def test_triangle_generator(self) -> None:
        """Test triangular number generator."""
        triangles = list(triangle_generator(20))
        expected = [1, 3, 6, 10, 15]
        assert triangles == expected

    def test_pentagonal_generator(self) -> None:
        """Test pentagonal number generator."""
        pentagons = list(pentagonal_generator(20))
        expected = [1, 5, 12]
        assert pentagons == expected

    def test_hexagonal_generator(self) -> None:
        """Test hexagonal number generator."""
        hexagons = list(hexagonal_generator(20))
        expected = [1, 6, 15]
        assert hexagons == expected


class TestNumberChecking:
    """Test number type checking functions."""

    @pytest.mark.parametrize(
        "x,expected",
        [
            (1, True),
            (3, True),
            (6, True),
            (10, True),
            (15, True),
            (2, False),
            (4, False),
            (5, False),
            (7, False),
            (8, False),
        ],
    )
    def test_is_triangle_number(self, x: int, expected: bool) -> None:
        """Test triangular number checking."""
        assert is_triangle_number(x) == expected

    @pytest.mark.parametrize(
        "x,expected",
        [
            (1, True),
            (5, True),
            (12, True),
            (22, True),
            (35, True),
            (2, False),
            (3, False),
            (4, False),
            (6, False),
            (7, False),
        ],
    )
    def test_is_pentagonal_number(self, x: int, expected: bool) -> None:
        """Test pentagonal number checking."""
        assert is_pentagonal_number(x) == expected

    @pytest.mark.parametrize(
        "x,expected",
        [
            (1, True),
            (6, True),
            (15, True),
            (28, True),
            (45, True),
            (2, False),
            (3, False),
            (4, False),
            (5, False),
            (7, False),
        ],
    )
    def test_is_hexagonal_number(self, x: int, expected: bool) -> None:
        """Test hexagonal number checking."""
        assert is_hexagonal_number(x) == expected

    def test_consistency_between_generators_and_checkers(self) -> None:
        """Test that generators and checkers are consistent."""
        # Generate first 10 triangular numbers and verify they pass the checker
        for n in range(1, 11):
            triangle_num = generate_triangle(n)
            assert is_triangle_number(triangle_num)

        # Same for pentagonal
        for n in range(1, 11):
            pentagonal_num = generate_pentagonal(n)
            assert is_pentagonal_number(pentagonal_num)

        # Same for hexagonal
        for n in range(1, 11):
            hexagonal_num = generate_hexagonal(n)
            assert is_hexagonal_number(hexagonal_num)


class TestEdgeCases:
    """Test edge cases for sequence functions."""

    def test_negative_inputs(self) -> None:
        """Test behavior with negative inputs."""
        # Most functions should handle negative inputs gracefully
        assert generate_triangle(0) == 0
        assert not is_triangle_number(0)
        assert not is_triangle_number(-1)

    def test_large_numbers(self) -> None:
        """Test with larger numbers."""
        # Test that functions work with reasonably large inputs
        large_triangle = generate_triangle(1000)
        assert is_triangle_number(large_triangle)

        large_pentagonal = generate_pentagonal(100)
        assert is_pentagonal_number(large_pentagonal)
