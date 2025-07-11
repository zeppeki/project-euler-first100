#!/usr/bin/env python3
"""
Problem 075: Singular integer right triangles

It turns out that 12 cm is the smallest length of wire that can be bent to form
an integer sided right angle triangle in exactly one way, but there are many more such lengths.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15) or (12,16,20)
40 cm: (8,15,17)
48 cm: (12,16,20) or (15,20,25)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
and other lengths allow more than one solution to be found; for example, 120 cm can be made into
exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of wire, for how many values of L ≤ 1,500,000 is exactly one
integer sided right angle triangle possible?
"""

import math
from typing import Any


def gcd(a: int, b: int) -> int:
    """
    最大公約数を計算（ユークリッドの互除法）

    時間計算量: O(log(min(a, b)))
    空間計算量: O(1)

    Args:
        a: 第1の数値
        b: 第2の数値

    Returns:
        最大公約数
    """
    while b:
        a, b = b, a % b
    return a


def generate_primitive_pythagorean_triples(limit: int) -> list[tuple[int, int, int]]:
    """
    指定された周長以下の原始ピタゴラス三角形を生成

    ユークリッドの公式を使用:
    a = m² - n², b = 2mn, c = m² + n²
    周長 = a + b + c = 2m(m + n)

    時間計算量: O(√limit)
    空間計算量: O(count of primitive triples)

    Args:
        limit: 周長の上限

    Returns:
        原始ピタゴラス三角形のリスト [(a, b, c), ...]
    """
    triples: list[tuple[int, int, int]] = []

    # m > n > 0 の条件で探索
    # 周長 = 2m(m + n) ≤ limit なので m ≤ √(limit/2) 程度
    m_max = int(math.sqrt(limit // 2)) + 1

    for m in range(2, m_max + 1):
        for n in range(1, m):
            # 原始三角形の条件:
            # 1. gcd(m, n) = 1 (互いに素)
            # 2. m と n の一方が偶数、他方が奇数
            if gcd(m, n) == 1 and (m % 2) != (n % 2):
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n

                perimeter = a + b + c
                if perimeter <= limit:
                    # a ≤ b となるように調整
                    if a > b:
                        a, b = b, a
                    triples.append((a, b, c))
                else:
                    break  # この m では上限を超えるので次の m へ

    return triples


def count_triangles_by_perimeter(limit: int) -> dict[int, int]:
    """
    各周長で形成可能な直角三角形の数をカウント

    時間計算量: O(√limit × log(limit))
    空間計算量: O(limit)

    Args:
        limit: 周長の上限

    Returns:
        周長をキー、三角形の数をバリューとする辞書
    """
    triangle_counts: dict[int, int] = {}

    # 原始ピタゴラス三角形を生成
    primitive_triples = generate_primitive_pythagorean_triples(limit)

    # 各原始三角形について、スケールした三角形も考慮
    for a, b, c in primitive_triples:
        base_perimeter = a + b + c

        # k倍スケールした三角形の周長
        k = 1
        while k * base_perimeter <= limit:
            scaled_perimeter = k * base_perimeter
            triangle_counts[scaled_perimeter] = (
                triangle_counts.get(scaled_perimeter, 0) + 1
            )
            k += 1

    return triangle_counts


def solve_naive(limit: int) -> int:
    """
    素直な解法: 各周長で三角形数をカウントして、1個の場合を数える

    時間計算量: O(√limit × log(limit))
    空間計算量: O(limit)

    Args:
        limit: 周長の上限

    Returns:
        ちょうど1つの直角三角形を形成できる周長の数
    """
    triangle_counts = count_triangles_by_perimeter(limit)

    # ちょうど1つの三角形を形成できる周長をカウント
    singular_count = 0
    for _perimeter, count in triangle_counts.items():
        if count == 1:
            singular_count += 1

    return singular_count


def solve_optimized(limit: int) -> int:
    """
    最適化解法: メモリ効率を改善したカウント

    時間計算量: O(√limit × log(limit))
    空間計算量: O(limit)

    Args:
        limit: 周長の上限

    Returns:
        ちょうど1つの直角三角形を形成できる周長の数
    """
    # 各周長での三角形カウント用配列
    counts = [0] * (limit + 1)

    # 原始ピタゴラス三角形を生成してカウント
    m_max = int(math.sqrt(limit // 2)) + 1

    for m in range(2, m_max + 1):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m % 2) != (n % 2):
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n

                base_perimeter = a + b + c
                if base_perimeter > limit:
                    break

                # スケールした三角形をカウント
                k = 1
                while k * base_perimeter <= limit:
                    counts[k * base_perimeter] += 1
                    k += 1

    # ちょうど1つの三角形を形成できる周長をカウント
    return sum(1 for count in counts if count == 1)


def find_triangles_with_perimeter(perimeter: int) -> list[tuple[int, int, int]]:
    """
    指定された周長で形成可能な直角三角形を検索

    時間計算量: O(√perimeter)
    空間計算量: O(count of triangles)

    Args:
        perimeter: 周長

    Returns:
        直角三角形のリスト [(a, b, c), ...]
    """
    triangles: list[tuple[int, int, int]] = []

    # a ≤ b < c の条件で探索
    # a + b + c = perimeter より c = perimeter - a - b
    # a² + b² = c² の条件を確認

    for a in range(1, perimeter // 3 + 1):  # a ≤ b < c なので a ≤ perimeter/3
        for b in range(
            a, (perimeter - a) // 2 + 1
        ):  # b < c なので b ≤ (perimeter - a)/2
            c = perimeter - a - b
            if c > b and a * a + b * b == c * c:  # c > b の条件も追加
                triangles.append((a, b, c))

    return triangles


def analyze_perimeter_distribution(limit: int) -> dict[str, Any]:
    """
    周長分布の分析

    Args:
        limit: 分析する範囲の上限

    Returns:
        分析結果の辞書
    """
    triangle_counts = count_triangles_by_perimeter(limit)

    # 三角形数による分布
    count_distribution: dict[int, int] = {}
    for count in triangle_counts.values():
        count_distribution[count] = count_distribution.get(count, 0) + 1

    # 統計情報
    total_perimeters = len(triangle_counts)
    singular_perimeters = count_distribution.get(1, 0)
    multiple_perimeters = sum(
        freq for count, freq in count_distribution.items() if count > 1
    )

    return {
        "total_valid_perimeters": total_perimeters,
        "singular_perimeters": singular_perimeters,
        "multiple_solution_perimeters": multiple_perimeters,
        "count_distribution": dict(sorted(count_distribution.items())),
        "max_triangles_per_perimeter": max(count_distribution.keys())
        if count_distribution
        else 0,
        "avg_triangles_per_perimeter": sum(
            count * freq for count, freq in count_distribution.items()
        )
        / total_perimeters
        if total_perimeters > 0
        else 0,
    }


def get_examples_by_triangle_count(
    limit: int, target_count: int, max_examples: int = 5
) -> list[tuple[int, list[tuple[int, int, int]]]]:
    """
    指定された三角形数を持つ周長の例を取得

    Args:
        limit: 検索範囲の上限
        target_count: 目標とする三角形数
        max_examples: 最大例数

    Returns:
        (周長, 三角形リスト) のリスト
    """
    triangle_counts = count_triangles_by_perimeter(limit)
    examples: list[tuple[int, list[tuple[int, int, int]]]] = []

    for perimeter, count in sorted(triangle_counts.items()):
        if count == target_count and len(examples) < max_examples:
            triangles = find_triangles_with_perimeter(perimeter)
            examples.append((perimeter, triangles))

    return examples
