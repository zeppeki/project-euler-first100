"""
Runner for Problem 085: Counting rectangles
"""

from problems.problem_085 import count_rectangles, solve_naive, solve_optimized
from problems.utils.display import (
    print_final_answer,
    print_solution_header,
)
from problems.utils.performance import measure_performance


def run_tests() -> None:
    """Run test cases."""
    # Test cases: (m, n, expected_count)
    test_cases = [
        (1, 1, 1),
        (2, 1, 3),
        (3, 2, 18),  # Problem example
        (4, 3, 60),
        (5, 5, 225),
    ]

    print("=== テストケース ===")
    print("長方形の数を確認:")

    for m, n, expected in test_cases:
        count = count_rectangles(m, n)
        status = "✓" if count == expected else "✗"
        print(f"  {m}×{n}グリッド: {count} 個の長方形 (期待値: {expected}) {status}")

    # Test small targets
    print("\n小さい目標値でのテスト:")
    small_targets = [18, 100, 1000]

    for target in small_targets:
        result = solve_naive(target)
        print(f"  目標 {target}に最も近いグリッドの面積: {result}")


def run_problem() -> None:
    """Run the main problem."""
    print("=== 本問題の解答 ===")
    print("200万個に最も近い長方形数を持つグリッドを探索中...")
    print()

    # Run both solutions and compare
    print("素直な解法実行中...")
    result_naive, time_naive = measure_performance(solve_naive)
    print(f"  実行時間: {time_naive:.6f}秒")
    print(f"  結果: {result_naive}")

    print("\n最適化解法実行中...")
    result_optimized, time_optimized = measure_performance(solve_optimized)
    print(f"  実行時間: {time_optimized:.6f}秒")
    print(f"  結果: {result_optimized}")

    print(f"\n速度改善: {time_naive / time_optimized:.2f}倍")

    # Display the final answer
    print_final_answer(result_optimized)

    # Show details about the answer
    print("\n結果の詳細:")
    best_area = result_optimized
    min_diff = float("inf")
    best_m, best_n = 0, 0

    # Find the actual dimensions
    for m in range(1, 100):
        for n in range(1, m + 1):
            if m * n == best_area:
                count = count_rectangles(m, n)
                diff = abs(count - 2000000)
                if diff < min_diff:
                    min_diff = diff
                    best_m, best_n = m, n

    if best_m > 0:
        count = count_rectangles(best_m, best_n)
        print(f"  グリッドサイズ: {best_m}×{best_n}")
        print(f"  面積: {best_area}")
        print(f"  長方形数: {count:,}")
        print(f"  目標との差: {abs(count - 2000000):,}")


def run_analysis() -> None:
    """Run analysis of different grid sizes."""
    print("=== グリッドサイズ分析 ===")
    print("目標に近いグリッドの探索:")

    candidates = []
    for m in range(1, 100):
        for n in range(1, m + 1):
            count = count_rectangles(m, n)
            diff = abs(count - 2000000)
            if diff < 10000:  # Within 10k of target
                candidates.append((m, n, m * n, count, diff))

    # Sort by difference from target
    candidates.sort(key=lambda x: x[4])

    print("\n上位10候補:")
    print("  順位 | サイズ | 面積 | 長方形数 | 差")
    print("  -----|--------|------|----------|----")
    for i, (m, n, area, count, diff) in enumerate(candidates[:10], 1):
        print(f"  {i:3d}  | {m:2d}×{n:2d} | {area:4d} | {count:,} | {diff:,}")


def main() -> None:
    """Main function."""
    print_solution_header("085", "Counting rectangles")

    print("長方形グリッド内の部分長方形の数を計算\n")

    run_tests()

    print("\n" + "=" * 50)
    run_analysis()

    print("\n" + "=" * 50)
    run_problem()


if __name__ == "__main__":
    main()
