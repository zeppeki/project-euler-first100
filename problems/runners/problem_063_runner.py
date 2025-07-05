#!/usr/bin/env python3
"""
Runner for Problem 063: Powerful digit counts

This module contains the execution code for Problem 063, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_063 import (
    count_digits,
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
    # Test known examples from the problem statement
    assert count_digits(16807) == 5  # 7^5 is a 5-digit number
    assert count_digits(134217728) == 9  # 8^9 is a 9-digit number

    # Verify the examples are indeed powers
    assert 7**5 == 16807
    assert 8**9 == 134217728

    print("基本的な桁数計算と累乗の検証テストが完了しました")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header(
        "063",
        "Powerful digit counts",
        "Counting n-digit positive integers that are nth powers",
    )

    # Run tests first
    run_tests()

    # Run main problem with performance measurement
    functions = [
        ("素直な解法", lambda: solve_naive()),
        ("最適化解法", lambda: solve_optimized()),
        ("数学的解法", lambda: solve_mathematical()),
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
