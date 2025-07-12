"""
グラフアルゴリズム関連のユーティリティ関数

Project Euler問題で使用されるグラフ理論のアルゴリズムを提供する。
主にトポロジカルソートと最短経路アルゴリズムを含む。

抽出元:
- Problem 079: トポロジカルソート（パスコード導出）
- Problem 083: Dijkstra法（最短経路探索）
"""

import heapq
from typing import Any


def build_dependency_graph(
    sequences: list[str] | list[list[Any]], element_type: type = str
) -> dict[Any, set[Any]]:
    """
    シーケンスのリストから依存関係グラフを構築する

    各要素について、その要素の後に来る必要がある要素の集合を記録する。

    Args:
        sequences: 順序付きシーケンスのリスト（文字列または要素のリスト）
        element_type: 要素の型（型変換に使用）

    Returns:
        dependencies[element] = {後に来る必要がある要素の集合}

    時間計算量: O(n × m²) where n=シーケンス数, m=シーケンス平均長
    空間計算量: O(k²) where k=ユニーク要素数

    Examples:
        >>> sequences = ["531", "624", "735"]
        >>> graph = build_dependency_graph(sequences)
        >>> graph["5"]  # 5の後に来る要素
        {"3", "1"}
    """
    dependencies: dict[Any, set[Any]] = {}

    for sequence in sequences:
        for i in range(len(sequence)):
            element = element_type(sequence[i])
            if element not in dependencies:
                dependencies[element] = set()

            # この要素の後に来る全ての要素を依存関係に追加
            for j in range(i + 1, len(sequence)):
                next_element = element_type(sequence[j])
                dependencies[element].add(next_element)

    return dependencies


def topological_sort(
    dependencies: dict[Any, set[Any]], stable_sort: bool = True
) -> list[Any]:
    """
    依存関係グラフに対してトポロジカルソートを実行する

    Kahn's アルゴリズムを使用して、依存関係を満たす順序を決定する。

    Args:
        dependencies: 依存関係グラフ（build_dependency_graph の出力）
        stable_sort: 安定ソート（辞書順）を使用するかどうか

    Returns:
        トポロジカル順序に並んだ要素のリスト

    Raises:
        ValueError: グラフに循環依存がある場合

    時間計算量: O(V + E) where V=頂点数, E=辺数
    空間計算量: O(V)

    Examples:
        >>> deps = {"A": {"B", "C"}, "B": {"C"}, "C": set()}
        >>> topological_sort(deps)
        ["A", "B", "C"]
    """
    # 全ての要素を収集
    all_elements = set(dependencies.keys())
    for deps in dependencies.values():
        all_elements.update(deps)

    # 各要素への入次数を計算
    in_degree = dict.fromkeys(all_elements, 0)
    for element in dependencies:
        for dep in dependencies[element]:
            in_degree[dep] += 1

    # 入次数が0の要素から開始
    queue = [element for element in all_elements if in_degree[element] == 0]
    result = []

    while queue:
        if stable_sort:
            # 安定ソート: 辞書順で最小の要素を選択
            queue.sort()

        current = queue.pop(0)
        result.append(current)

        # この要素に依存する要素の入次数を減らす
        if current in dependencies:
            for neighbor in dependencies[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    # 循環依存チェック
    if len(result) != len(all_elements):
        remaining = all_elements - set(result)
        raise ValueError(f"循環依存が検出されました: {remaining}")

    return result


def dijkstra_shortest_path(
    graph: list[list[int]] | dict[Any, dict[Any, int]],
    start: tuple[int, int] | Any,
    end: tuple[int, int] | Any,
    directions: list[tuple[int, int]] | None = None,
) -> tuple[int | float, list[Any]]:
    """
    Dijkstra法を使用して最短経路を探索する

    グリッド（2次元配列）または隣接リスト形式のグラフに対応。

    Args:
        graph: グリッド（list[list[int]]）または隣接リスト（dict）
        start: 開始位置（グリッドの場合は(row, col)、グラフの場合は頂点）
        end: 終了位置
        directions: グリッドの場合の移動方向 [(dr, dc), ...]

    Returns:
        (最短距離, 最短経路のリスト)

    時間計算量: O(V log V + E) where V=頂点数, E=辺数
    空間計算量: O(V)

    Examples:
        >>> matrix = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        >>> distance, path = dijkstra_shortest_path(matrix, (0, 0), (2, 2))
        >>> distance
        7
    """
    if isinstance(graph, list) and isinstance(graph[0], list):
        # グリッド形式の場合
        return _dijkstra_grid(graph, start, end, directions)
    # 隣接リスト形式の場合
    return _dijkstra_graph(graph, start, end)


def _dijkstra_grid(
    matrix: list[list[int]],
    start: tuple[int, int],
    end: tuple[int, int],
    directions: list[tuple[int, int]] | None = None,
) -> tuple[int | float, list[tuple[int, int]]]:
    """グリッド用のDijkstra法実装"""
    if directions is None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上

    rows, cols = len(matrix), len(matrix[0])

    # Priority queue: (distance, row, col)
    pq = [(matrix[start[0]][start[1]], start[0], start[1])]
    distances = {start: matrix[start[0]][start[1]]}
    previous: dict[tuple[int, int], tuple[int, int] | None] = {}

    while pq:
        current_dist, row, col = heapq.heappop(pq)

        # 目的地に到達
        if (row, col) == end:
            # 経路を再構築
            path = []
            current = end
            while current in previous:
                path.append(current)
                prev_node = previous[current]
                if prev_node is None:
                    break
                current = prev_node
            path.append(start)
            return current_dist, list(reversed(path))

        # より良い経路が既に見つかっている場合はスキップ
        if current_dist > distances.get((row, col), float("inf")):
            continue

        # 全方向を試す
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # 境界チェック
            if 0 <= new_row < rows and 0 <= new_col < cols:
                new_dist = current_dist + matrix[new_row][new_col]

                # より短い経路を発見した場合
                if new_dist < distances.get((new_row, new_col), float("inf")):
                    distances[(new_row, new_col)] = new_dist
                    previous[(new_row, new_col)] = (row, col)
                    heapq.heappush(pq, (new_dist, new_row, new_col))

    # 経路が見つからない場合
    return float("inf"), []


def _dijkstra_graph(
    graph: dict[Any, dict[Any, int]], start: Any, end: Any
) -> tuple[int | float, list[Any]]:
    """隣接リスト用のDijkstra法実装"""
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    distances = {start: 0}
    previous: dict[Any, Any | None] = {}

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        # 目的地に到達
        if current_vertex == end:
            # 経路を再構築
            path = []
            current = end
            while current in previous:
                path.append(current)
                prev_node = previous[current]
                if prev_node is None:
                    break
                current = prev_node
            path.append(start)
            return current_dist, list(reversed(path))

        # より良い経路が既に見つかっている場合はスキップ
        if current_dist > distances.get(current_vertex, float("inf")):
            continue

        # 隣接頂点を確認
        if current_vertex in graph:
            for neighbor, weight in graph[current_vertex].items():
                new_dist = current_dist + weight

                # より短い経路を発見した場合
                if new_dist < distances.get(neighbor, float("inf")):
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (new_dist, neighbor))

    # 経路が見つからない場合
    return float("inf"), []


def has_cycle(dependencies: dict[Any, set[Any]]) -> bool:
    """
    依存関係グラフに循環があるかチェックする

    Args:
        dependencies: 依存関係グラフ

    Returns:
        循環がある場合True、ない場合False

    時間計算量: O(V + E)
    空間計算量: O(V)
    """
    try:
        topological_sort(dependencies, stable_sort=False)
        return False
    except ValueError:
        return True


def find_strongly_connected_components(graph: dict[Any, list[Any]]) -> list[list[Any]]:
    """
    強連結成分を見つける（Kosaraju's algorithm）

    Args:
        graph: 隣接リスト形式の有向グラフ

    Returns:
        強連結成分のリスト

    時間計算量: O(V + E)
    空間計算量: O(V)
    """
    # 第1回DFS：終了時刻順にスタックに積む
    visited = set()
    stack = []

    def dfs1(vertex: Any) -> None:
        visited.add(vertex)
        if vertex in graph:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    dfs1(neighbor)
        stack.append(vertex)

    # 全頂点について第1回DFS
    all_vertices = set(graph.keys())
    for neighbors in graph.values():
        all_vertices.update(neighbors)

    for vertex in all_vertices:
        if vertex not in visited:
            dfs1(vertex)

    # グラフを反転
    reversed_graph: dict[Any, list[Any]] = {}
    for vertex in all_vertices:
        reversed_graph[vertex] = []

    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            reversed_graph[neighbor].append(vertex)

    # 第2回DFS：スタックの逆順で強連結成分を見つける
    visited = set()
    components = []

    def dfs2(vertex: Any, component: list[Any]) -> None:
        visited.add(vertex)
        component.append(vertex)
        for neighbor in reversed_graph[vertex]:
            if neighbor not in visited:
                dfs2(neighbor, component)

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component: list[Any] = []
            dfs2(vertex, component)
            components.append(component)

    return components
