"""
Problem 76: Counting summations

How many different ways can one hundred be written as a sum of at least two positive integers?
"""


def solve_naive(n: int) -> int:
    """
    素直な解法: 動的計画法を使用して整数分割を計算

    Args:
        n: 分割する正の整数

    Returns:
        nを2つ以上の正の整数の和で表す方法の数

    時間計算量: O(n^2)
    空間計算量: O(n^2)
    """
    # dp[i][j] = iをj以下の正の整数の和で表す方法の数
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 初期化: 0は何も使わずに表せる（空の和）
    for j in range(n + 1):
        dp[0][j] = 1

    # 動的計画法で計算
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j > i:
                # jがiより大きい場合、j-1以下で表す方法と同じ
                dp[i][j] = dp[i][j - 1]
            else:
                # jを使う場合と使わない場合の和
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]

    # nをn以下の正の整数の和で表す方法の数から、n自身だけで表す場合を引く
    return dp[n][n] - 1


def solve_optimized(n: int) -> int:
    """
    最適化解法: 空間計算量を削減した動的計画法

    Args:
        n: 分割する正の整数

    Returns:
        nを2つ以上の正の整数の和で表す方法の数

    時間計算量: O(n^2)
    空間計算量: O(n)
    """
    # ways[i] = iを正の整数の和で表す方法の数
    ways = [0] * (n + 1)
    ways[0] = 1  # 0は空の和で表せる

    # 各数値kを使って和を作る
    for k in range(1, n):  # n未満まで（n自身を使わない）
        for i in range(k, n + 1):
            ways[i] += ways[i - k]

    return ways[n]
