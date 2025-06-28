#!/usr/bin/env python3
"""
Problem 032: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written
as a 1 through 9 pandigital.

Answer: 45228
"""


def is_pandigital_1_to_9(digits_str: str) -> bool:
    """
    1から9のパンデジタル数かどうか判定
    時間計算量: O(1) - 最大9文字の固定長
    空間計算量: O(1)
    """
    if len(digits_str) != 9:
        return False

    digit_set = set(digits_str)
    return digit_set == {"1", "2", "3", "4", "5", "6", "7", "8", "9"}


def solve_naive() -> int:
    """
    素直な解法: 全ての可能な組み合わせを総当たりで検証
    時間計算量: O(n^2) - nは探索範囲
    空間計算量: O(k) - kは見つかった積の数
    """
    pandigital_products = set()

    # 全ての可能な乗数と被乗数の組み合わせを試行
    # 1桁 × 4桁 = 4桁のケース: a × bcde = fghi
    for a in range(1, 10):
        for bcde in range(1000, 10000):
            product = a * bcde
            if product >= 10000:  # 5桁以上になったら無意味
                break

            # パンデジタル判定
            combined = str(a) + str(bcde) + str(product)
            if is_pandigital_1_to_9(combined):
                pandigital_products.add(product)

    # 2桁 × 3桁 = 4桁のケース: ab × cde = fghi
    for ab in range(10, 100):
        for cde in range(100, 1000):
            product = ab * cde
            if product >= 10000:  # 5桁以上になったら無意味
                break

            # パンデジタル判定
            combined = str(ab) + str(cde) + str(product)
            if is_pandigital_1_to_9(combined):
                pandigital_products.add(product)

    return sum(pandigital_products)


def solve_optimized() -> int:
    """
    最適化解法: 桁数の制約を利用した効率的な探索
    時間計算量: O(n) - より狭い範囲での探索
    空間計算量: O(k) - kは見つかった積の数
    """
    pandigital_products = set()

    # 数学的分析:
    # 1 × 4桁 = 4桁: 1 + 4 + 4 = 9桁 ✓
    # 2桁 × 3桁 = 4桁: 2 + 3 + 4 = 9桁 ✓
    # その他の組み合わせは9桁にならない

    # 1桁 × 4桁 = 4桁のケース
    for multiplicand in range(1, 10):
        # 4桁の乗数の範囲を計算
        min_multiplier = 1000
        max_multiplier = min(9999, 9999 // multiplicand)

        for multiplier in range(min_multiplier, max_multiplier + 1):
            product = multiplicand * multiplier

            # 積が4桁でない場合はスキップ
            if product < 1000 or product >= 10000:
                continue

            # パンデジタル判定
            combined = str(multiplicand) + str(multiplier) + str(product)
            if is_pandigital_1_to_9(combined):
                pandigital_products.add(product)

    # 2桁 × 3桁 = 4桁のケース
    for multiplicand in range(10, 100):
        # 3桁の乗数の範囲を計算
        min_multiplier = max(100, 1000 // multiplicand)
        max_multiplier = min(999, 9999 // multiplicand)

        if min_multiplier > max_multiplier:
            continue

        for multiplier in range(min_multiplier, max_multiplier + 1):
            product = multiplicand * multiplier

            # 積が4桁でない場合はスキップ
            if product < 1000 or product >= 10000:
                continue

            # パンデジタル判定
            combined = str(multiplicand) + str(multiplier) + str(product)
            if is_pandigital_1_to_9(combined):
                pandigital_products.add(product)

    return sum(pandigital_products)


def solve_mathematical() -> int:
    """
    数学的解法: パンデジタル条件を満たす乗数の桁数パターンの分析
    時間計算量: O(n) - より効率的な探索
    空間計算量: O(k) - kは見つかった積の数
    """
    pandigital_products = set()

    # 数学的洞察:
    # 9桁のパンデジタル数では、可能な乗算パターンは限定される
    # a × bcde = fghi (1 + 4 + 4 = 9)
    # ab × cde = fghi (2 + 3 + 4 = 9)

    def find_pandigital_products_pattern_1() -> set[int]:
        """1桁 × 4桁 = 4桁パターン"""
        products = set()

        # 1桁の乗数は1-9
        for a in range(1, 10):

            # 4桁数の最小値と最大値を計算
            min_4digit = 1000
            max_4digit = 9999

            # より効率的な範囲計算
            start = max(min_4digit, 1000 // a if a != 0 else min_4digit)
            end = min(max_4digit, 9999 // a if a != 0 else max_4digit)

            for bcde in range(start, end + 1):
                product = a * bcde
                if 1000 <= product <= 9999:
                    combined = str(a) + str(bcde) + str(product)
                    if is_pandigital_1_to_9(combined):
                        products.add(product)

        return products

    def find_pandigital_products_pattern_2() -> set[int]:
        """2桁 × 3桁 = 4桁パターン"""
        products = set()

        # 2桁の乗数: 10-99
        for ab in range(10, 100):
            # 3桁の乗数の効率的な範囲計算
            start = max(100, 1000 // ab)
            end = min(999, 9999 // ab)

            if start <= end:
                for cde in range(start, end + 1):
                    product = ab * cde
                    if 1000 <= product <= 9999:
                        combined = str(ab) + str(cde) + str(product)
                        if is_pandigital_1_to_9(combined):
                            products.add(product)

        return products

    # 両パターンの結果を結合
    pandigital_products.update(find_pandigital_products_pattern_1())
    pandigital_products.update(find_pandigital_products_pattern_2())

    return sum(pandigital_products)

