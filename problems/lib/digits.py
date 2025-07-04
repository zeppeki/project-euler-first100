"""
数字・文字列処理関数

Project Euler問題で使用される数字・文字列処理の共通関数を提供する。
重複していた数字処理関数を統合。
"""

from itertools import permutations


def get_digit_signature(n: int) -> str:
    """
    数の桁を並び替えたシグネチャを返す

    Args:
        n: 正の整数

    Returns:
        各桁をソートした文字列

    時間計算量: O(d log d) where d is number of digits
    空間計算量: O(d)
    """
    return "".join(sorted(str(n)))


def get_digit_signature_tuple(n: int) -> tuple[int, ...]:
    """
    数値の各桁の出現回数を取得

    Args:
        n: 正の整数

    Returns:
        各桁(0-9)の出現回数のタプル

    時間計算量: O(log n)
    空間計算量: O(1)
    """
    if n == 0:
        return (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    digits = [0] * 10
    while n > 0:
        digits[n % 10] += 1
        n //= 10
    return tuple(digits)


def is_pandigital(n: int | str, start: int = 1, end: int | None = None) -> bool:
    """
    パンデジタル数かどうかを判定

    Args:
        n: 判定対象の数値または文字列
        start: 開始桁（デフォルト: 1）
        end: 終了桁（Noneの場合は文字列長に応じて自動設定）

    Returns:
        パンデジタル数の場合True、そうでなければFalse

    時間計算量: O(d) where d is number of digits
    空間計算量: O(d)
    """
    s = str(n)

    if end is None:
        if start == 0:
            end = len(s) - 1
        else:
            end = len(s)

    expected_length = end - start + 1
    if len(s) != expected_length:
        return False

    expected = {str(i) for i in range(start, end + 1)}
    actual = set(s)
    return expected == actual


def is_pandigital_1_to_9(digits_str: str) -> bool:
    """
    1から9のパンデジタル数かどうか判定

    Args:
        digits_str: 判定対象の文字列

    Returns:
        1-9パンデジタル数の場合True、そうでなければFalse

    時間計算量: O(1) - 最大9文字の固定長
    空間計算量: O(1)
    """
    return is_pandigital(digits_str, 1, 9)


def is_pandigital_0_to_9(digits_str: str) -> bool:
    """
    0から9のパンデジタル数かどうか判定

    Args:
        digits_str: 判定対象の文字列

    Returns:
        0-9パンデジタル数の場合True、そうでなければFalse

    時間計算量: O(1) - 固定長10桁
    空間計算量: O(1)
    """
    return is_pandigital(digits_str, 0, 9)


def is_palindrome(n: int | str) -> bool:
    """
    数値または文字列が回文かどうかを判定

    Args:
        n: 判定対象の数値または文字列

    Returns:
        回文の場合True、そうでなければFalse

    時間計算量: O(d) where d is number of digits
    空間計算量: O(d)
    """
    s = str(n)
    return s == s[::-1]


def reverse_number(n: int) -> int:
    """
    数値を逆転させる

    Args:
        n: 逆転対象の整数

    Returns:
        逆転した数値

    時間計算量: O(log n)
    空間計算量: O(log n)
    """
    return int(str(n)[::-1])


def get_rotations(n: int) -> list[int]:
    """
    数の全ての回転を取得

    Args:
        n: 回転対象の整数

    Returns:
        全ての回転数のリスト

    時間計算量: O(d^2) where d is number of digits
    空間計算量: O(d^2)
    """
    s = str(n)
    rotations = []
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        rotations.append(int(rotated))
    return rotations


def get_permutations_4digit(n: int) -> list[int]:
    """
    4桁数のすべての順列を返す

    Args:
        n: 4桁の整数

    Returns:
        有効な4桁数の順列のソート済みリスト

    時間計算量: O(d!)
    空間計算量: O(d!)
    """
    digits = str(n)
    perms = set()

    for perm in permutations(digits):
        # 先頭が0でない4桁の数のみ
        if perm[0] != "0" and len(perm) == 4:
            num = int("".join(perm))
            if 1000 <= num <= 9999:  # 4桁の数のみ
                perms.add(num)

    return sorted(perms)


def are_permutations(n1: int, n2: int) -> bool:
    """
    2つの数が同じ桁の順列かチェック

    Args:
        n1: 最初の数
        n2: 2番目の数

    Returns:
        同じ桁の順列の場合True、そうでなければFalse

    時間計算量: O(log max(n1, n2))
    空間計算量: O(log max(n1, n2))
    """
    return get_digit_signature(n1) == get_digit_signature(n2)


def digit_factorial_sum(number: int) -> int:
    """
    数字の各桁の階乗の和を計算

    Args:
        number: 対象の整数

    Returns:
        各桁の階乗の和

    時間計算量: O(log n) - 数字の桁数に比例
    空間計算量: O(1)
    """
    from .math_utils import factorial

    if number == 0:
        return factorial(0)  # 0! = 1

    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10
    return total


def digit_power_sum(number: int, power: int) -> int:
    """
    数字の各桁のべき乗の和を計算

    Args:
        number: 対象の整数
        power: べき乗の指数

    Returns:
        各桁のべき乗の和

    時間計算量: O(log n)
    空間計算量: O(1)
    """
    return sum(int(digit) ** power for digit in str(number))


def concatenated_product(base: int, n: int) -> str:
    """
    基数と1,2,...,nの積を連結した文字列を生成

    Args:
        base: 基数
        n: 乗数の上限

    Returns:
        連結された積の文字列

    時間計算量: O(n * log(base * n))
    空間計算量: O(n * log(base * n))
    """
    result = ""
    for i in range(1, n + 1):
        result += str(base * i)
    return result


def get_digit_at_position(pos: int) -> int:
    """
    連続する自然数列（123456789101112...）の指定位置の桁を取得

    Args:
        pos: 位置（1から開始）

    Returns:
        その位置の桁

    時間計算量: O(log pos)
    空間計算量: O(log pos)
    """
    if pos <= 9:
        return pos

    length = 1
    count = 9
    start = 1

    while pos > length * count:
        pos -= length * count
        length += 1
        count *= 10
        start *= 10

    number = start + (pos - 1) // length
    digit_index = (pos - 1) % length

    return int(str(number)[digit_index])


def has_substring_divisibility(num_str: str, primes: list[int] | None = None) -> bool:
    """
    部分文字列の割り切れ条件をチェック（Problem 043用）

    Args:
        num_str: 10桁の数字文字列
        primes: チェックする素数のリスト（デフォルト: [2,3,5,7,11,13,17]）

    Returns:
        すべての条件を満たす場合True、そうでなければFalse

    時間計算量: O(1) - 固定数の条件チェック
    空間計算量: O(1)
    """
    if len(num_str) != 10:
        return False

    if primes is None:
        primes = [2, 3, 5, 7, 11, 13, 17]

    # 各条件をチェック
    for i, prime in enumerate(primes):
        # d(i+2)d(i+3)d(i+4) が prime で割り切れるかチェック
        substring = num_str[i + 1 : i + 4]  # インデックス i+1 から 3文字
        if int(substring) % prime != 0:
            return False

    return True


def is_circular_prime_candidate(n: int) -> bool:
    """
    循環素数の候補かどうかをチェック（0,2,4,5,6,8を含まないか）

    Args:
        n: 判定対象の整数

    Returns:
        循環素数の候補の場合True、そうでなければFalse

    時間計算量: O(log n)
    空間計算量: O(1)
    """
    if n < 10:
        return n in (2, 3, 5, 7)

    # 0,2,4,5,6,8を含む場合は循環素数になれない
    s = str(n)
    forbidden = {"0", "2", "4", "5", "6", "8"}
    return not any(digit in forbidden for digit in s)


def count_digits(n: int) -> int:
    """
    整数の桁数を数える

    Args:
        n: 対象の整数

    Returns:
        桁数

    時間計算量: O(log n)
    空間計算量: O(1)
    """
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        count += 1
        n //= 10
    return count


def sum_of_digits(n: int) -> int:
    """
    整数の各桁の和を計算

    Args:
        n: 対象の整数

    Returns:
        各桁の和

    時間計算量: O(log n)
    空間計算量: O(1)
    """
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total
