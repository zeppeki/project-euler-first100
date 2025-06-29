#!/usr/bin/env python3
"""
Runner for Problem 013: Large sum
"""

import time

from problems.problem_013 import (
    get_fifty_digit_numbers,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    print("=== テストケース ===")

    # 小さなテストケース
    test_numbers = [
        "12345678901234567890123456789012345678901234567890",
        "98765432109876543210987654321098765432109876543210",
        "11111111111111111111111111111111111111111111111111",
    ]

    # テスト用の小さな関数
    def test_small_sum() -> str:
        total = sum(int(num) for num in test_numbers)
        return str(total)[:10]

    small_result = test_small_sum()
    print(f"小さなテストケース結果: {small_result}")

    # 本問題の解答
    result_naive = solve_naive()
    result_optimized = solve_optimized()
    result_math = solve_mathematical()

    print(f"Naive: {result_naive}")
    print(f"Optimized: {result_optimized}")
    print(f"Mathematical: {result_math}")

    # 検証
    if result_naive == result_optimized == result_math:
        print(f"✓ 全解法一致: {result_naive}")
    else:
        print("✗ 解法間で結果が異なります")


def main() -> None:
    """メイン関数"""
    print("=== Problem 013: Large sum ===")
    print("100個の50桁数字の合計の最初の10桁を求める")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("\n=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive()
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized()
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical()
    math_time = time.time() - start_time

    print(f"素直な解法: {result_naive} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math} (実行時間: {math_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized:
        print(f"✓ 解答: {result_naive}")
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

    numbers = get_fifty_digit_numbers()
    total_sum = sum(int(num) for num in numbers)

    print(f"数字の個数: {len(numbers)}")
    print(f"各数字の桁数: {len(numbers[0])}")
    print(f"合計値: {total_sum}")
    print(f"合計値の桁数: {len(str(total_sum))}")
    print(f"最初の10桁: {str(total_sum)[:10]}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: Pythonの大整数演算を使用して直接合計計算")
    print("最適化解法: 桁ごとに加算してキャリーオーバーを手動処理")
    print("数学的解法: 上位桁のみを使用した近似計算（最適化されたアプローチ）")


if __name__ == "__main__":
    main()
