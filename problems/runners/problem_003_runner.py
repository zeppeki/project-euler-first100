#!/usr/bin/env python3
"""
Runner for Problem 003: Largest prime factor

This module contains the execution code for Problem 003, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_003 import solve_naive, solve_optimized
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
    print_test_results,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    test_cases = [
        (13195, 29),  # Example: 5, 7, 13, 29 → max is 29
        (100, 5),  # 100 = 2^2 × 5^2 → max is 5
        (84, 7),  # 84 = 2^2 × 3 × 7 → max is 7
        (17, 17),  # 素数 → 最大は17
        (25, 5),  # 25 = 5^2 → 最大は5
    ]

    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
    ]

    print_test_results(test_cases, functions)


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    n = 600851475143

    print_solution_header("003", "Largest prime factor", n)

    # Run tests first
    run_tests()

    # Run main problem with performance measurement
    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
    ]

    performance_results = compare_performance(functions, n)

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
