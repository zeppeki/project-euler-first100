#!/usr/bin/env python3
"""
Problem 007 Runner: 10001st prime

実行・表示・パフォーマンス測定を担当
"""

import os
import sys

# Add problems directory to path to import problem modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problem_007 import solve_mathematical, solve_naive, solve_optimized
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
        (1, 2),  # 1番目の素数は2
        (2, 3),  # 2番目の素数は3
        (3, 5),  # 3番目の素数は5
        (4, 7),  # 4番目の素数は7
        (5, 11),  # 5番目の素数は11
        (6, 13),  # 6番目の素数は13（問題例）
        (10, 29),  # 10番目の素数は29
        (25, 97),  # 25番目の素数は97
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

    # 最初の10個の素数を表示
    print("最初の10個の素数:")
    primes = []
    for i in range(1, 11):
        prime = solve_optimized(i)
        primes.append(prime)
        print(f"{i:2d}番目: {prime}")

    print(f"\n素数列: {', '.join(map(str, primes))}")

    # 素数定理による近似
    n = 10001
    import math

    if n >= 6:
        approx = n * (math.log(n) + math.log(math.log(n)))
        print("\n=== 素数定理による近似 ===")
        print(f"{n}番目の素数の近似上限: {approx:.0f}")
        print("実際の値と比較することで精度を確認できます")

    # アルゴリズムの特徴説明
    print("\n=== アルゴリズムの特徴 ===")
    print("1. 素直な解法: 各数を順次素数判定")
    print("2. 最適化解法: エラトステネスの篩で効率的に素数生成")
    print("3. 数学的解法: 6k±1の形の数のみをチェックして効率化")


def run_problem() -> None:
    """Run the main problem solution with performance analysis."""
    n = 10001

    print_solution_header("007", "10001st prime", f"{n}番目の素数")

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
