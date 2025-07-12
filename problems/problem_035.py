#!/usr/bin/env python3
"""
Problem 035: Circular primes

円順列素数は、その数の桁をすべて循環させても素数となる数のことです。
例えば、197は円順列素数です。なぜなら197、971、719はすべて素数だからです。

100未満の円順列素数は13個あります: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97

問題: 100万未満の円順列素数は何個ありますか？

Answer: 55
"""

from problems.lib.primes import is_prime, sieve_of_eratosthenes


def solve_naive(limit: int = 1000000) -> int:
    """
    素直な解法: 各数について全ての回転をチェック
    時間計算量: O(n * log(n) * sqrt(n)) - 各数の回転と素数判定
    空間計算量: O(1)
    """

    def get_rotations(n: int) -> list[int]:
        """数の全ての回転を取得"""
        s = str(n)
        rotations = []
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            rotations.append(int(rotated))
        return rotations

    def is_circular_prime(n: int) -> bool:
        """円順列素数かどうか判定"""
        if not is_prime(n):
            return False

        rotations = get_rotations(n)
        return all(is_prime(rotation) for rotation in rotations)

    count = 0
    for n in range(2, limit):
        if is_circular_prime(n):
            count += 1

    return count


def solve_optimized(limit: int = 1000000) -> int:
    """
    最適化解法: エラトステネスの篩を使い、処理済み数をマーク
    時間計算量: O(n log log n) - 篩の生成が支配的
    空間計算量: O(n) - 篩とチェック済みセット
    """

    def get_rotations(n: int) -> list[int]:
        """数の全ての回転を取得"""
        s = str(n)
        rotations = []
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            rotations.append(int(rotated))
        return rotations

    # 篩を十分大きなサイズで生成（最大の回転を考慮）
    # 最悪の場合、6桁の数 (999999) の回転も6桁なので limit で十分
    max_possible = max(limit, 10 ** len(str(limit - 1)))
    primes_list = sieve_of_eratosthenes(max_possible, "bool_array")
    is_prime = primes_list

    # 処理済みの数を記録
    checked = set()
    circular_primes = set()

    for n in range(2, limit):
        if n in checked or not is_prime[n]:
            continue

        # 回転を取得
        rotations = get_rotations(n)

        # 全ての回転が素数かチェック
        all_prime = True
        for rotation in rotations:
            if rotation >= max_possible or not is_prime[rotation]:
                all_prime = False
                break

        # 処理済みとしてマーク
        for rotation in rotations:
            if rotation < limit:
                checked.add(rotation)

        # 円順列素数の場合、全ての回転を追加
        if all_prime:
            for rotation in rotations:
                if rotation < limit:
                    circular_primes.add(rotation)

    return len(circular_primes)
