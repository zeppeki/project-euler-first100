#!/usr/bin/env python3
"""
Runner for Problem 015: Lattice paths
"""

import time

from problems.problem_015 import (
    solve_mathematical,
    solve_mathematical_factorial,
    solve_naive,
    solve_optimized,
)


def test_solutions() -> None:
    """テストケースで解答を検証"""
    test_cases = [
        (0, 1),  # 0×0グリッド: 1通り（移動なし）
        (1, 2),  # 1×1グリッド: 2通り（右→下 or 下→右）
        (2, 6),  # 2×2グリッド: 6通り（問題例）
        (3, 20),  # 3×3グリッド: 20通り
        (4, 70),  # 4×4グリッド: 70通り
        (5, 252),  # 5×5グリッド: 252通り
        (10, 184756),  # 10×10グリッド: 184756通り
    ]

    print("=== テストケース ===")
    for n, expected in test_cases:
        result_naive = solve_naive(n)
        result_optimized = solve_optimized(n)
        result_math = solve_mathematical(n)
        result_factorial = solve_mathematical_factorial(n)

        print(f"n = {n}")
        print(f"  Expected: {expected}")
        print(f"  Naive: {result_naive} {'✓' if result_naive == expected else '✗'}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == expected else '✗'}"
        )
        print(
            f"  Factorial: {result_factorial} {'✓' if result_factorial == expected else '✗'}"
        )
        print()


def main() -> None:
    """メイン関数"""
    n = 20

    print("=== Problem 015: Lattice paths ===")
    print(f"Finding the number of paths in a {n}×{n} grid")
    print()

    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(n)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(n)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(n)
    math_time = time.time() - start_time

    start_time = time.time()
    result_factorial = solve_mathematical_factorial(n)
    factorial_time = time.time() - start_time

    print(f"素直な解法: {result_naive:,} (実行時間: {naive_time:.6f}秒)")
    print(f"最適化解法: {result_optimized:,} (実行時間: {optimized_time:.6f}秒)")
    print(f"数学的解法: {result_math:,} (実行時間: {math_time:.6f}秒)")
    print(f"階乗解法: {result_factorial:,} (実行時間: {factorial_time:.6f}秒)")
    print()

    # 結果の検証
    if result_naive == result_optimized == result_math == result_factorial:
        print(f"✓ 解答: {result_math:,}")
    else:
        print("✗ 解答が一致しません")
        print(f"  Naive: {result_naive}")
        print(f"  Optimized: {result_optimized}")
        print(f"  Mathematical: {result_math}")
        print(f"  Factorial: {result_factorial}")
        return

    # パフォーマンス比較
    print("=== パフォーマンス比較 ===")
    fastest_time = min(naive_time, optimized_time, math_time, factorial_time)
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")
    print(f"階乗解法: {factorial_time / fastest_time:.2f}x")

    # 詳細な計算過程の表示
    print("\n=== 計算過程の詳細 ===")

    # 小さなグリッドの可視化
    print("2×2グリッドの経路例:")
    print("Start → → End")
    print("  ↓   ↘   ↓")
    print("  ↓   ↓   ↓")
    print("  → → → End")
    print("可能な経路: 右右下下, 右下右下, 右下下右, 下右右下, 下右下右, 下下右右")
    print(f"総経路数: {solve_mathematical(2)}通り")

    # 組み合わせ論の説明
    print(f"\n{n}×{n}グリッドの場合:")
    print(f"・総移動回数: {2 * n}回（右に{n}回、下に{n}回）")
    print(f"・組み合わせ数: C({2 * n}, {n}) = {2 * n}! / ({n}! × {n}!)")
    print(f"・計算結果: {result_math:,}")

    # アルゴリズムの説明
    print("\n=== アルゴリズムの説明 ===")
    print("素直な解法: 動的プログラミングで各点までの経路数を計算")
    print("最適化解法: 動的プログラミングで空間効率を向上")
    print("数学的解法: 組み合わせ論 C(2n,n) を効率的に計算")
    print("階乗解法: math.factorial()を使用した直接計算")


if __name__ == "__main__":
    main()
