#!/usr/bin/env python3
"""
Problem 099: Largest exponential

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult,
as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt, a text file containing one thousand lines with a base/exponent
pair on each line, determine which line has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

import math
import os


def load_base_exp_data(filename: str = "p099_base_exp.txt") -> list[tuple[int, int]]:
    """
    指数データファイルを読み込む
    時間計算量: O(n) where n is number of lines
    空間計算量: O(n)
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(os.path.dirname(current_dir), "data")
    file_path = os.path.join(data_dir, filename)

    base_exp_pairs = []
    with open(file_path) as f:
        for line in f:
            base, exp = map(int, line.strip().split(","))
            base_exp_pairs.append((base, exp))

    return base_exp_pairs


def compare_exponentials_naive(base1: int, exp1: int, base2: int, exp2: int) -> int:
    """
    指数を素直に比較（小さな数のみ対応）
    時間計算量: O(exp) - 指数の大きさに比例
    空間計算量: O(1)
    """
    if base1**exp1 > base2**exp2:
        return 1
    if base1**exp1 < base2**exp2:
        return -1
    return 0


def compare_exponentials_logarithmic(
    base1: int, exp1: int, base2: int, exp2: int
) -> int:
    """
    対数を使って指数を比較
    a^b vs c^d => b*log(a) vs d*log(c)
    時間計算量: O(1)
    空間計算量: O(1)
    """
    # log(a^b) = b * log(a)
    log_val1 = exp1 * math.log(base1)
    log_val2 = exp2 * math.log(base2)

    if log_val1 > log_val2:
        return 1
    if log_val1 < log_val2:
        return -1
    return 0


def solve_naive(filename: str = "p099_base_exp.txt") -> int:
    """
    素直な解法: 小さな指数のみ直接比較可能
    注意: 大きな指数では実用的でない
    時間計算量: O(n * max_exp) where n is number of pairs
    空間計算量: O(n)
    """
    base_exp_pairs = load_base_exp_data(filename)

    if not base_exp_pairs:
        return 0

    max_line = 1
    max_base, max_exp = base_exp_pairs[0]

    # 小さな指数の場合のみ直接比較
    for i, (base, exp) in enumerate(base_exp_pairs[1:], 2):
        # 指数が大きすぎる場合は対数比較にフォールバック
        if exp > 1000 or max_exp > 1000:
            if compare_exponentials_logarithmic(base, exp, max_base, max_exp) > 0:
                max_line = i
                max_base, max_exp = base, exp
        else:
            if compare_exponentials_naive(base, exp, max_base, max_exp) > 0:
                max_line = i
                max_base, max_exp = base, exp

    return max_line


def solve_optimized(filename: str = "p099_base_exp.txt") -> int:
    """
    最適化解法: 対数を使った効率的な比較
    時間計算量: O(n) where n is number of pairs
    空間計算量: O(n)
    """
    base_exp_pairs = load_base_exp_data(filename)

    if not base_exp_pairs:
        return 0

    max_line = 1
    max_log_value = 0.0

    for i, (base, exp) in enumerate(base_exp_pairs, 1):
        # log(base^exp) = exp * log(base)
        log_value = exp * math.log(base)

        if log_value > max_log_value:
            max_log_value = log_value
            max_line = i

    return max_line


def solve_mathematical(filename: str = "p099_base_exp.txt") -> int:
    """
    数学的解法: 対数の性質を利用した最適化
    log(a^b) = b * log(a) の性質を利用
    時間計算量: O(n)
    空間計算量: O(1) - ストリーミング処理
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(os.path.dirname(current_dir), "data")
    file_path = os.path.join(data_dir, filename)

    max_line = 1
    max_log_value = 0.0

    with open(file_path) as f:
        for line_num, line in enumerate(f, 1):
            base, exp = map(int, line.strip().split(","))

            # 数学的性質: log(a^b) = b * log(a)
            log_value = exp * math.log(base)

            if log_value > max_log_value:
                max_log_value = log_value
                max_line = line_num

    return max_line


def get_exponential_info(base: int, exp: int) -> dict:
    """
    指数の情報を取得（デバッグ・解析用）
    """
    log_value = exp * math.log(base)
    estimated_digits = int(log_value / math.log(10)) + 1

    return {
        "base": base,
        "exponent": exp,
        "log_value": log_value,
        "estimated_digits": estimated_digits,
        "base_log": math.log(base),
        "natural_log": log_value,
    }


def main() -> None:
    """メイン実行関数"""
    print("Problem 099: Largest exponential")
    print("=" * 40)

    # Load and analyze data
    base_exp_pairs = load_base_exp_data()
    print(f"Loaded {len(base_exp_pairs)} base-exponent pairs")

    # Show some examples
    print("\nFirst 5 pairs:")
    for i, (base, exp) in enumerate(base_exp_pairs[:5], 1):
        info = get_exponential_info(base, exp)
        print(f"  Line {i}: {base}^{exp} (~{info['estimated_digits']} digits)")

    # Compare solution approaches
    print("\nSolving...")

    import time

    # Test optimized solution
    start_time = time.time()
    result_optimized = solve_optimized()
    end_time = time.time()

    print(f"Optimized solution: Line {result_optimized}")
    print(f"Computation time: {end_time - start_time:.6f}s")

    # Show details of the largest exponential
    if result_optimized > 0:
        base, exp = base_exp_pairs[result_optimized - 1]
        info = get_exponential_info(base, exp)
        print("\nLargest exponential:")
        print(f"  Line {result_optimized}: {base}^{exp}")
        print(f"  Estimated digits: {info['estimated_digits']:,}")
        print(f"  Log value: {info['log_value']:.6f}")

    # Show comparison with nearby values
    print("\nComparison with nearby lines:")
    for offset in [-2, -1, 0, 1, 2]:
        line_idx = result_optimized - 1 + offset
        if 0 <= line_idx < len(base_exp_pairs):
            base, exp = base_exp_pairs[line_idx]
            info = get_exponential_info(base, exp)
            marker = " <-- LARGEST" if offset == 0 else ""
            print(
                f"  Line {line_idx + 1}: {base}^{exp} "
                f"(log={info['log_value']:.6f}){marker}"
            )


if __name__ == "__main__":
    main()
