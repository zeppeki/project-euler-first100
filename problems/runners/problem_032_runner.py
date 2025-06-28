#!/usr/bin/env python3
"""
Problem 032 Runner: Pandigital products

実行・表示・パフォーマンス測定を担当
"""

from problems.problem_032 import (
    is_pandigital_1_to_9,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.utils.display import print_final_answer, print_performance_comparison
from problems.utils.performance import compare_performance


def test_solutions() -> bool:
    """テストケースで解答を検証"""
    print("=== パンデジタル判定テスト ===")

    # パンデジタル判定のテストケース
    test_cases = [
        ("123456789", True),   # 正常な1-9パンデジタル
        ("987654321", True),   # 逆順の1-9パンデジタル
        ("123456788", False),  # 8が重複
        ("12345679", False),   # 8文字（不足）
        ("1234567890", False), # 10文字（過多）
        ("023456789", False),  # 0を含む
        ("391867254", True),   # 例題の組み合わせ
    ]

    print("パンデジタル判定:")
    for digits, expected in test_cases:
        result = is_pandigital_1_to_9(digits)
        status = "✓" if result == expected else "✗"
        print(f"  {digits}: {result} {status}")

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
        return True
    print("✗ 解法間で結果が異なります")
    return False


def demonstrate_pandigital_examples() -> None:
    """パンデジタル積の例を表示"""
    print("\n=== パンデジタル積の例 ===")

    # 既知の例
    examples = [
        (39, 186, 7254),   # 39 × 186 = 7254
        (4, 1738, 6952),   # 4 × 1738 = 6952
        (4, 1963, 7852),   # 4 × 1963 = 7852
    ]

    for multiplicand, multiplier, expected_product in examples:
        product = multiplicand * multiplier
        combined = str(multiplicand) + str(multiplier) + str(product)
        is_pandigital = is_pandigital_1_to_9(combined)

        print(f"  {multiplicand} × {multiplier} = {product}")
        print(f"    組み合わせ: {combined}")
        print(f"    パンデジタル: {'✓' if is_pandigital else '✗'}")
        print(f"    検証: {'✓' if product == expected_product else '✗'}")
        print()


def run_problem() -> None:
    """問題の実行"""
    print("Problem 032: Pandigital products")
    print("=" * 50)

    # テストケース実行
    if not test_solutions():
        print("エラー: テストケースが失敗しました")
        return

    # パンデジタル積の例を表示
    demonstrate_pandigital_examples()

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
