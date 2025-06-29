#!/usr/bin/env python3
"""
Runner for Problem 019: Counting Sundays
"""

import os
import sys
import time

# Add problems directory to path to import problem modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from problem_019 import (
    solve_mathematical,
    solve_naive,
    solve_optimized,
    validate_days_in_month_calculation,
    validate_leap_year_calculation,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    print("=== 基本検証 ===")
    validate_leap_year_calculation()
    validate_days_in_month_calculation()

    # 小さな範囲でのテスト
    print("=== 小範囲テスト ===")
    test_ranges = [
        (1901, 1901),  # 1年だけ
        (1901, 1905),  # 5年
        (1901, 1910),  # 10年
    ]

    for start, end in test_ranges:
        result_naive = solve_naive(start, end)
        result_optimized = solve_optimized(start, end)
        result_math = solve_mathematical(start, end)

        print(f"{start}-{end}年の月初日曜日数:")
        print(f"  Naive: {result_naive}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == result_naive else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == result_naive else '✗'}"
        )
        print()


def main() -> None:
    """メイン関数"""
    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")
    start_year, end_year = 1901, 2000

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(start_year, end_year)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(start_year, end_year)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(start_year, end_year)
    math_time = time.time() - start_time

    print(f"{start_year}-{end_year}年の月初日曜日数:")
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
    print("1. 素直な解法: 日付を順次カウントして曜日を追跡")
    print("2. 最適化解法: Zellerの公式を使用した直接計算")
    print("3. 数学的解法: Python datetimeモジュールを活用")
    print()
    print("日付計算の要点:")
    print("- うるう年の正確な判定（400年ルール）")
    print("- 各月の日数の正確な計算")
    print("- 曜日計算の効率的な実装")

    # 検証情報
    print("\n=== 検証情報 ===")
    print("基準日: 1900年1月1日は月曜日")
    print("対象期間: 1901年1月1日〜2000年12月31日")
    print("計算対象: 各月の1日が日曜日だった回数")
    print(f"総月数: {(end_year - start_year + 1) * 12} ヶ月")


if __name__ == "__main__":
    main()
