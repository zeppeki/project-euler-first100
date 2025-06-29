#!/usr/bin/env python3
"""
Problem 024: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012, 021, 102, 120, 201, 210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Answer: 2783915460
"""

import math
from itertools import permutations


def solve_naive(digits: str = "0123456789", n: int = 1_000_000) -> str:
    """
    Solves the problem by generating all permutations.
    Time complexity: O(d! * d) where d is the number of digits.
    Space complexity: O(d! * d)
    """
    num_permutations = math.factorial(len(digits))
    if not 1 <= n <= num_permutations:
        return ""

    # The nth permutation is at index n-1
    return "".join(list(permutations(digits))[n - 1])


def solve_optimized(digits: str = "0123456789", n: int = 1_000_000) -> str:
    """
    Solves the problem using a mathematical approach with factorials.
    Time complexity: O(d^2) where d is the number of digits.
    Space complexity: O(d)
    """
    num_permutations = math.factorial(len(digits))
    if not 1 <= n <= num_permutations:
        return ""

    result = []
    digit_list = list(digits)
    n -= 1  # Use 0-based index

    for i in range(len(digit_list) - 1, -1, -1):
        f = math.factorial(i)
        index = n // f
        n %= f
        result.append(digit_list.pop(index))

    return "".join(result)
