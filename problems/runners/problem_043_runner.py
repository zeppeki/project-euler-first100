#!/usr/bin/env python3
"""
Runner for Problem 043: Sub-string divisibility

This module contains the execution code for Problem 043, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_043 import (
    has_substring_divisibility,
    is_pandigital_0_to_9,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    print("Testing example from problem statement:")
    example = "1406357289"

    # Test the example number
    is_pandigital = is_pandigital_0_to_9(example)
    has_property = has_substring_divisibility(example)

    print(f"  Example number: {example}")
    print(f"  Is 0-9 pandigital: {'✓' if is_pandigital else '✗'}")
    print(f"  Has substring divisibility: {'✓' if has_property else '✗'}")

    # Test individual divisibility conditions
    print("\n  Divisibility conditions:")
    primes = [2, 3, 5, 7, 11, 13, 17]
    labels = ["d₂d₃d₄", "d₃d₄d₅", "d₄d₅d₆", "d₅d₆d₇", "d₆d₇d₈", "d₇d₈d₉", "d₈d₉d₁₀"]

    for i, (prime, label) in enumerate(zip(primes, labels, strict=False)):
        substring = example[i+1:i+4]
        divisible = int(substring) % prime == 0
        print(f"    {label} = {substring} ÷ {prime}: {'✓' if divisible else '✗'}")

    print("\nTesting solution functions:")
    # Test that all functions return the same result
    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    results = []
    for name, func in functions:
        try:
            result = func()
            results.append(result)
            print(f"  ✓ {name}: {result}")
        except Exception as e:
            print(f"  ✗ {name}: Error - {e}")
            return

    if len(set(results)) == 1:
        print(f"  ✓ All solutions agree: {results[0]}")
    else:
        print(f"  ✗ Solutions disagree: {results}")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header("043", "Sub-string divisibility", "0-9 pandigital numbers")

    # Run tests first
    run_tests()

    print("\nPerformance comparison:")
    # Run main problem with performance measurement
    functions = [
        ("素直な解法 (Generate all)", lambda: solve_naive()),
        ("最適化解法 (Backtracking)", lambda: solve_optimized()),
        ("数学的解法 (Direct check)", lambda: solve_mathematical()),
    ]

    performance_results = compare_performance(functions)

    # Verify all solutions agree
    results = [data["result"] for data in performance_results.values()]
    all_agree = len(set(results)) == 1

    if all_agree:
        answer = results[0]
        print_final_answer(answer, verified=True)
        print_performance_comparison(performance_results)
    else:
        print_final_answer(None, verified=False)
        print("Results:", results)


def main() -> None:
    """Main function for standalone execution."""
    run_problem()


if __name__ == "__main__":
    main()
