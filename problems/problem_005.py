#!/usr/bin/env python3
"""
Problem 005: Smallest multiple

2520 is the smallest number that can be evenly divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Answer: 232792560
"""

import math
import time
from typing import List, Tuple


def gcd(a: int, b: int) -> int:
    """ユークリッドの互除法による最大公約数の計算"""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """最小公倍数の計算: LCM(a,b) = a*b / GCD(a,b)"""
    return abs(a * b) // gcd(a, b)


def solve_naive(n: int) -> int:
    """
    素直な解法: 1から順番に各数で割り切れるかチェック
    時間計算量: O(result * n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    candidate = n  # 最小でもnは必要
    while True:
        is_divisible = True
        for i in range(1, n + 1):
            if candidate % i != 0:
                is_divisible = False
                break

        if is_divisible:
            return candidate

        candidate += 1


def solve_optimized(n: int) -> int:
    """
    最適化解法: LCMの性質を利用した効率的計算
    LCM(1,2,...,n) = LCM(LCM(1,2,...,n-1), n)
    時間計算量: O(n * log(max_value))
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)

    return result


def solve_mathematical(n: int) -> int:
    """
    数学的解法: 素因数分解を利用した直接計算
    各素数について、1～nの範囲で最大の冪を求める
    時間計算量: O(n * log(log(n))) - エラトステネスの篩 + O(n * log(n))
    空間計算量: O(n)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # エラトステネスの篩で素数を求める
    def sieve_of_eratosthenes(limit: int) -> List[int]:
        """エラトステネスの篩による素数列挙"""
        if limit < 2:
            return []

        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        return [i for i in range(2, limit + 1) if is_prime[i]]

    # 各素数について最大の冪を求める
    def max_prime_power(prime: int, limit: int) -> int:
        """primeのlimit以下での最大冪を求める"""
        power = 1
        while prime ** (power + 1) <= limit:
            power += 1
        return power

    primes = sieve_of_eratosthenes(n)
    result = 1

    for prime in primes:
        max_power = max_prime_power(prime, n)
        result *= prime**max_power

    return result


def solve_builtin(n: int) -> int:
    """
    Python標準ライブラリ使用解法: math.lcmを活用
    時間計算量: O(n * log(max_value))
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Python 3.9以降でmath.lcmが利用可能
    try:
        result = 1
        for i in range(2, n + 1):
            result = math.lcm(result, i)
        return result
    except AttributeError:
        # math.lcmが利用できない場合は最適化解法にフォールバック
        return solve_optimized(n)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (1, 1),  # LCM(1) = 1
        (2, 2),  # LCM(1,2) = 2
        (3, 6),  # LCM(1,2,3) = 6
        (4, 12),  # LCM(1,2,3,4) = 12
        (5, 60),  # LCM(1,2,3,4,5) = 60
        (10, 2520),  # 問題例: LCM(1,...,10) = 2520
    ]

    print("=== テストケース ===")
    for n, expected in test_cases:
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)
        result_builtin = solve_builtin(n)

        print(f"n = {n}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} "
            f"{'✓' if result_optimized == expected else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}"
        )
        print(
            f"  Builtin: {result_builtin} {'✓' if result_builtin == expected else '✗'}"
        )
        print()


def main() -> None:
    """メイン関数"""
    n = 20

    print("=== Problem 005: Smallest multiple ===")
    print(f"Finding smallest positive number divisible by all numbers from 1 to {n}")
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

    start_time = time.time()
    result_builtin = solve_builtin(n)
    builtin_time = time.time() - start_time

    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print(f"標準ライブラリ解法: {result_builtin:,} (実行時間: {builtin_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized == result_math == result_builtin:
        print(f"✓ 解答: {result_optimized:,}")
    else:
        print("✗ 解答が一致しません")
        print(f"  Naive: {result_naive}")
        print(f"  Optimized: {result_optimized}")
        print(f"  Mathematical: {result_math}")
        print(f"  Builtin: {result_builtin}")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time, builtin_time)
    print(f"素直な解法: {naive_time/fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time/fastest_time:.2f}x")
    print(f"数学的解法: {math_time/fastest_time:.2f}x")
    print(f"標準ライブラリ解法: {builtin_time/fastest_time:.2f}x")

    # 素因数分解の確認
    print("\n=== 素因数分解の確認 ===")
    print(f"結果: {result_optimized:,}")

    # 簡単な因数分解表示
    def prime_factorization(num: int) -> List[Tuple[int, int]]:
        """素因数分解を行う"""
        factors: List[Tuple[int, int]] = []
        d = 2
        while d * d <= num:
            while num % d == 0:
                # 既存の因数があるか確認
                found = False
                for i, (prime, count) in enumerate(factors):
                    if prime == d:
                        factors[i] = (prime, count + 1)
                        found = True
                        break
                if not found:
                    factors.append((d, 1))
                num //= d
            d += 1
        if num > 1:
            factors.append((num, 1))
        return factors

    factors = prime_factorization(result_optimized)
    factor_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factors])
    print(f"素因数分解: {factor_str}")

    # 検証: 1からnまでの各数で割り切れることを確認
    print("\n=== 除数確認 ===")
    verification_failed = False
    for i in range(1, min(n + 1, 11)):  # 表示は最初の10個まで
        if result_optimized % i == 0:
            print(f"{result_optimized:,} ÷ {i} = {result_optimized//i:,} ✓")
        else:
            print(f"{result_optimized:,} ÷ {i} = 余り{result_optimized%i} ✗")
            verification_failed = True

    if n > 10:
        print(f"... (11から{n}まで省略)")
        for i in range(11, n + 1):
            if result_optimized % i != 0:
                print(f"{result_optimized:,} ÷ {i} = 余り{result_optimized%i} ✗")
                verification_failed = True

    if not verification_failed:
        print("全ての数で割り切れることを確認 ✓")


if __name__ == "__main__":
    main()
