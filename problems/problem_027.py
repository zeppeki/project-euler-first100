#!/usr/bin/env python3
"""
Problem 027: Quadratic primes

Euler discovered the remarkable quadratic formula:
n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer
values 0 ≤ n ≤ 39. However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula n² - 79n + 1601 was discovered, which produces 80 primes
for the consecutive values 0 ≤ n ≤ 79. The product of the coefficients, -79 and 1601,
is -126479.

Considering quadratics of the form:
n² + an + b, where |a| < 1000 and |b| ≤ 1000

(where |n| is the modulus/absolute value of n)
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""


def is_prime(n: int) -> bool:
    """
    素数判定を行う
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


def sieve_of_eratosthenes(limit: int) -> set[int]:
    """
    エラトステネスの篩で指定した範囲の素数を生成
    時間計算量: O(n log log n)
    空間計算量: O(n)
    """
    if limit < 2:
        return set()

    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime_arr[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_arr[j] = False

    return {i for i in range(2, limit + 1) if is_prime_arr[i]}


def count_consecutive_primes(
    a: int, b: int, prime_set: set[int] | None = None, max_prime: int | None = None
) -> int:
    """
    n² + an + b で連続する素数の個数を数える
    時間計算量: O(k√m) ここで k は連続素数の個数、m は最大の値
    空間計算量: O(1)
    """
    n = 0
    while True:
        value = n * n + a * n + b
        if value < 2:
            break

        # 事前計算された素数セットがある場合はそれを使用
        if prime_set is not None and max_prime is not None:
            if value <= max_prime:
                if value not in prime_set:
                    break
            else:
                if not is_prime(value):
                    break
        else:
            if not is_prime(value):
                break

        n += 1

    return n


def solve_naive(limit: int = 1000) -> int:
    """
    素直な解法: 制約を絞り込んだ全探索
    時間計算量: O(p × limit × k)
    空間計算量: O(1)
    """
    max_primes = 0
    result_product = 0

    # b は n=0 で素数になる必要があるため、正の素数である必要がある
    # 小さな素数リストを事前計算
    b_candidates = [i for i in range(2, limit + 1) if is_prime(i)]

    for b in b_candidates:
        for a in range(-limit + 1, limit):
            # n=1の場合: 1 + a + b が正の数になる必要がある
            if 1 + a + b <= 1:
                continue

            primes_count = count_consecutive_primes(a, b)

            if primes_count > max_primes:
                max_primes = primes_count
                result_product = a * b

    return result_product


def solve_optimized(limit: int = 1000) -> int:
    """
    最適化解法: 素数を事前計算し、条件を絞り込む
    時間計算量: O(p × limit × k) ここで p は素数の個数
    空間計算量: O(n)
    """
    # 十分大きな範囲で素数を事前計算
    # 最大値の見積もりを保守的にする
    max_possible_value = 10000  # 実用的な範囲に制限
    prime_set = sieve_of_eratosthenes(max_possible_value)

    max_primes = 0
    result_product = 0

    # b は n=0 で素数になる必要があるため、正の素数である必要がある
    primes_up_to_limit = [p for p in prime_set if p <= limit]

    for b in primes_up_to_limit:
        for a in range(-limit + 1, limit):
            # n=1 の場合: 1 + a + b が正の数になる必要がある
            if 1 + a + b <= 1:
                continue

            primes_count = count_consecutive_primes(a, b, prime_set, max_possible_value)

            if primes_count > max_primes:
                max_primes = primes_count
                result_product = a * b

    return result_product
