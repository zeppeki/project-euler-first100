#!/usr/bin/env python3
"""
Tests for Problem 071: Ordered fractions

Project Euler Problem 071のテストケース
"""

from collections.abc import Callable

import pytest

from problems.problem_071 import (
    analyze_fraction_sequence,
    find_fraction_left_of_target,
    solve_mathematical,
    solve_mediant,
    solve_optimized,
)


def verify_farey_neighbor(a: int, b: int, c: int, d: int) -> bool:
    """
    ファレー数列で隣接する分数かどうかを検証
    隣接する分数a/bとc/dは ad - bc = 1 を満たす
    """
    return c * b - d * a == 1


class TestProblem071:
    """Problem 071のテストクラス"""

    def test_solve_optimized_small_case(self) -> None:
        """最適化解法の小さなケースでのテスト"""
        # 問題文の例: d ≤ 8で3/7のすぐ左は2/5
        result = solve_optimized(8)
        assert result == 2

        # より大きな例
        result_100 = solve_optimized(100)
        assert isinstance(result_100, int)
        assert result_100 > 0

    def test_solve_mathematical_small_case(self) -> None:
        """数学的解法の小さなケースでのテスト"""
        # 問題文の例
        result = solve_mathematical(8)
        assert result == 2

        # より大きな例
        result_100 = solve_mathematical(100)
        assert isinstance(result_100, int)
        assert result_100 > 0

    def test_solve_mediant_small_case(self) -> None:
        """メディアント法の小さなケースでのテスト"""
        # 問題文の例
        result = solve_mediant(8)
        assert result == 2

        # より大きな例
        result_100 = solve_mediant(100)
        assert isinstance(result_100, int)
        assert result_100 > 0

    def test_solution_consistency(self) -> None:
        """解法間の一貫性テスト"""
        test_limits = [8, 100, 1000]

        for limit in test_limits:
            result_optimized = solve_optimized(limit)
            result_mathematical = solve_mathematical(limit)
            result_mediant = solve_mediant(limit)

            assert result_optimized == result_mathematical
            assert result_mathematical == result_mediant

    def test_find_fraction_left_of_target_basic(self) -> None:
        """目標分数の左側分数探索の基本テスト"""
        # 3/7のすぐ左を探す（d ≤ 8）
        left_num, left_den = find_fraction_left_of_target(3, 7, 8)
        assert left_num == 2
        assert left_den == 5

        # 1/2のすぐ左を探す（d ≤ 10）
        left_num, left_den = find_fraction_left_of_target(1, 2, 10)
        assert left_num * 2 < left_den  # n/d < 1/2を確認

    def test_verify_farey_neighbor_basic(self) -> None:
        """ファレー数列隣接関係の基本テスト"""
        # 2/5と3/7は隣接
        assert verify_farey_neighbor(2, 5, 3, 7)

        # 1/3と1/2は隣接
        assert verify_farey_neighbor(1, 3, 1, 2)

        # 非隣接のケース
        assert not verify_farey_neighbor(1, 4, 3, 7)

    def test_verify_farey_neighbor_properties(self) -> None:
        """ファレー数列隣接関係の性質テスト"""
        # ad - bc = 1の性質
        test_cases = [
            (2, 5, 3, 7),  # 3*5 - 7*2 = 15 - 14 = 1
            (1, 3, 1, 2),  # 1*3 - 2*1 = 3 - 2 = 1
            (3, 8, 2, 5),  # 2*8 - 5*3 = 16 - 15 = 1
        ]

        for a, b, c, d in test_cases:
            assert verify_farey_neighbor(a, b, c, d)
            assert c * b - d * a == 1

    def test_analyze_fraction_sequence_structure(self) -> None:
        """分数列分析の構造テスト"""
        results = analyze_fraction_sequence(20)

        # 結果の形式確認
        assert isinstance(results, list)
        for n, d, val in results:
            assert isinstance(n, int)
            assert isinstance(d, int)
            assert isinstance(val, float)
            assert n > 0
            assert d > 0
            assert n < d
            assert 0 < val < 1

        # ソート順の確認
        if len(results) > 1:
            for i in range(len(results) - 1):
                assert results[i][2] <= results[i + 1][2]

    def test_mathematical_relationship(self) -> None:
        """数学的関係式のテスト"""
        # 3q - 7p = 1の関係をテスト
        limit = 100
        p = solve_mathematical(limit)

        # q = (7p + 1)/3を計算
        if (7 * p + 1) % 3 == 0:
            q = (7 * p + 1) // 3
            assert q <= limit
            assert 3 * q - 7 * p == 1

    def test_edge_cases(self) -> None:
        """エッジケースのテスト"""
        # 最小のケース
        result = solve_optimized(2)
        assert result >= 0

        # 目標分数より小さい分母のケース
        result = solve_optimized(7)
        assert result >= 0

    def test_fraction_values(self) -> None:
        """分数値の妥当性テスト"""
        limit = 1000
        p = solve_mathematical(limit)

        if (7 * p + 1) % 3 == 0:
            q = (7 * p + 1) // 3
            fraction_val = p / q
            target_val = 3 / 7

            # p/q < 3/7であることを確認
            assert fraction_val < target_val

            # 差が妥当な範囲内であることを確認
            diff = target_val - fraction_val
            assert 0 < diff < 0.01  # 適度に近い値

    @pytest.mark.parametrize(
        "solve_func",
        [solve_optimized, solve_mathematical, solve_mediant],
        ids=["optimized", "mathematical", "mediant"],
    )
    def test_solution_functions_return_valid_result(
        self, solve_func: Callable[[int], int]
    ) -> None:
        """全ての解法が有効な結果を返すことをテスト"""
        test_limits = [8, 50, 100]

        for limit in test_limits:
            result = solve_func(limit)
            assert isinstance(result, int)
            assert result > 0

            # 対応する分母が存在し、制限内であることを確認
            if (7 * result + 1) % 3 == 0:
                q = (7 * result + 1) // 3
                assert q <= limit

    def test_problem_example_verification(self) -> None:
        """問題文の例の検証"""
        # d ≤ 8で3/7のすぐ左は2/5
        result = solve_optimized(8)
        assert result == 2

        # 2/5が3/7のすぐ左であることを確認
        assert verify_farey_neighbor(2, 5, 3, 7)

        # 2/5 < 3/7であることを確認
        assert 2 / 5 < 3 / 7

    def test_large_case_properties(self) -> None:
        """大きなケースでの性質テスト"""
        limit = 10000
        p = solve_mathematical(limit)

        # 基本的な性質の確認
        assert isinstance(p, int)
        assert p > 0

        # 数学的関係の確認
        if (7 * p + 1) % 3 == 0:
            q = (7 * p + 1) // 3
            assert q <= limit
            assert 3 * q - 7 * p == 1

    def test_mediant_property(self) -> None:
        """メディアント性質のテスト"""
        # 既知の隣接分数でメディアントをテスト
        a, b = 2, 5  # 左側
        c, d = 3, 7  # 右側

        # メディアント
        med_num = a + c
        med_den = b + d
        assert med_num == 5
        assert med_den == 12

        # メディアントが両端の間にあることを確認
        assert a / b < med_num / med_den < c / d

    def test_gcd_property(self) -> None:
        """最大公約数の性質テスト"""
        from math import gcd

        # 解法で得られる分数が既約であることを確認
        limit = 100
        p = solve_mathematical(limit)

        if (7 * p + 1) % 3 == 0:
            q = (7 * p + 1) // 3
            assert gcd(p, q) == 1  # 既約分数

    @pytest.mark.slow
    def test_solve_medium_case(self) -> None:
        """中規模ケースでの解法テスト（スロー）"""
        limit = 100000
        result = solve_mathematical(limit)

        assert isinstance(result, int)
        assert result > 0

        # 対応する分母の計算と検証
        if (7 * result + 1) % 3 == 0:
            q = (7 * result + 1) // 3
            assert q <= limit

            # 分数値の妥当性
            fraction_val = result / q
            target_val = 3 / 7
            assert fraction_val < target_val
            assert target_val - fraction_val < 0.001

    def test_sequence_monotonicity(self) -> None:
        """数列の単調性テスト"""
        # 分母が増加すると、3/7に近い分数も改善されることを確認
        limits = [50, 100, 200]
        prev_fraction = 0.0

        for limit in limits:
            p = solve_mathematical(limit)
            if (7 * p + 1) % 3 == 0:
                q = (7 * p + 1) // 3
                fraction_val = p / q
                assert fraction_val >= prev_fraction  # 単調増加
                prev_fraction = fraction_val

    def test_boundary_conditions(self) -> None:
        """境界条件のテスト"""
        # 分母が目標分数の分母と同じ場合
        result = solve_mathematical(7)
        assert result >= 0

        # 分母が目標分数の分母より小さい場合
        result = solve_mathematical(6)
        assert result >= 0


if __name__ == "__main__":
    pytest.main([__file__])
