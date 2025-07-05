#!/usr/bin/env python3
"""
Problem 009 Runner: Execution and demonstration code for Problem 009.

This module handles the execution and demonstration of Problem 009 solutions,
separated from the core algorithm implementations.
"""

import math
from collections.abc import Callable
from typing import Any

from problems.problem_009 import (
    find_pythagorean_triplet,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem009Runner(BaseProblemRunner):
    """Runner for Problem 009: Special Pythagorean triplet."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "009",
            "Special Pythagorean triplet",
            problem_answer=31875000,  # Known answer for a + b + c = 1000
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 009."""
        return [
            (12, 60),  # (3, 4, 5): 3+4+5=12, 3*4*5=60
            (30, 780),  # (5, 12, 13): 5+12+13=30, 5*12*13=780
            (24, 480),  # (6, 8, 10): 6+8+10=24, 6*8*10=480
            (36, 1620),  # (9, 12, 15): 9+12+15=36, 9*12*15=1620
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 009."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get main problem parameters."""
        return (1000,)

    def run_tests(self) -> bool:
        """
        Run test cases with special handling for mathematical solution.

        The mathematical solution uses Euclid's formula which may find
        different valid Pythagorean triplets than the naive/optimized solutions.
        """
        from problems.utils.display import print_test_results

        test_cases = self.get_test_cases()
        functions = self.get_solution_functions()

        if not test_cases or not functions:
            print("警告: テストケースまたは解法関数が定義されていません")
            return False

        print_test_results(test_cases, functions)

        # Custom validation for this problem
        all_passed = True
        for test_case in test_cases:
            inputs = test_case[:-1]
            expected = test_case[-1]
            target_sum = inputs[0]

            for name, func in functions:
                try:
                    result = func(*inputs)

                    # For mathematical solution, verify it's a valid Pythagorean triplet product
                    if name == "数学的解法":
                        # Verify the result corresponds to a valid Pythagorean triplet
                        is_valid = self._is_valid_pythagorean_product(
                            target_sum, result
                        )
                        if not is_valid:
                            print(
                                f"テスト失敗: {name} - 結果 {result} は和 {target_sum} の有効なピタゴラス数積ではありません"
                            )
                            all_passed = False
                    else:
                        # For naive and optimized, expect exact match
                        if result != expected:
                            print(
                                f"テスト失敗: {name} - 期待値: {expected}, 実際: {result}"
                            )
                            all_passed = False

                except Exception as e:
                    print(f"テスト失敗: {name} - エラー: {e}")
                    all_passed = False

        return all_passed

    def _is_valid_pythagorean_product(self, target_sum: int, product: int) -> bool:
        """Check if the product corresponds to a valid Pythagorean triplet with the given sum."""
        for a in range(1, target_sum // 3):
            for b in range(a + 1, (target_sum - a + 1) // 2):
                c = target_sum - a - b
                if b >= c:
                    continue
                if a * a + b * b == c * c and a * b * c == product:
                    return True
        return False

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 009."""
        return [
            self._demonstrate_pythagorean_properties,
            self._demonstrate_triplet_generation,
            self._demonstrate_euclid_formula,
        ]

    def _demonstrate_pythagorean_properties(self) -> None:
        """Demonstrate properties of Pythagorean triplets."""
        print("=== ピタゴラス数の性質 ===")

        # Show classic examples
        classic_triplets = [
            (3, 4, 5),
            (5, 12, 13),
            (8, 15, 17),
            (7, 24, 25),
            (20, 21, 29),
            (9, 40, 41),
        ]

        print("古典的なピタゴラス数:")
        print(f"{'a':>3} {'b':>3} {'c':>3} {'a²+b²':>8} {'c²':>8} {'和':>6} {'積':>10}")
        print("-" * 45)

        for a, b, c in classic_triplets:
            a_sq_plus_b_sq = a * a + b * b
            c_sq = c * c
            sum_abc = a + b + c
            product_abc = a * b * c
            print(
                f"{a:3d} {b:3d} {c:3d} {a_sq_plus_b_sq:8d} {c_sq:8d} {sum_abc:6d} {product_abc:10d}"
            )

        # Verify Pythagorean theorem for each
        print("\nピタゴラスの定理検証:")
        for a, b, c in classic_triplets:
            if a * a + b * b == c * c:
                print(f"  ({a}, {b}, {c}): ✓ {a}² + {b}² = {c}²")
            else:
                print(f"  ({a}, {b}, {c}): ✗ 不正なピタゴラス数")

    def _demonstrate_triplet_generation(self) -> None:
        """Demonstrate triplet generation for different sums."""
        print("=== 異なる和でのピタゴラス数生成 ===")

        test_sums = [12, 24, 30, 36, 60, 84, 120, 156, 180]
        print(f"{'和':>4} {'a':>3} {'b':>3} {'c':>3} {'積':>10} {'検証':>6}")
        print("-" * 35)

        for target_sum in test_sums:
            triplet = find_pythagorean_triplet(target_sum)
            if triplet:
                a, b, c = triplet
                product = a * b * c
                # Verify
                is_valid = (
                    a * a + b * b == c * c and a + b + c == target_sum and a < b < c
                )
                status = "✓" if is_valid else "✗"
                print(f"{target_sum:4d} {a:3d} {b:3d} {c:3d} {product:10d} {status:>6}")
            else:
                print(
                    f"{target_sum:4d} {'---':>3} {'---':>3} {'---':>3} {'---':>10} {'N/A':>6}"
                )

    def _demonstrate_euclid_formula(self) -> None:
        """Demonstrate Euclid's formula for generating Pythagorean triplets."""
        print("=== ユークリッドの公式によるピタゴラス数生成 ===")
        print("原始ピタゴラス数の一般形:")
        print("  a = m² - n²")
        print("  b = 2mn")
        print("  c = m² + n²")
        print("条件: m > n > 0, gcd(m,n) = 1, m と n の一方は偶数")
        print()

        print(
            f"{'m':>2} {'n':>2} {'a':>3} {'b':>3} {'c':>3} {'和':>6} {'積':>10} {'gcd':>4}"
        )
        print("-" * 40)

        # Generate primitive Pythagorean triplets using Euclid's formula
        for m in range(2, 8):
            for n in range(1, m):
                # Check conditions for primitive triplets
                if math.gcd(m, n) != 1:
                    continue
                if (m % 2) == (n % 2):  # Both odd or both even
                    continue

                # Generate triplet
                a_raw = m * m - n * n
                b_raw = 2 * m * n
                c_raw = m * m + n * n

                # Ensure a < b
                a, b = (a_raw, b_raw) if a_raw < b_raw else (b_raw, a_raw)
                c = c_raw

                sum_abc = a + b + c
                product_abc = a * b * c
                gcd_mn = math.gcd(m, n)

                print(
                    f"{m:2d} {n:2d} {a:3d} {b:3d} {c:3d} {sum_abc:6d} {product_abc:10d} {gcd_mn:4d}"
                )

        print("\n数学的解法はこの公式を使用して効率的に解を探索します")

        # Show how this applies to our problem
        print("\n問題の和=1000での解:")
        triplet_1000 = find_pythagorean_triplet(1000)
        if triplet_1000:
            a, b, c = triplet_1000
            product = a * b * c
            print(f"  ピタゴラス数: ({a}, {b}, {c})")
            print(f"  和: {a} + {b} + {c} = {a + b + c}")
            print(f"  積: {a} × {b} × {c} = {product}")
            print(
                f"  ピタゴラスの定理: {a}² + {b}² = {a * a} + {b * b} = {a * a + b * b} = {c * c} = {c}²"
            )

            # Try to find the m, n values that generate this triplet
            print("\n  この数の生成パラメータを逆算:")
            found_params = False
            for m in range(2, int(math.sqrt(1000)) + 1):
                for n in range(1, m):
                    if math.gcd(m, n) != 1 or (m % 2) == (n % 2):
                        continue

                    a_test = m * m - n * n
                    b_test = 2 * m * n
                    c_test = m * m + n * n

                    # Check for scaling factor
                    for k in range(1, 1000 // (a_test + b_test + c_test) + 1):
                        if k * (a_test + b_test + c_test) == 1000 and {
                            k * a_test,
                            k * b_test,
                            k * c_test,
                        } == {a, b, c}:
                            print(
                                f"    原始ピタゴラス数: ({a_test}, {b_test}, {c_test})"
                            )
                            print(f"    パラメータ: m={m}, n={n}")
                            print(f"    スケール係数: k={k}")
                            found_params = True
                            break
                    if found_params:
                        break
                if found_params:
                    break


def main() -> None:
    """Main entry point."""
    runner = Problem009Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 009."""
    print("=== Problem 009 Performance Benchmark ===")
    runner = Problem009Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
