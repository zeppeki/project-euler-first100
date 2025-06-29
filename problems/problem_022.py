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
