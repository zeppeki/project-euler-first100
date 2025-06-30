#!/usr/bin/env python3
"""Tests for Problem 042"""

from problems.problem_042 import (
    generate_triangle_numbers,
    get_word_value,
    is_triangle_number,
    load_words,
    solve_naive,
    solve_optimized,
)


class TestProblem042:
    """Test cases for Problem 042"""

    def test_get_word_value(self) -> None:
        """Test word value calculation"""
        assert get_word_value("A") == 1
        assert get_word_value("B") == 2
        assert get_word_value("Z") == 26
        assert get_word_value("SKY") == 19 + 11 + 25  # 55
        assert get_word_value("ABC") == 1 + 2 + 3  # 6

    def test_is_triangle_number(self) -> None:
        """Test triangle number detection"""
        # First 10 triangle numbers: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
        triangle_numbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        non_triangle_numbers = [2, 4, 5, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20]

        for num in triangle_numbers:
            assert is_triangle_number(num), f"{num} should be a triangle number"

        for num in non_triangle_numbers:
            assert not is_triangle_number(num), f"{num} should not be a triangle number"

    def test_generate_triangle_numbers(self) -> None:
        """Test triangle number generation"""
        triangle_numbers = generate_triangle_numbers(60)
        expected = {1, 3, 6, 10, 15, 21, 28, 36, 45, 55}
        assert expected.issubset(triangle_numbers)
        assert 66 not in triangle_numbers  # 66 > 60

    def test_load_words(self) -> None:
        """Test word loading from file"""
        words = load_words()
        assert len(words) > 1000  # Should have many words
        assert "SKY" in words  # Example from problem description
        assert all(isinstance(word, str) for word in words)
        assert all(word.isupper() for word in words)  # Words should be uppercase

    def test_triangle_word_example(self) -> None:
        """Test the SKY example from problem description"""
        assert get_word_value("SKY") == 55
        assert is_triangle_number(55)

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0  # Should find some triangle words

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0  # Should find some triangle words

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()

        assert naive_result == optimized_result, (
            f"Solutions disagree: naive={naive_result}, optimized={optimized_result}"
        )
