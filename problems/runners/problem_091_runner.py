#!/usr/bin/env python3
"""Runner for Problem 091: Right triangles with integer coordinates"""

from collections.abc import Callable
from typing import Any

from problems.problem_091 import (
    is_right_triangle,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem091Runner(BaseProblemRunner):
    """Runner for Problem 091: Right triangles with integer coordinates"""

    def __init__(self) -> None:
        super().__init__(
            problem_number="091",
            problem_title="Right triangles with integer coordinates",
            problem_answer=None,  # Expected answer not provided to avoid spoilers
            enable_performance_test=True,
            enable_demonstrations=True,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 091"""
        return [
            (0, 0),  # 0x0 grid - no triangles possible
            (1, 3),  # 1x1 grid - 3 triangles
            (2, 14),  # 2x2 grid - problem statement example
            (3, 33),  # 3x3 grid - known value
            (5, 101),  # 5x5 grid - known value
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 091"""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for main problem execution"""
        return (50,)  # Main problem uses 50x50 grid

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for additional analysis"""
        return [
            self._demonstrate_growth_pattern,
            self._demonstrate_example_triangles,
            self._demonstrate_mathematical_insights,
        ]

    def _demonstrate_growth_pattern(self) -> None:
        """Demonstrate how triangle count grows with grid size"""
        print("Growth pattern of triangle count:")
        print("-" * 40)
        limits = [1, 2, 3, 5, 10, 15, 20]
        for limit in limits:
            count = solve_naive(limit) if limit <= 10 else solve_optimized(limit)
            ratio = count / (limit**4) if limit > 0 else 0
            print(
                f"{limit:3}x{limit:3} grid: {count:6} triangles (ratio to n⁴: {ratio:.4f})"
            )

    def _demonstrate_example_triangles(self) -> None:
        """Demonstrate example right triangles in 2x2 grid"""
        print("Example right triangles in 2x2 grid:")
        print("-" * 40)
        examples = [
            ((1, 0), (0, 1), "Right angle at origin"),
            ((1, 0), (1, 1), "Right angle at P"),
            ((0, 1), (1, 1), "Right angle at Q"),
            ((2, 0), (0, 1), "Right angle at origin"),
            ((2, 0), (2, 1), "Right angle at P"),
        ]

        for p, q, description in examples:
            x1, y1 = p
            x2, y2 = q
            if is_right_triangle(x1, y1, x2, y2):
                print(f"✓ O(0,0), P{p}, Q{q} - {description}")

    def _demonstrate_mathematical_insights(self) -> None:
        """Demonstrate mathematical insights about the problem"""
        print("Mathematical insights:")
        print("-" * 40)
        print("• Three types of right triangles based on vertex location:")
        print("  - Right angle at origin O")
        print("  - Right angle at point P")
        print("  - Right angle at point Q")
        print("• Uses Pythagorean theorem: a² + b² = c² for validation")
        print("• Growth is approximately O(n⁴) for an n×n grid")
        print("• Optimization avoids counting each triangle twice")


def main() -> None:
    """Main entry point for Problem 091 runner"""
    runner = Problem091Runner()
    runner.main()


if __name__ == "__main__":
    main()
