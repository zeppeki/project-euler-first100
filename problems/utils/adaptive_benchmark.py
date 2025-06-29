#!/usr/bin/env python3
"""
Adaptive benchmark framework for Problem 005 with timeout and staged measurement.

This module provides specialized benchmarking capabilities for Problem 005,
featuring adaptive measurement strategies, timeout handling, and memory usage tracking.
"""

import signal
import statistics
import time
import tracemalloc
from collections.abc import Callable
from contextlib import contextmanager
from typing import Any, TypedDict

from .benchmark import BenchmarkConfig


class TimeoutError(Exception):
    """Raised when function execution exceeds timeout limit."""


class MemoryMetrics(TypedDict):
    """Memory usage metrics for a solution."""

    peak_memory_mb: float
    current_memory_mb: float
    memory_blocks: int


class AdaptiveSolutionMetrics(TypedDict):
    """Extended solution metrics with timeout and memory information."""

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
    timeout_occurred: bool
    memory_metrics: MemoryMetrics | None
    adaptive_runs: int  # actual number of runs performed


class StagedBenchmarkConfig(TypedDict):
    """Configuration for staged benchmark execution."""

    basic_range: list[int]  # Full measurement range
    extended_range: list[int]  # Efficient algorithms only
    scalability_range: list[int]  # Mathematical algorithm only
    timeout_seconds: float
    max_total_time_minutes: float
    early_skip_threshold: float  # Skip if single run exceeds this time


@contextmanager
def timeout_handler(timeout_seconds: float) -> Any:
    """Context manager for function timeout handling."""

    def timeout_signal_handler(_signum: Any, _frame: Any) -> None:
        raise TimeoutError(f"Function exceeded {timeout_seconds} seconds")

    old_handler = signal.signal(signal.SIGALRM, timeout_signal_handler)
    signal.alarm(int(timeout_seconds))
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)


class AdaptiveBenchmarkSuite:
    """
    Adaptive benchmarking suite for Problem 005 with intelligent measurement strategies.

    Features:
    - Timeout handling for long-running algorithms
    - Memory usage tracking
    - Staged measurement (basic -> extended -> scalability)
    - Early termination for inefficient algorithms
    """

    def __init__(self, config: StagedBenchmarkConfig):
        """Initialize adaptive benchmark suite."""
        self.config = config
        self.base_config = BenchmarkConfig(
            runs=5, warmup_runs=2, min_time=0.001, max_time=config["timeout_seconds"]
        )
        self.start_time = time.time()

    def check_total_time_limit(self) -> bool:
        """Check if total benchmark time limit has been exceeded."""
        elapsed_minutes = (time.time() - self.start_time) / 60
        return elapsed_minutes >= self.config["max_total_time_minutes"]

    def _measure_memory_usage(
        self, func: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> tuple[Any, MemoryMetrics]:
        """Measure memory usage during function execution."""
        tracemalloc.start()

        try:
            result = func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()

            # Get current memory snapshot
            snapshot = tracemalloc.take_snapshot()
            memory_blocks = len(snapshot.statistics("lineno"))

            memory_metrics: MemoryMetrics = {
                "peak_memory_mb": peak / 1024 / 1024,
                "current_memory_mb": current / 1024 / 1024,
                "memory_blocks": memory_blocks,
            }

            return result, memory_metrics
        finally:
            tracemalloc.stop()

    def benchmark_solution_adaptive(
        self,
        name: str,
        func: Callable[..., Any],
        algorithm_type: str,
        complexity_class: str,
        input_value: int,
        *args: Any,
        **kwargs: Any,
    ) -> AdaptiveSolutionMetrics:
        """
        Benchmark a single solution with adaptive measurement and timeout handling.

        Args:
            name: Human-readable name for the solution
            func: Function to benchmark
            algorithm_type: Type of algorithm (naive, optimized, mathematical, builtin)
            complexity_class: Big O notation for time complexity
            input_value: The n value being tested
            *args: Additional arguments to pass to the function
            **kwargs: Additional keyword arguments to pass to the function

        Returns:
            Detailed performance metrics with timeout and memory information
        """
        timeout_occurred = False
        memory_metrics = None
        execution_times = []
        result = None
        actual_runs = 0

        # Warmup run with memory measurement
        try:
            with timeout_handler(self.config["timeout_seconds"]):
                result, memory_metrics = self._measure_memory_usage(
                    func, input_value, *args, **kwargs
                )
        except TimeoutError:
            timeout_occurred = True
        except Exception:
            timeout_occurred = True

        if timeout_occurred:
            return {
                "name": name,
                "function_name": func.__name__,
                "algorithm_type": algorithm_type,
                "result": None,
                "execution_times": [],
                "mean_time": float("inf"),
                "median_time": float("inf"),
                "std_deviation": 0.0,
                "min_time": float("inf"),
                "max_time": float("inf"),
                "relative_speed": float("inf"),
                "complexity_class": complexity_class,
                "timeout_occurred": True,
                "memory_metrics": None,
                "adaptive_runs": 0,
            }

        # Adaptive number of runs based on execution time
        target_runs = self.base_config["runs"]

        # Single run timing test to determine if we should proceed
        start_time = time.time()
        try:
            with timeout_handler(self.config["timeout_seconds"]):
                test_result = func(input_value, *args, **kwargs)
                single_run_time = time.time() - start_time

                # Early skip if single run is too slow
                if single_run_time > self.config["early_skip_threshold"]:
                    return {
                        "name": name,
                        "function_name": func.__name__,
                        "algorithm_type": algorithm_type,
                        "result": test_result,
                        "execution_times": [single_run_time],
                        "mean_time": single_run_time,
                        "median_time": single_run_time,
                        "std_deviation": 0.0,
                        "min_time": single_run_time,
                        "max_time": single_run_time,
                        "relative_speed": 1.0,
                        "complexity_class": complexity_class,
                        "timeout_occurred": False,
                        "memory_metrics": memory_metrics,
                        "adaptive_runs": 1,
                    }

                # Adjust number of runs based on execution time
                if single_run_time > 1.0:  # If single run takes more than 1 second
                    target_runs = 2
                elif single_run_time > 0.1:  # If single run takes more than 100ms
                    target_runs = 3
                else:
                    target_runs = self.base_config["runs"]

        except TimeoutError:
            timeout_occurred = True
        except Exception:
            timeout_occurred = True

        if timeout_occurred:
            return {
                "name": name,
                "function_name": func.__name__,
                "algorithm_type": algorithm_type,
                "result": result,
                "execution_times": [],
                "mean_time": float("inf"),
                "median_time": float("inf"),
                "std_deviation": 0.0,
                "min_time": float("inf"),
                "max_time": float("inf"),
                "relative_speed": float("inf"),
                "complexity_class": complexity_class,
                "timeout_occurred": True,
                "memory_metrics": memory_metrics,
                "adaptive_runs": 0,
            }

        # Perform measured runs
        for _run in range(target_runs):
            if self.check_total_time_limit():
                break

            try:
                with timeout_handler(self.config["timeout_seconds"]):
                    start_time = time.time()
                    test_result = func(input_value, *args, **kwargs)
                    end_time = time.time()

                    execution_times.append(end_time - start_time)
                    result = test_result
                    actual_runs += 1

            except TimeoutError:
                timeout_occurred = True
                break
            except Exception:
                timeout_occurred = True
                break

        # Calculate statistics
        if execution_times:
            mean_time = statistics.mean(execution_times)
            median_time = statistics.median(execution_times)
            std_dev = (
                statistics.stdev(execution_times) if len(execution_times) > 1 else 0.0
            )
            min_time = min(execution_times)
            max_time = max(execution_times)
        else:
            mean_time = median_time = min_time = max_time = float("inf")
            std_dev = 0.0

        return {
            "name": name,
            "function_name": func.__name__,
            "algorithm_type": algorithm_type,
            "result": result,
            "execution_times": execution_times,
            "mean_time": mean_time,
            "median_time": median_time,
            "std_deviation": std_dev,
            "min_time": min_time,
            "max_time": max_time,
            "relative_speed": 1.0,  # Will be calculated later
            "complexity_class": complexity_class,
            "timeout_occurred": timeout_occurred,
            "memory_metrics": memory_metrics,
            "adaptive_runs": actual_runs,
        }

    def should_skip_algorithm(
        self, algorithm_type: str, input_range: list[int]
    ) -> bool:
        """
        Determine if an algorithm should be skipped for a given input range.

        Args:
            algorithm_type: Type of algorithm (naive, optimized, mathematical, builtin)
            input_range: List of input values to be tested

        Returns:
            True if algorithm should be skipped for this range
        """
        max_input = max(input_range)

        # Skip naive algorithm for extended and scalability ranges
        if algorithm_type == "naive" and max_input >= 25:  # Extended range starts at 25
            return True

        # Skip non-mathematical algorithms for scalability range
        return (
            algorithm_type in ["naive", "optimized", "builtin"] and max_input >= 50
        )  # Scalability range starts at 50

    def calculate_relative_speeds(
        self, metrics_list: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """Calculate relative speeds with timeout handling."""
        # Find the fastest valid time (excluding timeouts and infs)
        valid_times = [
            m["mean_time"]
            for m in metrics_list
            if not m["timeout_occurred"] and m["mean_time"] != float("inf")
        ]

        if not valid_times:
            return metrics_list

        fastest_time = min(valid_times)

        # Update relative speeds
        updated_metrics = []
        for metrics in metrics_list:
            if metrics["timeout_occurred"] or metrics["mean_time"] == float("inf"):
                relative_speed = float("inf")
            else:
                relative_speed = metrics["mean_time"] / fastest_time

            # Create updated metrics with proper relative speed
            updated = dict(metrics)
            updated["relative_speed"] = relative_speed
            updated_metrics.append(updated)

        return updated_metrics
