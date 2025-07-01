#!/usr/bin/env python3
"""
Problem 010 Runner: Execution and demonstration code for Problem 010.

This module handles the execution and demonstration of Problem 010 solutions,
separated from the core algorithm implementations.
"""

import math
from collections.abc import Callable
from typing import Any

from problems.problem_010 import (
    is_prime_naive,
    sieve_of_eratosthenes,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem010Runner(BaseProblemRunner):
    """Runner for Problem 010: Summation of primes."""

    def __init__(self) -> None:
        super().__init__("010", "Summation of primes")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 010."""
        return [
            (2, 0),  # No primes below 2
            (3, 2),  # Only 2 is below 3
            (10, 17),  # Problem example: 2 + 3 + 5 + 7 = 17
            (11, 17),  # Same as above, 11 is not included
            (30, 129),  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 = 129
            (100, 1060),  # Sum of primes below 100
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 010."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (2000000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 010."""
        return [
            self._demonstrate_prime_properties,
            self._demonstrate_sieve_algorithm,
            self._demonstrate_prime_distribution,
        ]

    def _demonstrate_prime_properties(self) -> None:
        """Demonstrate properties of prime numbers."""
        print("=== 素数の性質 ===")

        # Show first several primes
        first_primes = sieve_of_eratosthenes(100)
        print(f"100未満の素数 ({len(first_primes)}個):")
        print(f"{', '.join(map(str, first_primes))}")

        # Verify prime checking function
        print("\n素数判定関数の検証:")
        test_numbers = [
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            13,
            15,
            17,
            19,
            21,
            23,
            25,
            29,
            31,
        ]
        print(f"{'数':>3} {'素数?':>6} {'判定結果':>8}")
        print("-" * 20)

        for num in test_numbers:
            is_prime = is_prime_naive(num)
            expected_prime = num in first_primes
            status = "✓" if is_prime == expected_prime else "✗"
            print(f"{num:3d} {expected_prime!s:>6} {is_prime!s:>8} {status}")

        # Show small prime gaps
        print("\n素数ギャップ (連続する素数の差):")
        gaps = []
        for i in range(1, min(20, len(first_primes))):
            gap = first_primes[i] - first_primes[i - 1]
            gaps.append(gap)
            print(f"  {first_primes[i - 1]} → {first_primes[i]}: gap = {gap}")

        print(f"\n最初の19個の素数ギャップの平均: {sum(gaps) / len(gaps):.2f}")

    def _demonstrate_sieve_algorithm(self) -> None:
        """Demonstrate the Sieve of Eratosthenes algorithm."""
        print("=== エラトステネスの篩アルゴリズム ===")

        # Demonstrate with small numbers
        demo_limit = 30
        print("30までの数でのエラトステネスの篩の実行過程:")
        print("初期状態: 2から30までの数を素数候補とする")

        # Start with all numbers marked as potential primes
        is_prime = [True] * (demo_limit + 1)
        is_prime[0] = is_prime[1] = False

        print(f"候補: {[i for i in range(2, demo_limit + 1) if is_prime[i]]}")

        # Apply sieve step by step
        for p in range(2, int(math.sqrt(demo_limit)) + 1):
            if is_prime[p]:
                print(f"\n素数 {p} の倍数を除去:")
                multiples = []
                for i in range(p * p, demo_limit + 1, p):
                    if is_prime[i]:
                        is_prime[i] = False
                        multiples.append(i)

                if multiples:
                    print(f"  除去: {multiples}")
                else:
                    print(f"  除去する数なし ({p}² = {p * p} > {demo_limit})")

                remaining = [i for i in range(2, demo_limit + 1) if is_prime[i]]
                print(f"  残り: {remaining}")

        final_primes = [i for i in range(2, demo_limit + 1) if is_prime[i]]
        print(f"\n最終結果: {final_primes}")

        # Verify against our function
        expected_primes = sieve_of_eratosthenes(demo_limit)
        print(f"関数結果:   {expected_primes}")
        print(f"一致: {'✓' if final_primes == expected_primes else '✗'}")

    def _demonstrate_prime_distribution(self) -> None:
        """Demonstrate prime number distribution and the Prime Number Theorem."""
        print("=== 素数分布と素数定理 ===")

        # Show prime counts for different ranges
        test_limits = [10, 100, 1000, 10000, 100000]
        print(
            f"{'範囲':>10} {'素数個数':>10} {'密度(%)':>10} {'定理予測':>10} {'誤差':>8}"
        )
        print("-" * 55)

        for limit in test_limits:
            primes = sieve_of_eratosthenes(limit - 1)
            prime_count = len(primes)
            density = (prime_count / limit) * 100

            # Prime Number Theorem approximation: π(x) ≈ x / ln(x)
            if limit > 1:
                pnt_estimate = limit / math.log(limit)
                error = abs(prime_count - pnt_estimate)
            else:
                pnt_estimate = 0
                error = 0

            print(
                f"{limit:10,} {prime_count:10,} {density:10.3f} {pnt_estimate:10.0f} {error:8.0f}"
            )

        # Show prime gaps in larger ranges
        print("\n素数ギャップの分析 (100未満):")
        primes_100 = sieve_of_eratosthenes(99)
        gap_counts: dict[int, int] = {}

        for i in range(1, len(primes_100)):
            gap = primes_100[i] - primes_100[i - 1]
            gap_counts[gap] = gap_counts.get(gap, 0) + 1

        print("ギャップ   出現回数")
        for gap in sorted(gap_counts.keys()):
            print(f"{gap:6d} {gap_counts[gap]:10d}")

        # Example calculation for the main problem
        print("\n2,000,000未満での予測:")
        main_limit = 2000000
        pnt_prediction = main_limit / math.log(main_limit)
        print(f"素数定理による素数個数予測: {pnt_prediction:.0f}")

        # Show memory usage estimation for different sieve methods
        print("\nメモリ使用量比較 (2,000,000未満):")
        standard_memory = main_limit  # boolean array
        optimized_memory = main_limit // 2  # odd numbers only

        print(f"標準的な篩: {standard_memory:,} bytes (全数)")
        print(f"最適化篩:   {optimized_memory:,} bytes (奇数のみ)")
        print(
            f"メモリ削減: {((standard_memory - optimized_memory) / standard_memory) * 100:.1f}%"
        )


def main() -> None:
    """Main entry point."""
    runner = Problem010Runner()
    runner.main()


if __name__ == "__main__":
    main()
