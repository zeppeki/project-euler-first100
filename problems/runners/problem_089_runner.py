"""
Runner for Problem 089: Roman numerals
"""

import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from problems.problem_089 import (
    decimal_to_roman,
    roman_to_decimal,
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

    # Test Roman numeral conversion
    print("ローマ数字変換のテスト:")
    test_cases = [
        ("IV", 4),
        ("IX", 9),
        ("XIV", 14),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MCMXC", 1990),
        ("MMXXI", 2021),
    ]

    print("  ローマ数字 → 10進数:")
    for roman, expected in test_cases:
        result = roman_to_decimal(roman)
        status = "✓" if result == expected else "✗"
        print(f"    {roman:6} → {result:4} (期待値: {expected:4}) {status}")

    print("\n  10進数 → ローマ数字:")
    for expected_roman, decimal_val in test_cases:
        result = decimal_to_roman(decimal_val)
        status = "✓" if result == expected_roman else "✗"
        print(f"    {decimal_val:4} → {result:6} (期待値: {expected_roman:6}) {status}")


def run_optimization_examples() -> None:
    """Run optimization examples."""
    print("=== 最適化の例 ===")

    # Examples of non-optimal Roman numerals and their optimizations
    examples = [
        ("IIIIIIIII", "IX", "9を表す非効率な表記"),
        ("VIIII", "IX", "9を表す別の非効率な表記"),
        ("XIIII", "XIV", "14を表す非効率な表記"),
        ("LXXXX", "XC", "90を表す非効率な表記"),
        ("CCCC", "CD", "400を表す非効率な表記"),
        ("DCCCC", "CM", "900を表す非効率な表記"),
    ]

    print("非最適 → 最適 (説明)")
    print("-" * 40)

    total_original = 0
    total_optimized = 0

    for original, optimal, description in examples:
        decimal_value = roman_to_decimal(original)
        computed_optimal = decimal_to_roman(decimal_value)

        original_len = len(original)
        optimal_len = len(optimal)
        saved = original_len - optimal_len

        total_original += original_len
        total_optimized += optimal_len

        status = "✓" if computed_optimal == optimal else "✗"
        print(f"{original:9} → {optimal:4} ({description}) {status}")
        print(f"         文字数: {original_len} → {optimal_len} ({saved}文字節約)")
        print()

    total_saved = total_original - total_optimized
    print(f"合計: {total_original}文字 → {total_optimized}文字 ({total_saved}文字節約)")


def run_pattern_analysis() -> None:
    """Analyze common patterns in Roman numerals."""
    print("=== パターン分析 ===")

    print("よくある非効率パターン:")
    patterns = [
        ("IIII", "IV", "4つのIを減算記法に"),
        ("VIIII", "IX", "VIIIIを減算記法に"),
        ("XXXX", "XL", "4つのXを減算記法に"),
        ("LXXXX", "XC", "LXXXXを減算記法に"),
        ("CCCC", "CD", "4つのCを減算記法に"),
        ("DCCCC", "CM", "DCCCCを減算記法に"),
    ]

    print("  パターン        → 最適化      説明")
    print("  " + "-" * 45)

    for old, new, desc in patterns:
        saved = len(old) - len(new)
        print(f"  {old:12} → {new:8} {desc} ({saved}文字節約)")


def run_problem() -> None:
    """Run the main problem."""
    print("=== 本問題の解答 ===")

    # Check if data file exists
    data_file = "data/p089_roman.txt"
    if not os.path.exists(data_file):
        print(f"データファイル {data_file} が見つかりません。")
        print("テスト用のサンプルデータで実行します。")
        print()

    print("ローマ数字の最適化による文字数節約を計算中...")
    print()

    # Run with different approaches
    result_naive, time_naive = measure_performance(solve_naive, data_file)
    result_optimized, time_optimized = measure_performance(solve_optimized, data_file)
    result_mathematical, time_mathematical = measure_performance(
        solve_mathematical, data_file
    )

    print("結果:")
    print(f"  素直な解法:     {result_naive} 文字節約 (実行時間: {time_naive:.6f}秒)")
    print(
        f"  最適化解法:     {result_optimized} 文字節約 (実行時間: {time_optimized:.6f}秒)"
    )
    print(
        f"  数学的解法:     {result_mathematical} 文字節約 (実行時間: {time_mathematical:.6f}秒)"
    )

    # Verify all approaches give the same result
    if result_naive == result_optimized == result_mathematical:
        print(f"\n✓ 全ての解法が一致しました: {result_naive} 文字節約")
        print_final_answer(result_naive)
    else:
        print("\n✗ 解法間で結果が一致しません。実装を確認してください。")


def run_performance_comparison() -> None:
    """Compare performance of different solutions."""
    print("=== パフォーマンス比較 ===")

    data_file = "data/p089_roman.txt"

    print("解法               | 実行時間   | 結果")
    print("------------------|-----------|-------")

    approaches = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
    ]

    results = []
    for name, func in approaches:
        result, exec_time = measure_performance(func, data_file)
        results.append(result)
        print(f"{name:16} | {exec_time:.6f}s | {result}")

    # Verify consistency
    if len(set(results)) == 1:
        print(f"\n✓ 全ての解法が一致: {results[0]} 文字節約")
    else:
        print(f"\n✗ 結果が一致しません: {results}")


def run_detailed_analysis() -> None:
    """Run detailed analysis of the optimization process."""
    print("=== 詳細分析 ===")

    # Sample data for detailed analysis
    sample_data = [
        "IIIIIIIII",  # 9 characters → IX (2 characters) = 7 saved
        "VIIII",  # 5 characters → IX (2 characters) = 3 saved
        "XIIII",  # 5 characters → XIV (3 characters) = 2 saved
        "LXXXX",  # 5 characters → XC (2 characters) = 3 saved
        "CCCC",  # 4 characters → CD (2 characters) = 2 saved
        "MCCCC",  # 5 characters → MCD (3 characters) = 2 saved
    ]

    print("詳細な変換例:")
    print("元のローマ数字 | 10進数 | 最適化後 | 節約文字数")
    print("-------------|-------|---------|----------")

    total_original = 0
    total_optimized = 0

    for original in sample_data:
        decimal_val = roman_to_decimal(original)
        optimized = decimal_to_roman(decimal_val)

        original_len = len(original)
        optimized_len = len(optimized)
        saved = original_len - optimized_len

        total_original += original_len
        total_optimized += optimized_len

        print(f"{original:12} | {decimal_val:5} | {optimized:8} | {saved:8}")

    total_saved = total_original - total_optimized
    print("-" * 45)
    print(f"合計         |       |          | {total_saved:8}")
    print()
    print(f"元の文字数合計: {total_original}")
    print(f"最適化後合計:   {total_optimized}")
    print(f"節約文字数:     {total_saved}")

    if total_original > 0:
        efficiency = (total_saved / total_original) * 100
        print(f"効率化率:       {efficiency:.1f}%")


def main() -> None:
    """Main function."""
    print_solution_header("089", "Roman numerals")

    print("ローマ数字の最適化問題\n")

    run_tests()

    print("\n" + "=" * 50)
    run_optimization_examples()

    print("\n" + "=" * 50)
    run_pattern_analysis()

    print("\n" + "=" * 50)
    run_detailed_analysis()

    print("\n" + "=" * 50)
    run_performance_comparison()

    print("\n" + "=" * 50)
    run_problem()


if __name__ == "__main__":
    main()
