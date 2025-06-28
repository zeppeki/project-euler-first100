#!/usr/bin/env python3
"""
Problem 033: Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
is obtained by cancelling the 9s.

We shall consider fractions like 30/50 = 3/5, to be trivial examples.

There are exactly four such fractions, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

Answer: 100
"""

from fractions import Fraction


def gcd(a: int, b: int) -> int:
    """
    最大公約数を求める（ユークリッドの互除法）
    時間計算量: O(log(min(a, b)))
    空間計算量: O(1)
    """
    while b:
        a, b = b, a % b
    return a


def is_digit_cancelling_fraction(numerator: int, denominator: int) -> bool:
    """
    桁キャンセル分数かどうか判定
    時間計算量: O(1) - 固定長の数字操作
    空間計算量: O(1)
    """
    # 自明な例（分母・分子が10の倍数）は除外
    if numerator % 10 == 0 and denominator % 10 == 0:
        return False

    # 分数は1未満でなければならない
    if numerator >= denominator:
        return False

    # 2桁の数字であることを確認
    if numerator < 10 or numerator > 99 or denominator < 10 or denominator > 99:
        return False

    # 各桁を取得
    n1, n2 = divmod(numerator, 10)
    d1, d2 = divmod(denominator, 10)

    # 共通の桁があるかチェック
    common_digit_found = False
    cancelled_num = 0
    cancelled_den = 0

    # n1 == d1の場合: n2/d2と比較
    if n1 == d1 and n1 != 0 and d2 != 0:
        cancelled_num = n2
        cancelled_den = d2
        common_digit_found = True

    # n1 == d2の場合: n2/d1と比較
    elif n1 == d2 and n1 != 0 and d1 != 0:
        cancelled_num = n2
        cancelled_den = d1
        common_digit_found = True

    # n2 == d1の場合: n1/d2と比較
    elif n2 == d1 and n2 != 0 and d2 != 0:
        cancelled_num = n1
        cancelled_den = d2
        common_digit_found = True

    # n2 == d2の場合: n1/d1と比較
    elif n2 == d2 and n2 != 0 and d1 != 0:
        cancelled_num = n1
        cancelled_den = d1
        common_digit_found = True

    if not common_digit_found or cancelled_den == 0:
        return False

    # 元の分数とキャンセル後の分数が等しいかチェック
    # numerator/denominator == cancelled_num/cancelled_den
    # 交差乗算で比較: numerator * cancelled_den == denominator * cancelled_num
    return numerator * cancelled_den == denominator * cancelled_num


def solve_naive() -> int:
    """
    素直な解法: 全ての2桁分数を総当たりで検証
    時間計算量: O(n²) - nは2桁数の範囲
    空間計算量: O(k) - kは見つかった分数の数
    """
    digit_cancelling_fractions = []

    # 全ての2桁分数をチェック
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):  # numerator < denominator
            if is_digit_cancelling_fraction(numerator, denominator):
                digit_cancelling_fractions.append((numerator, denominator))

    # 4つの分数の積を計算
    if len(digit_cancelling_fractions) != 4:
        raise ValueError(
            f"Expected 4 fractions, found {len(digit_cancelling_fractions)}"
        )

    # 分数の積を計算
    product_num = 1
    product_den = 1

    for num, den in digit_cancelling_fractions:
        product_num *= num
        product_den *= den

    # 最小公倍数に約分
    common_divisor = gcd(product_num, product_den)
    return product_den // common_divisor


def solve_optimized() -> int:
    """
    最適化解法: 共通桁の存在を事前にチェックして効率化
    時間計算量: O(n) - より効率的な探索
    空間計算量: O(k) - kは見つかった分数の数
    """
    digit_cancelling_fractions = []

    # 各桁の組み合わせごとに効率的に探索
    for common_digit in range(1, 10):  # 共通桁（0は除外）
        # パターン1: (10a + common_digit) / (10common_digit + b) = a / b
        for a in range(1, 10):
            for b in range(1, 10):
                if a < b:  # 分数が1未満
                    numerator = 10 * a + common_digit
                    denominator = 10 * common_digit + b

                    # 自明でない場合のみ（両方が10の倍数でない）
                    if (
                        10 <= numerator <= 99
                        and 10 <= denominator <= 99
                        and not (numerator % 10 == 0 and denominator % 10 == 0)
                        and numerator * b == denominator * a
                    ):
                        digit_cancelling_fractions.append((numerator, denominator))

        # パターン2: (10a + common_digit) / (10b + common_digit) = a / b
        for a in range(1, 10):
            for b in range(1, 10):
                if a < b:  # 分数が1未満
                    numerator = 10 * a + common_digit
                    denominator = 10 * b + common_digit

                    # 自明でない場合のみ
                    if (
                        10 <= numerator <= 99
                        and 10 <= denominator <= 99
                        and not (numerator % 10 == 0 and denominator % 10 == 0)
                        and numerator * b == denominator * a
                    ):
                        digit_cancelling_fractions.append((numerator, denominator))

        # パターン3: (10common_digit + a) / (10b + common_digit) = a / b
        for a in range(1, 10):
            for b in range(1, 10):
                if a < b:  # 分数が1未満
                    numerator = 10 * common_digit + a
                    denominator = 10 * b + common_digit

                    # 自明でない場合のみ
                    if (
                        10 <= numerator <= 99
                        and 10 <= denominator <= 99
                        and not (numerator % 10 == 0 and denominator % 10 == 0)
                        and numerator * b == denominator * a
                    ):
                        digit_cancelling_fractions.append((numerator, denominator))

    # 重複を除去
    digit_cancelling_fractions = list(set(digit_cancelling_fractions))

    # 4つの分数の積を計算
    if len(digit_cancelling_fractions) != 4:
        raise ValueError(
            f"Expected 4 fractions, found {len(digit_cancelling_fractions)}"
        )

    # Fractionクラスを使用して正確な計算
    product = Fraction(1, 1)
    for num, den in digit_cancelling_fractions:
        product *= Fraction(num, den)

    return product.denominator


def solve_mathematical() -> int:
    """
    数学的解法: 分数の性質を利用した探索の最適化
    時間計算量: O(1) - 数学的分析による直接計算
    空間計算量: O(1)
    """
    # 数学的分析による直接的なアプローチ
    # 桁キャンセル分数の条件を数式で表現

    digit_cancelling_fractions = []

    # 数学的分析: (10a + c) / (10c + b) = a / b
    # この場合: (10a + c) * b = (10c + b) * a
    # 展開: 10ab + cb = 10ca + ba
    # 整理: 10ab + cb = 10ca + ab
    # 9ab + cb = 10ca
    # b(9a + c) = 10ca
    # b = 10ca / (9a + c)

    for a in range(1, 10):
        for c in range(1, 10):
            if (10 * c * a) % (9 * a + c) == 0:
                b = (10 * c * a) // (9 * a + c)
                if 1 <= b <= 9 and a < b:  # 有効な桁かつ分数が1未満
                    numerator = 10 * a + c
                    denominator = 10 * c + b
                    if 10 <= numerator <= 99 and 10 <= denominator <= 99:
                        digit_cancelling_fractions.append((numerator, denominator))

    # 数学的分析: (10a + c) / (10b + c) = a / b
    # この場合: (10a + c) * b = (10b + c) * a
    # 展開: 10ab + cb = 10ba + ca
    # 整理: cb = ca
    # c(b - a) = 0
    # この場合はc = 0または a = bとなり、有効な解はない（c = 0は自明、a = bは分数が1）

    # 数学的分析: (10c + a) / (10b + c) = a / b
    # この場合: (10c + a) * b = (10b + c) * a
    # 展開: 10cb + ab = 10ba + ca
    # 整理: 10cb + ab = 10ab + ca
    # 10cb - 9ab = ca
    # b(10c - 9a) = ca
    # b = ca / (10c - 9a)

    for a in range(1, 10):
        for c in range(1, 10):
            if 10 * c - 9 * a > 0 and (c * a) % (10 * c - 9 * a) == 0:
                b = (c * a) // (10 * c - 9 * a)
                if 1 <= b <= 9 and a < b:  # 有効な桁かつ分数が1未満
                    numerator = 10 * c + a
                    denominator = 10 * b + c
                    if 10 <= numerator <= 99 and 10 <= denominator <= 99:
                        digit_cancelling_fractions.append((numerator, denominator))

    # 重複を除去
    digit_cancelling_fractions = list(set(digit_cancelling_fractions))

    # 4つの分数の積を計算
    if len(digit_cancelling_fractions) != 4:
        raise ValueError(
            f"Expected 4 fractions, found {len(digit_cancelling_fractions)}"
        )

    # 積を計算
    product = Fraction(1, 1)
    for num, den in digit_cancelling_fractions:
        product *= Fraction(num, den)

    return product.denominator


def get_digit_cancelling_fractions() -> list[tuple[int, int]]:
    """
    桁キャンセル分数のリストを取得（デバッグ用）
    """
    fractions = []

    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            if is_digit_cancelling_fraction(numerator, denominator):
                fractions.append((numerator, denominator))

    return fractions
