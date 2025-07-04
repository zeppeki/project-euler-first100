#!/usr/bin/env python3
"""
Tests for Problem 050: Consecutive prime sum
"""

import pytest

from problems.problem_050 import (
    is_prime,
    sieve_of_eratosthenes,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestSieveOfEratosthenes:
    """エラトステネスの篩のテスト"""

    def test_small_limit(self) -> None:
        """小さい上限値でのテスト"""
        result = sieve_of_eratosthenes(10)
        expected = [2, 3, 5, 7]
        assert result == expected

    def test_very_small_limit(self) -> None:
        """非常に小さい上限値でのテスト"""
        assert sieve_of_eratosthenes(1) == []
        assert sieve_of_eratosthenes(2) == [2]
        assert sieve_of_eratosthenes(3) == [2, 3]

    def test_zero_and_negative(self) -> None:
        """0以下の値でのテスト"""
        assert sieve_of_eratosthenes(0) == []
        assert sieve_of_eratosthenes(-1) == []


class TestIsPrime:
    """素数判定関数のテスト"""

    def test_small_primes(self) -> None:
        """小さい素数のテスト"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for p in primes:
            assert is_prime(p), f"{p} should be prime"

    def test_small_composites(self) -> None:
        """小さい合成数のテスト"""
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for c in composites:
            assert not is_prime(c), f"{c} should not be prime"

    def test_edge_cases(self) -> None:
        """境界値のテスト"""
        assert not is_prime(0)
        assert not is_prime(1)
        assert is_prime(2)
        assert not is_prime(-1)


class TestSolutions:
    """解法のテスト"""

    def test_small_limit_consistency(self) -> None:
        """小さい上限での解法間の一致性テスト"""
        limit = 100
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_mathematical = solve_mathematical(limit)

        assert result_naive == result_optimized == result_mathematical
        # 問題文より、100未満では41が答え
        assert result_naive == 41

    def test_known_example(self) -> None:
        """問題文の既知の例でのテスト"""
        # 41 = 2 + 3 + 5 + 7 + 11 + 13 (6つの連続する素数の和)
        limit = 50
        result = solve_naive(limit)
        assert result == 41

    def test_solution_is_prime(self) -> None:
        """解が素数であることの確認"""
        result = solve_naive(1000)
        assert is_prime(result), f"Result {result} should be prime"

    def test_default_parameter(self) -> None:
        """デフォルト引数での実行テスト"""
        # デフォルト引数で実行可能であることを確認
        result_naive = solve_naive()
        result_optimized = solve_optimized()
        result_mathematical = solve_mathematical()

        assert result_naive == result_optimized == result_mathematical
        assert result_naive > 0


class TestEdgeCases:
    """境界値テスト"""

    def test_very_small_limits(self) -> None:
        """非常に小さい上限値でのテスト"""
        # 素数が存在しない場合
        assert solve_naive(1) == 0
        assert solve_optimized(1) == 0
        assert solve_mathematical(1) == 0

        # 最小の素数のみ
        assert solve_naive(2) == 0  # 連続する素数の和ではない
        assert solve_optimized(2) == 0
        assert solve_mathematical(2) == 0

    def test_medium_limit(self) -> None:
        """中程度の上限値でのテスト"""
        limit = 1000
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_mathematical = solve_mathematical(limit)

        assert result_naive == result_optimized == result_mathematical
        assert result_naive > 41  # 100未満の答えより大きいはず
        assert result_naive < limit
        assert is_prime(result_naive)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
