#!/usr/bin/env python3
"""
Comprehensive benchmark runner for Project Euler solutions.

This module provides automated benchmarking capabilities that integrate with the
existing problem structure and runner architecture.
"""

import importlib
import json
import sys
from pathlib import Path
from typing import Any

from .benchmark import BenchmarkSuite, ProblemBenchmark


class ProjectEulerBenchmarkRunner:
    """Benchmark runner for Project Euler problems."""

    def __init__(self, benchmark_suite: BenchmarkSuite | None = None):
        """Initialize the benchmark runner."""
        self.suite = benchmark_suite or BenchmarkSuite()
        self.problems_dir = Path(__file__).parent.parent
        self.benchmarks_dir = Path(__file__).parent.parent.parent / "benchmarks"

    def discover_problems(self) -> list[str]:
        """Discover all available problem modules."""
        problem_files = list(self.problems_dir.glob("problem_*.py"))
        problem_numbers = []

        for file in problem_files:
            # Extract problem number from filename
            stem = file.stem  # e.g., "problem_001"
            if stem.startswith("problem_"):
                number = stem[8:]  # Remove "problem_" prefix
                problem_numbers.append(number)

        return sorted(problem_numbers)

    def get_problem_info(self, problem_number: str) -> dict[str, Any]:
        """Get problem information from module docstring."""
        try:
            module_name = f"problem_{problem_number}"
            module = importlib.import_module(f"problems.{module_name}")

            # Parse docstring for problem title
            docstring = module.__doc__ or ""
            lines = docstring.strip().split("\n")

            title = "Unknown Problem"
            for line in lines:
                if line.startswith("Problem"):
                    # Extract title from "Problem XXX: Title" format
                    if ":" in line:
                        title = line.split(":", 1)[1].strip()
                    break

            return {
                "number": problem_number,
                "title": title,
                "module": module,
            }

        except ImportError:
            return {
                "number": problem_number,
                "title": f"Problem {problem_number}",
                "module": None,
            }

    def discover_solution_functions(
        self, module: Any
    ) -> list[tuple[str, Any, str, str]]:
        """
        Discover solution functions in a problem module.

        Returns:
            List of (name, function, algorithm_type, complexity_class) tuples
        """
        solutions = []

        # Standard solution function patterns
        function_patterns = [
            ("solve_naive", "素直な解法", "naive", "O(n)"),
            ("solve_optimized", "最適化解法", "optimized", "O(log n)"),
            ("solve_mathematical", "数学的解法", "mathematical", "O(1)"),
        ]

        for func_name, display_name, algo_type, default_complexity in function_patterns:
            if hasattr(module, func_name):
                func = getattr(module, func_name)

                # Try to extract complexity from docstring
                complexity = default_complexity
                if func.__doc__:
                    for line in func.__doc__.split("\n"):
                        if "時間計算量:" in line or "Time complexity:" in line:
                            # Extract O(...) notation
                            if "O(" in line:
                                start = line.find("O(")
                                end = line.find(")", start)
                                if end > start:
                                    complexity = line[start : end + 1]
                            break

                solutions.append((display_name, func, algo_type, complexity))

        return solutions

    def determine_problem_input(
        self, problem_number: str, _module: Any
    ) -> dict[str, Any]:
        """Determine input parameters for a problem based on standard patterns."""
        # Default input patterns for common problem types
        default_inputs = {
            "001": {"limit": 1000},
            "002": {"limit": 4000000},
            "003": {"n": 600851475143},
            "004": {"digits": 3},
            "005": {"n": 20},
            "006": {"n": 100},
            "007": {"n": 10001},
            "008": {"consecutive_digits": 13},
            "009": {"target_sum": 1000},
            "010": {"limit": 2000000},
            # Add more as needed
        }

        if problem_number in default_inputs:
            return default_inputs[problem_number]

        # Try to extract from runner module or use common patterns
        try:
            runner_module = importlib.import_module(
                f"problems.runners.problem_{problem_number}_runner"
            )

            # Look for run_problem function and extract parameters
            if hasattr(runner_module, "run_problem"):
                # This is a heuristic - you might need to adjust based on actual patterns
                source = runner_module.run_problem.__doc__ or ""
                if "limit" in source.lower():
                    return {"limit": 1000}  # Default limit
                if "target" in source.lower():
                    return {"target": 1000}  # Default target

        except ImportError:
            pass

        # Fallback - return empty dict, solutions should handle no parameters
        return {}

    def benchmark_single_problem(self, problem_number: str) -> ProblemBenchmark | None:
        """Benchmark a single problem."""
        print(f"Benchmarking Problem {problem_number}...")

        problem_info = self.get_problem_info(problem_number)
        if not problem_info["module"]:
            print(f"  ⚠ Warning: Could not import problem_{problem_number}")
            return None

        module = problem_info["module"]
        solutions = self.discover_solution_functions(module)

        if not solutions:
            print(
                f"  ⚠ Warning: No solution functions found in problem_{problem_number}"
            )
            return None

        input_params = self.determine_problem_input(problem_number, module)

        try:
            # Convert input_params to args for the function calls
            args = []
            kwargs = {}

            # Common parameter patterns
            if "limit" in input_params:
                args = [input_params["limit"]]
            elif "n" in input_params:
                args = [input_params["n"]]
            elif "digits" in input_params:
                args = [input_params["digits"]]
            elif "consecutive_digits" in input_params:
                args = [input_params["consecutive_digits"]]
            elif "target_sum" in input_params:
                args = [input_params["target_sum"]]
            else:
                # Try with no arguments first
                args = []

            benchmark_result = self.suite.benchmark_problem(
                problem_number,
                problem_info["title"],
                solutions,
                input_params,
                *args,
                **kwargs,
            )

            # Save individual result
            individual_path = (
                self.benchmarks_dir / "individual" / f"problem_{problem_number}.json"
            )
            individual_path.parent.mkdir(parents=True, exist_ok=True)

            with open(individual_path, "w", encoding="utf-8") as f:
                json.dump(benchmark_result, f, indent=2, ensure_ascii=False)

            print(f"  ✓ Completed - Fastest: {benchmark_result['fastest_solution']}")
            return benchmark_result

        except Exception as e:
            print(f"  ✗ Error benchmarking problem {problem_number}: {e}")
            return None

    def benchmark_all_problems(self, problem_numbers: list[str] | None = None) -> None:
        """Benchmark all or specified problems."""
        if problem_numbers is None:
            problem_numbers = self.discover_problems()

        print(f"Starting benchmark run for {len(problem_numbers)} problems...")
        print("=" * 60)

        successful_benchmarks = 0
        self.suite.results.clear()  # Reset results

        for problem_number in problem_numbers:
            result = self.benchmark_single_problem(problem_number)
            if result:
                self.suite.results.append(result)
                successful_benchmarks += 1

        print("=" * 60)
        print(
            f"Benchmark completed: {successful_benchmarks}/{len(problem_numbers)} problems"
        )

        # Save aggregated results
        aggregated_path = self.benchmarks_dir / "aggregated" / "latest.json"
        self.suite.save_results(aggregated_path)
        print(f"Results saved to {aggregated_path}")

        # Generate summary report
        self._generate_summary_report()

    def _generate_summary_report(self) -> None:
        """Generate a human-readable summary report."""
        if not self.suite.results:
            return

        report_path = self.benchmarks_dir / "reports" / "performance_summary.txt"
        report_path.parent.mkdir(parents=True, exist_ok=True)

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("PROJECT EULER PERFORMANCE BENCHMARK SUMMARY\n")
            f.write("=" * 50 + "\n\n")

            summary = self.suite._generate_summary()  # noqa: SLF001

            f.write(f"Total Problems Benchmarked: {summary.get('total_problems', 0)}\n")
            f.write(f"Verification Rate: {summary.get('verification_rate', 0):.1%}\n")
            f.write(f"Total Solutions: {summary.get('total_solutions', 0)}\n\n")

            # Algorithm distribution
            algo_dist = summary.get("algorithm_distribution", {})
            f.write("Algorithm Type Distribution:\n")
            f.writelines(
                f"  {algo_type}: {count}\n" for algo_type, count in algo_dist.items()
            )
            f.write("\n")

            # Performance statistics
            perf_stats = summary.get("performance_stats", {})
            if perf_stats:
                f.write("Performance Statistics:\n")
                f.write(
                    f"  Mean Execution Time: {perf_stats.get('mean_execution_time', 0):.6f}s\n"
                )
                f.write(
                    f"  Median Execution Time: {perf_stats.get('median_execution_time', 0):.6f}s\n"
                )
                f.write(
                    f"  Fastest Solution: {perf_stats.get('fastest_execution_time', 0):.6f}s\n"
                )
                f.write(
                    f"  Slowest Solution: {perf_stats.get('slowest_execution_time', 0):.6f}s\n\n"
                )

            # Top performers
            f.write("Top 10 Fastest Solutions:\n")
            all_solutions = []
            for problem in self.suite.results:
                for solution in problem["solutions"]:
                    if solution["mean_time"] != float("inf"):
                        all_solutions.append(
                            (
                                f"Problem {problem['problem_number']}",
                                solution["name"],
                                solution["mean_time"],
                                solution["complexity_class"],
                            )
                        )

            all_solutions.sort(key=lambda x: x[2])  # Sort by execution time
            for i, (problem, solution, time, complexity) in enumerate(
                all_solutions[:10]
            ):
                f.write(
                    f"  {i + 1:2d}. {problem} - {solution}: {time:.6f}s ({complexity})\n"
                )

        print(f"Summary report saved to {report_path}")


def main() -> None:
    """Main entry point for standalone execution."""
    if len(sys.argv) > 1:
        # Benchmark specific problems
        problem_numbers = sys.argv[1:]
        runner = ProjectEulerBenchmarkRunner()
        runner.benchmark_all_problems(problem_numbers)
    else:
        # Benchmark all problems
        runner = ProjectEulerBenchmarkRunner()
        runner.benchmark_all_problems()


if __name__ == "__main__":
    main()
