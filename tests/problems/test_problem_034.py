#!/usr/bin/env python3
"""
Test for Problem 034: Digit factorials
"""

import pytest

from problems.problem_034 import (
    digit_factorial_sum,
    factorial,
    get_digit_factorials,
    is_digit_factorial,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    verify_examples,
)


class TestProblem034:
    """Problem 034のテストクラス"""

    def test_factorial(self) -> None:
        """階乗関数のテスト"""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
        assert factorial(9) == 362880

    def test_digit_factorial_sum(self) -> None:
        """桁階乗和計算のテスト"""
        # 例題: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
        assert digit_factorial_sum(145) == 145

        # その他のテストケース
        assert digit_factorial_sum(1) == 1  # 1!
        assert digit_factorial_sum(2) == 2  # 2!
        assert digit_factorial_sum(12) == 3  # 1! + 2! = 1 + 2 = 3
        assert digit_factorial_sum(123) == 9  # 1! + 2! + 3! = 1 + 2 + 6 = 9
        assert digit_factorial_sum(9) == 362880  # 9! = 362880

    def test_is_digit_factorial(self) -> None:
        """桁階乗数判定のテスト"""
        # 既知の桁階乗数
        assert is_digit_factorial(145) is True  # 1! + 4! + 5! = 145

        # 1!, 2!は和ではないので問題では除外
        assert is_digit_factorial(1) is True  # 技術的には正しいが問題では除外
        assert is_digit_factorial(2) is True  # 技術的には正しいが問題では除外

        # 桁階乗数ではない例
        assert is_digit_factorial(123) is False  # 1! + 2! + 3! = 9 ≠ 123
        assert is_digit_factorial(100) is False  # 1! + 0! + 0! = 3 ≠ 100
        assert is_digit_factorial(999) is False  # 9! + 9! + 9! = 1,088,640 ≠ 999

    def test_verify_examples(self) -> None:
        """問題の例の検証"""
        assert verify_examples() is True

    @pytest.mark.slow
    def test_get_digit_factorials(self) -> None:
        """桁階乗数取得のテスト"""
        digit_factorials = get_digit_factorials()

        # 既知の桁階乗数が含まれることを確認
        assert 145 in digit_factorials

        # 1, 2は除外されていることを確認（問題の注記より）
        assert 1 not in digit_factorials
        assert 2 not in digit_factorials

        # すべてが桁階乗数であることを確認
        for number in digit_factorials:
            assert is_digit_factorial(number)

        # 結果が空でないことを確認
        assert len(digit_factorials) > 0

    @pytest.mark.slow
    def test_solve_naive(self) -> None:
        """素直な解法のテスト（slow test）"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0
        # 期待される解答の範囲をテスト
        assert 40000 <= result <= 50000

    @pytest.mark.slow
    def test_solve_optimized(self) -> None:
        """最適化解法のテスト"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0
        # 期待される解答の範囲をテスト
        assert 40000 <= result <= 50000

    @pytest.mark.slow
    def test_solve_mathematical(self) -> None:
        """数学的解法のテスト"""
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 0
        # 期待される解答の範囲をテスト
        assert 40000 <= result <= 50000

    @pytest.mark.slow
    def test_all_solutions_agree(self) -> None:
        """すべての解法が同じ結果を返すことを確認（slow test）"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert naive_result == optimized_result == mathematical_result

    @pytest.mark.slow
    def test_digit_factorial_properties(self) -> None:
        """桁階乗数の性質をテスト"""
        digit_factorials = get_digit_factorials()

        for number in digit_factorials:
            # 各数が実際に桁階乗数であることを確認
            assert is_digit_factorial(number)

            # 桁階乗和が元の数と等しいことを確認
            factorial_sum = digit_factorial_sum(number)
            assert number == factorial_sum

            # 3以上であることを確認（1!, 2!は除外）
            assert number >= 3

    @pytest.mark.slow
    def test_sum_calculation(self) -> None:
        """和の計算をテスト（slow test）"""
        digit_factorials = get_digit_factorials()
        manual_sum = sum(digit_factorials)

        # 各解法の結果と一致することを確認
        assert solve_naive() == manual_sum
        assert solve_optimized() == manual_sum
        assert solve_mathematical() == manual_sum

    def test_edge_cases(self) -> None:
        """エッジケースのテスト"""
        # 単桁数
        assert digit_factorial_sum(0) == 1  # 0! = 1
        assert digit_factorial_sum(9) == 362880  # 9! = 362880

        # 桁階乗数の境界値
        assert is_digit_factorial(145) is True
        assert is_digit_factorial(144) is False
        assert is_digit_factorial(146) is False

    @pytest.mark.slow
    def test_mathematical_properties(self) -> None:
        """数学的性質の検証"""
        import math

        # 上限の妥当性をテスト
        # 8桁以上で数値が階乗和を超えることを確認
        min_8_digit = 10000000
        max_8_digit_factorial_sum = 8 * math.factorial(9)
        assert min_8_digit > max_8_digit_factorial_sum

        # よって7 * 9!が適切な上限
        upper_limit = 7 * math.factorial(9)

        # 見つかった桁階乗数がすべて上限以下であることを確認
        digit_factorials = get_digit_factorials()
        for number in digit_factorials:
            assert number <= upper_limit

    @pytest.mark.slow
    def test_known_digit_factorials(self) -> None:
        """既知の桁階乗数のテスト"""
        # Problem 034で見つかるべき桁階乗数をテスト
        known_factorials = [145]  # 問題文の例

        for number in known_factorials:
            assert is_digit_factorial(number)
            assert digit_factorial_sum(number) == number

        # これらが結果に含まれることを確認
        digit_factorials = get_digit_factorials()
        for number in known_factorials:
            assert number in digit_factorials

    def test_factorial_correctness(self) -> None:
        """階乗計算の正確性をテスト"""
        # 手動計算との比較
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
        assert factorial(6) == 720
        assert factorial(7) == 5040
        assert factorial(8) == 40320
        assert factorial(9) == 362880
