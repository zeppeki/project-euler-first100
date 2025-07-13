#!/usr/bin/env python3
"""
Runner for Problem 080: Square root digital expansion

This module contains the execution code for Problem 080, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_080 import (
    get_irrational_square_roots,
    solve_naive,
    solve_optimized,
    validate_sqrt_calculation,
)
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
    print_test_results,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    # Test with smaller precision for faster testing
    test_cases: list[tuple[tuple[int, int], int]] = [
        # (limit, precision), expected_output
        ((4, 5), 25),  # √2 + √3 with 5 digits each (12 + 13 = 25)
        ((4, 10), 62),  # √2 + √3 with 10 digits each (29 + 33 = 62)
    ]

    functions = [
        ("素直な解法", lambda args: solve_naive(*args)),
        ("最適化解法", lambda args: solve_optimized(*args)),
    ]

    print_test_results(test_cases, functions)

    # Additional validation tests
    print("\n=== 検証テスト ===")

    # Test square root calculation validation
    test_numbers = [2, 3, 5, 7, 8, 10]
    print("平方根計算の精度検証:")
    for n in test_numbers:
        is_valid = validate_sqrt_calculation(n, precision=20)
        print(f"  √{n}: {'✓' if is_valid else '✗'}")

    # Show irrational square roots in range 1-20
    irrational_roots = get_irrational_square_roots(20)
    print(f"\n1-20の無理数平方根: {irrational_roots}")
    print(f"完全平方数を除外した数: {len(irrational_roots)}個")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    limit = 100
    precision = 100

    print_solution_header(
        "080", "Square root digital expansion", f"limit={limit}, precision={precision}"
    )

    # Run tests first
    run_tests()

    # Run main problem with performance measurement
    functions = [
        ("素直な解法", lambda: solve_naive(limit, precision)),
        ("最適化解法", lambda: solve_optimized(limit, precision)),
    ]

    performance_results = compare_performance(functions)

    # Verify all solutions agree
    results = [data["result"] for data in performance_results.values()]
    all_agree = len(set(results)) == 1

    if all_agree:
        answer = results[0]
        print_final_answer(answer, verified=True)
        print_performance_comparison(performance_results)

        # Additional insights
        irrational_count = len(get_irrational_square_roots(limit))
        print("\n=== 問題分析 ===")
        print(f"対象数値範囲: 1-{limit}")
        print(f"無理数平方根の数: {irrational_count}個")
        print(f"計算精度: {precision}桁")
        print(f"平均デジタル和: {answer / irrational_count:.2f}")

    else:
        print_final_answer(None, verified=False)
        print("Results:", results)


def run_benchmark() -> None:
    """Run performance benchmark for Problem 080."""
    print("=== Problem 080 Performance Benchmark ===")
    
    # Run the main function which handles the problem
    main()


def main() -> None:
    """Main function for standalone execution."""
    run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
