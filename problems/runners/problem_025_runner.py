#!/usr/bin/env python3
"""
Runner for Problem 025: 1000-digit Fibonacci number
"""

import time

from problems.problem_025 import solve_naive, solve_optimized


def main() -> None:
    """Main function to run and compare solutions."""
    target_digits = 1000

    print("Solving Problem 025...")

    # --- Naive Solution ---
    start_time = time.time()
    naive_answer = solve_naive(target_digits)
    naive_time = time.time() - start_time
    print(f"Naive solution: {naive_answer} (took {naive_time:.6f} seconds)")

    # --- Optimized Solution ---
    start_time = time.time()
    optimized_answer = solve_optimized(target_digits)
    optimized_time = time.time() - start_time
    print(f"Optimized solution: {optimized_answer} (took {optimized_time:.6f} seconds)")


if __name__ == "__main__":
    main()
