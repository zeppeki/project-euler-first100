#!/usr/bin/env python3
"""
Problem 009: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math


def solve_naive(target_sum: int = 1000) -> int:
    """
    素直な解法: 3重ループで全ての組み合わせをチェック
    時間計算量: O(n³)
    空間計算量: O(1)
    """
    if target_sum <= 0:
        raise ValueError("target_sum must be positive")

    # a < b < c かつ a + b + c = target_sum
    # 最小のピタゴラス数は (3, 4, 5) なので a は最低 1 から開始
    for a in range(1, target_sum // 3):  # a は target_sum の 1/3 未満
        for b in range(
            a + 1, target_sum // 2
        ):  # b は a より大きく、target_sum の 1/2 未満
            c = target_sum - a - b

            # c > b である必要がある
            if c <= b:
                continue

            # ピタゴラスの定理をチェック
            if a * a + b * b == c * c:
                return a * b * c

    return 0  # 解が見つからない場合


def solve_optimized(target_sum: int = 1000) -> int:
    """
    最適化解法: 2重ループで c を計算により求める
    時間計算量: O(n²)
    空間計算量: O(1)
    """
    if target_sum <= 0:
        raise ValueError("target_sum must be positive")

    # a < b < c かつ a + b + c = target_sum
    # c = target_sum - a - b として計算
    for a in range(1, target_sum // 3):  # a は target_sum の 1/3 未満
        for b in range(a + 1, (target_sum - a + 1) // 2):  # b < c を満たすように
            c = target_sum - a - b

            # b < c の条件を確認（念のため）
            if b >= c:
                continue

            # ピタゴラスの定理をチェック
            if a * a + b * b == c * c:
                return a * b * c

    return 0  # 解が見つからない場合


def solve_mathematical(target_sum: int = 1000) -> int:
    """
    数学的解法: 原始ピタゴラス数の生成公式を使用
    時間計算量: O(sqrt(n))
    空間計算量: O(1)

    原始ピタゴラス数の一般形:
    a = m² - n²
    b = 2mn
    c = m² + n²
    ここで m > n > 0, gcd(m,n) = 1, m と n の一方は偶数
    """
    if target_sum <= 0:
        raise ValueError("target_sum must be positive")

    # 原始ピタゴラス数とその倍数を探索
    # m の上限は √(target_sum/2) 程度
    m_limit = int(math.sqrt(target_sum / 2)) + 1

    for m in range(2, m_limit):
        for n in range(1, m):
            # 原始ピタゴラス数の条件をチェック
            if math.gcd(m, n) != 1:
                continue
            if (m % 2) == (n % 2):  # m と n の一方は偶数である必要
                continue

            # 原始ピタゴラス数を生成
            a_primitive = m * m - n * n
            b_primitive = 2 * m * n
            c_primitive = m * m + n * n

            # a < b を保証するため、必要に応じて交換
            if a_primitive > b_primitive:
                a_primitive, b_primitive = b_primitive, a_primitive

            sum_primitive = a_primitive + b_primitive + c_primitive

            # target_sum が原始ピタゴラス数の倍数になるかチェック
            if target_sum % sum_primitive == 0:
                k = target_sum // sum_primitive
                a = k * a_primitive
                b = k * b_primitive
                c = k * c_primitive

                # 解が見つかった
                return a * b * c

    return 0  # 解が見つからない場合


def find_pythagorean_triplet(target_sum: int = 1000) -> tuple[int, int, int] | None:
    """
    指定された和を持つピタゴラス数の組を返すヘルパー関数
    """
    if target_sum <= 0:
        raise ValueError("target_sum must be positive")

    for a in range(1, target_sum // 3):
        for b in range(a + 1, (target_sum - a + 1) // 2):
            c = target_sum - a - b

            # b < c の条件を確認（念のため）
            if b >= c:
                continue

            if a * a + b * b == c * c:
                return (a, b, c)

    return None
