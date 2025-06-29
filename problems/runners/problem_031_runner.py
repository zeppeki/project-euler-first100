#!/usr/bin/env python3
"""
Runner for Problem 031: Coin sums
"""

import time

from ..problem_031 import solve_naive, solve_optimized


def test_solutions() -> None:
    """テストケースで解答を検証"""
    # 5pを作る方法: 5p, 2p+2p+1p, 2p+1p+1p+1p, 1p+1p+1p+1p+1p
    result_5 = solve_optimized(5)
    print(f"5pを作る方法の数: {result_5}")

    result_10 = solve_optimized(10)  # 10pを作る方法
    print(f"10pを作る方法の数: {result_10}")

    # メイン問題のテスト（素直な解法は遅いので小さい値のみ）
    naive_10 = solve_naive(10)
    optimized_10 = solve_optimized(10)
    print(f"10p: 素直な解法={naive_10}, 最適化解法={optimized_10}")

    if naive_10 != optimized_10:
        print("✗ 解答が一致しません")
    else:
        print("✓ 解答が一致します")


def main() -> None:
    """メイン関数"""
    print("=== Problem 031: Coin sums ===")

    # テスト実行
    test_solutions()

    # 実際の問題を解く（200p = £2）
    start_time = time.time()
    result_optimized = solve_optimized(200)
    optimized_time = time.time() - start_time

    print(f"Optimized solution: {result_optimized}")
    print(f"Execution time (optimized): {optimized_time:.6f} seconds")

    # 小さい値での比較
    print("\nSmall test comparisons:")
    for test_val in [5, 10, 20]:
        start_time = time.time()
        naive_result = solve_naive(test_val)
        naive_time = time.time() - start_time

        start_time = time.time()
        opt_result = solve_optimized(test_val)
        opt_time = time.time() - start_time

        print(
            f"Target {test_val}p: Naive={naive_result} ({naive_time:.6f}s), "
            f"Optimized={opt_result} ({opt_time:.6f}s)"
        )


if __name__ == "__main__":
    main()
