#!/usr/bin/env python3
"""
Runner for Problem 081: Path sum: two ways

This module contains the execution code for Problem 081, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_081 import load_matrix, solve_naive, solve_optimized
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
    print_test_results,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    # Test with the example matrix from the problem
    test_matrix = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]

    test_cases: list[tuple[list[list[int]], int]] = [
        # Single cell
        ([[5]], 5),
        # 2x2 matrix
        ([[1, 2], [3, 4]], 7),
        # 3x3 matrix
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 21),
        # Example matrix
        (test_matrix, 2427),
    ]

    functions = [
        ("素直な解法", lambda matrix: solve_naive(matrix)),
        ("最適化解法", lambda matrix: solve_optimized(matrix)),
    ]

    print_test_results(test_cases, functions)

    # Additional insights for the example matrix
    print("\n=== 問題例の分析 ===")
    print("経路の詳細:")
    print("131 -> 201 -> 96 -> 342 -> 746 -> 422 -> 121 -> 37 -> 331 = 2427")
    print("移動: 下 -> 右 -> 右 -> 下 -> 右 -> 下 -> 右 -> 下")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    print_solution_header("081", "Path sum: two ways", "80x80 matrix")

    # Run tests first
    run_tests()

    try:
        # Load the problem matrix
        matrix = load_matrix()
        rows, cols = len(matrix), len(matrix[0])

        print("\n=== 問題の行列 ===")
        print(f"サイズ: {rows}×{cols}")
        print(f"左上の値: {matrix[0][0]}")
        print(f"右下の値: {matrix[-1][-1]}")

        # For large matrices, only run the optimized solution
        # The naive solution would take too long (O(2^160))
        print(
            "\n注: 80×80の行列では素直な解法は計算量が膨大なため、最適化解法のみ実行します。"
        )

        functions = [("最適化解法", lambda: solve_optimized(matrix))]

        performance_results = compare_performance(functions)

        # Get the answer
        answer = performance_results["最適化解法"]["result"]
        print_final_answer(answer, verified=True)
        print_performance_comparison(performance_results)

        # Additional analysis
        print("\n=== 問題分析 ===")
        print(f"グリッドサイズ: {rows}×{cols}")
        print(f"総セル数: {rows * cols}")
        print(f"最短経路の長さ: {rows + cols - 1}セル")
        print(f"可能な経路数: {(rows + cols - 2)}! / ({rows - 1}! × {cols - 1}!)")

    except FileNotFoundError:
        print("\n⚠️  行列ファイルが見つかりません。")
        print("テスト用の小さい行列で実行します。")

        # Use a test matrix
        test_size = 10
        import random

        random.seed(81)
        test_matrix = [
            [random.randint(1, 100) for _ in range(test_size)]  # nosec B311
            for _ in range(test_size)
        ]

        functions = [
            ("素直な解法", lambda: solve_naive(test_matrix)),
            ("最適化解法", lambda: solve_optimized(test_matrix)),
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
    """Run performance benchmark for Problem 081."""
    print("=== Problem 081 Performance Benchmark ===")
    runner = Problem081Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


def main() -> None:
    """Main function for standalone execution."""
    run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
