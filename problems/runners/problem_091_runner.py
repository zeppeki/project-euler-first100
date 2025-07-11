#!/usr/bin/env python3
"""Runner for Problem 091: Right triangles with integer coordinates"""

import sys
import time
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from problems.problem_091 import (
    is_right_triangle,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    test_solutions,
)


def main() -> None:
    """Run all solutions for Problem 091 and display results."""
    print("=" * 60)
    print("Problem 091: Right triangles with integer coordinates")
    print("=" * 60)

    # Run built-in test
    print("\nRunning built-in tests...")
    test_solutions()

    print("\n" + "=" * 60)
    print("Solving main problem (50x50 grid)...")
    print("=" * 60)

    # Benchmark different approaches
    approaches = [
        ("Naive (10x10 only)", solve_naive, 10),
        ("Optimized", solve_optimized, 50),
        ("Mathematical", solve_mathematical, 50),
    ]

    results = []
    for name, func, limit in approaches:
        print(f"\nRunning {name} approach (limit={limit})...")
        start_time = time.time()
        result = func(limit)
        elapsed_time = time.time() - start_time
        results.append((name, result, elapsed_time, limit))
        print(f"Result: {result} triangles")
        print(f"Time: {elapsed_time:.6f} seconds")

    # Display summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for name, result, elapsed_time, limit in results:
        print(
            f"{name:20} (limit={limit:2}): {result:6} triangles in {elapsed_time:.6f}s"
        )

    # Final answer for the actual problem
    final_results = [r for r in results if r[3] == 50]
    if final_results:
        print("\n" + "=" * 60)
        print(f"FINAL ANSWER: {final_results[0][1]} triangles in a 50x50 grid")
        print("=" * 60)

    # Additional analysis
    print("\n" + "=" * 60)
    print("ADDITIONAL ANALYSIS")
    print("=" * 60)

    # Show growth pattern
    print("\nGrowth pattern of triangle count:")
    print("-" * 40)
    limits = [1, 2, 3, 5, 10, 15, 20]
    for limit in limits:
        count = solve_naive(limit) if limit <= 10 else solve_optimized(limit)
        ratio = count / (limit**4) if limit > 0 else 0
        print(
            f"{limit:3}x{limit:3} grid: {count:6} triangles (ratio to n⁴: {ratio:.4f})"
        )

    # Example triangles
    print("\nExample right triangles in 2x2 grid:")
    print("-" * 40)
    examples = [
        ((1, 0), (0, 1), "Right angle at origin"),
        ((1, 0), (1, 1), "Right angle at P"),
        ((0, 1), (1, 1), "Right angle at Q"),
        ((2, 0), (0, 1), "Right angle at origin"),
        ((2, 0), (2, 1), "Right angle at P"),
    ]

    for p, q, description in examples:
        x1, y1 = p
        x2, y2 = q
        if is_right_triangle(x1, y1, x2, y2):
            print(f"✓ O(0,0), P{p}, Q{q} - {description}")

    # Mathematical insights
    print("\nMathematical insights:")
    print("-" * 40)
    print("• Three types of right triangles based on vertex location:")
    print("  - Right angle at origin O")
    print("  - Right angle at point P")
    print("  - Right angle at point Q")
    print("• Uses Pythagorean theorem: a² + b² = c² for validation")
    print("• Growth is approximately O(n⁴) for an n×n grid")
    print("• Optimization avoids counting each triangle twice")


if __name__ == "__main__":
    main()
