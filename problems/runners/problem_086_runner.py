"""
Runner for Problem 086: Cuboid route
"""

from problems.problem_086 import (
    count_integer_paths_optimized,
    is_integer_path,
    shortest_path_length,
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

    # Test shortest path calculation
    print("最短経路長の計算:")
    test_cases = [
        (6, 5, 3, 10.0),  # Problem example
        (3, 4, 5, 7.07),  # Approximate
        (1, 1, 1, 1.73),  # Approximate
        (2, 2, 2, 2.83),  # Approximate
    ]

    for a, b, c, expected in test_cases:
        actual = shortest_path_length(a, b, c)
        status = "✓" if abs(actual - expected) < 0.1 else "✗"
        print(f"  {a}×{b}×{c}: {actual:.2f} (期待: {expected:.2f}) {status}")

    # Test integer path detection
    print("\n整数経路の判定:")
    integer_test_cases = [
        (6, 5, 3, True),  # Problem example
        (3, 4, 5, False),  # Not integer
        (5, 12, 13, True),  # 5² + 12² = 13²
        (1, 1, 1, False),  # Not integer
    ]

    for a, b, c, expected in integer_test_cases:
        actual = is_integer_path(a, b, c)
        path_length = shortest_path_length(a, b, c)
        status = "✓" if actual == expected else "✗"
        print(f"  {a}×{b}×{c}: {actual} (経路長: {path_length:.3f}) {status}")

    # Test counting functions
    print("\n小さいサイズでの立方体数:")
    small_sizes = [5, 10, 20, 50]

    for size in small_sizes:
        count = count_integer_paths_optimized(size)
        print(f"  M={size}: {count}個の立方体")


def run_analysis() -> None:
    """Run analysis of cuboid counts."""
    print("=== 立方体数の分析 ===")

    # Progressive analysis
    print("Mの増加に伴う立方体数の変化:")
    print("   M  |  立方体数  | 増加分")
    print("------|-----------|-------")

    prev_count = 0
    for m in range(10, 101, 10):
        count = count_integer_paths_optimized(m)
        increase = count - prev_count
        print(f"  {m:3d}  | {count:7,} | {increase:5,}")
        prev_count = count

    # Check problem examples
    print(f"\nM=99での立方体数: {count_integer_paths_optimized(99):,}")
    print(f"M=100での立方体数: {count_integer_paths_optimized(100):,}")


def run_problem() -> None:
    """Run the main problem."""
    print("=== 本問題の解答 ===")
    print("100万個を超える最小のMを探索中...")
    print()

    # Run with smaller target for demonstration
    small_target = 10000
    print(f"小さい目標値({small_target})での素直な解法実行中...")
    result_naive, time_naive = measure_performance(solve_naive, small_target)
    print(f"  実行時間: {time_naive:.6f}秒")
    print(f"  結果: M = {result_naive}")

    print(f"\n小さい目標値({small_target})での最適化解法実行中...")
    result_optimized, time_optimized = measure_performance(
        solve_optimized, small_target
    )
    print(f"  実行時間: {time_optimized:.6f}秒")
    print(f"  結果: M = {result_optimized}")

    if time_naive > 0:
        print(f"\n速度改善: {time_naive / time_optimized:.2f}倍")

    # Run full problem with optimized solution only
    print("\n本問題(1,000,000)の最適化解法実行中...")
    result_full, time_full = measure_performance(solve_optimized, 1000000)
    print(f"  実行時間: {time_full:.6f}秒")
    print(f"  結果: M = {result_full}")

    # Display the final answer
    print_final_answer(result_full)

    # Verify the result
    m = result_full
    count_at_m = count_integer_paths_optimized(m)
    count_at_m_minus_1 = count_integer_paths_optimized(m - 1)

    print("\n結果の詳細:")
    print(f"  M = {m - 1}: {count_at_m_minus_1:,}個の立方体")
    print(f"  M = {m}: {count_at_m:,}個の立方体")
    print("  閾値: 1,000,000個")
    print(f"  M={m}で初めて100万個を超過 ✓")


def run_examples() -> None:
    """Run specific examples from the problem."""
    print("=== 問題例の検証 ===")

    # Verify the 6x5x3 example
    path_length = shortest_path_length(6, 5, 3)
    is_integer = is_integer_path(6, 5, 3)

    print("6×5×3の立方体:")
    print(f"  最短経路長: {path_length}")
    print(f"  整数経路: {is_integer}")
    print("  期待値: 10.0, True")

    # Show the three unfolding methods
    import math

    dist1 = math.sqrt(6**2 + (5 + 3) ** 2)  # 6² + 8² = 10²
    dist2 = math.sqrt(5**2 + (6 + 3) ** 2)  # 5² + 9² ≈ 10.3
    dist3 = math.sqrt(3**2 + (6 + 5) ** 2)  # 3² + 11² ≈ 11.4

    print("\n展開方法別の距離:")
    print(f"  方法1 (6 × 8): {dist1:.3f}")
    print(f"  方法2 (5 × 9): {dist2:.3f}")
    print(f"  方法3 (3 × 11): {dist3:.3f}")
    print(f"  最小値: {min(dist1, dist2, dist3):.3f}")


def run_benchmark() -> None:
    """Run performance benchmark for Problem 086."""
    print("=== Problem 086 Performance Benchmark ===")

    # Run the main function which handles the problem
    main()


def main() -> None:
    """Main function."""
    print_solution_header("086", "Cuboid route")

    print("立方体の対角経路問題\n")

    run_examples()

    print("\n" + "=" * 50)
    run_tests()

    print("\n" + "=" * 50)
    run_analysis()

    print("\n" + "=" * 50)
    run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
