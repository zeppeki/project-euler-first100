"""
Project Euler Problem 85: Counting rectangles
==============================================

長方形グリッド内の部分長方形の数を計算する問題。

例: 3×2のグリッドには18個の長方形が含まれる。

目標: ちょうど200万個に最も近い（ただし完全に一致しない）長方形の数を持つ
     長方形グリッドの面積を見つける。
"""


def count_rectangles(m: int, n: int) -> int:
    """
    m×nのグリッドに含まれる長方形の総数を計算する。

    長方形の数は、左上と右下の2つの頂点を選ぶ組み合わせの数に等しい。
    水平方向にm+1個の線、垂直方向にn+1個の線があるので、
    長方形の数 = C(m+1, 2) * C(n+1, 2) = m(m+1)n(n+1)/4

    Args:
        m: グリッドの幅
        n: グリッドの高さ

    Returns:
        グリッドに含まれる長方形の総数
    """
    return m * (m + 1) * n * (n + 1) // 4


def solve_naive(target: int = 2000000) -> int:
    """
    素直な解法: 全探索でtargetに最も近い長方形数を持つグリッドを見つける。

    時間計算量: O(n²) - 各次元についてnまで探索
    空間計算量: O(1)

    Args:
        target: 目標とする長方形の数（デフォルト: 2,000,000）

    Returns:
        targetに最も近い長方形数を持つグリッドの面積
    """
    best_area = 0
    min_diff = float("inf")

    # 上限を設定: count_rectangles(m, n) = m(m+1)n(n+1)/4
    # 最大値を見積もるために、m ≈ n として m²(m+1)²/4 ≈ target
    # これより m ≈ (4*target)^(1/4) だが、m != n の場合も考慮して余裕を持たせる
    max_size = int((4 * target) ** 0.25) + 30

    for m in range(1, max_size):
        # 各mに対して、長方形数がtargetを超えない最大のnを見つける
        for n in range(1, max_size):
            count = count_rectangles(m, n)
            diff = abs(count - target)

            if diff < min_diff:
                min_diff = diff
                best_area = m * n

            # targetを超えたら次のnでも超えるので終了
            if count > target:
                # ただし、超える直前の値も確認済みなのでbreak可能
                break

    return best_area


def solve_optimized(target: int = 2000000) -> int:
    """
    最適化解法: 二分探索を活用した効率的な探索。

    各mに対して、targetに最も近い長方形数を持つnを二分探索で見つける。

    時間計算量: O(n log n) - n個のmに対してそれぞれO(log n)の二分探索
    空間計算量: O(1)

    Args:
        target: 目標とする長方形の数（デフォルト: 2,000,000）

    Returns:
        targetに最も近い長方形数を持つグリッドの面積
    """
    best_area = 0
    min_diff = float("inf")

    # 上限を設定
    max_size = int((4 * target) ** 0.25) + 30

    for m in range(1, max_size):
        # nの範囲で二分探索: count_rectangles(m, n) ≈ targetとなるnを探す
        left, right = 1, max_size

        while left <= right:
            mid = (left + right) // 2
            count = count_rectangles(m, mid)
            diff = abs(count - target)

            if diff < min_diff:
                min_diff = diff
                best_area = m * mid

            if count < target:
                left = mid + 1
            else:
                right = mid - 1

        # mが大きくなりすぎたら終了
        if count_rectangles(m, 1) > target + min_diff:
            break

    return best_area
