#!/usr/bin/env python3
"""
Problem 026: Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2  = 0.5
1/3  = 0.(3)
1/4  = 0.25
1/5  = 0.2
1/6  = 0.1(6)
1/7  = 0.(142857)
1/8  = 0.125
1/9  = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""


def get_cycle_length_naive(d: int) -> int:
    """
    素直な解法: 長除法をシミュレートして循環周期を求める
    時間計算量: O(d)
    空間計算量: O(d)
    """
    if d <= 1:
        return 0

    # 2と5の因数を除去（これらは循環しない）
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5

    if d == 1:
        return 0

    # 長除法をシミュレート
    remainder = 1
    seen_remainders: dict[int, int] = {}
    position = 0

    while remainder != 0:
        if remainder in seen_remainders:
            # 循環を発見
            return position - seen_remainders[remainder]

        seen_remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1

    return 0


def get_cycle_length_optimized(d: int) -> int:
    """
    最適化解法: 法の性質を利用した効率的な循環周期計算
    時間計算量: O(log d)
    空間計算量: O(1)
    """
    if d <= 1:
        return 0

    # 2と5の因数を除去（これらは循環しない）
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5

    if d == 1:
        return 0

    # 10^k ≡ 1 (mod d) となる最小のkを求める
    # これが循環周期となる
    remainder = 1
    for k in range(1, d):
        remainder = (remainder * 10) % d
        if remainder == 1:
            return k

    return 0


def solve_naive(limit: int = 1000) -> int:
    """
    素直な解法: 全てのdについて循環周期を計算
    時間計算量: O(n²)
    空間計算量: O(n)
    """
    max_cycle_length = 0
    result = 0

    for d in range(2, limit):
        cycle_length = get_cycle_length_naive(d)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            result = d

    return result


def solve_optimized(limit: int = 1000) -> int:
    """
    最適化解法: 効率的な循環周期計算を使用
    時間計算量: O(n × log n)
    空間計算量: O(1)
    """
    max_cycle_length = 0
    result = 0

    for d in range(2, limit):
        cycle_length = get_cycle_length_optimized(d)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            result = d

    return result


def main() -> None:
    """Main function to run and compare solutions."""
    import time

    limit = 1000

    print("Solving Problem 026...")

    # --- Naive Solution ---
    start_time = time.time()
    naive_answer = solve_naive(limit)
    naive_time = time.time() - start_time
    print(f"Naive solution: {naive_answer} (took {naive_time:.6f} seconds)")

    # --- Optimized Solution ---
    start_time = time.time()
    optimized_answer = solve_optimized(limit)
    optimized_time = time.time() - start_time
    print(f"Optimized solution: {optimized_answer} (took {optimized_time:.6f} seconds)")

    # Verify solutions match
    if naive_answer == optimized_answer:
        print(f"✓ Both solutions agree: {naive_answer}")
    else:
        print(
            f"✗ Solutions disagree: naive={naive_answer}, optimized={optimized_answer}"
        )


if __name__ == "__main__":
    main()
