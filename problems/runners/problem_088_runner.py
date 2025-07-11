"""
Runner for Problem 088: Product-sum numbers
"""

from problems.problem_088 import (
    find_minimal_product_sum_numbers,
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

    # Test with examples from problem
    print("問題文の例:")
    print("k=2: 4 = 2 × 2 = 2 + 2")
    print("k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3")
    print("k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4")
    print("k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2")
    print("k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6")

    # Verify minimal product-sum numbers
    print("\n最小積和数の検証:")
    k_values = find_minimal_product_sum_numbers(6)

    for k in range(2, 7):
        if k in k_values:
            print(f"  k={k}: {k_values[k]}")

    # Test sum for k=2 to 6
    print("\nk=2から6の和:")
    result = solve_naive(6)
    expected = 30
    print(f"  計算値: {result}")
    print(f"  期待値: {expected}")
    print(f"  {'✓' if result == expected else '✗'}")

    # Test sum for k=2 to 12
    print("\nk=2から12の和:")
    result2 = solve_naive(12)
    expected2 = 61
    print(f"  計算値: {result2}")
    print(f"  期待値: {expected2}")
    print(f"  {'✓' if result2 == expected2 else '✗'}")


def run_analysis() -> None:
    """Run analysis of product-sum numbers."""
    print("=== 積和数の分析 ===")

    # Analyze small k values
    print("小さいkでの最小積和数:")
    max_k = 20
    k_values = find_minimal_product_sum_numbers(max_k)

    print("  k | 最小積和数 | 分解")
    print("----|-----------|---------")

    for k in range(2, min(11, max_k + 1)):
        if k in k_values:
            n = k_values[k]
            # 簡単な分解例を表示
            if k == 2:
                factors = f"{n // 2} × {n // 2}"
            elif k == 3 and n == 6:
                factors = "1 × 2 × 3"
            elif k == 4 and n == 8:
                factors = "1 × 1 × 2 × 4"
            else:
                factors = "..."
            print(f" {k:2d} | {n:9d} | {factors}")

    # Count unique values
    print("\n重複の分析:")
    unique_values: dict[int, list[int]] = {}
    for k in range(2, max_k + 1):
        if k in k_values:
            n = k_values[k]
            if n not in unique_values:
                unique_values[n] = []
            unique_values[n].append(k)

    # Show duplicates
    print("同じ最小積和数を持つk値:")
    for n, ks in sorted(unique_values.items())[:5]:
        if len(ks) > 1:
            print(f"  {n}: k = {ks}")


def run_problem() -> None:
    """Run the main problem."""
    print("=== 本問題の解答 ===")
    max_k = 12000
    print(f"2≤k≤{max_k}の最小積和数の和を計算中...")
    print()

    # Run with smaller limit for demonstration
    demo_limit = 100
    print(f"デモンストレーション（k≤{demo_limit}）:")

    result_demo, time_demo = measure_performance(solve_optimized, demo_limit)
    print(f"  結果: {result_demo}")
    print(f"  実行時間: {time_demo:.6f}秒")

    # Find unique values for demo
    k_values_demo = find_minimal_product_sum_numbers(demo_limit)
    unique_demo = len(set(k_values_demo.values()))
    print(f"  ユニークな値の数: {unique_demo}")

    # Run full problem
    print(f"\n本問題（k≤{max_k}）:")

    result_full, time_full = measure_performance(solve_optimized, max_k)
    print(f"  結果: {result_full}")
    print(f"  実行時間: {time_full:.6f}秒")

    # Display the final answer
    print_final_answer(result_full)

    # Additional statistics
    print("\n統計情報:")
    k_values_full = find_minimal_product_sum_numbers(max_k)
    unique_full = len(set(k_values_full.values()))
    print(f"  ユニークな最小積和数の個数: {unique_full}")
    print(f"  最大の最小積和数: {max(k_values_full.values())}")
    print(f"  最小の最小積和数: {min(k_values_full.values())}")


def run_performance_comparison() -> None:
    """Compare performance of different solutions."""
    print("=== パフォーマンス比較 ===")

    test_limits = [12, 50, 100, 500, 1000]

    print("上限 k  | 素直な解法 | 最適化解法 | 数学的解法")
    print("--------|-----------|-----------|----------")

    for limit in test_limits:
        # Skip very large limits for naive solution
        if limit <= 100:
            result1, time1 = measure_performance(solve_naive, limit)
            time1_str = f"{time1:.4f}s"
        else:
            result1 = "-"
            time1_str = "    -    "

        result2, time2 = measure_performance(solve_optimized, limit)
        result3, time3 = measure_performance(solve_mathematical, limit)

        print(f"{limit:7d} | {time1_str:>9} | {time2:.4f}s | {time3:.4f}s")

        # Verify all methods give same result
        if limit <= 100:
            assert result1 == result2 == result3


def run_examples() -> None:
    """Run specific examples from the problem."""
    print("=== 具体例の検証 ===")

    # Show factorizations for small product-sum numbers
    examples = [
        (4, 2, [2, 2]),
        (6, 3, [1, 2, 3]),
        (8, 4, [1, 1, 2, 4]),
        (8, 5, [1, 1, 2, 2, 2]),
        (12, 6, [1, 1, 1, 1, 2, 6]),
    ]

    print("積和数の分解例:")
    for n, k, factors in examples:
        prod = 1
        for f in factors:
            prod *= f
        sum_val = sum(factors)

        factors_str = " × ".join(map(str, factors))
        sum_str = " + ".join(map(str, factors))

        print(f"k={k}: {n} = {factors_str} = {sum_str}")
        print(f"       積: {prod}, 和: {sum_val}, 1の個数: {n - sum_val}")
        assert prod == n
        assert sum_val + (n - sum_val) == n
        print()


def main() -> None:
    """Main function."""
    print_solution_header("088", "Product-sum numbers")

    print("積和数の問題\n")

    run_tests()

    print("\n" + "=" * 50)
    run_examples()

    print("\n" + "=" * 50)
    run_analysis()

    print("\n" + "=" * 50)
    run_performance_comparison()

    print("\n" + "=" * 50)
    run_problem()


if __name__ == "__main__":
    main()
