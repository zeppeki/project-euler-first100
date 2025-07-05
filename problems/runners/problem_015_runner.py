#!/usr/bin/env python3
"""
Problem 015 Runner: Execution and demonstration code for Problem 015.

This module handles the execution and demonstration of Problem 015 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_015 import (
    solve_mathematical,
    solve_mathematical_factorial,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem015Runner(BaseProblemRunner):
    """Runner for Problem 015: Lattice paths."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "015",
            "Lattice paths",
            problem_answer=137846528820,  # Known answer for 20x20 grid
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 015."""
        return [
            (0, 1),  # 0×0グリッド: 1通り（移動なし）
            (1, 2),  # 1×1グリッド: 2通り（右→下 or 下→右）
            (2, 6),  # 2×2グリッド: 6通り（問題例）
            (3, 20),  # 3×3グリッド: 20通り
            (4, 70),  # 4×4グリッド: 70通り
            (5, 252),  # 5×5グリッド: 252通り
            (10, 184756),  # 10×10グリッド: 184756通り
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 015."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
            ("階乗解法", solve_mathematical_factorial),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (20,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 015."""
        return [self._demonstrate_lattice_analysis]

    def _demonstrate_lattice_analysis(self) -> None:
        """格子経路の数学的分析を表示"""
        n = 20
        result = solve_mathematical(n)

        print(f"{n}×{n}グリッドの総経路数: {result:,}")
        print(f"組み合わせ公式: C({2 * n}, {n}) = {2 * n}! / ({n}! * {n}!)")

        print("\n小さなグリッドの経路数:")
        for i in range(1, 11):
            paths = solve_mathematical(i)
            print(f"{i}×{i}: {paths:,}")

        print("\n数学的背景:")
        print(f"- 右に{n}回、下に{n}回の移動が必要")
        print(f"- 総移動回数: {2 * n}回")
        print(f"- その中から右移動{n}回を選ぶ組み合わせ")
        print(f"- C({2 * n}, {n}) = C(40, 20) = {result:,}")


def main() -> None:
    """Main entry point."""
    runner = Problem015Runner(enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 015."""
    print("=== Problem 015 Performance Benchmark ===")
    runner = Problem015Runner(enable_performance_test=True, enable_demonstrations=False)
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
