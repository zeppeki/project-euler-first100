#!/usr/bin/env python3
"""
Comprehensive benchmark script for Problem 005: Smallest multiple.

This script implements the staged measurement approach optimized for Problem 005,
with timeout handling, memory tracking, and adaptive measurement strategies.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Add the project root to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from problems.problem_005 import (
    solve_builtin,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.utils.adaptive_benchmark import (
    AdaptiveBenchmarkSuite,
    AdaptiveSolutionMetrics,
    StagedBenchmarkConfig,
)


class Problem005BenchmarkResult:
    """Container for Problem 005 benchmark results."""

    def __init__(self):
        self.problem_number = "005"
        self.problem_title = "Smallest multiple"
        self.timestamp = datetime.now().isoformat()
        self.stages = {"basic": {}, "extended": {}, "scalability": {}}
        self.summary = {}
        self.total_benchmark_time = 0.0

    def to_dict(self) -> dict[str, Any]:
        """Convert benchmark result to dictionary for JSON serialization."""
        return {
            "problem_number": self.problem_number,
            "problem_title": self.problem_title,
            "timestamp": self.timestamp,
            "benchmark_config": {
                "basic_range": [1, 2, 5, 10, 15, 20],
                "extended_range": [25, 30, 35, 40],
                "scalability_range": [50, 100],
                "timeout_seconds": 10.0,
                "max_total_time_minutes": 5.0,
                "early_skip_threshold": 5.0,
            },
            "stages": self.stages,
            "summary": self.summary,
            "total_benchmark_time": self.total_benchmark_time,
        }


def run_stage_benchmark(
    suite: AdaptiveBenchmarkSuite, input_range: list[int], stage_name: str
) -> dict[str, dict[int, list[AdaptiveSolutionMetrics]]]:
    """
    Run benchmark for a specific stage with given input range.

    Args:
        suite: Adaptive benchmark suite instance
        input_range: List of input values to test
        stage_name: Name of the benchmark stage

    Returns:
        Dictionary with algorithm results organized by input value
    """
    # Define all available algorithms
    algorithms = [
        ("素直な解法", solve_naive, "naive", "O(result × n)"),
        ("最適化解法", solve_optimized, "optimized", "O(n × log(max_value))"),
        ("数学的解法", solve_mathematical, "mathematical", "O(n × log(log(n)))"),
        ("標準ライブラリ解法", solve_builtin, "builtin", "O(n × log(max_value))"),
    ]

    stage_results = {}

    print(f"\n=== {stage_name.upper()} STAGE ===")
    print(f"Input range: {input_range}")

    for input_value in input_range:
        print(f"\nTesting n = {input_value}")

        # Track which algorithms to run for this input
        algorithms_to_run = []
        for name, func, alg_type, complexity in algorithms:
            if not suite.should_skip_algorithm(alg_type, [input_value]):
                algorithms_to_run.append((name, func, alg_type, complexity))
            else:
                print(f"  Skipping {name} (too slow for this range)")

        input_results = []

        # Run benchmarks for each algorithm
        for name, func, alg_type, complexity in algorithms_to_run:
            print(f"  Running {name}...", end=" ", flush=True)

            try:
                result = suite.benchmark_solution_adaptive(
                    name=name,
                    func=func,
                    algorithm_type=alg_type,
                    complexity_class=complexity,
                    input_value=input_value,
                )

                if result["timeout_occurred"]:
                    print("TIMEOUT")
                else:
                    print(
                        f"{result['mean_time']:.6f}s ({result['adaptive_runs']} runs)"
                    )

                input_results.append(result)

            except Exception as e:
                print(f"ERROR: {e}")
                continue

        # Calculate relative speeds for this input value
        if input_results:
            input_results = suite.calculate_relative_speeds(input_results)
            stage_results[input_value] = input_results

        # Check total time limit
        if suite.check_total_time_limit():
            print(f"\nReached total time limit, stopping at n = {input_value}")
            break

    return stage_results


def generate_summary(all_results: dict[str, Any]) -> dict[str, Any]:
    """Generate summary statistics from benchmark results."""
    summary = {
        "stages_completed": list(all_results["stages"].keys()),
        "total_input_values_tested": 0,
        "algorithms_tested": set(),
        "timeout_statistics": {},
        "performance_insights": {},
    }

    # Count inputs and algorithms tested
    for _stage_name, stage_data in all_results["stages"].items():
        if stage_data:  # If stage has results
            summary["total_input_values_tested"] += len(stage_data)

            for _input_value, results in stage_data.items():
                for result in results:
                    summary["algorithms_tested"].add(result["algorithm_type"])

    summary["algorithms_tested"] = list(summary["algorithms_tested"])

    # Timeout statistics
    timeout_counts = {}
    total_measurements = 0

    for _stage_name, stage_data in all_results["stages"].items():
        for _input_value, results in stage_data.items():
            for result in results:
                alg_type = result["algorithm_type"]
                total_measurements += 1

                if result["timeout_occurred"]:
                    timeout_counts[alg_type] = timeout_counts.get(alg_type, 0) + 1

    summary["timeout_statistics"] = {
        "total_measurements": total_measurements,
        "timeout_by_algorithm": timeout_counts,
        "timeout_rate": len(timeout_counts) / max(total_measurements, 1),
    }

    # Performance insights - find fastest algorithm for each stage
    fastest_by_stage = {}
    for stage_name, stage_data in all_results["stages"].items():
        if not stage_data:
            continue

        stage_fastest = {}
        for input_value, results in stage_data.items():
            valid_results = [r for r in results if not r["timeout_occurred"]]
            if valid_results:
                fastest = min(valid_results, key=lambda x: x["mean_time"])
                stage_fastest[str(input_value)] = fastest["name"]

        fastest_by_stage[stage_name] = stage_fastest

    summary["performance_insights"]["fastest_by_stage"] = fastest_by_stage

    return summary


def main():
    """Main benchmark execution function."""
    print("Problem 005: Smallest multiple - Comprehensive Benchmark")
    print("=" * 60)

    # Configure adaptive benchmark suite
    config = StagedBenchmarkConfig(
        basic_range=[1, 2, 5, 10, 15, 20],
        extended_range=[25, 30, 35, 40],
        scalability_range=[50, 100],
        timeout_seconds=10.0,
        max_total_time_minutes=5.0,
        early_skip_threshold=5.0,
    )

    suite = AdaptiveBenchmarkSuite(config)
    result_container = Problem005BenchmarkResult()

    start_time = suite.start_time

    try:
        # Stage 1: Basic measurement (all algorithms)
        print("\nStage 1: Basic range - testing all algorithms")
        basic_results = run_stage_benchmark(suite, config["basic_range"], "Basic")
        result_container.stages["basic"] = {
            str(k): [dict(r) for r in v] for k, v in basic_results.items()
        }

        # Stage 2: Extended measurement (efficient algorithms only)
        if not suite.check_total_time_limit():
            print("\nStage 2: Extended range - efficient algorithms only")
            extended_results = run_stage_benchmark(
                suite, config["extended_range"], "Extended"
            )
            result_container.stages["extended"] = {
                str(k): [dict(r) for r in v] for k, v in extended_results.items()
            }

        # Stage 3: Scalability measurement (mathematical algorithm focus)
        if not suite.check_total_time_limit():
            print("\nStage 3: Scalability range - mathematical algorithm focus")
            scalability_results = run_stage_benchmark(
                suite, config["scalability_range"], "Scalability"
            )
            result_container.stages["scalability"] = {
                str(k): [dict(r) for r in v] for k, v in scalability_results.items()
            }

    except KeyboardInterrupt:
        print("\nBenchmark interrupted by user")
    except Exception as e:
        print(f"\nBenchmark failed with error: {e}")
        return 1

    # Calculate total benchmark time
    result_container.total_benchmark_time = suite.start_time - start_time

    # Generate summary
    result_dict = result_container.to_dict()
    result_container.summary = generate_summary(result_dict)

    # Save results to JSON file
    output_path = Path("benchmarks/individual/problem_005.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    final_result = result_container.to_dict()
    final_result["summary"] = result_container.summary

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_result, f, indent=2, ensure_ascii=False)

    print("\n=== BENCHMARK COMPLETED ===")
    print(f"Total time: {result_container.total_benchmark_time:.2f} seconds")
    print(f"Results saved to: {output_path}")
    print(
        f"Stages completed: {', '.join(result_container.summary['stages_completed'])}"
    )
    print(
        f"Total measurements: {result_container.summary['timeout_statistics']['total_measurements']}"
    )
    print(
        f"Algorithms tested: {', '.join(result_container.summary['algorithms_tested'])}"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
