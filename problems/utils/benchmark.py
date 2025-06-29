#!/usr/bin/env python3
"""
Enhanced benchmark framework for systematic performance analysis.

This module provides comprehensive benchmarking capabilities for Project Euler solutions,
including detailed performance metrics, result storage, and analysis tools.
"""

import contextlib
import json
import statistics
import time
from collections.abc import Callable
from datetime import datetime
from pathlib import Path
from typing import Any, TypedDict

from .performance import compare_performance


class BenchmarkConfig(TypedDict):
    """Configuration for benchmark execution."""

    runs: int
    warmup_runs: int
    min_time: float  # minimum time to run each benchmark
    max_time: float  # maximum time to run each benchmark


class SolutionMetrics(TypedDict):
    """Performance metrics for a single solution approach."""

    name: str
    function_name: str
    algorithm_type: str  # naive, optimized, mathematical
    result: Any
    execution_times: list[float]
    mean_time: float
    median_time: float
    std_deviation: float
    min_time: float
    max_time: float
    relative_speed: float
    complexity_class: str  # O(1), O(log n), O(n), etc.


class ProblemBenchmark(TypedDict):
    """Complete benchmark results for a problem."""

    problem_number: str
    problem_title: str
    timestamp: str
    config: BenchmarkConfig
    input_parameters: dict[str, Any]
    solutions: list[SolutionMetrics]
    fastest_solution: str
    verified: bool
    total_benchmark_time: float


class BenchmarkSuite:
    """Advanced benchmarking suite for Project Euler solutions."""

    def __init__(self, config: BenchmarkConfig | None = None):
        """Initialize benchmark suite with configuration."""
        self.config = config or BenchmarkConfig(
            runs=5,
            warmup_runs=2,
            min_time=0.001,  # 1ms minimum
            max_time=10.0,  # 10s maximum
        )
        self.results: list[ProblemBenchmark] = []

    def benchmark_solution(
        self,
        name: str,
        func: Callable[..., Any],
        algorithm_type: str,
        complexity_class: str,
        *args: Any,
        **kwargs: Any,
    ) -> SolutionMetrics:
        """
        Benchmark a single solution with multiple runs and statistical analysis.

        Args:
            name: Human-readable name for the solution
            func: Function to benchmark
            algorithm_type: Type of algorithm (naive, optimized, mathematical)
            complexity_class: Big O notation for time complexity
            *args: Arguments to pass to the function
            **kwargs: Keyword arguments to pass to the function

        Returns:
            Detailed performance metrics
        """
        # Warmup runs
        for _ in range(self.config["warmup_runs"]):
            with contextlib.suppress(Exception):
                func(*args, **kwargs)

        execution_times: list[float] = []
        result = None

        # Determine number of runs based on execution time
        runs = self.config["runs"]

        for run in range(runs):
            start_time = time.perf_counter()
            try:
                current_result = func(*args, **kwargs)
                end_time = time.perf_counter()

                execution_time = end_time - start_time
                execution_times.append(execution_time)

                # Store result from first successful run
                if result is None:
                    result = current_result

                # Stop if taking too long
                if execution_time > self.config["max_time"]:
                    break

                # Increase runs if execution is very fast
                if execution_time < self.config["min_time"] and run == runs - 1:
                    additional_runs = min(
                        10, int(self.config["min_time"] / execution_time)
                    )
                    runs += additional_runs

            except Exception as e:
                # Record failed execution
                execution_times.append(float("inf"))
                if result is None:
                    result = f"Error: {e!s}"

        # Calculate statistics
        valid_times = [t for t in execution_times if t != float("inf")]

        if not valid_times:
            return SolutionMetrics(
                name=name,
                function_name=func.__name__,
                algorithm_type=algorithm_type,
                result=result,
                execution_times=execution_times,
                mean_time=float("inf"),
                median_time=float("inf"),
                std_deviation=0.0,
                min_time=float("inf"),
                max_time=float("inf"),
                relative_speed=float("inf"),
                complexity_class=complexity_class,
            )

        return SolutionMetrics(
            name=name,
            function_name=func.__name__,
            algorithm_type=algorithm_type,
            result=result,
            execution_times=execution_times,
            mean_time=statistics.mean(valid_times),
            median_time=statistics.median(valid_times),
            std_deviation=statistics.stdev(valid_times)
            if len(valid_times) > 1
            else 0.0,
            min_time=min(valid_times),
            max_time=max(valid_times),
            relative_speed=1.0,  # Will be calculated later
            complexity_class=complexity_class,
        )

    def benchmark_problem(
        self,
        problem_number: str,
        problem_title: str,
        solutions: list[
            tuple[str, Callable[..., Any], str, str]
        ],  # (name, func, algorithm_type, complexity)
        input_parameters: dict[str, Any],
        *args: Any,
        **kwargs: Any,
    ) -> ProblemBenchmark:
        """
        Benchmark all solutions for a single problem.

        Args:
            problem_number: Problem identifier (e.g., "001")
            problem_title: Human-readable problem title
            solutions: List of (name, function, algorithm_type, complexity_class) tuples
            input_parameters: Dictionary of input parameters used
            *args: Arguments to pass to all functions
            **kwargs: Keyword arguments to pass to all functions

        Returns:
            Complete benchmark results for the problem
        """
        benchmark_start_time = time.perf_counter()

        solution_metrics: list[SolutionMetrics] = []

        for name, func, algorithm_type, complexity_class in solutions:
            metrics = self.benchmark_solution(
                name, func, algorithm_type, complexity_class, *args, **kwargs
            )
            solution_metrics.append(metrics)

        # Calculate relative speeds
        valid_metrics = [m for m in solution_metrics if m["mean_time"] != float("inf")]
        if valid_metrics:
            fastest_time = min(m["mean_time"] for m in valid_metrics)
            for metrics in solution_metrics:
                if metrics["mean_time"] != float("inf"):
                    metrics["relative_speed"] = metrics["mean_time"] / fastest_time

        # Verify all solutions agree
        results = [m["result"] for m in valid_metrics]
        verified = len({str(r) for r in results}) <= 1 if results else False

        # Find fastest solution
        fastest_solution = ""
        if valid_metrics:
            fastest_metrics = min(valid_metrics, key=lambda m: m["mean_time"])
            fastest_solution = fastest_metrics["name"]

        benchmark_end_time = time.perf_counter()
        total_benchmark_time = benchmark_end_time - benchmark_start_time

        return ProblemBenchmark(
            problem_number=problem_number,
            problem_title=problem_title,
            timestamp=datetime.now().isoformat(),
            config=self.config,
            input_parameters=input_parameters,
            solutions=solution_metrics,
            fastest_solution=fastest_solution,
            verified=verified,
            total_benchmark_time=total_benchmark_time,
        )

    def save_results(self, filepath: Path) -> None:
        """Save benchmark results to JSON file."""
        filepath.parent.mkdir(parents=True, exist_ok=True)

        output_data = {
            "benchmark_suite_version": "1.0",
            "timestamp": datetime.now().isoformat(),
            "config": self.config,
            "problems": self.results,
            "summary": self._generate_summary(),
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

    def load_results(self, filepath: Path) -> None:
        """Load benchmark results from JSON file."""
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)

        self.results = data.get("problems", [])
        if "config" in data:
            self.config.update(data["config"])

    def _generate_summary(self) -> dict[str, Any]:
        """Generate summary statistics for all benchmarked problems."""
        if not self.results:
            return {}

        total_problems = len(self.results)
        verified_problems = sum(1 for r in self.results if r["verified"])

        all_solutions = []
        for problem in self.results:
            all_solutions.extend(problem["solutions"])

        if not all_solutions:
            return {
                "total_problems": total_problems,
                "verified_problems": verified_problems,
            }

        # Algorithm type distribution
        algorithm_types: dict[str, int] = {}
        for solution in all_solutions:
            algo_type = solution["algorithm_type"]
            algorithm_types[algo_type] = algorithm_types.get(algo_type, 0) + 1

        # Performance statistics
        valid_times = [
            s["mean_time"] for s in all_solutions if s["mean_time"] != float("inf")
        ]

        summary: dict[str, Any] = {
            "total_problems": total_problems,
            "verified_problems": verified_problems,
            "verification_rate": verified_problems / total_problems
            if total_problems > 0
            else 0,
            "total_solutions": len(all_solutions),
            "algorithm_distribution": algorithm_types,
        }

        if valid_times:
            summary.update(
                {
                    "performance_stats": {
                        "mean_execution_time": statistics.mean(valid_times),
                        "median_execution_time": statistics.median(valid_times),
                        "fastest_execution_time": min(valid_times),
                        "slowest_execution_time": max(valid_times),
                    }
                }
            )

        return summary


def create_default_benchmark_suite() -> BenchmarkSuite:
    """Create a benchmark suite with default configuration."""
    return BenchmarkSuite()


def benchmark_legacy_compatibility(
    functions: list[tuple[str, Callable[..., Any]]], *args: Any, **kwargs: Any
) -> dict[str, dict[str, Any]]:
    """
    Legacy compatibility function that mimics the original compare_performance.

    Args:
        functions: List of (name, function) tuples
        *args: Arguments to pass to all functions
        **kwargs: Keyword arguments to pass to all functions

    Returns:
        Dictionary with performance results for each function
    """
    return compare_performance(functions, *args, **kwargs)
