#!/usr/bin/env python3
"""
Problem 036: Double-base palindromes

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

Answer: Project Euler公式サイトで確認してください
"""


def is_palindrome(s: str) -> bool:
    """
    文字列が回文かどうかをチェック
    時間計算量: O(n)
    空間計算量: O(1)
    """
    return s == s[::-1]


def solve_naive(limit: int = 1000000) -> int:
    """
    素直な解法: 全ての数をチェックして、10進と2進の両方で回文かどうか確認
    時間計算量: O(n * log n)
    空間計算量: O(log n)
    """
    total_sum = 0

    for num in range(1, limit):
        decimal_str = str(num)
        binary_str = bin(num)[2:]

        if is_palindrome(decimal_str) and is_palindrome(binary_str):
            total_sum += num

    return total_sum


def solve_optimized(limit: int = 1000000) -> int:
    """
    最適化解法: 10進の回文を生成してから2進回文かチェック
    時間計算量: O(√n * log n)
    空間計算量: O(log n)
    """
    total_sum = 0
    palindromes_found = set()

    # 1桁の回文
    for i in range(1, 10):
        if i < limit:
            binary_str = bin(i)[2:]
            if is_palindrome(binary_str):
                palindromes_found.add(i)
                total_sum += i

    # 2桁以上の回文を生成
    digits = 2
    while True:
        found_any = False

        # 偶数桁の回文
        half_digits = digits // 2
        start = 10 ** (half_digits - 1)
        end = 10**half_digits

        for i in range(start, end):
            s = str(i)
            palindrome_str = s + s[::-1]
            palindrome = int(palindrome_str)

            if palindrome >= limit:
                break

            if palindrome not in palindromes_found:
                found_any = True
                binary_str = bin(palindrome)[2:]
                if is_palindrome(binary_str):
                    palindromes_found.add(palindrome)
                    total_sum += palindrome

        # 奇数桁の回文
        half_digits = (digits - 1) // 2
        if half_digits >= 0:
            start = 10 ** (half_digits - 1) if half_digits > 0 else 0
            end = 10**half_digits if half_digits > 0 else 1

            for i in range(start, end):
                for middle in range(10):
                    s = str(i)
                    palindrome_str = s + str(middle) + s[::-1]
                    palindrome = int(palindrome_str)

                    if palindrome >= limit:
                        break

                    if palindrome not in palindromes_found:
                        found_any = True
                        binary_str = bin(palindrome)[2:]
                        if is_palindrome(binary_str):
                            palindromes_found.add(palindrome)
                            total_sum += palindrome

        if not found_any:
            break

        digits += 1

    return total_sum
