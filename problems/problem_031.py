#!/usr/bin/env python3
"""
Problem 031: Coin sums

In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

Answer: Check on Project Euler official site
"""


def solve_naive(target: int = 200) -> int:
    """
    素直な解法: 再帰的に全ての組み合わせを試す
    時間計算量: O(8^target) - 指数的
    空間計算量: O(target) - 再帰の深さ
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    def count_ways(amount: int, coin_index: int) -> int:
        if amount == 0:
            return 1
        if amount < 0 or coin_index >= len(coins):
            return 0

        # 現在のコインを使わない場合と使う場合
        return count_ways(amount, coin_index + 1) + count_ways(
            amount - coins[coin_index], coin_index
        )

    return count_ways(target, 0)


def solve_optimized(target: int = 200) -> int:
    """
    最適化解法: 動的プログラミングを使用
    時間計算量: O(target * coins) = O(8 * target)
    空間計算量: O(target)
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[target]
