#!/usr/bin/env python3
"""
Problem 071: Ordered fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order,
find the numerator of the fraction immediately to the left of 3/7.
"""

from math import gcd


def solve_naive(limit: int) -> int:
    """
    素直な解法: 全ての既約分数を生成して3/7に最も近い分数を探す

    時間計算量: O(n² log n)
    空間計算量: O(n²)

    Args:
        limit: 分母の上限値

    Returns:
        3/7のすぐ左の分数の分子
    """
    target = 3 / 7
    best_fraction = 0.0
    best_numerator = 0

    for d in range(2, limit + 1):
        for n in range(1, d):
            if gcd(n, d) == 1:  # 既約分数のみ
                fraction = n / d
                if fraction < target and fraction > best_fraction:
                    best_fraction = fraction
                    best_numerator = n

    return best_numerator


def solve_optimized(limit: int) -> int:
    """
    最適化解法: ファレー数列の性質を利用した効率的な探索

    3/7のすぐ左の分数p/qは、3q - 7p = 1の関係を満たす
    これをqについて解くと: q = (7p + 1)/3

    時間計算量: O(limit)
    空間計算量: O(1)

    Args:
        limit: 分母の上限値

    Returns:
        3/7のすぐ左の分数の分子
    """
    max_p = 0

    # p = 1から始めて、q = (7p + 1)/3 <= limitを満たす最大のpを見つける
    p = 1
    while True:
        if (7 * p + 1) % 3 == 0:  # (7p + 1)が3で割り切れる場合
            q = (7 * p + 1) // 3
            if q <= limit:
                max_p = p
                p += 1
            else:
                break
        else:
            p += 1

    return max_p


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: 直接計算による最適解

    ファレー数列の性質から、3/7のすぐ左の分数p/qは以下を満たす:
    - 3q - 7p = 1
    - q = (7p + 1)/3

    時間計算量: O(1)
    空間計算量: O(1)

    Args:
        limit: 分母の上限値

    Returns:
        3/7のすぐ左の分数の分子
    """
    # q = (7p + 1)/3 <= limit から p <= (3*limit - 1)/7
    max_p_theoretical = (3 * limit - 1) // 7

    # 7p + 1が3で割り切れる最大のpを見つける
    for p in range(max_p_theoretical, 0, -1):
        if (7 * p + 1) % 3 == 0:
            q = (7 * p + 1) // 3
            if q <= limit:
                return p

    return 0


def solve_mediant(limit: int) -> int:
    """
    メディアント法: ファレー数列の中央値性質を利用

    連続する分数a/bとc/dに対して、その間に挿入される分数は
    メディアント (a+c)/(b+d) である

    時間計算量: O(log n)
    空間計算量: O(1)

    Args:
        limit: 分母の上限値

    Returns:
        3/7のすぐ左の分数の分子
    """
    # 2/5が3/7の左側にあることは既知
    a, b = 2, 5  # 左側の分数
    c, d = 3, 7  # 目標の分数

    # メディアント (a+c)/(b+d) を繰り返し計算
    while b + d <= limit:
        a = a + c
        b = b + d

    return a


def find_fraction_left_of_target(
    target_num: int, target_den: int, limit: int
) -> tuple[int, int]:
    """
    指定された分数の左側にある分数を見つける

    Args:
        target_num: 目標分数の分子
        target_den: 目標分数の分母
        limit: 分母の上限値

    Returns:
        (分子, 分母)のタプル
    """
    # 3/7の場合のメディアント法
    if target_num == 3 and target_den == 7:
        # 2/5が3/7の左側にあることは既知
        a, b = 2, 5  # 左側の分数
        c, d = 3, 7  # 目標の分数

        # メディアント (a+c)/(b+d) を繰り返し計算
        while b + d <= limit:
            a = a + c
            b = b + d

        return a, b

    # 一般的なケース
    a, b = 0, 1  # 左側の分数
    c, d = target_num, target_den  # 目標の分数

    # 二分探索的にメディアントを計算
    while b + d <= limit:
        mediant_num = a + c
        mediant_den = b + d

        # メディアントが目標より小さい場合、左側を更新
        if mediant_num * target_den < target_num * mediant_den:
            a, b = mediant_num, mediant_den
        else:
            # メディアントが目標以上の場合、右側を更新
            c, d = mediant_num, mediant_den

    return a, b


def verify_farey_neighbor(p: int, q: int, target_num: int, target_den: int) -> bool:
    """
    ファレー数列での隣接関係を検証

    Args:
        p: 分子
        q: 分母
        target_num: 目標分数の分子
        target_den: 目標分数の分母

    Returns:
        隣接関係があるかどうか
    """
    # ad - bc = 1 (determinant property)
    return target_num * q - target_den * p == 1


def analyze_fraction_sequence(limit: int) -> list[tuple[int, int, float]]:
    """
    3/7付近の分数を分析

    Args:
        limit: 分母の上限値

    Returns:
        (分子, 分母, 分数値)のリスト
    """
    target = 3 / 7
    results = []

    # 3/7の周辺の分数を収集
    for d in range(2, min(limit + 1, 1000)):  # サンプル用に制限
        for n in range(1, d):
            if gcd(n, d) == 1:
                fraction_val = n / d
                if abs(fraction_val - target) < 0.01:  # 3/7に近い分数
                    results.append((n, d, fraction_val))

    # 分数値でソート
    results.sort(key=lambda x: x[2])
    return results
