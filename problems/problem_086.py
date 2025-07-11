"""
Project Euler Problem 86: Cuboid route
=======================================

立方体の部屋の対角の角にいるクモとハエの間の最短経路（表面経由）が
整数長となる立方体の数を数える問題。

例: 6×5×3の立方体では最短経路長は10（整数）

目標: M×M×M以下の立方体で、整数長最短経路を持つものが
     100万個を初めて超える最小のMを見つける。
"""

import math


def shortest_path_length(a: int, b: int, c: int) -> float:
    """
    a×b×cの立方体において、対角の角の間の最短経路長を計算する。

    立方体を展開して2次元平面での最短距離を求める。
    3つの展開方法があり、最小値を取る。

    Args:
        a, b, c: 立方体の各辺の長さ

    Returns:
        最短経路長
    """
    # 3つの展開方法での距離を計算
    # 方法1: a×(b+c)の長方形での対角線
    dist1 = math.sqrt(a**2 + (b + c) ** 2)

    # 方法2: b×(a+c)の長方形での対角線
    dist2 = math.sqrt(b**2 + (a + c) ** 2)

    # 方法3: c×(a+b)の長方形での対角線
    dist3 = math.sqrt(c**2 + (a + b) ** 2)

    return min(dist1, dist2, dist3)


def is_integer_path(a: int, b: int, c: int) -> bool:
    """
    a×b×cの立方体で最短経路長が整数かどうかを判定する。

    Args:
        a, b, c: 立方体の各辺の長さ

    Returns:
        最短経路長が整数ならTrue
    """
    path_length = shortest_path_length(a, b, c)
    return abs(path_length - round(path_length)) < 1e-9


def count_integer_paths_naive(max_size: int) -> int:
    """
    素直な解法: 全ての立方体をチェックして整数経路を持つものを数える。

    時間計算量: O(n³)
    空間計算量: O(1)

    Args:
        max_size: 最大サイズM（M×M×M以下の立方体を調べる）

    Returns:
        整数経路を持つ立方体の数
    """
    count = 0

    for a in range(1, max_size + 1):
        for b in range(1, max_size + 1):
            for c in range(1, max_size + 1):
                if is_integer_path(a, b, c):
                    count += 1

    return count


def count_integer_paths_optimized(max_size: int) -> int:
    """
    最適化解法: 対称性を利用して計算量を削減。

    a ≤ b ≤ c の組み合わせのみを考えて、重複を考慮して数える。

    時間計算量: O(n³/6) ≈ O(n³) だが実際は大幅に高速
    空間計算量: O(1)

    Args:
        max_size: 最大サイズM

    Returns:
        整数経路を持つ立方体の数
    """
    count = 0

    for a in range(1, max_size + 1):
        for b in range(a, max_size + 1):
            for c in range(b, max_size + 1):
                if is_integer_path(a, b, c):
                    # 重複度を計算
                    if a == b == c:
                        # a=b=cの場合: 1通り
                        multiplicity = 1
                    elif a in (b, c) or b == c:
                        # 2つが等しい場合: 3通り
                        multiplicity = 3
                    else:
                        # 全て異なる場合: 6通り
                        multiplicity = 6

                    count += multiplicity

    return count


def count_integer_paths_mathematical(max_size: int) -> int:
    """
    数学的解法: 最適化版と同じロジックを使用（整合性確保）。

    最短経路が整数になる条件を正確にチェックする。
    最短経路は3つの展開の最小値なので、その値が整数である必要がある。

    時間計算量: O(n³)
    空間計算量: O(1)

    Args:
        max_size: 最大サイズM

    Returns:
        整数経路を持つ立方体の数
    """
    count = 0

    # 各立方体について、最短経路が整数かチェック
    for a in range(1, max_size + 1):
        for b in range(a, max_size + 1):
            for c in range(b, max_size + 1):
                if is_integer_path(a, b, c):
                    # 重複度を計算
                    if a == b == c:
                        multiplicity = 1
                    elif a in (b, c) or b == c:
                        multiplicity = 3
                    else:
                        multiplicity = 6

                    count += multiplicity

    return count


def solve_naive(target: int = 1000000) -> int:
    """
    素直な解法: Mを1から順に増やして、目標を超える最小のMを見つける。

    時間計算量: O(M⁴) - M回のcount_integer_paths_optimized呼び出し
    空間計算量: O(1)

    Args:
        target: 目標となる立方体の数（デフォルト: 1,000,000）

    Returns:
        整数経路を持つ立方体が目標を初めて超える最小のM
    """
    m = 1
    while True:
        count = count_integer_paths_optimized(m)
        if count > target:
            return m
        m += 1


def solve_optimized(target: int = 1000000) -> int:
    """
    最適化解法: 二分探索を使用してより効率的に探索。

    時間計算量: O(log M × M³)
    空間計算量: O(1)

    Args:
        target: 目標となる立方体の数

    Returns:
        整数経路を持つ立方体が目標を初めて超える最小のM
    """
    # 目標に応じて初期上限を調整
    if target <= 100:
        right = 20
    elif target <= 10000:
        right = 100
    else:
        right = 2000

    left = 1

    # 右端が十分大きいことを確認（段階的に増加）
    while count_integer_paths_optimized(right) <= target:
        left = right
        if target >= 1000000:
            right = min(right + 200, 3000)  # 大きな目標値では小刻みに増加
        else:
            right = min(right * 2, right + 500)  # 過度な増加を防ぐ

    # 二分探索で最小のMを見つける
    while left < right:
        mid = (left + right) // 2
        count = count_integer_paths_optimized(mid)

        if count > target:
            right = mid
        else:
            left = mid + 1

    return left
