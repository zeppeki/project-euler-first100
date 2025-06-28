#!/usr/bin/env python3
"""
Test for Problem 032: Pandigital products
"""

import pytest

from problems.problem_032 import (
    is_pandigital_1_to_9,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem032:
    """Problem 032のテストクラス"""

    def test_is_pandigital_1_to_9(self) -> None:
        """パンデジタル判定関数のテスト"""
        # 正常な1-9パンデジタル
        assert is_pandigital_1_to_9("123456789") is True
        assert is_pandigital_1_to_9("987654321") is True
        assert is_pandigital_1_to_9("391867254") is True  # 39 × 186 × 7254

        # 異常ケース
        assert is_pandigital_1_to_9("123456788") is False  # 8が重複
        assert is_pandigital_1_to_9("12345679") is False  # 8文字（不足）
        assert is_pandigital_1_to_9("1234567890") is False  # 10文字（過多）
        assert is_pandigital_1_to_9("023456789") is False  # 0を含む
        assert is_pandigital_1_to_9("123456780") is False  # 0を含む、9がない

    def test_known_pandigital_products(self) -> None:
        """既知のパンデジタル積の例をテスト"""
        # 例題で示されている組み合わせ
        examples = [
            (39, 186, 7254),  # 39 × 186 = 7254
            (4, 1738, 6952),  # 4 × 1738 = 6952 (推定)
            (4, 1963, 7852),  # 4 × 1963 = 7852 (推定)
        ]

        for multiplicand, multiplier, expected_product in examples:
            # 乗算が正しいことを確認
            assert multiplicand * multiplier == expected_product

            # パンデジタル条件を満たすことを確認
            combined = str(multiplicand) + str(multiplier) + str(expected_product)
            if len(combined) == 9:  # 9桁の場合のみテスト
                assert is_pandigital_1_to_9(combined)

    def test_solve_naive(self) -> None:
        """素直な解法のテスト"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0
        # 期待される解答の範囲をテスト（具体的な値は隠匿）
        assert 40000 <= result <= 50000

    def test_solve_optimized(self) -> None:
        """最適化解法のテスト"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0
        # 期待される解答の範囲をテスト
        assert 40000 <= result <= 50000

    def test_solve_mathematical(self) -> None:
        """数学的解法のテスト"""
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 0
        # 期待される解答の範囲をテスト
        assert 40000 <= result <= 50000

    def test_all_solutions_agree(self) -> None:
        """すべての解法が同じ結果を返すことを確認"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert naive_result == optimized_result == mathematical_result

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

        # 最適化解法の方が高速であることを期待（絶対的ではない）
        print(f"素直な解法: {naive_time:.6f}秒")
        print(f"最適化解法: {optimized_time:.6f}秒")
        print(f"数学的解法: {mathematical_time:.6f}秒")

        # 全ての解法が妥当な時間内で実行されることを確認
        assert naive_time < 10.0  # 10秒以内
        assert optimized_time < 5.0  # 5秒以内
        assert mathematical_time < 5.0  # 5秒以内

    def test_edge_cases(self) -> None:
        """エッジケースのテスト"""
        # パンデジタル判定のエッジケース
        assert is_pandigital_1_to_9("") is False
        assert is_pandigital_1_to_9("1") is False
        assert is_pandigital_1_to_9("123456789123456789") is False

        # 重複数字
        assert is_pandigital_1_to_9("111111111") is False
        assert is_pandigital_1_to_9("123123123") is False

    def test_digit_patterns(self) -> None:
        """桁数パターンのテスト"""
        # 1桁 × 4桁 = 4桁パターンの検証
        # 例: 4 × 1738 = 6952 → "417386952"
        combined_1 = "417386952"
        assert len(combined_1) == 9
        assert is_pandigital_1_to_9(combined_1)

        # 2桁 × 3桁 = 4桁パターンの検証
        # 例: 39 × 186 = 7254 → "391867254"
        combined_2 = "391867254"
        assert len(combined_2) == 9
        assert is_pandigital_1_to_9(combined_2)
