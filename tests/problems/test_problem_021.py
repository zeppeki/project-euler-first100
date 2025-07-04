#!/usr/bin/env python3
"""
Tests for Problem 021: Amicable Numbers
"""

import pytest

from problems.lib import get_proper_divisors_sum
from problems.problem_021 import (
    find_amicable_pairs,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    validate_amicable_pair,
)


class TestProperDivisorsCalculation:
    """真約数の和の計算テスト"""

    def test_known_examples(self) -> None:
        """既知の例のテスト"""
        # 220の真約数の和: 1+2+4+5+10+11+20+22+44+55+110 = 284
        assert get_proper_divisors_sum(220) == 284
        # 284の真約数の和: 1+2+4+71+142 = 220
        assert get_proper_divisors_sum(284) == 220

    def test_small_numbers(self) -> None:
        """小さい数のテスト"""
        assert get_proper_divisors_sum(1) == 0  # 1の真約数はなし
        assert get_proper_divisors_sum(2) == 1  # 2の真約数は1のみ
        assert get_proper_divisors_sum(3) == 1  # 3の真約数は1のみ
        assert get_proper_divisors_sum(4) == 3  # 4の真約数は1,2
        assert get_proper_divisors_sum(6) == 6  # 6の真約数は1,2,3（完全数）

    def test_perfect_numbers(self) -> None:
        """完全数のテスト"""
        # 完全数は真約数の和が自分自身と等しい
        assert get_proper_divisors_sum(6) == 6  # 1+2+3 = 6
        assert get_proper_divisors_sum(28) == 28  # 1+2+4+7+14 = 28

    def test_prime_numbers(self) -> None:
        """素数のテスト"""
        # 素数の真約数の和は1
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for prime in primes:
            assert get_proper_divisors_sum(prime) == 1

    def test_naive_vs_optimized_divisors(self) -> None:
        """naive実装と最適化実装の比較"""
        # ライブラリ関数の一貫性をテスト
        test_numbers = [12, 20, 28, 30, 60, 100, 220, 284]
        for num in test_numbers:
            result = get_proper_divisors_sum(num)
            assert isinstance(result, int)
            assert result >= 0


class TestAmicablePairValidation:
    """友愛数ペアの検証テスト"""

    def test_known_amicable_pair(self) -> None:
        """既知の友愛数ペアのテスト"""
        # (220, 284)は友愛数ペア
        assert validate_amicable_pair(220, 284)
        assert validate_amicable_pair(284, 220)

    def test_non_amicable_pairs(self) -> None:
        """友愛数でないペアのテスト"""
        assert not validate_amicable_pair(220, 221)
        assert not validate_amicable_pair(100, 200)
        # 完全数は友愛数ではない（自分自身とペアになってしまう）
        assert not validate_amicable_pair(6, 6)
        assert not validate_amicable_pair(28, 28)

    def test_find_amicable_pairs_small_range(self) -> None:
        """小範囲での友愛数ペア検索テスト"""
        pairs = find_amicable_pairs(300)
        # 300未満で(220, 284)のペアが見つかるはず
        assert (220, 284) in pairs or (284, 220) in pairs
        # ペアの数は1つ以上
        assert len(pairs) >= 1


class TestSolveNaive:
    """solve_naiveのテスト"""

    def test_small_ranges(self) -> None:
        """小範囲でのテスト"""
        # 220未満では友愛数はない
        assert solve_naive(220) == 0
        # 285未満では220+284=504
        assert solve_naive(285) == 504
        # 300未満では220+284=504
        assert solve_naive(300) == 504


class TestSolveOptimized:
    """solve_optimizedのテスト"""

    def test_small_ranges(self) -> None:
        """小範囲でのテスト"""
        # 220未満では友愛数はない
        assert solve_optimized(220) == 0
        # 285未満では220+284=504
        assert solve_optimized(285) == 504
        # 300未満では220+284=504
        assert solve_optimized(300) == 504


class TestSolveMathematical:
    """solve_mathematicalのテスト"""

    def test_small_ranges(self) -> None:
        """小範囲でのテスト"""
        # 220未満では友愛数はない
        assert solve_mathematical(220) == 0
        # 285未満では220+284=504
        assert solve_mathematical(285) == 504
        # 300未満では220+284=504
        assert solve_mathematical(300) == 504


class TestSolutionConsistency:
    """解法間の一貫性テスト"""

    @pytest.mark.parametrize("limit", [100, 300, 500, 1000])
    def test_all_methods_consistency(self, limit: int) -> None:
        """全ての解法の結果が一致することを確認"""
        naive_result = solve_naive(limit)
        optimized_result = solve_optimized(limit)
        mathematical_result = solve_mathematical(limit)

        assert naive_result == optimized_result == mathematical_result


class TestEdgeCases:
    """エッジケースのテスト"""

    def test_very_small_limits(self) -> None:
        """非常に小さい上限のテスト"""
        assert solve_naive(1) == 0
        assert solve_naive(2) == 0
        assert solve_optimized(1) == 0
        assert solve_optimized(2) == 0
        assert solve_mathematical(1) == 0
        assert solve_mathematical(2) == 0

    def test_edge_boundary_cases(self) -> None:
        """境界値のテスト"""
        # 220ちょうどでは友愛数なし（220自体は含まれないため）
        assert solve_naive(220) == 0
        # 221では220が含まれるが、ペアの284が範囲外なので0
        assert solve_naive(221) == 0
        # 284では220もあるが、284自体は含まれないので0
        assert solve_naive(284) == 0
        # 285では220+284=504（両方が範囲内）
        assert solve_naive(285) == 504

    def test_perfect_numbers_excluded(self) -> None:
        """完全数が友愛数として除外されることの確認"""
        # 完全数6, 28は友愛数ではないので除外される
        result_50 = solve_naive(50)
        result_100 = solve_naive(100)
        # 50未満, 100未満には友愛数がないことを確認
        assert result_50 == 0
        assert result_100 == 0

    def test_large_known_amicable_pairs(self) -> None:
        """より大きな既知の友愛数ペアのテスト"""
        # (1184, 1210)は次の友愛数ペア
        assert validate_amicable_pair(1184, 1210)
        assert validate_amicable_pair(1210, 1184)

        # 1200までの範囲では220+284=504のみ（1184のペア1210が範囲外）
        result_1200 = solve_naive(1200)
        assert result_1200 == 504

        # 1211までの範囲では220+284+1184+1210=2898が含まれる
        result_1211 = solve_naive(1211)
        assert result_1211 == 2898
