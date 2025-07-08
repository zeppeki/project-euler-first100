"""
Tests for Problem 77: Prime summations
"""

from collections.abc import Callable

import pytest

from problems.problem_077 import (
    count_prime_partitions,
    generate_primes,
    solve_naive,
    solve_optimized,
)


class TestProblem077:
    """Problem 77のテストクラス"""

    def test_generate_primes(self) -> None:
        """素数生成のテスト"""
        assert generate_primes(1) == []
        assert generate_primes(2) == [2]
        assert generate_primes(10) == [2, 3, 5, 7]
        assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
        assert generate_primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_count_prime_partitions(self) -> None:
        """素数分割数計算のテスト"""
        # 問題文の例: 10の素数分割
        primes = generate_primes(10)
        assert count_prime_partitions(10, primes) == 5

        # 小さい値でのテスト
        test_cases = [
            (2, 1),  # 2 = 2
            (3, 1),  # 3 = 3
            (4, 1),  # 4 = 2 + 2
            (5, 2),  # 5 = 5, 3 + 2
            (6, 2),  # 6 = 3 + 3, 2 + 2 + 2
            (7, 3),  # 7 = 7, 5 + 2, 3 + 2 + 2
            (8, 3),  # 8 = 5 + 3, 3 + 3 + 2, 2 + 2 + 2 + 2
            (9, 4),  # 9 = 7 + 2, 5 + 2 + 2, 3 + 3 + 3, 3 + 2 + 2 + 2
        ]

        for n, expected in test_cases:
            primes = generate_primes(n)
            result = count_prime_partitions(n, primes)
            assert result == expected, (
                f"Failed for n={n}: expected {expected}, got {result}"
            )

    @pytest.mark.parametrize("func", [solve_naive, solve_optimized])
    def test_small_targets(self, func: Callable[[int], int]) -> None:
        """小さい目標値でのテスト"""
        # 10通り以上の素数分割を持つ最初の数
        result = func(10)
        primes = generate_primes(result)
        ways = count_prime_partitions(result, primes)
        assert ways > 10

        # 結果が正しいことを確認（1つ前の数では10通り以下）
        if result > 2:
            primes_prev = generate_primes(result - 1)
            ways_prev = count_prime_partitions(result - 1, primes_prev)
            assert ways_prev <= 10

    def test_solution_consistency(self) -> None:
        """異なる解法の結果が一致することを確認"""
        test_targets = [5, 10, 20, 50, 100]

        for target in test_targets:
            naive_result = solve_naive(target)
            optimized_result = solve_optimized(target)
            assert naive_result == optimized_result, (
                f"Solutions disagree for target={target}"
            )

    @pytest.mark.slow
    def test_project_euler(self) -> None:
        """Project Eulerの問題を解く"""
        target = 5000

        # 両方の解法を実行
        naive_result = solve_naive(target)
        optimized_result = solve_optimized(target)

        # 結果が一致することを確認
        assert naive_result == optimized_result

        # 結果が正の整数であることを確認
        assert isinstance(naive_result, int)
        assert naive_result > 0

        # 実際に5000通り以上の分割を持つことを確認
        primes = generate_primes(naive_result)
        ways = count_prime_partitions(naive_result, primes)
        assert ways > target

        # Project Eulerの回答確認用（実際の値は表示しない）
        print(
            f"\nProblem 77 - 素数の和で{target}通り以上表せる最初の数: {naive_result}"
        )
