#!/usr/bin/env python3
"""
Runner for Problem 024: Lexicographic permutations
"""

import time

from problems.problem_024 import solve_naive, solve_optimized


def main() -> None:
    """Main function to run and compare solutions."""
    digits = "0123456789"
    n = 1_000_000

    print("Solving Problem 024...")

    # --- Naive Solution ---
    start_time = time.time()
    naive_answer = solve_naive(digits, n)
    naive_time = time.time() - start_time
    print(f"Naive solution: {naive_answer} (took {naive_time:.6f} seconds)")

    # --- Optimized Solution ---
    start_time = time.time()
    optimized_answer = solve_optimized(digits, n)
    optimized_time = time.time() - start_time
    print(f"Optimized solution: {optimized_answer} (took {optimized_time:.6f} seconds)")


if __name__ == "__main__":
    main()
