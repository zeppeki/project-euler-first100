#!/usr/bin/env python3
"""
Runner for Problem 011: Largest product in a grid
"""

import time

from problems.problem_011 import (
    GRID_DATA,
    find_max_product_sequence,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    # 小さなテストグリッド
    test_grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    test_cases = [
        (test_grid, 4, 43680),  # 13×14×15×16 = 43680
    ]

    print("=== テストケース ===")
    for grid, length, expected in test_cases:
        result_naive = solve_naive(grid, length)
        result_optimized = solve_optimized(grid, length)
        result_math = solve_mathematical(grid, length)

        print(f"Grid size: {len(grid)}×{len(grid[0])}, Length: {length}")
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
    length = 4

    print("=== Problem 011: Largest product in a grid ===")
    print(f"Finding largest product of {length} adjacent numbers")
    print(f"Grid size: {len(GRID_DATA)}×{len(GRID_DATA[0])}")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(GRID_DATA, length)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(GRID_DATA, length)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(GRID_DATA, length)
    math_time = time.time() - start_time

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

    # 最大積のシーケンスを表示
    max_product, sequence, direction = find_max_product_sequence(GRID_DATA, length)
    print(f"最大積のシーケンス: {sequence}")
    print(f"方向: {direction}")
    print(f"積: {max_product:,}")
    print()

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")


if __name__ == "__main__":
    main()
