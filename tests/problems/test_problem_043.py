#!/usr/bin/env python3
"""Tests for Problem 043"""

from problems.problem_043 import (
    has_substring_divisibility,
    is_pandigital_0_to_9,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem043:
    """Test cases for Problem 043"""

    def test_is_pandigital_0_to_9(self) -> None:
        """Test pandigital number validation"""
        assert is_pandigital_0_to_9("1406357289")
        assert is_pandigital_0_to_9("9876543210")
        assert is_pandigital_0_to_9("1023456789")

        # Invalid cases
        assert not is_pandigital_0_to_9("123456789")  # Missing 0, only 9 digits
        assert not is_pandigital_0_to_9("1406357288")  # Duplicate 8, missing 9
        assert not is_pandigital_0_to_9("140635728")  # Too short
        assert not is_pandigital_0_to_9("14063572891")  # Too long
        assert not is_pandigital_0_to_9("1234567899")  # Duplicate 9

    def test_has_substring_divisibility(self) -> None:
        """Test substring divisibility conditions"""
        # Known example from problem statement
        assert has_substring_divisibility("1406357289")

        # Test individual conditions for "1406357289"
        # d2d3d4=406 divisible by 2: True (406 % 2 == 0)
        # d3d4d5=063 divisible by 3: True (63 % 3 == 0)
        # d4d5d6=635 divisible by 5: True (635 % 5 == 0)
        # d5d6d7=357 divisible by 7: True (357 % 7 == 0)
        # d6d7d8=572 divisible by 11: True (572 % 11 == 0)
        # d7d8d9=728 divisible by 13: True (728 % 13 == 0)
        # d8d9d10=289 divisible by 17: True (289 % 17 == 0)

        # Verify the example step by step
        num = "1406357289"
        assert int(num[1:4]) % 2 == 0  # 406 % 2
        assert int(num[2:5]) % 3 == 0  # 063 % 3
        assert int(num[3:6]) % 5 == 0  # 635 % 5
        assert int(num[4:7]) % 7 == 0  # 357 % 7
        assert int(num[5:8]) % 11 == 0  # 572 % 11
        assert int(num[6:9]) % 13 == 0  # 728 % 13
        assert int(num[7:10]) % 17 == 0  # 289 % 17

        # Test a number that doesn't satisfy the conditions
        assert not has_substring_divisibility("1234567890")
        assert not has_substring_divisibility("9876543210")

    def test_example_verification(self) -> None:
        """Test the specific example from the problem"""
        example = "1406357289"
        assert is_pandigital_0_to_9(example)
        assert has_substring_divisibility(example)

        # Verify each divisibility condition explicitly
        assert int("406") % 2 == 0
        assert int("063") % 3 == 0  # 63 % 3
        assert int("635") % 5 == 0
        assert int("357") % 7 == 0
        assert int("572") % 11 == 0
        assert int("728") % 13 == 0
        assert int("289") % 17 == 0

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0  # Should find some valid numbers

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0  # Should find some valid numbers

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution"""
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 0  # Should find some valid numbers

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert naive_result == optimized_result, (
            f"Naive and optimized disagree: {naive_result} != {optimized_result}"
        )
        assert naive_result == mathematical_result, (
            f"Naive and mathematical disagree: {naive_result} != {mathematical_result}"
        )
        assert optimized_result == mathematical_result, (
            f"Optimized and mathematical disagree: {optimized_result} != {mathematical_result}"
        )

    def test_edge_cases(self) -> None:
        """Test edge cases"""
        # Test short strings
        assert not has_substring_divisibility("123")
        assert not has_substring_divisibility("")

        # Test strings with wrong length
        assert not has_substring_divisibility("12345678901")  # 11 digits
        assert not has_substring_divisibility("123456789")    # 9 digits
