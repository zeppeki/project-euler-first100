#!/usr/bin/env python3
"""
Problem 033 Runner: Digit cancelling fractions

実行・表示・パフォーマンス測定を担当
"""

from problems.problem_033 import (
    get_digit_cancelling_fractions,
    is_digit_cancelling_fraction,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.utils.display import print_final_answer, print_performance_comparison
from problems.utils.performance import compare_performance


def test_solutions() -> bool:
    """テストケースで解答を検証"""
    print("=== 桁キャンセル分数判定テスト ===")

    # 桁キャンセル分数判定のテストケース
    test_cases = [
        (49, 98, True),  # 例題: 49/98 = 4/8
        (16, 64, True),  # 16/64 = 1/4
        (26, 65, True),  # 26/65 = 2/5
        (19, 95, True),  # 19/95 = 1/5
        (30, 50, False),  # 自明な例
        (12, 21, False),  # 桁キャンセルできるが結果が異なる
        (11, 22, False),  # 同じ桁だが桁キャンセルの結果が異なる
        (12, 34, False),  # 共通桁なし
    ]

    print("桁キャンセル分数判定:")
    all_passed = True
    for numerator, denominator, expected in test_cases:
        result = is_digit_cancelling_fraction(numerator, denominator)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {numerator}/{denominator}: {result} {status}")

    print("\n=== 解法一致確認 ===")

    # 全ての解法が同じ結果を返すことを確認
    result_naive = solve_naive()
    result_optimized = solve_optimized()
    result_mathematical = solve_mathematical()

    print(f"素直な解法: {result_naive}")
    print(f"最適化解法: {result_optimized}")
    print(f"数学的解法: {result_mathematical}")

    if result_naive == result_optimized == result_mathematical:
        print("✓ 全ての解法が一致しました")
        return all_passed
    print("✗ 解法間で結果が異なります")
    return False


def demonstrate_digit_cancelling_fractions() -> None:
    """桁キャンセル分数の例を表示"""
    print("\n=== 桁キャンセル分数の一覧 ===")

    fractions = get_digit_cancelling_fractions()
    print(f"見つかった桁キャンセル分数: {len(fractions)}個")

    for numerator, denominator in fractions:
        # 元の分数の値
        original_value = numerator / denominator

        # キャンセル後の分数を見つける
        n1, n2 = divmod(numerator, 10)
        d1, d2 = divmod(denominator, 10)

        cancelled_fraction = None

        # どの桁がキャンセルされたかを特定
        if n1 == d1 and n1 != 0 and d2 != 0:
            cancelled_fraction = f"{n2}/{d2}"
            cancelled_value = n2 / d2
        elif n1 == d2 and n1 != 0 and d1 != 0:
            cancelled_fraction = f"{n2}/{d1}"
            cancelled_value = n2 / d1
        elif n2 == d1 and n2 != 0 and d2 != 0:
            cancelled_fraction = f"{n1}/{d2}"
            cancelled_value = n1 / d2
        elif n2 == d2 and n2 != 0 and d1 != 0:
            cancelled_fraction = f"{n1}/{d1}"
            cancelled_value = n1 / d1

        print(f"  {numerator}/{denominator} = {cancelled_fraction}")
        print(f"    値: {original_value:.6f} = {cancelled_value:.6f}")
        print()


def demonstrate_mathematical_analysis() -> None:
    """数学的分析の表示"""
    print("\n=== 数学的分析 ===")

    fractions = get_digit_cancelling_fractions()

    print("桁キャンセル分数の積:")
    product_num = 1
    product_den = 1

    for numerator, denominator in fractions:
        product_num *= numerator
        product_den *= denominator
        print(f"  {numerator}/{denominator}")

    print(f"\n積: {product_num}/{product_den}")

    # 最大公約数で約分
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    common_divisor = gcd(product_num, product_den)
    reduced_num = product_num // common_divisor
    reduced_den = product_den // common_divisor

    print(f"約分後: {reduced_num}/{reduced_den}")
    print(f"分母: {reduced_den}")


def run_problem() -> None:
    """問題の実行"""
    print("Problem 033: Digit cancelling fractions")
    print("=" * 50)

    # テストケース実行
    if not test_solutions():
        print("エラー: テストケースが失敗しました")
        return

    # 桁キャンセル分数の例を表示
    demonstrate_digit_cancelling_fractions()

    # 数学的分析を表示
    demonstrate_mathematical_analysis()

    print("=== 本問題の解答 ===")

    # パフォーマンス比較と結果表示
    solutions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    results = compare_performance(solutions)
    print_performance_comparison(results)

    # Get the result from the first solution
    first_solution_name = next(iter(results.keys()))
    answer = results[first_solution_name]["result"]
    print_final_answer(answer)


if __name__ == "__main__":
    run_problem()
