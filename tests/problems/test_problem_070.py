#!/usr/bin/env python3
"""
Tests for Problem 070: Totient permutation

Project Euler Problem 070のテストケース
"""

from collections.abc import Callable

import pytest

from problems.problem_070 import (
    analyze_totient_permutation_example,
    euler_totient,
    find_totient_permutations,
    is_permutation,
    solve_mathematical,
    solve_optimized,
)


class TestProblem070:
    """Problem 070のテストクラス"""

    def test_euler_totient_basic_cases(self) -> None:
        """オイラーのトーシェント関数の基本テストケース"""
        # 基本的な値
        assert euler_totient(1) == 1
        assert euler_totient(2) == 1  # φ(2) = 1
        assert euler_totient(3) == 2  # φ(3) = 2
        assert euler_totient(4) == 2  # φ(4) = 2
        assert euler_totient(5) == 4  # φ(5) = 4
        assert euler_totient(6) == 2  # φ(6) = 2
        assert euler_totient(9) == 6  # φ(9) = 6

    def test_euler_totient_prime_pairs(self) -> None:
        """2つの素数の積に対するトーシェント関数のテスト"""
        # φ(p*q) = (p-1)(q-1) for distinct primes p, q
        test_cases = [
            (6, 2),  # φ(2×3) = (2-1)×(3-1) = 1×2 = 2
            (15, 8),  # φ(3×5) = (3-1)×(5-1) = 2×4 = 8
            (21, 12),  # φ(3×7) = (3-1)×(7-1) = 2×6 = 12
            (35, 24),  # φ(5×7) = (5-1)×(7-1) = 4×6 = 24
        ]

        for n, expected in test_cases:
            assert euler_totient(n) == expected

    def test_is_permutation_basic_cases(self) -> None:
        """順列判定関数の基本テストケース"""
        # 同じ数値
        assert is_permutation(123, 123)

        # 順列の例
        assert is_permutation(123, 321)
        assert is_permutation(87109, 79180)  # 問題文の例
        assert is_permutation(1234, 4321)

        # 順列でない例
        assert not is_permutation(123, 124)
        assert not is_permutation(123, 1234)
        assert not is_permutation(100, 10)

    def test_is_permutation_edge_cases(self) -> None:
        """順列判定の境界ケース"""
        # 1桁の数
        assert is_permutation(1, 1)
        assert not is_permutation(1, 2)

        # 0を含む数
        assert is_permutation(102, 210)
        assert not is_permutation(1000, 1)  # 実際には異なる数値（桁数も違う）

        # 異なる桁数
        assert not is_permutation(12, 123)

    def test_analyze_totient_permutation_example(self) -> None:
        """問題文の例（87109）の分析テスト"""
        n, phi_n, ratio = analyze_totient_permutation_example()

        assert n == 87109
        assert phi_n == 79180  # 問題文に記載の値
        assert is_permutation(n, phi_n)
        assert abs(ratio - (87109 / 79180)) < 1e-10

    def test_find_totient_permutations_small_range(self) -> None:
        """小規模範囲でのトーシェント順列探索"""
        results = find_totient_permutations(1000, max_results=5)

        # 結果の形式確認
        for n, phi_n, ratio in results:
            assert isinstance(n, int)
            assert isinstance(phi_n, int)
            assert isinstance(ratio, float)
            assert n > 1
            assert phi_n > 0
            assert ratio > 1.0  # n/φ(n) > 1
            assert is_permutation(n, phi_n)

        # 比率でソートされていることを確認
        if len(results) > 1:
            for i in range(len(results) - 1):
                assert results[i][2] <= results[i + 1][2]

    def test_solve_optimized_small_case(self) -> None:
        """最適化解法の小さなケースでのテスト"""
        result = solve_optimized(1000)

        if result > 0:  # 解が見つかった場合
            phi_result = euler_totient(result)
            assert is_permutation(result, phi_result)
            assert result < 1000

    def test_solve_mathematical_small_case(self) -> None:
        """数学的解法の小さなケースでのテスト"""
        result = solve_mathematical(1000)

        if result > 0:  # 解が見つかった場合
            phi_result = euler_totient(result)
            assert is_permutation(result, phi_result)
            assert result < 1000

    def test_solve_consistency_small_range(self) -> None:
        """解法間の一貫性テスト（小さな範囲）"""
        limit = 1000

        result_optimized = solve_optimized(limit)
        result_mathematical = solve_mathematical(limit)

        # 両方とも同じ結果を返すか、両方とも0を返すべき
        assert result_optimized == result_mathematical

    @pytest.mark.parametrize(
        "solve_func",
        [solve_optimized, solve_mathematical],
        ids=["optimized", "mathematical"],
    )
    def test_solution_functions_return_valid_result(
        self, solve_func: Callable[[int], int]
    ) -> None:
        """全ての解法が有効な結果を返すことをテスト"""
        result = solve_func(10000)

        if result > 0:  # 解が見つかった場合
            assert isinstance(result, int)
            assert result > 1
            assert result < 10000

            phi_result = euler_totient(result)
            assert is_permutation(result, phi_result)

    def test_totient_permutation_properties(self) -> None:
        """トーシェント順列の数学的性質のテスト"""
        # 知られている例をテスト
        test_cases = [
            21,  # φ(21) = 12, 順列: 21 ↔ 12
        ]

        for n in test_cases:
            phi_n = euler_totient(n)
            if is_permutation(n, phi_n):
                # 比率が1より大きいことを確認
                ratio = n / phi_n
                assert ratio > 1.0

    def test_prime_pair_totient_calculation(self) -> None:
        """素数ペアに対するトーシェント計算の正確性"""
        # 既知の素数ペア
        prime_pairs = [(3, 5), (5, 7), (7, 11), (11, 13)]

        for p, q in prime_pairs:
            n = p * q
            phi_n_formula = (p - 1) * (q - 1)
            phi_n_function = euler_totient(n)

            assert phi_n_formula == phi_n_function

    def test_permutation_with_leading_zeros(self) -> None:
        """先頭ゼロを含む順列の処理"""
        # 実際の数値では先頭ゼロは存在しないが、
        # 内部的な文字列比較での処理を確認
        assert is_permutation(1023, 3210)
        assert not is_permutation(1000, 1)  # "1000" vs "1" -> False (different lengths)

    @pytest.mark.slow
    def test_solve_medium_case(self) -> None:
        """中規模ケースでの解法テスト（スロー）"""
        # より大きな範囲でのテスト
        result = solve_mathematical(100000)

        if result > 0:
            assert isinstance(result, int)
            assert 1 < result < 100000

            phi_result = euler_totient(result)
            assert is_permutation(result, phi_result)

            # 比率が合理的な範囲内であることを確認
            ratio = result / phi_result
            assert 1.0 < ratio < 2.0  # 理論的な上限

    def test_euler_totient_edge_cases(self) -> None:
        """トーシェント関数のエッジケース"""
        # 境界値
        assert euler_totient(0) == 0
        assert euler_totient(1) == 1

        # 大きな素数
        large_prime = 97
        assert euler_totient(large_prime) == large_prime - 1

    def test_large_permutation_check(self) -> None:
        """大きな数値での順列チェック"""
        # 問題文の例
        assert is_permutation(87109, 79180)

        # より大きな例
        a = 1234567
        b = 7654321
        assert is_permutation(a, b)


if __name__ == "__main__":
    pytest.main([__file__])
