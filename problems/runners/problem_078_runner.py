"""
Runner for Problem 78: Coin partitions
"""

from problems.problem_078 import (
    partition_function_naive,
    partition_function_optimized,
    solve_naive,
    solve_optimized,
)
from problems.utils.display import print_final_answer
from problems.utils.performance import measure_performance


def test_solutions() -> None:
    """
    テストケースで解答を検証
    """
    # テストケース1: 小さい値での分割数の確認
    test_cases = [
        (0, 1),  # p(0) = 1 (空の分割)
        (1, 1),  # p(1) = 1 (1)
        (2, 2),  # p(2) = 2 (2, 1+1)
        (3, 3),  # p(3) = 3 (3, 2+1, 1+1+1)
        (4, 5),  # p(4) = 5 (4, 3+1, 2+2, 2+1+1, 1+1+1+1)
        (5, 7),  # p(5) = 7 (問題文の例)
    ]

    print("分割数の検証:")
    for n, expected in test_cases:
        # 両方の実装で確認
        naive_result = partition_function_naive(n)
        optimized_result = partition_function_optimized(n)

        assert naive_result == expected, (
            f"Naive failed for p({n}): expected {expected}, got {naive_result}"
        )
        assert optimized_result == expected, (
            f"Optimized failed for p({n}): expected {expected}, got {optimized_result}"
        )
        print(f"  p({n}) = {naive_result} ✓")

    # テストケース2: 剰余を取った場合の動作確認
    modulo = 100
    for n in range(10):
        naive_mod = partition_function_naive(n, modulo)
        optimized_mod = partition_function_optimized(n, modulo)
        assert naive_mod == optimized_mod, (
            f"Modulo results differ for n={n}: naive={naive_mod}, optimized={optimized_mod}"
        )

    # テストケース3: より大きな値での一致確認
    for n in [10, 15, 20]:
        naive_result = partition_function_naive(n)
        optimized_result = partition_function_optimized(n)
        assert naive_result == optimized_result, (
            f"Results differ for n={n}: naive={naive_result}, optimized={optimized_result}"
        )
        print(f"  p({n}) = {naive_result} ✓")

    print("\n✓ すべてのテストケースが成功しました")


def main() -> None:
    """
    メイン関数: テストの実行とProject Euler問題の解答
    """
    print("=" * 60)
    print("Problem 78: Coin partitions")
    print("=" * 60)

    # テスト実行
    print("\n▼ テスト実行:")
    test_solutions()

    # 本番の問題を解く
    target_divisor = 1_000_000

    print(f"\n▼ 問題: p(n)が{target_divisor:,}で割り切れる最小のn")

    # 最適化解法の性能測定と結果表示
    print("\n【最適化解法】")
    print("オイラーの五角数定理を使用した高速計算")
    print("時間計算量: O(n²√n), 空間計算量: O(n)")
    optimized_result, optimized_time = measure_performance(
        solve_optimized, target_divisor
    )
    print(f"実行時間: {optimized_time:.6f}秒")
    print(f"結果: n = {optimized_result}")

    # 検証のため実際の分割数を計算（剰余で）
    p_n_mod = partition_function_optimized(optimized_result, target_divisor)
    print(f"\n▼ 検証: p({optimized_result}) mod {target_divisor:,} = {p_n_mod}")
    assert p_n_mod == 0, "結果が正しくありません"

    # 素直な解法は時間がかかるため、小さい値でのみテスト
    print("\n【素直な解法】（小規模テストのみ）")
    print("動的計画法による計算")
    print("時間計算量: O(n³), 空間計算量: O(n²)")
    # 小さい除数でテスト
    small_divisor = 100
    naive_result, naive_time = measure_performance(solve_naive, small_divisor)
    print(f"テスト: p(n)が{small_divisor}で割り切れる最小のn = {naive_result}")
    print(f"実行時間: {naive_time:.6f}秒")

    # 同じ条件で最適化解法も確認
    optimized_small = solve_optimized(small_divisor)
    assert naive_result == optimized_small, (
        f"Small test failed: naive={naive_result}, optimized={optimized_small}"
    )
    print("✓ 小規模テストで両解法の結果が一致")

    print_final_answer(optimized_result)


if __name__ == "__main__":
    main()
