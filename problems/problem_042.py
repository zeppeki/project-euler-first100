#!/usr/bin/env python3
"""
Problem 042: Coded triangle numbers

The nth term of the sequence of triangle numbers is given by tn = n(n+1)/2.
So the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55.

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value. For example, the word value
for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we
shall call it a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words,
how many of the words are triangle words?

Answer: [Hidden]
"""

import os


def get_word_value(word: str) -> int:
    """
    文字列の語彙値を計算（A=1, B=2, ...）
    時間計算量: O(m) where m is word length
    空間計算量: O(1)
    """
    return sum(ord(char) - ord("A") + 1 for char in word.upper())


def generate_triangle_numbers(max_value: int) -> set[int]:
    """
    指定された最大値までの三角数を生成
    時間計算量: O(√max_value)
    空間計算量: O(√max_value)
    """
    triangle_numbers = set()
    n = 1
    while True:
        triangle_num = n * (n + 1) // 2
        if triangle_num > max_value:
            break
        triangle_numbers.add(triangle_num)
        n += 1
    return triangle_numbers


def is_triangle_number(num: int) -> bool:
    """
    数値が三角数かどうか判定（数式解法）
    時間計算量: O(1)
    空間計算量: O(1)
    """
    # tn = n(n+1)/2 = num
    # n^2 + n - 2*num = 0
    # n = (-1 + sqrt(1 + 8*num)) / 2
    import math

    discriminant = 1 + 8 * num
    if discriminant < 0:
        return False

    sqrt_discriminant = math.sqrt(discriminant)
    n = (-1 + sqrt_discriminant) / 2

    return n.is_integer() and n > 0


def load_words() -> list[str]:
    """
    データファイルから単語リストを読み込み
    時間計算量: O(n) where n is file size
    空間計算量: O(w) where w is number of words
    """
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(script_dir, "data", "p042_words.txt")

    with open(file_path) as file:
        content = file.read().strip()
        # Remove quotes and split by comma
        return [word.strip('"') for word in content.split(",")]


def solve_naive() -> int:
    """
    素直な解法: 全三角数を事前生成してセット検索
    時間計算量: O(n + √max_value) where n is number of words
    空間計算量: O(√max_value)
    """
    words = load_words()

    # Find maximum possible word value to generate triangle numbers
    max_word_value = max(get_word_value(word) for word in words)

    # Generate all triangle numbers up to max word value
    triangle_numbers = generate_triangle_numbers(max_word_value)

    # Count triangle words
    triangle_word_count = 0
    for word in words:
        word_value = get_word_value(word)
        if word_value in triangle_numbers:
            triangle_word_count += 1

    return triangle_word_count


def solve_optimized() -> int:
    """
    最適化解法: 各単語に対して数学的に三角数判定
    時間計算量: O(n) where n is number of words
    空間計算量: O(1)
    """
    words = load_words()

    triangle_word_count = 0
    for word in words:
        word_value = get_word_value(word)
        if is_triangle_number(word_value):
            triangle_word_count += 1

    return triangle_word_count
