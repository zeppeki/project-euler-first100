#!/usr/bin/env python3
"""
Runner for Problem 039: Integer right triangles

This module contains the execution code for Problem 039, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_039 import (
    count_solutions,
    get_solutions,
    solve_mathematical,
    solve_naive,
    solve_optimized,
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
    test_cases = [
        (12, 12),  # (3,4,5) の周囲が唯一の解
        (30, 12),  # p≤30の範囲では p=12 が最大解数
        (60, 60),  # p=60 が2つの解を持ち最大
        (120, 120),  # p=120 が3つの解を持ち最大
        (200, 120),  # p≤200の範囲では p=120 が最大
        (500, 420),  # p≤500の範囲では p=420 が最大
    ]

    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    print_test_results(test_cases, functions)


def run_analysis() -> None:
    """Run detailed analysis of the problem."""
    print("\n=== 詳細分析 ===")

    # 例題の分析
    print("\n例題: p = 120 の場合")
    solutions_120 = get_solutions(120)
    print(f"解の数: {count_solutions(120)}")
    print("解の一覧:")
    for i, (a, b, c) in enumerate(solutions_120, 1):
        print(
            f"  {i}. ({a}, {b}, {c}) -> {a}² + {b}² = {a * a} + {b * b} = {a * a + b * b} = {c}² = {c * c}"
        )

    # 小さな値での解の分布
    print("\n小さな周囲での解の数:")
    for p in range(12, 61, 12):
        count = count_solutions(p)
        if count > 0:
            solutions = get_solutions(p)
            print(f"  p = {p}: {count}個の解 -> {solutions}")

    # 解の数が多い周囲を探索
    print("\n解の数が多い周囲 (p ≤ 200):")
    solution_counts = []
    for p in range(12, 201):
        count = count_solutions(p)
        if count > 0:
            solution_counts.append((p, count))

    # 解の数でソートして上位を表示
    solution_counts.sort(key=lambda x: x[1], reverse=True)
    for p, count in solution_counts[:10]:
        print(f"  p = {p}: {count}個の解")


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    max_perimeter = 1000

    print_solution_header(
        problem_number="039", title="Integer right triangles", limit=max_perimeter
    )

    # 解法の実行と比較
    functions = [
        ("素直な解法", solve_naive, "O(n³)"),
        ("最適化解法", solve_optimized, "O(n²)"),
        ("数学的解法", solve_mathematical, "O(n√n)"),
    ]

    results = []
    for name, func, complexity in functions:
        result = func(max_perimeter)
        results.append((name, result, complexity))
        print(f"{name} ({complexity}): {result}")

    # 結果の一致確認
    if len({result for _, result, _ in results}) == 1:
        final_answer = results[0][1]
        print_final_answer(final_answer)

        # 最適解の詳細分析
        print("\n=== 最適解の詳細分析 ===")
        max_solution_count = count_solutions(final_answer)
        solutions = get_solutions(final_answer)

        print(f"周囲の長さ: {final_answer}")
        print(f"解の数: {max_solution_count}")
        print("解の一覧 (最初の10個):")
        for i, (a, b, c) in enumerate(solutions[:10], 1):
            print(f"  {i}. ({a}, {b}, {c})")

        if len(solutions) > 10:
            print(f"  ... (他に{len(solutions) - 10}個)")
    else:
        print("✗ エラー: 解法間で結果が一致しません")
        for name, result, _ in results:
            print(f"  {name}: {result}")

    # パフォーマンス比較
    performance_functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    smaller_limit = 100  # パフォーマンステスト用の小さな値
    performance_results = compare_performance(performance_functions, smaller_limit)
    print_performance_comparison(performance_results)


def main() -> None:
    """Main execution function."""
    run_tests()
    run_analysis()
    run_problem()


if __name__ == "__main__":
    main()
