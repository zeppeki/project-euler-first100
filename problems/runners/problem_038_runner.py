#!/usr/bin/env python3
"""
Runner for Problem 038: Pandigital multiples

This module contains the execution code for Problem 038, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_038 import (
    concatenated_product,
    is_pandigital,
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

    # Test helper functions first
    print("Testing helper functions:")
    print(f"is_pandigital('123456789'): {is_pandigital('123456789')}")
    print(f"is_pandigital('192384576'): {is_pandigital('192384576')}")
    print(f"is_pandigital('918273645'): {is_pandigital('918273645')}")
    print(f"concatenated_product(192, 3): {concatenated_product(192, 3)}")
    print(f"concatenated_product(9, 5): {concatenated_product(9, 5)}")
    print()

    # No parameterized test cases needed since the problem asks for the largest value
    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
    ]

    # Just verify both functions return the same result
    results: list[int] = []
    for name, func in functions:
        try:
            result = func()
            results.append(result)
            print(f"{name}: {result}")
        except Exception as e:
            print(f"{name}: Error - {e}")
            # Don't append None for type safety - just continue

    if len(set(results)) == 1 and len(results) == 2:
        print("✓ All solutions agree")
    else:
        print("✗ Solutions disagree")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header(
        "038", "Pandigital multiples", "Find largest 9-digit pandigital"
    )

    # Run tests first
    run_tests()

    # Run main problem with performance measurement
    functions = [
        ("素直な解法", lambda: solve_naive()),
        ("最適化解法", lambda: solve_optimized()),
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
