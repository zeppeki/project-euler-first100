"""
Runner for Problem 083: Path sum: four ways
"""

from problems.problem_083 import load_matrix, solve_naive, solve_optimized
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
    print_test_results,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases."""
    # Test cases: (matrix, expected_result)
    test_cases = [
        # Single cell
        ([[5]], 5),
        # Single row
        ([[1, 2, 3]], 6),
        # Single column
        ([[1], [2], [3]], 6),
        # 2x2 matrix
        ([[1, 2], [3, 4]], 7),
        # 3x3 matrix
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 21),
        # Example from problem statement
        (
            [
                [131, 673, 234, 103, 18],
                [201, 96, 342, 965, 150],
                [630, 803, 746, 422, 111],
                [537, 699, 497, 121, 956],
                [805, 732, 524, 37, 331],
            ],
            2297,
        ),
    ]

    functions = [
        ("solve_naive", solve_naive),
        ("solve_optimized", solve_optimized),
    ]

    print_test_results(test_cases, functions)


def run_problem() -> None:
    """Run the main problem."""
    matrix_file = "data/p083_matrix.txt"

    try:
        # Load the matrix
        matrix = load_matrix(matrix_file)
        print(f"Loaded {len(matrix)}x{len(matrix[0])} matrix from {matrix_file}")
        print()

        # For large matrices, only use optimized solution
        # as naive solution would be too slow
        if len(matrix) > 10:
            print("Matrix is large, using only optimized solution...")
            from problems.utils.performance import measure_performance

            result, execution_time = measure_performance(solve_optimized, matrix)
            print(f"Result: {result}")
            print(f"Execution time: {execution_time:.6f}s")
            print()
            print_final_answer(result)
        else:
            # Compare performance for smaller matrices
            functions = [
                ("solve_naive", lambda: solve_naive(matrix)),
                ("solve_optimized", lambda: solve_optimized(matrix)),
            ]

            results = compare_performance(functions)

            # Verify all solutions give the same result
            all_results = [data["result"] for data in results.values()]
            if len(set(all_results)) == 1:
                print_final_answer(all_results[0])
            else:
                print("✗ Solutions do not agree!")
                for name, data in results.items():
                    print(f"  {name}: {data['result']}")
                print()

            print_performance_comparison(results)

    except FileNotFoundError:
        print(f"Error: Could not find matrix file '{matrix_file}'")
        print("Please ensure the data file exists.")
        print("\nRunning example case instead:")

        # Run example case
        example_matrix = [
            [131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331],
        ]

        functions = [
            ("solve_naive", lambda: solve_naive(example_matrix)),
            ("solve_optimized", lambda: solve_optimized(example_matrix)),
        ]

        results = compare_performance(functions)
        all_results = [data["result"] for data in results.values()]

        if len(set(all_results)) == 1:
            print_final_answer(all_results[0])

        print_performance_comparison(results)


def main() -> None:
    """Main function."""
    print_solution_header("083", "Path sum: four ways")

    print("Running tests...\n")
    run_tests()

    print("\nSolving main problem...\n")
    run_problem()


if __name__ == "__main__":
    main()
