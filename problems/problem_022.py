#!/usr/bin/env python3
"""
Problem 022: Names Scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
over five-thousand first names, begin by sorting it into alphabetical order. Then working
out the alphabetical value for each name, multiply this value by its alphabetical position
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score
of 938 × 53 = 49,714.

What is the total of all the name scores in the file?

Answer: 871198282
"""

import os
import time
from pathlib import Path


def get_alphabetical_value(name: str) -> int:
    """
    名前のアルファベット値を計算する（A=1, B=2, ..., Z=26）

    Args:
        name: 計算対象の名前（大文字）

    Returns:
        アルファベット値の合計
    """
    return sum(ord(char) - ord("A") + 1 for char in name.upper())


def load_names_from_file(file_path: str) -> list[str]:
    """
    ファイルから名前のリストを読み込む

    Args:
        file_path: ファイルパス

    Returns:
        名前のリスト
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Names file not found: {file_path}")

    with open(file_path, encoding="utf-8") as f:
        content = f.read().strip()
        # 引用符で囲まれた名前をカンマで分割
        return [name.strip('"') for name in content.split(",")]


def solve_naive(names: list[str]) -> int:
    """
    素直な解法
    名前をソートして各名前のスコアを計算し、合計を求める

    時間計算量: O(n log n) - ソートのため
    空間計算量: O(n) - ソート用の新しいリスト
    """
    # 名前をアルファベット順にソート
    sorted_names = sorted(names)

    total_score = 0

    for position, name in enumerate(sorted_names, 1):
        alphabetical_value = get_alphabetical_value(name)
        name_score = position * alphabetical_value
        total_score += name_score

    return total_score


def solve_optimized(names: list[str]) -> int:
    """
    最適化解法
    インプレースソートと効率的な計算を使用

    時間計算量: O(n log n) - ソートのボトルネック
    空間計算量: O(1) - インプレースソート（元のリストを変更）
    """
    # インプレースソート（元のリストを変更する点に注意）
    names_copy = names.copy()
    names_copy.sort()

    total_score = 0

    for position, name in enumerate(names_copy, 1):
        # 効率的なアルファベット値計算
        alphabetical_value = sum(ord(char) - ord("A") + 1 for char in name)
        total_score += position * alphabetical_value

    return total_score


def solve_mathematical(names: list[str]) -> int:
    """
    数学的解法
    同じアルゴリズムだが、より明確な数学的表現

    時間計算量: O(n log n) - ソートが支配的
    空間計算量: O(n)
    """
    # この問題では、ソートが必須なので数学的な最適化は限定的
    # 代わりに計算の最適化を行う

    sorted_names = sorted(names)

    # より数学的なアプローチ：一度にスコアを計算
    return sum(
        (position + 1) * sum(ord(char) - ord("A") + 1 for char in name)
        for position, name in enumerate(sorted_names)
    )


def create_sample_names() -> list[str]:
    """
    テスト用のサンプル名前リストを作成

    Returns:
        サンプル名前のリスト
    """
    return [
        "MARY",
        "PATRICIA",
        "LINDA",
        "BARBARA",
        "ELIZABETH",
        "JENNIFER",
        "MARIA",
        "SUSAN",
        "MARGARET",
        "DOROTHY",
        "LISA",
        "NANCY",
        "KAREN",
        "BETTY",
        "HELEN",
        "SANDRA",
        "DONNA",
        "CAROL",
        "RUTH",
        "SHARON",
        "MICHELLE",
        "LAURA",
        "SARAH",
        "KIMBERLY",
        "DEBORAH",
        "JESSICA",
        "SHIRLEY",
        "CYNTHIA",
        "ANGELA",
        "MELISSA",
        "BRENDA",
        "AMY",
        "ANNA",
        "REBECCA",
        "VIRGINIA",
        "KATHLEEN",
        "PAMELA",
        "MARTHA",
        "DEBRA",
        "AMANDA",
        "STEPHANIE",
        "CAROLYN",
        "CHRISTINE",
        "MARIE",
        "JANET",
        "CATHERINE",
        "FRANCES",
        "ANN",
        "JOYCE",
        "DIANE",
        "ALICE",
        "JULIE",
        "HEATHER",
        "TERESA",
        "DORIS",
        "GLORIA",
        "EVELYN",
        "JEAN",
        "CHERYL",
        "MILDRED",
        "KATHERINE",
        "JOAN",
        "ASHLEY",
        "JUDITH",
        "ROSE",
        "JANICE",
        "KELLY",
        "NICOLE",
        "JUDY",
        "CHRISTINA",
        "KATHY",
        "THERESA",
        "BEVERLY",
        "DENISE",
        "TAMMY",
        "IRENE",
        "JANE",
        "LORI",
        "RACHEL",
        "MARILYN",
        "ANDREA",
        "KATHRYN",
        "LOUISE",
        "SARA",
        "ANNE",
        "JACQUELINE",
        "WANDA",
        "BONNIE",
        "JULIA",
        "RUBY",
        "LOIS",
        "TINA",
        "PHYLLIS",
        "NORMA",
        "PAULA",
        "DIANA",
        "ANNIE",
        "LILLIAN",
        "EMILY",
        "ROBIN",
        "COLIN",  # COLINを含める（問題文の例として）
    ]


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
    data_file = Path(__file__).parent.parent / "data" / "p022_names.txt"

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
