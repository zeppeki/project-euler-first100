#!/usr/bin/env python3
"""
Runner for Problem 014: Longest Collatz sequence
"""

import time

from problems.problem_014 import (
    collatz_length_simple,
    solve_naive,
    solve_optimized,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (2, 1),  # 1のみ
        (3, 2),  # 1, 2
        (5, 3),  # 1, 2, 3, 4 -> 3が最長(8ステップ)
        (10, 9),  # 9が最長(20ステップ)
        (14, 9),  # 13も9も同じ長さだが9の方が小さい番号
        (20, 18),  # 18が最長(21ステップ) - 18と19は同じ長さだが18が小さい
    ]

    print("=== テストケース ===")
    for limit, expected in test_cases:
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        print(f"limit = {limit}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
        )

        # 詳細情報を表示
        length = collatz_length_simple(expected)
        print(f"  Length of chain from {expected}: {length}")
        print()


def main() -> None:
    """メイン関数"""
    limit = 1000000

    print("=== Problem 014: Longest Collatz sequence ===")
    print(
        f"Finding the starting number under {limit:,} that produces the longest chain"
    )
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(min(10000, limit))  # 素直な解法は時間がかかるので制限
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(limit)
    optimized_time = time.time() - start_time

    print(
        f"素直な解法 (limit={min(10000, limit):,}): {result_naive:,} (実行時間: {naive_time:.6f}秒)"
    )
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print()

    # 結果の検証
    print(f"✓ 解答: {result_optimized:,}")

    # 最長チェーンの詳細
    max_length = collatz_length_simple(result_optimized)
    print(f"✓ チェーンの長さ: {max_length:,}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 各数について個別にCollatz数列の長さを計算")
    print("最適化解法: メモ化を使用して計算済みの値を再利用")

    # Collatz予想の説明
    print("\n=== Collatz予想について ===")
    print("• 全ての正の整数はCollatz数列によって最終的に1に到達する")
    print("• 未証明だが、現在まで反例は見つかっていない")
    print("• 数学の未解決問題の一つ")

    # 具体例の表示
    print(f"\n=== {result_optimized}から始まるCollatz数列（最初の10項） ===")
    sequence = []
    n = result_optimized
    for _ in range(10):
        sequence.append(str(n))
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(" → ".join(sequence) + " → ...")


if __name__ == "__main__":
    main()
