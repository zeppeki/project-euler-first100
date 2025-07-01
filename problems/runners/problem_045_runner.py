#!/usr/bin/env python3
"""
Runner for Problem 045: Triangular, pentagonal, and hexagonal

This module contains the execution code for Problem 045, separated from the
algorithm implementations for better test coverage and code organization.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

from problems.problem_045 import (
    generate_hexagonal,
    generate_pentagonal,
    generate_triangle,
    is_hexagonal,
    is_pentagonal,
    is_triangle,
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
    print("Testing number generation and detection:")

    # Test first few numbers of each type
    print("  First 10 triangular numbers:")
    expected_triangular = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    for i, expected in enumerate(expected_triangular, 1):
        generated = generate_triangle(i)
        correct = generated == expected
        print(f"    T{i} = {generated} {'✓' if correct else '✗'}")

    print("\n  First 10 pentagonal numbers:")
    expected_pentagonal = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    for i, expected in enumerate(expected_pentagonal, 1):
        generated = generate_pentagonal(i)
        correct = generated == expected
        print(f"    P{i} = {generated} {'✓' if correct else '✗'}")

    print("\n  First 10 hexagonal numbers:")
    expected_hexagonal = [1, 6, 15, 28, 45, 66, 91, 120, 153, 190]
    for i, expected in enumerate(expected_hexagonal, 1):
        generated = generate_hexagonal(i)
        correct = generated == expected
        print(f"    H{i} = {generated} {'✓' if correct else '✗'}")

    # Test number detection
    print("\n  Testing number detection:")
    test_cases = [
        (1, True, True, True),  # T1, P1, H1
        (3, True, False, False),  # T2
        (6, True, False, True),  # T3, H2
        (10, True, False, False),  # T4
        (15, True, False, True),  # T5, H3
        (40755, True, True, True),  # Known example: T285, P165, H143
    ]

    for num, is_tri, is_pent, is_hex in test_cases:
        tri_result = is_triangle(num)
        pent_result = is_pentagonal(num)
        hex_result = is_hexagonal(num)

        tri_ok = tri_result == is_tri
        pent_ok = pent_result == is_pent
        hex_ok = hex_result == is_hex

        status = "✓" if tri_ok and pent_ok and hex_ok else "✗"
        print(f"    {num}: T={tri_result} P={pent_result} H={hex_result} {status}")

    # Test the known example from problem statement
    print("\n  Testing known example:")
    example_num = 40755
    print(
        f"    T285 = {generate_triangle(285)} {'✓' if generate_triangle(285) == example_num else '✗'}"
    )
    print(
        f"    P165 = {generate_pentagonal(165)} {'✓' if generate_pentagonal(165) == example_num else '✗'}"
    )
    print(
        f"    H143 = {generate_hexagonal(143)} {'✓' if generate_hexagonal(143) == example_num else '✗'}"
    )
    print(
        f"    All equal to 40755: {'✓' if all(f(n) == example_num for f, n in [(generate_triangle, 285), (generate_pentagonal, 165), (generate_hexagonal, 143)]) else '✗'}"
    )

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
    print_solution_header(
        "045", "Triangular, pentagonal, and hexagonal", "Number sequence convergence"
    )

    # Run tests first
    run_tests()

    print("\nPerformance comparison:")
    # Run main problem with performance measurement
    functions = [
        ("素直な解法 (Triangle-based)", lambda: solve_naive()),
        ("最適化解法 (Hexagonal-based)", lambda: solve_optimized()),
        ("数学的解法 (Mathematical properties)", lambda: solve_mathematical()),
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
