#!/usr/bin/env python3
"""
Runner for Problem 026: Reciprocal cycles
"""

import time

from ..problem_026 import solve_naive, solve_optimized


def main() -> None:
    """Main function to run and compare solutions."""
    limit = 1000

    print("Solving Problem 026...")

    # --- Naive Solution ---
    start_time = time.time()
    naive_answer = solve_naive(limit)
    naive_time = time.time() - start_time
    print(f"Naive solution: {naive_answer} (took {naive_time:.6f} seconds)")

    # --- Optimized Solution ---
    start_time = time.time()
    optimized_answer = solve_optimized(limit)
    optimized_time = time.time() - start_time
    print(f"Optimized solution: {optimized_answer} (took {optimized_time:.6f} seconds)")

    # Verify solutions match
    if naive_answer == optimized_answer:
        print(f"✓ Both solutions agree: {naive_answer}")
    else:
        print(
            f"✗ Solutions disagree: naive={naive_answer}, optimized={optimized_answer}"
        )


if __name__ == "__main__":
    main()
