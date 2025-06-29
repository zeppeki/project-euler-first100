#!/usr/bin/env python3
"""
Runner for Problem 017: Number Letter Counts
"""

import time

from problems.problem_017 import (
    count_letters,
    number_to_words,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    # 基本的なテストケース
    test_cases = [
        (1, "one", 3),
        (2, "two", 3),
        (5, "five", 4),
        (12, "twelve", 6),
        (21, "twenty one", 9),
        (42, "forty two", 8),
        (115, "one hundred and fifteen", 20),
        (342, "three hundred and forty two", 23),
        (1000, "one thousand", 11),
    ]

    print("=== 個別テストケース ===")
    for num, expected_words, expected_letters in test_cases:
        actual_words = number_to_words(num)
        actual_letters = count_letters(actual_words)

        print(f"{num}: '{actual_words}' ({actual_letters} letters)")
        print(f"  Expected: '{expected_words}' ({expected_letters} letters)")
        print(f"  Words: {'✓' if actual_words == expected_words else '✗'}")
        print(f"  Letters: {'✓' if actual_letters == expected_letters else '✗'}")
        print()

    # 範囲テストケース
    range_test_cases = [
        (5, 19),  # 1-5: one(3) + two(3) + three(5) + four(4) + five(4) = 19
        (20, 112),  # 予想される値
    ]

    print("=== 範囲テストケース ===")
    for limit, expected in range_test_cases:
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_math = solve_mathematical(limit)

        print(f"1-{limit} の文字数合計:")
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
    limit = 1000

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

    print(f"1-{limit} の文字数合計:")
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
    print("\n=== 追加情報 ===")
    print("イギリス式表記の特徴:")
    print("- 100以上の数では 'and' を使用")
    print("- 例: 115 = 'one hundred and fifteen'")
    print("- 例: 342 = 'three hundred and forty two'")
    print(f"- 1000 = 'one thousand' ({count_letters(number_to_words(1000))} letters)")


if __name__ == "__main__":
    main()
