#!/usr/bin/env python3
"""
Runner for Problem 022: Names Scores
"""

import time
from pathlib import Path

from problems.problem_022 import (
    create_sample_names,
    get_alphabetical_value,
    load_names_from_file,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    # 小さなサンプルでテスト
    sample_names = ["COLIN", "MARY", "ANN"]

    print("=== 個別テストケース ===")
    for name in sample_names:
        value = get_alphabetical_value(name)
        print(f"{name}: アルファベット値 = {value}")
        # COLIN = 3+15+12+9+14 = 53
        # MARY = 13+1+18+25 = 57
        # ANN = 1+14+14 = 29
    print()

    # ソート後の順序確認
    sorted_sample = sorted(sample_names)
    print("=== ソート順序確認 ===")
    for i, name in enumerate(sorted_sample, 1):
        value = get_alphabetical_value(name)
        score = i * value
        print(f"{i}. {name}: {value} × {i} = {score}")
    print()

    # COLINの特別なテスト（問題文の例）
    if "COLIN" in sample_names:
        # 実際の5000名のリストではCOLINは938番目になる
        colin_value = get_alphabetical_value("COLIN")
        colin_expected_score = 938 * colin_value
        print("=== COLIN特別テスト ===")
        print(f"COLIN のアルファベット値: {colin_value}")
        print(f"938番目での期待スコア: {colin_expected_score}")
        print()

    # 各解法のテスト
    print("=== 解法比較テスト ===")
    sample_names_for_test = create_sample_names()

    result_naive = solve_naive(sample_names_for_test)
    result_optimized = solve_optimized(sample_names_for_test)
    result_math = solve_mathematical(sample_names_for_test)

    print(f"サンプルデータ ({len(sample_names_for_test)} 名) の結果:")
    print(f"  Naive: {result_naive:,}")
    print(f"  Optimized: {result_optimized:,}")
    print(f"  Mathematical: {result_math:,}")

    if result_naive == result_optimized == result_math:
        print("  ✓ 全ての解法が一致")
    else:
        print("  ✗ 解法間で結果が異なります")
    print()


def main() -> None:
    """メイン関数"""
    # テストケース
    test_solutions()

    # データファイルのパス
    data_file = Path(__file__).parent.parent.parent / "data" / "p022_names.txt"

    print("=== 本問題の解答 ===")

    try:
        # 実際のデータファイルから読み込み
        names = load_names_from_file(str(data_file))
        print(f"データファイルから {len(names):,} 個の名前を読み込みました")

    except FileNotFoundError:
        # データファイルがない場合はサンプルデータを使用
        print("データファイルが見つかりません。サンプルデータを使用します。")
        names = create_sample_names()
        print(f"サンプルデータ: {len(names)} 個の名前")
        print("注意: 正確な解答には公式のnames.txtファイルが必要です")

    print()

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(names)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(names)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(names)
    math_time = time.time() - start_time

    print("全名前スコアの合計:")
    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized == result_math:
        print(f"✓ 解答: {result_optimized:,}")
    else:
        print("✗ 解答が一致しません")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 追加情報
    print("\n=== 追加情報 ===")
    print("アルゴリズムの特徴:")
    print("- 文字列のソートが主要な計算コスト")
    print("- アルファベット値計算は線形時間")
    print("- 全体の時間計算量: O(n log n)")
    print(f"- データサイズ: {len(names):,} 個の名前")

    if len(names) < 1000:
        print("注意: サンプルデータを使用しています")
        print("正確な解答には公式のnames.txtファイル（約5000名）が必要です")


if __name__ == "__main__":
    main()
