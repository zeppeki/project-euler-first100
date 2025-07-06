"""
Display and formatting utilities for Project Euler solutions.
"""

from collections.abc import Callable
from typing import Any


def print_test_results(
    test_cases: list[tuple[Any, ...]], functions: list[tuple[str, Callable[..., Any]]]
) -> None:
    """
    Print test results for multiple functions with test cases.

    Args:
        test_cases: List of (input, expected_output) tuples
        functions: List of (name, function) tuples to test
    """
    print("=== テストケース ===")

    for test_case in test_cases:
        inputs = test_case[:-1]
        expected = test_case[-1]

        print(f"入力: {inputs if len(inputs) > 1 else inputs[0]}")
        print(f"期待値: {expected}")

        for name, func in functions:
            try:
                result = func(*inputs)
                status = "✓" if result == expected else "✗"
                print(f"  {name}: {result} {status}")
            except Exception as e:
                print(f"  {name}: エラー - {e}")

        print()


def print_performance_comparison(
    performance_results: dict[str, dict[str, Any]],
) -> None:
    """
    Print performance comparison results.

    Args:
        performance_results: Results from compare_performance function
    """
    print("=== パフォーマンス比較 ===")

    for name, data in performance_results.items():
        execution_time = data["execution_time"]
        relative_speed = data.get("relative_speed", 1.0)
        print(f"{name}: {execution_time:.6f}秒 ({relative_speed:.2f}x)")


def print_solution_header(problem_number: str, title: str, limit: Any = None) -> None:
    """
    Print solution header.

    Args:
        problem_number: Problem number (e.g., "001")
        title: Problem title
        limit: Problem limit/parameter if applicable
    """
    print(f"=== Problem {problem_number}: {title} ===")
    if limit is not None:
        print(f"Limit: {limit}")
    print()


def print_final_answer(result: Any, verified: bool = True) -> None:
    """
    Print final answer with verification status.

    Args:
        result: The calculated result
        verified: Whether all solutions agree
    """
    print("=== 本問題の解答 ===")
    if verified:
        # Handle different result types appropriately
        if isinstance(result, int | float):
            print(f"✓ 解答: {result:,}")
        else:
            print(f"✓ 解答: {result}")
    else:
        print("✗ 解答が一致しません")
    print()
