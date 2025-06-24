#!/usr/bin/env python3
"""
Problem 010: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer: 142913828922
"""

import math
import time


def solve_naive(limit: int) -> int:
    """
    素直な解法: 各数を素数判定して合計を計算
    時間計算量: O(n * sqrt(n))
    空間計算量: O(1)
    """
    if limit <= 2:
        return 0

    prime_sum = 2  # 最初の素数2を加算

    # 3から始めて奇数のみをチェック
    for num in range(3, limit, 2):
        if is_prime_naive(num):
            prime_sum += num

    return prime_sum


def is_prime_naive(num: int) -> bool:
    """素数判定（素直な方法）"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    return all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2))


def solve_optimized(limit: int) -> int:
    """
    最適化解法: エラトステネスの篩を使用
    時間計算量: O(n * log(log(n)))
    空間計算量: O(n)
    """
    if limit <= 2:
        return 0

    # エラトステネスの篩で素数を見つけて合計
    primes = sieve_of_eratosthenes(limit - 1)
    return sum(primes)


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


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: 最適化されたエラトステネスの篩（メモリ効率版）
    時間計算量: O(n * log(log(n)))
    空間計算量: O(n)
    """
    if limit <= 2:
        return 0

    # 2は別途処理
    prime_sum = 2

    # 奇数のみの篩を使用してメモリを半分に削減
    odd_limit = (limit - 1) // 2
    is_prime_odd = [True] * (odd_limit + 1)

    # 3から始めて奇数の合成数をマーク
    for i in range(1, int(math.sqrt(limit)) // 2 + 1):
        if is_prime_odd[i]:
            prime = 2 * i + 1
            # prime * prime から開始して、prime の奇数倍をマーク
            start = (prime * prime - 1) // 2
            for j in range(start, odd_limit + 1, prime):
                is_prime_odd[j] = False

    # 奇数の素数の合計を計算 (limitより小さい数のみ)
    for i in range(1, odd_limit + 1):
        if is_prime_odd[i]:
            prime = 2 * i + 1
            if prime < limit:
                prime_sum += prime

    return prime_sum


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (2, 0),  # 2未満の素数はなし
        (3, 2),  # 3未満の素数は2のみ
        (10, 17),  # 問題例: 2 + 3 + 5 + 7 = 17
        (30, 129),  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 = 129
        (100, 1060),  # 100未満の素数の和
    ]

    print("=== テストケース ===")
    for limit, expected in test_cases:
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_math = solve_mathematical(limit)

        print(f"limit = {limit}")
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
    limit = 2000000

    print("=== Problem 010: Summation of primes ===")
    print(f"Finding the sum of all primes below {limit:,}")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(limit)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(limit)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(limit)
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

    # 最初の100までの素数の合計を表示
    small_limit = 100
    small_primes = sieve_of_eratosthenes(small_limit - 1)
    print(f"100未満の素数: {', '.join(map(str, small_primes))}")
    print(f"100未満の素数の和: {sum(small_primes)}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 各数を順次チェックして素数判定し合計")
    print("最適化解法: エラトステネスの篩で効率的に素数を生成し合計")
    print("数学的解法: メモリ最適化されたエラトステネスの篩（奇数のみ）")

    # 素数の密度
    prime_count = len(sieve_of_eratosthenes(limit - 1))
    density = prime_count / limit * 100
    print(f"\n{limit:,}未満の素数の個数: {prime_count:,}")
    print(f"素数の密度: {density:.3f}%")

    # 素数定理による近似
    approx_count = limit / math.log(limit)
    print(f"素数定理による近似個数: {approx_count:.0f}")
    print(f"実際の個数: {prime_count}")
    print(f"誤差: {abs(prime_count - approx_count):.0f}")


if __name__ == "__main__":
    main()
