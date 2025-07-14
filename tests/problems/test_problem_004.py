"""Tests for Problem 004: Largest palindrome product."""

import os
import sys

import pytest

# Add the problems directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "problems"))

# Import after path modification
from problems.problem_004 import (
    is_palindrome,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem004:
    """Test cases for Problem 004."""

    def test_is_palindrome(self) -> None:
        """Test the palindrome detection function."""
        # Test palindromes
        assert is_palindrome(0)
        assert is_palindrome(1)
        assert is_palindrome(9)
        assert is_palindrome(11)
        assert is_palindrome(121)
        assert is_palindrome(1221)
        assert is_palindrome(9009)
        assert is_palindrome(906609)

        # Test non-palindromes
        assert not is_palindrome(10)
        assert not is_palindrome(12)
        assert not is_palindrome(123)
        assert not is_palindrome(1234)
        assert not is_palindrome(9008)

    @pytest.mark.parametrize(
        "min_digits,max_digits,expected_palindrome",
        [
            (1, 1, 9),  # 3 * 3 = 9
            (2, 2, 9009),  # 91 * 99 = 9009
        ],
    )
    def test_solve_naive(
        self, min_digits: int, max_digits: int, expected_palindrome: int
    ) -> None:
        """Test the naive solution."""
        result = solve_naive(min_digits, max_digits)
        assert result == expected_palindrome, (
            f"Expected {expected_palindrome}, got {result}"
        )
        assert is_palindrome(result), f"Result {result} is not a palindrome"

    @pytest.mark.parametrize(
        "min_digits,max_digits,expected_palindrome",
        [
            (1, 1, 9),  # 3 * 3 = 9
            (2, 2, 9009),  # 91 * 99 = 9009
        ],
    )
    def test_solve_optimized(
        self, min_digits: int, max_digits: int, expected_palindrome: int
    ) -> None:
        """Test the optimized solution."""
        result = solve_optimized(min_digits, max_digits)
        assert result == expected_palindrome, (
            f"Expected {expected_palindrome}, got {result}"
        )
        assert is_palindrome(result), f"Result {result} is not a palindrome"

    @pytest.mark.parametrize(
        "min_digits,max_digits,expected_palindrome",
        [
            (1, 1, 9),  # 3 * 3 = 9
            (2, 2, 9009),  # 91 * 99 = 9009
        ],
    )
    def test_solve_mathematical(
        self, min_digits: int, max_digits: int, expected_palindrome: int
    ) -> None:
        """Test the mathematical solution."""
        result = solve_mathematical(min_digits, max_digits)
        assert result == expected_palindrome, (
            f"Expected {expected_palindrome}, got {result}"
        )
        assert is_palindrome(result), f"Result {result} is not a palindrome"

    @pytest.mark.parametrize("min_digits,max_digits", [(1, 1), (2, 2)])
    def test_all_solutions_agree(self, min_digits: int, max_digits: int) -> None:
        """Test that all solutions give the same result."""
        naive_result = solve_naive(min_digits, max_digits)
        optimized_result = solve_optimized(min_digits, max_digits)
        math_result = solve_mathematical(min_digits, max_digits)

        assert naive_result == optimized_result == math_result, (
            f"Solutions disagree for {min_digits}-{max_digits} digits: "
            f"naive={naive_result}, optimized={optimized_result}, "
            f"math={math_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test with invalid input (min_digits > max_digits)
        result = solve_naive(3, 2)
        assert result == 0

        result = solve_optimized(3, 2)
        assert result == 0

        result = solve_mathematical(3, 2)
        assert result == 0

    def test_problem_answer(self) -> None:
        """Test the actual problem with 3-digit numbers (optimized for speed)."""
        # This is the actual problem we need to solve
        min_digits = 3
        max_digits = 3
        expected_answer = 906609

        # Test mathematical solution first (fastest)
        result_math = solve_mathematical(min_digits, max_digits)
        assert result_math == expected_answer
        assert is_palindrome(result_math)

        # Test optimized solution
        result_optimized = solve_optimized(min_digits, max_digits)
        assert result_optimized == expected_answer

        # Skip naive solution for 3-digit case as it's too slow

    def test_palindrome_structure(self) -> None:
        """Test understanding of palindrome structure."""
        # Test that 6-digit palindromes are divisible by 11
        # 6-digit palindrome: abccba = 100001*a + 10010*b + 1100*c
        # = 11*(9091*a + 910*b + 100*c)

        # Generate some 6-digit palindromes
        palindromes_6_digit = []
        for a in range(1, 10):  # First digit can't be 0
            for b in range(10):
                for c in range(10):
                    palindrome = 100001 * a + 10010 * b + 1100 * c
                    palindromes_6_digit.append(palindrome)
                    if len(palindromes_6_digit) >= 10:  # Test just a few
                        break
                if len(palindromes_6_digit) >= 10:
                    break
            if len(palindromes_6_digit) >= 10:
                break

        # All 6-digit palindromes should be divisible by 11
        for palindrome in palindromes_6_digit:
            assert palindrome % 11 == 0, (
                f"6-digit palindrome {palindrome} not divisible by 11"
            )
            assert is_palindrome(palindrome), f"{palindrome} is not a palindrome"

    def test_solution_functionality(self) -> None:
        """Test that all solutions work correctly without timing measurements."""
        min_digits = 2
        max_digits = 2
        expected = 9009

        # Test that all solutions return the correct answer
        result_naive = solve_naive(min_digits, max_digits)
        result_optimized = solve_optimized(min_digits, max_digits)
        result_math = solve_mathematical(min_digits, max_digits)

        # All should return the same correct result
        assert result_naive == expected
        assert result_optimized == expected
        assert result_math == expected

        # Verify palindrome properties
        assert is_palindrome(result_naive)
        assert is_palindrome(result_optimized)
        assert is_palindrome(result_math)
