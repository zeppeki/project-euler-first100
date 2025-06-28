#!/usr/bin/env python3
"""
Runner for Problem 004: Largest palindrome product

This module contains the execution code for Problem 004, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_004 import is_palindrome, solve_mathematical, solve_naive, solve_optimized
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
        (1, 1, (9, 3, 3)),  # 1桁の場合: 3 * 3 = 9
        (2, 2, (9009, 91, 99)),  # 2桁の場合: 91 * 99 = 9009
    ]

    functions = [
        ("素直な解法", lambda min_d, max_d: solve_naive(min_d, max_d)[0]),
        ("最適化解法", lambda min_d, max_d: solve_optimized(min_d, max_d)[0]),
        ("数学的解法", lambda min_d, max_d: solve_mathematical(min_d, max_d)[0]),
    ]

    print("=== テストケース ===")
    for min_digits, max_digits, expected in test_cases:
        expected_palindrome, expected_factor1, expected_factor2 = expected

        result_naive = solve_naive(min_digits, max_digits)
        result_optimized = solve_optimized(min_digits, max_digits)
        result_math = solve_mathematical(min_digits, max_digits)

        print(f"Digits: {min_digits}-{max_digits}")
        print(
            f"  Expected: {expected_palindrome} = "
            f"{expected_factor1} × {expected_factor2}"
        )
        print(
            f"  Naive: {result_naive[0]} = {result_naive[1]} × {result_naive[2]} "
            f"{'✓' if result_naive[0] == expected_palindrome else '✗'}"
        )
        print(
            f"  Optimized: {result_optimized[0]} = "
            f"{result_optimized[1]} × {result_optimized[2]} "
            f"{'✓' if result_optimized[0] == expected_palindrome else '✗'}"
        )
        print(
            f"  Mathematical: {result_math[0]} = "
            f"{result_math[1]} × {result_math[2]} "
            f"{'✓' if result_math[0] == expected_palindrome else '✗'}"
        )
        print()


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    min_digits = 3
    max_digits = 3

    print_solution_header("004", "Largest palindrome product", 
                         f"product of {min_digits}-digit numbers")

    # Run tests first
    run_tests()

    # Run main problem with performance measurement
    functions = [
        ("素直な解法", lambda: solve_naive(min_digits, max_digits)),
        ("最適化解法", lambda: solve_optimized(min_digits, max_digits)),
        ("数学的解法", lambda: solve_mathematical(min_digits, max_digits)),
    ]

    performance_results = compare_performance(functions)

    # Verify all solutions agree
    results = [data["result"] for data in performance_results.values()]
    palindromes = [result[0] for result in results]
    all_agree = len(set(palindromes)) == 1

    print("=== 本問題の解答 ===")
    if all_agree:
        result = results[0]
        palindrome, factor1, factor2 = result
        print(
            f"✓ 解答: {palindrome:,} = {factor1} × {factor2}"
        )
        print()
        print_performance_comparison(performance_results)
        
        # 回文の検証
        print("\n=== 回文の検証 ===")
        print(f"数値: {palindrome}")
        print(f"文字列: {palindrome!s}")
        print(f"逆順: {str(palindrome)[::-1]}")
        print(f"回文: {'✓' if is_palindrome(palindrome) else '✗'}")
    else:
        print_final_answer(None, verified=False)
        print("Results:", palindromes)


def main() -> None:
    """Main function for standalone execution."""
    run_problem()


if __name__ == "__main__":
    main()