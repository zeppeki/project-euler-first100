#!/usr/bin/env python3
"""
Generate dashboard performance data from benchmark results.

This script extracts real benchmark data and converts it to a format
suitable for the dashboard.js performance chart.
"""

import json
from pathlib import Path
from typing import Any


def load_latest_benchmark() -> dict[str, Any]:
    """Load the most recent comprehensive benchmark result."""
    benchmarks_dir = Path("benchmarks/results")
    if not benchmarks_dir.exists():
        return {}

    # Find the latest comprehensive benchmark file
    benchmark_files = list(benchmarks_dir.glob("comprehensive_benchmark_*.json"))
    if not benchmark_files:
        return {}

    # Sort by modification time and get the latest
    latest_file = max(benchmark_files, key=lambda f: f.stat().st_mtime)

    with open(latest_file, encoding="utf-8") as f:
        return json.load(f)


def extract_performance_data(benchmark_data: dict[str, Any]) -> dict[str, Any]:
    """Extract and organize performance data for dashboard chart."""
    if not benchmark_data or "problems" not in benchmark_data:
        return {}

    problems = benchmark_data["problems"]

    # Initialize data structures
    problem_numbers = []
    naive_times = []
    optimized_times = []
    mathematical_times = []

    # Process each problem
    for problem_num in sorted(problems.keys()):
        problem_data = problems[problem_num]

        if problem_data["status"] != "success":
            continue

        problem_numbers.append(problem_num)

        # Extract solution times
        solutions = problem_data["solutions"]
        naive_time = None
        optimized_time = None
        mathematical_time = None

        for solution in solutions:
            if solution["status"] != "success":
                continue

            name = solution["name"]
            time = solution["time"]

            if "素直な解法" in name or "Naive" in name:
                naive_time = time
            elif "最適化解法" in name or "Optimized" in name:
                optimized_time = time
            elif "数学的解法" in name or "Mathematical" in name:
                mathematical_time = time

        # Convert to milliseconds for better readability
        naive_times.append(naive_time * 1000 if naive_time is not None else None)
        optimized_times.append(
            optimized_time * 1000 if optimized_time is not None else None
        )
        mathematical_times.append(
            mathematical_time * 1000 if mathematical_time is not None else None
        )

    return {
        "problems": problem_numbers,
        "naive": naive_times,
        "optimized": optimized_times,
        "mathematical": mathematical_times,
        "metadata": {
            "unit": "milliseconds",
            "generated_from": benchmark_data.get("benchmark_info", {}).get(
                "timestamp", "unknown"
            ),
            "total_problems": len(problem_numbers),
        },
    }


def calculate_relative_speeds(performance_data: dict[str, Any]) -> dict[str, Any]:
    """Calculate relative speeds based on fastest solution per problem."""
    if not performance_data:
        return {}

    problems = performance_data["problems"]
    naive = performance_data["naive"]
    optimized = performance_data["optimized"]
    mathematical = performance_data["mathematical"]

    relative_naive = []
    relative_optimized = []
    relative_mathematical = []

    for i in range(len(problems)):
        times = []
        if naive[i] is not None:
            times.append(naive[i])
        if optimized[i] is not None:
            times.append(optimized[i])
        if mathematical[i] is not None:
            times.append(mathematical[i])

        if not times:
            relative_naive.append(None)
            relative_optimized.append(None)
            relative_mathematical.append(None)
            continue

        fastest_time = min(times)

        relative_naive.append(naive[i] / fastest_time if naive[i] is not None else None)
        relative_optimized.append(
            optimized[i] / fastest_time if optimized[i] is not None else None
        )
        relative_mathematical.append(
            mathematical[i] / fastest_time if mathematical[i] is not None else None
        )

    return {
        "problems": problems,
        "naive": relative_naive,
        "optimized": relative_optimized,
        "mathematical": relative_mathematical,
        "metadata": {
            "unit": "relative_speed",
            "description": "Speed relative to fastest solution (1.0 = fastest)",
            "generated_from": performance_data["metadata"]["generated_from"],
            "total_problems": len(problems),
        },
    }


def generate_dashboard_data() -> str:
    """Generate JavaScript data for dashboard.js."""
    benchmark_data = load_latest_benchmark()

    if not benchmark_data:
        return """
// No benchmark data available
const performanceData = {
  problems: [],
  times: { naive: [], optimized: [], mathematical: [] },
  relative: { naive: [], optimized: [], mathematical: [] },
  metadata: { error: 'No benchmark data found' }
};
"""

    performance_data = extract_performance_data(benchmark_data)
    relative_data = calculate_relative_speeds(performance_data)

    if not performance_data:
        return """
// Invalid benchmark data
const performanceData = {
  problems: [],
  times: { naive: [], optimized: [], mathematical: [] },
  relative: { naive: [], optimized: [], mathematical: [] },
  metadata: { error: 'Invalid benchmark data' }
};
"""

    # Generate JavaScript code
    return f"""
// Generated performance data from real benchmarks
// Generated on: {performance_data["metadata"]["generated_from"]}
// Total problems: {performance_data["metadata"]["total_problems"]}

const performanceData = {{
  problems: {json.dumps(performance_data["problems"])},

  // Execution times in milliseconds
  times: {{
    naive: {json.dumps(performance_data["naive"])},
    optimized: {json.dumps(performance_data["optimized"])},
    mathematical: {json.dumps(performance_data["mathematical"])}
  }},

  // Relative speeds (fastest = 1.0)
  relative: {{
    naive: {json.dumps(relative_data["naive"])},
    optimized: {json.dumps(relative_data["optimized"])},
    mathematical: {json.dumps(relative_data["mathematical"])}
  }},

  metadata: {{
    unit_times: 'milliseconds',
    unit_relative: 'relative_speed',
    generated_from: '{performance_data["metadata"]["generated_from"]}',
    total_problems: {performance_data["metadata"]["total_problems"]}
  }}
}};
"""


def main() -> None:
    """Main function to generate and save dashboard data."""
    js_data = generate_dashboard_data()

    # Save to docs/js directory
    output_file = Path("docs/js/performance_data.js")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(js_data)

    print(f"Dashboard performance data generated: {output_file}")

    # Also print to stdout for verification
    print("\nGenerated data preview:")
    print(js_data[:500] + "..." if len(js_data) > 500 else js_data)


if __name__ == "__main__":
    main()
