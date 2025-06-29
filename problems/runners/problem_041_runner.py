#!/usr/bin/env python3
"""
Problem 041 Runner: Pandigital prime

実行・テスト・表示用のランナーモジュール
"""

from problems.problem_041 import solve_mathematical, solve_naive, solve_optimized
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
)
from problems.utils.performance import compare_performance


def test_solutions() -> None:
    """テストケースで解答を検証"""

    # 小さなケースでのテスト用関数
    def test_specific_pandigital_primes() -> None:
        """特定のpandigital素数のテスト"""
        from problems.problem_041 import is_pandigital, is_prime

        # 既知のpandigital素数
        assert is_prime(2143) and is_pandigital(2143, 4), "2143は4桁のpandigital素数"
        assert is_prime(4231) and is_pandigital(4231, 4), "4231は4桁のpandigital素数"

        # 非素数のpandigital数
        assert not is_prime(1234), "1234は素数ではない"
        assert is_pandigital(1234, 4), "1234は4桁のpandigital数"

        print("✓ 特定のpandigital素数テストが完了")

    def test_digit_sum_insight() -> None:
        """桁数の和による数学的洞察のテスト"""
        # 8桁と9桁のpandigital数の桁の和
        sum_8_digits = sum(range(1, 9))  # 1+2+...+8 = 36
        sum_9_digits = sum(range(1, 10))  # 1+2+...+9 = 45

        assert sum_8_digits % 3 == 0, "8桁pandigital数の桁の和は3で割り切れる"
        assert sum_9_digits % 3 == 0, "9桁pandigital数の桁の和は3で割り切れる"

        print("✓ 桁数の和による数学的洞察テストが完了")

    # 個別テストの実行
    test_specific_pandigital_primes()
    test_digit_sum_insight()

    # 全解法の実行と結果確認
    print("全解法の実行と検証中...")

    result_naive = solve_naive()
    result_optimized = solve_optimized()
    result_mathematical = solve_mathematical()

    # 結果の一致確認
    assert result_naive == result_optimized, (
        f"素直な解法と最適化解法の結果が不一致: {result_naive} != {result_optimized}"
    )
    assert result_optimized == result_mathematical, (
        f"最適化解法と数学的解法の結果が不一致: {result_optimized} != {result_mathematical}"
    )

    print(f"✓ 全解法の結果が一致: {result_naive}")


def run_performance_comparison() -> None:
    """Run performance comparison between different solutions."""
    solutions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    results = compare_performance(solutions)
    print_performance_comparison(results)


def main() -> None:
    """メイン実行関数"""
    print_solution_header("Problem 041", "Pandigital prime")

    # テスト実行
    print("解法のテストを実行中...")
    test_solutions()
    print("✓ 全てのテストが完了しました")

    # パフォーマンス比較
    run_performance_comparison()

    # 最終結果の表示
    result = solve_mathematical()  # 最も効率的な解法
    print_final_answer(result)


if __name__ == "__main__":
    main()
