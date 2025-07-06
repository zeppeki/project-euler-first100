#!/usr/bin/env python3
"""
Problem 065 Runner: Execution and demonstration code for Problem 065.

This module handles the execution and demonstration of Problem 065 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_065 import (
    compute_convergent,
    get_e_continued_fraction_coefficient,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    sum_of_digits,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem065Runner(BaseProblemRunner):
    """Runner for Problem 065: Convergents of e."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "065",
            "Convergents of e",
            272,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 065."""
        # Test e continued fraction coefficients
        assert get_e_continued_fraction_coefficient(0) == 2
        assert get_e_continued_fraction_coefficient(1) == 1
        assert get_e_continued_fraction_coefficient(2) == 2
        assert get_e_continued_fraction_coefficient(3) == 1
        assert get_e_continued_fraction_coefficient(4) == 1
        assert get_e_continued_fraction_coefficient(5) == 4
        assert get_e_continued_fraction_coefficient(6) == 1
        assert get_e_continued_fraction_coefficient(7) == 1
        assert get_e_continued_fraction_coefficient(8) == 6

        # Test convergents (from problem description)
        convergents = [
            (2, 1),  # 0th: 2
            (3, 1),  # 1st: 3
            (8, 3),  # 2nd: 8/3
            (11, 4),  # 3rd: 11/4
            (19, 7),  # 4th: 19/7
            (87, 32),  # 5th: 87/32
            (106, 39),  # 6th: 106/39
            (193, 71),  # 7th: 193/71
            (1264, 465),  # 8th: 1264/465
            (1457, 536),  # 9th: 1457/536
        ]

        for i, (expected_num, expected_den) in enumerate(convergents):
            num, den = compute_convergent(i)
            assert num == expected_num, (
                f"Convergent {i}: expected numerator {expected_num}, got {num}"
            )
            assert den == expected_den, (
                f"Convergent {i}: expected denominator {expected_den}, got {den}"
            )

        # Test sum of digits for 10th convergent (1457)
        assert sum_of_digits(1457) == 17

        print("e連分数係数と収束分数の検証テストが完了しました")
        return []

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 065."""
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
    runner = Problem065Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem065Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
