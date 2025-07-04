"""
数学ユーティリティ関数

Project Euler問題で使用される数学的計算の共通関数を提供する。
重複していた数学関数を統合。
"""

import math
from collections import defaultdict


def gcd(a: int, b: int) -> int:
    """
    最大公約数を求める（ユークリッドの互除法）

    Args:
        a: 第一の整数
        b: 第二の整数

    Returns:
        aとbの最大公約数

    時間計算量: O(log(min(a, b)))
    空間計算量: O(1)
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    最小公倍数の計算

    Args:
        a: 第一の整数
        b: 第二の整数

    Returns:
        aとbの最小公倍数

    時間計算量: O(log(min(a, b)))
    空間計算量: O(1)
    """
    return abs(a * b) // gcd(a, b)


def factorial(n: int) -> int:
    """
    階乗を計算

    Args:
        n: 非負整数

    Returns:
        nの階乗

    Raises:
        ValueError: nが負の場合

    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_builtin(n: int) -> int:
    """
    標準ライブラリを使用した階乗計算（高速版）

    Args:
        n: 非負整数

    Returns:
        nの階乗

    時間計算量: O(1) - math.factorialを使用
    空間計算量: O(1)
    """
    return math.factorial(n)


def combination(n: int, r: int) -> int:
    """
    組み合わせの数を効率的に計算（オーバーフローを避ける）

    Args:
        n: 全体の要素数
        r: 選択する要素数

    Returns:
        C(n,r) = n! / (r! * (n-r)!)

    時間計算量: O(min(r, n-r))
    空間計算量: O(1)
    """
    if r < 0 or r > n or n < 0:
        return 0
    if r == 0 or r == n:
        return 1

    # C(n,r) = C(n,n-r) なので、計算量を減らすため小さい方を使用
    r = min(r, n - r)

    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)

    return result


def prime_factorization(n: int) -> dict[int, int]:
    """
    素因数分解を行い、各素因数の指数を返す

    Args:
        n: 素因数分解する整数

    Returns:
        素因数をキー、指数を値とする辞書

    時間計算量: O(√n)
    空間計算量: O(log n)
    """
    factors: defaultdict[int, int] = defaultdict(int)

    if n <= 1:
        return dict(factors)

    # 2で割り切れる回数を数える
    while n % 2 == 0:
        factors[2] += 1
        n //= 2

    # 3以上の奇数で割り切れる回数を数える
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors[factor] += 1
            n //= factor
        factor += 2

    # 残りが1より大きい場合、それも素因数
    if n > 1:
        factors[n] += 1

    return dict(factors)


def get_divisors(n: int) -> list[int]:
    """
    指定された数の約数をすべて取得

    Args:
        n: 約数を求める整数

    Returns:
        nのすべての約数のソート済みリスト

    時間計算量: O(√n)
    空間計算量: O(d(n))、d(n)は約数の個数
    """
    if n <= 0:
        return []

    divisors = []
    sqrt_n = int(math.sqrt(n))

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return sorted(divisors)


def count_divisors(n: int) -> int:
    """
    素因数分解を使用して約数の個数を効率的に計算

    Args:
        n: 約数の個数を求める整数

    Returns:
        nの約数の個数

    時間計算量: O(√n)
    空間計算量: O(log n)
    """
    if n <= 0:
        return 0

    factors = prime_factorization(n)
    divisor_count = 1

    for exponent in factors.values():
        divisor_count *= exponent + 1

    return divisor_count


def get_proper_divisors_sum(n: int) -> int:
    """
    nの真の約数（nを除く約数）の和を計算

    Args:
        n: 真の約数の和を求める整数

    Returns:
        nの真の約数の和

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n <= 1:
        return 0

    divisor_sum = 1  # 1は常に真の約数
    i = 2

    while i * i <= n:
        if n % i == 0:
            divisor_sum += i
            # i != n//iの場合のみ、n//iも追加
            if i != n // i:
                divisor_sum += n // i
        i += 1

    return divisor_sum


def is_abundant(n: int) -> bool:
    """
    nが過剰数かどうかを判定

    Args:
        n: 判定対象の整数

    Returns:
        nが過剰数の場合True、そうでなければFalse

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    return get_proper_divisors_sum(n) > n


def is_palindrome(n: int | str) -> bool:
    """
    数値または文字列が回文かどうかを判定

    Args:
        n: 判定対象の数値または文字列

    Returns:
        回文の場合True、そうでなければFalse

    時間計算量: O(d)、dは桁数
    空間計算量: O(d)
    """
    s = str(n)
    return s == s[::-1]


def fibonacci(n: int) -> int:
    """
    n番目のフィボナッチ数を計算

    Args:
        n: フィボナッチ数列のインデックス（1から開始）

    Returns:
        n番目のフィボナッチ数

    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def get_triangular_number(n: int) -> int:
    """
    n番目の三角数を計算

    Args:
        n: 三角数のインデックス

    Returns:
        n番目の三角数

    時間計算量: O(1)
    空間計算量: O(1)
    """
    return n * (n + 1) // 2


def get_pentagonal_number(n: int) -> int:
    """
    n番目の五角数を計算

    Args:
        n: 五角数のインデックス

    Returns:
        n番目の五角数

    時間計算量: O(1)
    空間計算量: O(1)
    """
    return n * (3 * n - 1) // 2


def get_hexagonal_number(n: int) -> int:
    """
    n番目の六角数を計算

    Args:
        n: 六角数のインデックス

    Returns:
        n番目の六角数

    時間計算量: O(1)
    空間計算量: O(1)
    """
    return n * (2 * n - 1)
