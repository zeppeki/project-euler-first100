#!/usr/bin/env python3
"""
Problem 001 Runner: Execution and demonstration code for Problem 001.

This module handles the execution and demonstration of Problem 001 solutions,
separated from the core algorithm implementations.
"""

import os
import sys

# Add problems directory to path to import problem modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problem_001 import solve_naive, solve_optimized
from utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
    print_test_results,
)
from utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify solution correctness."""
    test_cases = [
        (10, 23),  # 3 + 5 + 6 + 9 = 23
        (20, 78),  # 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
        (100, 2318),  # Known result for limit 100
    ]

    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
    ]

    print_test_results(test_cases, functions)


def run_problem() -> None:
    """Run the main problem solution with performance analysis."""
    limit = 1000

    print_solution_header("001", "Multiples of 3 and 5", limit)

    # Run tests first
    run_tests()

    # Solve the main problem
    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
    ]

    performance_results = compare_performance(functions, limit)

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


def main() -> None:
    """Main entry point."""
    run_problem()


if __name__ == "__main__":
    main()
