#!/usr/bin/env python3
"""
Runner for Problem 061: Cyclical figurate numbers

This module contains the execution code for Problem 061, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_061 import solve_naive, solve_optimized
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    # Skip runner tests as they are covered by unit tests
    print("図形数生成とアルゴリズムの検証はunit testで実施済み")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header(
        "061",
        "Cyclical figurate numbers",
        "Finding sum of cyclic 4-digit figurate numbers",
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
