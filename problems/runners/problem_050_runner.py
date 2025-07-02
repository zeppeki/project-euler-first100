#!/usr/bin/env python3
"""
Runner for Problem 050: Consecutive prime sum

This module provides a runner for executing and testing Problem 050 solutions.
"""

import time
from collections.abc import Callable

from problems.problem_050 import solve_mathematical, solve_naive, solve_optimized


def run_solution(func: Callable[[], int], name: str) -> tuple[int, float]:
    """
    指定された解法を実行し、結果と実行時間を返す

    Args:
        func: 実行する関数
        name: 解法の名前

    Returns:
        結果と実行時間のタプル
    """
    print(f"\n{name}を実行中...")
    start_time = time.time()
    result = func()
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"結果: {result}")
    print(f"実行時間: {execution_time:.6f}秒")

    return result, execution_time


def run_all_solutions() -> dict[str, tuple[int, float]]:
    """
    全ての解法を実行し、結果を比較する

    Returns:
        各解法の結果と実行時間の辞書
    """
    print("Problem 050: Consecutive prime sum")
    print("=" * 50)

    results = {}

    # 各解法の実行
    solutions = [
        (solve_naive, "素直な解法"),
        (solve_optimized, "最適化解法"),
        (solve_mathematical, "数学的解法"),
    ]

    for func, name in solutions:
        result, exec_time = run_solution(func, name)
        results[name] = (result, exec_time)

    # 結果の検証
    print("\n" + "=" * 50)
    print("結果の検証:")

    all_results = [result for result, _ in results.values()]
    if len(set(all_results)) == 1:
        print("✓ 全ての解法で同じ結果が得られました")
        print(f"答え: {all_results[0]}")
    else:
        print("✗ 解法間で結果が異なります")
        for name, (result, _) in results.items():
            print(f"  {name}: {result}")

    # 性能比較
    print("\n性能比較:")
    sorted_results = sorted(results.items(), key=lambda x: x[1][1])
    fastest_time = sorted_results[0][1][1]

    for name, (_result, exec_time) in sorted_results:
        if exec_time > 0:
            speedup = exec_time / fastest_time
            print(f"  {name}: {exec_time:.6f}秒 (基準の{speedup:.2f}倍)")
        else:
            print(f"  {name}: {exec_time:.6f}秒")

    return results


def validate_solution() -> bool:
    """
    解法の正当性を検証する

    Returns:
        検証結果
    """
    print("解法の検証を実行中...")

    try:
        # 小さい値での検証
        test_limit = 100

        # 各解法をテスト
        result_naive = solve_naive(test_limit)
        result_optimized = solve_optimized(test_limit)
        result_mathematical = solve_mathematical(test_limit)

        # 期待値（問題文から）
        expected = 41  # 41 = 2 + 3 + 5 + 7 + 11 + 13 (6つの連続する素数の和)

        if result_naive == result_optimized == result_mathematical == expected:
            print(f"✓ 検証成功: 全解法が期待値 {expected} を返しました")
            return True
        print("✗ 検証失敗:")
        print(f"  期待値: {expected}")
        print(f"  素直な解法: {result_naive}")
        print(f"  最適化解法: {result_optimized}")
        print(f"  数学的解法: {result_mathematical}")
        return False

    except Exception as e:
        print(f"✗ 検証中にエラーが発生しました: {e}")
        return False


def main() -> None:
    """メイン関数"""
    # 検証の実行
    if not validate_solution():
        print("検証に失敗しました。実装を確認してください。")
        return

    print("\n" + "=" * 50)

    # 全解法の実行
    results = run_all_solutions()

    # 最終結果の表示
    print(f"\n最終結果: {next(iter(results.values()))[0]}")


if __name__ == "__main__":
    main()
