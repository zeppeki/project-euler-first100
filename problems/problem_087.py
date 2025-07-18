"""
Project Euler Problem 87: Prime power triples
============================================

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2² + 2³ + 2⁴
33 = 3² + 2³ + 2⁴
49 = 5² + 2³ + 2⁴
47 = 2² + 3³ + 2⁴

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

import math

from problems.lib.primes import sieve_of_eratosthenes


def solve_naive(limit: int = 50000000) -> int:
    """
    素直な解法: 全ての素数の組み合わせを試して、条件を満たす数を数える。

    時間計算量: O(p³) where p は素数の個数
    空間計算量: O(limit)

    Args:
        limit: 上限値（デフォルト: 50,000,000）

    Returns:
        limit未満で、素数の平方 + 素数の立方 + 素数の4乗で表せる数の個数
    """
    # 必要な素数を計算
    # 最大の素数は sqrt(limit) 以下
    max_prime_squared = int(math.sqrt(limit))
    max_prime_cubed = int(limit ** (1 / 3))
    max_prime_fourth = int(limit ** (1 / 4))

    # 素数を生成
    primes = sieve_of_eratosthenes(max_prime_squared)

    # 各べき乗で必要な素数をフィルタリング
    primes_squared = [p for p in primes if p <= max_prime_squared]
    primes_cubed = [p for p in primes if p <= max_prime_cubed]
    primes_fourth = [p for p in primes if p <= max_prime_fourth]

    # 条件を満たす数を集める
    numbers = set()

    for p2 in primes_squared:
        square = p2 * p2
        if square >= limit:
            break

        for p3 in primes_cubed:
            cube = p3 * p3 * p3
            if square + cube >= limit:
                break

            for p4 in primes_fourth:
                fourth = p4 * p4 * p4 * p4
                total = square + cube + fourth

                if total < limit:
                    numbers.add(total)
                else:
                    break

    return len(numbers)


def solve_optimized(limit: int = 50000000) -> int:
    """
    最適化解法: 素数の生成を最小限にし、早期終了を活用。

    時間計算量: O(p³) where p は素数の個数
    空間計算量: O(n) where n は結果の数

    Args:
        limit: 上限値

    Returns:
        limit未満で、素数の平方 + 素数の立方 + 素数の4乗で表せる数の個数
    """
    # 必要な最大素数を計算
    max_prime = int(math.sqrt(limit))
    primes = sieve_of_eratosthenes(max_prime)

    # 条件を満たす数を格納するセット
    prime_power_triples = set()

    # 素数の4乗から開始（最も制約が厳しい）
    for p4 in primes:
        fourth = p4**4
        if fourth >= limit:
            break

        # 素数の立方
        for p3 in primes:
            cube = p3**3
            if fourth + cube >= limit:
                break

            # 素数の平方
            for p2 in primes:
                square = p2**2
                total = square + cube + fourth

                if total < limit:
                    prime_power_triples.add(total)
                else:
                    break

    return len(prime_power_triples)


def solve_mathematical(limit: int = 50000000) -> int:
    """
    数学的解法: 事前計算でべき乗を保存し、効率的に組み合わせを生成。

    時間計算量: O(p²² + p³³ + p⁴⁴ + p² × p³ × p⁴)
    空間計算量: O(p² + p³ + p⁴ + n)

    Args:
        limit: 上限値

    Returns:
        limit未満で、素数の平方 + 素数の立方 + 素数の4乗で表せる数の個数
    """
    # エッジケース
    if limit <= 28:  # 最小の素数べき乗三項は 2² + 2³ + 2⁴ = 28
        return 0

    # 各べき乗の最大素数を計算
    max_p2 = int(math.sqrt(limit - 2**3 - 2**4))  # 最小のcubeとfourthを考慮
    max_p3 = int((limit - 2**2 - 2**4) ** (1 / 3))  # 最小のsquareとfourthを考慮
    max_p4 = int((limit - 2**2 - 2**3) ** (1 / 4))  # 最小のsquareとcubeを考慮

    # 十分な素数を生成
    max_prime = max(max_p2, max_p3, max_p4)
    primes = sieve_of_eratosthenes(max_prime)

    # 各べき乗を事前計算
    squares = []
    cubes = []
    fourths = []

    for p in primes:
        if p <= max_p2:
            squares.append(p * p)
        if p <= max_p3:
            cubes.append(p * p * p)
        if p <= max_p4:
            fourths.append(p * p * p * p)

    # 全ての組み合わせを試す
    prime_power_triples = set()

    for fourth in fourths:
        if fourth >= limit:
            break

        for cube in cubes:
            if fourth + cube >= limit:
                break

            for square in squares:
                total = square + cube + fourth
                if total < limit:
                    prime_power_triples.add(total)
                else:
                    break

    return len(prime_power_triples)
