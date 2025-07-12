"""
動的計画法関連のユーティリティ関数

Project Euler問題で使用される動的計画法のアルゴリズムを提供する。
主に三角形の最大パス問題、メモ化、最適化問題を含む。

抽出元:
- Problem 067: 三角形の最大パス合計（動的計画法）
- Problem 018: 三角形の最大パス問題
- Problem 031: コイン問題（動的計画法）
- Problem 076: 整数分割（動的計画法）
"""

from collections.abc import Callable
from typing import Any


def parse_triangle(triangle_str: str) -> list[list[int]]:
    """
    三角形の文字列表現を数値の二次元リストに変換

    Args:
        triangle_str: 三角形の文字列表現（行区切り、空白区切りの数値）

    Returns:
        数値の二次元リスト

    時間計算量: O(n²) where n=三角形の行数
    空間計算量: O(n²)

    Examples:
        >>> triangle_str = "3\n7 4\n2 4 6\n8 5 9 3"
        >>> parse_triangle(triangle_str)
        [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    """
    lines = triangle_str.strip().split("\n")
    triangle = []

    for line in lines:
        if line.strip():  # 空行をスキップ
            row = [int(x) for x in line.split()]
            triangle.append(row)

    return triangle


def max_path_sum_triangle(triangle: list[list[int]], minimize: bool = False) -> int:
    """
    三角形の最大（または最小）パス合計を動的計画法で計算

    上から下へ移動し、隣接する要素にのみ移動可能。

    Args:
        triangle: 三角形の数値配列
        minimize: Trueの場合は最小パス、Falseの場合は最大パス

    Returns:
        最大（または最小）パス合計

    時間計算量: O(n²)
    空間計算量: O(n)

    Examples:
        >>> triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        >>> max_path_sum_triangle(triangle)
        23
    """
    if not triangle or not triangle[0]:
        return 0

    n = len(triangle)

    # 最後の行をコピーして初期化
    dp = triangle[-1][:]

    # 下から上へ計算
    for row in range(n - 2, -1, -1):
        for col in range(len(triangle[row])):
            # 下の2つの要素のうち最適値を選択
            left_child = dp[col]
            right_child = dp[col + 1]

            if minimize:
                optimal_child = min(left_child, right_child)
            else:
                optimal_child = max(left_child, right_child)

            dp[col] = triangle[row][col] + optimal_child

    return dp[0]


def min_path_sum_matrix(
    matrix: list[list[int]], directions: list[tuple[int, int]] | None = None
) -> int:
    """
    行列の最小パス合計を動的計画法で計算

    Args:
        matrix: 数値の二次元配列
        directions: 移動可能方向 [(dr, dc), ...]
                   Noneの場合は右と下のみ

    Returns:
        左上から右下への最小パス合計

    時間計算量: O(m×n) for 2方向, O(m×n×d) for d方向
    空間計算量: O(m×n)

    Examples:
        >>> matrix = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        >>> min_path_sum_matrix(matrix)
        7
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    if directions is None:
        # 右と下のみの移動（高速版）
        dp = [[float("inf")] * cols for _ in range(rows)]
        dp[0][0] = matrix[0][0]

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue

                # 上から来る場合
                if row > 0:
                    dp[row][col] = min(
                        dp[row][col], dp[row - 1][col] + matrix[row][col]
                    )

                # 左から来る場合
                if col > 0:
                    dp[row][col] = min(
                        dp[row][col], dp[row][col - 1] + matrix[row][col]
                    )

        result = dp[rows - 1][cols - 1]
        return int(result) if result != float("inf") else 0

    # 任意方向の移動（汎用版）
    # 注意: この場合はDijkstra法を使用することを推奨
    from .graph_algorithms import dijkstra_shortest_path

    distance, _ = dijkstra_shortest_path(
        matrix, (0, 0), (rows - 1, cols - 1), directions
    )
    return int(distance) if distance != float("inf") else 0


def coin_change_ways(amount: int, coins: list[int]) -> int:
    """
    指定金額を硬貨で支払う方法の数を計算（動的計画法）

    Args:
        amount: 目標金額
        coins: 使用可能な硬貨の額面リスト

    Returns:
        支払い方法の数

    時間計算量: O(amount × len(coins))
    空間計算量: O(amount)

    Examples:
        >>> coin_change_ways(4, [1, 2, 3])
        4  # 1+1+1+1, 1+1+2, 2+2, 1+3
    """
    dp = [0] * (amount + 1)
    dp[0] = 1  # 金額0は1通り（何も取らない）

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


def partition_count(n: int) -> int:
    """
    整数nの分割数を計算（動的計画法）

    Args:
        n: 分割する整数

    Returns:
        分割方法の数

    時間計算量: O(n²)
    空間計算量: O(n)

    Examples:
        >>> partition_count(4)
        5  # 4, 3+1, 2+2, 2+1+1, 1+1+1+1
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]


def longest_increasing_subsequence(sequence: list[int]) -> int:
    """
    最長増加部分列の長さを計算（動的計画法）

    Args:
        sequence: 整数のシーケンス

    Returns:
        最長増加部分列の長さ

    時間計算量: O(n log n)
    空間計算量: O(n)

    Examples:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4  # [2, 3, 7, 18]
    """
    if not sequence:
        return 0

    from bisect import bisect_left

    # tails[i] = 長さi+1のLISの末尾要素の最小値
    tails: list[int] = []

    for num in sequence:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


class Memoization:
    """
    メモ化のためのデコレータクラス

    関数の結果をキャッシュして再計算を避ける。
    lru_cache のカスタム版で、より詳細な制御が可能。
    """

    def __init__(self, maxsize: int = 128):
        self.maxsize = maxsize
        self.cache: dict[Any, Any] = {}
        self.calls = 0
        self.hits = 0

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            self.calls += 1
            key = (args, tuple(sorted(kwargs.items())))

            if key in self.cache:
                self.hits += 1
                return self.cache[key]

            result = func(*args, **kwargs)

            if len(self.cache) < self.maxsize:
                self.cache[key] = result

            return result

        # Add cache management methods for compatibility with functools.lru_cache
        def cache_info_func() -> dict[str, int]:
            return {
                "hits": self.hits,
                "calls": self.calls,
                "cache_size": len(self.cache),
                "maxsize": self.maxsize,
            }

        def cache_clear_func() -> None:
            self.cache.clear()

        # Add dynamic attributes with type ignore for mypy
        wrapper.cache_info = cache_info_func  # type: ignore[attr-defined]
        wrapper.cache_clear = cache_clear_func  # type: ignore[attr-defined]

        return wrapper


def fibonacci_dp(n: int) -> int:
    """
    フィボナッチ数を動的計画法で計算（高速版）

    Args:
        n: フィボナッチ数のインデックス

    Returns:
        n番目のフィボナッチ数

    時間計算量: O(n)
    空間計算量: O(1)

    Examples:
        >>> fibonacci_dp(10)
        55
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def edit_distance(str1: str, str2: str) -> int:
    """
    2つの文字列間の編集距離（レーベンシュタイン距離）を計算

    Args:
        str1: 第1の文字列
        str2: 第2の文字列

    Returns:
        編集距離（挿入、削除、置換の最小回数）

    時間計算量: O(m×n) where m=len(str1), n=len(str2)
    空間計算量: O(m×n)

    Examples:
        >>> edit_distance("kitten", "sitting")
        3
    """
    m, n = len(str1), len(str2)

    # dp[i][j] = str1[:i] と str2[:j] の編集距離
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初期化
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # DP表を埋める
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 文字が同じ場合
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # 削除
                    dp[i][j - 1],  # 挿入
                    dp[i - 1][j - 1],  # 置換
                )

    return dp[m][n]


def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """
    0-1ナップサック問題を動的計画法で解く

    Args:
        weights: 各アイテムの重さリスト
        values: 各アイテムの価値リスト
        capacity: ナップサックの容量

    Returns:
        最大価値

    時間計算量: O(n×capacity) where n=アイテム数
    空間計算量: O(capacity)

    Examples:
        >>> knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7)
        9
    """
    n = len(weights)

    # dp[w] = 重さwまでで得られる最大価値
    dp = [0] * (capacity + 1)

    for i in range(n):
        # 逆順に更新（同じアイテムを複数回選ばないため）
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
