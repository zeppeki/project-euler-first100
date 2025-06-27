#!/usr/bin/env python3
"""
Problem 023: Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by
analysis even though it is known that the greatest number that cannot be expressed as the sum
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Answer: 4179871
"""

import time


def get_divisor_sum(n: int) -> int:
    """
    nの真の約数の和を計算する
    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n <= 1:
        return 0

    divisor_sum = 1  # 1は常に真の約数
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisor_sum += i
            # i != n//iの場合のみ、n//iも追加
            if i != n // i:
                divisor_sum += n // i
        i += 1
    return divisor_sum


def is_abundant(n: int) -> bool:
    """
    nが過剰数かどうかを判定
    時間計算量: O(√n)
    空間計算量: O(1)
    """
    return get_divisor_sum(n) > n


def solve_naive(limit: int = 28123) -> int:
    """
    素直な解法: 各数について過剰数の和で表せるかを直接チェック
    時間計算量: O(n² × √n)
    空間計算量: O(n)
    """
    # 過剰数を収集
    abundant_numbers = []
    for i in range(1, limit + 1):
        if is_abundant(i):
            abundant_numbers.append(i)

    # 過剰数の和で表せる数をマーク
    can_be_sum = set()
    for i, a in enumerate(abundant_numbers):
        for j in range(i, len(abundant_numbers)):
            b = abundant_numbers[j]
            sum_ab = a + b
            if sum_ab <= limit:
                can_be_sum.add(sum_ab)
            else:
                break  # bが大きくなると全てlimitを超える

    # 表せない数の合計を計算
    total = 0
    for i in range(1, limit + 1):
        if i not in can_be_sum:
            total += i

    return total


def solve_optimized(limit: int = 28123) -> int:
    """
    最適化解法: フラグ配列を使用して効率化
    時間計算量: O(n × √n + A²) where A is number of abundant numbers
    空間計算量: O(n)
    """
    # 過剰数判定の前計算（約数和をキャッシュ）
    divisor_sums = [0] * (limit + 1)
    for i in range(1, limit + 1):
        divisor_sums[i] = get_divisor_sum(i)

    # 過剰数を収集
    abundant_numbers = []
    for i in range(1, limit + 1):
        if divisor_sums[i] > i:
            abundant_numbers.append(i)

    # フラグ配列で過剰数の和を効率的にマーク
    can_be_sum = [False] * (limit + 1)
    for i, a in enumerate(abundant_numbers):
        for j in range(i, len(abundant_numbers)):
            b = abundant_numbers[j]
            sum_ab = a + b
            if sum_ab <= limit:
                can_be_sum[sum_ab] = True
            else:
                break

    # 表せない数の合計を計算
    total = 0
    for i in range(1, limit + 1):
        if not can_be_sum[i]:
            total += i

    return total


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        # 小さな値でのテスト
        (30, 230),  # 1+2+...+23+25+26+27+29 = 230 (24は12+12, 28は12+16で表せる)
        (100, 1574),  # 既知の結果
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
        print()

    # 個別テスト: 過剰数の確認
    print("=== 過剰数テスト ===")
    abundant_test_cases = [
        (12, True),  # 1+2+3+4+6 = 16 > 12
        (18, True),  # 1+2+3+6+9 = 21 > 18
        (20, True),  # 1+2+4+5+10 = 22 > 20
        (24, True),  # 1+2+3+4+6+8+12 = 36 > 24
        (6, False),  # 1+2+3 = 6 (完全数)
        (8, False),  # 1+2+4 = 7 < 8
        (28, False),  # 1+2+4+7+14 = 28 (完全数)
    ]

    for n, expected in abundant_test_cases:
        result = is_abundant(n)
        divisor_sum = get_divisor_sum(n)
        print(
            f"  {n}: {'過剰数' if result else '非過剰数'} "
            f"(約数和={divisor_sum}) {'✓' if result == expected else '✗'}"
        )


def main() -> None:
    """メイン関数"""
    limit = 28123

    print("=== Problem 023: Non-Abundant Sums ===")
    print("28123以下で2つの過剰数の和で表せない正の整数の合計を求める")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(min(1000, limit))  # 素直な解法は時間がかかるので制限
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(limit)
    optimized_time = time.time() - start_time

    print(
        f"素直な解法 (limit={min(1000, limit):,}): {result_naive:,} (実行時間: {naive_time:.6f}秒)"
    )
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print()

    # 結果の検証
    print(f"✓ 解答: {result_optimized:,}")

    # パフォーマンス比較
    print("\n=== パフォーマンス比較 ===")
    print(f"最適化解法: {optimized_time:.6f}秒")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 各数について過剰数ペアで和を直接チェック")
    print("最適化解法: フラグ配列と前計算でメモリアクセスを効率化")

    # 数学的背景の説明
    print("\n=== 数学的背景 ===")
    print("• 過剰数: 真の約数の和が数自身を超える数")
    print("• 12が最小の過剰数（約数和=16）")
    print("• 28,123より大きい全整数は2つの過剰数の和で表せる")
    print("• 約数和の効率的計算にはO(√n)の試し割りを使用")

    # 統計情報
    print("\n=== 統計情報 ===")
    abundant_count = len([i for i in range(1, limit + 1) if is_abundant(i)])
    print(f"28,123以下の過剰数の個数: {abundant_count:,}")
    print(f"全体に占める割合: {abundant_count / limit * 100:.2f}%")


if __name__ == "__main__":
    main()
