#!/usr/bin/env python3
"""
Problem 037: Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right
and from right to left.

NOTE: 2, 3, 5 and 7 are not considered to be truncatable primes.

Answer: Project Euler公式サイトで確認してください
"""

from problems.lib.primes import is_prime


def is_truncatable_prime(n: int) -> bool:
    """
    左右両方向から梅切り可能な素数かどうかを判定
    時間計算量: O(d * √n) where d is number of digits
    空間計算量: O(1)
    """
    if not is_prime(n):
        return False

    # 2, 3, 5, 7は除外
    if n in (2, 3, 5, 7):
        return False

    s = str(n)

    # 左から梅切りチェック (3797 -> 797 -> 97 -> 7)
    for i in range(1, len(s)):
        truncated = int(s[i:])
        if not is_prime(truncated):
            return False

    # 右から梅切りチェック (3797 -> 379 -> 37 -> 3)
    for i in range(len(s) - 1, 0, -1):
        truncated = int(s[:i])
        if not is_prime(truncated):
            return False

    return True


def solve_naive() -> int:
    """
    素直な解法: 素数を順番にチェックして梅切り素数を探す
    時間計算量: O(n * d * √n)
    空間計算量: O(1)
    """
    truncatable_primes: list[int] = []
    candidate = 11  # 2, 3, 5, 7を除外して最初の二桁数から開始

    while len(truncatable_primes) < 11:
        if is_truncatable_prime(candidate):
            truncatable_primes.append(candidate)
        candidate += 2  # 偶数をスキップ

    return sum(truncatable_primes)


def solve_optimized() -> int:
    """
    最適化解法: 特定の数字パターンを持つ数だけをチェック
    時間計算量: O(k * d * √k) where k is candidates
    空間計算量: O(1)
    """
    truncatable_primes: list[int] = []

    # 梅切り素数は特定の数字で始まり終わる必要がある
    # 左端: 2,3,5,7 (素数)
    # 右端: 3,7 (偶数で終わると左から梅切りで偶数になる)
    # 中間: 1,3,7,9 (他の数字だと梅切りで素数でなくなる)

    # 2桁数から開始
    for length in range(2, 8):  # 理論上最大6桁まで
        if len(truncatable_primes) >= 11:
            break

        # 特定のパターンで数を生成
        if length == 2:
            # 23, 37, 53, 73など
            for first in [2, 3, 5, 7]:
                for last in [3, 7]:
                    if first != last:  # 同じ数字は除外
                        candidate = first * 10 + last
                        if is_truncatable_prime(candidate):
                            truncatable_primes.append(candidate)
        else:
            # 3桁以上: 特定パターンで生成
            import itertools

            for first in [2, 3, 5, 7]:
                for last in [3, 7]:
                    for middle_digits in itertools.product(
                        [1, 3, 7, 9], repeat=length - 2
                    ):
                        candidate_str = (
                            str(first) + "".join(map(str, middle_digits)) + str(last)
                        )
                        candidate = int(candidate_str)
                        if is_truncatable_prime(candidate):
                            truncatable_primes.append(candidate)

    # ソートして最初の11個を取る
    truncatable_primes.sort()
    return sum(truncatable_primes[:11])
