#!/usr/bin/env python3
"""Tests for Problem 061"""

from problems.problem_061 import generate_figurate_numbers, solve_naive, solve_optimized


class TestProblem061:
    """Test cases for Problem 061"""

    def test_generate_figurate_numbers(self) -> None:
        """Test figurate number generation"""
        # Test triangle numbers
        triangle_numbers = generate_figurate_numbers(3, 1000, 2000)
        assert len(triangle_numbers) > 0
        assert 1035 in triangle_numbers  # 45th triangle number: 45*46/2 = 1035
        assert 1378 in triangle_numbers  # 52nd triangle number: 52*53/2 = 1378

        # Test square numbers
        square_numbers = generate_figurate_numbers(4, 1000, 2000)
        assert len(square_numbers) > 0
        assert 1024 in square_numbers  # 32^2 = 1024
        assert 1369 in square_numbers  # 37^2 = 1369

        # Test pentagonal numbers
        pentagonal_numbers = generate_figurate_numbers(5, 1000, 2000)
        assert len(pentagonal_numbers) > 0
        assert 1001 in pentagonal_numbers  # 26th pentagonal: 26*(3*26-1)/2 = 1001

        # Test hexagonal numbers
        hexagonal_numbers = generate_figurate_numbers(6, 1000, 2000)
        assert len(hexagonal_numbers) > 0
        assert 1128 in hexagonal_numbers  # 24th hexagonal: 24*(2*24-1) = 1128

        # Test heptagonal numbers
        heptagonal_numbers = generate_figurate_numbers(7, 1000, 2000)
        assert len(heptagonal_numbers) > 0
        assert 1071 in heptagonal_numbers  # 21st heptagonal: 21*(5*21-3)/2 = 1071

        # Test octagonal numbers
        octagonal_numbers = generate_figurate_numbers(8, 1000, 2000)
        assert len(octagonal_numbers) > 0
        assert 1045 in octagonal_numbers  # 19th octagonal: 19*(3*19-2) = 1045

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        result_naive = solve_naive()
        result_optimized = solve_optimized()

        assert result_naive == result_optimized
        assert result_naive > 0
