#!/usr/bin/env python3
"""
Project Euler Problem 055: Lychrel numbers

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume
that a number is Lychrel until proven otherwise. In addition, you are given that for every number
below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or,
(ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten thousand?
"""

from typing import Any

from .lib import is_palindrome, reverse_number


def is_lychrel_number(n: int, max_iterations: int = 50) -> bool:
    """
    Lychrel数かどうかを判定する
    max_iterations回の反転加算で回文数にならなければLychrel数とする
    時間計算量: O(max_iterations * log n)
    空間計算量: O(1)
    """
    current = n

    for _ in range(max_iterations):
        current = current + reverse_number(current)
        if is_palindrome(current):
            return False

    return True


def solve_naive(limit: int = 10000) -> int:
    """
    素直な解法: 各数値について反転加算プロセスを実行してLychrel数を数える
    時間計算量: O(n * k * log m) where k=50, m=最大数値
    空間計算量: O(1)
    """
    lychrel_count = 0

    for n in range(1, limit):
        if is_lychrel_number(n):
            lychrel_count += 1

    return lychrel_count


def solve_optimized(limit: int = 10000) -> int:
    """
    最適化解法: 早期終了やキャッシュを使った効率化
    時間計算量: O(n * k * log m) - 平均的には改善
    空間計算量: O(1)
    """
    lychrel_count = 0

    for n in range(1, limit):
        current = n
        is_lychrel = True

        # 最初から回文数の場合は特別扱い
        if is_palindrome(n):
            # 回文数でもLychrel数の場合がある（例：4994）
            # 1回でも反転加算して回文数になればLychrel数ではない
            current = n + reverse_number(n)
            if is_palindrome(current):
                is_lychrel = False
            else:
                # 49回の追加試行（最初の1回を除く）
                for _ in range(49):
                    current = current + reverse_number(current)
                    if is_palindrome(current):
                        is_lychrel = False
                        break
        else:
            # 通常の反転加算プロセス
            for _ in range(50):
                current = current + reverse_number(current)
                if is_palindrome(current):
                    is_lychrel = False
                    break

        if is_lychrel:
            lychrel_count += 1

    return lychrel_count


def test_lychrel_examples() -> bool:
    """
    問題で示された例をテストする
    """
    # 47は1回で回文数になる
    if is_lychrel_number(47):
        return False

    # 349は3回で回文数になる
    if is_lychrel_number(349):
        return False

    # 196は理論的にはLychrel数（50回では回文数にならない）
    if not is_lychrel_number(196):
        return False

    # 4994は回文数だがLychrel数
    return is_lychrel_number(4994)


def analyze_number_process(n: int, max_iterations: int = 50) -> dict[str, Any]:
    """
    特定の数値の反転加算プロセスを詳細に分析する
    """
    steps = []
    current = n

    for i in range(max_iterations):
        reversed_num = reverse_number(current)
        next_num = current + reversed_num
        steps.append(
            {
                "iteration": i + 1,
                "current": current,
                "reversed": reversed_num,
                "sum": next_num,
                "is_palindrome": is_palindrome(next_num),
            }
        )

        current = next_num
        if is_palindrome(current):
            return {
                "number": n,
                "is_lychrel": False,
                "iterations_to_palindrome": i + 1,
                "final_palindrome": current,
                "steps": steps,
            }

    return {
        "number": n,
        "is_lychrel": True,
        "iterations_to_palindrome": None,
        "final_palindrome": None,
        "steps": steps,
    }


def get_lychrel_statistics(limit: int = 10000) -> dict[str, Any]:
    """
    Lychrel数の統計情報を取得する
    """
    lychrel_numbers = []
    palindromic_lychrel_numbers = []
    iteration_distribution: dict[int, int] = {}

    for n in range(1, limit):
        if is_lychrel_number(n):
            lychrel_numbers.append(n)
            if is_palindrome(n):
                palindromic_lychrel_numbers.append(n)
        else:
            # 回文数になるまでの反復回数を記録
            analysis = analyze_number_process(n, 50)
            if analysis["iterations_to_palindrome"] is not None:
                iterations = analysis["iterations_to_palindrome"]
                if iterations not in iteration_distribution:
                    iteration_distribution[iterations] = 0
                iteration_distribution[iterations] += 1

    return {
        "total_numbers": limit - 1,
        "lychrel_count": len(lychrel_numbers),
        "lychrel_numbers": lychrel_numbers,
        "palindromic_lychrel_count": len(palindromic_lychrel_numbers),
        "palindromic_lychrel_numbers": palindromic_lychrel_numbers,
        "iteration_distribution": iteration_distribution,
    }
