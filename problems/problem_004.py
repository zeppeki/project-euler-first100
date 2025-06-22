#!/usr/bin/env python3
"""
Problem 004: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""

import time
from typing import Tuple


def is_palindrome(n: int) -> bool:
    """数値が回文かどうかを判定"""
    s = str(n)
    return s == s[::-1]


def solve_naive(min_digits: int, max_digits: int) -> Tuple[int, int, int]:
    """
    素直な解法: 全ての組み合わせをチェック
    時間計算量: O(n²)
    空間計算量: O(1)
    """
    if min_digits > max_digits:
        return 0, 0, 0

    min_num = 10 ** (min_digits - 1)
    max_num = 10**max_digits - 1

    largest_palindrome = 0
    factors = (0, 0)

    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):  # j >= i to avoid duplicates
            product = i * j
            if product <= largest_palindrome:
                break  # Early termination since products will only get smaller
            if is_palindrome(product):
                largest_palindrome = product
                factors = (i, j)

    return largest_palindrome, factors[0], factors[1]


def solve_optimized(min_digits: int, max_digits: int) -> Tuple[int, int, int]:
    """
    最適化解法: 上から下に向かって探索し、早期終了を活用
    時間計算量: O(n²) but with better pruning
    空間計算量: O(1)
    """
    if min_digits > max_digits:
        return 0, 0, 0

    min_num = 10 ** (min_digits - 1)
    max_num = 10**max_digits - 1

    largest_palindrome = 0
    factors = (0, 0)

    # 大きな数から小さな数に向かって探索
    for i in range(max_num, min_num - 1, -1):
        # 早期終了条件: i * max_num が現在の最大値以下なら終了
        if i * max_num <= largest_palindrome:
            break

        for j in range(min(i, max_num), min_num - 1, -1):
            product = i * j
            if product <= largest_palindrome:
                break  # 内側ループの早期終了

            if is_palindrome(product):
                largest_palindrome = product
                factors = (i, j)
                break  # 最大値を見つけたので内側ループを終了

    return largest_palindrome, factors[0], factors[1]


def solve_mathematical(min_digits: int, max_digits: int) -> Tuple[int, int, int]:
    """
    数学的解法: 回文の構造を利用した最適化
    回文は特定の構造を持つため、候補を絞り込める
    時間計算量: O(n²) but with mathematical optimizations
    空間計算量: O(1)
    """
    if min_digits > max_digits:
        return 0, 0, 0

    min_num = 10 ** (min_digits - 1)
    max_num = 10**max_digits - 1

    largest_palindrome = 0
    factors = (0, 0)

    # 1桁や2桁の場合は最適化を適用せず、通常の方法を使用
    if max_digits <= 2:
        return solve_optimized(min_digits, max_digits)

    # 6桁の回文の場合: abccba = 100001*a + 10010*b + 1100*c
    # = 11 * (9091*a + 910*b + 100*c)
    # つまり、6桁の回文は必ず11で割り切れる

    for i in range(max_num, min_num - 1, -1):
        # 早期終了の最適化
        if i * max_num <= largest_palindrome:
            break

        # iが11で割り切れない場合、jは11で割り切れる必要がある
        j_start = min(i, max_num)
        j_step = 1

        if i % 11 != 0:
            # jを11の倍数に調整
            j_start = j_start - (j_start % 11)
            j_step = 11

        j = j_start
        while j >= min_num:
            product = i * j
            if product <= largest_palindrome:
                break

            if is_palindrome(product):
                largest_palindrome = product
                factors = (i, j)
                break

            j -= j_step

    return largest_palindrome, factors[0], factors[1]


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (1, 1, (9, 3, 3)),  # 1桁の場合: 3 * 3 = 9
        (2, 2, (9009, 91, 99)),  # 2桁の場合: 91 * 99 = 9009
    ]

    print("=== テストケース ===")
    for min_digits, max_digits, expected in test_cases:
        result_naive = solve_naive(min_digits, max_digits)
        result_optimized = solve_optimized(min_digits, max_digits)
        result_math = solve_mathematical(min_digits, max_digits)

        expected_palindrome, expected_factor1, expected_factor2 = expected

        print(f"Digits: {min_digits}-{max_digits}")
        print(
            f"  Expected: {expected_palindrome} = "
            f"{expected_factor1} × {expected_factor2}"
        )
        print(
            f"  Naive: {result_naive[0]} = {result_naive[1]} × {result_naive[2]} "
            f"{'✓' if result_naive[0] == expected_palindrome else '✗'}"
        )
        print(
            f"  Optimized: {result_optimized[0]} = "
            f"{result_optimized[1]} × {result_optimized[2]} "
            f"{'✓' if result_optimized[0] == expected_palindrome else '✗'}"
        )
        print(
            f"  Mathematical: {result_math[0]} = "
            f"{result_math[1]} × {result_math[2]} "
            f"{'✓' if result_math[0] == expected_palindrome else '✗'}"
        )
        print()


def main() -> None:
    """メイン関数"""
    min_digits = 3
    max_digits = 3

    print("=== Problem 004: Largest palindrome product ===")
    print(f"Finding largest palindrome from product of {min_digits}-digit numbers")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(min_digits, max_digits)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(min_digits, max_digits)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(min_digits, max_digits)
    math_time = time.time() - start_time

    print(
        f"素直な解法: {result_naive[0]:,} = "
        f"{result_naive[1]} × {result_naive[2]} "
        f"(実行時間: {naive_time:.6f}秒)"
    )
    print(
        f"最適化解法: {result_optimized[0]:,} = "
        f"{result_optimized[1]} × {result_optimized[2]} "
        f"(実行時間: {optimized_time:.6f}秒)"
    )
    print(
        f"数学的解法: {result_math[0]:,} = "
        f"{result_math[1]} × {result_math[2]} "
        f"(実行時間: {math_time:.6f}秒)"
    )
    print()

    # 結果の検証
    if result_naive[0] == result_optimized[0] == result_math[0]:
        print(
            f"✓ 解答: {result_optimized[0]:,} = "
            f"{result_optimized[1]} × {result_optimized[2]}"
        )
    else:
        print("✗ 解答が一致しません")
        print(f"  Naive: {result_naive[0]}")
        print(f"  Optimized: {result_optimized[0]}")
        print(f"  Mathematical: {result_math[0]}")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time/fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time/fastest_time:.2f}x")
    print(f"数学的解法: {math_time/fastest_time:.2f}x")

    # 回文の検証
    print("\n=== 回文の検証 ===")
    palindrome = result_optimized[0]
    print(f"数値: {palindrome}")
    print(f"文字列: {str(palindrome)}")
    print(f"逆順: {str(palindrome)[::-1]}")
    print(f"回文: {'✓' if is_palindrome(palindrome) else '✗'}")


if __name__ == "__main__":
    main()
