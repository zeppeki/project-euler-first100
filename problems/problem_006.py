#!/usr/bin/env python3
"""
Problem 006: Sum square difference

The sum of the squares of the first ten natural numbers is:
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is: 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Answer: 25164150
"""

import time


def solve_naive(n: int) -> int:
    """
    素直な解法: 各数値を逐次計算してそれぞれの和を求める
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0

    # 平方の和を計算: 1² + 2² + ... + n²
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_squares += i * i

    # 和の平方を計算: (1 + 2 + ... + n)²
    sum_of_numbers = 0
    for i in range(1, n + 1):
        sum_of_numbers += i
    square_of_sum = sum_of_numbers * sum_of_numbers

    # 差を返す
    return square_of_sum - sum_of_squares


def solve_optimized(n: int) -> int:
    """
    最適化解法: 数学的公式を使用した効率的計算
    和の公式: 1 + 2 + ... + n = n(n+1)/2
    平方和の公式: 1² + 2² + ... + n² = n(n+1)(2n+1)/6
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0

    # 和の公式を使用: 1 + 2 + ... + n = n(n+1)/2
    sum_of_numbers = n * (n + 1) // 2
    square_of_sum = sum_of_numbers * sum_of_numbers

    # 平方和の公式を使用: 1² + 2² + ... + n² = n(n+1)(2n+1)/6
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6

    # 差を返す
    return square_of_sum - sum_of_squares


def solve_mathematical(n: int) -> int:
    """
    数学的解法: 差の公式を直接導出して使用
    (和の平方) - (平方の和) = [n(n+1)/2]² - n(n+1)(2n+1)/6
                            = n²(n+1)²/4 - n(n+1)(2n+1)/6
                            = n(n+1)[n(n+1)/4 - (2n+1)/6]
                            = n(n+1)[3n(n+1) - 2(2n+1)]/12
                            = n(n+1)[3n² + 3n - 4n - 2]/12
                            = n(n+1)(3n² - n - 2)/12
                            = n(n+1)(n-1)(3n+2)/12
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 0  # 1の場合、和の平方も平方の和も1なので差は0

    # 導出した公式を使用: n(n+1)(n-1)(3n+2)/12
    return n * (n + 1) * (n - 1) * (3 * n + 2) // 12


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (0, 0),  # n=0の場合
        (1, 0),  # n=1: 1² = 1, (1)² = 1, 差は0
        (2, 4),  # n=2: (1+2)² - (1²+2²) = 9 - 5 = 4
        (3, 22),  # n=3: (1+2+3)² - (1²+2²+3²) = 36 - 14 = 22
        (10, 2640),  # 問題例: n=10の場合
    ]

    print("=== テストケース ===")
    for n, expected in test_cases:
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)

        print(f"n = {n}")
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
    n = 100

    print("=== Problem 006: Sum square difference ===")
    print(f"Finding difference between square of sum and sum of squares for n={n}")
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
        print(f"  Naive: {result_naive}")
        print(f"  Optimized: {result_optimized}")
        print(f"  Mathematical: {result_math}")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 詳細な計算過程の表示
    print("\n=== 計算過程の詳細 ===")

    # n=10の例で詳細を表示
    example_n = 10
    print(f"例: n = {example_n}")

    # 平方の和
    sum_of_squares_example = sum(i * i for i in range(1, example_n + 1))
    print(f"平方の和: 1² + 2² + ... + {example_n}² = {sum_of_squares_example}")

    # 和の平方
    sum_of_numbers_example = sum(i for i in range(1, example_n + 1))
    square_of_sum_example = sum_of_numbers_example * sum_of_numbers_example
    print(
        f"和の平方: (1 + 2 + ... + {example_n})² = {sum_of_numbers_example}² = {square_of_sum_example}"
    )

    # 差
    difference_example = square_of_sum_example - sum_of_squares_example
    print(
        f"差: {square_of_sum_example} - {sum_of_squares_example} = {difference_example}"
    )

    # 公式の確認
    print(f"\n=== 公式の確認 (n={n}) ===")
    sum_formula = n * (n + 1) // 2
    sum_of_squares_formula = n * (n + 1) * (2 * n + 1) // 6
    print(f"1 + 2 + ... + {n} = {n}×{n + 1}/2 = {sum_formula}")
    print(
        f"1² + 2² + ... + {n}² = {n}×{n + 1}×{2 * n + 1}/6 = {sum_of_squares_formula}"
    )
    print(f"和の平方: {sum_formula}² = {sum_formula * sum_formula:,}")
    print(f"平方の和: {sum_of_squares_formula:,}")
    print(
        f"差: {sum_formula * sum_formula:,} - {sum_of_squares_formula:,} = {result_optimized:,}"
    )


if __name__ == "__main__":
    main()
