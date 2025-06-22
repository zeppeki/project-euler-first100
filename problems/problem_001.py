#!/usr/bin/env python3
"""
Problem 001: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
"""

import time


def solve_naive(limit: int) -> int:
    """
    素直な解法: 1からlimit-1までの数を順番にチェック
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if limit <= 0:
        return 0
    
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def solve_optimized(limit: int) -> int:
    """
    最適化解法: 等差数列の和の公式を使用
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if limit <= 0:
        return 0
    
    def sum_multiples(n: int, limit: int) -> int:
        """nの倍数の和を計算（limit未満）"""
        count = (limit - 1) // n
        return n * count * (count + 1) // 2
    
    # 3の倍数の和 + 5の倍数の和 - 15の倍数の和（重複を除く）
    return sum_multiples(3, limit) + sum_multiples(5, limit) - sum_multiples(15, limit)


def solve_mathematical(limit: int) -> int:
    """
    数学的解法: リスト内包表記を使用
    時間計算量: O(n)
    空間計算量: O(n)
    """
    if limit <= 0:
        return 0
    
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (10, 23),      # 3 + 5 + 6 + 9 = 23
        (20, 78),      # 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
        (100, 2318),   # Known result for limit 100
    ]
    
    print("=== テストケース ===")
    for limit, expected in test_cases:
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_math = solve_mathematical(limit)
        
        print(f"Limit: {limit}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}")
        print(f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}")
        print()


def main() -> None:
    """メイン関数"""
    limit = 1000
    
    print("=== Problem 001: Multiples of 3 and 5 ===")
    print(f"Limit: {limit}")
    print()
    
    # テストケース
    test_solutions()
    
    # 本問題の解答
    print("=== 本問題の解答 ===")
    
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
    print(f"素直な解法: {naive_time/fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time/fastest_time:.2f}x")
    print(f"数学的解法: {math_time/fastest_time:.2f}x")


if __name__ == "__main__":
    main() 