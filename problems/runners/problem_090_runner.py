#!/usr/bin/env python3
"""
Runner for Problem 090: Cube digit pairs

This module contains the execution code for Problem 090, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_090 import solve_mathematical, solve_naive, solve_optimized
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
    print_test_results,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    # テストケース: 問題文の例のキューブで全ての平方数が作成可能
    from problems.problem_090 import can_form_square

    test_cases = [
        # キューブ例とその検証
        ("Example cubes can form all squares", True),
    ]

    # 問題文の例のキューブ
    cube1_example = {0, 5, 6, 7, 8, 9}
    cube2_example = {1, 2, 3, 4, 8, 9}
    squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]

    print("検証: 問題文の例のキューブで全ての平方数が作成可能")
    print(f"キューブ1: {sorted(cube1_example)}")
    print(f"キューブ2: {sorted(cube2_example)}")

    all_possible = True
    for square in squares:
        can_form = can_form_square(cube1_example, cube2_example, square)
        print(f"  {square}: {'✓' if can_form else '✗'}")
        if not can_form:
            all_possible = False

    print(f"結果: {'全て作成可能' if all_possible else '作成不可能な平方数あり'}")

    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    print_test_results(test_cases, functions)


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header("090", "Cube digit pairs", "全ての平方数を表示可能な配置数")

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


def run_benchmark() -> None:
    """Run performance benchmark for Problem 090."""
    print("=== Problem 090 Performance Benchmark ===")

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
