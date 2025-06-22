#!/usr/bin/env python3
"""
Problem 001: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
"""

import time


def solve_naive(limit):
    """
    素直な解法: 1からlimit-1までの数を順番にチェック
    時間計算量: O(n)
    空間計算量: O(1)
    """
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def solve_optimized(limit):
    """
    最適化解法: 等差数列の和の公式を使用
    時間計算量: O(1)
    空間計算量: O(1)
    """
    def sum_multiples(n, limit):
        """nの倍数の和を計算（limit未満）"""
        count = (limit - 1) // n
        return n * count * (count + 1) // 2
    
    # 3の倍数の和 + 5の倍数の和 - 15の倍数の和（重複を除く）
    return sum_multiples(3, limit) + sum_multiples(5, limit) - sum_multiples(15, limit)


def solve_list_comprehension(limit):
    """
    リスト内包表記を使用した解法
    時間計算量: O(n)
    空間計算量: O(n)
    """
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)


def main():
    """メイン関数"""
    limit = 1000
    
    print("Problem 001: Multiples of 3 and 5")
    print("=" * 40)
    
    # テストケース
    test_limit = 10
    expected = 23
    result = solve_naive(test_limit)
    print(f"Test case (limit={test_limit}): {result} (expected: {expected})")
    assert result == expected, f"Test failed: {result} != {expected}"
    print("✅ Test case passed!")
    print()
    
    # 本問題の解答
    print(f"Finding sum of multiples of 3 or 5 below {limit}")
    print("-" * 40)
    
    # 各解法で解答
    methods = [
        ("Naive approach", solve_naive),
        ("Optimized approach", solve_optimized),
        ("List comprehension", solve_list_comprehension)
    ]
    
    for name, method in methods:
        start_time = time.time()
        result = method(limit)
        end_time = time.time()
        
        print(f"{name}:")
        print(f"  Answer: {result}")
        print(f"  Time: {(end_time - start_time) * 1000:.3f} ms")
        print()
    
    print("=" * 40)
    print(f"Final Answer: {solve_optimized(limit)}")


if __name__ == "__main__":
    main() 