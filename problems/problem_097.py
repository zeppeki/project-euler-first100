#!/usr/bin/env python3
"""
Problem 097: Large non-Mersenne prime

The first known prime found to be over one million digits was discovered in 1999,
and was a Mersenne prime of the form 2^p−1; it contains exactly 1,013,395 digits.
Subsequently other Mersenne primes, of the form 2^p−1, have been found which
contain more digits.

However, in 2004, a massive non-Mersenne prime was found which contains
2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.
"""


def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """
    モジュラー冪乗を効率的に計算
    時間計算量: O(log exponent)
    空間計算量: O(1)
    """
    if modulus == 1:
        return 0

    result = 1
    base = base % modulus

    while exponent > 0:
        # If exponent is odd, multiply base with result
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # exponent must be even now
        exponent = exponent >> 1  # exponent = exponent // 2
        base = (base * base) % modulus

    return result


def solve_naive(
    multiplier: int = 28433, exponent: int = 7830457, addend: int = 1
) -> int:
    """
    素直な解法: Pythonの組み込み関数を使用
    時間計算量: O(log exponent)
    空間計算量: O(1)
    """
    # Get last 10 digits (mod 10^10)
    modulus = 10**10

    # Calculate (multiplier * 2^exponent + addend) mod 10^10
    power_of_two = pow(2, exponent, modulus)
    return (multiplier * power_of_two + addend) % modulus


def solve_optimized(
    multiplier: int = 28433, exponent: int = 7830457, addend: int = 1
) -> int:
    """
    最適化解法: 自作のモジュラー冪乗を使用
    時間計算量: O(log exponent)
    空間計算量: O(1)
    """
    # Get last 10 digits (mod 10^10)
    modulus = 10**10

    # Calculate 2^exponent mod 10^10 using our implementation
    power_of_two = modular_exponentiation(2, exponent, modulus)
    return (multiplier * power_of_two + addend) % modulus


def solve_mathematical(
    multiplier: int = 28433, exponent: int = 7830457, addend: int = 1
) -> int:
    """
    数学的解法: モジュラー算術の性質を活用
    時間計算量: O(log exponent)
    空間計算量: O(1)
    """
    # This problem is fundamentally about modular exponentiation
    # The mathematical approach is the same as the optimized approach
    return solve_optimized(multiplier, exponent, addend)


def verify_small_case(multiplier: int, exponent: int, addend: int) -> int:
    """
    小さな指数の場合の検証用関数
    時間計算量: O(exponent) - 小さな値のみに使用
    空間計算量: O(1)
    """
    if exponent > 20:  # Avoid overflow for large exponents
        raise ValueError("This function is only for small exponents")

    # Direct calculation for small cases
    result: int = multiplier * (2**exponent) + addend
    return result % (10**10)


def main() -> None:
    """メイン実行関数"""
    import time

    print("Problem 097: Large non-Mersenne prime")
    print("=" * 40)

    # Small test case
    print("\n小さなテストケース:")
    small_mult, small_exp, small_add = 3, 5, 1

    print(f"3 × 2^5 + 1 = {3 * (2**5) + 1}")
    print(f"末尾10桁: {(3 * (2**5) + 1) % (10**10)}")

    result_naive = solve_naive(small_mult, small_exp, small_add)
    result_optimized = solve_optimized(small_mult, small_exp, small_add)
    result_mathematical = solve_mathematical(small_mult, small_exp, small_add)
    result_verify = verify_small_case(small_mult, small_exp, small_add)

    print(f"素直な解法: {result_naive}")
    print(f"最適化解法: {result_optimized}")
    print(f"数学的解法: {result_mathematical}")
    print(f"検証用関数: {result_verify}")

    # Main problem
    print("\nメイン問題: 28433 × 2^7830457 + 1 の末尾10桁")

    # Measure performance
    start_time = time.time()
    result = solve_optimized()
    end_time = time.time()

    print(f"結果: {result}")
    print(f"計算時間: {end_time - start_time:.6f}秒")

    # Verify all methods give the same result
    result_naive_main = solve_naive()
    result_mathematical_main = solve_mathematical()

    print("\n検証:")
    print(f"素直な解法: {result_naive_main}")
    print(f"最適化解法: {result}")
    print(f"数学的解法: {result_mathematical_main}")
    print(f"全て一致: {result_naive_main == result == result_mathematical_main}")


if __name__ == "__main__":
    main()
