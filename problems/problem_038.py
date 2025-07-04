#!/usr/bin/env python3
"""
Problem 038: Pandigital multiples

Take a number and multiply it by 1, 2, 3, ..., n, and concatenate
the products to form a 1 to 9 pandigital number.

Find the largest 9-digit pandigital number that can be formed by
concatenating the products of an integer with (1, 2, ..., n) where n > 1.

Example: 192 × (1,2,3) = 192384576 (9-digit pandigital)

Answer: [Answer here]
"""

from .lib import (
    concatenated_product,
)
from .lib import (
    is_pandigital_1_to_9 as is_pandigital,
)


def is_pandigital_str(num_str: str) -> bool:
    """Check if a string contains digits 1-9 exactly once."""
    return is_pandigital(num_str)


def solve_naive() -> int:
    """
    素直な解法: 全ての可能な組み合わせを試す
    時間計算量: O(n * m) where n is range of base numbers, m is max multiplier
    空間計算量: O(1)
    """
    largest_pandigital = 0

    for base in range(1, 10000):
        for n in range(2, 10):
            concat_result = concatenated_product(base, n)

            if len(concat_result) > 9:
                break

            if len(concat_result) == 9 and is_pandigital_str(concat_result):
                largest_pandigital = max(largest_pandigital, int(concat_result))

    return largest_pandigital


def solve_optimized() -> int:
    """
    最適化解法: より効率的な範囲制限
    時間計算量: O(n * log n)
    空間計算量: O(1)
    """
    largest_pandigital = 0

    for base in range(1, 10000):
        concat_str = ""
        multiplier = 1

        while len(concat_str) < 9:
            concat_str += str(base * multiplier)
            multiplier += 1

            if len(concat_str) == 9 and is_pandigital(concat_str) and multiplier > 2:
                largest_pandigital = max(largest_pandigital, int(concat_str))
                break
            if len(concat_str) > 9:
                break

    return largest_pandigital
