#!/usr/bin/env python3
"""
Tests for Problem 069: Totient maximum

Project Euler Problem 069のテストケース
"""

from collections.abc import Callable

import pytest

from problems.problem_069 import (
    analyze_totient_pattern,
    euler_totient_naive,
    euler_totient_optimized,
    get_totient_ratio,
    solve_mathematical,
    solve_optimized,
)


class TestProblem069:
    """Problem 069のテストクラス"""

    def test_euler_totient_naive_basic_cases(self) -> None:
        """オイラーのφ関数（素直な実装）の基本テストケース"""
        # 基本的な値
        assert euler_totient_naive(1) == 0  # 定義により
        assert euler_totient_naive(2) == 1  # φ(2) = 1 (relatively prime: 1)
        assert euler_totient_naive(3) == 2  # φ(3) = 2 (relatively prime: 1, 2)
        assert euler_totient_naive(4) == 2  # φ(4) = 2 (relatively prime: 1, 3)
        assert euler_totient_naive(5) == 4  # φ(5) = 4 (relatively prime: 1, 2, 3, 4)
        assert euler_totient_naive(6) == 2  # φ(6) = 2 (relatively prime: 1, 5)
        assert (
            euler_totient_naive(9) == 6
        )  # φ(9) = 6 (relatively prime: 1, 2, 4, 5, 7, 8)

    def test_euler_totient_optimized_basic_cases(self) -> None:
        """オイラーのφ関数（最適化実装）の基本テストケース"""
        # 基本的な値
        assert euler_totient_optimized(1) == 0
        assert euler_totient_optimized(2) == 1
        assert euler_totient_optimized(3) == 2
        assert euler_totient_optimized(4) == 2
        assert euler_totient_optimized(5) == 4
        assert euler_totient_optimized(6) == 2
        assert euler_totient_optimized(9) == 6

    def test_euler_totient_consistency(self) -> None:
        """素直な実装と最適化実装の結果が一致することをテスト"""
        # 比較的小さな値で両方の実装をテスト
        for n in range(1, 21):
            naive_result = euler_totient_naive(n)
            optimized_result = euler_totient_optimized(n)
            assert naive_result == optimized_result, (
                f"φ({n}): naive={naive_result}, optimized={optimized_result}"
            )

    def test_euler_totient_prime_numbers(self) -> None:
        """素数に対するφ(p) = p - 1の性質をテスト"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

        for p in primes:
            expected = p - 1
            assert euler_totient_optimized(p) == expected

    def test_euler_totient_prime_powers(self) -> None:
        """素数の冪に対するφ(p^k) = p^k - p^(k-1)の性質をテスト"""
        test_cases = [
            (4, 2),  # φ(2²) = 2² - 2¹ = 4 - 2 = 2
            (8, 4),  # φ(2³) = 2³ - 2² = 8 - 4 = 4
            (9, 6),  # φ(3²) = 3² - 3¹ = 9 - 3 = 6
            (25, 20),  # φ(5²) = 5² - 5¹ = 25 - 5 = 20
        ]

        for n, expected in test_cases:
            assert euler_totient_optimized(n) == expected

    def test_get_totient_ratio(self) -> None:
        """n/φ(n)比率の計算テスト"""
        # 問題文の例
        test_cases = [
            (2, 2.0),  # 2/1 = 2.0
            (3, 1.5),  # 3/2 = 1.5
            (4, 2.0),  # 4/2 = 2.0
            (5, 1.25),  # 5/4 = 1.25
            (6, 3.0),  # 6/2 = 3.0
            (9, 1.5),  # 9/6 = 1.5
            (10, 2.5),  # 10/4 = 2.5
        ]

        for n, expected_ratio in test_cases:
            calculated_ratio = get_totient_ratio(n)
            assert abs(calculated_ratio - expected_ratio) < 1e-10

    def test_solve_optimized_small_case(self) -> None:
        """最適化解法の小さなケースでのテスト"""
        result = solve_optimized(10)
        assert result == 6  # 問題文の例: n≤10で最大比率はn=6

    def test_solve_mathematical_small_case(self) -> None:
        """数学的解法の小さなケースでのテスト"""
        result = solve_mathematical(10)
        assert result == 6  # 問題文の例: n≤10で最大比率はn=6

    def test_solve_consistency(self) -> None:
        """全ての解法が同じ結果を返すことをテスト（小さな範囲）"""
        limit = 100

        result_optimized = solve_optimized(limit)
        result_mathematical = solve_mathematical(limit)

        # 最適化解法と数学的解法は同じ結果を返すべき
        assert result_optimized == result_mathematical

    def test_analyze_totient_pattern(self) -> None:
        """φ(n)パターン分析のテスト"""
        results = analyze_totient_pattern(10)

        # 結果の数は9個（2から10まで）
        assert len(results) == 9

        # 各要素は(n, φ(n), n/φ(n))のタプル
        for n, phi_n, ratio in results:
            assert isinstance(n, int)
            assert isinstance(phi_n, int)
            assert isinstance(ratio, float)
            assert n >= 2
            assert phi_n >= 1
            assert ratio > 0

        # 特定の値を確認
        n6_data = next((data for data in results if data[0] == 6), None)
        assert n6_data is not None
        assert n6_data[1] == 2  # φ(6) = 2
        assert abs(n6_data[2] - 3.0) < 1e-10  # 6/2 = 3.0

    @pytest.mark.parametrize(
        "solve_func",
        [solve_optimized, solve_mathematical],
        ids=["optimized", "mathematical"],
    )
    def test_solution_functions_return_positive(
        self, solve_func: Callable[[int], int]
    ) -> None:
        """全ての解法が正の整数を返すことをテスト"""
        result = solve_func(100)
        assert isinstance(result, int)
        assert result > 0
        assert result <= 100

    def test_mathematical_solution_properties(self) -> None:
        """数学的解法の性質をテスト"""
        # 数学的解法は小さな素数の積を返すべき
        result = solve_mathematical(1000)

        # 結果が素数の積であることを確認
        from problems.lib.primes import get_prime_factors

        factors = sorted(get_prime_factors(result))

        # 連続する小さな素数から始まっているべき
        expected_start = [2, 3, 5, 7]
        assert factors[: len(expected_start)] == expected_start[: len(factors)]

    def test_totient_special_cases(self) -> None:
        """φ関数の特殊ケースのテスト"""
        # φ(1) = 0 (定義による)
        assert euler_totient_optimized(1) == 0

        # 0以下の入力
        assert euler_totient_optimized(0) == 0
        assert euler_totient_optimized(-1) == 0

    @pytest.mark.slow
    def test_solve_large_case(self) -> None:
        """大きなケースでの解法テスト（スロー）"""
        # 実際の問題サイズでのテスト
        result = solve_mathematical(1000000)

        # 結果が範囲内であることを確認
        assert isinstance(result, int)
        assert 1 <= result <= 1000000

        # 結果が期待される値であることを確認
        assert result == 510510  # 2×3×5×7×11×13×17


if __name__ == "__main__":
    pytest.main([__file__])
