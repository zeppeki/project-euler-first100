#!/usr/bin/env python3
"""
Problem 017 Runner: Execution and demonstration code for Problem 017.

This module handles the execution and demonstration of Problem 017 solutions,
separated from the core algorithm implementations.
"""

from collections.abc import Callable
from typing import Any

from problems.problem_017 import (
    count_letters,
    number_to_words,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem017Runner(BaseProblemRunner):
    """Runner for Problem 017: Number Letter Counts."""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "017",
            "Number Letter Counts",
            problem_answer=21124,  # Known answer for 1-1000
            enable_performance_test=enable_performance_test,
            enable_demonstrations=enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 017."""
        return [
            (1, 3),  # "one" = 3 letters
            (2, 6),  # "one" + "two" = 3 + 3 = 6 letters
            (
                5,
                19,
            ),  # "one" + "two" + "three" + "four" + "five" = 3+3+5+4+4 = 19 letters
            (12, 51),  # Sum of letters from 1 to 12
            (21, 121),  # Sum of letters from 1 to 21
            (42, 319),  # Sum of letters from 1 to 42
            (115, 1133),  # Sum of letters from 1 to 115
            (342, 6117),  # Sum of letters from 1 to 342
            (1000, 21124),  # Sum of letters from 1 to 1000
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """Get solution functions for Problem 017."""
        return [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """Get parameters for the main problem."""
        return (1000,)

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """Get demonstration functions for Problem 017."""
        return [self._demonstrate_number_words]

    def _demonstrate_number_words(self) -> None:
        """数値の英単語変換例を表示"""
        examples = [1, 5, 12, 21, 42, 115, 342, 1000]

        print("数値から英単語への変換例:")
        for num in examples:
            words = number_to_words(num)
            letter_count = count_letters(words)
            print(f"{num:4d}: '{words}' → {letter_count} letters")

        print(f"\n1から1000までの文字数合計: {solve_optimized(1000)}")

        print("\n各桁数別の分析:")
        ranges = [
            (1, 9, "1桁"),
            (10, 19, "10代"),
            (20, 99, "2桁"),
            (100, 999, "3桁"),
            (1000, 1000, "1000"),
        ]

        for start, end, description in ranges:
            if start == end:
                count = count_letters(number_to_words(start))
                print(f"{description}: {count} letters")
            else:
                total = sum(
                    count_letters(number_to_words(i)) for i in range(start, end + 1)
                )
                average = total / (end - start + 1)
                print(
                    f"{description} ({start}-{end}): 総計 {total}, 平均 {average:.1f} letters"
                )


def main() -> None:
    """Main entry point."""
    # デフォルト実行（パフォーマンステストのみ無効、デモンストレーションは有効）
    runner = Problem017Runner(enable_demonstrations=True)
    runner.main()


def run_with_all_features() -> None:
    """Run with all features enabled for demonstration."""
    print("=== 全機能有効 ===")
    runner = Problem017Runner(enable_performance_test=True, enable_demonstrations=True)
    runner.main()


def run_benchmark() -> None:
    """Run performance benchmark for Problem 017."""
    print("=== Problem 017 Performance Benchmark ===")
    runner = Problem017Runner(enable_performance_test=True, enable_demonstrations=False)
    # Skip tests and run only the performance benchmark
    result = runner.run_problem()
    print(f"Benchmark result: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        run_benchmark()
    else:
        main()
