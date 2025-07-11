#!/usr/bin/env python3
"""
Project Euler Problem 057: Square root convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√2 = 1 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 1 + 1/(5/2) = 1 + 2/5 = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 1 + 1/(2 + 2/5) = 1 + 1/(12/5) = 1 + 5/12 = 17/12 ≈ 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 1 + 1/(2 + 1/(12/5)) = 1 + 1/(2 + 5/12) = 1 + 1/(29/12) = 1 + 12/29 = 41/29 ≈ 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions have a numerator with more digits than the denominator?
"""

from fractions import Fraction
from typing import Any


def generate_sqrt2_convergent(n: int) -> Fraction:
    """
    √2の第n近似分数を生成する
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n == 0:
        return Fraction(1, 1)

    # √2 = 1 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))
    # これを底から構築する

    # 初期値: 2 (最下層)
    current = Fraction(2, 1)

    # n-1回反復して上に構築
    for _ in range(n - 1):
        current = 2 + Fraction(1, current)

    # 最後に 1 + 1/current
    return 1 + Fraction(1, current)


def count_digits(n: int) -> int:
    """
    数値の桁数を計算する
    時間計算量: O(log n)
    空間計算量: O(1)
    """
    return len(str(abs(n)))


def has_numerator_more_digits(convergent: Fraction) -> bool:
    """
    分数の分子が分母より多くの桁数を持つかチェック
    時間計算量: O(log(max(numerator, denominator)))
    空間計算量: O(1)
    """
    numerator_digits = count_digits(convergent.numerator)
    denominator_digits = count_digits(convergent.denominator)
    return numerator_digits > denominator_digits


def solve_naive(limit: int = 1000) -> int:
    """
    素直な解法: 各近似分数を生成して桁数を比較
    時間計算量: O(n^2)
    空間計算量: O(1)
    """
    count = 0

    for n in range(1, limit + 1):
        convergent = generate_sqrt2_convergent(n)
        if has_numerator_more_digits(convergent):
            count += 1

    return count


def solve_optimized(limit: int = 1000) -> int:
    """
    最適化解法: 反復的に近似分数を計算
    時間計算量: O(n)
    空間計算量: O(1)
    """
    count = 0

    # 初期値: 最初の近似分数 3/2
    numerator = 3
    denominator = 2

    # 最初の近似分数をチェック
    if count_digits(numerator) > count_digits(denominator):
        count += 1

    # 残りの近似分数を反復的に計算
    for _ in range(2, limit + 1):
        # 次の近似分数の計算
        # 新しい分子 = 古い分子 + 2 * 古い分母
        # 新しい分母 = 古い分子 + 古い分母
        new_numerator = numerator + 2 * denominator
        new_denominator = numerator + denominator

        numerator = new_numerator
        denominator = new_denominator

        if count_digits(numerator) > count_digits(denominator):
            count += 1

    return count


def get_convergent_sequence(limit: int = 10) -> list[dict[str, Any]]:
    """
    √2の近似分数の列を取得（分析用）
    """
    convergents = []

    for n in range(1, limit + 1):
        convergent = generate_sqrt2_convergent(n)
        numerator_digits = count_digits(convergent.numerator)
        denominator_digits = count_digits(convergent.denominator)
        has_more_digits = numerator_digits > denominator_digits

        convergents.append(
            {
                "n": n,
                "numerator": convergent.numerator,
                "denominator": convergent.denominator,
                "fraction": convergent,
                "decimal_value": float(convergent),
                "numerator_digits": numerator_digits,
                "denominator_digits": denominator_digits,
                "has_more_digits": has_more_digits,
            }
        )

    return convergents


def analyze_convergent_pattern(limit: int = 100) -> dict[str, Any]:
    """
    近似分数のパターンを分析
    """
    convergents = get_convergent_sequence(limit)

    more_digits_count = sum(1 for c in convergents if c["has_more_digits"])
    more_digits_positions = [c["n"] for c in convergents if c["has_more_digits"]]

    # 桁数の分布
    numerator_digit_counts = {}
    denominator_digit_counts = {}

    for c in convergents:
        num_digits = c["numerator_digits"]
        den_digits = c["denominator_digits"]

        if num_digits not in numerator_digit_counts:
            numerator_digit_counts[num_digits] = 0
        numerator_digit_counts[num_digits] += 1

        if den_digits not in denominator_digit_counts:
            denominator_digit_counts[den_digits] = 0
        denominator_digit_counts[den_digits] += 1

    return {
        "total_convergents": limit,
        "more_digits_count": more_digits_count,
        "more_digits_positions": more_digits_positions,
        "numerator_digit_distribution": numerator_digit_counts,
        "denominator_digit_distribution": denominator_digit_counts,
        "first_few_convergents": convergents[:10],
    }


def demonstrate_convergence() -> list[dict[str, Any]]:
    """
    √2への収束をデモンストレーション
    """
    import math

    sqrt2_actual = math.sqrt(2)

    demonstrations = []
    convergents = get_convergent_sequence(15)

    for c in convergents:
        error = abs(c["decimal_value"] - sqrt2_actual)
        demonstrations.append(
            {
                "n": c["n"],
                "fraction_str": f"{c['numerator']}/{c['denominator']}",
                "decimal_value": c["decimal_value"],
                "error": error,
                "error_scientific": f"{error:.2e}",
                "numerator_digits": c["numerator_digits"],
                "denominator_digits": c["denominator_digits"],
                "has_more_digits": c["has_more_digits"],
            }
        )

    return demonstrations


def find_digit_difference_pattern(limit: int = 100) -> dict[str, Any]:
    """
    分子と分母の桁数の差のパターンを分析
    """
    convergents = get_convergent_sequence(limit)

    digit_differences = []
    for c in convergents:
        diff = c["numerator_digits"] - c["denominator_digits"]
        digit_differences.append(
            {"n": c["n"], "difference": diff, "has_more_digits": c["has_more_digits"]}
        )

    # 差の分布
    difference_distribution = {}
    for d in digit_differences:
        diff = d["difference"]
        if diff not in difference_distribution:
            difference_distribution[diff] = 0
        difference_distribution[diff] += 1

    return {
        "digit_differences": digit_differences,
        "difference_distribution": difference_distribution,
        "positive_differences": [d for d in digit_differences if d["difference"] > 0],
    }


def get_large_convergents(start_n: int = 990, count: int = 10) -> list[dict[str, Any]]:
    """
    大きなnでの近似分数を取得（巨大な数値の例）
    """
    large_convergents = []

    for n in range(start_n, start_n + count):
        convergent = generate_sqrt2_convergent(n)

        # 数値が非常に大きい場合は文字列の一部のみ表示
        num_str = str(convergent.numerator)
        den_str = str(convergent.denominator)

        if len(num_str) > 50:
            num_display = f"{num_str[:20]}...{num_str[-20:]}"
        else:
            num_display = num_str

        if len(den_str) > 50:
            den_display = f"{den_str[:20]}...{den_str[-20:]}"
        else:
            den_display = den_str

        large_convergents.append(
            {
                "n": n,
                "numerator_digits": count_digits(convergent.numerator),
                "denominator_digits": count_digits(convergent.denominator),
                "numerator_display": num_display,
                "denominator_display": den_display,
                "has_more_digits": has_numerator_more_digits(convergent),
            }
        )

    return large_convergents
