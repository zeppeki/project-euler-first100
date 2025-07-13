#!/usr/bin/env python3
"""
Problem 100: Arranged probability

A box contains colored discs (blue and red).

When 21 discs are in the box (15 blue, 6 red), the probability of drawing
2 blue discs is exactly 50%: P(BB) = (15/21) × (14/20) = 1/2.

Find the first arrangement with over 10^12 total discs where the probability
of drawing 2 blue discs is exactly 50%.

Mathematical formulation:
If b = blue discs, n = total discs, then:
P(BB) = b/n × (b-1)/(n-1) = 1/2
=> 2b(b-1) = n(n-1)

This leads to a Pell equation that can be solved efficiently.
"""

import math


def is_valid_arrangement(blue: int, total: int) -> bool:
    """
    青と全体の数が有効な配置かチェック
    P(BB) = b/n × (b-1)/(n-1) = 1/2
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if blue <= 0 or total <= 0 or blue > total:
        return False

    # 2b(b-1) = n(n-1) かチェック
    return 2 * blue * (blue - 1) == total * (total - 1)


def solve_naive(limit: int = 10**12) -> int:
    """
    素直な解法: Pell方程式の解を順次計算
    大きな数でも動作するよう、数学的解法と同じ漸化式を使用
    時間計算量: O(log limit)
    空間計算量: O(1)
    """
    # 初期解: (b=15, n=21) => (x=29, y=41)
    x, y = 29, 41

    while True:
        # x = 2b - 1, y = 2n - 1 から b, n を復元
        blue = (x + 1) // 2
        total = (y + 1) // 2

        # 検証
        if not is_valid_arrangement(blue, total):
            raise ValueError(f"Invalid arrangement: b={blue}, n={total}")

        if total > limit:
            return blue

        # 次の解を計算: y² - 2x² = -1 の漸化式
        x_new = 2 * y + 3 * x
        y_new = 3 * y + 4 * x
        x, y = x_new, y_new


def solve_optimized(limit: int = 10**12) -> int:
    """
    最適化解法: Pell方程式を使った効率的な解法

    2b(b-1) = n(n-1) を変形すると:
    y² - 2x² = -1 の形になる

    x = 2b - 1, y = 2n - 1 とすると:
    y² - 2x² = -1 (Pell方程式)

    時間計算量: O(log limit)
    空間計算量: O(1)
    """
    # 初期解: (b=15, n=21) => (x=29, y=41)
    x, y = 29, 41

    # Pell方程式 y² - 2x² = -1 の漸化式
    # (x', y') = (2y + 3x, 3y + 4x)

    while True:
        # x = 2b - 1, y = 2n - 1 から b, n を復元
        b = (x + 1) // 2
        n = (y + 1) // 2

        if n > limit:
            return b

        # 次の解を計算
        x_new = 2 * y + 3 * x
        y_new = 3 * y + 4 * x
        x, y = x_new, y_new


def solve_mathematical(limit: int = 10**12) -> int:
    """
    数学的解法: Pell方程式の理論を使った最適解

    問題は y² - 2x² = -1 型のPell方程式に帰着される
    基本解から漸化式で次の解を求める

    時間計算量: O(log limit)
    空間計算量: O(1)
    """
    # 基本解: x₀ = 1, y₀ = 1 (y² - 2x² = -1の最小解)
    # 問題の最初の解: x₁ = 29, y₁ = 41 (b=15, n=21に対応)

    x, y = 29, 41

    # 漸化式による解の生成
    # (xₖ₊₁, yₖ₊₁) = (2yₖ + 3xₖ, 3yₖ + 4xₖ)

    while True:
        # 座標変換: x = 2b - 1, y = 2n - 1
        blue_discs = (x + 1) // 2
        total_discs = (y + 1) // 2

        # 検証
        if not is_valid_arrangement(blue_discs, total_discs):
            raise ValueError(f"Invalid arrangement: b={blue_discs}, n={total_discs}")

        if total_discs > limit:
            return blue_discs

        # 次の解を計算
        x_next = 2 * y + 3 * x
        y_next = 3 * y + 4 * x
        x, y = x_next, y_next


def find_next_arrangement(blue: int, total: int) -> tuple[int, int]:
    """
    現在の配置から次の有効な配置を見つける
    """
    # x = 2b - 1, y = 2n - 1 に変換
    x = 2 * blue - 1
    y = 2 * total - 1

    # 次の解を計算: y² - 2x² = -1 の漸化式
    x_next = 2 * y + 3 * x
    y_next = 3 * y + 4 * x

    # b, n に変換して戻す
    blue_next = (x_next + 1) // 2
    total_next = (y_next + 1) // 2

    return blue_next, total_next


def verify_arrangement(blue: int, total: int) -> dict:
    """
    配置の詳細情報を検証・取得
    """
    red = total - blue

    # 確率計算
    prob_first_blue = blue / total
    prob_second_blue_given_first = (blue - 1) / (total - 1)
    prob_both_blue = prob_first_blue * prob_second_blue_given_first

    # 数式検証
    formula_left = 2 * blue * (blue - 1)
    formula_right = total * (total - 1)

    return {
        "blue": blue,
        "red": red,
        "total": total,
        "prob_both_blue": prob_both_blue,
        "is_exactly_half": abs(prob_both_blue - 0.5) < 1e-15,
        "formula_valid": formula_left == formula_right,
        "formula_left": formula_left,
        "formula_right": formula_right,
    }


def main() -> None:
    """メイン実行関数"""
    print("Problem 100: Arranged probability")
    print("=" * 40)

    # 問題の例を検証
    print("例の検証:")
    examples = [(15, 21), (85, 120)]

    for blue, total in examples:
        info = verify_arrangement(blue, total)
        print(f"  青: {blue}, 全体: {total}")
        print(f"  確率: {info['prob_both_blue']:.10f}")
        print(f"  正確に1/2: {info['is_exactly_half']}")
        print(f"  数式検証: {info['formula_valid']}")
        print()

    # 解を求める
    print("解を計算中...")
    import time

    limit = 10**12

    start_time = time.time()
    result = solve_mathematical(limit)
    end_time = time.time()

    # 結果の検証
    blue, total = result, 0

    # totalを逆算
    # 2b(b-1) = n(n-1) から n を求める
    # n² - n - 2b(b-1) = 0
    # n = (1 + √(1 + 8b(b-1))) / 2

    discriminant = 1 + 8 * blue * (blue - 1)
    total = int((1 + math.sqrt(discriminant)) / 2)

    info = verify_arrangement(blue, total)

    print("結果:")
    print(f"  青いディスクの数: {blue:,}")
    print(f"  全体のディスク数: {total:,}")
    print(f"  赤いディスクの数: {info['red']:,}")
    print(f"  計算時間: {end_time - start_time:.6f}秒")
    print()

    print("検証:")
    print(f"  確率: {info['prob_both_blue']:.15f}")
    print(f"  正確に1/2: {info['is_exactly_half']}")
    print(f"  数式検証: {info['formula_valid']}")
    print(f"  制約チェック: {total > limit}")


if __name__ == "__main__":
    main()
