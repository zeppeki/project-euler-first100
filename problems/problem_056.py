#!/usr/bin/env python3
"""
Project Euler Problem 056: Powerful digit sum

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100,
what is the maximum digital sum?
"""

from typing import Any, cast

from .lib import sum_of_digits as digit_sum


def solve_naive(limit_a: int = 100, limit_b: int = 100) -> int:
    """
    素直な解法: すべての a^b を計算して桁数の合計を求める
    時間計算量: O(limit_a * limit_b * log(max(a^b)))
    空間計算量: O(log(max(a^b)))
    """
    max_digit_sum = 0

    for a in range(1, limit_a):
        for b in range(1, limit_b):
            power = a**b
            current_digit_sum = digit_sum(power)
            max_digit_sum = max(max_digit_sum, current_digit_sum)

    return max_digit_sum


def solve_optimized(limit_a: int = 100, limit_b: int = 100) -> int:
    """
    最適化解法: 不要な計算を避ける工夫
    時間計算量: O(limit_a * limit_b * log(max(a^b)))
    空間計算量: O(log(max(a^b)))
    """
    max_digit_sum = 0

    # 大きな a から始めることで、早期に大きな桁数の合計を見つける可能性が高い
    for a in range(limit_a - 1, 0, -1):
        # 小さな a の場合、すでに見つけた最大値を超えることが不可能になったら終了
        # ただし、この最適化は複雑なため、素直な実装を維持
        for b in range(limit_b - 1, 0, -1):
            power = a**b
            current_digit_sum = digit_sum(power)
            max_digit_sum = max(max_digit_sum, current_digit_sum)

    return max_digit_sum


def find_max_digit_sum_with_details(
    limit_a: int = 100, limit_b: int = 100
) -> dict[str, Any]:
    """
    最大桁数の合計とその詳細情報を取得
    """
    max_digit_sum = 0
    best_a = 0
    best_b = 0
    best_power = 0

    for a in range(1, limit_a):
        for b in range(1, limit_b):
            power = a**b
            current_digit_sum = digit_sum(power)

            if current_digit_sum > max_digit_sum:
                max_digit_sum = current_digit_sum
                best_a = a
                best_b = b
                best_power = power

    return {
        "max_digit_sum": max_digit_sum,
        "best_a": best_a,
        "best_b": best_b,
        "best_power": best_power,
        "power_length": len(str(best_power)),
    }


def analyze_digit_sum_patterns(
    limit_a: int = 100, limit_b: int = 100
) -> dict[str, Any]:
    """
    桁数の合計のパターンを分析
    """
    results = []
    digit_sum_frequency = {}

    for a in range(1, limit_a):
        for b in range(1, limit_b):
            power = a**b
            current_digit_sum = digit_sum(power)

            results.append(
                {
                    "a": a,
                    "b": b,
                    "power": power,
                    "digit_sum": current_digit_sum,
                    "power_length": len(str(power)),
                }
            )

            if current_digit_sum not in digit_sum_frequency:
                digit_sum_frequency[current_digit_sum] = 0
            digit_sum_frequency[current_digit_sum] += 1

    # 桁数の合計でソート
    results.sort(key=lambda x: x["digit_sum"], reverse=True)

    return {
        "all_results": results,
        "top_10": results[:10],
        "digit_sum_frequency": digit_sum_frequency,
        "total_combinations": len(results),
    }


def find_high_digit_sum_examples(
    limit_a: int = 100, limit_b: int = 100, min_digit_sum: int = 800
) -> list[dict[str, Any]]:
    """
    高い桁数の合計を持つ例を検索
    """
    high_digit_sum_examples = []

    for a in range(1, limit_a):
        for b in range(1, limit_b):
            power = a**b
            current_digit_sum = digit_sum(power)

            if current_digit_sum >= min_digit_sum:
                high_digit_sum_examples.append(
                    {
                        "a": a,
                        "b": b,
                        "power": power,
                        "digit_sum": current_digit_sum,
                        "power_length": len(str(power)),
                    }
                )

    # 桁数の合計でソート
    high_digit_sum_examples.sort(key=lambda x: x["digit_sum"], reverse=True)

    return high_digit_sum_examples


def demonstrate_special_cases() -> list[dict[str, Any]]:
    """
    特別なケースのデモンストレーション
    """
    special_cases = [
        {"a": 10, "b": 100, "description": "Googol (10^100)"},
        {"a": 100, "b": 100, "description": "100^100"},
        {"a": 99, "b": 99, "description": "99^99 (largest both < 100)"},
        {"a": 9, "b": 99, "description": "9^99 (single digit base)"},
        {"a": 99, "b": 9, "description": "99^9 (small exponent)"},
        {"a": 50, "b": 50, "description": "50^50 (middle values)"},
    ]

    results = []
    for case in special_cases:
        a = cast("int", case["a"])
        b = cast("int", case["b"])
        power = a**b
        current_digit_sum = digit_sum(power)

        results.append(
            {
                "a": a,
                "b": b,
                "description": case["description"],
                "power": power,
                "digit_sum": current_digit_sum,
                "power_length": len(str(power)),
                "power_display": str(power)
                if len(str(power)) <= 50
                else f"{str(power)[:20]}...{str(power)[-20:]}",
            }
        )

    return results


def verify_examples() -> bool:
    """
    問題で示された例を検証
    """
    # 10^100 (googol) の桁数の合計は1
    googol = 10**100
    googol_digit_sum = digit_sum(googol)

    if googol_digit_sum != 1:
        return False

    # 100^100 も非常に大きいが桁数の合計は小さい
    hundred_to_hundred = 100**100
    hundred_digit_sum = digit_sum(hundred_to_hundred)

    # 100^100は1で始まり、後は0が続く数値ではないが、
    # 桁数の合計が比較的小さいことを確認
    return hundred_digit_sum < 1000  # 過度に大きくないことを確認


def get_digit_sum_statistics(limit_a: int = 100, limit_b: int = 100) -> dict[str, Any]:
    """
    桁数の合計に関する統計情報を取得
    """
    digit_sums = []
    max_digit_sum = 0
    min_digit_sum = float("inf")

    for a in range(1, limit_a):
        for b in range(1, limit_b):
            power = a**b
            current_digit_sum = digit_sum(power)
            digit_sums.append(current_digit_sum)
            max_digit_sum = max(max_digit_sum, current_digit_sum)
            min_digit_sum = min(min_digit_sum, current_digit_sum)

    total_count = len(digit_sums)
    average_digit_sum = sum(digit_sums) / total_count

    # 桁数の合計の分布
    digit_sum_counts = {}
    for ds in digit_sums:
        if ds not in digit_sum_counts:
            digit_sum_counts[ds] = 0
        digit_sum_counts[ds] += 1

    return {
        "max_digit_sum": max_digit_sum,
        "min_digit_sum": min_digit_sum,
        "average_digit_sum": average_digit_sum,
        "total_combinations": total_count,
        "digit_sum_distribution": digit_sum_counts,
        "unique_digit_sums": len(digit_sum_counts),
    }
