#!/usr/bin/env python3
"""
Problem 064 Runner: Execution and demonstration code for Problem 064.

This module handles the execution and demonstration of Problem 064 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_064 import (
    get_continued_fraction_period,
    is_perfect_square,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem064Runner(BaseProblemRunner):
    """Runner for Problem 064: Odd period square roots."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "064",
            "Odd period square roots",
            1322,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 064."""
        # Test perfect square detection
        assert is_perfect_square(1)
        assert is_perfect_square(4)
        assert is_perfect_square(9)
        assert not is_perfect_square(2)
        assert not is_perfect_square(3)

        # Test continued fraction periods for known examples
        # √2 has period 1: [1;(2)]
        assert get_continued_fraction_period(2) == 1

        # √3 has period 2: [1;(1,2)]
        assert get_continued_fraction_period(3) == 2

        # √5 has period 1: [2;(4)]
        assert get_continued_fraction_period(5) == 1

        # √23 has period 4: [4;(1,3,1,8)]
        assert get_continued_fraction_period(23) == 4

        print("連分数周期計算と完全平方数判定の検証テストが完了しました")
        return []

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 064."""
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
    runner = Problem064Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem064Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
