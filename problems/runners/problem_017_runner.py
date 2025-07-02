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

    def __init__(self) -> None:
        super().__init__("017", "Number Letter Counts")

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """Get test cases for Problem 017."""
        test_cases = []
        numbers_words = [
            (1, "one"),
            (2, "two"),
            (5, "five"),
            (12, "twelve"),
            (21, "twenty one"),
            (42, "forty two"),
            (115, "one hundred and fifteen"),
            (342, "three hundred and forty two"),
            (1000, "one thousand"),
        ]

        for num, words in numbers_words:
            expected = count_letters(words)
            test_cases.append((num, expected))

        return test_cases

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

    def get_demonstration_functions(self) -> list[tuple[str, Callable[[], None]]]:
        """Get demonstration functions for Problem 017."""
        return [("数値の英単語変換例", self._demonstrate_number_words)]

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
    """メイン関数"""
    runner = Problem017Runner()
    runner.main()


if __name__ == "__main__":
    main()
