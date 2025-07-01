#!/usr/bin/env python3
"""
Base Problem Runner for Project Euler Solutions.

This module provides the abstract base class for all Project Euler problem runners,
standardizing test execution, performance measurement, and result display.
"""

from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
    print_test_results,
)
from problems.utils.performance import compare_performance


class BaseProblemRunner(ABC):
    """
    Abstract base class for Project Euler problem runners.

    This class provides a consistent interface for running problems with
    test verification, performance analysis, and result display.
    """

    def __init__(self, problem_number: str, problem_title: str):
        """
        Initialize the problem runner.

        Args:
            problem_number: Problem number (e.g., "001")
            problem_title: Problem title for display
        """
        self.problem_number = problem_number
        self.problem_title = problem_title

    @abstractmethod
    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """
        Get test cases for the problem.

        Returns:
            List of tuples where each tuple contains (input_args..., expected_result)
        """

    @abstractmethod
    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """
        Get solution functions to test and compare.

        Returns:
            List of (function_name, function) tuples
        """

    @abstractmethod
    def get_main_parameters(self) -> tuple[Any, ...]:
        """
        Get parameters for the main problem execution.

        Returns:
            Tuple of arguments to pass to solution functions for the main problem
        """

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """
        Get optional demonstration functions for complex analysis.

        Returns:
            List of demonstration functions, or None if not applicable
        """
        return None

    def run_tests(self) -> bool:
        """
        Run test cases to verify solution correctness.

        Returns:
            True if all tests pass, False otherwise
        """
        test_cases = self.get_test_cases()
        functions = self.get_solution_functions()

        if not test_cases or not functions:
            print("警告: テストケースまたは解法関数が定義されていません")
            return False

        print_test_results(test_cases, functions)

        # Verify all functions produce correct results for all test cases
        all_passed = True
        for test_case in test_cases:
            inputs = test_case[:-1]
            expected = test_case[-1]

            for name, func in functions:
                try:
                    result = func(*inputs)
                    if result != expected:
                        print(
                            f"テスト失敗: {name} - 期待値: {expected}, 実際: {result}"
                        )
                        all_passed = False
                except Exception as e:
                    print(f"テスト失敗: {name} - エラー: {e}")
                    all_passed = False

        return all_passed

    def run_problem(self) -> Any:
        """
        Run the main problem with performance analysis.

        Returns:
            The problem solution result
        """
        # Print problem header
        main_params = self.get_main_parameters()
        limit_display = main_params[0] if main_params else None
        print_solution_header(self.problem_number, self.problem_title, limit_display)

        # Get solution functions
        functions = self.get_solution_functions()
        if not functions:
            print("エラー: 解法関数が定義されていません")
            return None

        # Run performance comparison
        performance_results = compare_performance(functions, *main_params)

        # Display performance results
        print_performance_comparison(performance_results)

        # Verify all solutions agree
        results = [data["result"] for data in performance_results.values()]

        # For tuple results, compare the first element (main answer)
        if results and isinstance(results[0], tuple):
            comparison_values = [result[0] for result in results]
        else:
            comparison_values = results

        verified = len(set(comparison_values)) == 1

        # Display final answer
        final_result = results[0] if results else None

        # Handle tuple results (e.g., Problem 004 returns (palindrome, factor1, factor2))
        if isinstance(final_result, tuple):
            display_result = final_result[0]  # Use first element for display
        else:
            display_result = final_result

        print_final_answer(display_result, verified=verified)

        # Run demonstrations if available
        demonstrations = self.get_demonstration_functions()
        if demonstrations:
            print("=== 追加デモンストレーション ===")
            for demo_func in demonstrations:
                try:
                    demo_func()
                    print()
                except Exception as e:
                    print(f"デモンストレーションエラー: {e}")
                    print()

        return final_result

    def main(self) -> None:
        """
        Main entry point for the problem runner.

        Runs tests first, then executes the main problem if tests pass.
        """
        print(f"=== Problem {self.problem_number} Runner ===")
        print()

        # Run tests first
        tests_passed = self.run_tests()

        if tests_passed:
            print("✓ 全てのテストが通過しました")
            print()

            # Run main problem
            self.run_problem()
        else:
            print("✗ テストが失敗しました。問題を確認してください。")
            return

        print("=== 実行完了 ===")
