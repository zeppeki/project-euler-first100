#!/usr/bin/env python3
"""
Problem 034 Runner: Digit factorials

実行・表示・パフォーマンス測定を担当
"""

from problems.problem_034 import (
    digit_factorial_sum,
    get_digit_factorials,
    is_digit_factorial,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    verify_examples,
)
from problems.utils.display import print_final_answer, print_performance_comparison
from problems.utils.performance import compare_performance


def test_solutions() -> bool:
    """テストケースで解答を検証"""
    print("=== 桁階乗数判定テスト ===")

    # 問題の例を検証
    if not verify_examples():
        print("✗ 例の検証が失敗しました")
        return False
    print("✓ 例の検証が成功しました (145 = 1! + 4! + 5!)")

    # 桁階乗数判定のテストケース
    test_cases = [
        (145, True),  # 例題: 1! + 4! + 5! = 1 + 24 + 120 = 145
        (1, False),  # 1! = 1 は和ではない
        (2, False),  # 2! = 2 は和ではない
        (123, False),  # 1! + 2! + 3! = 1 + 2 + 6 = 9 ≠ 123
        (40585, True),  # 実際の桁階乗数
    ]

    print("\n桁階乗数判定:")
    all_passed = True
    for number, expected in test_cases:
        result = is_digit_factorial(number)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {number}: {result} {status}")
        if result:
            factorial_sum = digit_factorial_sum(number)
            print(f"    階乗和: {factorial_sum}")

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


def demonstrate_digit_factorials() -> None:
    """桁階乗数の例を表示"""
    print("\n=== 桁階乗数の一覧 ===")

    digit_factorials = get_digit_factorials()
    print(f"見つかった桁階乗数: {len(digit_factorials)}個")

    for number in digit_factorials:
        factorial_sum = digit_factorial_sum(number)

        # 各桁と階乗を表示
        digits = []
        factorials = []
        temp = number
        while temp > 0:
            digit = temp % 10
            digits.append(digit)
            factorials.append(f"{digit}!")
            temp //= 10

        digits.reverse()
        factorials.reverse()

        print(f"  {number} = {' + '.join(factorials)} = {factorial_sum}")
        print(
            f"    検証: {number} == {factorial_sum} → {'✓' if number == factorial_sum else '✗'}"
        )
        print()


def demonstrate_mathematical_analysis() -> None:
    """数学的分析の表示"""
    print("\n=== 数学的分析 ===")

    import math

    print("上限の数学的導出:")
    print("d桁の数の最大値 vs d * 9! の比較:")

    for d in range(1, 8):
        max_d_digit = 10**d - 1
        max_factorial_sum = d * math.factorial(9)

        print(f"  {d}桁: 最大値 {max_d_digit:,} vs 階乗和最大 {max_factorial_sum:,}")

        if max_d_digit > max_factorial_sum:
            print(f"    → {d}桁で検索終了 (数値が階乗和を超える)")
            break

    print(f"\n検索上限: {7 * math.factorial(9):,}")

    print("\n桁階乗数の性質:")
    digit_factorials = get_digit_factorials()
    total_sum = sum(digit_factorials)

    print(f"発見された桁階乗数: {digit_factorials}")
    print(f"合計: {total_sum}")


def run_problem() -> None:
    """問題の実行"""
    print("Problem 034: Digit factorials")
    print("=" * 50)

    # テストケース実行
    if not test_solutions():
        print("エラー: テストケースが失敗しました")
        return

    # 桁階乗数の例を表示
    demonstrate_digit_factorials()

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
