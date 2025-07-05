#!/usr/bin/env python3
"""
Runner for Problem 064: Odd period square roots

This module contains the execution code for Problem 064, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_064 import (
    get_continued_fraction_period,
    is_perfect_square,
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
    # Test perfect square detection
    assert is_perfect_square(1)
    assert is_perfect_square(4)
    assert is_perfect_square(9)
    assert not is_perfect_square(2)
    assert not is_perfect_square(3)

    # Test continued fraction periods for known examples
    # √2 has period 1: [1;(2)]
    assert get_continued_fraction_period(2) == 1

    # √3 has period 2: [1;(1,2)]
    assert get_continued_fraction_period(3) == 2

    # √5 has period 1: [2;(4)]
    assert get_continued_fraction_period(5) == 1

    # √23 has period 4: [4;(1,3,1,8)]
    assert get_continued_fraction_period(23) == 4

    print("連分数周期計算と完全平方数判定の検証テストが完了しました")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header(
        "064",
        "Odd period square roots",
        "Counting square roots with odd period continued fractions (N ≤ 10000)",
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
