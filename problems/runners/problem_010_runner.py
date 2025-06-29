#!/usr/bin/env python3
"""
Problem 010 Runner: Summation of primes

実行・表示・パフォーマンス測定を担当
"""

import math
import os
import sys

# Add problems directory to path to import problem modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problem_010 import (
    sieve_of_eratosthenes,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
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
        (2, 0),  # 2未満の素数はなし
        (3, 2),  # 3未満の素数は2のみ
        (10, 17),  # 問題例: 2 + 3 + 5 + 7 = 17
        (30, 129),  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 = 129
        (100, 1060),  # 100未満の素数の和
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

    limit = 2000000

    # 最初の100までの素数の合計を表示
    small_limit = 100
    small_primes = sieve_of_eratosthenes(small_limit - 1)
    print(f"100未満の素数: {', '.join(map(str, small_primes))}")
    print(f"100未満の素数の和: {sum(small_primes)}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 各数を順次チェックして素数判定し合計")
    print("最適化解法: エラトステネスの篩で効率的に素数を生成し合計")
    print("数学的解法: メモリ最適化されたエラトステネスの篩（奇数のみ）")

    # 素数の密度
    prime_count = len(sieve_of_eratosthenes(limit - 1))
    density = prime_count / limit * 100
    print(f"\n{limit:,}未満の素数の個数: {prime_count:,}")
    print(f"素数の密度: {density:.3f}%")

    # 素数定理による近似
    approx_count = limit / math.log(limit)
    print(f"素数定理による近似個数: {approx_count:.0f}")
    print(f"実際の個数: {prime_count}")
    print(f"誤差: {abs(prime_count - approx_count):.0f}")


def run_problem() -> None:
    """Run the main problem solution with performance analysis."""
    limit = 2000000

    print_solution_header("010", "Summation of primes", "2,000,000未満の素数の和")

    # Run tests first
    run_tests()

    # Solve the main problem
    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
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

    # Show calculation details
    show_calculation_details()


def main() -> None:
    """Main entry point."""
    run_problem()


if __name__ == "__main__":
    main()
