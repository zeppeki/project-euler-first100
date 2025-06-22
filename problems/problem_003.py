#!/usr/bin/env python3
"""
Problem 003: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Answer: 6857
"""

import time
import math

def is_prime(n: int) -> bool:
    """
    素数判定関数
    
    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 3から√nまでの奇数で試し割り
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve_naive(n: int) -> int:
    """
    素直な解法
    2から順に試し割りで素因数分解
    
    時間計算量: O(n)
    空間計算量: O(1)
    """
    if n < 2:
        return n
    
    largest_prime = 1
    current = n
    
    # 2で割り切れるだけ割る
    while current % 2 == 0:
        largest_prime = 2
        current //= 2
    
    # 3から順に奇数で試し割り
    for i in range(3, current + 1, 2):
        while current % i == 0:
            largest_prime = i
            current //= i
        if current == 1:
            break
    
    return largest_prime

def solve_optimized(n: int) -> int:
    """
    最適化解法
    平方根まで試し割り、その後残った数が素数かチェック
    
    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n < 2:
        return n
    
    largest_prime = 1
    current = n
    
    # 2で割り切れるだけ割る
    while current % 2 == 0:
        largest_prime = 2
        current //= 2
    
    # 3から√nまでの奇数で試し割り
    sqrt_n = int(math.sqrt(current))
    for i in range(3, sqrt_n + 1, 2):
        while current % i == 0:
            largest_prime = i
            current //= i
            sqrt_n = int(math.sqrt(current))  # 平方根を再計算
    
    # 残った数が1より大きければ、それは素数
    if current > 1:
        largest_prime = current
    
    return largest_prime

def solve_mathematical(n: int) -> int:
    """
    数学的解法
    より効率的な素因数分解アルゴリズム
    
    時間計算量: O(√n)
    空間計算量: O(1)
    """
    if n < 2:
        return n
    
    def trial_division(n: int) -> list:
        """試し割りによる素因数分解"""
        factors = []
        current = n
        
        # 2で割り切れるだけ割る
        while current % 2 == 0:
            factors.append(2)
            current //= 2
        
        # 3から√nまでの奇数で試し割り
        for i in range(3, int(math.sqrt(current)) + 1, 2):
            while current % i == 0:
                factors.append(i)
                current //= i
        
        # 残った数が1より大きければ、それは素数
        if current > 1:
            factors.append(current)
        
        return factors
    
    factors = trial_division(n)
    return max(factors) if factors else 1

def test_solutions():
    """テストケースで解答を検証"""
    test_cases = [
        (13195, 29),      # 例題: 5, 7, 13, 29 → 最大は29
        (100, 5),         # 100 = 2^2 × 5^2 → 最大は5
        (84, 7),          # 84 = 2^2 × 3 × 7 → 最大は7
        (17, 17),         # 素数 → 最大は17
        (25, 5),          # 25 = 5^2 → 最大は5
    ]
    
    print("=== テストケース ===")
    for n, expected in test_cases:
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)
        
        print(f"n = {n}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}")
        print(f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}")
        print()

def main():
    """メイン関数"""
    n = 600851475143
    
    print("=== Problem 003: Largest prime factor ===")
    print(f"n = {n:,}")
    print()
    
    # テストケース
    test_solutions()
    
    # 本問題の解答
    print("=== 本問題の解答 ===")
    
    # 素直な解法（大きな数では時間がかかりすぎるため、小さな数でテスト）
    print("素直な解法は大きな数では時間がかかりすぎるため、小さな数でテスト:")
    test_n = 13195
    start_time = time.time()
    result_naive = solve_naive(test_n)
    naive_time = time.time() - start_time
    print(f"  n = {test_n}: {result_naive} (実行時間: {naive_time:.6f}秒)")
    
    # 最適化解法
    start_time = time.time()
    result_optimized = solve_optimized(n)
    optimized_time = time.time() - start_time
    
    # 数学的解法
    start_time = time.time()
    result_math = solve_mathematical(n)
    math_time = time.time() - start_time
    
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print()
    
    # 結果の検証
    if result_optimized == result_math:
        print(f"✓ 解答: {result_optimized:,}")
        
        # 素因数分解の確認
        print(f"\n素因数分解の確認:")
        current = n
        factors = []
        
        # 2で割り切れるだけ割る
        while current % 2 == 0:
            factors.append(2)
            current //= 2
        
        # 3から順に奇数で試し割り
        for i in range(3, int(math.sqrt(current)) + 1, 2):
            while current % i == 0:
                factors.append(i)
                current //= i
        
        if current > 1:
            factors.append(current)
        
        print(f"  素因数: {factors}")
        print(f"  最大の素因数: {max(factors)}")
        print(f"  検証: {result_optimized == max(factors)}")
        
    else:
        print("✗ 解答が一致しません")
        return
    
    # パフォーマンス比較
    print("\n=== パフォーマンス比較 ===")
    fastest_time = min(optimized_time, math_time)
    print(f"最適化解法: {optimized_time/fastest_time:.2f}x")
    print(f"数学的解法: {math_time/fastest_time:.2f}x")

if __name__ == "__main__":
    main() 