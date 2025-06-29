#!/usr/bin/env python3
"""
Problem 008 Runner: Largest product in a series

実行・表示・パフォーマンス測定を担当
"""

import os
import sys

# Add problems directory to path to import problem modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problem_008 import (
    THOUSAND_DIGIT_NUMBER,
    get_max_product_sequence,
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
        (1, 9),  # 1桁の最大値は9
        (2, 81),  # 2桁の最大積（例：9×9=81）
        (4, 5832),  # 問題例：4桁の場合は5832
        (13, 23514624000),  # 本問題：13桁の場合
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

    adjacent_digits = 13

    # 最大積となるシーケンスを表示
    max_sequence, max_product = get_max_product_sequence(adjacent_digits)
    print(f"最大積となる{adjacent_digits}桁のシーケンス: {max_sequence}")
    print(f"各桁: {' × '.join(max_sequence)}")
    print(f"積: {max_product:,}")

    # 問題例（4桁の場合）も表示
    print("\n問題例（4桁の場合）:")
    example_sequence, example_product = get_max_product_sequence(4)
    print(f"最大積となる4桁のシーケンス: {example_sequence}")
    print(f"各桁: {' × '.join(example_sequence)} = {example_product}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 全ての隣接するシーケンスをチェックして積を計算")
    print("最適化解法: ゼロを含むシーケンスをスキップするスライディングウィンドウ")
    print("数学的解法: reduce関数を使用した効率的な積計算とゼロスキップ")

    # 1000桁の数値に関する統計
    zero_count = THOUSAND_DIGIT_NUMBER.count("0")
    total_digits = len(THOUSAND_DIGIT_NUMBER)
    print("\n=== 1000桁数値の統計 ===")
    print(f"総桁数: {total_digits}")
    print(f"ゼロの個数: {zero_count}")
    print(f"ゼロの割合: {zero_count / total_digits * 100:.1f}%")
    print(f"最大桁: {max(THOUSAND_DIGIT_NUMBER)}")
    print(f"最小桁: {min(THOUSAND_DIGIT_NUMBER)}")


def run_problem() -> None:
    """Run the main problem solution with performance analysis."""
    adjacent_digits = 13

    print_solution_header(
        "008", "Largest product in a series", f"{adjacent_digits}桁の隣接する桁"
    )

    # Run tests first
    run_tests()

    # Solve the main problem
    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    performance_results = compare_performance(functions, adjacent_digits)

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
