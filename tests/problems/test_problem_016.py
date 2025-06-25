#!/usr/bin/env python3
"""
Test for Problem 016: Power Digit Sum
"""

import pytest

from problems.problem_016 import solve_mathematical, solve_naive, solve_optimized


class TestProblem016:
    """Problem 016のテストクラス"""

    def test_solve_naive(self) -> None:
        """素直な解法のテスト"""
        test_cases = [
            (15, 26),  # 2^15 = 32768 → 3+2+7+6+8 = 26
            (10, 7),  # 2^10 = 1024 → 1+0+2+4 = 7
            (5, 5),  # 2^5 = 32 → 3+2 = 5
            (0, 1),  # 2^0 = 1 → 1 = 1
            (1, 2),  # 2^1 = 2 → 2 = 2
            (2, 4),  # 2^2 = 4 → 4 = 4
            (3, 8),  # 2^3 = 8 → 8 = 8
            (4, 7),  # 2^4 = 16 → 1+6 = 7
        ]

        for power, expected in test_cases:
            assert solve_naive(power) == expected, f"Failed for 2^{power}"

    def test_solve_optimized(self) -> None:
        """最適化解法のテスト"""
        test_cases = [
            (15, 26),  # 2^15 = 32768 → 3+2+7+6+8 = 26
            (10, 7),  # 2^10 = 1024 → 1+0+2+4 = 7
            (5, 5),  # 2^5 = 32 → 3+2 = 5
            (0, 1),  # 2^0 = 1 → 1 = 1
            (1, 2),  # 2^1 = 2 → 2 = 2
            (2, 4),  # 2^2 = 4 → 4 = 4
            (3, 8),  # 2^3 = 8 → 8 = 8
            (4, 7),  # 2^4 = 16 → 1+6 = 7
        ]

        for power, expected in test_cases:
            assert solve_optimized(power) == expected, f"Failed for 2^{power}"

    def test_solve_mathematical(self) -> None:
        """数学的解法のテスト"""
        test_cases = [
            (15, 26),  # 2^15 = 32768 → 3+2+7+6+8 = 26
            (10, 7),  # 2^10 = 1024 → 1+0+2+4 = 7
            (5, 5),  # 2^5 = 32 → 3+2 = 5
            (0, 1),  # 2^0 = 1 → 1 = 1
            (1, 2),  # 2^1 = 2 → 2 = 2
            (2, 4),  # 2^2 = 4 → 4 = 4
            (3, 8),  # 2^3 = 8 → 8 = 8
            (4, 7),  # 2^4 = 16 → 1+6 = 7
        ]

        for power, expected in test_cases:
            assert solve_mathematical(power) == expected, f"Failed for 2^{power}"

    def test_all_solutions_agree(self) -> None:
        """すべての解法が同じ結果を返すことを確認"""
        test_cases = [0, 1, 2, 3, 4, 5, 10, 15, 20, 50, 100]

        for power in test_cases:
            result_naive = solve_naive(power)
            result_optimized = solve_optimized(power)
            result_math = solve_mathematical(power)

            assert result_naive == result_optimized == result_math, (
                f"Solutions disagree for 2^{power}: "
                f"naive={result_naive}, optimized={result_optimized}, math={result_math}"
            )

    def test_edge_cases(self) -> None:
        """エッジケースのテスト"""
        # 0の累乗
        assert solve_naive(0) == 1
        assert solve_optimized(0) == 1
        assert solve_mathematical(0) == 1

        # 1の累乗
        assert solve_naive(1) == 2
        assert solve_optimized(1) == 2
        assert solve_mathematical(1) == 2

    def test_large_numbers(self) -> None:
        """大きな数のテスト"""
        # 2^100の桁の和を確認（手動計算可能な範囲）
        result_100 = solve_naive(100)
        assert result_100 == solve_optimized(100)
        assert result_100 == solve_mathematical(100)
        assert result_100 > 0  # 正の数であることを確認

    def test_known_values(self) -> None:
        """既知の値でのテスト"""
        # 2^15 = 32768 → 3+2+7+6+8 = 26
        assert solve_naive(15) == 26
        assert solve_optimized(15) == 26
        assert solve_mathematical(15) == 26

        # 2^10 = 1024 → 1+0+2+4 = 7
        assert solve_naive(10) == 7
        assert solve_optimized(10) == 7
        assert solve_mathematical(10) == 7

    def test_digit_sum_properties(self) -> None:
        """桁の和の性質をテスト"""
        # 2^nの桁の和は常に正の数
        for n in range(1, 21):
            result = solve_naive(n)
            assert result > 0, f"Digit sum for 2^{n} should be positive"

        # 2^nの桁の和はnが増加しても必ずしも増加しない
        # （例：2^4=16→7, 2^5=32→5）
        assert solve_naive(4) == 7
        assert solve_naive(5) == 5
        assert solve_naive(4) > solve_naive(5)

    @pytest.mark.slow
    def test_performance(self) -> None:
        """パフォーマンステスト"""
        # 大きな数での実行時間テスト（機能検証ベース）
        power = 1000

        # すべての解法が同じ結果を返すことを確認
        result_naive = solve_naive(power)
        result_optimized = solve_optimized(power)
        result_math = solve_mathematical(power)

        assert result_naive == result_optimized == result_math
        assert result_naive > 0  # 正の数であることを確認
        assert result_naive < 10000  # 妥当な範囲内であることを確認

    def test_solution_consistency(self) -> None:
        """解答の一貫性テスト"""
        # 同じ入力に対して常に同じ結果を返すことを確認
        power = 50

        result1 = solve_naive(power)
        result2 = solve_naive(power)
        result3 = solve_naive(power)

        assert result1 == result2 == result3

    def test_mathematical_correctness(self) -> None:
        """数学的正確性のテスト"""
        # 2^nの計算が正しいことを確認
        for n in range(10):
            expected = 2**n
            # 桁の和を逆算して確認
            digit_sum = solve_naive(n)
            # 実際の数値の桁の和と一致することを確認
            actual_digit_sum = sum(int(d) for d in str(expected))
            assert digit_sum == actual_digit_sum, f"Failed for 2^{n}"
