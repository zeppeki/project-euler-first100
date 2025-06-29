#!/usr/bin/env python3
"""
Performance visualization utilities for Project Euler benchmarks.

This module provides simple text-based visualizations and reports that don't
require external dependencies like matplotlib.
"""

import json
import statistics
from pathlib import Path
from typing import Any


def create_performance_table(benchmark_data: dict[str, Any]) -> str:
    """Create a formatted table of performance results."""
    problems = benchmark_data.get("problems", [])
    if not problems:
        return "No benchmark data available."

    lines = []
    lines.append("PERFORMANCE COMPARISON TABLE")
    lines.append("=" * 80)
    lines.append(
        f"{'Problem':>8} {'Solution':25} {'Time (μs)':>12} {'Relative':>10} {'Complexity':>12}"
    )
    lines.append("-" * 80)

    for problem in problems:
        problem_num = problem.get("problem_number", "")
        solutions = problem.get("solutions", [])

        for i, solution in enumerate(solutions):
            name = solution.get("name", "")
            mean_time = solution.get("mean_time", 0.0)
            relative_speed = solution.get("relative_speed", 1.0)
            complexity = solution.get("complexity_class", "")

            # Convert to microseconds for better readability
            time_us = mean_time * 1_000_000

            # Show problem number only for first solution
            prob_display = problem_num if i == 0 else ""

            lines.append(
                f"{prob_display:>8} {name:25} {time_us:>12.2f} "
                f"{relative_speed:>10.1f}x {complexity:>12}"
            )

        lines.append("")  # Empty line between problems

    return "\n".join(lines)


def create_algorithm_distribution_chart(benchmark_data: dict[str, Any]) -> str:
    """Create a text-based chart showing algorithm type distribution."""
    summary = benchmark_data.get("summary", {})
    algo_dist = summary.get("algorithm_distribution", {})

    if not algo_dist:
        return "No algorithm distribution data available."

    lines = []
    lines.append("ALGORITHM TYPE DISTRIBUTION")
    lines.append("=" * 40)

    total = sum(algo_dist.values())
    max_count = max(algo_dist.values()) if algo_dist else 1

    for algo_type, count in sorted(algo_dist.items()):
        percentage = (count / total) * 100 if total > 0 else 0

        # Create a simple bar chart using characters
        bar_length = int((count / max_count) * 30) if max_count > 0 else 0
        bar = "█" * bar_length + "░" * (30 - bar_length)

        lines.append(f"{algo_type:12} |{bar}| {count:3d} ({percentage:5.1f}%)")

    lines.append("")
    lines.append(f"Total: {total} solutions")

    return "\n".join(lines)


def create_performance_summary(benchmark_data: dict[str, Any]) -> str:
    """Create a performance summary with key statistics."""
    summary = benchmark_data.get("summary", {})
    perf_stats = summary.get("performance_stats", {})

    if not perf_stats:
        return "No performance statistics available."

    lines = []
    lines.append("PERFORMANCE STATISTICS SUMMARY")
    lines.append("=" * 40)

    mean_time = perf_stats.get("mean_execution_time", 0.0)
    median_time = perf_stats.get("median_execution_time", 0.0)
    fastest_time = perf_stats.get("fastest_execution_time", 0.0)
    slowest_time = perf_stats.get("slowest_execution_time", 0.0)

    lines.append(f"Mean execution time:   {mean_time * 1000:8.3f} ms")
    lines.append(f"Median execution time: {median_time * 1000:8.3f} ms")
    lines.append(f"Fastest solution:      {fastest_time * 1000000:8.2f} μs")
    lines.append(f"Slowest solution:      {slowest_time * 1000:8.3f} ms")

    # Calculate speed ratio
    if fastest_time > 0:
        speed_ratio = slowest_time / fastest_time
        lines.append(f"Speed ratio (max/min): {speed_ratio:8.1f}x")

    lines.append("")

    # Verification statistics
    total_problems = summary.get("total_problems", 0)
    verified_problems = summary.get("verified_problems", 0)
    verification_rate = summary.get("verification_rate", 0.0)

    lines.append(f"Problems benchmarked:  {total_problems:8d}")
    lines.append(f"Solutions verified:    {verified_problems:8d}")
    lines.append(f"Verification rate:     {verification_rate:8.1%}")

    return "\n".join(lines)


def create_top_performers_list(benchmark_data: dict[str, Any], top_n: int = 10) -> str:
    """Create a list of top performing solutions."""
    problems = benchmark_data.get("problems", [])
    if not problems:
        return "No benchmark data available."

    # Collect all solutions with their performance data
    all_solutions = []
    for problem in problems:
        problem_num = problem.get("problem_number", "")
        problem_title = problem.get("problem_title", "")
        solutions = problem.get("solutions", [])

        for solution in solutions:
            name = solution.get("name", "")
            mean_time = solution.get("mean_time", float("inf"))
            complexity = solution.get("complexity_class", "")

            if mean_time != float("inf"):
                all_solutions.append(
                    {
                        "problem": problem_num,
                        "title": problem_title,
                        "solution": name,
                        "time": mean_time,
                        "complexity": complexity,
                    }
                )

    # Sort by execution time
    all_solutions.sort(key=lambda x: x["time"])

    lines = []
    lines.append(f"TOP {top_n} FASTEST SOLUTIONS")
    lines.append("=" * 60)
    lines.append(
        f"{'Rank':>4} {'Problem':>8} {'Solution':20} {'Time':>12} {'Complexity':>10}"
    )
    lines.append("-" * 60)

    for i, solution in enumerate(all_solutions[:top_n], 1):
        time_display = f"{solution['time'] * 1_000_000:.2f} μs"

        lines.append(
            f"{i:>4} {solution['problem']:>8} {solution['solution']:20} "
            f"{time_display:>12} {solution['complexity']:>10}"
        )

    return "\n".join(lines)


def create_complexity_analysis(benchmark_data: dict[str, Any]) -> str:
    """Create an analysis of time complexity performance."""
    problems = benchmark_data.get("problems", [])
    if not problems:
        return "No benchmark data available."

    # Group solutions by complexity class
    complexity_groups: dict[str, list[float]] = {}

    for problem in problems:
        solutions = problem.get("solutions", [])
        for solution in solutions:
            complexity = solution.get("complexity_class", "Unknown")
            mean_time = solution.get("mean_time", float("inf"))

            if mean_time != float("inf"):
                if complexity not in complexity_groups:
                    complexity_groups[complexity] = []
                complexity_groups[complexity].append(mean_time)

    lines = []
    lines.append("TIME COMPLEXITY PERFORMANCE ANALYSIS")
    lines.append("=" * 50)
    lines.append(
        f"{'Complexity':>12} {'Count':>6} {'Mean (ms)':>12} {'Median (ms)':>14} {'Range':>20}"
    )
    lines.append("-" * 50)

    # Sort complexity classes for consistent display
    for complexity in sorted(complexity_groups.keys()):
        times = complexity_groups[complexity]
        count = len(times)
        mean_time = statistics.mean(times) * 1000  # Convert to ms
        median_time = statistics.median(times) * 1000  # Convert to ms
        min_time = min(times) * 1000
        max_time = max(times) * 1000

        range_str = f"{min_time:.2f} - {max_time:.2f}"

        lines.append(
            f"{complexity:>12} {count:>6} {mean_time:>12.3f} "
            f"{median_time:>14.3f} {range_str:>20}"
        )

    return "\n".join(lines)


def generate_comprehensive_report(
    benchmark_file: Path, output_file: Path | None = None
) -> str:
    """Generate a comprehensive performance report."""
    try:
        with open(benchmark_file, encoding="utf-8") as f:
            benchmark_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error loading benchmark data: {e}"

    # Generate all sections
    sections = [
        create_performance_summary(benchmark_data),
        "",
        create_algorithm_distribution_chart(benchmark_data),
        "",
        create_complexity_analysis(benchmark_data),
        "",
        create_top_performers_list(benchmark_data),
        "",
        create_performance_table(benchmark_data),
    ]

    report = "\n".join(sections)

    # Save to file if requested
    if output_file:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report)

    return report


def main() -> None:
    """Main entry point for standalone execution."""
    benchmarks_dir = Path(__file__).parent.parent.parent / "benchmarks"
    latest_file = benchmarks_dir / "aggregated" / "latest.json"

    if not latest_file.exists():
        print("❌ No benchmark results found. Run 'make benchmark' first.")
        return

    # Generate comprehensive report
    output_file = benchmarks_dir / "reports" / "performance_visualization.txt"
    report = generate_comprehensive_report(latest_file, output_file)

    print(report)
    print(f"\n📊 Visualization report saved to: {output_file}")


if __name__ == "__main__":
    main()
