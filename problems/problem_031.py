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

import time


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


def test_solutions() -> None:
    """テストケースで解答を検証"""
    assert (
        solve_optimized(5) == 4
    )  # 5pを作る方法: 5p, 2p+2p+1p, 2p+1p+1p+1p, 1p+1p+1p+1p+1p
    assert solve_optimized(10) == 11  # 10pを作る方法

    # メイン問題のテスト（素直な解法は遅いので小さい値のみ）
    assert solve_naive(10) == solve_optimized(10)

    print("All tests passed!")


def main() -> None:
    """メイン関数"""
    print("=== Problem 031: Coin sums ===")

    # テスト実行
    test_solutions()

    # 実際の問題を解く（200p = £2）
    start_time = time.time()
    result_optimized = solve_optimized(200)
    optimized_time = time.time() - start_time

    print(f"Optimized solution: {result_optimized}")
    print(f"Execution time (optimized): {optimized_time:.6f} seconds")

    # 小さい値での比較
    print("\nSmall test comparisons:")
    for test_val in [5, 10, 20]:
        start_time = time.time()
        naive_result = solve_naive(test_val)
        naive_time = time.time() - start_time

        start_time = time.time()
        opt_result = solve_optimized(test_val)
        opt_time = time.time() - start_time

        print(
            f"Target {test_val}p: Naive={naive_result} ({naive_time:.6f}s), "
            f"Optimized={opt_result} ({opt_time:.6f}s)"
        )


if __name__ == "__main__":
    main()
