"""
数列生成関数

Project Euler問題で使用される数列生成の共通関数を提供する。
"""

from collections.abc import Iterator


def generate_triangle(n: int) -> int:
    """
    n番目の三角数を計算

    Args:
        n: 三角数のインデックス（1から開始）

    Returns:
        n番目の三角数 T(n) = n(n+1)/2

    時間計算量: O(1)
    空間計算量: O(1)
    """
    return n * (n + 1) // 2


def generate_pentagonal(n: int) -> int:
    """
    n番目の五角数を計算

    Args:
        n: 五角数のインデックス（1から開始）

    Returns:
        n番目の五角数 P(n) = n(3n-1)/2

    時間計算量: O(1)
    空間計算量: O(1)
    """
    return n * (3 * n - 1) // 2


def generate_hexagonal(n: int) -> int:
    """
    n番目の六角数を計算

    Args:
        n: 六角数のインデックス（1から開始）

    Returns:
        n番目の六角数 H(n) = n(2n-1)

    時間計算量: O(1)
    空間計算量: O(1)
    """
    return n * (2 * n - 1)


def generate_octagonal(n: int) -> int:
    """
    n番目の八角数を計算

    Args:
        n: 八角数のインデックス（1から開始）

    Returns:
        n番目の八角数 O(n) = n(3n-2)

    時間計算量: O(1)
    空間計算量: O(1)
    """
    return n * (3 * n - 2)


def generate_square(n: int) -> int:
    """
    n番目の平方数を計算

    Args:
        n: 平方数のインデックス（1から開始）

    Returns:
        n番目の平方数 S(n) = n²

    時間計算量: O(1)
    空間計算量: O(1)
    """
    return n * n


def generate_heptagonal(n: int) -> int:
    """
    n番目の七角数を計算

    Args:
        n: 七角数のインデックス（1から開始）

    Returns:
        n番目の七角数 H(n) = n(5n-3)/2

    時間計算量: O(1)
    空間計算量: O(1)
    """
    return n * (5 * n - 3) // 2


def fibonacci_generator(limit: int | None = None) -> Iterator[int]:
    """
    フィボナッチ数列のジェネレータ

    Args:
        limit: 上限値（Noneの場合は無限）

    Yields:
        フィボナッチ数

    時間計算量: O(1) per iteration
    空間計算量: O(1)
    """
    a, b = 1, 1
    while limit is None or a <= limit:
        yield a
        a, b = b, a + b


def triangle_generator(limit: int | None = None) -> Iterator[int]:
    """
    三角数列のジェネレータ

    Args:
        limit: 上限値（Noneの場合は無限）

    Yields:
        三角数

    時間計算量: O(1) per iteration
    空間計算量: O(1)
    """
    n = 1
    while True:
        triangle = generate_triangle(n)
        if limit is not None and triangle > limit:
            break
        yield triangle
        n += 1


def pentagonal_generator(limit: int | None = None) -> Iterator[int]:
    """
    五角数列のジェネレータ

    Args:
        limit: 上限値（Noneの場合は無限）

    Yields:
        五角数

    時間計算量: O(1) per iteration
    空間計算量: O(1)
    """
    n = 1
    while True:
        pentagonal = generate_pentagonal(n)
        if limit is not None and pentagonal > limit:
            break
        yield pentagonal
        n += 1


def hexagonal_generator(limit: int | None = None) -> Iterator[int]:
    """
    六角数列のジェネレータ

    Args:
        limit: 上限値（Noneの場合は無限）

    Yields:
        六角数

    時間計算量: O(1) per iteration
    空間計算量: O(1)
    """
    n = 1
    while True:
        hexagonal = generate_hexagonal(n)
        if limit is not None and hexagonal > limit:
            break
        yield hexagonal
        n += 1


def is_triangle_number(x: int) -> bool:
    """
    指定された数が三角数かどうかを判定

    Args:
        x: 判定対象の数

    Returns:
        三角数の場合True、そうでなければFalse

    時間計算量: O(1)
    空間計算量: O(1)
    """
    if x < 1:
        return False

    # n(n+1)/2 = x から n を求める
    # n² + n - 2x = 0
    # n = (-1 + √(1 + 8x)) / 2
    import math

    discriminant = 1 + 8 * x
    sqrt_discriminant = int(math.sqrt(discriminant))

    # 判別式が完全平方数かつ、nが正の整数かチェック
    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return False

    n = (-1 + sqrt_discriminant) // 2
    return n * (n + 1) // 2 == x


def is_pentagonal_number(x: int) -> bool:
    """
    指定された数が五角数かどうかを判定

    Args:
        x: 判定対象の数

    Returns:
        五角数の場合True、そうでなければFalse

    時間計算量: O(1)
    空間計算量: O(1)
    """
    if x < 1:
        return False

    # n(3n-1)/2 = x から n を求める
    # 3n² - n - 2x = 0
    # n = (1 + √(1 + 24x)) / 6
    import math

    discriminant = 1 + 24 * x
    sqrt_discriminant = int(math.sqrt(discriminant))

    # 判別式が完全平方数かつ、nが正の整数かチェック
    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return False

    n = (1 + sqrt_discriminant) // 6
    return n * (3 * n - 1) // 2 == x


def is_hexagonal_number(x: int) -> bool:
    """
    指定された数が六角数かどうかを判定

    Args:
        x: 判定対象の数

    Returns:
        六角数の場合True、そうでなければFalse

    時間計算量: O(1)
    空間計算量: O(1)
    """
    if x < 1:
        return False

    # n(2n-1) = x から n を求める
    # 2n² - n - x = 0
    # n = (1 + √(1 + 8x)) / 4
    import math

    discriminant = 1 + 8 * x
    sqrt_discriminant = int(math.sqrt(discriminant))

    # 判別式が完全平方数かつ、nが正の整数かチェック
    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return False

    n = (1 + sqrt_discriminant) // 4
    return n * (2 * n - 1) == x
