#!/usr/bin/env python3
"""
Problem 030: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth
powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

Answer: 443839
"""


def solve(power: int = 5) -> int:
    """
    Finds the sum of all numbers that can be written as the sum of the given
    power of their digits.
    """
    # Determine the upper bound for the search.
    # For a number with d digits, the maximum sum of powers is d * 9^power.
    # We need to find the largest d for which d * 9^power has d digits.
    # 6 * 9^5 = 354294 (a 6-digit number)
    # 7 * 9^5 = 413343 (a 6-digit number, less than the smallest 7-digit number 1,000,000)
    # So, the upper bound is around 355000.
    upper_bound = (power + 1) * (9**power)

    total_sum = 0
    for i in range(10, upper_bound):
        sum_of_powers = sum(int(digit) ** power for digit in str(i))
        if i == sum_of_powers:
            total_sum += i

    return total_sum
