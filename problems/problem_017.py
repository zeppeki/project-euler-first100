#!/usr/bin/env python3
"""
Problem 017: Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

Answer: 21124
"""

import time


def number_to_words(n: int) -> str:
    """
    数値を英語の単語に変換する（イギリス式表記）

    Args:
        n: 変換する数値 (1-1000)

    Returns:
        数値の英語表記
    """
    if n < 1 or n > 1000:
        raise ValueError("Number must be between 1 and 1000")

    # 基本単語の定義
    ones = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    if n == 1000:
        return "one thousand"

    words = []

    # 百の位
    if n >= 100:
        hundreds = n // 100
        words.append(ones[hundreds])
        words.append("hundred")
        n %= 100

        # 100の倍数でない場合は "and" を追加
        if n > 0:
            words.append("and")

    # 十の位と一の位
    if n >= 20:
        tens_digit = n // 10
        ones_digit = n % 10
        words.append(tens[tens_digit])
        if ones_digit > 0:
            words.append(ones[ones_digit])
    elif n > 0:
        words.append(ones[n])

    return " ".join(words)


def count_letters(text: str) -> int:
    """
    テキストの文字数をカウント（スペースとハイフンを除く）

    Args:
        text: カウント対象のテキスト

    Returns:
        文字数
    """
    return len(text.replace(" ", "").replace("-", ""))


def solve_naive(limit: int) -> int:
    """
    素直な解法
    1からlimitまでの各数値を英語に変換し、文字数をカウント

    時間計算量: O(n)
    空間計算量: O(1)
    """
    total_letters = 0

    for i in range(1, limit + 1):
        words = number_to_words(i)
        letters = count_letters(words)
        total_letters += letters

    return total_letters


def solve_optimized(limit: int) -> int:
    """
    最適化解法
    パターンごとの文字数を事前計算し、効率的にカウント

    時間計算量: O(1) - limitが1000以下の場合
    空間計算量: O(1)
    """
    # 基本単語の文字数
    ones_letters = [
        0,
        3,
        3,
        5,
        4,
        4,
        3,
        5,
        5,
        4,  # "", "one", "two", ..., "nine"
        3,
        6,
        6,
        8,
        8,
        7,
        7,
        9,
        8,
        8,
    ]  # "ten", "eleven", ..., "nineteen"

    tens_letters = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]  # "", "", "twenty", ..., "ninety"

    hundred_letters = 7  # "hundred"
    and_letters = 3  # "and"
    thousand_letters = 8  # "thousand"

    total_letters = 0

    if limit >= 1000:
        # "one thousand" = 3 + 8 = 11 letters
        total_letters += ones_letters[1] + thousand_letters
        limit = 999

    # 1-999の計算
    for i in range(1, limit + 1):
        letters = 0

        # 百の位
        if i >= 100:
            hundreds = i // 100
            letters += ones_letters[hundreds] + hundred_letters
            remainder = i % 100

            # "and" を追加（百の倍数でない場合）
            if remainder > 0:
                letters += and_letters

                # 十の位と一の位
                if remainder >= 20:
                    tens_digit = remainder // 10
                    ones_digit = remainder % 10
                    letters += tens_letters[tens_digit]
                    if ones_digit > 0:
                        letters += ones_letters[ones_digit]
                else:
                    letters += ones_letters[remainder]

        else:
            # 1-99の範囲
            if i >= 20:
                tens_digit = i // 10
                ones_digit = i % 10
                letters += tens_letters[tens_digit]
                if ones_digit > 0:
                    letters += ones_letters[ones_digit]
            else:
                letters += ones_letters[i]

        total_letters += letters

    return total_letters


def solve_mathematical(limit: int) -> int:
    """
    数学的解法
    パターン分析による効率的な計算

    時間計算量: O(1) - 限定的な範囲での定数時間計算
    空間計算量: O(1)
    """
    if limit <= 1000:
        # 1000以下は最適化解法を使用（十分に効率的）
        return solve_optimized(limit)

    # より大きな範囲の場合の数学的最適化をここに実装
    # 現在の問題では1000が上限なので、最適化解法で十分
    return solve_optimized(limit)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    # 基本的なテストケース
    test_cases = [
        (1, "one", 3),
        (2, "two", 3),
        (5, "five", 4),
        (12, "twelve", 6),
        (21, "twenty one", 9),
        (42, "forty two", 8),
        (115, "one hundred and fifteen", 20),
        (342, "three hundred and forty two", 23),
        (1000, "one thousand", 11),
    ]

    print("=== 個別テストケース ===")
    for num, expected_words, expected_letters in test_cases:
        actual_words = number_to_words(num)
        actual_letters = count_letters(actual_words)

        print(f"{num}: '{actual_words}' ({actual_letters} letters)")
        print(f"  Expected: '{expected_words}' ({expected_letters} letters)")
        print(f"  Words: {'✓' if actual_words == expected_words else '✗'}")
        print(f"  Letters: {'✓' if actual_letters == expected_letters else '✗'}")
        print()

    # 範囲テストケース
    range_test_cases = [
        (5, 19),  # 1-5: one(3) + two(3) + three(5) + four(4) + five(4) = 19
        (20, 112),  # 予想される値
    ]

    print("=== 範囲テストケース ===")
    for limit, expected in range_test_cases:
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_math = solve_mathematical(limit)

        print(f"1-{limit} の文字数合計:")
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
    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")
    limit = 1000

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(limit)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(limit)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(limit)
    math_time = time.time() - start_time

    print(f"1-{limit} の文字数合計:")
    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized == result_math:
        print(f"✓ 解答: {result_optimized:,}")
    else:
        print("✗ 解答が一致しません")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 追加情報
    print("\n=== 追加情報 ===")
    print("イギリス式表記の特徴:")
    print("- 100以上の数では 'and' を使用")
    print("- 例: 115 = 'one hundred and fifteen'")
    print("- 例: 342 = 'three hundred and forty two'")
    print(f"- 1000 = 'one thousand' ({count_letters(number_to_words(1000))} letters)")


if __name__ == "__main__":
    main()
