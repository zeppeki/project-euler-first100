"""
Runner for Problem 77: Prime summations
"""

import sys
from pathlib import Path

# プロジェクトルートをパスに追加
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from problems.problem_077 import (  # noqa: E402
    count_prime_partitions,
    generate_primes,
    solve_naive,
    solve_optimized,
)
from problems.utils.display import print_final_answer  # noqa: E402
from problems.utils.performance import measure_performance  # noqa: E402


def test_solutions() -> None:
    """
    テストケースで解答を検証
    """
    # テストケース1: 問題文の例（10の素数分割）
    test_n = 10
    expected = 5  # 問題文より
    primes = generate_primes(test_n)
    result = count_prime_partitions(test_n, primes)

    assert result == expected, (
        f"Failed for n={test_n}: expected {expected}, got {result}"
    )

    # テストケース2: 小さい値での確認
    test_cases = [
        (2, 1),  # 2 = 2
        (3, 1),  # 3 = 3
        (4, 1),  # 4 = 2 + 2
        (5, 2),  # 5 = 5, 3 + 2
        (6, 2),  # 6 = 3 + 3, 2 + 2 + 2
        (7, 3),  # 7 = 7, 5 + 2, 3 + 2 + 2
    ]

    for n, expected in test_cases:
        primes = generate_primes(n)
        result = count_prime_partitions(n, primes)
        assert result == expected, (
            f"Failed for n={n}: expected {expected}, got {result}"
        )

    # テストケース3: 両方の解法が同じ答えを返すか確認
    target = 10
    naive_result = solve_naive(target)
    optimized_result = solve_optimized(target)
    assert naive_result == optimized_result, (
        f"Solutions disagree: naive={naive_result}, optimized={optimized_result}"
    )

    print("✓ すべてのテストケースが成功しました")


def main() -> None:
    """
    メイン関数: テストの実行とProject Euler問題の解答
    """
    print("=" * 60)
    print("Problem 77: Prime summations")
    print("=" * 60)

    # テスト実行
    print("\n▼ テスト実行:")
    test_solutions()

    # 本番の問題を解く
    target = 5000

    print(f"\n▼ 問題: 素数の和で{target}通り以上表せる最初の数")

    # 素直な解法の性能測定と結果表示
    print("\n【素直な解法】")
    naive_result, naive_time = measure_performance(solve_naive, target)
    print("個別に素数分割を計算")
    print("時間計算量: O(n² × p), 空間計算量: O(n)")
    print(f"実行時間: {naive_time:.6f}秒")
    print(f"結果: {naive_result}")

    # 最適化解法の性能測定と結果表示
    print("\n【最適化解法】")
    optimized_result, optimized_time = measure_performance(solve_optimized, target)
    print("動的計画法で一括計算")
    print("時間計算量: O(n × p), 空間計算量: O(n)")
    print(f"実行時間: {optimized_time:.6f}秒")
    print(f"結果: {optimized_result}")

    # 結果の検証
    print("\n▼ 結果の検証:")
    if naive_result == optimized_result:
        print("✓ すべての解法の結果が一致しました")

        # 実際の分割数を確認
        primes = generate_primes(naive_result)
        ways = count_prime_partitions(naive_result, primes)
        print(f"\n{naive_result}を素数の和で表す方法: {ways}通り")

        print_final_answer(naive_result)
    else:
        print("✗ 解法の結果が一致しません！")
        sys.exit(1)


if __name__ == "__main__":
    main()
