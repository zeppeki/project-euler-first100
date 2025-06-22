#!/usr/bin/env python3
"""
Problem 003: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Answer: 6857
"""

import math
import time


def is_prime(n: int) -> bool:
    """
    素数判定関数

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 3から√nまでの奇数で試し割り
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def solve_naive(n: int) -> int:
    """
    素直な解法: 2から順番に試し割り

    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0

    if n == 1:
        return 1

    largest_factor = 1

    # 2で割り切れるだけ割る
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # 奇数の約数を試す
    for i in range(3, n + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i
        if n == 1:
            break

    return largest_factor


def solve_optimized(n: int) -> int:
    """
    最適化解法: 平方根まで試し割り

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0

    if n == 1:
        return 1

    largest_factor = 1

    # 2で割り切れるだけ割る
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # 奇数の約数を平方根まで試す
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i

    # nが1より大きい場合、n自体が素数
    if n > 1:
        largest_factor = n

    return largest_factor


def solve_mathematical(n: int) -> int:
    """
    数学的解法: より効率的な素因数分解

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0

    if n == 1:
        return 1

    largest_factor = 1

    # 2で割り切れるだけ割る
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # 奇数の約数を平方根まで試す
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i

    # nが1より大きい場合、n自体が素数
    if n > 1:
        largest_factor = n

    return largest_factor


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (13195, 29),  # Example: 5, 7, 13, 29 → max is 29
        (100, 5),  # 100 = 2^2 × 5^2 → max is 5
        (84, 7),  # 84 = 2^2 × 3 × 7 → max is 7
        (17, 17),  # 素数 → 最大は17
        (25, 5),  # 25 = 5^2 → 最大は5
    ]

    print("=== テストケース ===")
    for n, expected in test_cases:
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)

        print(f"n: {n}")
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
    n = 600851475143

    print("=== Problem 003: Largest prime factor ===")
    print(f"n: {n:,}")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(n)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(n)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(n)
    math_time = time.time() - start_time

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
    print(f"素直な解法: {naive_time/fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time/fastest_time:.2f}x")
    print(f"数学的解法: {math_time/fastest_time:.2f}x")


if __name__ == "__main__":
    main()
