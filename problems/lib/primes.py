"""
素数関連のユーティリティ関数

Project Euler問題で使用される素数関連の共通関数を提供する。
複数の問題で重複していた素数関数を統合。
"""

from typing import Literal, overload


def is_prime(n: int) -> bool:
    """
    素数判定関数

    Args:
        n: 判定対象の整数

    Returns:
        nが素数の場合True、そうでなければFalse

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


def is_prime_optimized(n: int) -> bool:
    """
    最適化された素数判定（6k±1の形を利用）

    Args:
        n: 判定対象の整数

    Returns:
        nが素数の場合True、そうでなければFalse

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


@overload
def sieve_of_eratosthenes(
    limit: int, return_type: Literal["list"] = "list"
) -> list[int]: ...


@overload
def sieve_of_eratosthenes(limit: int, return_type: Literal["set"]) -> set[int]: ...


@overload
def sieve_of_eratosthenes(
    limit: int, return_type: Literal["bool_array"]
) -> list[bool]: ...


def sieve_of_eratosthenes(
    limit: int, return_type: str = "list"
) -> list[int] | set[int] | list[bool]:
    """
    エラトステネスの篩で指定された範囲の素数を全て求める

    Args:
        limit: 上限値
        return_type: 戻り値の型 ('list', 'set', 'bool_array')

    Returns:
        return_type='list': 素数のリスト
        return_type='set': 素数の集合
        return_type='bool_array': 素数判定の真偽値配列

    時間計算量: O(n log log n)
    空間計算量: O(n)
    """
    if limit < 2:
        if return_type == "bool_array":
            return [False] * max(0, limit + 1)
        return [] if return_type == "list" else set()

    is_prime_array = [True] * (limit + 1)
    is_prime_array[0] = is_prime_array[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime_array[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_array[j] = False

    if return_type == "bool_array":
        return is_prime_array
    if return_type == "set":
        return {i for i in range(2, limit + 1) if is_prime_array[i]}
    # return_type == 'list'
    return [i for i in range(2, limit + 1) if is_prime_array[i]]


def generate_primes(limit: int) -> list[int]:
    """
    エラトステネスの篩で素数生成（sieve_of_eratosthenesのエイリアス）

    Args:
        limit: 上限値

    Returns:
        素数のリスト

    時間計算量: O(n log log n)
    空間計算量: O(n)
    """
    result = sieve_of_eratosthenes(limit, "list")
    assert isinstance(result, list)
    return result


def get_prime_factors(n: int) -> set[int]:
    """
    数値の素因数を取得

    Args:
        n: 素因数分解対象の整数

    Returns:
        素因数の集合

    時間計算量: O(√n)
    空間計算量: O(log n)
    """
    factors = set()
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1

    if n > 1:
        factors.add(n)

    return factors


def count_distinct_prime_factors(n: int) -> int:
    """
    数値の異なる素因数の個数を取得

    Args:
        n: 対象の整数

    Returns:
        異なる素因数の個数

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    count = 0
    d = 2

    while d * d <= n:
        if n % d == 0:
            count += 1
            while n % d == 0:
                n //= d
        d += 1

    if n > 1:
        count += 1

    return count


def is_truncatable_prime(n: int) -> bool:
    """
    左右両方向から切り取り可能な素数かどうかを判定

    Args:
        n: 判定対象の整数

    Returns:
        左右切り取り可能素数の場合True、そうでなければFalse

    時間計算量: O(d√n)、dは桁数
    空間計算量: O(d)
    """
    if not is_prime(n):
        return False

    # 一桁の素数は除外
    if n in (2, 3, 5, 7):
        return False

    s = str(n)

    # 左から切り取りチェック
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False

    # 右から切り取りチェック
    return all(is_prime(int(s[:i])) for i in range(len(s) - 1, 0, -1))
