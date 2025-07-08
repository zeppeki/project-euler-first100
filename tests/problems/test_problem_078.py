"""
Test cases for Problem 78: Coin partitions
"""

import pytest

from problems.problem_078 import (
    partition_function_naive,
    partition_function_optimized,
    solve_naive,
    solve_optimized,
)


class TestPartitionFunction:
    """分割関数のテスト"""

    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 1),  # p(0) = 1 (空の分割)
            (1, 1),  # p(1) = 1 (1)
            (2, 2),  # p(2) = 2 (2, 1+1)
            (3, 3),  # p(3) = 3 (3, 2+1, 1+1+1)
            (4, 5),  # p(4) = 5 (4, 3+1, 2+2, 2+1+1, 1+1+1+1)
            (5, 7),  # p(5) = 7 (問題文の例)
            (6, 11),  # p(6) = 11
            (7, 15),  # p(7) = 15
            (8, 22),  # p(8) = 22
            (9, 30),  # p(9) = 30
            (10, 42),  # p(10) = 42
        ],
    )
    def test_partition_values(self, n: int, expected: int) -> None:
        """既知の分割数の検証"""
        assert partition_function_naive(n) == expected
        assert partition_function_optimized(n) == expected

    def test_modulo_calculation(self) -> None:
        """剰余計算の動作確認"""
        modulo = 100
        for n in range(20):
            naive_result = partition_function_naive(n, modulo)
            optimized_result = partition_function_optimized(n, modulo)
            assert naive_result == optimized_result
            assert 0 <= naive_result < modulo

    def test_larger_values(self) -> None:
        """より大きな値での一致確認"""
        test_values = [15, 20, 25, 30]
        for n in test_values:
            naive_result = partition_function_naive(n)
            optimized_result = partition_function_optimized(n)
            assert naive_result == optimized_result


class TestSolutions:
    """解法のテスト"""

    def test_small_divisor(self) -> None:
        """小さな除数でのテスト"""
        # p(n)が10で割り切れる最小のn
        divisor = 10
        naive_result = solve_naive(divisor)
        optimized_result = solve_optimized(divisor)
        assert naive_result == optimized_result

        # 実際に割り切れることを確認
        p_n = partition_function_optimized(naive_result, divisor)
        assert p_n == 0

    def test_known_values(self) -> None:
        """既知の結果の確認"""
        # p(n)が2で割り切れる最小のn
        result = solve_optimized(2)
        assert partition_function_optimized(result) % 2 == 0
        assert partition_function_optimized(result - 1) % 2 != 0

    @pytest.mark.slow
    def test_large_divisor(self) -> None:
        """大きな除数での最適化解法のテスト"""
        # p(n)が1000で割り切れる最小のn
        divisor = 1000
        result = solve_optimized(divisor)
        assert partition_function_optimized(result, divisor) == 0

    def test_algorithm_correctness(self) -> None:
        """アルゴリズムの正確性テスト"""
        # 素直な解法と最適化解法が同じ結果を返すことを確認
        test_divisors = [5, 7, 10, 25]
        for divisor in test_divisors:
            naive_result = solve_naive(divisor)
            optimized_result = solve_optimized(divisor)
            assert naive_result == optimized_result
