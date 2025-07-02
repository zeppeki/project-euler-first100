#!/usr/bin/env python3
"""
Problem 048: Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Answer: [Hidden]
"""


def calculate_self_powers_sum(limit: int) -> int:
    """
    自己べき乗の和を完全な値で計算（テスト用）
    時間計算量: O(n * log n)
    空間計算量: O(1)
    """
    total = 0
    for i in range(1, limit + 1):
        total += i**i
    return total


def solve_naive(limit: int = 1000) -> int:
    """
    素直な解法: 各項をそのまま計算して足し合わせる
    時間計算量: O(n * log n) - n項のべき乗計算
    空間計算量: O(1)
    """
    total = 0
    for i in range(1, limit + 1):
        total += i**i

    # 最後の10桁を返す
    return total % 10**10


def solve_optimized(limit: int = 1000) -> int:
    """
    最適化解法: モジュラー算術を使って各べき乗の計算時に余りを取る
    時間計算量: O(n * log n) - modular exponentiationでべき乗計算を効率化
    空間計算量: O(1)
    """
    modulo = 10**10
    total = 0

    for i in range(1, limit + 1):
        # modular exponentiationを使ってi^i mod 10^10を計算
        power_mod = pow(i, i, modulo)
        total = (total + power_mod) % modulo

    return total


def solve_mathematical(limit: int = 1000) -> int:
    """
    数学的解法: 末尾の0に寄与しない項のみを効率的に計算
    10の倍数は i^i の末尾10桁に0を多く含むため、寄与を最適化
    時間計算量: O(n * log n) - 但し実際の計算量は少ない
    空間計算量: O(1)
    """
    modulo = 10**10
    total = 0

    for i in range(1, limit + 1):
        # 10の倍数の場合、i^iの末尾10桁は0になる可能性が高い
        # i = 10k とすると i^i = (10k)^(10k) = 10^(10k) * k^(10k)
        # 10^(10k) は k >= 1 のとき末尾10桁は0になる
        if i % 10 == 0 and i >= 10:
            # 10以上の10の倍数は末尾10桁に影響しない
            continue

        # modular exponentiationでi^i mod 10^10を計算
        power_mod = pow(i, i, modulo)
        total = (total + power_mod) % modulo

    return total
