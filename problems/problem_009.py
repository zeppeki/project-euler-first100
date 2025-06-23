#!/usr/bin/env python3
"""
Problem 009: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
import time


def solve_naive(target_sum: int = 1000) -> int:
    """
    素直な解法: 3重ループで全ての組み合わせをチェック
    時間計算量: O(n³)
    空間計算量: O(1)
    """
    if target_sum <= 0:
        raise ValueError("target_sum must be positive")

    # a < b < c かつ a + b + c = target_sum
    # 最小のピタゴラス数は (3, 4, 5) なので a は最低 1 から開始
    for a in range(1, target_sum // 3):  # a は target_sum の 1/3 未満
        for b in range(
            a + 1, target_sum // 2
        ):  # b は a より大きく、target_sum の 1/2 未満
            c = target_sum - a - b

            # c > b である必要がある
            if c <= b:
                continue

            # ピタゴラスの定理をチェック
            if a * a + b * b == c * c:
                return a * b * c

    return 0  # 解が見つからない場合


def solve_optimized(target_sum: int = 1000) -> int:
    """
    最適化解法: 2重ループで c を計算により求める
    時間計算量: O(n²)
    空間計算量: O(1)
    """
    if target_sum <= 0:
        raise ValueError("target_sum must be positive")

    # a < b < c かつ a + b + c = target_sum
    # c = target_sum - a - b として計算
    for a in range(1, target_sum // 3):  # a は target_sum の 1/3 未満
        for b in range(a + 1, (target_sum - a + 1) // 2):  # b < c を満たすように
            c = target_sum - a - b

            # b < c の条件を確認（念のため）
            if b >= c:
                continue

            # ピタゴラスの定理をチェック
            if a * a + b * b == c * c:
                return a * b * c

    return 0  # 解が見つからない場合


def solve_mathematical(target_sum: int = 1000) -> int:
    """
    数学的解法: 原始ピタゴラス数の生成公式を使用
    時間計算量: O(sqrt(n))
    空間計算量: O(1)

    原始ピタゴラス数の一般形:
    a = m² - n²
    b = 2mn
    c = m² + n²
    ここで m > n > 0, gcd(m,n) = 1, m と n の一方は偶数
    """
    if target_sum <= 0:
        raise ValueError("target_sum must be positive")

    # 原始ピタゴラス数とその倍数を探索
    # m の上限は √(target_sum/2) 程度
    m_limit = int(math.sqrt(target_sum / 2)) + 1

    for m in range(2, m_limit):
        for n in range(1, m):
            # 原始ピタゴラス数の条件をチェック
            if math.gcd(m, n) != 1:
                continue
            if (m % 2) == (n % 2):  # m と n の一方は偶数である必要
                continue

            # 原始ピタゴラス数を生成
            a_primitive = m * m - n * n
            b_primitive = 2 * m * n
            c_primitive = m * m + n * n

            # a < b を保証するため、必要に応じて交換
            if a_primitive > b_primitive:
                a_primitive, b_primitive = b_primitive, a_primitive

            sum_primitive = a_primitive + b_primitive + c_primitive

            # target_sum が原始ピタゴラス数の倍数になるかチェック
            if target_sum % sum_primitive == 0:
                k = target_sum // sum_primitive
                a = k * a_primitive
                b = k * b_primitive
                c = k * c_primitive

                # 解が見つかった
                return a * b * c

    return 0  # 解が見つからない場合


def find_pythagorean_triplet(target_sum: int = 1000) -> tuple[int, int, int] | None:
    """
    指定された和を持つピタゴラス数の組を返すヘルパー関数
    """
    if target_sum <= 0:
        raise ValueError("target_sum must be positive")

    for a in range(1, target_sum // 3):
        for b in range(a + 1, (target_sum - a + 1) // 2):
            c = target_sum - a - b

            # b < c の条件を確認（念のため）
            if b >= c:
                continue

            if a * a + b * b == c * c:
                return (a, b, c)

    return None


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (12, 60),  # (3, 4, 5): 3+4+5=12, 3*4*5=60
        (30, 780),  # (5, 12, 13): 5+12+13=30, 5*12*13=780
        (24, 480),  # (6, 8, 10): 6+8+10=24, 6*8*10=480
        (1000, 31875000),  # 本問題の解答
    ]

    print("=== テストケース ===")
    for target_sum, expected in test_cases:
        result_naive = solve_naive(target_sum)
        result_optimized = solve_optimized(target_sum)
        result_math = solve_mathematical(target_sum)

        print(f"Target sum = {target_sum}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}"
        )

        # ピタゴラス数の組も表示
        triplet = find_pythagorean_triplet(target_sum)
        if triplet:
            a, b, c = triplet
            print(f"  Triplet: ({a}, {b}, {c})")
            print(
                f"  Verification: {a}² + {b}² = {a * a} + {b * b} = {a * a + b * b} = {c * c} = {c}²"
            )
        print()


def main() -> None:
    """メイン関数"""
    target_sum = 1000

    print("=== Problem 009: Special Pythagorean triplet ===")
    print(f"Finding Pythagorean triplet where a + b + c = {target_sum}")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(target_sum)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(target_sum)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(target_sum)
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
        print(f"  Naive: {result_naive}")
        print(f"  Optimized: {result_optimized}")
        print(f"  Mathematical: {result_math}")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 詳細な計算過程の表示
    print("\n=== 計算過程の詳細 ===")

    # ピタゴラス数の組を表示
    triplet = find_pythagorean_triplet(target_sum)
    if triplet:
        a, b, c = triplet
        print(f"ピタゴラス数の組: ({a}, {b}, {c})")
        print("条件確認:")
        print(f"  a < b < c: {a} < {b} < {c} {'✓' if a < b < c else '✗'}")
        print(
            f"  a + b + c = {target_sum}: {a} + {b} + {c} = {a + b + c} {'✓' if a + b + c == target_sum else '✗'}"
        )
        print(
            f"  a² + b² = c²: {a}² + {b}² = {a * a} + {b * b} = {a * a + b * b} = {c * c} = {c}² {'✓' if a * a + b * b == c * c else '✗'}"
        )
        print(f"  積 abc: {a} × {b} × {c} = {a * b * c:,}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 3重ループで全ての (a, b, c) の組み合わせをチェック")
    print("最適化解法: 2重ループで c = target_sum - a - b として計算")
    print("数学的解法: 原始ピタゴラス数の生成公式 (m² - n², 2mn, m² + n²) を使用")

    # ピタゴラス数に関する数学的背景
    print("\n=== 数学的背景 ===")
    print("ピタゴラスの定理: a² + b² = c²")
    print("原始ピタゴラス数: gcd(a, b, c) = 1 となるピタゴラス数")
    print("ユークリッドの公式: a = m² - n², b = 2mn, c = m² + n²")
    print("  条件: m > n > 0, gcd(m, n) = 1, m と n の一方は偶数")

    # 小さな例での説明
    print("\n=== 小さな例での説明 ===")
    small_examples = [12, 30, 24]
    for example_sum in small_examples:
        example_triplet = find_pythagorean_triplet(example_sum)
        if example_triplet:
            a, b, c = example_triplet
            print(f"a + b + c = {example_sum}: ({a}, {b}, {c}), 積 = {a * b * c}")
        else:
            print(f"a + b + c = {example_sum}: 解なし")


if __name__ == "__main__":
    main()
