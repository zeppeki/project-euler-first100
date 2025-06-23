#!/usr/bin/env python3
"""
Problem 007: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime?

Answer: 104743
"""

import math
import time


def solve_naive(n: int) -> int:
    """
    素直な解法: 各数を素数判定して順次n番目の素数を見つける
    時間計算量: O(n * sqrt(m)) where m is the nth prime
    空間計算量: O(1)
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 2

    count = 1  # 2を最初の素数として数える
    candidate = 3  # 次の候補は3

    while count < n:
        if is_prime_naive(candidate):
            count += 1
        if count < n:
            candidate += 2  # 奇数のみをチェック

    return candidate


def is_prime_naive(num: int) -> bool:
    """素数判定（素直な方法）"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    return all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2))


def solve_optimized(n: int) -> int:
    """
    最適化解法: エラトステネスの篩を使用した効率的な素数生成
    時間計算量: O(m * log(log(m))) where m is the upper bound
    空間計算量: O(m)
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 2

    # n番目の素数の近似上限を計算（素数定理より）
    limit = 12 if n < 6 else int(n * (math.log(n) + math.log(math.log(n))))

    # エラトステネスの篩
    primes = sieve_of_eratosthenes(limit)

    # 必要な数の素数が見つからない場合、範囲を拡張
    while len(primes) < n:
        limit *= 2
        primes = sieve_of_eratosthenes(limit)

    return primes[n - 1]


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """エラトステネスの篩で指定された範囲の素数を全て求める"""
    if limit < 2:
        return []

    # 篩を初期化
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # 篩を実行
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # 素数のリストを作成
    return [i for i in range(2, limit + 1) if is_prime[i]]


def solve_mathematical(n: int) -> int:
    """
    数学的解法: 試行割り付きの最適化された素数判定
    6k±1の形の数のみをチェックして効率化
    時間計算量: O(n * sqrt(m) / 3) where m is the nth prime
    空間計算量: O(1)
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 2
    if n == 2:
        return 3

    count = 2  # 2と3を既に数えている
    candidate = 5  # 次の候補は5 (6*1-1)
    increment = 2  # 5の次は7 (6*1+1), その次は11 (6*2-1)

    while count < n:
        if is_prime_optimized(candidate):
            count += 1
        if count < n:
            candidate += increment
            increment = 6 - increment  # 2と4を交互に

    return candidate


def is_prime_optimized(num: int) -> bool:
    """最適化された素数判定（6k±1の形を利用）"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    # 5から始めて6k±1の形の数のみをチェック
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (1, 2),  # 最初の素数は2
        (2, 3),  # 2番目の素数は3
        (3, 5),  # 3番目の素数は5
        (4, 7),  # 4番目の素数は7
        (5, 11),  # 5番目の素数は11
        (6, 13),  # 6番目の素数は13（問題例）
        (10, 29),  # 10番目の素数は29
        (100, 541),  # 100番目の素数は541
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
    n = 10001

    print("=== Problem 007: 10001st prime ===")
    print(f"Finding the {n}st prime number")
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

    # 最初の20個の素数を表示
    print("最初の20個の素数:")
    primes_list = []
    for i in range(1, 21):
        primes_list.append(str(solve_optimized(i)))
    print(", ".join(primes_list))

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 各数を順次チェックして素数判定")
    print("最適化解法: エラトステネスの篩で効率的に素数を生成")
    print("数学的解法: 6k±1の形の数のみをチェックして効率化")

    # 素数定理による近似
    approx_nth_prime = n * math.log(n)
    print(f"\n素数定理による{n}番目の素数の近似値: {approx_nth_prime:.0f}")
    print(f"実際の値: {result_optimized}")
    print(f"誤差: {abs(result_optimized - approx_nth_prime):.0f}")


if __name__ == "__main__":
    main()
