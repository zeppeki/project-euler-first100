"""
データ構造ライブラリモジュールのテスト

problems.lib.data_structures モジュールの全関数とクラスに対する
包括的なテストケースを提供する。
"""

import pytest

from problems.lib.data_structures import (
    PriorityQueue,
    UnionFind,
    create_adjacency_list,
    find_duplicates,
    find_unique_elements,
    flatten_nested_list,
    get_frequency_distribution,
    group_by,
    group_by_count,
    invert_dictionary,
    set_operations_summary,
    sliding_window,
)


class TestGroupingFunctions:
    """グループ化関数のテスト"""

    def test_group_by_basic(self) -> None:
        """基本的なグループ化"""
        words = ["cat", "dog", "bat", "elephant"]
        result = group_by(words, len)
        expected = {3: ["cat", "dog", "bat"], 8: ["elephant"]}
        assert result == expected

    def test_group_by_numbers(self) -> None:
        """数値のグループ化"""
        numbers = [1, 2, 3, 4, 5, 6]
        result = group_by(numbers, lambda x: x % 2)
        expected = {1: [1, 3, 5], 0: [2, 4, 6]}
        assert result == expected

    def test_group_by_empty(self) -> None:
        """空リストのグループ化"""
        result: dict[int, list[str]] = group_by([], len)
        assert result == {}

    def test_group_by_count_basic(self) -> None:
        """基本的なカウントグループ化"""
        words = ["cat", "dog", "bat", "elephant"]
        result = group_by_count(words, len)
        expected = {3: 3, 8: 1}
        assert result == expected

    def test_group_by_count_empty(self) -> None:
        """空リストのカウントグループ化"""
        result = group_by_count([], len)
        assert result == {}


class TestDuplicateFunctions:
    """重複検出関数のテスト"""

    def test_find_duplicates_basic(self) -> None:
        """基本的な重複検出"""
        items = [1, 2, 2, 3, 3, 3, 4]
        result = find_duplicates(items)
        assert set(result) == {2, 3}

    def test_find_duplicates_min_count(self) -> None:
        """最小出現回数指定の重複検出"""
        items = [1, 2, 2, 3, 3, 3, 4]
        result = find_duplicates(items, min_count=3)
        assert result == [3]

    def test_find_duplicates_no_duplicates(self) -> None:
        """重複なしの場合"""
        items = [1, 2, 3, 4]
        result = find_duplicates(items)
        assert result == []

    def test_find_unique_elements_basic(self) -> None:
        """基本的なユニーク要素検出"""
        items = [1, 2, 2, 3, 3, 3, 4]
        result = find_unique_elements(items)
        assert set(result) == {1, 4}

    def test_find_unique_elements_all_duplicates(self) -> None:
        """全て重複の場合"""
        items = [1, 1, 2, 2, 3, 3]
        result = find_unique_elements(items)
        assert result == []


class TestFrequencyFunctions:
    """頻度分析関数のテスト"""

    def test_get_frequency_distribution_basic(self) -> None:
        """基本的な頻度分布"""
        items = ["a", "b", "a", "c", "b", "a"]
        result = get_frequency_distribution(items)
        expected = {"a": 3, "b": 2, "c": 1}
        assert result == expected

    def test_get_frequency_distribution_numbers(self) -> None:
        """数値の頻度分布"""
        items = [1, 2, 1, 3, 2, 1]
        result = get_frequency_distribution(items)
        expected = {1: 3, 2: 2, 3: 1}
        assert result == expected

    def test_get_frequency_distribution_empty(self) -> None:
        """空リストの頻度分布"""
        result: dict[str, int] = get_frequency_distribution([])
        assert result == {}


class TestSetOperations:
    """集合演算のテスト"""

    def test_set_operations_summary_basic(self) -> None:
        """基本的な集合演算"""
        set_a = {1, 2, 3, 4}
        set_b = {3, 4, 5, 6}
        result = set_operations_summary(set_a, set_b)

        assert result["union"] == {1, 2, 3, 4, 5, 6}
        assert result["intersection"] == {3, 4}
        assert result["difference_a_b"] == {1, 2}
        assert result["difference_b_a"] == {5, 6}
        assert result["symmetric_difference"] == {1, 2, 5, 6}

    def test_set_operations_summary_disjoint(self) -> None:
        """互いに素な集合"""
        set_a = {1, 2}
        set_b = {3, 4}
        result = set_operations_summary(set_a, set_b)

        assert result["union"] == {1, 2, 3, 4}
        assert result["intersection"] == set()
        assert result["difference_a_b"] == {1, 2}
        assert result["difference_b_a"] == {3, 4}
        assert result["symmetric_difference"] == {1, 2, 3, 4}

    def test_set_operations_summary_identical(self) -> None:
        """同一集合"""
        set_a = {1, 2, 3}
        set_b = {1, 2, 3}
        result = set_operations_summary(set_a, set_b)

        assert result["union"] == {1, 2, 3}
        assert result["intersection"] == {1, 2, 3}
        assert result["difference_a_b"] == set()
        assert result["difference_b_a"] == set()
        assert result["symmetric_difference"] == set()


class TestPriorityQueue:
    """優先度付きキューのテスト"""

    def test_priority_queue_basic(self) -> None:
        """基本的な優先度付きキュー操作"""
        pq = PriorityQueue[str]()

        pq.push("low", 3.0)
        pq.push("high", 1.0)
        pq.push("medium", 2.0)

        assert pq.pop() == "high"
        assert pq.pop() == "medium"
        assert pq.pop() == "low"

    def test_priority_queue_same_priority(self) -> None:
        """同じ優先度の要素"""
        pq = PriorityQueue[str]()

        pq.push("first", 1.0)
        pq.push("second", 1.0)
        pq.push("third", 1.0)

        # 同じ優先度では挿入順序が保たれる
        assert pq.pop() == "first"
        assert pq.pop() == "second"
        assert pq.pop() == "third"

    def test_priority_queue_peek(self) -> None:
        """peek操作のテスト"""
        pq = PriorityQueue[int]()

        pq.push(30, 3.0)
        pq.push(10, 1.0)
        pq.push(20, 2.0)

        assert pq.peek() == 10
        assert pq.size() == 3
        assert pq.pop() == 10
        assert pq.size() == 2

    def test_priority_queue_empty_operations(self) -> None:
        """空キューでの操作"""
        pq = PriorityQueue[str]()

        assert pq.is_empty() is True
        assert pq.size() == 0

        with pytest.raises(IndexError):
            pq.pop()

        with pytest.raises(IndexError):
            pq.peek()


class TestUnionFind:
    """Union-Findデータ構造のテスト"""

    def test_union_find_basic(self) -> None:
        """基本的なUnion-Find操作"""
        uf = UnionFind(5)

        assert uf.get_component_count() == 5

        # 0と1を結合
        assert uf.union(0, 1) is True
        assert uf.connected(0, 1) is True
        assert uf.get_component_count() == 4

        # 2と3を結合
        assert uf.union(2, 3) is True
        assert uf.connected(2, 3) is True
        assert uf.get_component_count() == 3

        # 0と2は接続されていない
        assert uf.connected(0, 2) is False

    def test_union_find_same_set(self) -> None:
        """同じ集合の要素の結合"""
        uf = UnionFind(3)

        uf.union(0, 1)

        # 既に同じ集合の要素を結合
        assert uf.union(0, 1) is False
        assert uf.get_component_count() == 2

    def test_union_find_path_compression(self) -> None:
        """パス圧縮の動作確認"""
        uf = UnionFind(4)

        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)

        # パス圧縮により全ての要素が同じ根を持つ
        root = uf.find(0)
        assert uf.find(1) == root
        assert uf.find(2) == root
        assert uf.find(3) == root


class TestUtilityFunctions:
    """ユーティリティ関数のテスト"""

    def test_create_adjacency_list_undirected(self) -> None:
        """無向グラフの隣接リスト作成"""
        edges = [(1, 2), (2, 3), (3, 1)]
        result = create_adjacency_list(edges)
        expected = {1: [2, 3], 2: [1, 3], 3: [2, 1]}
        assert result == expected

    def test_create_adjacency_list_directed(self) -> None:
        """有向グラフの隣接リスト作成"""
        edges = [(1, 2), (2, 3), (3, 1)]
        result = create_adjacency_list(edges, directed=True)
        expected = {1: [2], 2: [3], 3: [1]}
        assert result == expected

    def test_invert_dictionary_basic(self) -> None:
        """基本的な辞書の逆転"""
        d = {"a": 1, "b": 2, "c": 1}
        result = invert_dictionary(d)
        expected = {1: ["a", "c"], 2: ["b"]}
        assert result == expected

    def test_invert_dictionary_unique_values(self) -> None:
        """値がユニークな辞書の逆転"""
        d = {"a": 1, "b": 2, "c": 3}
        result = invert_dictionary(d)
        expected = {1: ["a"], 2: ["b"], 3: ["c"]}
        assert result == expected

    def test_flatten_nested_list_basic(self) -> None:
        """基本的なネストリストの平坦化"""
        nested = [1, [2, 3], [4, [5, 6]], 7]
        result = flatten_nested_list(nested)
        expected = [1, 2, 3, 4, 5, 6, 7]
        assert result == expected

    def test_flatten_nested_list_deep(self) -> None:
        """深いネストの平坦化"""
        nested = [1, [2, [3, [4, [5]]]]]
        result = flatten_nested_list(nested)
        expected = [1, 2, 3, 4, 5]
        assert result == expected

    def test_flatten_nested_list_empty(self) -> None:
        """空リストの平坦化"""
        result = flatten_nested_list([])
        assert result == []

    def test_sliding_window_basic(self) -> None:
        """基本的なスライディングウィンドウ"""
        items = [1, 2, 3, 4, 5]
        result = sliding_window(items, 3)
        expected = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        assert result == expected

    def test_sliding_window_window_size_too_large(self) -> None:
        """ウィンドウサイズが大きすぎる場合"""
        items = [1, 2, 3]
        result = sliding_window(items, 5)
        assert result == []

    def test_sliding_window_window_size_one(self) -> None:
        """ウィンドウサイズが1の場合"""
        items = [1, 2, 3]
        result = sliding_window(items, 1)
        expected = [[1], [2], [3]]
        assert result == expected

    def test_sliding_window_empty_list(self) -> None:
        """空リストのスライディングウィンドウ"""
        result: list[list[int]] = sliding_window([], 3)
        assert result == []


class TestEdgeCases:
    """エッジケースのテスト"""

    def test_empty_inputs(self) -> None:
        """空入力のテスト"""
        assert group_by([], str) == {}
        assert find_duplicates([]) == []
        assert find_unique_elements([]) == []
        assert get_frequency_distribution([]) == {}
        assert flatten_nested_list([]) == []
        assert sliding_window([], 1) == []

    def test_single_element_inputs(self) -> None:
        """単一要素入力のテスト"""
        assert group_by([1], lambda x: x) == {1: [1]}
        assert find_duplicates([1]) == []
        assert find_unique_elements([1]) == [1]
        assert get_frequency_distribution([1]) == {1: 1}
        assert flatten_nested_list([1]) == [1]
        assert sliding_window([1], 1) == [[1]]

    def test_large_inputs(self) -> None:
        """大きな入力のパフォーマンステスト"""
        large_list = list(range(1000))

        # グループ化のパフォーマンス
        group_result = group_by(large_list, lambda x: x % 10)
        assert len(group_result) == 10
        assert all(len(group) == 100 for group in group_result.values())

        # 頻度分析のパフォーマンス
        duplicated_list = large_list * 2
        freq_result = get_frequency_distribution(duplicated_list)
        assert all(count == 2 for count in freq_result.values())
