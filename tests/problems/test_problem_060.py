#!/usr/bin/env python3
"""
Test for Problem 060: Prime pair sets
"""

import pytest

from problems.problem_060 import (
    are_prime_pair,
    can_form_complete_set,
    concatenate_numbers,
    demonstrate_example_set,
    find_prime_pair_sets_by_size,
    find_prime_pairs,
    get_prime_pair_details,
    is_prime,
    sieve_of_eratosthenes,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem060:
    """Problem 060のテストクラス"""

    def test_sieve_of_eratosthenes(self) -> None:
        """エラトステネスの篩のテスト"""
        # 小さな範囲でのテスト
        result = sieve_of_eratosthenes(10, "bool_array")
        expected = [
            False,
            False,
            True,
            True,
            False,
            True,
            False,
            True,
            False,
            False,
            False,
        ]
        assert result == expected

        # 素数の個数確認
        primes_up_to_100 = [
            i for i in range(2, 101) if sieve_of_eratosthenes(100, "bool_array")[i]
        ]
        assert len(primes_up_to_100) == 25  # 100以下の素数は25個

    def test_is_prime(self) -> None:
        """素数判定のテスト"""
        # 既知の素数
        assert is_prime(2)
        assert is_prime(3)
        assert is_prime(5)
        assert is_prime(7)
        assert is_prime(11)
        assert is_prime(13)
        assert is_prime(17)
        assert is_prime(19)
        assert is_prime(23)

        # 合成数
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

        # より大きな数
        assert is_prime(97)
        assert is_prime(101)
        assert not is_prime(100)
        assert not is_prime(102)

    def test_concatenate_numbers(self) -> None:
        """数値連結のテスト"""
        assert concatenate_numbers(3, 7) == 37
        assert concatenate_numbers(7, 3) == 73
        assert concatenate_numbers(109, 673) == 109673
        assert concatenate_numbers(673, 109) == 673109
        assert concatenate_numbers(1, 23) == 123
        assert concatenate_numbers(23, 1) == 231

    def test_are_prime_pair(self) -> None:
        """素数ペア判定のテスト"""
        # 問題で与えられた例
        assert are_prime_pair(3, 7)  # 37と73は両方素数
        assert are_prime_pair(7, 109)  # 7109と1097は両方素数
        assert are_prime_pair(109, 673)  # 109673と673109は両方素数

        # 素数ペアでない例
        assert not are_prime_pair(2, 3)  # 23は素数だが32は合成数
        assert not are_prime_pair(5, 11)  # 511は合成数

    def test_find_prime_pairs(self) -> None:
        """素数ペア検索のテスト"""
        small_primes = [3, 7, 11, 13, 17, 19, 23]

        # 3とペアを形成する素数
        pairs_with_3 = find_prime_pairs(small_primes, 3)
        assert 7 in pairs_with_3  # 3と7は素数ペア

        # 結果の検証
        for prime in pairs_with_3:
            assert are_prime_pair(3, prime)

    def test_can_form_complete_set(self) -> None:
        """完全集合形成判定のテスト"""
        # 問題で与えられた例（サイズ4）
        example_set = [3, 7, 109, 673]
        assert can_form_complete_set(example_set, 4)

        # 小さな有効な集合
        small_valid_set = [3, 7]
        assert can_form_complete_set(small_valid_set, 2)

        # 無効な集合
        invalid_set = [2, 3, 5]
        assert not can_form_complete_set(invalid_set, 3)

        # サイズが一致しない場合
        assert not can_form_complete_set([3, 7], 3)

    def test_solve_naive_small_cases(self) -> None:
        """素直な解法の小さなケースでのテスト"""
        # サイズ2の最小集合を探す（小さな範囲で）
        result = solve_naive(set_size=2, prime_limit=100)
        assert result > 0  # 解が見つかることを確認

        # サイズ3の集合（小さな範囲で）
        result = solve_naive(set_size=3, prime_limit=100)
        assert result > 0  # 解が見つかることを確認

    def test_solve_optimized_small_cases(self) -> None:
        """最適化解法の小さなケースでのテスト"""
        # サイズ2の最小集合を探す
        result = solve_optimized(set_size=2, prime_limit=100)
        assert result > 0

        # サイズ3の集合
        result = solve_optimized(set_size=3, prime_limit=100)
        assert result > 0

    def test_solve_mathematical_small_cases(self) -> None:
        """数学的解法の小さなケースでのテスト"""
        # サイズ2の最小集合を探す
        result = solve_mathematical(set_size=2, prime_limit=100)
        assert result > 0

        # サイズ3の集合
        result = solve_mathematical(set_size=3, prime_limit=100)
        assert result > 0

    def test_solutions_consistency_small_cases(self) -> None:
        """小さなケースでの解法の一致性テスト"""
        # サイズ2での一致性確認
        naive_result = solve_naive(set_size=2, prime_limit=50)
        optimized_result = solve_optimized(set_size=2, prime_limit=50)
        mathematical_result = solve_mathematical(set_size=2, prime_limit=50)

        assert naive_result == optimized_result == mathematical_result

        # サイズ3での一致性確認（範囲を限定）
        naive_result = solve_naive(set_size=3, prime_limit=50)
        optimized_result = solve_optimized(set_size=3, prime_limit=50)
        mathematical_result = solve_mathematical(set_size=3, prime_limit=50)

        assert naive_result == optimized_result == mathematical_result

    @pytest.mark.slow
    def test_solve_naive_main_problem(self) -> None:
        """素直な解法のメイン問題テスト（サイズ5）"""
        result = solve_naive(set_size=5, prime_limit=10000)
        assert isinstance(result, int)
        assert result > 0

    @pytest.mark.slow
    def test_solve_optimized_main_problem(self) -> None:
        """最適化解法のメイン問題テスト（サイズ5）"""
        result = solve_optimized(set_size=5, prime_limit=10000)
        assert isinstance(result, int)
        assert result > 0

    @pytest.mark.slow
    def test_solve_mathematical_main_problem(self) -> None:
        """数学的解法のメイン問題テスト（サイズ5）"""
        result = solve_mathematical(set_size=5, prime_limit=10000)
        assert isinstance(result, int)
        assert result > 0

    @pytest.mark.slow
    def test_all_solutions_agree_main_problem(self) -> None:
        """すべての解法が同じ結果を返すことを確認（メイン問題）"""
        naive_result = solve_naive(set_size=5, prime_limit=8000)
        optimized_result = solve_optimized(set_size=5, prime_limit=8000)
        mathematical_result = solve_mathematical(set_size=5, prime_limit=8000)

        assert naive_result == optimized_result == mathematical_result
        assert naive_result > 0

    @pytest.mark.slow
    def test_find_prime_pair_sets_by_size(self) -> None:
        """サイズ別素数集合探索のテスト"""
        results = find_prime_pair_sets_by_size(max_size=3, prime_limit=100)

        # サイズ2の結果を確認
        assert 2 in results
        assert "set" in results[2]
        assert "sum" in results[2]
        assert "verified" in results[2]
        assert results[2]["verified"] is True

        # サイズ3の結果を確認
        assert 3 in results
        assert results[3]["verified"] is True

    def test_get_prime_pair_details(self) -> None:
        """素数集合詳細取得のテスト"""
        # 問題で与えられた例
        example_set = [3, 7, 109, 673]
        details = get_prime_pair_details(example_set)

        assert details["prime_set"] == example_set
        assert details["sum"] == 792
        assert details["size"] == 4
        assert details["is_valid_complete_set"] is True
        assert details["total_pairs"] == 6  # C(4,2) = 6
        assert details["valid_pairs"] == 6

        # 空の集合
        empty_details = get_prime_pair_details([])
        assert "error" in empty_details

    def test_demonstrate_example_set(self) -> None:
        """例示集合デモンストレーションのテスト"""
        demo = demonstrate_example_set()

        assert demo["prime_set"] == [3, 7, 109, 673]
        assert demo["sum"] == 792
        assert demo["is_valid_complete_set"] is True
        assert demo["valid_pairs"] == demo["total_pairs"]

    def test_edge_cases(self) -> None:
        """エッジケースのテスト"""
        # 解が見つからない場合（制限が小さすぎる）
        result = solve_naive(set_size=5, prime_limit=50)
        assert result == -1

        # サイズ1の場合
        result = solve_naive(set_size=1, prime_limit=100)
        assert result > 0  # 最小の素数2が返される

    def test_prime_pair_properties(self) -> None:
        """素数ペアの性質テスト"""
        # 対称性
        assert are_prime_pair(3, 7) == are_prime_pair(7, 3)
        assert are_prime_pair(7, 109) == are_prime_pair(109, 7)

        # 反射性（自分自身とのペア）は通常Falseになる
        # 例：33は合成数、77も合成数
        assert not are_prime_pair(3, 3)
        assert not are_prime_pair(7, 7)

    def test_concatenation_edge_cases(self) -> None:
        """連結のエッジケーステスト"""
        # 1桁同士
        assert concatenate_numbers(1, 2) == 12
        assert concatenate_numbers(9, 8) == 98

        # 異なる桁数
        assert concatenate_numbers(1, 234) == 1234
        assert concatenate_numbers(234, 1) == 2341

        # 大きな数
        assert concatenate_numbers(999, 111) == 999111

    @pytest.mark.slow
    def test_performance_characteristics(self) -> None:
        """パフォーマンス特性のテスト"""
        # 小さな範囲での実行時間を測定（相対的な比較）
        import time

        start_time = time.time()
        solve_naive(set_size=3, prime_limit=100)
        naive_time = time.time() - start_time

        start_time = time.time()
        solve_optimized(set_size=3, prime_limit=100)
        optimized_time = time.time() - start_time

        start_time = time.time()
        solve_mathematical(set_size=3, prime_limit=100)
        mathematical_time = time.time() - start_time

        # 実行時間が合理的な範囲内であることを確認
        assert naive_time < 10.0  # 10秒以内
        assert optimized_time < 10.0
        assert mathematical_time < 10.0
