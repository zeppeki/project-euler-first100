#!/usr/bin/env python3
"""
Runner for Problem 049: Prime permutations

This module contains the execution code for Problem 049, separated from the
algorithm implementations for better test coverage and code organization.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

from problems.problem_049 import (
    find_arithmetic_sequences,
    get_digit_signature,
    get_permutations,
    is_prime,
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
    print("Testing prime permutation calculations:")

    # Test prime checking
    print("  Prime checking tests:")
    prime_tests = [
        (1487, True),
        (4817, True),
        (8147, True),
        (1000, False),
        (1001, False),
        (1009, True),
        (9999, False),
    ]

    for num, expected in prime_tests:
        result = is_prime(num)
        print(f"    is_prime({num}) = {result} {'✓' if result == expected else '✗'}")

    # Test digit signature
    print("\n  Digit signature tests:")
    signature_tests = [
        (1487, "1478"),
        (4817, "1478"),
        (8147, "1478"),
        (1234, "1234"),
        (4321, "1234"),
    ]

    for number, expected_sig in signature_tests:
        signature_result = get_digit_signature(number)
        print(
            f"    get_digit_signature({number}) = '{signature_result}' {'✓' if signature_result == expected_sig else '✗'}"
        )

    # Test permutation generation
    print("\n  Permutation generation tests:")
    perms_1487 = get_permutations(1487)

    # Check if known permutations are included
    known_perms = [1487, 4817, 8147]
    all_included = all(p in perms_1487 for p in known_perms)
    print(
        f"    Permutations of 1487 include known sequence: {'✓' if all_included else '✗'}"
    )
    print(f"    Total permutations of 1487: {len(perms_1487)}")

    # Test arithmetic sequence finding
    print("\n  Arithmetic sequence tests:")
    test_numbers = [1487, 4817, 8147]
    sequences = find_arithmetic_sequences(test_numbers)
    expected_sequence = (1487, 4817, 8147)
    found_expected = expected_sequence in sequences
    print(
        f"    Found known sequence (1487, 4817, 8147): {'✓' if found_expected else '✗'}"
    )

    if sequences:
        for seq in sequences:
            diff1 = seq[1] - seq[0]
            diff2 = seq[2] - seq[1]
            is_arithmetic = diff1 == diff2
            print(
                f"    Sequence {seq}: difference = {diff1} {'✓' if is_arithmetic else '✗'}"
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

        # Verify the result format (should be 12 digits)
        result_str = str(results[0])
        if len(result_str) == 12:
            # Extract the three 4-digit numbers
            a = int(result_str[0:4])
            b = int(result_str[4:8])
            c = int(result_str[8:12])

            print(f"  ✓ Result format: {a}, {b}, {c}")

            # Verify they are all prime
            all_prime = all(is_prime(x) for x in [a, b, c])
            print(f"  ✓ All numbers are prime: {'✓' if all_prime else '✗'}")

            # Verify they form arithmetic sequence
            diff1 = b - a
            diff2 = c - b
            is_arithmetic = diff1 == diff2
            print(
                f"  ✓ Forms arithmetic sequence (diff={diff1}): {'✓' if is_arithmetic else '✗'}"
            )

            # Verify they are permutations of each other
            sig_a = get_digit_signature(a)
            sig_b = get_digit_signature(b)
            sig_c = get_digit_signature(c)
            are_permutations = sig_a == sig_b == sig_c
            print(
                f"  ✓ All are permutations of each other: {'✓' if are_permutations else '✗'}"
            )

            # Verify it's not the known example
            is_not_known = (a, b, c) != (1487, 4817, 8147)
            print(f"  ✓ Different from known example: {'✓' if is_not_known else '✗'}")

        else:
            print(f"  ✗ Result should be 12 digits, got {len(result_str)} digits")
    else:
        print(f"  ✗ Solutions disagree: {results}")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header(
        "049", "Prime permutations", "Arithmetic sequences in prime permutation groups"
    )

    # Run tests first
    run_tests()

    print("\nPerformance comparison:")
    # Run main problem with performance measurement
    functions = [
        ("素直な解法 (Brute force with basic primality)", lambda: solve_naive()),
        ("最適化解法 (Sieve of Eratosthenes)", lambda: solve_optimized()),
        (
            "数学的解法 (Optimized arithmetic sequence search)",
            lambda: solve_mathematical(),
        ),
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
