#!/usr/bin/env python3
"""
Problem 066 Runner: Execution and demonstration code for Problem 066.

This module handles the execution and demonstration of Problem 066 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_066 import (
    find_pell_solution,
    is_perfect_square,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem066Runner(BaseProblemRunner):
    """Runner for Problem 066: Diophantine equation."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "066",
            "Diophantine equation",
            661,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 066."""
        # Test perfect square detection
        assert is_perfect_square(1)
        assert is_perfect_square(4)
        assert is_perfect_square(9)
        assert not is_perfect_square(2)
        assert not is_perfect_square(3)
        assert not is_perfect_square(5)

        # Test known Pell equation solutions from problem description
        test_cases = [
            (2, (3, 2)),  # x=3, y=2 for D=2
            (3, (2, 1)),  # x=2, y=1 for D=3
            (5, (9, 4)),  # x=9, y=4 for D=5
            (6, (5, 2)),  # x=5, y=2 for D=6
            (7, (8, 3)),  # x=8, y=3 for D=7
            (13, (649, 180)),  # x=649, y=180 for D=13
        ]

        for d, (expected_x, expected_y) in test_cases:
            x, y = find_pell_solution(d)
            assert x == expected_x, f"D={d}: expected x={expected_x}, got x={x}"
            assert y == expected_y, f"D={d}: expected y={expected_y}, got y={y}"
            # Verify the Pell equation
            assert x * x - d * y * y == 1, f"D={d}: Pell equation not satisfied"

        print("Pell方程式の解法と完全平方数検出の検証テストが完了しました")
        return []

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 066."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return ()


def main() -> None:
    """メイン関数"""
    runner = Problem066Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem066Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
