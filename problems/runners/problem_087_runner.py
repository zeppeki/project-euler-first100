"""
Runner for Problem 087: Prime power triples
"""

import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from problems.problem_087 import (
    sieve_of_eratosthenes,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.utils.display import (
    print_final_answer,
    print_solution_header,
)
from problems.utils.performance import measure_performance


def run_tests() -> None:
    """Run test cases."""
    print("=== テストケース ===")

    # Test with small example from problem
    print("問題文の例 (50未満):")
    test_limit = 50
    expected = 4

    result_naive = solve_naive(test_limit)
    result_optimized = solve_optimized(test_limit)
    result_mathematical = solve_mathematical(test_limit)

    print(f"  期待値: {expected}")
    print(f"  素直な解法: {result_naive} {'✓' if result_naive == expected else '✗'}")
    print(
        f"  最適化解法: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
    )
    print(
        f"  数学的解法: {result_mathematical} {'✓' if result_mathematical == expected else '✗'}"
    )

    # Test specific examples from problem
    print("\n具体例の検証:")
    examples = [
        (28, 2, 2, 2),  # 2² + 2³ + 2⁴
        (33, 3, 2, 2),  # 3² + 2³ + 2⁴
        (49, 5, 2, 2),  # 5² + 2³ + 2⁴
        (47, 2, 3, 2),  # 2² + 3³ + 2⁴
    ]

    for total, p2, p3, p4 in examples:
        calculated = p2**2 + p3**3 + p4**4
        status = "✓" if calculated == total else "✗"
        print(f"  {p2}² + {p3}³ + {p4}⁴ = {calculated} (期待: {total}) {status}")


def run_analysis() -> None:
    """Run analysis of prime power triples."""
    print("=== 素数べき乗三項の分析 ===")

    # Analyze contribution of each power
    print("各べき乗の寄与分析:")
    limit = 1000
    primes = sieve_of_eratosthenes(int(limit**0.5))

    squares_count = 0
    cubes_count = 0
    fourths_count = 0

    for p in primes:
        if p * p < limit:
            squares_count += 1
        if p * p * p < limit:
            cubes_count += 1
        if p * p * p * p < limit:
            fourths_count += 1

    print(f"  上限 {limit} での素数の個数:")
    print(f"    平方可能: {squares_count}")
    print(f"    立方可能: {cubes_count}")
    print(f"    4乗可能: {fourths_count}")

    # Show growth pattern
    print("\n成長パターン:")
    test_limits = [50, 100, 500, 1000, 5000, 10000]
    print("  上限  |  個数")
    print("--------|-------")

    for lim in test_limits:
        count = solve_optimized(lim)
        print(f"  {lim:5d} | {count:5d}")


def run_problem() -> None:
    """Run the main problem."""
    print("=== 本問題の解答 ===")
    limit = 50000000
    print("50,000,000未満で素数べき乗三項で表せる数を探索中...")
    print()

    # Run with smaller limit for demonstration
    demo_limit = 100000
    print(f"デモンストレーション（上限: {demo_limit:,}）:")

    result_demo, time_demo = measure_performance(solve_optimized, demo_limit)
    print(f"  結果: {result_demo:,}個")
    print(f"  実行時間: {time_demo:.6f}秒")

    # Run full problem
    print(f"\n本問題（上限: {limit:,}）:")

    result_full, time_full = measure_performance(solve_optimized, limit)
    print(f"  結果: {result_full:,}個")
    print(f"  実行時間: {time_full:.6f}秒")

    # Display the final answer
    print_final_answer(result_full)

    # Show some examples
    print("\n最小の10個の例:")
    all_numbers = []

    # Generate some examples
    primes = sieve_of_eratosthenes(100)
    for p4 in primes[:5]:
        fourth = p4**4
        if fourth >= 1000:
            break
        for p3 in primes[:10]:
            cube = p3**3
            if fourth + cube >= 1000:
                break
            for p2 in primes[:15]:
                square = p2**2
                total = square + cube + fourth
                if total < 1000:
                    all_numbers.append((total, p2, p3, p4))

    # Sort and display
    all_numbers.sort()
    for i, (total, p2, p3, p4) in enumerate(all_numbers[:10]):
        print(f"  {i + 1:2d}. {total:3d} = {p2}² + {p3}³ + {p4}⁴")


def run_performance_comparison() -> None:
    """Compare performance of different solutions."""
    print("=== パフォーマンス比較 ===")

    test_limits = [1000, 10000, 100000, 1000000]

    print("上限     | 素直な解法 | 最適化解法 | 数学的解法")
    print("---------|-----------|-----------|----------")

    for limit in test_limits:
        # Skip very large limits for naive solution
        if limit <= 100000:
            result1, time1 = measure_performance(solve_naive, limit)
            time1_str = f"{time1:.4f}s"
        else:
            result1 = "-"
            time1_str = "    -    "

        result2, time2 = measure_performance(solve_optimized, limit)
        result3, time3 = measure_performance(solve_mathematical, limit)

        print(f"{limit:8,} | {time1_str:>9} | {time2:.4f}s | {time3:.4f}s")

        # Verify all methods give same result
        if limit <= 100000:
            assert result1 == result2 == result3


def main() -> None:
    """Main function."""
    print_solution_header("087", "Prime power triples")

    print("素数べき乗三項の問題\n")

    run_tests()

    print("\n" + "=" * 50)
    run_analysis()

    print("\n" + "=" * 50)
    run_performance_comparison()

    print("\n" + "=" * 50)
    run_problem()


if __name__ == "__main__":
    main()
