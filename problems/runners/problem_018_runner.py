#!/usr/bin/env python3
"""
Runner for Problem 018: Maximum Path Sum I
"""

import time

from problems.problem_018 import (
    get_example_triangle,
    get_problem_triangle,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    print("=== 例題テスト ===")
    example_triangle = get_example_triangle()
    expected_example = 23

    result_naive = solve_naive(example_triangle)
    result_optimized = solve_optimized(example_triangle)
    result_math = solve_mathematical(example_triangle)

    print("例題三角形の最大パス合計:")
    print(f"  Expected: {expected_example}")
    print(f"  Naive: {result_naive} {'✓' if result_naive == expected_example else '✗'}")
    print(
        f"  Optimized: {result_optimized} {'✓' if result_optimized == expected_example else '✗'}"
    )
    print(
        f"  Mathematical: {result_math} {'✓' if result_math == expected_example else '✗'}"
    )
    print()

    # 小さなテストケース
    print("=== 追加テストケース ===")
    small_triangles = [
        # 単一要素
        ([[5]], 5),
        # 2行
        ([[1], [2, 3]], 4),  # 1 + 3 = 4
        # 3行
        ([[1], [2, 3], [4, 5, 6]], 10),  # 1 + 3 + 6 = 10
    ]

    for i, (triangle, expected) in enumerate(small_triangles, 1):
        result_naive = solve_naive(triangle)
        result_optimized = solve_optimized(triangle)
        result_math = solve_mathematical(triangle)

        print(f"テストケース {i}:")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}"
        )
        print()


def main() -> None:
    """メイン関数"""
    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")
    triangle = get_problem_triangle()

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(triangle)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(triangle)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(triangle)
    math_time = time.time() - start_time

    print("15行三角形の最大パス合計:")
    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized == result_math:
        print(f"✓ 解答: {result_optimized:,}")
    else:
        print("✗ 解答が一致しません")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 追加情報
    print("\n=== アルゴリズム解説 ===")
    print("1. 素直な解法: 全経路を再帰的に探索（指数時間）")
    print("2. 最適化解法: メモ化による動的プログラミング（O(n²)）")
    print("3. 数学的解法: ボトムアップDP、空間効率的（O(n²)時間、O(n)空間）")
    print()
    print("ボトムアップDPの利点:")
    print("- 底辺から計算するため、各位置で最適解が確定")
    print("- 再帰オーバーヘッドがない")
    print("- メモリ使用量が少ない")


if __name__ == "__main__":
    main()
