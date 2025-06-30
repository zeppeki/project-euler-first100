#!/usr/bin/env python3
"""
Runner for Problem 042: Coded triangle numbers

This module contains the execution code for Problem 042, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_042 import (
    get_word_value,
    is_triangle_number,
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
    # Test with known triangle words and non-triangle words
    test_cases = [
        # Format: (function_name, word, expected_is_triangle)
        ("SKY example", "SKY", True),  # 19+11+25=55, which is t10
        ("Simple A", "A", True),  # 1, which is t1
        ("Simple B", "B", False),  # 2, which is not a triangle number
    ]

    print("Testing word value calculations and triangle number detection:")
    for description, word, expected_is_triangle in test_cases:
        word_value = get_word_value(word)
        is_triangle = is_triangle_number(word_value)
        status = "✓" if is_triangle == expected_is_triangle else "✗"
        print(
            f"  {status} {description}: '{word}' = {word_value} ({'triangle' if is_triangle else 'not triangle'})"
        )

    print("\nTesting solution functions:")
    # Both solutions should return the same result
    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
    ]

    # Run each function and compare results
    results = []
    for name, func in functions:
        try:
            result = func()
            results.append(result)
            print(f"  ✓ {name}: {result}")
        except Exception as e:
            print(f"  ✗ {name}: Error - {e}")
            return  # Early return on error instead of appending None

    if len(set(results)) == 1 and results[0] is not None:
        print(f"  ✓ All solutions agree: {results[0]}")
    else:
        print(f"  ✗ Solutions disagree: {results}")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header("042", "Coded triangle numbers", "~2000 English words")

    # Run tests first
    run_tests()

    print("\nPerformance comparison:")
    # Run main problem with performance measurement
    functions = [
        ("素直な解法 (Set lookup)", lambda: solve_naive()),
        ("最適化解法 (Mathematical)", lambda: solve_optimized()),
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
