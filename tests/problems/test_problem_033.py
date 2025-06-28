#!/usr/bin/env python3
"""
Test for Problem 033: Digit cancelling fractions
"""

import pytest

from problems.problem_033 import (
    gcd,
    get_digit_cancelling_fractions,
    is_digit_cancelling_fraction,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem033:
    """Problem 033のテストクラス"""

    def test_gcd(self) -> None:
        """最大公約数関数のテスト"""
        assert gcd(12, 8) == 4
        assert gcd(48, 18) == 6
        assert gcd(7, 13) == 1
        assert gcd(100, 50) == 50
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5

    def test_is_digit_cancelling_fraction(self) -> None:
        """桁キャンセル分数判定関数のテスト"""
        # 既知の桁キャンセル分数
        assert is_digit_cancelling_fraction(49, 98) is True  # 49/98 = 4/8
        assert is_digit_cancelling_fraction(16, 64) is True  # 16/64 = 1/4
        assert is_digit_cancelling_fraction(26, 65) is True  # 26/65 = 2/5
        assert is_digit_cancelling_fraction(19, 95) is True  # 19/95 = 1/5

        # 自明な例（除外されるべき）
        assert is_digit_cancelling_fraction(30, 50) is False  # 30/50 = 3/5 (自明)
        assert is_digit_cancelling_fraction(40, 80) is False  # 40/80 = 4/8 (自明)

        # 桁キャンセルできるが結果が異なる
        assert is_digit_cancelling_fraction(12, 21) is False  # 12/21 ≠ 1/2
        assert is_digit_cancelling_fraction(13, 31) is False  # 13/31 ≠ 1/3

        # 共通桁がない
        assert is_digit_cancelling_fraction(12, 34) is False
        assert is_digit_cancelling_fraction(23, 45) is False

        # 分数が1以上
        assert is_digit_cancelling_fraction(98, 49) is False  # 元の分数の逆
        assert is_digit_cancelling_fraction(64, 16) is False  # 元の分数の逆

        # 1桁の数字
        assert is_digit_cancelling_fraction(4, 8) is False
        assert is_digit_cancelling_fraction(9, 98) is False
        assert is_digit_cancelling_fraction(49, 8) is False

    def test_get_digit_cancelling_fractions(self) -> None:
        """桁キャンセル分数取得関数のテスト"""
        fractions = get_digit_cancelling_fractions()

        # 正確に4つの分数が見つかることを確認
        assert len(fractions) == 4

        # 既知の分数が含まれることを確認
        expected_fractions = {(16, 64), (26, 65), (19, 95), (49, 98)}
        assert set(fractions) == expected_fractions

        # すべてが1未満であることを確認
        for num, den in fractions:
            assert num < den

        # すべてが2桁であることを確認
        for num, den in fractions:
            assert 10 <= num <= 99
            assert 10 <= den <= 99

    def test_solve_naive(self) -> None:
        """素直な解法のテスト"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0
        # 期待される解答の範囲をテスト
        assert 50 <= result <= 200

    def test_solve_optimized(self) -> None:
        """最適化解法のテスト"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0
        # 期待される解答の範囲をテスト
        assert 50 <= result <= 200

    def test_solve_mathematical(self) -> None:
        """数学的解法のテスト"""
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 0
        # 期待される解答の範囲をテスト
        assert 50 <= result <= 200

    def test_all_solutions_agree(self) -> None:
        """すべての解法が同じ結果を返すことを確認"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert naive_result == optimized_result == mathematical_result

    def test_fraction_properties(self) -> None:
        """分数の性質をテスト"""
        fractions = get_digit_cancelling_fractions()

        for num, den in fractions:
            # 各分数が実際に桁キャンセル分数であることを確認
            assert is_digit_cancelling_fraction(num, den)

            # 分数値の検証
            original_value = num / den
            assert 0 < original_value < 1

            # 桁キャンセル後の値が同じであることを確認
            n1, n2 = divmod(num, 10)
            d1, d2 = divmod(den, 10)

            cancelled_found = False

            if n1 == d1 and n1 != 0 and d2 != 0:
                cancelled_value = n2 / d2
                assert abs(original_value - cancelled_value) < 1e-10
                cancelled_found = True
            elif n1 == d2 and n1 != 0 and d1 != 0:
                cancelled_value = n2 / d1
                assert abs(original_value - cancelled_value) < 1e-10
                cancelled_found = True
            elif n2 == d1 and n2 != 0 and d2 != 0:
                cancelled_value = n1 / d2
                assert abs(original_value - cancelled_value) < 1e-10
                cancelled_found = True
            elif n2 == d2 and n2 != 0 and d1 != 0:
                cancelled_value = n1 / d1
                assert abs(original_value - cancelled_value) < 1e-10
                cancelled_found = True

            assert cancelled_found, f"No valid cancellation found for {num}/{den}"

    def test_product_calculation(self) -> None:
        """積の計算をテスト"""
        fractions = get_digit_cancelling_fractions()

        # 手動で積を計算
        product_num = 1
        product_den = 1
        for num, den in fractions:
            product_num *= num
            product_den *= den

        # 最大公約数で約分
        common_divisor = gcd(product_num, product_den)
        reduced_denominator = product_den // common_divisor

        # 各解法の結果と一致することを確認
        assert solve_naive() == reduced_denominator
        assert solve_optimized() == reduced_denominator
        assert solve_mathematical() == reduced_denominator

    @pytest.mark.slow
    def test_performance_comparison(self) -> None:
        """パフォーマンス比較のテスト（時間測定）"""
        import time

        # 素直な解法
        start_time = time.time()
        result_naive = solve_naive()
        naive_time = time.time() - start_time

        # 最適化解法
        start_time = time.time()
        result_optimized = solve_optimized()
        optimized_time = time.time() - start_time

        # 数学的解法
        start_time = time.time()
        result_mathematical = solve_mathematical()
        mathematical_time = time.time() - start_time

        # 結果が一致することを確認
        assert result_naive == result_optimized == result_mathematical

        # 最適化解法の方が高速であることを期待
        print(f"素直な解法: {naive_time:.6f}秒")
        print(f"最適化解法: {optimized_time:.6f}秒")
        print(f"数学的解法: {mathematical_time:.6f}秒")

        # 全ての解法が妥当な時間内で実行されることを確認
        assert naive_time < 5.0  # 5秒以内
        assert optimized_time < 1.0  # 1秒以内
        assert mathematical_time < 1.0  # 1秒以内

    def test_edge_cases(self) -> None:
        """エッジケースのテスト"""
        # 境界値での桁キャンセル分数判定
        assert is_digit_cancelling_fraction(10, 20) is False  # 最小の2桁数
        assert is_digit_cancelling_fraction(99, 99) is False  # 同じ数字

        # ゼロを含む場合
        assert is_digit_cancelling_fraction(10, 50) is False  # 分子に0
        assert is_digit_cancelling_fraction(15, 50) is False  # 分母に0

    def test_mathematical_verification(self) -> None:
        """数学的な検証"""
        # 既知の例の詳細検証
        test_cases = [
            (49, 98, 4, 8),  # 49/98 = 4/8
            (16, 64, 1, 4),  # 16/64 = 1/4
            (26, 65, 2, 5),  # 26/65 = 2/5
            (19, 95, 1, 5),  # 19/95 = 1/5
        ]

        for orig_num, orig_den, canc_num, canc_den in test_cases:
            # 元の分数とキャンセル後の分数が等しいことを確認
            assert orig_num * canc_den == orig_den * canc_num

            # 桁キャンセル分数として判定されることを確認
            assert is_digit_cancelling_fraction(orig_num, orig_den)

            # 分数値が等しいことを確認
            orig_value = orig_num / orig_den
            canc_value = canc_num / canc_den
            assert abs(orig_value - canc_value) < 1e-10