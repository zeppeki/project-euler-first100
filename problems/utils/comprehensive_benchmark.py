#!/usr/bin/env python3
"""
Comprehensive benchmark system for Project Euler problems with timeout functionality.

This module provides a complete benchmarking system with the following features:
- 60-second timeout for individual solution methods
- Comprehensive coverage of all 75 implemented problems
- Enhanced data structure with detailed execution information
- Error recovery and retry mechanisms
- Integration with the existing simple benchmark framework
"""

import importlib
import json
import signal
import time
from collections.abc import Callable, Generator
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Any

from .simple_benchmark import SimpleBenchmark
from .simple_runner import SimpleBenchmarkRunner


class TimeoutError(Exception):
    """Custom exception for timeout scenarios."""


@contextmanager
def timeout_context(seconds: int) -> Generator[None, None, None]:
    """
    Context manager for setting a timeout using signal.alarm.

    Args:
        seconds: Timeout duration in seconds

    Raises:
        TimeoutError: If the operation exceeds the timeout
    """

    def timeout_handler(signum: int, frame: Any) -> None:
        del signum, frame  # Suppress unused argument warnings
        raise TimeoutError(f"Operation timed out after {seconds} seconds")

    # Set up the signal handler
    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)

    try:
        yield
    finally:
        # Restore the old signal handler and cancel the alarm
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)


class ComprehensiveBenchmark:
    """
    Comprehensive benchmark system with timeout functionality.

    This class extends the simple benchmark framework with:
    - Timeout-based execution control
    - Enhanced error handling and recovery
    - Detailed execution metadata
    - Comprehensive problem coverage
    """

    def __init__(self, timeout_seconds: int = 60):
        """
        Initialize the comprehensive benchmark system.

        Args:
            timeout_seconds: Timeout for individual solution methods (default: 60)
        """
        self.timeout_seconds = timeout_seconds
        self.simple_benchmark = SimpleBenchmark()
        self.simple_runner = SimpleBenchmarkRunner()
        self.results: dict[str, dict[str, Any]] = {}
        self.failed_problems: list[str] = []
        self.timeout_problems: list[str] = []

    def benchmark_solution_with_timeout(
        self, name: str, func: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> dict[str, Any]:
        """
        Benchmark a single solution with timeout protection.

        Args:
            name: Name of the solution method
            func: Solution function to benchmark
            *args: Arguments to pass to the function
            **kwargs: Keyword arguments to pass to the function

        Returns:
            Dict containing execution results and metadata
        """
        result_data: dict[str, Any] = {
            "name": name,
            "status": "unknown",
            "time": None,
            "result": None,
            "error": None,
            "timeout": False,
        }

        try:
            with timeout_context(self.timeout_seconds):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()

                execution_time = end_time - start_time
                result_data.update(
                    {
                        "status": "success",
                        "time": execution_time,
                        "result": "[隠匿]",  # Hide actual result for Project Euler policy
                        "raw_result": result,  # Keep raw result for validation
                    }
                )

        except TimeoutError:
            result_data.update(
                {
                    "status": "timeout",
                    "timeout": True,
                    "error": f"Timed out after {self.timeout_seconds} seconds",
                }
            )

        except Exception as e:
            result_data.update({"status": "error", "error": str(e)})

        return result_data

    def benchmark_problem_comprehensive(self, problem_number: str) -> dict[str, Any]:
        """
        Perform comprehensive benchmarking for a single problem.

        Args:
            problem_number: Problem number (e.g., "001")

        Returns:
            Dict containing comprehensive benchmark results
        """
        print(f"Benchmarking Problem {problem_number}...")

        try:
            # Import the problem module
            module_name = f"problems.problem_{problem_number.zfill(3)}"
            problem_module = importlib.import_module(module_name)

            # Try to get runner for expected answer checking
            runner = None
            try:
                runner_module_name = (
                    f"problems.runners.problem_{problem_number.zfill(3)}_runner"
                )
                runner_module = importlib.import_module(runner_module_name)
                runner_class_name = f"Problem{problem_number.zfill(3)}Runner"
                runner_class = getattr(runner_module, runner_class_name)
                runner = runner_class()
            except (ImportError, AttributeError):
                # No runner available, continue without expected answer checking
                pass

            # Get problem information
            problem_title = self.simple_runner.get_problem_title(problem_module)
            args, kwargs = self.simple_runner.get_problem_arguments(problem_number)
            solutions = self.simple_runner.discover_solutions(problem_module)

            if not solutions:
                return {
                    "status": "error",
                    "error": f"No solution functions found in {module_name}",
                }

            # Benchmark each solution with timeout
            solution_results = []
            successful_solutions = []

            for solution_name, solution_func in solutions:
                print(f"  Testing {solution_name}...")

                result_data = self.benchmark_solution_with_timeout(
                    solution_name, solution_func, *args, **kwargs
                )

                solution_results.append(result_data)

                if result_data["status"] == "success":
                    successful_solutions.append(result_data)
                    print(f"    ✓ {result_data['time']:.6f}s")
                elif result_data["status"] == "timeout":
                    print(f"    ⏱ Timeout ({self.timeout_seconds}s)")
                else:
                    print(f"    ✗ Error: {result_data['error']}")

            # Analyze results
            problem_result = {
                "problem_number": problem_number,
                "problem_title": problem_title,
                "timestamp": datetime.now().isoformat(),
                "solutions": solution_results,
                "total_solutions": len(solutions),
                "successful_solutions": len(successful_solutions),
                "timeout_solutions": len(
                    [s for s in solution_results if s["status"] == "timeout"]
                ),
                "error_solutions": len(
                    [s for s in solution_results if s["status"] == "error"]
                ),
                "status": "success" if successful_solutions else "failed",
            }

            # Add performance analysis for successful solutions
            if successful_solutions:
                # Find fastest solution
                fastest = min(successful_solutions, key=lambda x: x["time"])
                problem_result["fastest_solution"] = fastest["name"]
                problem_result["fastest_time"] = fastest["time"]

                # Check one-minute rule compliance
                all_under_60s = all(s["time"] < 60.0 for s in successful_solutions)
                problem_result["one_minute_rule"] = all_under_60s

                # Verify all solutions produce same result
                results = [s["raw_result"] for s in successful_solutions]
                if len({str(r) for r in results}) == 1:
                    problem_result["result_consistency"] = True
                    problem_result["verified_result"] = "[隠匿]"

                    # Check against expected answer if available
                    common_result = results[0]
                    if (
                        runner is not None
                        and hasattr(runner, "problem_answer")
                        and runner.problem_answer is not None
                    ):
                        if common_result == runner.problem_answer:
                            problem_result["answer_correct"] = True
                        else:
                            problem_result["answer_correct"] = False
                            problem_result["status"] = "error"
                            problem_result["error"] = (
                                f"Result {common_result} does not match expected answer {runner.problem_answer}"
                            )
                            problem_result["warning"] = (
                                f"Expected {runner.problem_answer}, got {common_result}"
                            )
                else:
                    problem_result["result_consistency"] = False
                    problem_result["status"] = "error"
                    problem_result["error"] = "Solutions produced different results"
                    problem_result["warning"] = "Solutions produced different results"

            return problem_result

        except ImportError as e:
            return {
                "status": "error",
                "error": f"Could not import problem {problem_number}: {e}",
            }
        except Exception as e:
            return {
                "status": "error",
                "error": f"Unexpected error for problem {problem_number}: {e}",
            }

    def discover_all_problems(self) -> list[str]:
        """
        Discover all available problem numbers.

        Returns:
            List of problem numbers as strings
        """
        problems_dir = Path("problems")
        problem_files = list(problems_dir.glob("problem_*.py"))
        problem_numbers = []

        for file in problem_files:
            number = self.simple_runner.extract_problem_number(file.stem)
            if number:
                problem_numbers.append(number)

        return sorted(problem_numbers)

    def run_comprehensive_benchmark(
        self, problem_numbers: list[str] | None = None
    ) -> dict[str, Any]:
        """
        Run comprehensive benchmark for all or specified problems.

        Args:
            problem_numbers: List of problem numbers to benchmark (None for all)

        Returns:
            Dict containing comprehensive benchmark results
        """
        if problem_numbers is None:
            problem_numbers = self.discover_all_problems()

        print("=== Comprehensive Benchmark System ===")
        print(f"Timeout: {self.timeout_seconds} seconds per solution")
        print(f"Problems to benchmark: {len(problem_numbers)}")
        print("=" * 50)

        start_time = time.perf_counter()
        results = {}

        for i, problem_number in enumerate(problem_numbers, 1):
            print(f"[{i}/{len(problem_numbers)}] ", end="")

            problem_result = self.benchmark_problem_comprehensive(problem_number)
            results[problem_number] = problem_result

            # Track failed and timeout problems
            if problem_result["status"] == "error":
                self.failed_problems.append(problem_number)
            elif problem_result.get("timeout_solutions", 0) > 0:
                self.timeout_problems.append(problem_number)

            print()

        end_time = time.perf_counter()
        total_time = end_time - start_time

        # Generate comprehensive summary
        successful_problems = [p for p in results.values() if p["status"] == "success"]
        failed_problems = [p for p in results.values() if p["status"] == "error"]

        summary = {
            "benchmark_info": {
                "version": "2.0",
                "timestamp": datetime.now().isoformat(),
                "timeout_seconds": self.timeout_seconds,
                "total_problems": len(problem_numbers),
                "total_execution_time": total_time,
            },
            "summary": {
                "successful_problems": len(successful_problems),
                "failed_problems": len(failed_problems),
                "problems_with_timeouts": len(self.timeout_problems),
                "total_solutions_tested": sum(
                    p.get("total_solutions", 0) for p in results.values()
                ),
                "total_successful_solutions": sum(
                    p.get("successful_solutions", 0) for p in results.values()
                ),
                "total_timeout_solutions": sum(
                    p.get("timeout_solutions", 0) for p in results.values()
                ),
                "one_minute_rule_compliance": len(
                    [p for p in successful_problems if p.get("one_minute_rule", False)]
                ),
                "result_consistency_rate": len(
                    [
                        p
                        for p in successful_problems
                        if p.get("result_consistency", False)
                    ]
                )
                / len(successful_problems)
                if successful_problems
                else 0,
            },
            "problems": results,
        }

        # Display summary
        print("=" * 50)
        print("=== Benchmark Summary ===")
        print(f"Total problems: {len(problem_numbers)}")
        print(f"Successful: {len(successful_problems)}")
        print(f"Failed: {len(failed_problems)}")
        print(f"Problems with timeouts: {len(self.timeout_problems)}")
        print(f"Total execution time: {total_time:.2f}s")
        print(
            f"One-minute rule compliance: {summary['summary']['one_minute_rule_compliance']}/{len(successful_problems)}"
        )

        if self.failed_problems:
            print(f"Failed problems: {', '.join(self.failed_problems)}")

        if self.timeout_problems:
            print(f"Problems with timeouts: {', '.join(self.timeout_problems)}")

        return summary

    def save_results(self, filepath: str) -> None:
        """
        Save benchmark results to a JSON file.

        Args:
            filepath: Path to save the results
        """
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

        print(f"Results saved to: {filepath}")

    def retry_failed_problems(self) -> dict[str, Any]:
        """
        Retry benchmarking for previously failed problems.

        Returns:
            Dict containing retry benchmark results
        """
        if not self.failed_problems:
            print("No failed problems to retry.")
            return {}

        print(f"Retrying {len(self.failed_problems)} failed problems...")

        retry_results = self.run_comprehensive_benchmark(self.failed_problems)

        # Update failed problems list
        self.failed_problems = [
            p
            for p in self.failed_problems
            if retry_results["problems"][p]["status"] == "error"
        ]

        return retry_results


def main() -> None:
    """Main entry point for standalone execution."""
    import sys

    # Parse command line arguments
    timeout_seconds = 60
    specific_problems = []

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--timeout":
            timeout_seconds = int(args[i + 1])
            i += 2
        elif args[i] == "--problems":
            specific_problems = args[i + 1].split(",")
            i += 2
        else:
            specific_problems.append(args[i])
            i += 1

    # Initialize benchmark system
    benchmark = ComprehensiveBenchmark(timeout_seconds=timeout_seconds)

    # Run benchmark
    if specific_problems:
        results = benchmark.run_comprehensive_benchmark(specific_problems)
    else:
        results = benchmark.run_comprehensive_benchmark()

    # Save results
    results_dir = Path("benchmarks/results")
    results_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    filename = f"comprehensive_benchmark_{timestamp}.json"
    filepath = results_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Comprehensive benchmark results saved to: {filepath}")


if __name__ == "__main__":
    main()
