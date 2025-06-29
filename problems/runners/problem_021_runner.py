#!/usr/bin/env python3
"""
Runner for Problem 021: Amicable Numbers
"""

import time

from problems.problem_021 import (
    find_amicable_pairs,
    get_proper_divisors_optimized,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    validate_amicable_pair,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    print("=== 基本テスト ===")

    # 既知の友愛数ペア
    print("220の真約数の和:", get_proper_divisors_optimized(220))
    print("284の真約数の和:", get_proper_divisors_optimized(284))
    print("220と284は友愛数か:", validate_amicable_pair(220, 284))
    print()

    # 小さい範囲でのテスト
    test_limits = [300, 1000]

    for limit in test_limits:
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_math = solve_mathematical(limit)

        print(f"{limit}未満の友愛数の和:")
        print(f"  Naive: {result_naive}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == result_naive else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == result_naive else '✗'}"
        )

        # 友愛数ペアの詳細表示
        pairs = find_amicable_pairs(limit)
        print(f"  友愛数ペア: {pairs}")
        print()


def main() -> None:
    """メイン関数"""
    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")
    limit = 10000

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(limit)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(limit)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(limit)
    math_time = time.time() - start_time

    print(f"{limit}未満の友愛数の和:")
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

    # 友愛数ペアの表示
    print("\n=== 友愛数ペア一覧 ===")
    pairs = find_amicable_pairs(limit)
    for a, b in pairs:
        print(f"({a}, {b}): d({a}) = {b}, d({b}) = {a}")

    print(f"\n総計: {len(pairs)}組の友愛数ペア")
    print(f"友愛数の個数: {len(pairs) * 2}個")

    # アルゴリズム解説
    print("\n=== アルゴリズム解説 ===")
    print("1. 素直な解法: 各数で1からn-1まで全約数をチェック O(n²)")
    print("2. 最適化解法: 平方根まで試し割りで約数計算を効率化 O(n√n)")
    print("3. 数学的解法: エラトステネス篩的前処理で一括計算 O(n√n)")
    print()
    print("友愛数の性質:")
    print("- d(a) = b かつ d(b) = a (a ≠ b)")
    print("- 完全数 (d(n) = n) は友愛数ではない")
    print("- 真約数は自分自身を含まない約数")


if __name__ == "__main__":
    main()
