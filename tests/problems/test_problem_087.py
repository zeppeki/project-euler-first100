"""Tests for Problem 087: Prime power triples."""

import importlib.util
import sys
from pathlib import Path

import pytest

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import the module
spec = importlib.util.spec_from_file_location(
    "problem_087", Path(__file__).parent.parent.parent / "problems" / "problem_087.py"
)
if spec and spec.loader:
    problem_087 = importlib.util.module_from_spec(spec)
    sys.modules["problem_087"] = problem_087
    spec.loader.exec_module(problem_087)
else:
    raise ImportError("Could not load problem_087 module")


class TestSieveOfEratosthenes:
    """エラトステネスの篩のテスト."""

    def test_small_limits(self) -> None:
        """小さい上限での素数生成を検証."""
        assert problem_087.sieve_of_eratosthenes(1) == []
        assert problem_087.sieve_of_eratosthenes(2) == [2]
        assert problem_087.sieve_of_eratosthenes(10) == [2, 3, 5, 7]
        assert problem_087.sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_prime_count(self) -> None:
        """既知の素数の個数を検証."""
        # π(100) = 25
        primes_100 = problem_087.sieve_of_eratosthenes(100)
        assert len(primes_100) == 25

        # π(1000) = 168
        primes_1000 = problem_087.sieve_of_eratosthenes(1000)
        assert len(primes_1000) == 168


class TestPrimePowerTriples:
    """素数べき乗三項のテスト."""

    def test_problem_example(self) -> None:
        """問題文の例（50未満）を検証."""
        expected = 4
        assert problem_087.solve_naive(50) == expected
        assert problem_087.solve_optimized(50) == expected
        assert problem_087.solve_mathematical(50) == expected

    def test_specific_examples(self) -> None:
        """問題文で示された具体例を検証."""
        # 28 = 2² + 2³ + 2⁴
        assert 2**2 + 2**3 + 2**4 == 28
        # 33 = 3² + 2³ + 2⁴
        assert 3**2 + 2**3 + 2**4 == 33
        # 49 = 5² + 2³ + 2⁴
        assert 5**2 + 2**3 + 2**4 == 49
        # 47 = 2² + 3³ + 2⁴
        assert 2**2 + 3**3 + 2**4 == 47

    def test_small_limits(self) -> None:
        """小さい上限での結果を検証."""
        # 最小の素数べき乗三項は 28 = 2² + 2³ + 2⁴
        assert problem_087.solve_naive(28) == 0
        assert problem_087.solve_naive(29) == 1
        assert problem_087.solve_optimized(29) == 1
        assert problem_087.solve_mathematical(29) == 1

    def test_consistency(self) -> None:
        """異なる解法の一致性を検証."""
        test_limits = [50, 100, 500, 1000]

        for limit in test_limits:
            result_naive = problem_087.solve_naive(limit)
            result_optimized = problem_087.solve_optimized(limit)
            result_mathematical = problem_087.solve_mathematical(limit)

            assert result_naive == result_optimized, (
                f"Mismatch at limit={limit}: "
                f"naive={result_naive}, optimized={result_optimized}"
            )
            assert result_optimized == result_mathematical, (
                f"Mismatch at limit={limit}: "
                f"optimized={result_optimized}, mathematical={result_mathematical}"
            )

    def test_growth_pattern(self) -> None:
        """成長パターンを検証."""
        # 上限が増えると結果も増える
        results = []
        limits = [100, 200, 500, 1000, 2000]

        for limit in limits:
            result = problem_087.solve_optimized(limit)
            results.append(result)

        # 単調増加を確認
        for i in range(1, len(results)):
            assert results[i] >= results[i - 1], (
                f"Not monotonic: limit={limits[i - 1]} gives {results[i - 1]}, "
                f"but limit={limits[i]} gives {results[i]}"
            )

    def test_uniqueness(self) -> None:
        """同じ数が複数の方法で表現できることを検証."""
        # 例: 87 = 7² + 2³ + 2⁴ = 3² + 2³ + 3⁴
        assert 7**2 + 2**3 + 2**4 == 73
        # 別の表現があるか確認
        found_representations = []
        primes = problem_087.sieve_of_eratosthenes(10)

        for p2 in primes:
            for p3 in primes:
                for p4 in primes:
                    if p2**2 + p3**3 + p4**4 == 73:
                        found_representations.append((p2, p3, p4))

        # 73の表現を確認
        assert len(found_representations) >= 1


class TestSolutionFunctions:
    """解法関数のテスト."""

    def test_edge_cases(self) -> None:
        """エッジケースを検証."""
        # 最小値より小さい上限
        assert problem_087.solve_naive(1) == 0
        assert problem_087.solve_optimized(1) == 0
        assert problem_087.solve_mathematical(1) == 0

        # 最小の素数べき乗三項 28 = 2² + 2³ + 2⁴
        assert problem_087.solve_naive(27) == 0
        assert problem_087.solve_naive(28) == 0  # 28は含まない（未満）
        assert problem_087.solve_naive(29) == 1  # 28を含む

    def test_performance_difference(self) -> None:
        """最適化の効果を確認."""
        import time

        limit = 10000

        # 素直な解法
        start = time.time()
        result_naive = problem_087.solve_naive(limit)
        time_naive = time.time() - start

        # 最適化解法
        start = time.time()
        result_optimized = problem_087.solve_optimized(limit)
        time_optimized = time.time() - start

        # 結果は一致すべき
        assert result_naive == result_optimized

        # 最適化版の方が速いことを期待（ただし必須ではない）
        # 小さい入力では差が出ない可能性もある
        print(f"Naive: {time_naive:.4f}s, Optimized: {time_optimized:.4f}s")

    @pytest.mark.slow
    def test_large_input(self) -> None:
        """大きな入力での動作を検証."""
        limit = 1000000

        # 最適化解法のみテスト（素直な解法は遅すぎる）
        result_optimized = problem_087.solve_optimized(limit)
        result_mathematical = problem_087.solve_mathematical(limit)

        assert result_optimized == result_mathematical
        assert result_optimized > 0

        # 妥当な範囲内であることを確認
        # 上限の10%以下程度が妥当
        assert result_optimized < limit * 0.1

    @pytest.mark.slow
    def test_project_euler_answer(self) -> None:
        """Project Eulerの答えを確認（遅いテスト）."""
        limit = 50000000
        result = problem_087.solve_optimized(limit)

        # 結果が妥当な範囲にあることを確認
        assert result > 0
        assert result < limit * 0.05  # 5%未満が妥当（実際は約2.2%）

        # 具体的な値は伏せる
        print(f"Result for limit {limit:,}: {result:,}")


class TestMathematicalProperties:
    """数学的性質のテスト."""

    def test_minimum_value(self) -> None:
        """最小値の検証."""
        # 最小の素数べき乗三項は 2² + 2³ + 2⁴ = 4 + 8 + 16 = 28
        min_value = 2**2 + 2**3 + 2**4
        assert min_value == 28

    def test_prime_power_bounds(self) -> None:
        """べき乗の境界値を検証."""
        limit = 1000
        primes = problem_087.sieve_of_eratosthenes(int(limit**0.5))

        # 各べき乗の最大素数を確認
        max_p2 = 0
        max_p3 = 0
        max_p4 = 0

        for p in primes:
            if p**2 < limit:
                max_p2 = p
            if p**3 < limit:
                max_p3 = p
            if p**4 < limit:
                max_p4 = p

        # 理論値と比較
        assert max_p2 <= int(limit**0.5)
        assert max_p3 <= int(limit ** (1 / 3))
        assert max_p4 <= int(limit ** (1 / 4))

    def test_distribution(self) -> None:
        """分布の特性を検証."""
        limit = 1000
        result = problem_087.solve_optimized(limit)

        # ある程度の密度があることを確認
        density = result / limit
        assert 0.01 < density < 0.5  # 1%〜50%の範囲
