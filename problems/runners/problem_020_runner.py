#!/usr/bin/env python3
"""
Runner for Problem 020: Factorial digit sum
"""

import math
import time

from problems.problem_020 import solve_mathematical, solve_naive, solve_optimized


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (0, 1),  # 0! = 1 → 1
        (1, 1),  # 1! = 1 → 1
        (5, 3),  # 5! = 120 → 1+2+0 = 3
        (10, 27),  # 10! = 3628800 → 3+6+2+8+8+0+0 = 27
    ]

    print("=== テストケース ===")
    for n, expected in test_cases:
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)

        print(f"{n}! の桁の和:")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}"
        )
        print(f"  ({n}! = {math.factorial(n)})")
        print()


def main() -> None:
    """メイン関数"""
    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")
    n = 100

    # 各解法の実行と時間測定
    start_time = time.time()
    result_naive = solve_naive(n)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(n)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(n)
    math_time = time.time() - start_time

    print("100!の各桁の数字の合計:")
    print(f"  素直な解法: {result_naive} (実行時間: {naive_time:.6f}秒)")
    print(f"  最適化解法: {result_optimized} (実行時間: {optimized_time:.6f}秒)")
    print(f"  数学的解法: {result_math} (実行時間: {math_time:.6f}秒)")

    # 結果の検証
    if result_naive == result_optimized == result_math:
        print(f"\n✓ 解答: {result_naive}")
    else:
        print("\n✗ 解答が一致しません")
        print(f"  素直な解法: {result_naive}")
        print(f"  最適化解法: {result_optimized}")
        print(f"  数学的解法: {result_math}")

    # パフォーマンス比較
    print("\n=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 追加情報
    print("\n=== 追加情報 ===")
    factorial_100 = math.factorial(100)
    print(f"100! の桁数: {len(str(factorial_100))}")
    print(f"100! の最初の20桁: {str(factorial_100)[:20]}...")
    print(f"100! の最後の20桁: ...{str(factorial_100)[-20:]}")


if __name__ == "__main__":
    main()
