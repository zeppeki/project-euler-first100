#!/usr/bin/env python3
"""
Problem 019: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September, April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap-years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

Answer: 171
"""

import time
from datetime import datetime


def is_leap_year(year: int) -> bool:
    """
    うるう年判定

    Args:
        year: 判定対象の年

    Returns:
        うるう年の場合True
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def days_in_month(year: int, month: int) -> int:
    """
    指定年月の日数を取得

    Args:
        year: 年
        month: 月 (1-12)

    Returns:
        その月の日数
    """
    if month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    if month == 2:  # February
        return 29 if is_leap_year(year) else 28
    # January, March, May, July, August, October, December
    return 31


def solve_naive(start_year: int, end_year: int) -> int:
    """
    素直な解法: 日付を順次カウントして日曜日を数える

    時間計算量: O(n) - nは日数
    空間計算量: O(1)

    Args:
        start_year: 開始年（含む）
        end_year: 終了年（含む）

    Returns:
        月の初日が日曜日だった回数
    """
    # 1900年1月1日は月曜日（0=月曜日, 6=日曜日）
    current_day_of_week = 0  # Monday
    sundays_count = 0

    # 1900年から start_year の直前まで進める
    for year in range(1900, start_year):
        for month in range(1, 13):
            days = days_in_month(year, month)
            current_day_of_week = (current_day_of_week + days) % 7

    # start_year から end_year まで
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # 月の初日が日曜日かチェック
            if current_day_of_week == 6:  # Sunday
                sundays_count += 1

            # 次の月の初日へ移動
            days = days_in_month(year, month)
            current_day_of_week = (current_day_of_week + days) % 7

    return sundays_count


def solve_optimized(start_year: int, end_year: int) -> int:
    """
    最適化解法: Zellerの公式を使用した日付計算

    時間計算量: O(n) - nは月数
    空間計算量: O(1)

    Args:
        start_year: 開始年（含む）
        end_year: 終了年（含む）

    Returns:
        月の初日が日曜日だった回数
    """

    def zeller_day_of_week(year: int, month: int, day: int) -> int:
        """
        Zellerの公式で曜日を計算

        Returns:
            0=土曜日, 1=日曜日, 2=月曜日, ..., 6=金曜日
        """
        if month < 3:
            month += 12
            year -= 1

        k = year % 100
        j = year // 100

        return (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - 2 * j) % 7

    sundays_count = 0

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # 各月の1日が日曜日かチェック
            day_of_week = zeller_day_of_week(year, month, 1)
            if day_of_week == 1:  # Sunday in Zeller's formula
                sundays_count += 1

    return sundays_count


def solve_mathematical(start_year: int, end_year: int) -> int:
    """
    数学的解法: Python datetimeモジュールを使用

    時間計算量: O(n) - nは月数
    空間計算量: O(1)

    Args:
        start_year: 開始年（含む）
        end_year: 終了年（含む）

    Returns:
        月の初日が日曜日だった回数
    """
    sundays_count = 0

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # Python datetimeで月の初日の曜日を取得
            date = datetime(year, month, 1)
            if date.weekday() == 6:  # Sunday (Monday=0, Sunday=6)
                sundays_count += 1

    return sundays_count


def validate_leap_year_calculation() -> None:
    """うるう年計算の検証"""
    test_cases = [
        (1900, False),  # 世紀年で400で割り切れない
        (2000, True),  # 世紀年で400で割り切れる
        (1996, True),  # 4で割り切れる
        (1997, False),  # 4で割り切れない
        (1800, False),  # 世紀年で400で割り切れない
        (2004, True),  # 4で割り切れる
    ]

    print("=== うるう年判定テスト ===")
    for year, expected in test_cases:
        result = is_leap_year(year)
        print(f"{year}: {result} {'✓' if result == expected else '✗'}")
    print()


def validate_days_in_month_calculation() -> None:
    """月の日数計算の検証"""
    print("=== 月の日数テスト ===")

    # 平年の月日数
    for month in range(1, 13):
        days = days_in_month(1997, month)  # 1997は平年
        expected = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
        print(f"1997年{month}月: {days}日 {'✓' if days == expected else '✗'}")

    # うるう年の2月
    print(
        f"2000年2月: {days_in_month(2000, 2)}日 {'✓' if days_in_month(2000, 2) == 29 else '✗'}"
    )
    print(
        f"1900年2月: {days_in_month(1900, 2)}日 {'✓' if days_in_month(1900, 2) == 28 else '✗'}"
    )
    print()


def test_solutions() -> None:
    """テストケースで解答を検証"""
    print("=== 基本検証 ===")
    validate_leap_year_calculation()
    validate_days_in_month_calculation()

    # 小さな範囲でのテスト
    print("=== 小範囲テスト ===")
    test_ranges = [
        (1901, 1901),  # 1年だけ
        (1901, 1905),  # 5年
        (1901, 1910),  # 10年
    ]

    for start, end in test_ranges:
        result_naive = solve_naive(start, end)
        result_optimized = solve_optimized(start, end)
        result_math = solve_mathematical(start, end)

        print(f"{start}-{end}年の月初日曜日数:")
        print(f"  Naive: {result_naive}")
        print(
            f"  Optimized: {result_optimized} {'✓' if result_optimized == result_naive else '✗'}"
        )
        print(
            f"  Mathematical: {result_math} {'✓' if result_math == result_naive else '✗'}"
        )
        print()


def main() -> None:
    """メイン関数"""
    # テストケース
    test_solutions()

    # 本問題の解答
    print("=== 本問題の解答 ===")
    start_year, end_year = 1901, 2000

    # 各解法の実行時間測定
    start_time = time.time()
    result_naive = solve_naive(start_year, end_year)
    naive_time = time.time() - start_time

    start_time = time.time()
    result_optimized = solve_optimized(start_year, end_year)
    optimized_time = time.time() - start_time

    start_time = time.time()
    result_math = solve_mathematical(start_year, end_year)
    math_time = time.time() - start_time

    print(f"{start_year}-{end_year}年の月初日曜日数:")
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
    print(f"素直な解法: {naive_time / fastest_time:.2f}x")
    print(f"最適化解法: {optimized_time / fastest_time:.2f}x")
    print(f"数学的解法: {math_time / fastest_time:.2f}x")

    # 追加情報
    print("\n=== アルゴリズム解説 ===")
    print("1. 素直な解法: 日付を順次カウントして曜日を追跡")
    print("2. 最適化解法: Zellerの公式を使用した直接計算")
    print("3. 数学的解法: Python datetimeモジュールを活用")
    print()
    print("日付計算の要点:")
    print("- うるう年の正確な判定（400年ルール）")
    print("- 各月の日数の正確な計算")
    print("- 曜日計算の効率的な実装")

    # 検証情報
    print("\n=== 検証情報 ===")
    print("基準日: 1900年1月1日は月曜日")
    print("対象期間: 1901年1月1日〜2000年12月31日")
    print("計算対象: 各月の1日が日曜日だった回数")
    print(f"総月数: {(end_year - start_year + 1) * 12} ヶ月")


if __name__ == "__main__":
    main()
