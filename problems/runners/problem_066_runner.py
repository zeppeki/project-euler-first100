#!/usr/bin/env python3
"""
Runner for Problem 066: Diophantine equation

This module contains the execution code for Problem 066, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_066 import (
    is_perfect_square,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    solve_pell_equation,
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
    assert not is_perfect_square(5)

    # Test known Pell equation solutions from problem description
    test_cases = [
        (2, (3, 2)),  # x=3, y=2 for D=2
        (3, (2, 1)),  # x=2, y=1 for D=3
        (5, (9, 4)),  # x=9, y=4 for D=5
        (6, (5, 2)),  # x=5, y=2 for D=6
        (7, (8, 3)),  # x=8, y=3 for D=7
        (13, (649, 180)),  # x=649, y=180 for D=13
    ]

    for d, (expected_x, expected_y) in test_cases:
        x, y = solve_pell_equation(d)
        assert x == expected_x, f"D={d}: expected x={expected_x}, got x={x}"
        assert y == expected_y, f"D={d}: expected y={expected_y}, got y={y}"
        # Verify the Pell equation
        assert x * x - d * y * y == 1, f"D={d}: Pell equation not satisfied"

    print("Pell方程式の解法と完全平方数検出の検証テストが完了しました")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    # TODO: Set problem parameters
    # limit = 1000

    print_solution_header(
        "066", "Diophantine equation", "D ≤ 1000で最大の最小解xを持つDを見つける"
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
