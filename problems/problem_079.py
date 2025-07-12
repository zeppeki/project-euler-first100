#!/usr/bin/env python3
"""
Problem 079: Passcode derivation

A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyze the file so as to determine the shortest possible secret passcode of unknown length.

Answer: Check Project Euler website for verification
"""

from problems.lib.file_io import load_keylog_data
from problems.lib.graph_algorithms import build_dependency_graph, topological_sort


def solve_naive() -> int:
    """
    素直な解法: トポロジカルソートを使った依存関係解析
    時間計算量: O(V + E) where V=digits, E=dependencies
    空間計算量: O(V + E)
    """
    attempts = load_keylog_data("0079_keylog.txt")
    dependencies = build_dependency_graph(attempts)
    passcode_list = topological_sort(dependencies)
    return int("".join(passcode_list))


def solve_optimized() -> int:
    """
    最適化解法: 同じアルゴリズム（最適性を保持）
    時間計算量: O(V + E)
    空間計算量: O(V + E)
    """
    return solve_naive()


def solve_mathematical() -> int:
    """
    数学的解法: グラフ理論ベースの解法（ライブラリ関数使用）
    時間計算量: O(V + E)
    空間計算量: O(V + E)
    """
    attempts = load_keylog_data("0079_keylog.txt")
    dependencies = build_dependency_graph(attempts)
    passcode_list = topological_sort(dependencies, stable_sort=True)
    return int("".join(passcode_list))
