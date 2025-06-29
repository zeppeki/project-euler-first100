#!/usr/bin/env python3
"""
Runner for Problem 012: Highly divisible triangular number
"""

import time

from problems.problem_012 import (
    count_divisors_optimized,
    get_divisors,
    get_triangular_number,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (0, 1),  # 0個より多い約数を持つ最初の三角数は1
        (1, 3),  # 1個より多い約数を持つ最初の三角数は3
        (2, 6),  # 2個より多い約数を持つ最初の三角数は6
        (3, 6),  # 3個より多い約数を持つ最初の三角数は6
        (4, 28),  # 4個より多い約数を持つ最初の三角数は28
        (5, 28),  # 5個より多い約数を持つ最初の三角数は28（問題例）
    ]

    print("=== テストケース ===")
    for target, expected in test_cases:
        result_naive = solve_naive(target)
        result_optimized = solve_optimized(target)
        result_math = solve_mathematical(target)

        print(f"target_divisors = {target}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}"
        )

        # 約数の詳細表示（小さい数の場合）
        if expected <= 100:
            divisors = get_divisors(expected)
            print(f"  Divisors of {expected}: {divisors} (count: {len(divisors)})")
        print()


def main() -> None:
    """メイン関数"""
    target_divisors = 500

    print("=== Problem 012: Highly divisible triangular number ===")
    print(f"Finding the first triangular number with over {target_divisors} divisors")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(target_divisors)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(target_divisors)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(target_divisors)
    math_time = time.time() - start_time

    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized == result_math:
        print(f"✓ 解答: {result_optimized:,}")

        # 詳細情報の表示
        n = 1
        while get_triangular_number(n) != result_optimized:
            n += 1

        divisor_count = count_divisors_optimized(result_optimized)
        print(f"この三角数は {n} 番目の三角数です")
        print(f"約数の個数: {divisor_count}")
    else:
        print("✗ 解答が一致しません")
        print(f"  Naive: {result_naive}")
        print(f"  Optimized: {result_optimized}")
        print(f"  Mathematical: {result_math}")
        return

    # パフォーマンス比較
    print("\n=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 詳細な計算過程の表示
    print("\n=== 計算過程の詳細 ===")

    # 最初の10個の三角数とその約数の個数を表示
    print("最初の10個の三角数と約数の個数:")
    for i in range(1, 11):
        triangular = get_triangular_number(i)
        divisor_count = count_divisors_optimized(triangular)
        divisors = get_divisors(triangular)
        print(f"T_{i} = {triangular}, divisors: {len(divisors)} {divisors}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 三角数を順次生成し、各数の約数を直接数える")
    print("最適化解法: 素因数分解を使用して約数の個数を効率的に計算")
    print("数学的解法: T_n = n(n+1)/2 の性質を利用してnとn+1から約数を計算")

    # 三角数の公式の説明
    print("\n三角数の公式: T_n = n(n+1)/2")
    print(f"答えの三角数 {result_optimized:,} は T_{n} です")


if __name__ == "__main__":
    main()
