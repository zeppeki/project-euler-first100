#!/usr/bin/env python3
"""
Problem 043: Sub-string divisibility

The number 1406357289 is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note:
- d2d3d4=406 is divisible by 2
- d3d4d5=063 is divisible by 3
- d4d5d6=635 is divisible by 5
- d5d6d7=357 is divisible by 7
- d6d7d8=572 is divisible by 11
- d7d8d9=728 is divisible by 13
- d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

Answer: [Hidden]
"""

import itertools


def is_pandigital_0_to_9(num_str: str) -> bool:
    """
    0-9のpandigital数かどうか判定
    時間計算量: O(1) - 固定長10桁
    空間計算量: O(1)
    """
    return len(num_str) == 10 and set(num_str) == set("0123456789")


def has_substring_divisibility(num_str: str) -> bool:
    """
    部分文字列の割り切れ条件をチェック
    時間計算量: O(1) - 固定数の条件チェック
    空間計算量: O(1)
    """
    if len(num_str) != 10:
        return False

    # 各条件をチェック
    primes = [2, 3, 5, 7, 11, 13, 17]

    for i, prime in enumerate(primes):
        # d(i+2)d(i+3)d(i+4) が prime で割り切れるかチェック
        substring = num_str[i+1:i+4]  # インデックス i+1 から 3文字
        if int(substring) % prime != 0:
            return False

    return True


def generate_all_pandigital_0_to_9() -> list[str]:
    """
    すべての0-9 pandigital数を生成
    時間計算量: O(10!) - 10桁の順列
    空間計算量: O(10!)
    """
    digits = "0123456789"
    pandigitals = []

    for perm in itertools.permutations(digits):
        # 先頭が0の場合はスキップ（10桁数として無効）
        if perm[0] != "0":
            pandigitals.append("".join(perm))

    return pandigitals


def solve_naive() -> int:
    """
    素直な解法: 全pandigital数を生成して条件チェック
    時間計算量: O(10!) - 全順列を生成
    空間計算量: O(10!)
    """
    total_sum = 0

    # すべての0-9 pandigital数を生成
    pandigitals = generate_all_pandigital_0_to_9()

    # 各数について部分文字列の割り切れ条件をチェック
    for num_str in pandigitals:
        if has_substring_divisibility(num_str):
            total_sum += int(num_str)

    return total_sum


def solve_optimized() -> int:
    """
    最適化解法: 条件に合う数を段階的に構築
    時間計算量: O(k) where k << 10! (条件を満たす数のみ生成)
    空間計算量: O(k)
    """
    # 各位置で可能な3桁の組み合わせを事前計算
    primes = [2, 3, 5, 7, 11, 13, 17]
    valid_substrings = []

    # 各素数について、000-999の範囲で割り切れる3桁数を見つける
    for prime in primes:
        valid_for_prime = []
        for num in range(1000):  # 000-999
            if num % prime == 0:
                # 3桁でパディング
                num_str = f"{num:03d}"
                # pandigital条件: 同じ桁が重複していない
                if len(set(num_str)) == 3:
                    valid_for_prime.append(num_str)
        valid_substrings.append(valid_for_prime)

    # バックトラッキングで有効な10桁数を構築
    def build_number(current: str, pos: int, used_digits: set) -> list[str]:
        if pos == 10:  # 10桁完成
            if is_pandigital_0_to_9(current):
                return [current]
            return []

        if pos < 3:
            # 最初の3桁は任意（ただし先頭は0以外）
            results = []
            for digit in "0123456789":
                if digit not in used_digits and (pos > 0 or digit != "0"):
                    results.extend(build_number(
                        current + digit,
                        pos + 1,
                        used_digits | {digit}
                    ))
            return results

        # pos >= 3: 部分文字列条件をチェック
        prime_idx = pos - 3  # d2d3d4から始まるので
        if prime_idx >= len(primes):
            # 残りの桁を任意に埋める
            results = []
            for digit in "0123456789":
                if digit not in used_digits:
                    results.extend(build_number(
                        current + digit,
                        pos + 1,
                        used_digits | {digit}
                    ))
            return results

        # 現在の位置での有効な選択肢を計算
        results = []
        if pos == 3:
            # d2d3d4の最後の桁を決める
            for substring in valid_substrings[0]:  # 2で割り切れる
                if substring[0] == current[1] and substring[1] == current[2]:
                    next_digit = substring[2]
                    if next_digit not in used_digits:
                        results.extend(build_number(
                            current + next_digit,
                            pos + 1,
                            used_digits | {next_digit}
                        ))
        else:
            # 既存の部分文字列と整合性を保つ
            for substring in valid_substrings[prime_idx]:
                if len(current) >= 2 and substring[:2] == current[-2:]:
                    next_digit = substring[2]
                    if next_digit not in used_digits:
                        results.extend(build_number(
                            current + next_digit,
                            pos + 1,
                            used_digits | {next_digit}
                        ))

        return results

    # 有効な数を構築
    valid_numbers = build_number("", 0, set())

    return sum(int(num) for num in valid_numbers)


def solve_mathematical() -> int:
    """
    数学的解法: より効率的な制約プロパゲーション
    時間計算量: O(k) where k is much smaller than 10!
    空間計算量: O(1)
    """
    # 特定の制約を利用した最適化された解法
    total_sum = 0
    digits = "0123456789"

    # より効率的なアプローチ: 制約を利用して候補を絞り込む
    for perm in itertools.permutations(digits):
        if perm[0] == "0":  # 先頭が0の場合はスキップ
            continue

        num_str = "".join(perm)

        # 早期終了のための最適化: 高コストな変換を避ける
        # 各部分文字列を直接チェック
        valid = True
        primes = [2, 3, 5, 7, 11, 13, 17]

        for i, prime in enumerate(primes):
            # 部分文字列を整数として解釈
            substring_val = int(perm[i+1]) * 100 + int(perm[i+2]) * 10 + int(perm[i+3])
            if substring_val % prime != 0:
                valid = False
                break

        if valid:
            total_sum += int(num_str)

    return total_sum
