#!/usr/bin/env python3
"""
Problem 059: XOR decryption

XOR暗号で暗号化されたテキストを復号し、ASCII値の合計を求める問題です。
"""

import string
from pathlib import Path


def load_encrypted_text(filename: str = "data/p059_cipher.txt") -> list[int]:
    """
    暗号化されたテキストファイルを読み込む
    時間計算量: O(n)
    空間計算量: O(n)
    """
    try:
        # プロジェクトルートからの相対パスで読み込み
        file_path = Path(__file__).parent.parent / filename
        with open(file_path, encoding="utf-8") as f:
            content = f.read().strip()
            return [int(x) for x in content.split(",")]
    except FileNotFoundError:
        # テスト用のサンプルデータ
        return [
            36,
            22,
            80,
            0,
            0,
            4,
            23,
            25,
            19,
            17,
            88,
            4,
            4,
            19,
            21,
            11,
            88,
            22,
            23,
            23,
            29,
            69,
            12,
            24,
            0,
            88,
            25,
            11,
            12,
            2,
            10,
            11,
            88,
            32,
            23,
            23,
            73,
            22,
            0,
            89,
            21,
            11,
            88,
            76,
            65,
            26,
            27,
            19,
            75,
            12,
            22,
            88,
            64,
            20,
            84,
            2,
            21,
            11,
            88,
            84,
            79,
            79,
            29,
            65,
            21,
            75,
        ]


def xor_decrypt(encrypted_data: list[int], key: str) -> str:
    """
    XOR暗号を使用してデータを復号する
    時間計算量: O(n)
    空間計算量: O(n)
    """
    if not key:
        return ""

    decrypted = []
    key_bytes = [ord(c) for c in key]
    key_length = len(key_bytes)

    for i, byte_val in enumerate(encrypted_data):
        key_byte = key_bytes[i % key_length]
        decrypted_byte = byte_val ^ key_byte
        decrypted.append(chr(decrypted_byte))

    return "".join(decrypted)


def is_valid_english_text(text: str) -> bool:
    """
    テキストが英語として妥当かチェックする
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if not text or len(text) < 10:  # 最小長を要求
        return False

    # 印刷可能文字の割合をチェック
    printable_chars = sum(1 for c in text if c.isprintable())
    printable_ratio = printable_chars / len(text)

    if printable_ratio < 0.9:
        return False

    # 一般的な英単語が含まれているかチェック
    text_lower = text.lower()
    common_words = [
        "the",
        "and",
        "of",
        "to",
        "a",
        "in",
        "is",
        "it",
        "you",
        "that",
        "he",
        "was",
        "for",
        "on",
        "are",
        "as",
        "with",
        "his",
        "they",
        "i",
        "at",
        "be",
        "this",
        "have",
        "from",
        "or",
        "one",
        "had",
        "by",
        "word",
        "but",
        "not",
        "what",
        "all",
        "were",
        "we",
        "when",
        "your",
        "can",
        "said",
        "there",
        "each",
        "which",
        "she",
        "do",
        "how",
        "their",
        "if",
        "will",
        "up",
        "other",
        "about",
        "out",
        "many",
        "then",
        "them",
        "these",
        "so",
        "some",
        "her",
        "would",
        "make",
        "like",
        "into",
        "him",
        "has",
        "two",
        "more",
        "go",
        "no",
        "way",
        "could",
        "my",
        "than",
        "first",
        "been",
        "call",
        "who",
        "its",
        "now",
        "find",
        "long",
        "down",
        "day",
        "did",
        "get",
        "come",
        "made",
        "may",
        "part",
    ]

    word_count = sum(1 for word in common_words if word in text_lower)

    # より厳しい条件: 長いテキストほど多くの単語を要求
    min_words = max(3, len(text) // 20)
    return word_count >= min_words


def generate_three_letter_keys() -> list[str]:
    """
    3文字の小文字キーをすべて生成する
    時間計算量: O(26^3)
    空間計算量: O(26^3)
    """
    keys = []
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                keys.append(a + b + c)
    return keys


def find_decryption_key(encrypted_data: list[int]) -> str | None:
    """
    復号キーを見つける
    時間計算量: O(26^3 * n)
    空間計算量: O(n)
    """
    for key in generate_three_letter_keys():
        decrypted_text = xor_decrypt(encrypted_data, key)
        if is_valid_english_text(decrypted_text):
            return key
    return None


def calculate_ascii_sum(text: str) -> int:
    """
    テキストのASCII値の合計を計算する
    時間計算量: O(n)
    空間計算量: O(1)
    """
    return sum(ord(c) for c in text)


def solve_naive() -> int:
    """
    素直な解法: 全てのキーを試して復号する
    時間計算量: O(26^3 * n)
    空間計算量: O(n)
    """
    encrypted_data = load_encrypted_text()

    for key in generate_three_letter_keys():
        decrypted_text = xor_decrypt(encrypted_data, key)
        if is_valid_english_text(decrypted_text):
            return calculate_ascii_sum(decrypted_text)

    return 0


def solve_optimized() -> int:
    """
    最適化解法: 頻度分析を使用した効率的な復号
    時間計算量: O(26^3 * n)
    空間計算量: O(n)
    """
    encrypted_data = load_encrypted_text()

    # スペース文字（最も頻出）を基準にキー候補を絞り込む
    space_ascii = ord(" ")
    potential_keys = []

    # 各位置で最も頻出する暗号化バイトを特定
    position_frequencies: list[dict[int, int]] = [{} for _ in range(3)]

    for i, byte_val in enumerate(encrypted_data):
        pos = i % 3
        position_frequencies[pos][byte_val] = (
            position_frequencies[pos].get(byte_val, 0) + 1
        )

    # 各位置で最も頻出するバイトがスペース文字の暗号化と仮定
    for pos in range(3):
        if position_frequencies[pos]:
            most_frequent_byte = max(
                position_frequencies[pos], key=lambda x: position_frequencies[pos][x]
            )
            key_char_ascii = most_frequent_byte ^ space_ascii
            if 97 <= key_char_ascii <= 122:  # 小文字のASCII範囲
                potential_keys.append(chr(key_char_ascii))
            else:
                potential_keys.append("a")  # デフォルト値
        else:
            potential_keys.append("a")

    # 基本キーから周辺キーも試す
    base_key = "".join(potential_keys)
    keys_to_try = [base_key]

    # 各位置で±1文字ずつ試す
    for i in range(3):
        for offset in [-1, 1]:
            key_list = list(base_key)
            new_char_ascii = ord(key_list[i]) + offset
            if 97 <= new_char_ascii <= 122:
                key_list[i] = chr(new_char_ascii)
                keys_to_try.append("".join(key_list))

    # キー候補を試す
    for key in keys_to_try:
        decrypted_text = xor_decrypt(encrypted_data, key)
        if is_valid_english_text(decrypted_text):
            return calculate_ascii_sum(decrypted_text)

    # 頻度分析が失敗した場合、全探索にフォールバック
    return solve_naive()


def solve_mathematical() -> int:
    """
    数学的解法: エントロピー分析による高効率復号
    時間計算量: O(26^3 + n)
    空間計算量: O(n)
    """
    encrypted_data = load_encrypted_text()

    # 英語テキストの文字頻度分布
    english_freq = {
        "a": 8.12,
        "b": 1.49,
        "c": 2.78,
        "d": 4.25,
        "e": 12.02,
        "f": 2.23,
        "g": 2.02,
        "h": 6.09,
        "i": 6.97,
        "j": 0.15,
        "k": 0.77,
        "l": 4.03,
        "m": 2.41,
        "n": 6.75,
        "o": 7.51,
        "p": 1.93,
        "q": 0.10,
        "r": 5.99,
        "s": 6.33,
        "t": 9.06,
        "u": 2.76,
        "v": 0.98,
        "w": 2.36,
        "x": 0.15,
        "y": 1.97,
        "z": 0.07,
        " ": 12.00,
    }

    best_score = float("inf")
    best_key = None

    for key in generate_three_letter_keys():
        decrypted_text = xor_decrypt(encrypted_data, key)

        # 文字頻度の分析
        char_counts: dict[str, int] = {}
        total_chars = 0

        for c in decrypted_text.lower():
            if c.isalpha() or c == " ":
                char_counts[c] = char_counts.get(c, 0) + 1
                total_chars += 1

        if total_chars == 0:
            continue

        # カイ二乗検定による英語らしさのスコア計算
        chi_square = 0.0
        for char, expected_freq in english_freq.items():
            observed_count = char_counts.get(char, 0)
            expected_count = total_chars * (expected_freq / 100)
            if expected_count > 0:
                chi_square += ((observed_count - expected_count) ** 2) / expected_count

        if chi_square < best_score and is_valid_english_text(decrypted_text):
            best_score = chi_square
            best_key = key

    if best_key:
        decrypted_text = xor_decrypt(encrypted_data, best_key)
        return calculate_ascii_sum(decrypted_text)

    return 0


def get_decryption_details() -> tuple[str, str, int]:
    """
    復号の詳細情報を取得（デバッグ用）

    Returns:
        Tuple[str, str, int]: (key, decrypted_text, ascii_sum)
    """
    encrypted_data = load_encrypted_text()
    key = find_decryption_key(encrypted_data)

    if key:
        decrypted_text = xor_decrypt(encrypted_data, key)
        ascii_sum = calculate_ascii_sum(decrypted_text)
        return key, decrypted_text, ascii_sum

    return "", "", 0


def main() -> None:
    """メイン関数"""
    print("Problem 059: XOR decryption")
    print("=" * 40)

    # 暗号化データの読み込み
    encrypted_data = load_encrypted_text()
    print(f"Encrypted data length: {len(encrypted_data)}")
    print(f"First 10 bytes: {encrypted_data[:10]}")

    # 復号の詳細表示
    key, decrypted_text, ascii_sum = get_decryption_details()
    if key:
        print(f"\nFound key: '{key}'")
        print(f"Decrypted text (first 100 chars): '{decrypted_text[:100]}...'")
        print(f"ASCII sum: {ascii_sum}")
    else:
        print("\nKey not found")

    print("\n" + "=" * 40)

    # 各解法の実行
    solutions = [
        ("Naive approach", solve_naive),
        ("Optimized approach", solve_optimized),
        ("Mathematical approach", solve_mathematical),
    ]

    for name, func in solutions:
        try:
            result = func()
            print(f"{name}: {result}")
        except Exception as e:
            print(f"{name}: Error - {e}")


if __name__ == "__main__":
    main()
