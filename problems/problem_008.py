#!/usr/bin/env python3
"""
Problem 008: Largest product in a series

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?

Answer: 23514624000
"""

from functools import reduce
from operator import mul

# The 1000-digit number from Project Euler Problem 008
THOUSAND_DIGIT_NUMBER = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace("\n", "").replace(" ", "")


def solve_naive(adjacent_digits: int = 13) -> int:
    """
    素直な解法: 全ての隣接する桁のシーケンスをチェックして積を計算
    時間計算量: O(n * k) where n is number length, k is adjacent digits
    空間計算量: O(1)
    """
    if adjacent_digits <= 0:
        raise ValueError("adjacent_digits must be positive")
    if adjacent_digits > len(THOUSAND_DIGIT_NUMBER):
        raise ValueError("adjacent_digits cannot exceed number length")

    max_product = 0

    # 全ての可能な隣接する桁のシーケンスをチェック
    for i in range(len(THOUSAND_DIGIT_NUMBER) - adjacent_digits + 1):
        # 現在のシーケンスの積を計算
        current_product = 1
        for j in range(i, i + adjacent_digits):
            digit = int(THOUSAND_DIGIT_NUMBER[j])
            current_product *= digit

        max_product = max(max_product, current_product)

    return max_product


def solve_optimized(adjacent_digits: int = 13) -> int:
    """
    最適化解法: スライディングウィンドウ技法でゼロを含むシーケンスをスキップ
    時間計算量: O(n) where n is number length
    空間計算量: O(1)
    """
    if adjacent_digits <= 0:
        raise ValueError("adjacent_digits must be positive")
    if adjacent_digits > len(THOUSAND_DIGIT_NUMBER):
        raise ValueError("adjacent_digits cannot exceed number length")

    max_product = 0

    # スライディングウィンドウでゼロを含まないシーケンスのみを処理
    i = 0
    while i <= len(THOUSAND_DIGIT_NUMBER) - adjacent_digits:
        # 現在位置からadjacent_digits分の桁を取得
        sequence = THOUSAND_DIGIT_NUMBER[i : i + adjacent_digits]

        # ゼロが含まれている場合、ゼロの次の位置まで スキップ
        if "0" in sequence:
            zero_pos = sequence.find("0")
            i += zero_pos + 1
            continue

        # ゼロが含まれていない場合、積を計算
        current_product = 1
        for digit_char in sequence:
            current_product *= int(digit_char)

        max_product = max(max_product, current_product)
        i += 1

    return max_product


def solve_mathematical(adjacent_digits: int = 13) -> int:
    """
    数学的解法: 積の効率的計算とゼロスキップの組み合わせ
    現在の積から古い桁を除いて新しい桁を乗じる方式
    時間計算量: O(n) where n is number length
    空間計算量: O(1)
    """
    if adjacent_digits <= 0:
        raise ValueError("adjacent_digits must be positive")
    if adjacent_digits > len(THOUSAND_DIGIT_NUMBER):
        raise ValueError("adjacent_digits cannot exceed number length")

    max_product = 0

    i = 0
    while i <= len(THOUSAND_DIGIT_NUMBER) - adjacent_digits:
        # 現在位置からadjacent_digits分のシーケンスを取得
        sequence = THOUSAND_DIGIT_NUMBER[i : i + adjacent_digits]

        # ゼロが含まれている場合、ゼロの後まで スキップ
        if "0" in sequence:
            zero_pos = sequence.find("0")
            i += zero_pos + 1
            continue

        # reduce関数を使用して効率的に積を計算
        current_product = reduce(mul, (int(d) for d in sequence), 1)
        max_product = max(max_product, current_product)
        i += 1

    return max_product


def get_max_product_sequence(adjacent_digits: int = 13) -> tuple[str, int]:
    """
    最大積となるシーケンスとその積を返すヘルパー関数
    """
    max_product = 0
    max_sequence = ""

    for i in range(len(THOUSAND_DIGIT_NUMBER) - adjacent_digits + 1):
        sequence = THOUSAND_DIGIT_NUMBER[i : i + adjacent_digits]

        # ゼロが含まれている場合はスキップ
        if "0" in sequence:
            continue

        current_product = reduce(mul, (int(d) for d in sequence), 1)

        if current_product > max_product:
            max_product = current_product
            max_sequence = sequence

    return max_sequence, max_product
