"""
Problem 77: Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:
7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""


def generate_primes(limit: int) -> list[int]:
    """
    エラトステネスの篩を使用して素数を生成

    Args:
        limit: 素数を生成する上限

    Returns:
        limit以下の素数のリスト
    """
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(2, limit + 1) if sieve[i]]


def count_prime_partitions(n: int, primes: list[int]) -> int:
    """
    nを素数の和で表す方法の数を計算

    Args:
        n: 分割する数
        primes: 使用可能な素数のリスト

    Returns:
        素数の和で表す方法の数
    """
    # dp[i] = iを素数の和で表す方法の数
    dp = [0] * (n + 1)
    dp[0] = 1  # 0は空の和で表せる

    # 各素数を使って和を作る
    for prime in primes:
        if prime > n:
            break
        for i in range(prime, n + 1):
            dp[i] += dp[i - prime]

    return dp[n]


def solve_naive(target: int) -> int:
    """
    素直な解法: 各数について素数分割の数を計算

    Args:
        target: 目標となる分割方法の数

    Returns:
        target以上の分割方法を持つ最初の数

    時間計算量: O(n² × p) where p is the number of primes
    空間計算量: O(n)
    """
    # まず適当な上限で試す
    max_n = 100
    primes = generate_primes(max_n)

    for n in range(2, max_n + 1):
        # nより大きい素数は使えないので、必要な素数のみ使用
        usable_primes = [p for p in primes if p <= n]
        ways = count_prime_partitions(n, usable_primes)

        if ways > target:
            return n

    # 見つからない場合はエラー
    raise ValueError(f"Solution not found within limit {max_n}")


def solve_optimized(target: int) -> int:
    """
    最適化解法: 素数リストを事前に生成し、動的計画法を効率化

    Args:
        target: 目標となる分割方法の数

    Returns:
        target以上の分割方法を持つ最初の数

    時間計算量: O(n × p) where p is the number of primes up to n
    空間計算量: O(n)
    """
    # 素数を事前に生成（十分な数まで）
    max_n = 100
    primes = generate_primes(max_n)

    # 各数について分割数を計算していく
    # dp[i] = iを素数の和で表す方法の数
    dp = [0] * (max_n + 1)
    dp[0] = 1

    # 素数を順に追加していく
    for prime in primes:
        for i in range(prime, max_n + 1):
            dp[i] += dp[i - prime]

    # target以上の分割方法を持つ最初の数を探す
    for n in range(2, max_n + 1):
        if dp[n] > target:
            return n

    raise ValueError(f"Solution not found within limit {max_n}")
