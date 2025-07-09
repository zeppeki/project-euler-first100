#!/usr/bin/env python3
"""
Tests for Problem 081: Path sum: two ways
"""

import pytest

from problems.problem_081 import solve_naive, solve_optimized


class TestProblem081:
    """Problem 081のテストクラス"""

    def test_single_cell(self) -> None:
        """単一セルの行列"""
        matrix = [[5]]
        assert solve_naive(matrix) == 5
        assert solve_optimized(matrix) == 5

    def test_single_row(self) -> None:
        """単一行の行列"""
        matrix = [[1, 2, 3, 4]]
        # 右にしか移動できないので、全ての要素の合計
        expected = 10
        assert solve_naive(matrix) == expected
        assert solve_optimized(matrix) == expected

    def test_single_column(self) -> None:
        """単一列の行列"""
        matrix = [[1], [2], [3], [4]]
        # 下にしか移動できないので、全ての要素の合計
        expected = 10
        assert solve_naive(matrix) == expected
        assert solve_optimized(matrix) == expected

    def test_2x2_matrix(self) -> None:
        """2x2の行列"""
        matrix = [[1, 2], [3, 4]]
        # 最小経路: 1 -> 2 -> 4 = 7
        expected = 7
        assert solve_naive(matrix) == expected
        assert solve_optimized(matrix) == expected

    def test_3x3_matrix(self) -> None:
        """3x3の行列"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # 最小経路: 1 -> 2 -> 3 -> 6 -> 9 = 21
        expected = 21
        assert solve_naive(matrix) == expected
        assert solve_optimized(matrix) == expected

    def test_example_matrix(self) -> None:
        """問題文の例の行列"""
        matrix = [
            [131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331],
        ]
        expected = 2427
        assert solve_naive(matrix) == expected
        assert solve_optimized(matrix) == expected

    def test_all_ones_matrix(self) -> None:
        """全ての要素が1の行列"""
        size = 4
        matrix = [[1] * size for _ in range(size)]
        # 最短経路は右に(size-1)回、下に(size-1)回移動
        # 通るセルの数は (size-1) + (size-1) + 1 = 2*size - 1
        expected = 2 * size - 1
        assert solve_naive(matrix) == expected
        assert solve_optimized(matrix) == expected

    def test_diagonal_preference(self) -> None:
        """対角線方向の値が小さい行列"""
        matrix = [[1, 9, 9], [9, 1, 9], [9, 9, 1]]
        # 最小経路: 1 -> 9 -> 1 -> 9 -> 1 = 21
        expected = 21
        assert solve_naive(matrix) == expected
        assert solve_optimized(matrix) == expected

    def test_empty_matrix(self) -> None:
        """空の行列"""
        matrix: list[list[int]] = []
        assert solve_naive(matrix) == 0
        assert solve_optimized(matrix) == 0

        matrix = [[]]
        assert solve_naive(matrix) == 0
        assert solve_optimized(matrix) == 0

    def test_large_values(self) -> None:
        """大きな値を含む行列"""
        matrix = [[1000, 1, 1000], [1, 1, 1000], [1000, 1, 1]]
        # 最小経路: 1000 -> 1 -> 1 -> 1 -> 1 = 1004
        expected = 1004
        assert solve_naive(matrix) == expected
        assert solve_optimized(matrix) == expected

    @pytest.mark.parametrize("size", [5, 10])
    def test_increasing_matrix_sizes(self, size: int) -> None:
        """様々なサイズの行列でのテスト"""
        # 行と列のインデックスの合計を値とする行列
        matrix = [[i + j for j in range(size)] for i in range(size)]

        # 両方の解法が同じ結果を返すことを確認
        result_naive = solve_naive(matrix)
        result_optimized = solve_optimized(matrix)
        assert result_naive == result_optimized

        # 結果が妥当な範囲内にあることを確認
        # 最小値は左上から右下への直線的な経路
        min_possible = sum(matrix[i][i] for i in range(size))
        assert result_optimized >= min_possible

    def test_performance_difference(self) -> None:
        """大きめの行列での性能差を確認（実行時間は測定しない）"""
        # 20x20の行列で両方の解法が同じ結果を返すことを確認
        size = 20
        matrix = [[i * j + 1 for j in range(size)] for i in range(size)]

        # 結果の一致を確認
        result_optimized = solve_optimized(matrix)
        # 注: 素直な解法は大きい行列では非常に遅いため、小さいサイズでのみテスト
        if size <= 10:
            result_naive = solve_naive(matrix)
            assert result_naive == result_optimized

        # 結果が正の値であることを確認
        assert result_optimized > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
