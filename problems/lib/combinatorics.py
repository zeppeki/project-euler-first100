"""
組み合わせ・順列関数

Project Euler問題で使用される組み合わせ・順列計算の共通関数を提供する。
"""

import itertools
from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")


def combination_formula(n: int, r: int) -> int:
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


def permutation_formula(n: int, r: int) -> int:
    """
    順列の数を計算

    Args:
        n: 全体の要素数
        r: 選択する要素数

    Returns:
        P(n,r) = n! / (n-r)!

    時間計算量: O(r)
    空間計算量: O(1)
    """
    if r < 0 or r > n or n < 0:
        return 0
    if r == 0:
        return 1

    result = 1
    for i in range(n, n - r, -1):
        result *= i

    return result


def get_permutations(
    elements: list[T], r: int | None = None
) -> Iterator[tuple[T, ...]]:
    """
    要素の順列を生成

    Args:
        elements: 順列を生成する要素のリスト
        r: 選択する要素数（Noneの場合は全要素）

    Yields:
        順列のタプル

    時間計算量: O(P(n,r))
    空間計算量: O(r)
    """
    yield from itertools.permutations(elements, r)


def get_combinations(elements: list[T], r: int) -> Iterator[tuple[T, ...]]:
    """
    要素の組み合わせを生成

    Args:
        elements: 組み合わせを生成する要素のリスト
        r: 選択する要素数

    Yields:
        組み合わせのタプル

    時間計算量: O(C(n,r))
    空間計算量: O(r)
    """
    yield from itertools.combinations(elements, r)


def get_permutations_with_replacement(
    elements: list[T], r: int
) -> Iterator[tuple[T, ...]]:
    """
    重複を許可した順列を生成

    Args:
        elements: 順列を生成する要素のリスト
        r: 選択する要素数

    Yields:
        重複順列のタプル

    時間計算量: O(n^r)
    空間計算量: O(r)
    """
    yield from itertools.product(elements, repeat=r)


def get_combinations_with_replacement(
    elements: list[T], r: int
) -> Iterator[tuple[T, ...]]:
    """
    重複を許可した組み合わせを生成

    Args:
        elements: 組み合わせを生成する要素のリスト
        r: 選択する要素数

    Yields:
        重複組み合わせのタプル

    時間計算量: O(C(n+r-1,r))
    空間計算量: O(r)
    """
    yield from itertools.combinations_with_replacement(elements, r)


def multinomial_coefficient(*args: int) -> int:
    """
    多項係数を計算

    Args:
        *args: 各項の個数

    Returns:
        多項係数 n! / (k1! * k2! * ... * km!)

    時間計算量: O(n)
    空間計算量: O(1)
    """
    if not args:
        return 1  # Empty multinomial coefficient is 1
    if any(k < 0 for k in args):
        return 0

    n = sum(args)
    if n == 0:
        return 1

    result = 1
    curr_n = n

    for k in args:
        if k == 0:
            continue
        result *= combination_formula(curr_n, k)
        curr_n -= k

    return result
