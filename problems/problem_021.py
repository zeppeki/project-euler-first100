#!/usr/bin/env python3
"""
Problem 021: Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Answer: 31626
"""

import time


def get_proper_divisors_naive(n: int) -> int:
    """
    素直な解法: 1からn-1まで全てをチェックして真約数の和を求める

    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n <= 1:
        return 0

    divisor_sum = 1  # 1は常に真約数
    for i in range(2, n):
        if n % i == 0:
            divisor_sum += i

    return divisor_sum


def get_proper_divisors_optimized(n: int) -> int:
    """
    最適化解法: 平方根まで試し割りで真約数の和を求める

    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n <= 1:
        return 0

    divisor_sum = 1  # 1は常に真約数
    i = 2

    while i * i <= n:
        if n % i == 0:
            divisor_sum += i
            # 平方根でない場合は対応する約数も追加
            if i * i != n:
                divisor_sum += n // i
        i += 1

    return divisor_sum


def solve_naive(limit: int) -> int:
    """
    素直な解法: 各数について真約数の和を計算し友愛数を判定

    時間計算量: O(n²)
    空間計算量: O(1)
    """
    amicable_sum = 0

    for a in range(2, limit):
        b = get_proper_divisors_naive(a)
        # 友愛数の条件をチェック
        if a != b and b < limit and get_proper_divisors_naive(b) == a:
            amicable_sum += a

    return amicable_sum


def solve_optimized(limit: int) -> int:
    """
    最適化解法: 効率的な約数計算を使用

    時間計算量: O(n√n)
    空間計算量: O(1)
    """
    amicable_sum = 0

    for a in range(2, limit):
        b = get_proper_divisors_optimized(a)
        # 友愛数の条件をチェック
        if a != b and b < limit and get_proper_divisors_optimized(b) == a:
            amicable_sum += a

    return amicable_sum


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: 事前計算で全ての真約数の和をキャッシュ

    時間計算量: O(n√n)
    空間計算量: O(n)
    """
    # 全ての数の真約数の和を事前計算
    divisor_sums = [0] * limit

    # エラトステネスの篩的アプローチで効率的に計算
    for i in range(1, limit):
        # iを約数として持つ全ての数に加算
        for j in range(2 * i, limit, i):
            divisor_sums[j] += i

    # 友愛数を探索
    amicable_numbers: set[int] = set()

    for a in range(2, limit):
        b = divisor_sums[a]
        # 友愛数の条件をチェック
        if a != b and b < limit and divisor_sums[b] == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)

    return sum(amicable_numbers)


def find_amicable_pairs(limit: int) -> list[tuple[int, int]]:
    """
    指定した範囲内の友愛数ペアを全て取得

    Args:
        limit: 探索範囲の上限

    Returns:
        友愛数ペアのリスト
    """
    pairs = []
    found = set()

    for a in range(2, limit):
        if a in found:
            continue

        b = get_proper_divisors_optimized(a)
        if a != b and b < limit and get_proper_divisors_optimized(b) == a:
            pairs.append((a, b))
            found.add(a)
            found.add(b)

    return pairs


def validate_amicable_pair(a: int, b: int) -> bool:
    """
    友愛数ペアの検証

    Args:
        a, b: 検証する数のペア

    Returns:
        友愛数ペアの場合True
    """
    return (
        a != b
        and get_proper_divisors_optimized(a) == b
        and get_proper_divisors_optimized(b) == a
    )


def test_solutions() -> None:
    """テストケースで解答を検証"""
    print("=== 基本テスト ===")

    # 既知の友愛数ペア
    print("220の真約数の和:", get_proper_divisors_optimized(220))
    print("284の真約数の和:", get_proper_divisors_optimized(284))
    print("220と284は友愛数か:", validate_amicable_pair(220, 284))
    print()

    # 小さい範囲でのテスト
    test_limits = [300, 1000]

    for limit in test_limits:
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_math = solve_mathematical(limit)

        print(f"{limit}未満の友愛数の和:")
        print(f"  Naive: {result_naive}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == result_naive else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == result_naive else '✗'}"
        )

        # 友愛数ペアの詳細表示
        pairs = find_amicable_pairs(limit)
        print(f"  友愛数ペア: {pairs}")
        print()


def main() -> None:
    """メイン関数"""
    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")
    limit = 10000

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(limit)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(limit)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(limit)
    math_time = time.time() - start_time

    print(f"{limit}未満の友愛数の和:")
    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized == result_math:
        print(f"✓ 解答: {result_optimized:,}")
    else:
        print("✗ 解答が一致しません")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 友愛数ペアの表示
    print("\n=== 友愛数ペア一覧 ===")
    pairs = find_amicable_pairs(limit)
    for a, b in pairs:
        print(f"({a}, {b}): d({a}) = {b}, d({b}) = {a}")

    print(f"\n総計: {len(pairs)}組の友愛数ペア")
    print(f"友愛数の個数: {len(pairs) * 2}個")

    # アルゴリズム解説
    print("\n=== アルゴリズム解説 ===")
    print("1. 素直な解法: 各数で1からn-1まで全約数をチェック O(n²)")
    print("2. 最適化解法: 平方根まで試し割りで約数計算を効率化 O(n√n)")
    print("3. 数学的解法: エラトステネス篩的前処理で一括計算 O(n√n)")
    print()
    print("友愛数の性質:")
    print("- d(a) = b かつ d(b) = a (a ≠ b)")
    print("- 完全数 (d(n) = n) は友愛数ではない")
    print("- 真約数は自分自身を含まない約数")


if __name__ == "__main__":
    main()
