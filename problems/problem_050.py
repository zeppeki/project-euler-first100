#!/usr/bin/env python3
"""
Problem 050: Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The prime 953 can be written as the sum of twenty-one consecutive primes.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from problems.lib.primes import sieve_of_eratosthenes


def solve_naive(limit: int = 1000000) -> int:
    """
    素直な解法: 全ての連続する素数の和を計算して素数判定
    時間計算量: O(n² × √max_sum)
    空間計算量: O(n)

    全ての可能な連続する素数の組み合わせを生成し、
    その和が素数かどうかを確認する。
    """
    primes = sieve_of_eratosthenes(limit)
    prime_set = set(primes)

    max_length = 0
    result_prime = 0

    # 各開始位置から連続する素数の和を計算
    for start in range(len(primes)):
        current_sum = 0

        for end in range(start, len(primes)):
            current_sum += primes[end]

            # 上限を超えたら終了
            if current_sum >= limit:
                break

            # 連続する素数の数
            length = end - start + 1

            # 和が素数で、より長い連続和が見つかった場合
            if current_sum in prime_set and length > max_length:
                max_length = length
                result_prime = current_sum

    return result_prime


def solve_optimized(limit: int = 1000000) -> int:
    """
    最適化解法: 累積和を使用して計算効率を向上
    時間計算量: O(n²)
    空間計算量: O(n)

    累積和を事前計算することで、連続する素数の和を
    O(1)で計算できるように最適化。
    """
    primes = sieve_of_eratosthenes(limit)
    prime_set = set(primes)

    # 累積和を事前計算
    cumulative_sum = [0]
    for prime in primes:
        cumulative_sum.append(cumulative_sum[-1] + prime)

    max_length = 0
    result_prime = 0

    # 各開始位置から連続する素数の和を計算
    for start in range(len(primes)):
        for end in range(start, len(primes)):
            # 累積和を使用してO(1)で和を計算
            current_sum = cumulative_sum[end + 1] - cumulative_sum[start]

            # 上限を超えたら終了
            if current_sum >= limit:
                break

            # 連続する素数の数
            length = end - start + 1

            # 和が素数で、より長い連続和が見つかった場合
            if current_sum in prime_set and length > max_length:
                max_length = length
                result_prime = current_sum

    return result_prime


def solve_mathematical(limit: int = 1000000) -> int:
    """
    数学的解法: 最大長の探索範囲を数学的に制限
    時間計算量: O(n²)
    空間計算量: O(n)

    数学的洞察:
    - 最小の素数から始まる連続和が最も長くなる可能性が高い
    - 和がlimitに近づくにつれて、連続する数も少なくなる
    - 長い連続和から短い連続和へ優先的に探索することで効率化
    """
    primes = sieve_of_eratosthenes(limit)
    prime_set = set(primes)

    # 累積和を事前計算
    cumulative_sum = [0]
    for prime in primes:
        cumulative_sum.append(cumulative_sum[-1] + prime)

    max_length = 0
    result_prime = 0

    # 効率化: 最大可能長を制限（最初の素数から始まる和がlimitを超えない範囲）
    max_possible_length = 0
    for i in range(len(primes)):
        if cumulative_sum[i + 1] >= limit:
            max_possible_length = i
            break
    else:
        max_possible_length = len(primes)

    # 連続する素数の長さを降順で探索
    for length in range(min(max_possible_length, 1000), 0, -1):
        found = False

        # 各開始位置で指定した長さの連続和を計算
        for start in range(len(primes) - length + 1):
            end = start + length - 1
            current_sum = cumulative_sum[end + 1] - cumulative_sum[start]

            # 上限を超えたら次の開始位置へ
            if current_sum >= limit:
                continue

            # 和が素数で、より長い連続和が見つかった場合
            if current_sum in prime_set and length > max_length:
                max_length = length
                result_prime = current_sum
                found = True
                break

        # この長さで見つかった場合、これが最大長なので終了
        if found:
            break

    return result_prime
