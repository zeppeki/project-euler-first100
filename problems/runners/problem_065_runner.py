#!/usr/bin/env python3
"""
Runner for Problem 065: Convergents of e

This module contains the execution code for Problem 065, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_065 import (
    compute_convergent,
    get_e_continued_fraction_coefficient,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    sum_of_digits,
)
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    # Test e continued fraction coefficients
    assert get_e_continued_fraction_coefficient(0) == 2
    assert get_e_continued_fraction_coefficient(1) == 1
    assert get_e_continued_fraction_coefficient(2) == 2
    assert get_e_continued_fraction_coefficient(3) == 1
    assert get_e_continued_fraction_coefficient(4) == 1
    assert get_e_continued_fraction_coefficient(5) == 4
    assert get_e_continued_fraction_coefficient(6) == 1
    assert get_e_continued_fraction_coefficient(7) == 1
    assert get_e_continued_fraction_coefficient(8) == 6

    # Test convergents (from problem description)
    convergents = [
        (2, 1),  # 0th: 2
        (3, 1),  # 1st: 3
        (8, 3),  # 2nd: 8/3
        (11, 4),  # 3rd: 11/4
        (19, 7),  # 4th: 19/7
        (87, 32),  # 5th: 87/32
        (106, 39),  # 6th: 106/39
        (193, 71),  # 7th: 193/71
        (1264, 465),  # 8th: 1264/465
        (1457, 536),  # 9th: 1457/536
    ]

    for i, (expected_num, expected_den) in enumerate(convergents):
        num, den = compute_convergent(i)
        assert num == expected_num, (
            f"Convergent {i}: expected numerator {expected_num}, got {num}"
        )
        assert den == expected_den, (
            f"Convergent {i}: expected denominator {expected_den}, got {den}"
        )

    # Test sum of digits for 10th convergent (1457)
    assert sum_of_digits(1457) == 17

    print("e連分数係数と収束分数の検証テストが完了しました")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    # TODO: Set problem parameters
    # limit = 1000

    print_solution_header("065", "Convergents of e", "100番目の収束分数の分子の桁数和")

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
