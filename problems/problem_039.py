#!/usr/bin/env python3
"""
Problem 039: Integer right triangles

If p is the perimeter of a right triangle with integral sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000 is the number of solutions maximised?

Answer: 840
"""

import math


def solve_naive(max_perimeter: int) -> int:
    """
    素直な解法: 全ての(a,b,c)の組み合わせを調べる
    時間計算量: O(n³)
    空間計算量: O(n)
    """
    if max_perimeter <= 0:
        return 0

    solution_counts = [0] * (max_perimeter + 1)

    # 全ての可能な組み合わせを調べる
    for a in range(1, max_perimeter // 3):  # a < b < c なので a は最大でも p/3
        for b in range(a + 1, max_perimeter // 2):  # b は最大でも p/2
            c_squared = a * a + b * b
            c = int(math.sqrt(c_squared))

            # cが整数で、かつ直角三角形の条件を満たすかチェック
            if c * c == c_squared:
                perimeter = a + b + c
                if perimeter <= max_perimeter:
                    solution_counts[perimeter] += 1

    # 解の数が最大となる周囲を見つける
    max_solutions = max(solution_counts)
    if max_solutions == 0:
        return 0
    return solution_counts.index(max_solutions)


def solve_optimized(max_perimeter: int) -> int:
    """
    最適化解法: a ≤ b < c の制約を使って効率化
    時間計算量: O(n²)
    空間計算量: O(n)
    """
    if max_perimeter <= 0:
        return 0

    solution_counts = [0] * (max_perimeter + 1)

    # a ≤ b < c の制約を使って探索範囲を制限
    for a in range(1, max_perimeter // 3 + 1):
        for b in range(a, (max_perimeter - a) // 2 + 1):
            c_squared = a * a + b * b
            c = int(math.sqrt(c_squared))

            # 直角三角形の条件をチェック
            if c * c == c_squared and c > b:
                perimeter = a + b + c
                if perimeter <= max_perimeter:
                    solution_counts[perimeter] += 1

    # 解の数が最大となる周囲を見つける
    max_solutions = max(solution_counts)
    if max_solutions == 0:
        return 0
    return solution_counts.index(max_solutions)


def solve_mathematical(max_perimeter: int) -> int:
    """
    数学的解法: ピタゴラス数の公式を使用
    時間計算量: O(n√n)
    空間計算量: O(n)

    ピタゴラス数の基本形:
    a = k(m² - n²), b = k(2mn), c = k(m² + n²)
    ここで m > n > 0, gcd(m,n) = 1, m,n のうち一方は偶数
    """
    if max_perimeter <= 0:
        return 0

    solution_counts = [0] * (max_perimeter + 1)

    # ピタゴラス数の公式を使って全ての組み合わせを生成
    m = 2
    while m * m <= max_perimeter:
        for n in range(1, m):
            # gcd(m,n) = 1 かつ m,nのうち一方は偶数
            if math.gcd(m, n) == 1 and (m % 2 != n % 2):
                # 基本ピタゴラス数を生成
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n

                # a ≤ b になるように調整
                if a > b:
                    a, b = b, a

                base_perimeter = a + b + c

                # 倍数を含めて全ての解を生成
                k = 1
                while k * base_perimeter <= max_perimeter:
                    perimeter = k * base_perimeter
                    solution_counts[perimeter] += 1
                    k += 1
        m += 1

    # 解の数が最大となる周囲を見つける
    max_solutions = max(solution_counts)
    if max_solutions == 0:
        return 0
    return solution_counts.index(max_solutions)


def count_solutions(perimeter: int) -> int:
    """
    指定された周囲の長さで直角三角形の解の数を計算
    """
    if perimeter <= 0:
        return 0

    count = 0
    for a in range(1, perimeter // 3 + 1):
        for b in range(a, (perimeter - a) // 2 + 1):
            c = perimeter - a - b
            if c > 0 and a * a + b * b == c * c:
                count += 1

    return count


def get_solutions(perimeter: int) -> list[tuple[int, int, int]]:
    """
    指定された周囲の長さで直角三角形の解を全て取得
    """
    if perimeter <= 0:
        return []

    solutions = []
    for a in range(1, perimeter // 3 + 1):
        for b in range(a, (perimeter - a) // 2 + 1):
            c = perimeter - a - b
            if c > 0 and a * a + b * b == c * c:
                solutions.append((a, b, c))

    return solutions


def test_solutions() -> None:
    """テストケースで解答を検証"""
    # 例題: p = 120 の場合、解は3つ
    assert count_solutions(120) == 3
    solutions_120 = get_solutions(120)
    expected_120 = [(20, 48, 52), (24, 45, 51), (30, 40, 50)]
    assert sorted(solutions_120) == sorted(expected_120)

    # 小さな値でのテスト
    assert count_solutions(12) == 1  # (3,4,5)
    assert get_solutions(12) == [(3, 4, 5)]

    # 境界ケース
    assert count_solutions(0) == 0
    assert count_solutions(1) == 0
    assert count_solutions(2) == 0

    # 解答が一致することを確認
    result_naive = solve_naive(120)
    result_optimized = solve_optimized(120)
    result_mathematical = solve_mathematical(120)

    assert result_naive == result_optimized == result_mathematical

    print("✓ 全てのテストケースが成功しました")


def main() -> None:
    """メイン関数"""
    print("Problem 039: Integer right triangles")
    print("=" * 50)

    limit = 1000

    # 各解法の実行
    print(f"\n周囲の長さが{limit}以下で解の数が最大となる値を求めます...")

    result_naive = solve_naive(limit)
    print(f"素直な解法: {result_naive}")

    result_optimized = solve_optimized(limit)
    print(f"最適化解法: {result_optimized}")

    result_mathematical = solve_mathematical(limit)
    print(f"数学的解法: {result_mathematical}")

    # 解答の確認
    if result_naive == result_optimized == result_mathematical:
        print(f"\n✓ 全ての解法が一致: {result_naive}")
        print(f"p = {result_naive} での解の数: {count_solutions(result_naive)}")

        solutions = get_solutions(result_naive)
        print(f"解の例 (最初の5つ): {solutions[:5]}")
    else:
        print("✗ 解法間で結果が一致しません")


if __name__ == "__main__":
    test_solutions()
    main()
