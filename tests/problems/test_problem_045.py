#!/usr/bin/env python3
"""Tests for Problem 045"""

from problems.problem_045 import (
    generate_hexagonal,
    generate_pentagonal,
    generate_triangle,
    is_hexagonal,
    is_pentagonal,
    is_triangle,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem045:
    """Test cases for Problem 045"""

    def test_generate_triangle(self) -> None:
        """Test triangular number generation"""
        # First 10 triangular numbers: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
        expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

        for i, expected_value in enumerate(expected, 1):
            assert generate_triangle(i) == expected_value

        # Test some larger cases
        assert generate_triangle(100) == 5050  # 100 * 101 / 2
        assert generate_triangle(285) == 40755  # Known from problem

    def test_generate_pentagonal(self) -> None:
        """Test pentagonal number generation"""
        # First 10 pentagonal numbers: 1, 5, 12, 22, 35, 51, 70, 92, 117, 145
        expected = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]

        for i, expected_value in enumerate(expected, 1):
            assert generate_pentagonal(i) == expected_value

        # Test known case from problem
        assert generate_pentagonal(165) == 40755

    def test_generate_hexagonal(self) -> None:
        """Test hexagonal number generation"""
        # First 10 hexagonal numbers: 1, 6, 15, 28, 45, 66, 91, 120, 153, 190
        expected = [1, 6, 15, 28, 45, 66, 91, 120, 153, 190]

        for i, expected_value in enumerate(expected, 1):
            assert generate_hexagonal(i) == expected_value

        # Test known case from problem
        assert generate_hexagonal(143) == 40755

    def test_is_triangle(self) -> None:
        """Test triangular number detection"""
        # Test known triangular numbers
        triangular_numbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 40755]
        for num in triangular_numbers:
            assert is_triangle(num), f"{num} should be triangular"

        # Test non-triangular numbers
        non_triangular = [2, 4, 5, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 48, 100]
        for num in non_triangular:
            assert not is_triangle(num), f"{num} should not be triangular"

        # Test edge cases
        assert not is_triangle(0)
        assert not is_triangle(-1)
        assert not is_triangle(-10)

    def test_is_pentagonal(self) -> None:
        """Test pentagonal number detection"""
        # Test known pentagonal numbers
        pentagonal_numbers = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 40755]
        for num in pentagonal_numbers:
            assert is_pentagonal(num), f"{num} should be pentagonal"

        # Test non-pentagonal numbers
        non_pentagonal = [2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 48, 100]
        for num in non_pentagonal:
            assert not is_pentagonal(num), f"{num} should not be pentagonal"

        # Test edge cases
        assert not is_pentagonal(0)
        assert not is_pentagonal(-1)
        assert not is_pentagonal(-5)

    def test_is_hexagonal(self) -> None:
        """Test hexagonal number detection"""
        # Test known hexagonal numbers
        hexagonal_numbers = [1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 40755]
        for num in hexagonal_numbers:
            assert is_hexagonal(num), f"{num} should be hexagonal"

        # Test non-hexagonal numbers
        non_hexagonal = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 48, 100]
        for num in non_hexagonal:
            assert not is_hexagonal(num), f"{num} should not be hexagonal"

        # Test edge cases
        assert not is_hexagonal(0)
        assert not is_hexagonal(-1)
        assert not is_hexagonal(-6)

    def test_known_example_from_problem(self) -> None:
        """Test the known example from the problem statement"""
        # T285 = P165 = H143 = 40755
        example_num = 40755

        assert generate_triangle(285) == example_num
        assert generate_pentagonal(165) == example_num
        assert generate_hexagonal(143) == example_num

        # Verify that 40755 is detected as all three types
        assert is_triangle(example_num)
        assert is_pentagonal(example_num)
        assert is_hexagonal(example_num)

    def test_number_properties(self) -> None:
        """Test mathematical properties of the number sequences"""
        # Test that numbers in each sequence are strictly increasing
        for i in range(1, 20):
            assert generate_triangle(i) < generate_triangle(i + 1)
            assert generate_pentagonal(i) < generate_pentagonal(i + 1)
            assert generate_hexagonal(i) < generate_hexagonal(i + 1)

        # Test that hexagonal numbers are always triangular (mathematical fact)
        for i in range(1, 50):
            hex_num = generate_hexagonal(i)
            assert is_triangle(hex_num), f"H{i} = {hex_num} should be triangular"

    def test_mathematical_property_hexagonal_triangular(self) -> None:
        """Test that every hexagonal number is also triangular"""
        # Mathematical proof: H_n = n(2n-1) = T_{2n-1}
        for n in range(1, 100):
            hex_n = generate_hexagonal(n)
            triangle_2n_minus_1 = generate_triangle(2 * n - 1)
            assert hex_n == triangle_2n_minus_1, f"H_{n} should equal T_{2 * n - 1}"

    def test_inverse_formulas(self) -> None:
        """Test the inverse formulas used in detection functions"""
        # Test triangular number inverse formula
        for n in range(1, 50):
            tri = generate_triangle(n)
            # Formula: n = (-1 + sqrt(1 + 8*T)) / 2
            discriminant = 1 + 8 * tri
            sqrt_disc = int(discriminant**0.5)
            if sqrt_disc * sqrt_disc == discriminant and (sqrt_disc - 1) % 2 == 0:
                recovered_n = (sqrt_disc - 1) // 2
                assert recovered_n == n
                assert generate_triangle(recovered_n) == tri

        # Test pentagonal number inverse formula
        for n in range(1, 50):
            pent = generate_pentagonal(n)
            # Formula: n = (1 + sqrt(1 + 24*P)) / 6
            discriminant = 1 + 24 * pent
            sqrt_disc = int(discriminant**0.5)
            if sqrt_disc * sqrt_disc == discriminant and (1 + sqrt_disc) % 6 == 0:
                recovered_n = (1 + sqrt_disc) // 6
                assert recovered_n == n
                assert generate_pentagonal(recovered_n) == pent

        # Test hexagonal number inverse formula
        for n in range(1, 50):
            hex_num = generate_hexagonal(n)
            # Formula: n = (1 + sqrt(1 + 8*H)) / 4
            discriminant = 1 + 8 * hex_num
            sqrt_disc = int(discriminant**0.5)
            if sqrt_disc * sqrt_disc == discriminant and (1 + sqrt_disc) % 4 == 0:
                recovered_n = (1 + sqrt_disc) // 4
                assert recovered_n == n
                assert generate_hexagonal(recovered_n) == hex_num

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 40755, "Should find next number after 40755"
        # The result should be all three types
        assert is_triangle(result), "Result should be triangular"
        assert is_pentagonal(result), "Result should be pentagonal"
        assert is_hexagonal(result), "Result should be hexagonal"

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 40755, "Should find next number after 40755"
        # The result should be all three types
        assert is_triangle(result), "Result should be triangular"
        assert is_pentagonal(result), "Result should be pentagonal"
        assert is_hexagonal(result), "Result should be hexagonal"

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution"""
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 40755, "Should find next number after 40755"
        # The result should be all three types
        assert is_triangle(result), "Result should be triangular"
        assert is_pentagonal(result), "Result should be pentagonal"
        assert is_hexagonal(result), "Result should be hexagonal"

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

    def test_small_triple_numbers(self) -> None:
        """Test numbers that are triangular, pentagonal, and hexagonal"""
        # We know 1 and 40755 are triple numbers
        triple_numbers = [1, 40755]

        for num in triple_numbers:
            assert is_triangle(num), f"{num} should be triangular"
            assert is_pentagonal(num), f"{num} should be pentagonal"
            assert is_hexagonal(num), f"{num} should be hexagonal"

    def test_large_number_generation(self) -> None:
        """Test behavior with larger indices"""
        # Test some larger cases to ensure formulas work correctly
        large_indices = [1000, 5000]

        for n in large_indices:
            tri = generate_triangle(n)
            pent = generate_pentagonal(n)
            hex_num = generate_hexagonal(n)

            # Verify each number is detected correctly
            assert is_triangle(tri)
            assert is_pentagonal(pent)
            assert is_hexagonal(hex_num)

            # Test that nearby numbers are not of the same type
            assert not is_triangle(tri - 1)
            assert not is_triangle(tri + 1)
            assert not is_pentagonal(pent - 1)
            assert not is_pentagonal(pent + 1)
            assert not is_hexagonal(hex_num - 1)
            assert not is_hexagonal(hex_num + 1)
