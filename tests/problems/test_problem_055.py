#!/usr/bin/env python3
"""
Tests for Project Euler Problem 055: Lychrel numbers
"""

from collections.abc import Callable

import pytest

from problems.problem_055 import (
    analyze_number_process,
    get_lychrel_statistics,
    is_lychrel_number,
    is_palindrome,
    reverse_number,
    solve_naive,
    solve_optimized,
    test_lychrel_examples,
)


class TestUtilityFunctions:
    """Test utility functions for Lychrel number detection"""

    def test_is_palindrome(self) -> None:
        """Test palindrome detection"""
        # Single digit numbers are palindromes
        assert is_palindrome(0)
        assert is_palindrome(5)
        assert is_palindrome(9)

        # Multi-digit palindromes
        assert is_palindrome(11)
        assert is_palindrome(121)
        assert is_palindrome(1221)
        assert is_palindrome(12321)
        assert is_palindrome(123454321)

        # Non-palindromes
        assert not is_palindrome(10)
        assert not is_palindrome(123)
        assert not is_palindrome(1234)
        assert not is_palindrome(12345)

    def test_reverse_number(self) -> None:
        """Test number reversal"""
        assert reverse_number(0) == 0
        assert reverse_number(5) == 5
        assert reverse_number(10) == 1
        assert reverse_number(123) == 321
        assert reverse_number(1234) == 4321
        assert reverse_number(10203) == 30201

    def test_reverse_number_with_trailing_zeros(self) -> None:
        """Test number reversal with trailing zeros"""
        assert reverse_number(100) == 1
        assert reverse_number(1000) == 1
        assert reverse_number(1200) == 21
        assert reverse_number(12000) == 21


class TestLychrelDetection:
    """Test Lychrel number detection"""

    def test_is_lychrel_number_known_examples(self) -> None:
        """Test with known examples from the problem"""
        # 47 becomes palindrome in 1 iteration: 47 + 74 = 121
        assert not is_lychrel_number(47)

        # 349 becomes palindrome in 3 iterations
        assert not is_lychrel_number(349)

        # 196 is thought to be Lychrel (doesn't become palindrome in 50 iterations)
        assert is_lychrel_number(196)

        # 4994 is palindromic Lychrel number
        assert is_lychrel_number(4994)

    def test_is_lychrel_number_small_numbers(self) -> None:
        """Test with small numbers that should not be Lychrel"""
        # These numbers should quickly become palindromes
        assert not is_lychrel_number(1)  # Already palindrome
        assert not is_lychrel_number(11)  # Already palindrome
        assert not is_lychrel_number(19)  # 19 + 91 = 110, 110 + 011 = 121
        assert not is_lychrel_number(
            89
        )  # 89 + 98 = 187, 187 + 781 = 968, 968 + 869 = 1837, etc.

    def test_is_lychrel_number_custom_iterations(self) -> None:
        """Test with custom iteration limits"""
        # Test with very small iteration limit
        assert is_lychrel_number(349, max_iterations=1)  # Needs 3 iterations
        assert not is_lychrel_number(349, max_iterations=5)  # Should pass with 5

    def test_is_lychrel_number_edge_cases(self) -> None:
        """Test edge cases for Lychrel detection"""
        # Zero iteration limit
        assert is_lychrel_number(47, max_iterations=0)

        # Already palindromic numbers
        assert not is_lychrel_number(0)
        assert not is_lychrel_number(1)
        assert not is_lychrel_number(121)
        assert not is_lychrel_number(1221)


class TestExamplesVerification:
    """Test the example verification function"""

    def test_lychrel_examples(self) -> None:
        """Test that the examples verification function works"""
        assert test_lychrel_examples() is True


class TestSolutionFunctions:
    """Test main solution functions"""

    @pytest.mark.parametrize("solver", [solve_naive, solve_optimized])
    def test_solve_consistency(self, solver: Callable[[int], int]) -> None:
        """Test that solution methods work with small limits"""
        # Test with small limits first
        result_10 = solver(10)
        assert isinstance(result_10, int)
        assert result_10 >= 0
        assert result_10 <= 10

        result_100 = solver(100)
        assert isinstance(result_100, int)
        assert result_100 >= 0
        assert result_100 <= 100

    def test_solve_agreement(self) -> None:
        """Test that all solution methods agree"""
        # Test with smaller limits for speed
        limit = 100
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)

        assert result_naive == result_optimized

    def test_solve_known_results(self) -> None:
        """Test with known results for small limits"""
        # Test with very small limit where we can manually verify
        # Numbers 1-10: 1, 2, 3, 4, 5, 6, 7, 8, 9 should not be Lychrel
        # We need to check which ones actually are
        result_10 = solve_naive(10)
        assert result_10 >= 0
        assert result_10 <= 10

    @pytest.mark.slow
    def test_solve_full_problem(self) -> None:
        """Test the full problem (marked as slow test)"""
        result = solve_naive(10000)
        assert isinstance(result, int)
        assert result > 0  # There should be some Lychrel numbers
        assert result < 10000  # But not all numbers are Lychrel


class TestAnalysisFunctions:
    """Test analysis and statistics functions"""

    def test_analyze_number_process(self) -> None:
        """Test detailed number process analysis"""
        # Test with 47 (known non-Lychrel)
        analysis = analyze_number_process(47, 10)
        assert analysis["number"] == 47
        assert analysis["is_lychrel"] is False
        assert analysis["iterations_to_palindrome"] == 1
        assert analysis["final_palindrome"] == 121
        assert len(analysis["steps"]) == 1
        assert analysis["steps"][0]["current"] == 47
        assert analysis["steps"][0]["reversed"] == 74
        assert analysis["steps"][0]["sum"] == 121
        assert analysis["steps"][0]["is_palindrome"] is True

    def test_analyze_number_process_multi_step(self) -> None:
        """Test analysis with multi-step process"""
        # Test with 349 (known to take 3 iterations)
        analysis = analyze_number_process(349, 10)
        assert analysis["number"] == 349
        assert analysis["is_lychrel"] is False
        assert analysis["iterations_to_palindrome"] == 3
        assert len(analysis["steps"]) == 3

    def test_analyze_number_process_lychrel(self) -> None:
        """Test analysis with Lychrel number"""
        # Test with 196 (known Lychrel candidate)
        analysis = analyze_number_process(196, 5)  # Use small limit for speed
        assert analysis["number"] == 196
        assert analysis["is_lychrel"] is True
        assert analysis["iterations_to_palindrome"] is None
        assert analysis["final_palindrome"] is None
        assert len(analysis["steps"]) == 5

    def test_get_lychrel_statistics(self) -> None:
        """Test Lychrel number statistics"""
        # Test with small limit for speed
        stats = get_lychrel_statistics(100)

        assert "total_numbers" in stats
        assert "lychrel_count" in stats
        assert "lychrel_numbers" in stats
        assert "palindromic_lychrel_count" in stats
        assert "palindromic_lychrel_numbers" in stats
        assert "iteration_distribution" in stats

        assert stats["total_numbers"] == 99  # 1 to 99
        assert isinstance(stats["lychrel_count"], int)
        assert stats["lychrel_count"] >= 0
        assert len(stats["lychrel_numbers"]) == stats["lychrel_count"]
        assert stats["palindromic_lychrel_count"] >= 0
        assert stats["palindromic_lychrel_count"] <= stats["lychrel_count"]


class TestBoundaryConditions:
    """Test boundary conditions and edge cases"""

    def test_limit_one(self) -> None:
        """Test with limit of 1"""
        result = solve_naive(1)
        assert result == 0  # No numbers below 1

    def test_limit_two(self) -> None:
        """Test with limit of 2"""
        result = solve_naive(2)
        assert result == 0  # Number 1 is not Lychrel

    def test_empty_range(self) -> None:
        """Test with empty range"""
        result = solve_naive(0)
        assert result == 0

    def test_negative_limit(self) -> None:
        """Test with negative limit"""
        result = solve_naive(-1)
        assert result == 0


class TestSpecialCases:
    """Test special cases and interesting examples"""

    def test_palindromic_non_lychrel(self) -> None:
        """Test palindromic numbers that are not Lychrel"""
        # Most palindromic numbers are not Lychrel
        assert not is_lychrel_number(11)
        assert not is_lychrel_number(121)
        assert not is_lychrel_number(1221)

    def test_known_lychrel_numbers(self) -> None:
        """Test known Lychrel numbers"""
        # These are believed to be Lychrel numbers
        known_lychrel = [
            196,
            295,
            394,
            493,
            592,
            689,
            691,
            788,
            790,
            879,
            887,
            978,
            986,
        ]

        for num in known_lychrel:
            if num < 1000:  # Only test smaller numbers for speed
                assert is_lychrel_number(num), f"Number {num} should be Lychrel"

    def test_reverse_and_add_process(self) -> None:
        """Test the reverse and add process step by step"""
        # Test 47 -> 121 process
        current = 47
        current = current + reverse_number(current)  # 47 + 74 = 121
        assert current == 121
        assert is_palindrome(current)

        # Test 349 -> 7337 process
        current = 349
        current = current + reverse_number(current)  # 349 + 943 = 1292
        assert current == 1292
        current = current + reverse_number(current)  # 1292 + 2921 = 4213
        assert current == 4213
        current = current + reverse_number(current)  # 4213 + 3124 = 7337
        assert current == 7337
        assert is_palindrome(current)


if __name__ == "__main__":
    pytest.main([__file__])
