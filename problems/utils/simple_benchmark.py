#!/usr/bin/env python3
"""
Simple benchmark framework for Project Euler problems.

This module provides a streamlined benchmarking system optimized for learning
and understanding algorithm performance in the context of Project Euler's
one-minute rule and educational objectives.
"""

import re
import time
from collections.abc import Callable
from typing import Any, TypedDict


class SimpleSolutionMetrics(TypedDict):
    """Simple metrics for a single solution approach."""

    name: str
    function_name: str
    algorithm_type: str  # naive, optimized, mathematical
    result: Any
    execution_time: float
    relative_speed: float
    complexity_class: str  # O(1), O(log n), O(n), etc.
    one_minute_rule: bool


class SimpleProblemBenchmark(TypedDict):
    """Simple benchmark results for a problem."""

    problem_number: str
    problem_title: str
    timestamp: str
    solutions: list[SimpleSolutionMetrics]
    fastest_solution: str
    verified: bool


class SimpleBenchmark:
    """
    Simplified benchmark framework for Project Euler problems.

    Focuses on learning outcomes and one-minute rule verification
    rather than statistical analysis.
    """

    def __init__(self) -> None:
        self.results: dict[str, SimpleProblemBenchmark] = {}

    def extract_complexity(self, func: Callable) -> str:
        """
        Extract time complexity from function docstring.

        Args:
            func: Function to analyze

        Returns:
            Time complexity string (e.g., "O(n)", "O(log n)")
        """
        if not func.__doc__:
            return "O(?)"

        # Look for time complexity patterns in docstring
        patterns = [
            r"時間計算量[:\s]*([O]\([^)]+\))",
            r"Time complexity[:\s]*([O]\([^)]+\))",
            r"([O]\([^)]+\))",
        ]

        for pattern in patterns:
            match = re.search(pattern, func.__doc__, re.IGNORECASE)
            if match:
                return match.group(1)

        return "O(?)"

    def extract_algorithm_type(self, func_name: str) -> str:
        """
        Extract algorithm type from function name.

        Args:
            func_name: Name of the function

        Returns:
            Algorithm type (naive, optimized, mathematical)
        """
        if "naive" in func_name.lower():
            return "naive"
        if "optimized" in func_name.lower():
            return "optimized"
        if "mathematical" in func_name.lower():
            return "mathematical"
        if "builtin" in func_name.lower():
            return "builtin"

        return "unknown"

    def check_one_minute_rule(self, execution_time: float) -> bool:
        """
        Check if execution time satisfies Project Euler's one-minute rule.

        Args:
            execution_time: Execution time in seconds

        Returns:
            True if under 60 seconds, False otherwise
        """
        return execution_time <= 60.0

    def benchmark_solution(
        self, name: str, func: Callable, *args: Any, **kwargs: Any
    ) -> SimpleSolutionMetrics:
        """
        Benchmark a single solution with simple one-time measurement.

        Args:
            name: Human-readable name for the solution
            func: Function to benchmark
            *args: Arguments to pass to the function
            **kwargs: Keyword arguments to pass to the function

        Returns:
            Metrics for the solution
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time

        return {
            "name": name,
            "function_name": func.__name__,
            "algorithm_type": self.extract_algorithm_type(func.__name__),
            "result": result,
            "execution_time": execution_time,
            "relative_speed": 1.0,  # Will be calculated later
            "complexity_class": self.extract_complexity(func),
            "one_minute_rule": self.check_one_minute_rule(execution_time),
        }

    def benchmark_problem(
        self,
        problem_number: str,
        problem_title: str,
        solutions: list[tuple[str, Callable]],
        *args: Any,
        **kwargs: Any,
    ) -> SimpleProblemBenchmark:
        """
        Benchmark all solutions for a problem.

        Args:
            problem_number: Problem number (e.g., "001")
            problem_title: Problem title
            solutions: List of (name, function) tuples
            *args: Arguments to pass to all functions
            **kwargs: Keyword arguments to pass to all functions

        Returns:
            Complete benchmark results for the problem
        """
        metrics_list = []

        # Benchmark each solution
        for name, func in solutions:
            try:
                metrics = self.benchmark_solution(name, func, *args, **kwargs)
                metrics_list.append(metrics)
            except Exception as e:
                print(f"Error benchmarking {name}: {e}")
                continue

        # Verify all solutions agree
        if metrics_list:
            first_result = metrics_list[0]["result"]
            verified = all(m["result"] == first_result for m in metrics_list)
        else:
            verified = False

        # Calculate relative speeds
        if metrics_list:
            fastest_time = min(m["execution_time"] for m in metrics_list)
            for metrics in metrics_list:
                metrics["relative_speed"] = metrics["execution_time"] / fastest_time

            # Find fastest solution
            fastest_solution = min(metrics_list, key=lambda x: x["execution_time"])[
                "name"
            ]
        else:
            fastest_solution = "N/A"

        benchmark_result: SimpleProblemBenchmark = {
            "problem_number": problem_number,
            "problem_title": problem_title,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "solutions": metrics_list,
            "fastest_solution": fastest_solution,
            "verified": verified,
        }

        self.results[problem_number] = benchmark_result
        return benchmark_result

    def display_results(self, problem_number: str) -> None:
        """
        Display benchmark results in a learning-friendly format.

        Args:
            problem_number: Problem number to display
        """
        if problem_number not in self.results:
            print(f"No results found for Problem {problem_number}")
            return

        result = self.results[problem_number]

        print(f"\nProblem {result['problem_number']}: {result['problem_title']}")
        print("=" * 60)
        print(f"Timestamp: {result['timestamp']}")
        print(f"Solutions verified: {'✓' if result['verified'] else '✗'}")
        print(f"Fastest solution: {result['fastest_solution']}")
        print()

        # Display solution results
        for metrics in result["solutions"]:
            one_minute = "✓" if metrics["one_minute_rule"] else "✗"
            print(f"Solution: {metrics['name']}")
            print(f"  Algorithm type: {metrics['algorithm_type']}")
            print(f"  Time complexity: {metrics['complexity_class']}")
            print(f"  Execution time: {metrics['execution_time']:.6f}s")
            print(f"  Relative speed: {metrics['relative_speed']:.1f}x")
            print(f"  One-minute rule: {one_minute}")
            print(f"  Result: {metrics['result']}")
            print()

    def save_results(self, filepath: str) -> None:
        """
        Save benchmark results to JSON file.

        Args:
            filepath: Path to save the results
        """
        import json
        from pathlib import Path

        Path(filepath).parent.mkdir(parents=True, exist_ok=True)

        with open(filepath, "w") as f:
            json.dump(self.results, f, indent=2, default=str)

        print(f"Results saved to {filepath}")
