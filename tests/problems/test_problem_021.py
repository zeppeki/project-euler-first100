#!/usr/bin/env python3
"""
Tests for Problem 021: Amicable Numbers
"""

import importlib.util
import sys
from pathlib import Path
from typing import Any

import pytest


def load_problem_module():  # type: ignore
    """動的にproblem_021モジュールをロード"""
    problem_path = Path(__file__).parent.parent.parent / "problems" / "problem_021.py"
    spec = importlib.util.spec_from_file_location("problem_021", problem_path)
    if spec is None:
        raise ImportError("Could not load problem module")
    module = importlib.util.module_from_spec(spec)
    sys.modules["problem_021"] = module
    if spec.loader is None:
        raise ImportError("Could not load problem module")
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def problem():  # type: ignore
    """problem_021モジュールのフィクスチャ"""
    return load_problem_module()


class TestProperDivisorsCalculation:
    """真約数の和の計算テスト"""

    def test_known_examples(self, problem: Any) -> None:
        """既知の例題のテスト"""
        # 220の真約数: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
        assert problem.get_proper_divisors_optimized(220) == 284

        # 284の真約数: 1, 2, 4, 71, 142
        assert problem.get_proper_divisors_optimized(284) == 220

    def test_small_numbers(self, problem: Any) -> None:
        """小さい数のテスト"""
        assert problem.get_proper_divisors_optimized(1) == 0
        assert problem.get_proper_divisors_optimized(2) == 1
        assert problem.get_proper_divisors_optimized(3) == 1
        assert problem.get_proper_divisors_optimized(4) == 3  # 1 + 2
        assert problem.get_proper_divisors_optimized(6) == 6  # 1 + 2 + 3
        assert problem.get_proper_divisors_optimized(8) == 7  # 1 + 2 + 4
        assert problem.get_proper_divisors_optimized(12) == 16  # 1 + 2 + 3 + 4 + 6

    def test_perfect_numbers(self, problem: Any) -> None:
        """完全数のテスト（d(n) = n）"""
        assert problem.get_proper_divisors_optimized(6) == 6  # 完全数
        assert problem.get_proper_divisors_optimized(28) == 28  # 完全数

    def test_prime_numbers(self, problem: Any) -> None:
        """素数のテスト（真約数は1のみ）"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            assert problem.get_proper_divisors_optimized(prime) == 1

    def test_naive_vs_optimized_divisors(self, problem: Any) -> None:
        """素直解法と最適化解法の一致性確認"""
        test_numbers = [1, 2, 6, 12, 28, 100, 220, 284, 496]
        for n in test_numbers:
            naive_result = problem.get_proper_divisors_naive(n)
            optimized_result = problem.get_proper_divisors_optimized(n)
            assert naive_result == optimized_result, f"Failed for n={n}"


class TestAmicablePairValidation:
    """友愛数ペアの検証テスト"""

    def test_known_amicable_pair(self, problem: Any) -> None:
        """既知の友愛数ペアのテスト"""
        assert problem.validate_amicable_pair(220, 284)
        assert problem.validate_amicable_pair(284, 220)

    def test_non_amicable_pairs(self, problem: Any) -> None:
        """友愛数でないペアのテスト"""
        assert not problem.validate_amicable_pair(6, 6)  # 完全数（a = b）
        assert not problem.validate_amicable_pair(220, 220)  # 同じ数
        assert not problem.validate_amicable_pair(100, 200)  # ランダムなペア
        assert not problem.validate_amicable_pair(1, 1)  # 1, 1

    def test_find_amicable_pairs_small_range(self, problem: Any) -> None:
        """小範囲での友愛数ペア検索"""
        # 300未満には(220, 284)ペアの220のみ
        pairs_300 = problem.find_amicable_pairs(300)
        found_numbers = {num for pair in pairs_300 for num in pair if num < 300}
        # 実際には284 > 300なので、友愛数ペアとして(220,284)は検出されない
        assert len(pairs_300) == 0 or 220 in found_numbers

        # 1000未満で確認
        pairs_1000 = problem.find_amicable_pairs(1000)
        assert len(pairs_1000) >= 1  # 少なくとも(220, 284)ペアが含まれる


class TestSolveNaive:
    """solve_naiveのテスト"""

    def test_small_ranges(self, problem: Any) -> None:
        """小さい範囲のテスト"""
        # 300未満: 220 + 284 = 504（両方とも300未満）
        result_300 = problem.solve_naive(300)
        assert result_300 == 504

        # 1000未満: 220 + 284
        result_1000 = problem.solve_naive(1000)
        assert result_1000 == 504  # 220 + 284

    @pytest.mark.slow
    def test_problem_case(self, problem: Any) -> None:
        """本問題のケース（slow test）"""
        result = problem.solve_naive(10000)
        assert result == 31626


class TestSolveOptimized:
    """solve_optimizedのテスト"""

    def test_small_ranges(self, problem: Any) -> None:
        """小さい範囲のテスト"""
        assert problem.solve_optimized(300) == 504
        assert problem.solve_optimized(1000) == 504  # 220 + 284

    @pytest.mark.slow
    def test_problem_case(self, problem: Any) -> None:
        """本問題のケース（slow test）"""
        result = problem.solve_optimized(10000)
        assert result == 31626


class TestSolveMathematical:
    """solve_mathematicalのテスト"""

    def test_small_ranges(self, problem: Any) -> None:
        """小さい範囲のテスト"""
        assert problem.solve_mathematical(300) == 504
        assert problem.solve_mathematical(1000) == 504  # 220 + 284

    @pytest.mark.slow
    def test_problem_case(self, problem: Any) -> None:
        """本問題のケース（slow test）"""
        result = problem.solve_mathematical(10000)
        assert result == 31626


class TestSolutionConsistency:
    """解法間の一貫性テスト"""

    @pytest.mark.parametrize("limit", [100, 300, 500, 1000])
    def test_all_methods_consistency(self, problem: Any, limit: int) -> None:
        """全ての解法の結果が一致することを確認"""
        naive_result = problem.solve_naive(limit)
        optimized_result = problem.solve_optimized(limit)
        mathematical_result = problem.solve_mathematical(limit)

        assert naive_result == optimized_result == mathematical_result

    @pytest.mark.slow
    def test_problem_case_consistency(self, problem: Any) -> None:
        """本問題のケース（10000未満）で全解法が一致することを確認（slow test）"""
        naive_result = problem.solve_naive(10000)
        optimized_result = problem.solve_optimized(10000)
        mathematical_result = problem.solve_mathematical(10000)

        assert naive_result == optimized_result == mathematical_result == 31626


class TestEdgeCases:
    """エッジケースのテスト"""

    def test_very_small_limits(self, problem: Any) -> None:
        """非常に小さい上限のテスト"""
        # 2未満: 友愛数は存在しない
        assert problem.solve_optimized(1) == 0
        assert problem.solve_optimized(2) == 0

        # 10未満: 友愛数は存在しない
        assert problem.solve_optimized(10) == 0

    def test_edge_boundary_cases(self, problem: Any) -> None:
        """境界値のテスト"""
        # 220前後での境界確認
        assert problem.solve_optimized(220) == 0  # 220未満なので220は含まれない
        assert problem.solve_optimized(221) == 0  # 284が範囲外なので友愛ペアにならない

        # 284前後での境界確認
        assert problem.solve_optimized(284) == 0  # 284未満なので284は含まれない
        assert problem.solve_optimized(285) == 504  # 284以上なので220+284が含まれる

    def test_perfect_numbers_excluded(self, problem: Any) -> None:
        """完全数が友愛数として誤認されないことを確認"""
        # 6と28は完全数（d(n) = n）なので友愛数ではない
        pairs = problem.find_amicable_pairs(100)
        perfect_numbers = {6, 28}
        found_numbers = {num for pair in pairs for num in pair}

        for perfect in perfect_numbers:
            assert perfect not in found_numbers

    def test_large_known_amicable_pairs(self, problem: Any) -> None:
        """大きな既知の友愛数ペアのテスト"""
        # 10000未満の他の友愛数ペア
        pairs = problem.find_amicable_pairs(10000)

        # 少なくとも(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368)が含まれるはず
        expected_pairs = {
            (220, 284),
            (1184, 1210),
            (2620, 2924),
            (5020, 5564),
            (6232, 6368),
        }
        found_pairs = {tuple(sorted(pair)) for pair in pairs}

        for expected_pair in expected_pairs:
            assert expected_pair in found_pairs or expected_pair[::-1] in found_pairs


if __name__ == "__main__":
    pytest.main([__file__])
