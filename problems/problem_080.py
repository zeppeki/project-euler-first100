#!/usr/bin/env python3
"""
Problem 080: Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite and non-repeating.

The square root of two is 1.41421356237309504880168872420969807856967187537694...

The digital sum of the first one hundred decimal digits of √2 is 475.

For the first one hundred natural numbers, find the total of the digital sums of
the first one hundred decimal digits for all the irrational square roots.

Answer: Check Project Euler website for verification
"""

from decimal import Decimal, getcontext


def is_perfect_square(n: int) -> bool:
    """
    完全平方数かどうかを判定する
    時間計算量: O(log n)
    空間計算量: O(1)
    """
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n


def calculate_sqrt_digital_sum_naive(n: int, precision: int = 100) -> int:
    """
    素直な解法: decimal モジュールを使った高精度計算
    時間計算量: O(precision²)
    空間計算量: O(precision)
    """
    if is_perfect_square(n):
        return 0

    # 精度を十分に設定（計算誤差を考慮して多めに）
    getcontext().prec = precision + 50

    # 平方根を計算
    sqrt_n = Decimal(n).sqrt()

    # 文字列に変換して小数点以下の桁を取得
    sqrt_str = str(sqrt_n)

    # 小数点の位置を見つける
    decimal_pos = sqrt_str.find(".")
    if decimal_pos == -1:
        return 0

    # 小数点前の桁数を計算
    integer_part = sqrt_str[:decimal_pos]
    integer_digits = len(integer_part)

    # 必要な桁数を取得（小数点前 + 小数点後）
    if integer_digits >= precision:
        # 整数部分だけで精度を超える場合
        digits = integer_part[:precision]
    else:
        # 整数部分 + 小数点以下の必要桁数
        decimal_digits_needed = precision - integer_digits
        decimal_part = sqrt_str[decimal_pos + 1 :]

        if len(decimal_part) < decimal_digits_needed:
            # 精度が足りない場合（通常は起こらない）
            decimal_part = decimal_part.ljust(decimal_digits_needed, "0")

        digits = integer_part + decimal_part[:decimal_digits_needed]

    # 数字の合計を計算
    return sum(int(digit) for digit in digits if digit.isdigit())


def calculate_sqrt_digital_sum_optimized(n: int, precision: int = 100) -> int:
    """
    最適化解法: Newton-Raphson法による高精度平方根計算
    時間計算量: O(precision × log(precision))
    空間計算量: O(precision)
    """
    if is_perfect_square(n):
        return 0

    # Newton-Raphson法で高精度平方根を計算
    # x_{n+1} = (x_n + n/x_n) / 2

    # 初期値を設定（整数の平方根近似）
    x = Decimal(n**0.5)

    # 必要な精度を設定
    getcontext().prec = precision + 50
    n_decimal = Decimal(n)
    two = Decimal(2)

    # Newton-Raphson法で収束まで計算
    prev_x = Decimal(0)
    iteration_count = 0
    max_iterations = precision * 2  # 安全のための上限

    while (
        abs(x - prev_x) > Decimal(10) ** -(precision + 10)
        and iteration_count < max_iterations
    ):
        prev_x = x
        x = (x + n_decimal / x) / two
        iteration_count += 1

    # 文字列に変換して桁を抽出
    sqrt_str = str(x)
    decimal_pos = sqrt_str.find(".")

    if decimal_pos == -1:
        # 整数の場合（完全平方数）
        return 0

    # 必要な桁数を取得
    integer_part = sqrt_str[:decimal_pos]
    integer_digits = len(integer_part)

    if integer_digits >= precision:
        digits = integer_part[:precision]
    else:
        decimal_digits_needed = precision - integer_digits
        decimal_part = sqrt_str[decimal_pos + 1 :]
        digits = integer_part + decimal_part[:decimal_digits_needed]

    return sum(int(digit) for digit in digits if digit.isdigit())


def solve_naive(limit: int = 100, precision: int = 100) -> int:
    """
    素直な解法: 各数の平方根デジタル和を計算して合計
    時間計算量: O(limit × precision²)
    空間計算量: O(precision)
    """
    total_sum = 0

    for n in range(1, limit + 1):
        if not is_perfect_square(n):
            digital_sum = calculate_sqrt_digital_sum_naive(n, precision)
            total_sum += digital_sum

    return total_sum


def solve_optimized(limit: int = 100, precision: int = 100) -> int:
    """
    最適化解法: Newton-Raphson法による効率的な平方根計算
    時間計算量: O(limit × precision × log(precision))
    空間計算量: O(precision)
    """
    total_sum = 0

    # 完全平方数を事前に特定
    perfect_squares = set()
    i = 1
    while i * i <= limit:
        perfect_squares.add(i * i)
        i += 1

    for n in range(1, limit + 1):
        if n not in perfect_squares:
            digital_sum = calculate_sqrt_digital_sum_optimized(n, precision)
            total_sum += digital_sum

    return total_sum


def get_irrational_square_roots(limit: int) -> list[int]:
    """
    指定された範囲内の無理数平方根を返す
    時間計算量: O(√limit)
    空間計算量: O(limit)
    """
    irrational_roots = []
    perfect_squares = set()

    # 完全平方数を特定
    i = 1
    while i * i <= limit:
        perfect_squares.add(i * i)
        i += 1

    # 無理数平方根を抽出
    for n in range(1, limit + 1):
        if n not in perfect_squares:
            irrational_roots.append(n)

    return irrational_roots


def validate_sqrt_calculation(n: int, precision: int = 10) -> bool:
    """
    平方根計算の検証用関数
    計算した平方根を二乗して元の数に近いかを確認
    """
    if is_perfect_square(n):
        return True

    getcontext().prec = precision + 20
    sqrt_n = Decimal(n).sqrt()
    squared = sqrt_n * sqrt_n

    # 誤差が許容範囲内かを確認
    error = abs(squared - Decimal(n))
    tolerance = Decimal(10) ** -(precision - 2)

    return error < tolerance
