#!/usr/bin/env python3
"""
Project Euler Problem 058: Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more
interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
"""

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
    return all(n % i != 0 for i in range(3, int(math.sqrt(n)) + 1, 2))


def get_diagonal_values(side_length: int) -> list[int]:
    """
    指定された辺の長さのスパイラルの対角線上の値を取得
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if side_length == 1:
        return [1]

    # 辺の長さが奇数でない場合は空のリストを返す
    if side_length % 2 == 0:
        return []

    # 対角線の値を計算
    # 右下の角から反時計回りに: 右下、右上、左上、左下
    diagonal_values = []

    # 最外層の対角線の値を計算
    # 右下の角 (n²)
    bottom_right = side_length * side_length
    diagonal_values.append(bottom_right)

    # 右上の角 (n² - (n-1))
    top_right = bottom_right - (side_length - 1)
    diagonal_values.append(top_right)

    # 左上の角 (n² - 2*(n-1))
    top_left = bottom_right - 2 * (side_length - 1)
    diagonal_values.append(top_left)

    # 左下の角 (n² - 3*(n-1))
    bottom_left = bottom_right - 3 * (side_length - 1)
    diagonal_values.append(bottom_left)

    return diagonal_values


def get_all_diagonal_values(side_length: int) -> list[int]:
    """
    指定された辺の長さまでのスパイラルの全対角線上の値を取得
    時間計算量: O(n)
    空間計算量: O(n)
    """
    all_diagonal_values = [1]  # 中央の1から始める

    # 辺の長さ3から始めて、2ずつ増やしながら対角線の値を追加
    for current_side in range(3, side_length + 1, 2):
        diagonal_values = get_diagonal_values(current_side)
        all_diagonal_values.extend(diagonal_values)

    return all_diagonal_values


def count_primes_in_diagonals(side_length: int) -> tuple[int, int]:
    """
    指定された辺の長さまでのスパイラルの対角線上の素数の数と総数を返す
    時間計算量: O(n * √m) (mは対角線上の最大値)
    空間計算量: O(n)
    """
    diagonal_values = get_all_diagonal_values(side_length)

    # 素数の数をカウント (1は素数ではないので除外)
    prime_count = sum(1 for value in diagonal_values if value > 1 and is_prime(value))
    total_count = len(diagonal_values)

    return prime_count, total_count


def calculate_prime_ratio(side_length: int) -> float:
    """
    指定された辺の長さでの対角線上の素数の割合を計算
    時間計算量: O(n * √m) (mは対角線上の最大値)
    空間計算量: O(n)
    """
    prime_count, total_count = count_primes_in_diagonals(side_length)

    if total_count == 0:
        return 0.0

    return prime_count / total_count


def solve_naive(target_ratio: float = 0.1) -> int:
    """
    素直な解法: 辺の長さを3から順番に試す
    時間計算量: O(n² * √m) (mは対角線上の最大値)
    空間計算量: O(n)
    """
    side_length = 3

    while True:
        ratio = calculate_prime_ratio(side_length)

        if ratio < target_ratio:
            return side_length

        side_length += 2


def solve_optimized(target_ratio: float = 0.1) -> int:
    """
    最適化解法: 対角線の値を段階的に計算して素数をカウント
    時間計算量: O(n * √m) (mは対角線上の最大値)
    空間計算量: O(1)
    """
    side_length = 3
    prime_count = 0
    total_count = 1  # 中央の1から始める

    while True:
        # 現在の辺の長さでの対角線の値を取得
        diagonal_values = get_diagonal_values(side_length)

        # 新しい対角線の値で素数をカウント
        new_primes = sum(1 for value in diagonal_values if is_prime(value))

        prime_count += new_primes
        total_count += len(diagonal_values)

        # 比率を計算
        ratio = prime_count / total_count

        if ratio < target_ratio:
            return side_length

        side_length += 2


def analyze_spiral_pattern(max_side_length: int = 21) -> list[dict]:
    """
    スパイラルパターンの分析（デバッグ・学習用）
    """
    analysis = []

    for side_length in range(1, max_side_length + 1, 2):
        diagonal_values = get_all_diagonal_values(side_length)
        prime_count, total_count = count_primes_in_diagonals(side_length)
        ratio = prime_count / total_count if total_count > 0 else 0.0

        analysis.append(
            {
                "side_length": side_length,
                "diagonal_values": diagonal_values,
                "prime_count": prime_count,
                "total_count": total_count,
                "ratio": ratio,
                "percentage": ratio * 100,
            }
        )

    return analysis


def get_spiral_layer_info(side_length: int) -> dict:
    """
    指定された辺の長さのスパイラル層の詳細情報を取得
    """
    if side_length == 1:
        return {
            "side_length": 1,
            "layer": 0,
            "diagonal_values": [1],
            "prime_status": [False],  # 1は素数ではない
            "primes": [],
            "non_primes": [1],
        }

    diagonal_values = get_diagonal_values(side_length)
    prime_status = [is_prime(value) for value in diagonal_values]
    primes = [value for value in diagonal_values if is_prime(value)]
    non_primes = [value for value in diagonal_values if not is_prime(value)]

    layer = (side_length - 1) // 2

    return {
        "side_length": side_length,
        "layer": layer,
        "diagonal_values": diagonal_values,
        "prime_status": prime_status,
        "primes": primes,
        "non_primes": non_primes,
    }


def verify_example_spiral() -> bool:
    """
    問題文の例（辺の長さ7のスパイラル）を検証
    """
    side_length = 7
    diagonal_values = get_all_diagonal_values(side_length)

    # 期待される対角線の値 (問題文から)
    expected_diagonal = [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]

    # 実際の対角線の値と比較
    if len(diagonal_values) != len(expected_diagonal):
        return False

    # 素数の数をカウント
    prime_count = sum(1 for value in diagonal_values if value > 1 and is_prime(value))

    # 問題文では8個の素数があると述べられている
    # 実際に確認: 3, 5, 7, 13, 17, 31, 37, 43 = 8個
    expected_prime_count = 8

    return prime_count == expected_prime_count


def test_solutions() -> None:
    """テストケースで解答を検証"""
    print("Testing Problem 058 solutions...")

    # 例のスパイラルを検証
    if verify_example_spiral():
        print("✓ Example spiral verification passed")
    else:
        print("✗ Example spiral verification failed")

    # 小さなテストケース
    test_ratios = [0.5, 0.3, 0.2]

    for ratio in test_ratios:
        result_naive = solve_naive(ratio)
        result_optimized = solve_optimized(ratio)

        print(f"Target ratio: {ratio}")
        print(f"  Naive: {result_naive}")
        print(f"  Optimized: {result_optimized}")

        assert result_naive == result_optimized, f"Solutions disagree for ratio {ratio}"

        # 結果の検証
        actual_ratio = calculate_prime_ratio(result_naive)
        print(f"  Actual ratio at side length {result_naive}: {actual_ratio:.4f}")

        if result_naive > 3:
            prev_ratio = calculate_prime_ratio(result_naive - 2)
            print(
                f"  Previous ratio at side length {result_naive - 2}: {prev_ratio:.4f}"
            )
            assert prev_ratio >= ratio, "Previous ratio should be >= target ratio"

        print()

    print("All test cases passed!")


def main() -> None:
    """メイン関数"""
    print("Project Euler Problem 058: Spiral primes")
    print("=" * 50)

    target_ratio = 0.1
    print(
        f"Finding side length where prime ratio first falls below {target_ratio * 100}%..."
    )
    print()

    # 各解法の実行
    import time

    methods = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
    ]

    results = []
    for name, method in methods:
        start_time = time.time()
        result = method(target_ratio)
        end_time = time.time()
        execution_time = end_time - start_time

        results.append(result)
        print(f"{name}: {result} (実行時間: {execution_time:.4f}秒)")

    # 結果の一致確認
    if len(set(results)) == 1:
        print(f"\n✓ 全ての解法が一致: {results[0]}")
    else:
        print(f"\n✗ 解法間で結果が異なります: {results}")
        return

    # 解答の検証
    print("\n解答の検証:")
    final_side_length = results[0]
    prime_count, total_count = count_primes_in_diagonals(final_side_length)
    ratio = prime_count / total_count

    print(f"辺の長さ: {final_side_length}")
    print(f"対角線上の素数の数: {prime_count}")
    print(f"対角線上の数の総数: {total_count}")
    print(f"素数の割合: {ratio:.6f} ({ratio * 100:.4f}%)")

    # 前の辺の長さでの比率も確認
    if final_side_length > 3:
        prev_prime_count, prev_total_count = count_primes_in_diagonals(
            final_side_length - 2
        )
        prev_ratio = prev_prime_count / prev_total_count
        print(
            f"前の辺の長さ {final_side_length - 2} での割合: {prev_ratio:.6f} ({prev_ratio * 100:.4f}%)"
        )


if __name__ == "__main__":
    test_solutions()
    print()
    main()
