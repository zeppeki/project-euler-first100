"""
Problem 78: Coin partitions

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into piles
in exactly seven different ways, so p(5)=7.

Find the least value of n for which p(n) is divisible by one million.
"""


def partition_function_naive(n: int, modulo: int | None = None) -> int:
    """
    素直な解法: 動的計画法で分割数を計算

    Args:
        n: 分割する数
        modulo: 剰余を取る値（省略可能）

    Returns:
        nの分割数（moduloが指定されている場合はその剰余）

    時間計算量: O(n²)
    空間計算量: O(n²)
    """
    # dp[i][j] = iをj以下の数で分割する方法の数
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 初期値: 0はどんな数でも空の分割で表せる
    for j in range(n + 1):
        dp[0][j] = 1

    # 動的計画法で計算
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # jを使わない場合
            dp[i][j] = dp[i][j - 1]
            # jを使う場合
            if i >= j:
                dp[i][j] += dp[i - j][j]
            # 剰余を取る
            if modulo:
                dp[i][j] %= modulo

    return dp[n][n]


def partition_function_optimized(n: int, modulo: int | None = None) -> int:
    """
    最適化解法: オイラーの五角数定理を使用した高速計算

    p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - ...
    ここで、1, 2, 5, 7, 12, 15, ... は一般化五角数

    Args:
        n: 分割する数
        modulo: 剰余を取る値（省略可能）

    Returns:
        nの分割数（moduloが指定されている場合はその剰余）

    時間計算量: O(n√n)
    空間計算量: O(n)
    """
    # メモ化用の配列
    partition = [0] * (n + 1)
    partition[0] = 1

    for i in range(1, n + 1):
        # オイラーの五角数定理による計算
        k = 1
        sign = 1
        while True:
            # 一般化五角数: k(3k-1)/2 と k(3k+1)/2
            pentagonal1 = k * (3 * k - 1) // 2
            pentagonal2 = k * (3 * k + 1) // 2

            if pentagonal1 > i:
                break

            # p(i-pentagonal1)を加算/減算
            partition[i] += sign * partition[i - pentagonal1]
            if modulo:
                partition[i] %= modulo

            # p(i-pentagonal2)を加算/減算（範囲内の場合）
            if pentagonal2 <= i:
                partition[i] += sign * partition[i - pentagonal2]
                if modulo:
                    partition[i] %= modulo

            # 符号を反転
            sign = -sign
            k += 1

        # 最終的な剰余を取る
        if modulo:
            partition[i] = partition[i] % modulo

    return partition[n]


def solve_naive(target_divisor: int) -> int:
    """
    素直な解法: 各nについて分割数を計算し、target_divisorで割り切れるか確認

    Args:
        target_divisor: 分割数が割り切れるべき値

    Returns:
        p(n)がtarget_divisorで割り切れる最小のn

    時間計算量: O(n³)（最悪の場合）
    空間計算量: O(n²)
    """
    n = 1
    while True:
        p_n = partition_function_naive(n, target_divisor)
        if p_n == 0:  # target_divisorで割った余りが0
            return n
        n += 1
        # 安全のため上限を設定
        if n > 10000:
            raise ValueError("Solution not found within reasonable limit")


def solve_optimized(target_divisor: int) -> int:
    """
    最適化解法: オイラーの五角数定理を使用して高速に計算

    Args:
        target_divisor: 分割数が割り切れるべき値

    Returns:
        p(n)がtarget_divisorで割り切れる最小のn

    時間計算量: O(n²√n)（最悪の場合）
    空間計算量: O(n)
    """
    # 分割数を保持する配列（moduloで計算）
    max_n = 100000  # 十分大きな値
    partition = [0] * max_n
    partition[0] = 1

    for n in range(1, max_n):
        # オイラーの五角数定理による計算
        k = 1
        sign = 1
        while True:
            # 一般化五角数
            pentagonal1 = k * (3 * k - 1) // 2
            pentagonal2 = k * (3 * k + 1) // 2

            if pentagonal1 > n:
                break

            # 剰余を取りながら計算
            partition[n] = (
                partition[n] + sign * partition[n - pentagonal1]
            ) % target_divisor

            if pentagonal2 <= n:
                partition[n] = (
                    partition[n] + sign * partition[n - pentagonal2]
                ) % target_divisor

            sign = -sign
            k += 1

        # 答えが見つかったら返す
        if partition[n] == 0:
            return n

    raise ValueError("Solution not found within limit")
