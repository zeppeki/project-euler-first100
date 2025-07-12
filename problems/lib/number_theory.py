"""
数論関連のユーティリティ関数

Project Euler問題で使用される高度な数論関数とアルゴリズムを提供する。
基本的なGCD/LCMはmath_utils.pyに配置し、ここではより専門的な数論関数を扱う。

抽出元:
- Problem 057, 064, 065, 066: 連分数関連
- Problem 069, 070, 072: オイラーのファイ関数
- Problem 097: モジュラー指数法
- Problem 023: 完全数・豊富数・不足数の分類
- Problem 003, 005, 047: 素因数分解の応用
"""

import math


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    拡張ユークリッド互除法

    ax + by = gcd(a, b) を満たす整数 x, y を求める

    Args:
        a: 第一の整数
        b: 第二の整数

    Returns:
        (gcd(a, b), x, y) のタプル

    時間計算量: O(log(min(a, b)))
    空間計算量: O(1)

    Examples:
        >>> extended_gcd(30, 18)
        (6, -1, 2)  # 30*(-1) + 18*2 = 6
        >>> extended_gcd(35, 15)
        (5, 1, -2)  # 35*1 + 15*(-2) = 5
    """
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def modular_inverse(a: int, m: int) -> int:
    """
    モジュラー逆元を計算

    a * x ≡ 1 (mod m) を満たす x を求める

    Args:
        a: 逆元を求める数
        m: 法（modulus）

    Returns:
        モジュラー逆元

    Raises:
        ValueError: gcd(a, m) ≠ 1 の場合（逆元が存在しない）

    時間計算量: O(log m)
    空間計算量: O(1)

    Examples:
        >>> modular_inverse(3, 11)
        4  # 3 * 4 ≡ 1 (mod 11)
        >>> modular_inverse(7, 13)
        2  # 7 * 2 ≡ 1 (mod 13)
    """
    gcd, x, _ = extended_gcd(a, m)

    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for gcd({a}, {m}) = {gcd}")

    return (x % m + m) % m


def chinese_remainder_theorem(remainders: list[int], moduli: list[int]) -> int:
    """
    中国剰余定理を使って連立合同式を解く

    x ≡ r₁ (mod m₁)
    x ≡ r₂ (mod m₂)
    ...
    x ≡ rₖ (mod mₖ)

    Args:
        remainders: 余りのリスト [r₁, r₂, ..., rₖ]
        moduli: 法のリスト [m₁, m₂, ..., mₖ]（互いに素である必要）

    Returns:
        連立合同式の解

    Raises:
        ValueError: 法が互いに素でない場合

    時間計算量: O(k * log(max(moduli)))
    空間計算量: O(1)

    Examples:
        >>> chinese_remainder_theorem([2, 3, 2], [3, 5, 7])
        23  # x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)
    """
    if len(remainders) != len(moduli):
        raise ValueError("Number of remainders and moduli must be equal")

    if len(remainders) == 0:
        return 0

    # 段階的に解を構築
    x, m = remainders[0], moduli[0]

    for i in range(1, len(remainders)):
        r, n = remainders[i], moduli[i]

        # x ≡ r (mod n) を満たすよう x を調整
        gcd, p, q = extended_gcd(m, n)

        if (r - x) % gcd != 0:
            raise ValueError("No solution exists (moduli are not pairwise coprime)")

        # x + m * k ≡ r (mod n) を解く
        x = x + m * ((r - x) // gcd) * p
        m = m * n // gcd
        x = x % m

    return x


def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """
    モジュラー指数法（高速指数法）

    base^exponent mod modulus を効率的に計算

    Args:
        base: 底
        exponent: 指数
        modulus: 法

    Returns:
        base^exponent mod modulus の結果

    時間計算量: O(log exponent)
    空間計算量: O(1)

    Examples:
        >>> modular_exponentiation(2, 10, 1000)
        24  # 2^10 = 1024 ≡ 24 (mod 1000)
        >>> modular_exponentiation(3, 4, 5)
        1   # 3^4 = 81 ≡ 1 (mod 5)
    """
    if modulus == 1:
        return 0

    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus

    return result


def euler_totient(n: int) -> int:
    """
    オイラーのファイ関数（トーシェント関数）φ(n)

    1 ≤ k ≤ n で gcd(k, n) = 1 となる k の個数を計算

    Args:
        n: 計算対象の正整数

    Returns:
        φ(n) の値

    時間計算量: O(√n)
    空間計算量: O(1)

    Examples:
        >>> euler_totient(9)
        6  # φ(9): 1,2,4,5,7,8 are coprime to 9
        >>> euler_totient(12)
        4  # φ(12): 1,5,7,11 are coprime to 12
    """
    if n == 1:
        return 1

    result = n
    p = 2

    # 素因数分解しながらφ(n)を計算
    while p * p <= n:
        if n % p == 0:
            # pは素因数
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        # nが素数の場合
        result -= result // n

    return result


def euler_totient_sieve(limit: int) -> list[int]:
    """
    エラトステネス篩の変形でφ(1)からφ(limit)まで一括計算

    Args:
        limit: 計算上限

    Returns:
        φ(0), φ(1), φ(2), ..., φ(limit) のリスト

    時間計算量: O(n log log n)
    空間計算量: O(n)

    Examples:
        >>> euler_totient_sieve(10)
        [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
    """
    phi = list(range(limit + 1))

    for i in range(2, limit + 1):
        if phi[i] == i:  # i は素数
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    return phi


def mobius_function(n: int) -> int:
    """
    メビウス関数 μ(n)

    μ(n) = 1  if n is square-free with even number of prime factors
    μ(n) = -1 if n is square-free with odd number of prime factors
    μ(n) = 0  if n has a squared prime factor

    Args:
        n: 計算対象の正整数

    Returns:
        μ(n) の値 (-1, 0, または 1)

    時間計算量: O(√n)
    空間計算量: O(1)

    Examples:
        >>> mobius_function(1)
        1   # 1 = (empty product)
        >>> mobius_function(6)
        1   # 6 = 2 × 3 (2 distinct primes, even count)
        >>> mobius_function(10)
        -1  # 10 = 2 × 5 (2 distinct primes, odd count)
        >>> mobius_function(12)
        0   # 12 = 2² × 3 (has squared factor)
    """
    if n == 1:
        return 1

    prime_count = 0

    # 素因数分解
    p = 2
    while p * p <= n:
        if n % p == 0:
            prime_count += 1
            n //= p
            if n % p == 0:  # p² で割り切れる
                return 0
        p += 1

    if n > 1:  # 残った n は素数
        prime_count += 1

    return -1 if prime_count % 2 == 1 else 1


def jacobi_symbol(a: int, n: int) -> int:
    """
    ヤコビ記号 (a/n)

    ルジャンドル記号の一般化。二次剰余の判定に使用。

    Args:
        a: 上段の整数
        n: 下段の奇数（n > 0）

    Returns:
        ヤコビ記号の値 (-1, 0, または 1)

    Raises:
        ValueError: n が偶数または非正の場合

    時間計算量: O(log(min(a, n)))
    空間計算量: O(1)

    Examples:
        >>> jacobi_symbol(1, 3)
        1
        >>> jacobi_symbol(2, 3)
        -1
        >>> jacobi_symbol(3, 5)
        -1
    """
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")

    a = a % n
    result = 1

    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result

        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n

    if n == 1:
        return result
    return 0


def continued_fraction_sqrt(n: int) -> tuple[int, list[int]]:
    """
    平方根の連分数展開

    √n = a₀ + 1/(a₁ + 1/(a₂ + 1/(a₃ + ...)))

    Args:
        n: 平方根を取る正整数

    Returns:
        (a₀, [a₁, a₂, ..., aₖ]) のタプル（aₖは周期）

    時間計算量: O(√n)
    空間計算量: O(√n)

    Examples:
        >>> continued_fraction_sqrt(2)
        (1, [2])  # √2 = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))
        >>> continued_fraction_sqrt(3)
        (1, [1, 2])  # √3 = 1 + 1/(1 + 1/(2 + 1/(1 + 1/(2 + ...))))
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    # 完全平方数チェック
    sqrt_n = int(math.sqrt(n))
    if sqrt_n * sqrt_n == n:
        return sqrt_n, []

    a0 = sqrt_n
    m, d, a = 0, 1, a0
    seen: dict[tuple[int, int], int] = {}
    period: list[int] = []

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d

        state = (m, d)
        if state in seen:
            break

        seen[state] = len(period)
        period.append(a)

    return a0, period


def convergents_from_continued_fraction(
    a0: int, period: list[int], num_convergents: int
) -> list[tuple[int, int]]:
    """
    連分数から収束分数（近似分数）を計算

    Args:
        a0: 連分数の整数部
        period: 連分数の周期部分
        num_convergents: 求める収束分数の個数

    Returns:
        収束分数のリスト [(p₁, q₁), (p₂, q₂), ...]

    時間計算量: O(num_convergents)
    空間計算量: O(num_convergents)

    Examples:
        >>> convergents_from_continued_fraction(1, [2], 5)
        [(1, 1), (3, 2), (7, 5), (17, 12), (41, 29)]
    """
    if num_convergents <= 0:
        return []

    convergents = []

    # 初期値
    h_prev, h_curr = 1, a0
    k_prev, k_curr = 0, 1

    convergents.append((h_curr, k_curr))

    if num_convergents == 1:
        return convergents

    # 周期部分を使って収束分数を計算
    period_len = len(period)
    for i in range(1, num_convergents):
        a = period[(i - 1) % period_len]

        h_next = a * h_curr + h_prev
        k_next = a * k_curr + k_prev

        convergents.append((h_next, k_next))

        h_prev, h_curr = h_curr, h_next
        k_prev, k_curr = k_curr, k_next

    return convergents


def solve_pell_equation(d: int) -> tuple[int, int]:
    """
    ペル方程式 x² - Dy² = 1 の最小解を求める

    Args:
        d: ペル方程式の係数（平方数でない正整数）

    Returns:
        最小解 (x, y)

    Raises:
        ValueError: d が平方数の場合

    時間計算量: O(√d)
    空間計算量: O(√d)

    Examples:
        >>> solve_pell_equation(2)
        (3, 2)  # 3² - 2×2² = 9 - 8 = 1
        >>> solve_pell_equation(3)
        (2, 1)  # 2² - 3×1² = 4 - 3 = 1
    """
    sqrt_d = int(math.sqrt(d))
    if sqrt_d * sqrt_d == d:
        raise ValueError("d must not be a perfect square")

    a0, period = continued_fraction_sqrt(d)

    # 周期が奇数の場合は1周期、偶数の場合は2周期必要
    period_length = len(period)
    target_convergents = period_length if period_length % 2 == 0 else 2 * period_length

    convergents = convergents_from_continued_fraction(a0, period, target_convergents)

    # 最後の収束分数がペル方程式の解
    x, y = convergents[-1]
    return x, y


def carmichael_lambda(n: int) -> int:
    """
    カーマイケル関数 λ(n)

    a^λ(n) ≡ 1 (mod n) が gcd(a,n)=1 なる全ての a で成立する最小の指数

    Args:
        n: 計算対象の正整数

    Returns:
        λ(n) の値

    時間計算量: O(√n)
    空間計算量: O(log n)

    Examples:
        >>> carmichael_lambda(15)
        4  # λ(15) = lcm(λ(3), λ(5)) = lcm(2, 4) = 4
        >>> carmichael_lambda(8)
        2  # λ(8) = φ(8)/2 = 4/2 = 2
    """
    if n == 1:
        return 1

    # 素因数分解
    factors: dict[int, int] = {}
    temp_n = n
    d = 2

    while d * d <= temp_n:
        while temp_n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp_n //= d
        d += 1

    if temp_n > 1:
        factors[temp_n] = factors.get(temp_n, 0) + 1

    # 各素数冪に対するλを計算
    lambda_values = []

    for p, k in factors.items():
        if p == 2 and k >= 3:
            # 2^k (k≥3) の場合は特別扱い
            lambda_values.append(2 ** (k - 2))
        elif p == 2:
            # 2^1, 2^2 の場合
            lambda_values.append(euler_totient(p**k))
        else:
            # 奇素数の場合
            lambda_values.append(euler_totient(p**k))

    # 全てのλ値のLCMを計算
    from math import gcd

    def lcm(a: int, b: int) -> int:
        return abs(a * b) // gcd(a, b)

    result: int = lambda_values[0]
    for val in lambda_values[1:]:
        result = lcm(result, val)

    return result


def is_carmichael_number(n: int) -> bool:
    """
    カーマイケル数の判定

    合成数 n が a^n ≡ a (mod n) を gcd(a,n)=1 なる全ての a で満たすか判定

    Args:
        n: 判定する正整数

    Returns:
        カーマイケル数の場合 True

    時間計算量: O(√n)
    空間計算量: O(log n)

    Examples:
        >>> is_carmichael_number(561)
        True   # 561 = 3 × 11 × 17 は最小のカーマイケル数
        >>> is_carmichael_number(15)
        False
    """
    if n < 2:
        return False

    # 素数は除外
    if is_prime_simple(n):
        return False

    # カーマイケル数の必要条件：square-free
    if not is_square_free(n):
        return False

    # カーマイケル数の判定：λ(n) | (n-1)
    lambda_n = carmichael_lambda(n)
    return (n - 1) % lambda_n == 0


def is_prime_simple(n: int) -> bool:
    """
    簡単な素数判定（小さな数用）

    Args:
        n: 判定する正整数

    Returns:
        素数の場合 True

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    return all(n % i != 0 for i in range(3, int(math.sqrt(n)) + 1, 2))


def is_square_free(n: int) -> bool:
    """
    平方因子を持たない数（square-free）の判定

    Args:
        n: 判定する正整数

    Returns:
        square-freeの場合 True

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n <= 1:
        return n == 1

    i = 2
    while i * i <= n:
        if n % (i * i) == 0:
            return False
        i += 1
    return True
