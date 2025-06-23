#!/usr/bin/env python3
"""
Problem 008: Largest product in a series

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?

Answer: 23514624000
"""

import time
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


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (1, 9),  # 1桁の最大値は9
        (2, 81),  # 2桁の最大積（例：9×9=81）
        (4, 5832),  # 問題例：4桁の場合は5832
        (13, 23514624000),  # 本問題：13桁の場合
    ]

    print("=== テストケース ===")
    for digits, expected in test_cases:
        if digits <= len(THOUSAND_DIGIT_NUMBER):
            result_naive = solve_naive(digits)
            result_optimized = solve_optimized(digits)
            result_math = solve_mathematical(digits)

            print(f"Adjacent digits = {digits}")
            print(f"  Expected: {expected}")
            print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
            print(
                f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
            )
            print(
                f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}"
            )
            print()


def main() -> None:
    """メイン関数"""
    adjacent_digits = 13

    print("=== Problem 008: Largest product in a series ===")
    print(f"Finding the largest product of {adjacent_digits} adjacent digits")
    print("In the 1000-digit number")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(adjacent_digits)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(adjacent_digits)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(adjacent_digits)
    math_time = time.time() - start_time

    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized == result_math:
        print(f"✓ 解答: {result_optimized:,}")
    else:
        print("✗ 解答が一致しません")
        print(f"  Naive: {result_naive}")
        print(f"  Optimized: {result_optimized}")
        print(f"  Mathematical: {result_math}")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 詳細な計算過程の表示
    print("\n=== 計算過程の詳細 ===")

    # 最大積となるシーケンスを表示
    max_sequence, max_product = get_max_product_sequence(adjacent_digits)
    print(f"最大積となる{adjacent_digits}桁のシーケンス: {max_sequence}")
    print(f"各桁: {' × '.join(max_sequence)}")
    print(f"積: {max_product:,}")

    # 問題例（4桁の場合）も表示
    print("\n問題例（4桁の場合）:")
    example_sequence, example_product = get_max_product_sequence(4)
    print(f"最大積となる4桁のシーケンス: {example_sequence}")
    print(f"各桁: {' × '.join(example_sequence)} = {example_product}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 全ての隣接するシーケンスをチェックして積を計算")
    print("最適化解法: ゼロを含むシーケンスをスキップするスライディングウィンドウ")
    print("数学的解法: reduce関数を使用した効率的な積計算とゼロスキップ")

    # 1000桁の数値に関する統計
    zero_count = THOUSAND_DIGIT_NUMBER.count("0")
    total_digits = len(THOUSAND_DIGIT_NUMBER)
    print("\n=== 1000桁数値の統計 ===")
    print(f"総桁数: {total_digits}")
    print(f"ゼロの個数: {zero_count}")
    print(f"ゼロの割合: {zero_count / total_digits * 100:.1f}%")
    print(f"最大桁: {max(THOUSAND_DIGIT_NUMBER)}")
    print(f"最小桁: {min(THOUSAND_DIGIT_NUMBER)}")


if __name__ == "__main__":
    main()
