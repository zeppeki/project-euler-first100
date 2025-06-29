#!/usr/bin/env python3
"""
Problem 029 Runner: Distinct powers
実行・表示・パフォーマンス測定を担当
"""

import time

from problems.problem_029 import solve_naive, solve_optimized


def main() -> None:
    """Main function to run and compare solutions."""
    limit = 100

    print(f"Solving Problem 029 for limit = {limit}...")

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


if __name__ == "__main__":
    main()
