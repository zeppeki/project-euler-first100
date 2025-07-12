"""
データ構造関連のユーティリティ関数

Project Euler問題で頻繁に使用されるデータ構造操作と共通パターンを提供する。
主にグループ化、集合操作、優先度付きキュー、カウント処理を含む。

抽出元:
- Problem 021: 友愛数の集合管理
- Problem 023: 豊富数判定の集合操作
- Problem 027: 素数集合の高速検索
- Problem 029: 重複除去とユニークな項の管理
- Problem 054: カード/ポーカー手の構造化データ
- Problem 062: 桁署名によるグループ化
- Problem 084: モノポリー統計のカウント処理
- Problem 098: アナグラムのグループ化
"""

import heapq
from collections import Counter, defaultdict
from collections.abc import Callable
from typing import Any, Generic, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def group_by(items: list[T], key_func: Callable[[T], K]) -> dict[K, list[T]]:
    """
    要素をキー関数でグループ化する

    Args:
        items: グループ化する要素のリスト
        key_func: グループ化のキーを生成する関数

    Returns:
        キーごとにグループ化された辞書

    時間計算量: O(n)
    空間計算量: O(n)

    Examples:
        >>> words = ["cat", "dog", "bat", "fog"]
        >>> group_by(words, len)
        {3: ['cat', 'dog', 'bat', 'fog']}

        >>> numbers = [1, 2, 3, 4, 5, 6]
        >>> group_by(numbers, lambda x: x % 2)
        {1: [1, 3, 5], 0: [2, 4, 6]}
    """
    groups: defaultdict[K, list[T]] = defaultdict(list)
    for item in items:
        key = key_func(item)
        groups[key].append(item)
    return dict(groups)


def group_by_count(items: list[T], key_func: Callable[[T], K]) -> dict[K, int]:
    """
    要素をキー関数でグループ化し、各グループの要素数を返す

    Args:
        items: グループ化する要素のリスト
        key_func: グループ化のキーを生成する関数

    Returns:
        キーごとの要素数の辞書

    時間計算量: O(n)
    空間計算量: O(k) where k=ユニークキー数

    Examples:
        >>> words = ["cat", "dog", "bat", "elephant"]
        >>> group_by_count(words, len)
        {3: 3, 8: 1}
    """
    counts: defaultdict[K, int] = defaultdict(int)
    for item in items:
        key = key_func(item)
        counts[key] += 1
    return dict(counts)


def find_duplicates(items: list[T], min_count: int = 2) -> list[T]:
    """
    指定回数以上出現する要素を抽出する

    Args:
        items: 調査する要素のリスト
        min_count: 最小出現回数（デフォルト: 2）

    Returns:
        min_count以上出現する要素のリスト

    時間計算量: O(n)
    空間計算量: O(n)

    Examples:
        >>> find_duplicates([1, 2, 2, 3, 3, 3, 4])
        [2, 3]
        >>> find_duplicates([1, 2, 2, 3, 3, 3, 4], min_count=3)
        [3]
    """
    counts = Counter(items)
    return [item for item, count in counts.items() if count >= min_count]


def find_unique_elements(items: list[T]) -> list[T]:
    """
    1回だけ出現する要素を抽出する

    Args:
        items: 調査する要素のリスト

    Returns:
        1回だけ出現する要素のリスト

    時間計算量: O(n)
    空間計算量: O(n)

    Examples:
        >>> find_unique_elements([1, 2, 2, 3, 3, 3, 4])
        [1, 4]
    """
    counts = Counter(items)
    return [item for item, count in counts.items() if count == 1]


def get_frequency_distribution(items: list[T]) -> dict[T, int]:
    """
    要素の出現頻度分布を取得する

    Args:
        items: 調査する要素のリスト

    Returns:
        要素とその出現回数の辞書

    時間計算量: O(n)
    空間計算量: O(k) where k=ユニーク要素数

    Examples:
        >>> get_frequency_distribution(['a', 'b', 'a', 'c', 'b', 'a'])
        {'a': 3, 'b': 2, 'c': 1}
    """
    return dict(Counter(items))


def set_operations_summary(set_a: set[T], set_b: set[T]) -> dict[str, set[T]]:
    """
    二つの集合に対する主要な集合演算結果をまとめて返す

    Args:
        set_a: 第一集合
        set_b: 第二集合

    Returns:
        各種集合演算の結果を含む辞書

    時間計算量: O(|A| + |B|)
    空間計算量: O(|A| + |B|)

    Examples:
        >>> a = {1, 2, 3, 4}
        >>> b = {3, 4, 5, 6}
        >>> result = set_operations_summary(a, b)
        >>> result['union']
        {1, 2, 3, 4, 5, 6}
        >>> result['intersection']
        {3, 4}
    """
    return {
        "union": set_a | set_b,
        "intersection": set_a & set_b,
        "difference_a_b": set_a - set_b,
        "difference_b_a": set_b - set_a,
        "symmetric_difference": set_a ^ set_b,
    }


class PriorityQueue(Generic[T]):
    """
    優先度付きキューの実装

    heapqモジュールをラップして使いやすいインターフェースを提供する。
    最小ヒープベースで、小さい優先度値が高い優先度を持つ。

    時間計算量:
    - push: O(log n)
    - pop: O(log n)
    - peek: O(1)
    - empty: O(1)

    Examples:
        >>> pq = PriorityQueue[str]()
        >>> pq.push("low", 3.0)
        >>> pq.push("high", 1.0)
        >>> pq.push("medium", 2.0)
        >>> pq.pop()
        'high'
        >>> pq.pop()
        'medium'
    """

    def __init__(self) -> None:
        """優先度付きキューを初期化"""
        self._queue: list[tuple[float, int, T]] = []
        self._counter = 0  # 同じ優先度の要素の順序を保証

    def push(self, item: T, priority: float) -> None:
        """
        要素を優先度と共にキューに追加

        Args:
            item: 追加する要素
            priority: 優先度（小さい値ほど高い優先度）
        """
        heapq.heappush(self._queue, (priority, self._counter, item))
        self._counter += 1

    def pop(self) -> T:
        """
        最高優先度の要素を取り出して返す

        Returns:
            最高優先度の要素

        Raises:
            IndexError: キューが空の場合
        """
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self._queue)[2]

    def peek(self) -> T:
        """
        最高優先度の要素を取り出さずに参照

        Returns:
            最高優先度の要素

        Raises:
            IndexError: キューが空の場合
        """
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self._queue[0][2]

    def is_empty(self) -> bool:
        """
        キューが空かどうか確認

        Returns:
            キューが空の場合True
        """
        return len(self._queue) == 0

    def size(self) -> int:
        """
        キューのサイズを取得

        Returns:
            キュー内の要素数
        """
        return len(self._queue)


class UnionFind:
    """
    Union-Find（Disjoint Set Union）データ構造

    要素の集合を管理し、集合の結合と要素の所属判定を効率的に行う。
    パス圧縮とランクによる結合最適化を実装。

    時間計算量（償却計算量）:
    - find: O(α(n)) ≈ O(1)
    - union: O(α(n)) ≈ O(1)
    - connected: O(α(n)) ≈ O(1)

    Examples:
        >>> uf = UnionFind(5)  # 0-4の要素を持つ
        >>> uf.union(0, 1)
        >>> uf.union(2, 3)
        >>> uf.connected(0, 1)
        True
        >>> uf.connected(0, 2)
        False
    """

    def __init__(self, n: int) -> None:
        """
        n個の要素でUnion-Findを初期化

        Args:
            n: 管理する要素数（0からn-1）
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # 連結成分の数

    def find(self, x: int) -> int:
        """
        要素xの根を見つける（パス圧縮付き）

        Args:
            x: 調査する要素

        Returns:
            要素xが属する集合の根
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # パス圧縮
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        要素xとyの集合を結合する

        Args:
            x: 第一要素
            y: 第二要素

        Returns:
            結合が実行された場合True（既に同じ集合の場合False）
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # ランクによる結合
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """
        要素xとyが同じ集合に属するか確認

        Args:
            x: 第一要素
            y: 第二要素

        Returns:
            同じ集合に属する場合True
        """
        return self.find(x) == self.find(y)

    def get_component_count(self) -> int:
        """
        連結成分の数を取得

        Returns:
            現在の連結成分数
        """
        return self.count


def create_adjacency_list(
    edges: list[tuple[T, T]], directed: bool = False
) -> dict[T, list[T]]:
    """
    エッジリストから隣接リストを作成する

    Args:
        edges: エッジのリスト（(from, to)のタプル）
        directed: 有向グラフの場合True（デフォルト: False）

    Returns:
        隣接リスト表現の辞書

    時間計算量: O(E) where E=エッジ数
    空間計算量: O(V + E) where V=頂点数

    Examples:
        >>> edges = [(1, 2), (2, 3), (3, 1)]
        >>> create_adjacency_list(edges)
        {1: [2, 3], 2: [1, 3], 3: [2, 1]}
        >>> create_adjacency_list(edges, directed=True)
        {1: [2], 2: [3], 3: [1]}
    """
    adj_list: defaultdict[T, list[T]] = defaultdict(list)

    for from_node, to_node in edges:
        adj_list[from_node].append(to_node)
        if not directed:
            adj_list[to_node].append(from_node)

    return dict(adj_list)


def invert_dictionary(d: dict[K, V]) -> dict[V, list[K]]:
    """
    辞書のキーと値を逆転させる（値が重複する場合はリスト化）

    Args:
        d: 逆転する辞書

    Returns:
        値をキー、元のキーをリスト化した値とする辞書

    時間計算量: O(n)
    空間計算量: O(n)

    Examples:
        >>> invert_dictionary({'a': 1, 'b': 2, 'c': 1})
        {1: ['a', 'c'], 2: ['b']}
    """
    inverted: defaultdict[V, list[K]] = defaultdict(list)
    for key, value in d.items():
        inverted[value].append(key)
    return dict(inverted)


def flatten_nested_list(nested_list: list[Any]) -> list[Any]:
    """
    ネストしたリストを平坦化する

    Args:
        nested_list: ネストしたリスト

    Returns:
        平坦化されたリスト

    時間計算量: O(n) where n=全要素数
    空間計算量: O(n)

    Examples:
        >>> flatten_nested_list([1, [2, 3], [4, [5, 6]], 7])
        [1, 2, 3, 4, 5, 6, 7]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result


def sliding_window(items: list[T], window_size: int) -> list[list[T]]:
    """
    リストに対してスライディングウィンドウを適用

    Args:
        items: 対象のリスト
        window_size: ウィンドウサイズ

    Returns:
        各ウィンドウの要素リスト

    時間計算量: O(n * w) where w=window_size
    空間計算量: O(n * w)

    Examples:
        >>> sliding_window([1, 2, 3, 4, 5], 3)
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    """
    if window_size > len(items):
        return []

    return [items[i : i + window_size] for i in range(len(items) - window_size + 1)]
