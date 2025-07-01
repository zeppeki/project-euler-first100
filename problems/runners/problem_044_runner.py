#!/usr/bin/env python3
"""
Runner for Problem 044: Pentagon numbers

This module contains the execution code for Problem 044, separated from the
algorithm implementations for better test coverage and code organization.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

from problems.problem_044 import (
    generate_pentagonal,
    is_pentagonal,
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
    print("Testing pentagonal number generation and detection:")

    # Test first 10 pentagonal numbers
    expected_pentagonals = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    print("  First 10 pentagonal numbers:")
    for i, expected in enumerate(expected_pentagonals, 1):
        generated = generate_pentagonal(i)
        correct = generated == expected
        print(f"    P{i} = {generated} {'✓' if correct else '✗'}")

    # Test pentagonal number detection
    print("\n  Testing pentagonal number detection:")
    test_cases = [
        (1, True),
        (5, True),
        (12, True),
        (22, True),
        (35, True),
        (2, False),
        (6, False),
        (13, False),
        (23, False),
        (36, False),
        (145, True),
        (146, False),
    ]

    for num, expected in test_cases:
        result = is_pentagonal(num)
        correct = result == expected
        print(f"    is_pentagonal({num}) = {result} {'✓' if correct else '✗'}")

    # Test the example from problem statement
    print("\n  Testing example from problem statement:")
    p4, p7, p8 = 22, 70, 92
    print(f"    P₄ = {p4}, P₇ = {p7}, P₈ = {p8}")
    print(f"    P₄ + P₇ = {p4 + p7} = P₈ = {p8} {'✓' if p4 + p7 == p8 else '✗'}")
    print(f"    P₇ - P₄ = {p7 - p4} = 48")
    print(
        f"    48 is pentagonal: {is_pentagonal(48)} {'✗' if not is_pentagonal(48) else '✓'}"
    )
    print("    (This confirms 48 is NOT pentagonal, as expected)")

    print("\nTesting solution functions:")
    # Test that all functions return the same result
    functions: list[tuple[str, Callable[[], int]]] = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    results: list[int] = []
    for name, func in functions:
        try:
            func_result = func()
            results.append(func_result)
            print(f"  ✓ {name}: {func_result}")
        except Exception as e:
            print(f"  ✗ {name}: Error - {e}")
            return

    if len(set(results)) == 1:
        print(f"  ✓ All solutions agree: {results[0]}")
    else:
        print(f"  ✗ Solutions disagree: {results}")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header("044", "Pentagon numbers", "Pentagonal pairs")

    # Run tests first
    run_tests()

    print("\nPerformance comparison:")
    # Run main problem with performance measurement
    functions = [
        ("素直な解法 (Brute force)", lambda: solve_naive()),
        ("最適化解法 (Optimized search)", lambda: solve_optimized()),
        ("数学的解法 (Mathematical approach)", lambda: solve_mathematical()),
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
