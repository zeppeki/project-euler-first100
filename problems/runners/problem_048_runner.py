#!/usr/bin/env python3
"""
Runner for Problem 048: Self powers

This module contains the execution code for Problem 048, separated from the
algorithm implementations for better test coverage and code organization.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

from problems.problem_048 import (
    calculate_self_powers_sum,
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
    print("Testing self power calculations:")

    # Test small cases first
    print("  Small test cases:")
    test_cases = [
        (1, 1),  # 1^1 = 1
        (2, 5),  # 1^1 + 2^2 = 1 + 4 = 5
        (3, 32),  # 1^1 + 2^2 + 3^3 = 1 + 4 + 27 = 32
        (4, 288),  # 1^1 + 2^2 + 3^3 + 4^4 = 1 + 4 + 27 + 256 = 288
    ]

    for limit, expected in test_cases:
        # Test full calculation for small cases
        full_result = calculate_self_powers_sum(limit)
        full_correct = full_result == expected

        # Test modular calculations
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_mathematical = solve_mathematical(limit)

        expected_mod = expected % (10**10)
        naive_correct = result_naive == expected_mod
        opt_correct = result_optimized == expected_mod
        math_correct = result_mathematical == expected_mod
        all_correct = naive_correct and opt_correct and math_correct

        print(f"    Limit {limit}: Expected {expected}")
        print(f"      Full calculation: {full_result} {'✓' if full_correct else '✗'}")
        print(f"      Naive (mod): {result_naive} {'✓' if naive_correct else '✗'}")
        print(
            f"      Optimized (mod): {result_optimized} {'✓' if opt_correct else '✗'}"
        )
        print(
            f"      Mathematical (mod): {result_mathematical} {'✓' if math_correct else '✗'}"
        )
        print(f"      All mod results agree: {'✓' if all_correct else '✗'}")

    # Test the example from problem statement
    print("\n  Testing problem example:")
    example_limit = 10
    expected_example = 10405071317

    # Test full calculation
    full_example = calculate_self_powers_sum(example_limit)
    print(f"    1^1 + 2^2 + ... + 10^10 = {expected_example}")
    print(
        f"      Full calculation: {full_example} {'✓' if full_example == expected_example else '✗'}"
    )

    # Test modular calculations
    result_naive = solve_naive(example_limit)
    result_optimized = solve_optimized(example_limit)
    result_mathematical = solve_mathematical(example_limit)

    expected_mod = expected_example % (10**10)
    print(
        f"      Naive (mod): {result_naive} {'✓' if result_naive == expected_mod else '✗'}"
    )
    print(
        f"      Optimized (mod): {result_optimized} {'✓' if result_optimized == expected_mod else '✗'}"
    )
    print(
        f"      Mathematical (mod): {result_mathematical} {'✓' if result_mathematical == expected_mod else '✗'}"
    )

    # Test individual power calculations
    print("\n  Testing individual powers:")
    individual_tests = [
        (1, 1, 1),  # 1^1 = 1
        (2, 2, 4),  # 2^2 = 4
        (3, 3, 27),  # 3^3 = 27
        (4, 4, 256),  # 4^4 = 256
        (5, 5, 3125),  # 5^5 = 3125
    ]

    for base, exp, expected in individual_tests:
        if base == exp:  # Self power case
            result = pow(base, exp)
            print(f"    {base}^{exp} = {result} {'✓' if result == expected else '✗'}")

    print("\nTesting solution functions:")
    # Test that all functions return the same result for various limits
    test_limits = [5, 10, 50]

    for limit in test_limits:
        print(f"\n  Testing with limit {limit}:")

        functions: list[tuple[str, Callable[[int], int]]] = [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

        results: list[int] = []
        for name, func in functions:
            try:
                func_result = func(limit)
                results.append(func_result)
                print(f"    ✓ {name}: {func_result}")
            except Exception as e:
                print(f"    ✗ {name}: Error - {e}")
                return

        if len(set(results)) == 1:
            print(f"    ✓ All solutions agree: {results[0]}")
        else:
            print(f"    ✗ Solutions disagree: {results}")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header(
        "048", "Self powers", "Modular arithmetic and large number computation"
    )

    # Run tests first
    run_tests()

    print("\nPerformance comparison:")
    # Run main problem with performance measurement
    functions = [
        ("素直な解法 (Direct calculation)", lambda: solve_naive()),
        ("最適化解法 (Modular arithmetic)", lambda: solve_optimized()),
        ("数学的解法 (Optimized for multiples)", lambda: solve_mathematical()),
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
