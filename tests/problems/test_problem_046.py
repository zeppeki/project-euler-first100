#!/usr/bin/env python3
"""
Tests for Project Euler Problem 046: Goldbach's other conjecture
"""

from collections.abc import Callable

import pytest

from problems.problem_046 import (
    can_be_written_as_conjecture,
    generate_primes,
    is_perfect_square,
    is_prime,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestHelperFunctions:
    """ヘルパー関数のテスト"""

    def test_is_prime(self) -> None:
        """素数判定のテスト"""
        # 素数
        assert is_prime(2)
        assert is_prime(3)
        assert is_prime(5)
        assert is_prime(7)
        assert is_prime(11)
        assert is_prime(13)
        assert is_prime(17)
        assert is_prime(19)
        assert is_prime(23)
        assert is_prime(29)

        # 非素数
        assert not is_prime(0)
        assert not is_prime(1)
        assert not is_prime(4)
        assert not is_prime(6)
        assert not is_prime(8)
        assert not is_prime(9)
        assert not is_prime(10)
        assert not is_prime(12)
        assert not is_prime(14)
        assert not is_prime(15)
        assert not is_prime(16)
        assert not is_prime(18)
        assert not is_prime(20)

    def test_is_perfect_square(self) -> None:
        """完全平方数判定のテスト"""
        # 完全平方数
        assert is_perfect_square(0)
        assert is_perfect_square(1)
        assert is_perfect_square(4)
        assert is_perfect_square(9)
        assert is_perfect_square(16)
        assert is_perfect_square(25)
        assert is_perfect_square(36)
        assert is_perfect_square(49)
        assert is_perfect_square(64)
        assert is_perfect_square(81)
        assert is_perfect_square(100)

        # 完全平方数ではない
        assert not is_perfect_square(-1)
        assert not is_perfect_square(2)
        assert not is_perfect_square(3)
        assert not is_perfect_square(5)
        assert not is_perfect_square(6)
        assert not is_perfect_square(7)
        assert not is_perfect_square(8)
        assert not is_perfect_square(10)
        assert not is_perfect_square(15)
        assert not is_perfect_square(24)

    def test_generate_primes(self) -> None:
        """素数生成のテスト"""
        # 小さい範囲
        assert generate_primes(1) == []
        assert generate_primes(2) == [2]
        assert generate_primes(10) == [2, 3, 5, 7]
        assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

        # より大きい範囲
        primes_100 = generate_primes(100)
        expected_primes_100 = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]
        assert primes_100 == expected_primes_100

    def test_can_be_written_as_conjecture(self) -> None:
        """ゴールドバッハの他の予想判定のテスト"""
        primes = generate_primes(100)

        # 予想が成り立つ例
        assert can_be_written_as_conjecture(9, primes)  # 9 = 7 + 2×1²
        assert can_be_written_as_conjecture(15, primes)  # 15 = 7 + 2×2²
        assert can_be_written_as_conjecture(21, primes)  # 21 = 3 + 2×3²
        assert can_be_written_as_conjecture(25, primes)  # 25 = 7 + 2×3²
        assert can_be_written_as_conjecture(27, primes)  # 27 = 19 + 2×2²

        # 予想が成り立たない例（問題の答え）
        assert not can_be_written_as_conjecture(5777, primes)


class TestSolutions:
    """解法のテスト"""

    @pytest.mark.parametrize(
        "solve_func", [solve_naive, solve_optimized, solve_mathematical]
    )
    def test_small_limits(self, solve_func: Callable[[int], int]) -> None:
        """小さい制限での基本テスト"""
        # 6000以下で最初の反例を見つける
        result = solve_func(6000)
        assert result > 0, (
            f"{solve_func.__name__} should find a counterexample within limit 6000"
        )

    @pytest.mark.parametrize(
        "solve_func", [solve_naive, solve_optimized, solve_mathematical]
    )
    def test_known_result(self, solve_func: Callable[[int], int]) -> None:
        """既知の結果でのテスト"""
        result = solve_func(6000)
        assert result == 5777, f"{solve_func.__name__} should return 5777"

    def test_solution_consistency(self) -> None:
        """すべての解法が同じ結果を返すことを確認"""
        limit = 6000
        result_naive = solve_naive(limit)
        result_optimized = solve_optimized(limit)
        result_mathematical = solve_mathematical(limit)

        assert result_naive == result_optimized == result_mathematical, (
            f"Solutions disagree: naive={result_naive}, optimized={result_optimized}, mathematical={result_mathematical}"
        )

    @pytest.mark.slow
    @pytest.mark.parametrize("solve_func", [solve_optimized, solve_mathematical])
    def test_performance_with_larger_limit(
        self, solve_func: Callable[[int], int]
    ) -> None:
        """より大きい制限での性能テスト（最適化された解法のみ）"""
        result = solve_func(10000)
        assert result == 5777, (
            f"{solve_func.__name__} should handle larger limits efficiently"
        )


class TestEdgeCases:
    """エッジケースのテスト"""

    def test_empty_and_small_inputs(self) -> None:
        """空や小さい入力のテスト"""
        # 制限が小さすぎる場合
        assert solve_optimized(1) == -1
        assert solve_optimized(8) == -1  # 9未満では奇数合成数が存在しない

    def test_conjecture_examples(self) -> None:
        """問題文の例を検証"""
        primes = generate_primes(100)

        # 問題文の例
        examples = [
            (9, 7, 1),  # 9 = 7 + 2×1²
            (15, 7, 2),  # 15 = 7 + 2×2²
            (21, 3, 3),  # 21 = 3 + 2×3²
            (25, 7, 3),  # 25 = 7 + 2×3²
            (27, 19, 2),  # 27 = 19 + 2×2²
            (33, 31, 1),  # 33 = 31 + 2×1²
        ]

        for num, expected_prime, expected_k in examples:
            assert can_be_written_as_conjecture(num, primes), (
                f"{num} should satisfy the conjecture"
            )

            # 具体的な分解を確認
            remainder = num - expected_prime
            assert remainder > 0 and remainder % 2 == 0
            k_squared = remainder // 2
            assert is_perfect_square(k_squared)
            import math

            k = int(math.sqrt(k_squared))
            assert k == expected_k, f"{num} = {expected_prime} + 2×{expected_k}²"

    def test_first_counterexample_properties(self) -> None:
        """最初の反例の性質を確認"""
        result = solve_optimized(6000)

        # 5777が最初の反例であることを確認
        assert result == 5777

        # 5777は奇数合成数であることを確認
        assert result % 2 == 1  # 奇数
        assert not is_prime(result)  # 合成数

        # 5777未満の奇数合成数はすべて予想を満たすことを確認
        primes = generate_primes(result)
        for n in range(9, result, 2):
            if not is_prime(n):  # 奇数合成数
                assert can_be_written_as_conjecture(n, primes), (
                    f"{n} should satisfy the conjecture (it's before the first counterexample)"
                )


def test_runner_integration() -> None:
    """ランナーとの統合テスト"""
    from problems.runners.problem_046_runner import Problem046Runner

    runner = Problem046Runner()

    # テストケースの確認
    test_cases = runner.get_test_cases()
    assert len(test_cases) > 0

    # 解法関数の確認
    solution_functions = runner.get_solution_functions()
    assert len(solution_functions) == 3

    # メインパラメータの確認
    main_params = runner.get_main_parameters()
    assert len(main_params) == 1

    # デモンストレーション関数の確認
    demo_functions = runner.get_demonstration_functions()
    assert demo_functions is not None and len(demo_functions) > 0
