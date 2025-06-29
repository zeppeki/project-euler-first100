#!/usr/bin/env python3
"""
Runner for Problem 028: Number spiral diagonals
"""

import time

from ..problem_028 import solve_mathematical, solve_naive, solve_optimized


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (1, 1),
        (3, 25),  # 1 + 3 + 5 + 7 + 9 = 25
        (5, 101),  # 問題文の例
    ]

    print("=== テストケース ===")
    for size, expected in test_cases:
        result_naive = solve_naive(size)
        result_optimized = solve_optimized(size)
        result_mathematical = solve_mathematical(size)

        print(f"Size: {size}×{size}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
        )
        print(
            f"  Mathematical: {result_mathematical} {'✓' if result_mathematical == expected else '✗'}"
        )
        print()


def main() -> None:
    """メイン関数"""
    print("=== Problem 028: Number spiral diagonals ===")

    # テストケース
    test_solutions()

    # 本問題の解答
    size = 1001
    print(f"Size: {size}×{size}")
    print()

    # パフォーマンス測定と結果表示
    start_time = time.time()
    result_optimized = solve_optimized(size)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_mathematical = solve_mathematical(size)
    mathematical_time = time.time() - start_time

    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_mathematical:,} (実行時間: {mathematical_time:.6f}秒)")
    print()

    # 結果の検証
    if result_optimized == result_mathematical:
        print(f"✓ 解答: {result_mathematical:,}")
    else:
        print("✗ 解答が一致しません")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(optimized_time, mathematical_time)
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {mathematical_time / fastest_time:.2f}x")


if __name__ == "__main__":
    main()
