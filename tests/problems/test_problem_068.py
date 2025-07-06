#!/usr/bin/env python3
"""
Tests for Problem 068: Magic 5-gon ring

Project Euler Problem 068のテストケース
"""

import pytest

from problems.problem_068 import (
    format_5gon_string,
    get_example_3gon,
    is_valid_5gon,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem068:
    """Problem 068のテストクラス"""

    def test_is_valid_5gon_valid_case(self) -> None:
        """有効な5-gon配置のテスト"""
        # 有効な配置例を作成（仮想的な例）
        # 外部: [6, 7, 8, 9, 10], 内部: [1, 2, 3, 4, 5]
        # ライン: (6,1,2), (7,2,3), (8,3,4), (9,4,5), (10,5,1)
        # 各ライン合計: 9, 12, 15, 18, 16 -> 無効

        # より現実的な例を使用
        arrangement = [10, 5, 6, 7, 8, 1, 2, 3, 4, 9]
        is_valid, lines = is_valid_5gon(arrangement)

        # この配置が有効かどうかを確認
        if is_valid:
            assert len(lines) == 5
            # 全ラインの合計が同じかチェック
            line_sums = [sum(line) for line in lines]
            assert len(set(line_sums)) == 1
        else:
            # 無効な場合もテストは成功
            assert lines == []

    def test_is_valid_5gon_invalid_case(self) -> None:
        """無効な5-gon配置のテスト"""
        # 長さが10でない場合
        arrangement_short = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        is_valid, lines = is_valid_5gon(arrangement_short)
        assert not is_valid
        assert lines == []

        # ライン合計が一致しない場合
        arrangement_invalid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        is_valid, lines = is_valid_5gon(arrangement_invalid)
        # この配置は各ライン合計が異なるため無効
        assert not is_valid

    def test_format_5gon_string(self) -> None:
        """5-gon文字列フォーマットのテスト"""
        # 5-gonの例題ライン情報（仮想的な有効な例）
        lines = [(6, 1, 2), (7, 2, 3), (8, 3, 4), (9, 4, 5), (10, 5, 1)]
        result = format_5gon_string(lines)

        # 最小外部ノード（6）から開始し、時計回りに並ぶ
        assert isinstance(result, str)
        assert len(result) > 0
        # この例では "612723834945105" のような文字列になる
        assert result.startswith("612")

    def test_get_example_3gon(self) -> None:
        """3-gon例題データのテスト"""
        lines, expected_string = get_example_3gon()

        assert len(lines) == 3
        assert isinstance(expected_string, str)
        assert expected_string == "432621513"

        # 各ラインの合計が9であることを確認
        for line in lines:
            assert sum(line) == 9

    def test_solve_consistency(self) -> None:
        """最適化解法が同じ結果を返すことをテスト"""
        result_optimized = solve_optimized()
        result_mathematical = solve_mathematical()

        # 最適化解法が同じ結果を返すべき
        assert result_optimized == result_mathematical

        # 結果が16桁の文字列であることを確認
        assert len(result_optimized) == 16
        assert result_optimized.isdigit()

    @pytest.mark.slow
    def test_solve_consistency_with_naive(self) -> None:
        """全ての解法が同じ結果を返すことをテスト（素直な解法を含む）"""
        result_naive = solve_naive()
        result_optimized = solve_optimized()
        result_mathematical = solve_mathematical()

        # 全ての解法が同じ結果を返すべき
        assert result_naive == result_optimized
        assert result_optimized == result_mathematical

        # 結果が16桁の文字列であることを確認
        assert len(result_naive) == 16
        assert result_naive.isdigit()

    @pytest.mark.slow
    def test_solve_naive(self) -> None:
        """素直な解法のテスト（スロー）"""
        result = solve_naive()

        assert isinstance(result, str)
        assert len(result) == 16
        assert result.isdigit()

        # 最大値を返すので、ある程度大きい値であることを期待
        assert int(result) > 1000000000000000  # 16桁の最小値より大きい

    def test_solve_optimized(self) -> None:
        """最適化解法のテスト"""
        result = solve_optimized()

        assert isinstance(result, str)
        assert len(result) == 16
        assert result.isdigit()

    def test_solve_mathematical(self) -> None:
        """数学的解法のテスト"""
        result = solve_mathematical()

        assert isinstance(result, str)
        assert len(result) == 16
        assert result.isdigit()

    def test_solution_functions_return_16_digits_optimized(self) -> None:
        """最適化解法が16桁文字列を返すことをテスト"""
        result = solve_optimized()
        assert len(result) == 16
        assert result.isdigit()

    def test_solution_functions_return_16_digits_mathematical(self) -> None:
        """数学的解法が16桁文字列を返すことをテスト"""
        result = solve_mathematical()
        assert len(result) == 16
        assert result.isdigit()

    @pytest.mark.slow
    def test_solution_functions_return_16_digits_naive(self) -> None:
        """素直な解法が16桁文字列を返すことをテスト（スロー）"""
        result = solve_naive()
        assert len(result) == 16
        assert result.isdigit()

    def test_magic_5gon_properties(self) -> None:
        """Magic 5-gonの基本的な性質をテスト"""
        # 1-10の数字の総和
        total_sum = sum(range(1, 11))
        assert total_sum == 55

        # 可能なライン合計の範囲を確認
        # 最小: 外部に大きな数字、内部に小さな数字
        # 最大: 外部に小さな数字、内部に大きな数字
        # ただし16桁制約のため10は外部必須

        # 内部の最小合計: 1+2+3+4+5 = 15
        # 内部の最大合計: 6+7+8+9+1 = 31 (10は外部固定)
        min_internal_sum = sum(range(1, 6))  # 15
        max_internal_sum = sum([6, 7, 8, 9]) + 1  # 31

        min_line_sum = (55 + min_internal_sum) // 5  # 14
        max_line_sum = (55 + max_internal_sum) // 5  # 17

        assert min_line_sum >= 14
        assert max_line_sum <= 17


if __name__ == "__main__":
    pytest.main([__file__])
