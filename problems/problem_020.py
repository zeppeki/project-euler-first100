#!/usr/bin/env python3
"""
Problem 020: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Answer: 648
"""

import math
import time


def solve_naive(n: int) -> int:
    """
    素直な解法: math.factorialを使い、文字列変換して各桁を合計

    時間計算量: O(n log n) - 階乗計算
    空間計算量: O(log n) - 階乗の結果を格納
    """
    factorial = math.factorial(n)
    return sum(int(digit) for digit in str(factorial))


def solve_optimized(n: int) -> int:
    """
    最適化解法: 手動で階乗を計算し、各桁の和を求める

    時間計算量: O(n log n)
    空間計算量: O(log n)
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return sum(int(digit) for digit in str(factorial))


def solve_mathematical(n: int) -> int:
    """
    数学的解法: 段階的に階乗を計算しながら桁和を追跡

    時間計算量: O(n log n)
    空間計算量: O(1) - 階乗の中間結果を保持しない
    """
    factorial = 1
    digit_sum = 1  # 1! = 1の桁和

    if n == 0 or n == 1:
        return 1

    for i in range(2, n + 1):
        factorial *= i
        # 各段階で桁和を計算（メモリ効率のため）
        digit_sum = sum(int(digit) for digit in str(factorial))

    return digit_sum


def main() -> None:
    """メイン関数"""
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


if __name__ == "__main__":
    main()
