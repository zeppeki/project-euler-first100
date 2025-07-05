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

    def __init__(
        self,
        problem_number: str,
        problem_title: str,
        problem_answer: Any = None,
        enable_performance_test: bool = False,
        enable_demonstrations: bool = False,
    ):
        """
        Initialize the problem runner.

        Args:
            problem_number: Problem number (e.g., "001")
            problem_title: Problem title for display
            problem_answer: Expected answer for the problem (optional)
            enable_performance_test: Whether to run performance comparison (default: False)
            enable_demonstrations: Whether to run additional demonstrations (default: False)
        """
        self.problem_number = problem_number
        self.problem_title = problem_title
        self.problem_answer = problem_answer
        self.enable_performance_test = enable_performance_test
        self.enable_demonstrations = enable_demonstrations

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
        Run the main problem and verify the answer.
        Optionally run performance analysis and demonstrations.

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

        # Get the primary solution (first function)
        primary_function = functions[0][1]

        if self.enable_performance_test and len(functions) > 1:
            # Run performance comparison with all functions
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
            final_result = results[0] if results else None

        else:
            # Just run the primary function without performance comparison
            try:
                final_result = primary_function(*main_params)
                verified = True
            except Exception as e:
                print(f"エラー: 解法実行に失敗しました: {e}")
                return None

        # Handle tuple results (e.g., Problem 004 returns (palindrome, factor1, factor2))
        if isinstance(final_result, tuple):
            display_result = final_result[0]  # Use first element for display
        else:
            display_result = final_result

        # Check against expected answer if provided
        answer_correct = True
        if self.problem_answer is not None:
            if display_result == self.problem_answer:
                print(f"✓ 解答が期待値と一致: {self.problem_answer}")
            else:
                print(
                    f"✗ 解答が期待値と不一致: 期待値={self.problem_answer}, 実際={display_result}"
                )
                answer_correct = False

        print_final_answer(display_result, verified=verified and answer_correct)

        # Run demonstrations if enabled and available
        if self.enable_demonstrations:
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
