#!/usr/bin/env python3
"""
Problem 028: Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction,
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?

Answer: 669171001
"""

import time


def solve_naive(size: int) -> int:
    """
    素直な解法: 螺旋を実際に構築して対角線の和を計算
    時間計算量: O(n²)
    空間計算量: O(n²)
    """
    if size % 2 == 0:
        raise ValueError("Size must be odd")

    # 螺旋を格納する2次元配列
    spiral = [[0] * size for _ in range(size)]

    # 中心から開始
    x, y = size // 2, size // 2
    spiral[x][y] = 1

    # 方向: 右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0

    num = 2
    steps = 1

    while num <= size * size:
        for _ in range(2):  # 同じ歩数で2回移動
            dx, dy = directions[direction]
            for _ in range(steps):
                x, y = x + dx, y + dy
                if 0 <= x < size and 0 <= y < size:
                    spiral[x][y] = num
                    num += 1
                if num > size * size:
                    break
            direction = (direction + 1) % 4
            if num > size * size:
                break
        steps += 1

    # 対角線の和を計算
    diagonal_sum = 0
    for i in range(size):
        diagonal_sum += spiral[i][i]  # 主対角線
        diagonal_sum += spiral[i][size - 1 - i]  # 副対角線

    # 中心は重複しているので一度引く
    diagonal_sum -= spiral[size // 2][size // 2]

    return diagonal_sum


def solve_optimized(size: int) -> int:
    """
    最適化解法: 螺旋の特性を利用して直接対角線の値を計算
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if size % 2 == 0:
        raise ValueError("Size must be odd")

    if size == 1:
        return 1

    diagonal_sum = 1  # 中心の1から開始

    # 各層の対角線の値を計算
    num = 1
    for layer in range(1, (size + 1) // 2):
        # 各層で4つの角の値を計算
        # 右上、右下、左下、左上の順

        # 前の層の最後の数から続ける
        num += 2 * layer

        # 各角の値を計算
        for corner in range(4):
            diagonal_sum += num
            if corner < 3:  # 最後の角以外
                num += 2 * layer

    return diagonal_sum


def solve_mathematical(size: int) -> int:
    """
    数学的解法: 数学的パターンから公式を導出
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if size % 2 == 0:
        raise ValueError("Size must be odd")

    if size == 1:
        return 1

    # 螺旋の対角線要素のパターンを分析:
    # 1x1: 1
    # 3x3: 1 + 3 + 5 + 7 + 9 = 25
    # 5x5: 前回 + 13 + 17 + 21 + 25 = 25 + 76 = 101
    #
    # 各層での4つの角の値は等差数列を形成
    # k層目(k>=1)では: 4k² - 4k + 1, 4k² - 2k + 1, 4k² + 1, 4k² + 2k + 1
    # これらの和は: 16k² + 4k + 4
    #
    # 総和は: 1 + Σ(k=1 to (size-1)/2) (16k² + 4k + 4)
    #       = 1 + 16*Σk² + 4*Σk + 4*((size-1)/2)

    layers = (size - 1) // 2
    if layers == 0:
        return 1

    # Σ(k=1 to n) k = n(n+1)/2
    # Σ(k=1 to n) k² = n(n+1)(2n+1)/6

    sum_k = layers * (layers + 1) // 2
    sum_k2 = layers * (layers + 1) * (2 * layers + 1) // 6

    return 1 + 16 * sum_k2 + 4 * sum_k + 4 * layers


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (1, 1),
        (3, 25),  # 1 + 3 + 5 + 7 + 9 = 25
        (5, 101),  # 問題文の例
    ]

    print("=== テストケース ===")
    for size, expected in test_cases:
        result_naive = solve_naive(size)
        result_optimized = solve_optimized(size)
        result_mathematical = solve_mathematical(size)

        print(f"Size: {size}×{size}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
        )
        print(
            f"  Mathematical: {result_mathematical} {'✓' if result_mathematical == expected else '✗'}"
        )
        print()


def main() -> None:
    """メイン関数"""
    print("=== Problem 028: Number spiral diagonals ===")

    # テストケース
    test_solutions()

    # 本問題の解答
    size = 1001
    print(f"Size: {size}×{size}")
    print()

    # パフォーマンス測定と結果表示
    start_time = time.time()
    result_optimized = solve_optimized(size)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_mathematical = solve_mathematical(size)
    mathematical_time = time.time() - start_time

    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_mathematical:,} (実行時間: {mathematical_time:.6f}秒)")
    print()

    # 結果の検証
    if result_optimized == result_mathematical:
        print(f"✓ 解答: {result_mathematical:,}")
    else:
        print("✗ 解答が一致しません")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(optimized_time, mathematical_time)
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {mathematical_time / fastest_time:.2f}x")


if __name__ == "__main__":
    main()
