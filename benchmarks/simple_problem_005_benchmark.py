#!/usr/bin/env python3
"""
Simplified benchmark script for Problem 005: Smallest multiple.

This script uses the existing benchmark framework for quick testing.
"""

import json
import sys
import time
from datetime import datetime
from pathlib import Path

# Add the project root to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from problems.problem_005 import (
    solve_builtin,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.utils.benchmark import BenchmarkConfig, BenchmarkSuite


def run_simple_benchmark():
    """Run a simplified benchmark for Problem 005."""
    print("Problem 005: Smallest multiple - Simplified Benchmark")
    print("=" * 60)

    # Configure benchmark suite
    config = BenchmarkConfig(runs=3, warmup_runs=1, min_time=0.001, max_time=10.0)

    suite = BenchmarkSuite(config)

    # Define algorithms to test
    algorithms = [
        ("素直な解法", solve_naive, "naive", "O(result × n)"),
        ("最適化解法", solve_optimized, "optimized", "O(n × log(max_value))"),
        ("数学的解法", solve_mathematical, "mathematical", "O(n × log(log(n)))"),
        ("標準ライブラリ解法", solve_builtin, "builtin", "O(n × log(max_value))"),
    ]

    # Test inputs - start small to avoid timeouts
    test_inputs = [1, 2, 5, 10, 15, 20]

    results = {
        "problem_number": "005",
        "problem_title": "Smallest multiple",
        "timestamp": datetime.now().isoformat(),
        "config": {
            "runs": config["runs"],
            "warmup_runs": config["warmup_runs"],
            "min_time": config["min_time"],
            "max_time": config["max_time"],
        },
        "input_parameters": {"test_inputs": test_inputs},
        "solutions": [],
        "fastest_solution": "",
        "verified": True,
        "total_benchmark_time": 0.0,
    }

    start_time = time.time()

    # Test each input value
    for n in test_inputs:
        print(f"\nTesting n = {n}")

        input_results = []
        all_results_match = True
        expected_result = None

        for name, func, alg_type, complexity in algorithms:
            print(f"  Running {name}...", end=" ", flush=True)

            try:
                # Quick timeout check for naive algorithm on larger inputs
                if alg_type == "naive" and n >= 20:
                    print("SKIPPED (too slow)")
                    continue

                # Run benchmark
                result = suite.benchmark_solution(name, func, alg_type, complexity, n)

                # Store result
                input_results.append(result)

                # Verify correctness
                if expected_result is None:
                    expected_result = result["result"]
                elif expected_result != result["result"]:
                    all_results_match = False

                print(f"{result['mean_time']:.6f}s")

            except Exception as e:
                print(f"ERROR: {e}")
                all_results_match = False
                continue

        # Calculate relative speeds for this input
        if input_results:
            fastest_time = min(r["mean_time"] for r in input_results)
            for result in input_results:
                result["relative_speed"] = result["mean_time"] / fastest_time

        # Store results for this input
        for result in input_results:
            result["input_value"] = n
            results["solutions"].append(result)

        if not all_results_match:
            results["verified"] = False
            print(f"  WARNING: Results don't match for n={n}")

    # Find overall fastest solution
    if results["solutions"]:
        fastest = min(results["solutions"], key=lambda x: x["mean_time"])
        results["fastest_solution"] = fastest["name"]

    results["total_benchmark_time"] = time.time() - start_time

    # Save results
    output_path = Path("benchmarks/individual/problem_005.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n=== BENCHMARK COMPLETED ===")
    print(f"Total time: {results['total_benchmark_time']:.2f} seconds")
    print(f"Results saved to: {output_path}")
    print(f"Fastest solution: {results['fastest_solution']}")
    print(f"Verification: {'PASSED' if results['verified'] else 'FAILED'}")
    print(f"Total measurements: {len(results['solutions'])}")

    return 0


if __name__ == "__main__":
    sys.exit(run_simple_benchmark())
