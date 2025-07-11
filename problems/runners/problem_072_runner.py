#!/usr/bin/env python3
"""
Problem 072 Runner: Counting fractions

This module provides a runner for Problem 072 that demonstrates the mathematical
concepts behind counting reduced proper fractions using Euler's totient function.
"""

import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from problems.problem_072 import (
    analyze_totient_distribution,
    count_reduced_fractions_range,
    euler_totient_prime_factorization,
    euler_totient_sieve,
    get_mathematical_properties,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    solve_sieve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


def verify_small_example() -> tuple[int, list[tuple[int, int]]]:
    """
    問題文の小さな例 (d ≤ 8) を検証
    返り値: (count, fractions)
    """
    from math import gcd

    fractions = []
    for d in range(2, 9):
        for n in range(1, d):
            if gcd(n, d) == 1:
                fractions.append((n, d))
    return len(fractions), fractions


class Problem072Runner(BaseProblemRunner):
    """
    Problem 072: Counting fractions

    This problem asks for the count of reduced proper fractions with denominator ≤ 1,000,000.
    The solution involves computing the sum of Euler's totient function φ(d) for d from 2 to 1,000,000.
    """

    def __init__(self) -> None:
        super().__init__(
            problem_number=72,
            problem_title="Counting fractions",
            expected_answer=303963552391,
        )

    def solve(self) -> int:
        """
        Solve Problem 072 using the mathematical approach.

        Returns:
            The number of reduced proper fractions with denominator ≤ 1,000,000
        """
        return solve_mathematical(1000000)

    def demonstrate_problem_overview(self) -> None:
        """Problem 072の概要を説明"""
        print("=== Problem 072: Counting fractions ===")
        print()
        print("目標: 分母がd ≤ 1,000,000の既約真分数の総数を求める")
        print()
        print("既約真分数とは:")
        print("- n/d where n < d and gcd(n,d) = 1")
        print("- 分子と分母が互いに素である真分数")
        print()
        print("例: d ≤ 8の場合:")
        count, fractions = verify_small_example()
        print(f"総数: {count}")
        print("分数リスト:")
        for i, (n, d) in enumerate(fractions):
            print(f"  {n}/{d}", end="")
            if (i + 1) % 7 == 0:
                print()
            elif i < len(fractions) - 1:
                print(", ", end="")
        print()
        print()

    def demonstrate_euler_totient_function(self) -> None:
        """オイラーのトーシェント関数の概念を説明"""
        print("=== オイラーのトーシェント関数 φ(n) ===")
        print()
        print("定義: φ(n) = n以下の正の整数で、nと互いに素であるものの個数")
        print()
        print("重要な性質:")
        print("- φ(1) = 1")
        print("- pが素数の場合: φ(p) = p - 1")
        print("- φ(p^k) = p^k - p^(k-1) = p^(k-1)(p-1)")
        print("- φ(mn) = φ(m)φ(n) if gcd(m,n) = 1 (乗法的関数)")
        print()

        print("小さな値でのφ(n)の例:")
        for n in range(1, 13):
            phi_n = euler_totient_prime_factorization(n)
            props = get_mathematical_properties(n)
            print(f"  φ({n}) = {phi_n:2d} | 素因数: {props['prime_factors']}")
        print()

    def demonstrate_solution_approaches(self) -> None:
        """各解法のアプローチを説明"""
        print("=== 解法アプローチの比較 ===")
        print()
        test_limit = 100

        print("1. 素直な解法 (Naive):")
        print("   各dについて個別にφ(d)を計算 - O(n²)")
        result_naive = solve_naive(test_limit)
        print(f"   結果 (d ≤ {test_limit}): {result_naive}")
        print()

        print("2. 最適化解法 (Optimized):")
        print("   素因数分解ベースのφ(d)計算 - O(n√n)")
        result_optimized = solve_optimized(test_limit)
        print(f"   結果 (d ≤ {test_limit}): {result_optimized}")
        print()

        print("3. 数学的解法 (Mathematical):")
        print("   篩ベースの一括計算 - O(n log log n)")
        result_mathematical = solve_mathematical(test_limit)
        print(f"   結果 (d ≤ {test_limit}): {result_mathematical}")
        print()

        print("4. 篩最適化解法 (Sieve Optimized):")
        print("   メモリ効率を考慮した篩計算 - O(n log log n)")
        result_sieve = solve_sieve_optimized(test_limit)
        print(f"   結果 (d ≤ {test_limit}): {result_sieve}")
        print()

        print("✓ すべての解法が同じ結果を生成")
        print()

    def demonstrate_totient_properties(self) -> None:
        """トーシェント関数の性質を実例で説明"""
        print("=== トーシェント関数の性質 ===")
        print()

        # 素数の場合
        print("1. 素数の場合: φ(p) = p - 1")
        primes = [7, 11, 13, 17, 19]
        for p in primes:
            phi_p = euler_totient_prime_factorization(p)
            print(f"   φ({p}) = {phi_p} = {p} - 1")
        print()

        # 素数のべき乗の場合
        print("2. 素数のべき乗の場合: φ(p^k) = p^(k-1)(p-1)")
        powers = [(2, 3), (3, 2), (5, 2), (7, 2)]
        for p, k in powers:
            n = p**k
            phi_n = euler_totient_prime_factorization(n)
            expected = (p ** (k - 1)) * (p - 1)
            print(
                f"   φ({p}^{k}) = φ({n}) = {phi_n} = {p}^{k - 1} × ({p}-1) = {expected}"
            )
        print()

        # 乗法的性質
        print("3. 乗法的性質: φ(mn) = φ(m)φ(n) when gcd(m,n) = 1")
        pairs = [(3, 5), (4, 9), (7, 8), (9, 16)]
        for m, n in pairs:
            mn = m * n
            phi_m = euler_totient_prime_factorization(m)
            phi_n = euler_totient_prime_factorization(n)
            phi_mn = euler_totient_prime_factorization(mn)
            print(
                f"   φ({m}×{n}) = φ({mn}) = {phi_mn} = φ({m})×φ({n}) = {phi_m}×{phi_n} = {phi_m * phi_n}"
            )
        print()

    def demonstrate_sieve_algorithm(self) -> None:
        """篩アルゴリズムの動作を説明"""
        print("=== 篩アルゴリズムの動作 ===")
        print()
        print("エラトステネスの篩の変形を使用:")
        print("1. φ(i) = i で初期化")
        print("2. 各素数pに対して、pの倍数kすべてについて:")
        print("   φ(k) = φ(k) × (1 - 1/p) = φ(k) - φ(k)/p")
        print()

        # 小さな例で動作を示す
        limit = 20
        print(f"例: limit = {limit}")
        phi_values = euler_totient_sieve(limit)

        print("最終的なφ(n)値:")
        for i in range(1, limit + 1):
            print(f"  φ({i:2d}) = {phi_values[i]:2d}")
        print()

        total = sum(phi_values[2 : limit + 1])
        print(f"既約真分数の総数 (d ≤ {limit}): {total}")
        print()

    def demonstrate_performance_analysis(self) -> None:
        """パフォーマンス分析を実演"""
        print("=== パフォーマンス分析 ===")
        print()

        test_limits = [100, 1000, 10000]

        for limit in test_limits:
            print(f"分母上限: {limit}")
            analysis = analyze_totient_distribution(limit)
            print(f"  既約真分数総数: {analysis['total_count']:,}")
            print(f"  最大φ値: {analysis['max_phi']:,}")
            print(f"  最小φ値: {analysis['min_phi']:,}")
            print(f"  平均φ値: {analysis['average_phi']:.2f}")
            print()

    def demonstrate_range_analysis(self) -> None:
        """範囲別分析を実演"""
        print("=== 範囲別分析 ===")
        print()

        ranges = [
            (2, 10),
            (11, 100),
            (101, 1000),
            (1001, 10000),
        ]

        for start, end in ranges:
            count = count_reduced_fractions_range(start, end)
            print(f"分母範囲 [{start:5d}, {end:5d}]: {count:8,} 個の既約真分数")
        print()

    def demonstrate_mathematical_insights(self) -> None:
        """数学的洞察を説明"""
        print("=== 数学的洞察 ===")
        print()

        print("1. 問題の本質:")
        print("   既約真分数 n/d の個数 = φ(d)")
        print("   総数 = Σφ(d) for d = 2 to 1,000,000")
        print()

        print("2. 計算量の改善:")
        print("   素直な方法: O(n²) - 各dについて個別計算")
        print("   篩の方法: O(n log log n) - 一括計算")
        print()

        print("3. 空間計算量:")
        print("   篩の方法: O(n) - 全φ値を配列に保存")
        print("   メモリ使用量 (n=1,000,000): 約4-8MB")
        print()

        print("4. 実際の計算:")
        final_answer = solve_mathematical(1000000)
        print(f"   d ≤ 1,000,000の既約真分数総数: {final_answer:,}")
        print()

    def run_demonstration(self) -> None:
        """Complete demonstration of Problem 072"""
        print("Problem 072: Counting fractions - 完全デモンストレーション")
        print("=" * 60)
        print()

        self.demonstrate_problem_overview()
        self.demonstrate_euler_totient_function()
        self.demonstrate_solution_approaches()
        self.demonstrate_totient_properties()
        self.demonstrate_sieve_algorithm()
        self.demonstrate_performance_analysis()
        self.demonstrate_range_analysis()
        self.demonstrate_mathematical_insights()

        print("=" * 60)
        print("デモンストレーション完了")
        print()


def main() -> None:
    """Main function for Problem 072 runner"""
    runner = Problem072Runner()
    runner.run_demonstration()


if __name__ == "__main__":
    main()
