#!/usr/bin/env python3
"""
Problem 016: Power Digit Sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Answer: 1366
"""

import time


def solve_naive(power: int) -> int:
    """
    素直な解法
    2^powerを計算し、各桁の数字の和を求める

    時間計算量: O(power * log(2^power)) = O(power^2)
    空間計算量: O(power)
    """
    # 2^powerを計算
    result = 2**power

    # 各桁の数字の和を計算
    digit_sum = 0
    while result > 0:
        digit_sum += result % 10
        result //= 10

    return digit_sum


def solve_optimized(power: int) -> int:
    """
    最適化解法
    文字列変換を使用して桁の和を計算

    時間計算量: O(power * log(2^power)) = O(power^2)
    空間計算量: O(power)
    """
    # 2^powerを計算して文字列に変換
    result = str(2**power)

    # 各桁の数字の和を計算
    return sum(int(digit) for digit in result)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (15, 26),  # 2^15 = 32768 → 3+2+7+6+8 = 26
        (10, 7),  # 2^10 = 1024 → 1+0+2+4 = 7
        (5, 5),  # 2^5 = 32 → 3+2 = 5
        (0, 1),  # 2^0 = 1 → 1 = 1
        (1, 2),  # 2^1 = 2 → 2 = 2
        (2, 4),  # 2^2 = 4 → 4 = 4
        (3, 8),  # 2^3 = 8 → 8 = 8
        (4, 7),  # 2^4 = 16 → 1+6 = 7
    ]

    print("=== テストケース ===")
    for power, expected in test_cases:
        result_naive = solve_naive(power)
        result_optimized = solve_optimized(power)

        print(f"2^{power} の桁の和:")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
        )
        print()


def main() -> None:
    """メイン関数"""
    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")
    power = 1000

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(power)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(power)
    optimized_time = time.time() - start_time

    print(f"2^{power} の桁の和:")
    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized:
        print(f"✓ 解答: {result_optimized:,}")
    else:
        print("✗ 解答が一致しません")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")

    # 追加情報
    print("\n=== 追加情報 ===")
    result_number = 2**power
    print(f"2^{power} = {result_number}")
    print(f"桁数: {len(str(result_number))}")
    print(f"各桁の数字: {list(str(result_number))}")


if __name__ == "__main__":
    main()
