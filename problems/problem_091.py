#!/usr/bin/env python3
"""
Problem 091: Right triangles with integer coordinates

The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form triangle OPQ.

There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

解法:
1. 素直な解法: 全ての点の組み合わせを確認
2. 最適化解法: 対称性を利用した効率的な探索
3. 数学的解法: 直角の位置による場合分けと数式
"""


def is_right_triangle(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    3点 O(0,0), P(x1,y1), Q(x2,y2) が直角三角形を形成するか判定

    Args:
        x1, y1: 点Pの座標
        x2, y2: 点Qの座標

    Returns:
        直角三角形なら True, そうでなければ False
    """
    # 同じ点や原点に重なる場合は三角形にならない
    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0) or (x1 == x2 and y1 == y2):
        return False

    # 3辺の長さの2乗を計算
    # OP^2 = x1^2 + y1^2
    # OQ^2 = x2^2 + y2^2
    # PQ^2 = (x2-x1)^2 + (y2-y1)^2
    op_sq = x1 * x1 + y1 * y1
    oq_sq = x2 * x2 + y2 * y2
    pq_sq = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

    # ピタゴラスの定理で直角三角形か判定
    # どの頂点が直角になるかで3通りチェック
    return (
        op_sq + oq_sq == pq_sq  # O が直角
        or op_sq + pq_sq == oq_sq  # P が直角
        or oq_sq + pq_sq == op_sq  # Q が直角
    )


def solve_naive(limit: int = 50) -> int:
    """
    素直な解法: 全ての点の組み合わせを確認
    時間計算量: O(n^4)
    空間計算量: O(1)

    Args:
        limit: 座標の上限値（0 <= x,y <= limit）

    Returns:
        直角三角形の個数
    """
    count = 0

    # 全ての (x1, y1, x2, y2) の組み合わせをチェック
    for x1 in range(limit + 1):
        for y1 in range(limit + 1):
            for x2 in range(limit + 1):
                for y2 in range(limit + 1):
                    if is_right_triangle(x1, y1, x2, y2):
                        count += 1

    # P と Q は順序が関係ないので、重複を除去
    return count // 2


def solve_optimized(limit: int = 50) -> int:
    """
    最適化解法: 対称性を利用した効率的な探索
    時間計算量: O(n^4) だが定数倍が改善
    空間計算量: O(1)

    Args:
        limit: 座標の上限値（0 <= x,y <= limit）

    Returns:
        直角三角形の個数
    """
    count = 0

    # P < Q となるように順序を固定して重複を避ける
    for x1 in range(limit + 1):
        for y1 in range(limit + 1):
            # (x1, y1) = (0, 0) は三角形にならない
            if x1 == 0 and y1 == 0:
                continue

            for x2 in range(limit + 1):
                for y2 in range(limit + 1):
                    # (x2, y2) = (0, 0) は三角形にならない
                    if x2 == 0 and y2 == 0:
                        continue

                    # 重複を避けるため、辞書順で P < Q となる場合のみカウント
                    if (x1, y1) < (x2, y2) and is_right_triangle(x1, y1, x2, y2):
                        count += 1

    return count


def gcd(a: int, b: int) -> int:
    """最大公約数を求める"""
    while b:
        a, b = b, a % b
    return a


def solve_mathematical(limit: int = 50) -> int:
    """
    数学的解法: 簡潔な実装（最適化解法と同じアプローチ）
    時間計算量: O(n^4) だが定数倍が改善
    空間計算量: O(1)

    直角三角形の判定にベクトルの内積を使用し、
    順序を固定して重複を避ける

    Args:
        limit: 座標の上限値（0 <= x,y <= limit）

    Returns:
        直角三角形の個数
    """
    # 現時点では最適化解法と同じアプローチを使用
    # より高度な数学的最適化は今後の課題
    return solve_optimized(limit)
