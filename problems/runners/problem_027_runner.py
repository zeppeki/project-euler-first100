#!/usr/bin/env python3
"""
Problem 027 Runner: Quadratic primes
実行・表示・パフォーマンス測定を担当
"""

import time

from problems.problem_027 import solve_naive, solve_optimized


def main() -> None:
    """Main function to run and compare solutions."""
    limit = 1000

    print("Solving Problem 027...")

    # --- Optimized Solution ---
    start_time = time.time()
    optimized_answer = solve_optimized(limit)
    optimized_time = time.time() - start_time
    print(f"Optimized solution: {optimized_answer} (took {optimized_time:.6f} seconds)")

    # Test with smaller limit for naive solution to verify correctness
    print("\nVerifying correctness with smaller limit...")
    small_limit = 100

    start_time = time.time()
    naive_answer_small = solve_naive(small_limit)
    naive_time_small = time.time() - start_time
    print(
        f"Naive solution (limit={small_limit}): {naive_answer_small} (took {naive_time_small:.6f} seconds)"
    )

    start_time = time.time()
    optimized_answer_small = solve_optimized(small_limit)
    optimized_time_small = time.time() - start_time
    print(
        f"Optimized solution (limit={small_limit}): {optimized_answer_small} (took {optimized_time_small:.6f} seconds)"
    )

    # Verify solutions match for small limit
    if naive_answer_small == optimized_answer_small:
        print(f"✓ Both solutions agree for limit={small_limit}: {naive_answer_small}")
    else:
        print(
            f"✗ Solutions disagree for limit={small_limit}: naive={naive_answer_small}, optimized={optimized_answer_small}"
        )


if __name__ == "__main__":
    main()
