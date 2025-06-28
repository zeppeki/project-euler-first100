#!/usr/bin/env python3
"""
Problem 025: 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:
F_n = F_{n-1} + F_{n-2}, where F_1 = 1 and F_2 = 1.

Hence the first 12 terms will be:
F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144

The 12th term, F_12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import math


def solve_naive(target_digits: int = 1000) -> int:
    """
    素直な解法: フィボナッチ数列を順次計算して桁数をチェック
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if target_digits <= 0:
        return 0
    if target_digits == 1:
        return 1

    # F_1 = 1, F_2 = 1から開始
    prev, curr = 1, 1
    index = 2

    # target_digits桁の数の最小値は10^(target_digits-1)
    target_value = 10 ** (target_digits - 1)

    while curr < target_value:
        prev, curr = curr, prev + curr
        index += 1

    return index


def solve_optimized(target_digits: int = 1000) -> int:
    """
    最適化解法: ビネットの公式を使用して対数計算で桁数を求める
    時間計算量: O(log n)
    空間計算量: O(1)
    """
    if target_digits <= 0:
        return 0
    if target_digits == 1:
        return 1

    # ビネットの公式: F_n = (φ^n - ψ^n) / √5
    # φ = (1 + √5) / 2 (黄金比)
    # ψ = (1 - √5) / 2
    phi = (1 + math.sqrt(5)) / 2
    log_phi = math.log10(phi)
    log_sqrt5 = math.log10(math.sqrt(5))

    # F_nがd桁の数になる条件: 10^(d-1) ≤ F_n < 10^d
    # ビネットの公式から: log10(F_n) ≈ n * log10(φ) - log10(√5)
    # d桁の条件: d-1 ≤ log10(F_n) < d
    # つまり: d-1 ≤ n * log10(φ) - log10(√5) < d

    # n * log10(φ) - log10(√5) ≥ target_digits - 1
    # n ≥ (target_digits - 1 + log10(√5)) / log10(φ)
    min_n = math.ceil((target_digits - 1 + log_sqrt5) / log_phi)

    # 実際の計算で確認（ビネットの公式は近似なので）
    prev, curr = 1, 1
    index = 2
    target_value = 10 ** (target_digits - 1)

    # min_n付近から開始して精密に計算
    start_index = max(1, min_n - 10)

    # start_indexまでの値を計算
    for _ in range(start_index - 2):
        prev, curr = curr, prev + curr
        index += 1

    # 正確な値を見つける
    while curr < target_value:
        prev, curr = curr, prev + curr
        index += 1

    return index


def main() -> None:
    """Main function to run and compare solutions."""
    import time

    target_digits = 1000

    print("Solving Problem 025...")

    # --- Naive Solution ---
    start_time = time.time()
    naive_answer = solve_naive(target_digits)
    naive_time = time.time() - start_time
    print(f"Naive solution: {naive_answer} (took {naive_time:.6f} seconds)")

    # --- Optimized Solution ---
    start_time = time.time()
    optimized_answer = solve_optimized(target_digits)
    optimized_time = time.time() - start_time
    print(f"Optimized solution: {optimized_answer} (took {optimized_time:.6f} seconds)")


if __name__ == "__main__":
    main()
