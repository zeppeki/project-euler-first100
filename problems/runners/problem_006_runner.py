#!/usr/bin/env python3
"""
Problem 006 Runner: Sum square difference

実行・表示・パフォーマンス測定を担当
"""

import os
import sys

# Add problems directory to path to import problem modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problem_006 import solve_mathematical, solve_naive, solve_optimized
from utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
    print_test_results,
)
from utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    test_cases: list[tuple[int, int]] = [
        (0, 0),  # n=0の場合
        (1, 0),  # n=1: 1² = 1, (1)² = 1, 差は0
        (2, 4),  # n=2: (1+2)² - (1²+2²) = 9 - 5 = 4
        (3, 22),  # n=3: (1+2+3)² - (1²+2²+3²) = 36 - 14 = 22
        (10, 2640),  # 問題例: n=10の場合
    ]

    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    print_test_results(test_cases, functions)


def show_calculation_details() -> None:
    """Show detailed calculation process."""
    print("\n=== 計算過程の詳細 ===")

    # n=10の例で詳細を表示
    example_n = 10
    print(f"例: n = {example_n}")

    # 平方の和
    sum_of_squares_example = sum(i * i for i in range(1, example_n + 1))
    print(f"平方の和: 1² + 2² + ... + {example_n}² = {sum_of_squares_example}")

    # 和の平方
    sum_of_numbers_example = sum(i for i in range(1, example_n + 1))
    square_of_sum_example = sum_of_numbers_example * sum_of_numbers_example
    print(
        f"和の平方: (1 + 2 + ... + {example_n})² = {sum_of_numbers_example}² = {square_of_sum_example}"
    )

    # 差
    difference_example = square_of_sum_example - sum_of_squares_example
    print(
        f"差: {square_of_sum_example} - {sum_of_squares_example} = {difference_example}"
    )

    # 公式の確認
    n = 100
    print(f"\n=== 公式の確認 (n={n}) ===")
    sum_formula = n * (n + 1) // 2
    sum_of_squares_formula = n * (n + 1) * (2 * n + 1) // 6
    print(f"1 + 2 + ... + {n} = {n}×{n + 1}/2 = {sum_formula}")
    print(
        f"1² + 2² + ... + {n}² = {n}×{n + 1}×{2 * n + 1}/6 = {sum_of_squares_formula}"
    )
    print(f"和の平方: {sum_formula}² = {sum_formula * sum_formula:,}")
    print(f"平方の和: {sum_of_squares_formula:,}")

    result = solve_optimized(n)
    print(
        f"差: {sum_formula * sum_formula:,} - {sum_of_squares_formula:,} = {result:,}"
    )


def run_problem() -> None:
    """Run the main problem solution with performance analysis."""
    n = 100

    print_solution_header("006", "Sum square difference", n)

    # Run tests first
    run_tests()

    # Solve the main problem
    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    performance_results = compare_performance(functions, n)

    # Verify all solutions agree
    results = [data["result"] for data in performance_results.values()]
    verified = len(set(results)) == 1

    # Print results
    for name, data in performance_results.items():
        result = data["result"]
        execution_time = data["execution_time"]
        print(f"{name}: {result:,} (実行時間: {execution_time:.6f}秒)")

    print()
    print_final_answer(results[0], verified)
    print_performance_comparison(performance_results)

    # Show calculation details
    show_calculation_details()


def main() -> None:
    """Main entry point."""
    run_problem()


if __name__ == "__main__":
    main()
