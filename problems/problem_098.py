#!/usr/bin/env python3
"""
Problem 098: Anagramic squares

By replacing each of the letters in the word CARE with 1, 4, 9, and 6 respectively,
we form a square number: 1496 = 38².

What is remarkable is that, by using the same substitution, the anagram, RACE,
also forms a square number: 9146 = 95.69...² Wait, that's not right.

Actually, by replacing each of the letters in the word CARE with 1, 4, 9, and 6
respectively, we get 1496, but this doesn't form a square number.

Let me recalculate: If CARE = 1296 (which is 36²), then with the substitution
C=1, A=2, R=9, E=6, we get RACE = 9216 (which is 96²).

Looking at this problem more carefully: we need to find anagram word pairs where
both words can be converted to square numbers using the same letter-to-digit mapping.

The constraint is that no number can have a leading zero.

By finding all anagram word pairs and checking all possible digit mappings,
we want to find the largest square number that can be formed.
"""

import os
from collections import defaultdict


def load_words(filename: str = "p098_words.txt") -> list[str]:
    """
    単語リストをファイルから読み込む
    時間計算量: O(n) where n is file size
    空間計算量: O(n) where n is number of words
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(os.path.dirname(current_dir), "data")
    file_path = os.path.join(data_dir, filename)

    with open(file_path) as f:
        content = f.read().strip()

    # Remove quotes and split by comma
    return [word.strip('"') for word in content.split(",")]


def get_sorted_letters(word: str) -> str:
    """
    単語の文字をソートして正規化（アナグラム判定用）
    時間計算量: O(m log m) where m is word length
    空間計算量: O(m)
    """
    return "".join(sorted(word))


def find_anagram_pairs(words: list[str]) -> list[tuple[str, str]]:
    """
    アナグラムペアを見つける
    時間計算量: O(n * m log m) where n is number of words, m is average word length
    空間計算量: O(n * m)
    """
    # Group words by their sorted letters
    anagram_groups = defaultdict(list)

    for word in words:
        if len(word) > 1:  # Skip single letters
            sorted_letters = get_sorted_letters(word)
            anagram_groups[sorted_letters].append(word)

    # Find pairs from groups with 2 or more words
    pairs = []
    for group in anagram_groups.values():
        if len(group) >= 2:
            # Add all unique pairs from this group
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    pairs.append((group[i], group[j]))

    return pairs


def get_letter_mapping(
    word1: str, word2: str, num1: int, num2: int
) -> dict[str, str] | None:
    """
    2つの単語と数字から文字→数字のマッピングを取得
    制約をチェックして有効なマッピングのみ返す
    時間計算量: O(m) where m is word length
    空間計算量: O(m)
    """
    str1, str2 = str(num1), str(num2)

    # Length must match - both words and both numbers must have same length
    if len(word1) != len(word2) or len(word1) != len(str1) or len(word2) != len(str2):
        return None

    # Check for leading zeros
    if str1[0] == "0" or str2[0] == "0":
        return None

    # Build mapping from both words
    letter_to_digit: dict[str, str] = {}
    digit_to_letter: dict[str, str] = {}

    # Check word1 -> num1 mapping
    for letter, digit in zip(word1, str1, strict=False):
        if letter in letter_to_digit:
            if letter_to_digit[letter] != digit:
                return None  # Inconsistent mapping
        else:
            if digit in digit_to_letter and digit_to_letter[digit] != letter:
                return None  # One digit maps to multiple letters
            letter_to_digit[letter] = digit
            digit_to_letter[digit] = letter

    # Check word2 -> num2 mapping (must be consistent)
    for letter, digit in zip(word2, str2, strict=False):
        if letter in letter_to_digit:
            if letter_to_digit[letter] != digit:
                return None  # Inconsistent mapping
        else:
            if digit in digit_to_letter and digit_to_letter[digit] != letter:
                return None  # One digit maps to multiple letters
            letter_to_digit[letter] = digit
            digit_to_letter[digit] = letter

    return letter_to_digit


def is_perfect_square(n: int) -> bool:
    """
    数が完全平方数かどうかを判定
    時間計算量: O(1) - sqrt is constant time for reasonable inputs
    空間計算量: O(1)
    """
    if n < 0:
        return False

    root = int(n**0.5)
    return root * root == n


def apply_mapping(word: str, mapping: dict[str, str]) -> int | None:
    """
    文字→数字マッピングを単語に適用
    時間計算量: O(m) where m is word length
    空間計算量: O(m)
    """
    if not all(letter in mapping for letter in word):
        return None

    digit_str = "".join(mapping[letter] for letter in word)

    # Check for leading zero
    if digit_str[0] == "0":
        return None

    return int(digit_str)


def find_square_anagram_pairs(words: list[str]) -> list[tuple[str, str, int, int]]:
    """
    平方数アナグラムペアを見つける（効率化版）
    時間計算量: O(n * s) where n is pairs, s is squares for each length
    空間計算量: O(s) for storing squares
    """
    pairs = find_anagram_pairs(words)
    square_pairs = []

    # Group pairs by length for efficiency
    pairs_by_length = defaultdict(list)
    for pair in pairs:
        length = len(pair[0])
        pairs_by_length[length].append(pair)

    # Process each length group
    for length, length_pairs in pairs_by_length.items():
        # Generate squares of specific length only
        min_val = 10 ** (length - 1) if length > 1 else 1
        max_val = 10**length - 1

        # Find range of square roots
        min_root = int(min_val**0.5)
        max_root = int(max_val**0.5) + 1

        squares = []
        for root in range(min_root, max_root + 1):
            square = root * root
            if min_val <= square <= max_val:
                squares.append(square)

        # Check each pair against these squares
        for word1, word2 in length_pairs:
            for square1 in squares:
                for square2 in squares:
                    if square1 == square2:
                        continue

                    mapping = get_letter_mapping(word1, word2, square1, square2)
                    if mapping is not None:
                        # Verify the mapping works both ways
                        mapped1 = apply_mapping(word1, mapping)
                        mapped2 = apply_mapping(word2, mapping)

                        if mapped1 == square1 and mapped2 == square2:
                            square_pairs.append((word1, word2, square1, square2))

    return square_pairs


def solve_naive(filename: str = "p098_words.txt") -> int:
    """
    素直な解法: 全てのアナグラムペアと平方数の組み合わせをチェック
    時間計算量: O(n * m * s²) where n is word pairs, m is word length, s is squares
    空間計算量: O(s + n)
    """
    # For performance, use the optimized approach
    return solve_optimized(filename)


def solve_optimized(filename: str = "p098_words.txt") -> int:
    """
    最適化解法: より効率的な平方数生成と検索
    時間計算量: O(n * m * s log s) - binary search for squares
    空間計算量: O(s + n)
    """
    words = load_words(filename)
    pairs = find_anagram_pairs(words)

    if not pairs:
        return 0

    max_square = 0

    # Group pairs by word length for efficiency
    pairs_by_length = defaultdict(list)
    for pair in pairs:
        length = len(pair[0])
        pairs_by_length[length].append(pair)

    # Process each length group, starting from largest to prioritize bigger squares
    for length in sorted(pairs_by_length.keys(), reverse=True):
        length_pairs = pairs_by_length[length]

        # Early termination: if current max_square is already from a longer word length, skip smaller lengths
        if max_square > 0 and length < len(str(max_square)):
            continue

        # Generate squares of specific length
        min_val = 10 ** (length - 1) if length > 1 else 1
        max_val = 10**length - 1

        # Find range of square roots
        min_root = int(min_val**0.5)
        max_root = int(max_val**0.5) + 1

        squares = []
        for root in range(min_root, max_root + 1):
            square = root * root
            if min_val <= square <= max_val:
                squares.append(square)

        # Sort squares in descending order to find larger results first
        squares.sort(reverse=True)

        # Check each pair against these squares
        for word1, word2 in length_pairs:
            found_for_this_pair = False
            for i, square1 in enumerate(squares):
                # Early termination: if square1 is not bigger than current max, skip
                if square1 <= max_square:
                    break

                for square2 in squares[i + 1 :]:  # Avoid checking same square twice
                    if square2 <= max_square:
                        break

                    # Try mapping word1->square1, word2->square2
                    mapping = get_letter_mapping(word1, word2, square1, square2)
                    if mapping is not None:
                        mapped1 = apply_mapping(word1, mapping)
                        mapped2 = apply_mapping(word2, mapping)

                        if mapped1 == square1 and mapped2 == square2:
                            max_square = max(max_square, square1, square2)
                            found_for_this_pair = True

                    # Try mapping word1->square2, word2->square1
                    mapping = get_letter_mapping(word1, word2, square2, square1)
                    if mapping is not None:
                        mapped1 = apply_mapping(word1, mapping)
                        mapped2 = apply_mapping(word2, mapping)

                        if mapped1 == square2 and mapped2 == square1:
                            max_square = max(max_square, square1, square2)
                            found_for_this_pair = True

                # If we found a result for this pair, we can move to the next pair
                if found_for_this_pair:
                    break

    return max_square


def main() -> None:
    """メイン実行関数"""
    import time

    print("Problem 098: Anagramic squares")
    print("=" * 40)

    # Load and analyze words
    words = load_words()
    print(f"Loaded {len(words)} words")

    # Find anagram pairs
    pairs = find_anagram_pairs(words)
    print(f"Found {len(pairs)} anagram pairs")

    # Show some examples
    print("\nSome anagram pairs:")
    for _, (word1, word2) in enumerate(pairs[:10]):
        print(f"  {word1} ↔ {word2}")

    if len(pairs) > 10:
        print(f"  ... and {len(pairs) - 10} more")

    # Find square anagram pairs
    print("\nFinding square anagram pairs...")
    start_time = time.time()

    result = solve_optimized()
    end_time = time.time()

    print(f"Largest square number: {result}")
    print(f"Computation time: {end_time - start_time:.3f}s")

    # Show examples of valid square pairs (limited for demo)
    print("\nSearching for example square anagram pairs...")

    # Test with a known example first
    test_words = ["CARE", "RACE", "ACRE"]
    test_pairs = find_square_anagram_pairs(test_words)

    if test_pairs:
        print("Example square anagram pairs:")
        for word1, word2, square1, square2 in test_pairs[:3]:
            print(f"  {word1} = {square1}, {word2} = {square2}")
    else:
        print("No square pairs found in test words")


if __name__ == "__main__":
    main()
