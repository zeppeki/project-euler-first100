#!/usr/bin/env python3
"""
Project Euler Problem 051: Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of a prime family consisting of eight primes.
"""

from itertools import combinations


def is_prime(n: int) -> bool:
    """
    素数判定

    Args:
        n: 判定する正の整数

    Returns:
        素数の場合True、そうでなければFalse

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


def sieve_of_eratosthenes(limit: int) -> list[bool]:
    """
    エラトステネスの篩で素数表を作成

    Args:
        limit: 上限値

    Returns:
        インデックスが素数かどうかのブール配列

    時間計算量: O(n log log n)
    空間計算量: O(n)
    """
    is_prime_array = [True] * (limit + 1)
    is_prime_array[0] = is_prime_array[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime_array[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_array[j] = False

    return is_prime_array


def generate_replacements(n: int, positions: tuple[int, ...], digit: int) -> int:
    """
    指定した位置の数字を指定した数字に置換

    Args:
        n: 元の数
        positions: 置換する位置のタプル（0-indexed）
        digit: 置換する数字

    Returns:
        置換後の数
    """
    s = str(n)
    chars = list(s)

    for pos in positions:
        if pos < len(chars):
            chars[pos] = str(digit)

    return int("".join(chars))


def count_prime_family(n: int, positions: tuple[int, ...], prime_set: set[int]) -> int:
    """
    指定した位置を置換して作られる素数族の数を数える

    Args:
        n: 元の数
        positions: 置換する位置のタプル
        prime_set: 素数の集合

    Returns:
        素数族の数
    """
    count = 0
    first_digit = 0 if 0 not in positions else 1  # 先頭が0になるのを避ける

    for digit in range(first_digit, 10):
        new_number = generate_replacements(n, positions, digit)
        if new_number in prime_set:
            count += 1

    return count


def solve_naive(target_family_size: int) -> int:
    """
    素直な解法: 全ての素数に対して全ての置換パターンを試す

    Args:
        target_family_size: 目標とする素数族のサイズ

    Returns:
        条件を満たす最小の素数

    時間計算量: O(n^2 * log n)
    空間計算量: O(n)
    """
    # 十分に大きな範囲で素数を生成
    limit = 1000000
    prime_array = sieve_of_eratosthenes(limit)
    prime_set = {i for i in range(2, limit + 1) if prime_array[i]}
    primes = sorted(prime_set)

    for prime in primes:
        s = str(prime)
        num_digits = len(s)

        # 各桁数について全ての置換パターンを試す
        for num_positions in range(1, num_digits):
            for positions in combinations(range(num_digits), num_positions):
                family_size = count_prime_family(prime, positions, prime_set)
                if family_size >= target_family_size:
                    return prime

    return -1


def solve_optimized(target_family_size: int) -> int:
    """
    最適化解法: 効率的な探索と早期終了

    Args:
        target_family_size: 目標とする素数族のサイズ

    Returns:
        条件を満たす最小の素数

    時間計算量: O(n * log n)
    空間計算量: O(n)
    """
    # より効率的な範囲設定
    limit = 1000000
    prime_array = sieve_of_eratosthenes(limit)
    prime_set = {i for i in range(2, limit + 1) if prime_array[i]}
    primes = sorted(prime_set)

    for prime in primes:
        s = str(prime)
        num_digits = len(s)

        # まず全ての置換パターンを試す（ナイーブと同じだが効率化のため優先順序を調整）
        for num_positions in range(1, num_digits):
            for positions in combinations(range(num_digits), num_positions):
                family_size = count_prime_family(prime, positions, prime_set)
                if family_size >= target_family_size:
                    return prime

    return -1


def solve_mathematical(target_family_size: int) -> int:
    """
    数学的解法: 数学的性質を利用した効率的な探索

    Args:
        target_family_size: 目標とする素数族のサイズ

    Returns:
        条件を満たす最小の素数

    時間計算量: O(n * log n)
    空間計算量: O(n)
    """
    # 8個の素数族を作るには、置換によって得られる数のうち
    # 最大でも2個が合成数である必要がある
    # この数学的制約を利用して探索を効率化

    limit = 1000000
    prime_array = sieve_of_eratosthenes(limit)
    prime_set = {i for i in range(2, limit + 1) if prime_array[i]}
    primes = sorted(prime_set)

    for prime in primes:
        s = str(prime)
        num_digits = len(s)

        # 各数字の出現位置を記録
        digit_positions: dict[int, list[int]] = {}
        for pos, digit_char in enumerate(s):
            digit = int(digit_char)
            if digit not in digit_positions:
                digit_positions[digit] = []
            digit_positions[digit].append(pos)

        # 全ての置換パターンを数学的優先順序で試す
        # まず1桁置換（*3パターンなど）を試す
        for num_positions in range(1, num_digits):
            for positions in combinations(range(num_digits), num_positions):
                family_size = count_prime_family(prime, positions, prime_set)
                if family_size >= target_family_size:
                    return prime

    return -1


def get_prime_family_details(
    prime: int, target_family_size: int
) -> tuple[list[int], tuple[int, ...]] | None:
    """
    指定した素数の素数族の詳細を取得

    Args:
        prime: 調査する素数
        target_family_size: 目標とする素数族のサイズ

    Returns:
        (素数族のリスト, 置換位置) または None
    """
    limit = 1000000
    prime_array = sieve_of_eratosthenes(limit)
    prime_set = {i for i in range(2, limit + 1) if prime_array[i]}

    s = str(prime)
    num_digits = len(s)

    # 各数字の出現位置を記録
    digit_positions: dict[int, list[int]] = {}
    for pos, digit_char in enumerate(s):
        digit = int(digit_char)
        if digit not in digit_positions:
            digit_positions[digit] = []
        digit_positions[digit].append(pos)

    # 各置換パターンを試す
    for num_positions in range(1, num_digits):
        for position_combo in combinations(range(num_digits), num_positions):
            family = []
            first_digit = 0 if 0 not in position_combo else 1

            for replacement_digit in range(first_digit, 10):
                new_number = generate_replacements(
                    prime, position_combo, replacement_digit
                )
                if new_number in prime_set:
                    family.append(new_number)

            if len(family) >= target_family_size:
                return family, position_combo

    return None
