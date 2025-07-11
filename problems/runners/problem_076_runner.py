"""
Runner for Problem 76: Counting summations
"""

import sys

from problems.problem_076 import solve_naive, solve_optimized
from problems.utils.display import print_final_answer
from problems.utils.performance import measure_performance


def test_solutions() -> None:
    """
    テストケースで解答を検証
    """
    # テストケース1: 問題文の例（5の分割）
    test_n = 5
    expected = 6  # 問題文より
    naive_result = solve_naive(test_n)
    optimized_result = solve_optimized(test_n)

    assert naive_result == expected, (
        f"Naive solution failed for n={test_n}: expected {expected}, got {naive_result}"
    )
    assert optimized_result == expected, (
        f"Optimized solution failed for n={test_n}: expected {expected}, got {optimized_result}"
    )

    # テストケース2: 小さい値
    test_cases = [
        (2, 1),  # 2 = 1 + 1
        (3, 2),  # 3 = 2 + 1, 1 + 1 + 1
        (4, 4),  # 4 = 3 + 1, 2 + 2, 2 + 1 + 1, 1 + 1 + 1 + 1
    ]

    for n, expected in test_cases:
        naive_result = solve_naive(n)
        optimized_result = solve_optimized(n)
        assert naive_result == expected, (
            f"Naive solution failed for n={n}: expected {expected}, got {naive_result}"
        )
        assert optimized_result == expected, (
            f"Optimized solution failed for n={n}: expected {expected}, got {optimized_result}"
        )

    # テストケース3: 大きい値での一致確認
    for n in [10, 20, 30]:
        naive_result = solve_naive(n)
        optimized_result = solve_optimized(n)
        assert naive_result == optimized_result, (
            f"Solutions disagree for n={n}: naive={naive_result}, optimized={optimized_result}"
        )

    print("✓ すべてのテストケースが成功しました")


def main() -> None:
    """
    メイン関数: テストの実行とProject Euler問題の解答
    """
    print("=" * 60)
    print("Problem 76: Counting summations")
    print("=" * 60)

    # テスト実行
    print("\n▼ テスト実行:")
    test_solutions()

    # 本番の問題を解く
    n = 100

    print(f"\n▼ 問題: {n}を2つ以上の正の整数の和で表す方法の数")

    # 素直な解法の性能測定と結果表示
    print("\n【素直な解法】")
    naive_result, naive_time = measure_performance(solve_naive, n)
    print("動的計画法（2次元配列）")
    print("時間計算量: O(n²), 空間計算量: O(n²)")
    print(f"実行時間: {naive_time:.6f}秒")
    print(f"結果: {naive_result:,}")

    # 最適化解法の性能測定と結果表示
    print("\n【最適化解法】")
    optimized_result, optimized_time = measure_performance(solve_optimized, n)
    print("動的計画法（1次元配列）")
    print("時間計算量: O(n²), 空間計算量: O(n)")
    print(f"実行時間: {optimized_time:.6f}秒")
    print(f"結果: {optimized_result:,}")

    # 結果の検証
    print("\n▼ 結果の検証:")
    if naive_result == optimized_result:
        print("✓ すべての解法の結果が一致しました")
        print_final_answer(naive_result)
    else:
        print("✗ 解法の結果が一致しません！")
        sys.exit(1)


if __name__ == "__main__":
    main()
