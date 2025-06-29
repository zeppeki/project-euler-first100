#!/usr/bin/env python3
"""
Problem 009 Runner: Special Pythagorean triplet

実行・表示・パフォーマンス測定を担当
"""

import os
import sys

# Add problems directory to path to import problem modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problem_009 import (
    find_pythagorean_triplet,
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
        (12, 60),  # (3, 4, 5): 3+4+5=12, 3*4*5=60
        (30, 780),  # (5, 12, 13): 5+12+13=30, 5*12*13=780
        (24, 480),  # (6, 8, 10): 6+8+10=24, 6*8*10=480
        (1000, 31875000),  # 本問題の解答
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

    target_sum = 1000

    # ピタゴラス数の組を表示
    triplet = find_pythagorean_triplet(target_sum)
    if triplet:
        a, b, c = triplet
        print(f"ピタゴラス数の組: ({a}, {b}, {c})")
        print("条件確認:")
        print(f"  a < b < c: {a} < {b} < {c} {'✓' if a < b < c else '✗'}")
        print(
            f"  a + b + c = {target_sum}: {a} + {b} + {c} = {a + b + c} {'✓' if a + b + c == target_sum else '✗'}"
        )
        print(
            f"  a² + b² = c²: {a}² + {b}² = {a * a} + {b * b} = {a * a + b * b} = {c * c} = {c}² {'✓' if a * a + b * b == c * c else '✗'}"
        )
        print(f"  積 abc: {a} × {b} × {c} = {a * b * c:,}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 3重ループで全ての (a, b, c) の組み合わせをチェック")
    print("最適化解法: 2重ループで c = target_sum - a - b として計算")
    print("数学的解法: 原始ピタゴラス数の生成公式 (m² - n², 2mn, m² + n²) を使用")

    # ピタゴラス数に関する数学的背景
    print("\n=== 数学的背景 ===")
    print("ピタゴラスの定理: a² + b² = c²")
    print("原始ピタゴラス数: gcd(a, b, c) = 1 となるピタゴラス数")
    print("ユークリッドの公式: a = m² - n², b = 2mn, c = m² + n²")
    print("  条件: m > n > 0, gcd(m, n) = 1, m と n の一方は偶数")

    # 小さな例での説明
    print("\n=== 小さな例での説明 ===")
    small_examples = [12, 30, 24]
    for example_sum in small_examples:
        example_triplet = find_pythagorean_triplet(example_sum)
        if example_triplet:
            a, b, c = example_triplet
            print(f"a + b + c = {example_sum}: ({a}, {b}, {c}), 積 = {a * b * c}")
        else:
            print(f"a + b + c = {example_sum}: 解なし")


def run_problem() -> None:
    """Run the main problem solution with performance analysis."""
    target_sum = 1000

    print_solution_header(
        "009", "Special Pythagorean triplet", f"a + b + c = {target_sum}"
    )

    # Run tests first
    run_tests()

    # Solve the main problem
    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    performance_results = compare_performance(functions, target_sum)

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
