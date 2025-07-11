"""Tests for Problem 088: Product-sum numbers."""

import importlib.util
import sys
from pathlib import Path

import pytest

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import the module
spec = importlib.util.spec_from_file_location(
    "problem_088", Path(__file__).parent.parent.parent / "problems" / "problem_088.py"
)
if spec and spec.loader:
    problem_088 = importlib.util.module_from_spec(spec)
    sys.modules["problem_088"] = problem_088
    spec.loader.exec_module(problem_088)
else:
    raise ImportError("Could not load problem_088 module")


class TestProductSumNumbers:
    """積和数のテスト."""

    def test_specific_examples(self) -> None:
        """問題文で示された具体例を検証."""
        # k=2: 4 = 2 × 2 = 2 + 2
        assert 2 * 2 == 4
        assert 2 + 2 == 4

        # k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
        assert 1 * 2 * 3 == 6
        assert 1 + 2 + 3 == 6

        # k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
        assert 1 * 1 * 2 * 4 == 8
        assert 1 + 1 + 2 + 4 == 8

        # k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
        assert 1 * 1 * 2 * 2 * 2 == 8
        assert 1 + 1 + 2 + 2 + 2 == 8

        # k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
        assert 1 * 1 * 1 * 1 * 2 * 6 == 12
        assert 1 + 1 + 1 + 1 + 2 + 6 == 12

    def test_minimal_product_sum_numbers(self) -> None:
        """最小積和数の検証."""
        k_values = problem_088.find_minimal_product_sum_numbers(6)

        # 問題文の例と一致することを確認
        assert k_values[2] == 4
        assert k_values[3] == 6
        assert k_values[4] == 8
        assert k_values[5] == 8
        assert k_values[6] == 12

    def test_k_value_calculation(self) -> None:
        """k値の計算を検証."""
        # k = 因数の個数 + (積 - 和) 個の1
        # 例: 8 = 1 × 1 × 2 × 4
        # 因数: [2, 4] (1は後で追加)
        # 積: 8, 和: 2 + 4 = 6
        # k = 2 + (8 - 6) = 4

        factors = [2, 4]
        prod = 8
        sum_val = 6
        k = len(factors) + (prod - sum_val)
        assert k == 4


class TestSolutionFunctions:
    """解法関数のテスト."""

    def test_problem_examples(self) -> None:
        """問題文の例を検証."""
        # k=2 to 6: sum = 30
        expected1 = 30
        assert problem_088.solve_naive(6) == expected1
        assert problem_088.solve_optimized(6) == expected1
        assert problem_088.solve_mathematical(6) == expected1

        # k=2 to 12: sum = 61
        expected2 = 61
        assert problem_088.solve_naive(12) == expected2
        assert problem_088.solve_optimized(12) == expected2
        assert problem_088.solve_mathematical(12) == expected2

    def test_small_values(self) -> None:
        """小さい値での結果を検証."""
        # k=2のみ: 最小積和数は4
        assert problem_088.solve_naive(2) == 4
        assert problem_088.solve_optimized(2) == 4
        assert problem_088.solve_mathematical(2) == 4

        # k=2,3: 最小積和数は4,6 → 和は10
        assert problem_088.solve_naive(3) == 10
        assert problem_088.solve_optimized(3) == 10
        assert problem_088.solve_mathematical(3) == 10

    def test_consistency(self) -> None:
        """異なる解法の一致性を検証."""
        test_values = [10, 20, 30, 50]

        for max_k in test_values:
            result_naive = problem_088.solve_naive(max_k)
            result_optimized = problem_088.solve_optimized(max_k)
            result_mathematical = problem_088.solve_mathematical(max_k)

            assert result_naive == result_optimized, (
                f"Mismatch at k={max_k}: "
                f"naive={result_naive}, optimized={result_optimized}"
            )
            assert result_optimized == result_mathematical, (
                f"Mismatch at k={max_k}: "
                f"optimized={result_optimized}, mathematical={result_mathematical}"
            )

    def test_uniqueness(self) -> None:
        """重複除去の検証."""
        # k=4,5の両方で最小積和数は8
        # 和に8が2回含まれないことを確認
        k_values = problem_088.find_minimal_product_sum_numbers(5)
        assert k_values[4] == 8
        assert k_values[5] == 8

        # k=2 to 5の和: 4 + 6 + 8 = 18 (8は1回のみ)
        result = problem_088.solve_naive(5)
        assert result == 18


class TestMathematicalProperties:
    """数学的性質のテスト."""

    def test_minimum_bound(self) -> None:
        """最小値の境界を検証."""
        # k=2の最小積和数は4
        # 2 × 2 = 2 + 2 = 4
        k_values = problem_088.find_minimal_product_sum_numbers(2)
        assert k_values[2] == 4

        # kが大きくなると最小積和数も大きくなる傾向
        k_values = problem_088.find_minimal_product_sum_numbers(10)
        for k in range(3, 10):
            assert k_values[k] >= k  # 最小でもk以上

    def test_upper_bound(self) -> None:
        """上限の検証."""
        # 最小積和数は2k以下
        # なぜなら: k + k = 2k, 2 × k = 2k
        k_values = problem_088.find_minimal_product_sum_numbers(20)

        for k in range(2, 21):
            assert k_values[k] <= 2 * k

    def test_factorization_property(self) -> None:
        """因数分解の性質を検証."""
        # 積和数は必ず合成数（素数ではない）
        k_values = problem_088.find_minimal_product_sum_numbers(10)

        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

        for k in range(2, 11):
            assert not is_prime(k_values[k])


class TestPerformance:
    """パフォーマンステスト."""

    def test_performance_difference(self) -> None:
        """最適化の効果を確認."""
        import time

        max_k = 50

        # 素直な解法
        start = time.time()
        result_naive = problem_088.solve_naive(max_k)
        time_naive = time.time() - start

        # 最適化解法
        start = time.time()
        result_optimized = problem_088.solve_optimized(max_k)
        time_optimized = time.time() - start

        # 結果は一致すべき
        assert result_naive == result_optimized

        # パフォーマンス情報を出力
        print(f"\nPerformance (k≤{max_k}):")
        print(f"  Naive: {time_naive:.4f}s")
        print(f"  Optimized: {time_optimized:.4f}s")

    @pytest.mark.slow
    def test_large_input(self) -> None:
        """大きな入力での動作を検証."""
        max_k = 1000

        # 最適化解法のみテスト
        result_optimized = problem_088.solve_optimized(max_k)
        result_mathematical = problem_088.solve_mathematical(max_k)

        assert result_optimized == result_mathematical
        assert result_optimized > 0

    @pytest.mark.slow
    def test_project_euler_answer(self) -> None:
        """Project Eulerの答えを確認（遅いテスト）."""
        max_k = 12000
        result = problem_088.solve_optimized(max_k)

        # 結果が妥当な範囲にあることを確認
        assert result > 0
        assert result < 10000000  # 妥当な上限

        # 具体的な値は伏せる
        print(f"\nResult for k≤{max_k}: {result}")


class TestEdgeCases:
    """エッジケースのテスト."""

    def test_minimum_k(self) -> None:
        """最小のkでのテスト."""
        # k=2は最小値
        result = problem_088.solve_naive(2)
        assert result == 4

    def test_duplicate_handling(self) -> None:
        """重複処理の確認."""
        # 複数のkで同じ最小積和数を持つ場合
        k_values = problem_088.find_minimal_product_sum_numbers(10)

        # 重複をカウント
        value_counts = {}
        for _k, n in k_values.items():
            if n not in value_counts:
                value_counts[n] = 0
            value_counts[n] += 1

        # 重複が存在することを確認
        has_duplicates = any(count > 1 for count in value_counts.values())
        assert has_duplicates
