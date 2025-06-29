#!/usr/bin/env python3
"""
Runner for Problem 030: Digit fifth powers
"""

import time

from ..problem_030 import solve


def main() -> None:
    """Main function to run and display the solution."""
    power = 5

    print(f"Solving Problem 030 for power = {power}...")

    start_time = time.time()
    solution = solve(power)
    elapsed_time = time.time() - start_time

    print(f"Solution: {solution}")
    print(f"Took {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    main()
