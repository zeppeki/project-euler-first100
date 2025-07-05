#!/usr/bin/env python3
"""
Runner for Problem 062: Cubic permutations

This module contains the execution code for Problem 062, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_062 import get_digit_signature, solve_naive, solve_optimized
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    # Test the digit signature function with known examples
    test_signature_1 = get_digit_signature(41063625)  # 345³
    test_signature_2 = get_digit_signature(56623104)  # 384³
    test_signature_3 = get_digit_signature(66430125)  # 405³

    # These should all have the same signature since they're permutations
    assert test_signature_1 == test_signature_2 == test_signature_3
    print("桁順列の検証テストが完了しました")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header(
        "062",
        "Cubic permutations",
        "Finding smallest cube with exactly 5 digit permutations",
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
