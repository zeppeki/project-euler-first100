"""Tests for Problem 085: Counting rectangles."""

import importlib.util
import sys
from pathlib import Path

import pytest

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Dynamically import the module
spec = importlib.util.spec_from_file_location(
    "problem_085", Path(__file__).parent.parent.parent / "problems" / "problem_085.py"
)
if spec and spec.loader:
    problem_085 = importlib.util.module_from_spec(spec)
    sys.modules["problem_085"] = problem_085
    spec.loader.exec_module(problem_085)
else:
    raise ImportError("Could not load problem_085 module")


class TestCountRectangles:
    """長方形カウント関数のテスト."""

    @pytest.mark.parametrize(
        "m,n,expected",
        [
            (1, 1, 1),  # 1×1グリッドには1つの長方形
            (2, 1, 3),  # 2×1グリッドには3つの長方形
            (3, 2, 18),  # 問題文の例
            (2, 3, 18),  # 対称性の確認
            (4, 3, 60),  # 4×3グリッド
            (5, 5, 225),  # 正方形グリッド
        ],
    )
    def test_count_rectangles(self, m: int, n: int, expected: int) -> None:
        """様々なグリッドサイズでの長方形数を検証."""
        assert problem_085.count_rectangles(m, n) == expected

    def test_count_rectangles_formula(self) -> None:
        """数式の正しさを検証."""
        # 手動計算との比較
        m, n = 3, 2
        # 長方形数 = C(m+1, 2) * C(n+1, 2) = C(4, 2) * C(3, 2) = 6 * 3 = 18
        assert problem_085.count_rectangles(m, n) == 18

        # 大きいサイズでの検証
        m, n = 10, 8
        expected = m * (m + 1) * n * (n + 1) // 4
        assert problem_085.count_rectangles(m, n) == expected


class TestSolutions:
    """解法関数のテスト."""

    def test_solutions_consistency(self) -> None:
        """異なる解法の整合性を検証."""
        result_naive = problem_085.solve_naive()
        result_optimized = problem_085.solve_optimized()

        # 両方の解法が同じ結果を返すことを確認
        assert result_naive == result_optimized

    def test_solutions_small_target(self) -> None:
        """小さい目標値での動作確認."""
        # target=18の場合、3×2または2×3のグリッドが最適
        result = problem_085.solve_naive(18)
        assert result == 6  # 3×2 = 6

        # target=100の場合
        result = problem_085.solve_naive(100)
        # 最適解の確認
        best_area = 0
        min_diff = float("inf")
        for m in range(1, 20):
            for n in range(1, m + 1):
                count = problem_085.count_rectangles(m, n)
                diff = abs(count - 100)
                if diff < min_diff:
                    min_diff = diff
                    best_area = m * n
        assert result == best_area

    def test_optimized_efficiency(self) -> None:
        """最適化解法の効率性を確認."""
        # 小さい目標値で素直な解法と比較
        targets = [1000, 5000, 10000]
        for target in targets:
            result_naive = problem_085.solve_naive(target)
            result_optimized = problem_085.solve_optimized(target)
            assert result_naive == result_optimized

    def test_edge_cases(self) -> None:
        """エッジケースのテスト."""
        # 非常に小さい目標値
        result = problem_085.solve_naive(1)
        assert result == 1  # 1×1グリッドが最適

        # 目標値3の場合
        result = problem_085.solve_naive(3)
        assert result == 2  # 2×1グリッドが最適（3個の長方形）

    @pytest.mark.slow
    def test_project_euler_answer(self) -> None:
        """Project Eulerの答えを確認（遅いテスト）."""
        # デフォルト値（2,000,000）での結果を確認
        result = problem_085.solve_optimized()
        assert isinstance(result, int)
        assert result > 0

        # 具体的な答えの検証（結果の妥当性チェック）
        # 答えが約2000～3000の範囲にあることを確認
        assert 2000 <= result <= 3000
