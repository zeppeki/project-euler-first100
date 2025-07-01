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
    lines.append(f"{'Problem':>8} {'Solution':25} {'Time (μs)':>12} {'Relative':>10}")
    lines.append("-" * 80)

    for problem in problems:
        problem_num = problem.get("problem_number", "")
        solutions = problem.get("solutions", [])

        for i, solution in enumerate(solutions):
            name = solution.get("name", "")
            mean_time = solution.get("mean_time", 0.0)
            relative_speed = solution.get("relative_speed", 1.0)

            # Convert to microseconds for better readability
            time_us = mean_time * 1_000_000

            # Show problem number only for first solution
            prob_display = problem_num if i == 0 else ""

            lines.append(
                f"{prob_display:>8} {name:25} {time_us:>12.2f} {relative_speed:>10.1f}x"
            )

        lines.append("")  # Empty line between problems

    return "\n".join(lines)


def create_solution_type_performance(benchmark_data: dict[str, Any]) -> str:
    """Create solution type performance analysis based on execution time."""
    summary = benchmark_data.get("summary", {})
    algo_dist = summary.get("algorithm_distribution", {})
    algo_times = summary.get("algorithm_avg_times", {})

    if not algo_dist:
        return "No algorithm distribution data available."

    lines = []
    lines.append("SOLUTION TYPE PERFORMANCE")
    lines.append("=" * 50)

    total = sum(algo_dist.values())

    # Sort by average execution time (fastest first)
    sorted_algos = sorted(algo_times.items(), key=lambda x: x[1])

    for algo_type, avg_time in sorted_algos:
        count = algo_dist.get(algo_type, 0)

        # Create performance indicator based on execution time
        if avg_time < 0.001:  # < 1ms
            perf_indicator = "⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡"
        elif avg_time < 0.01:  # < 10ms
            perf_indicator = "⚡⚡⚡⚡⚡⚡⚡⚡"
        elif avg_time < 0.1:  # < 100ms
            perf_indicator = "⚡⚡⚡⚡⚡⚡"
        elif avg_time < 1.0:  # < 1s
            perf_indicator = "⚡⚡⚡"
        else:
            perf_indicator = "⚡⚡"

        # Format time display
        if avg_time < 0.001:
            time_display = f"{avg_time * 1000:.2f}μs"
        elif avg_time < 1.0:
            time_display = f"{avg_time * 1000:.0f}ms"
        else:
            time_display = f"{avg_time:.1f}s"

        # Add note for learning purpose solutions
        note = " (学習基準実装)" if algo_type == "naive" else ""

        lines.append(
            f"{algo_type.capitalize():12}: {count:2d}解法 - 平均: {time_display:>8} {perf_indicator}{note}"
        )

    lines.append("")
    lines.append(f"Total: {total} solutions")

    return "\n".join(lines)


def create_performance_summary(benchmark_data: dict[str, Any]) -> str:
    """Create a visual performance dashboard summary."""
    summary = benchmark_data.get("summary", {})
    perf_stats = summary.get("performance_stats", {})

    total_problems = summary.get("total_problems", 0)
    verification_rate = summary.get("verification_rate", 0.0)
    total_solutions = sum(summary.get("algorithm_distribution", {}).values())

    lines = []
    lines.append("PROJECT EULER BENCHMARK DASHBOARD")
    lines.append("=" * 50)

    # Progress bar for problems completed
    if total_problems > 0:
        progress_pct = total_problems / 100 * 100  # Assuming target of 100 problems
        progress_filled = int(progress_pct / 100 * 28)
        progress_bar = "█" * progress_filled + "░" * (28 - progress_filled)
        lines.append(
            f"🎯 進捗: {progress_bar} {total_problems}/100 ({progress_pct:.0f}%)"
        )

    lines.append(
        f"⚡ 解法: {total_solutions}個（平均{total_solutions / total_problems:.1f}解法/問題）"
    )
    lines.append(f"✅ 検証: {verification_rate:.0%} 成功")

    if perf_stats:
        mean_time = perf_stats.get("mean_execution_time", 0.0)
        fastest_time = perf_stats.get("fastest_execution_time", 0.0)
        slowest_time = perf_stats.get("slowest_execution_time", 0.0)

        # Format time displays
        if mean_time < 0.001:
            mean_display = f"{mean_time * 1000000:.0f}μs"
        elif mean_time < 1.0:
            mean_display = f"{mean_time * 1000:.0f}ms"
        else:
            mean_display = f"{mean_time:.1f}s"

        if fastest_time < 0.001:
            fastest_display = f"{fastest_time * 1000000:.1f}μs"
        elif fastest_time < 1.0:
            fastest_display = f"{fastest_time * 1000:.1f}ms"
        else:
            fastest_display = f"{fastest_time:.1f}s"

        if slowest_time < 0.001:
            slowest_display = f"{slowest_time * 1000000:.0f}μs"
        elif slowest_time < 1.0:
            slowest_display = f"{slowest_time * 1000:.0f}ms"
        else:
            slowest_display = f"{slowest_time:.1f}s"

        lines.append(f"⏱️  平均: {mean_display}（最速解法ベース）")
        lines.append(f"🏃 最速: {fastest_display} | 最遅: {slowest_display}")

        # Calculate and display speed ratio
        if fastest_time > 0:
            speed_ratio = slowest_time / fastest_time
            if speed_ratio > 1000000:
                ratio_display = f"{speed_ratio / 1000000:.1f}M倍"
            elif speed_ratio > 1000:
                ratio_display = f"{speed_ratio / 1000:.0f}K倍"
            else:
                ratio_display = f"{speed_ratio:.0f}倍"
            lines.append(f"📊 速度比: {ratio_display}")

        # One-minute rule compliance (assuming > 60s is violation)
        problems = benchmark_data.get("problems", [])
        violation_count = 0
        total_solution_count = 0

        for problem in problems:
            solutions = problem.get("solutions", [])
            for solution in solutions:
                total_solution_count += 1
                if solution.get("mean_time", 0) > 60:
                    violation_count += 1

        if total_solution_count > 0:
            compliance_rate = (
                total_solution_count - violation_count
            ) / total_solution_count
            lines.append(f"💯 One-minute rule: {compliance_rate:.1%} 遵守")

    return "\n".join(lines)


def create_fastest_solutions_by_problem(
    benchmark_data: dict[str, Any], top_n: int = 10
) -> str:
    """Create a list of fastest solutions (one per problem only)."""
    problems = benchmark_data.get("problems", [])
    if not problems:
        return "No benchmark data available."

    # Get fastest solution for each problem
    fastest_solutions = []
    for problem in problems:
        problem_num = problem.get("problem_number", "")
        problem_title = problem.get("problem_title", "")
        solutions = problem.get("solutions", [])

        if solutions:
            # Find fastest solution for this problem
            fastest = min(solutions, key=lambda s: s.get("mean_time", float("inf")))
            mean_time = fastest.get("mean_time", float("inf"))

            if mean_time != float("inf"):
                fastest_solutions.append(
                    {
                        "problem": problem_num,
                        "title": problem_title,
                        "solution": fastest.get("name", ""),
                        "time": mean_time,
                    }
                )

    # Sort by execution time
    fastest_solutions.sort(key=lambda x: x["time"])

    lines = []
    lines.append("🏆 FASTEST SOLUTIONS (各問題の最速解法のみ)")
    lines.append("=" * 60)
    lines.append(f"{'Rank':>4} {'Problem':>8} {'Solution':25} {'Time':>12}")
    lines.append("-" * 60)

    for i, solution in enumerate(fastest_solutions[:top_n], 1):
        if solution["time"] < 0.001:
            time_display = f"{solution['time'] * 1_000_000:.2f}μs"
        elif solution["time"] < 1.0:
            time_display = f"{solution['time'] * 1000:.2f}ms"
        else:
            time_display = f"{solution['time']:.2f}s"

        # Visual bar for relative performance
        bar = "█" * 32

        lines.append(
            f"{i:>4} P{solution['problem']:>3} {solution['solution']:25} ⚡ {time_display:>8} [{bar}]"
        )

    return "\n".join(lines)


def create_computationally_intensive_problems(
    benchmark_data: dict[str, Any], top_n: int = 5
) -> str:
    """Create a list of computationally intensive problems (even fastest solutions are slow)."""
    problems = benchmark_data.get("problems", [])
    if not problems:
        return "No benchmark data available."

    # Get fastest solution for each problem
    problem_times = []
    for problem in problems:
        problem_num = problem.get("problem_number", "")
        solutions = problem.get("solutions", [])

        if solutions:
            # Find fastest solution for this problem
            fastest_time = min(s.get("mean_time", float("inf")) for s in solutions)
            fastest_solution = min(
                solutions, key=lambda s: s.get("mean_time", float("inf"))
            )

            if fastest_time != float("inf"):
                problem_times.append(
                    {
                        "problem": problem_num,
                        "fastest_time": fastest_time,
                        "fastest_solution": fastest_solution.get("name", ""),
                    }
                )

    # Sort by fastest time (slowest first)
    problem_times.sort(key=lambda x: x["fastest_time"], reverse=True)

    lines = []
    lines.append("🔥 COMPUTATIONALLY INTENSIVE (各問題の最速解法でも重い)")
    lines.append("=" * 60)
    lines.append(f"{'Rank':>4} {'Problem':>8} {'Solution':25} {'Time':>12}")
    lines.append("-" * 60)

    for i, item in enumerate(problem_times[:top_n], 1):
        if item["fastest_time"] < 0.001:
            time_display = f"{item['fastest_time'] * 1_000_000:.1f}μs"
        elif item["fastest_time"] < 1.0:
            time_display = f"{item['fastest_time'] * 1000:.1f}ms"
        else:
            time_display = f"{item['fastest_time']:.1f}s"

        lines.append(
            f"{i:>4} P{item['problem']:>3} {item['fastest_solution']:25} ⏳ {time_display:>8} [最速でもこの時間]"
        )

    return "\n".join(lines)


def create_execution_time_distribution(benchmark_data: dict[str, Any]) -> str:
    """Create execution time distribution analysis."""
    problems = benchmark_data.get("problems", [])
    if not problems:
        return "No benchmark data available."

    # Collect all execution times
    all_times = []
    for problem in problems:
        solutions = problem.get("solutions", [])
        for solution in solutions:
            mean_time = solution.get("mean_time", 0.0)
            if mean_time > 0:
                all_times.append(mean_time)

    if not all_times:
        return "No execution time data available."

    lines = []
    lines.append("EXECUTION TIME DISTRIBUTION (全解法)")
    lines.append("=" * 50)

    total_solutions = len(all_times)

    # Define time buckets
    buckets = [
        ("< 1ms", lambda t: t < 0.001),
        ("1-10ms", lambda t: 0.001 <= t < 0.01),
        ("10-100ms", lambda t: 0.01 <= t < 0.1),
        ("100ms-1s", lambda t: 0.1 <= t < 1.0),
        ("> 1s", lambda t: t >= 1.0),
    ]

    max_count = 0
    bucket_counts = []

    for bucket_name, condition in buckets:
        count = sum(1 for t in all_times if condition(t))
        bucket_counts.append((bucket_name, count))
        max_count = max(max_count, count)

    for bucket_name, count in bucket_counts:
        percentage = (count / total_solutions) * 100 if total_solutions > 0 else 0

        # Create visual bar
        bar_length = int((count / max_count) * 32) if max_count > 0 else 0
        bar = "█" * bar_length + "░" * (32 - bar_length)

        lines.append(f"{bucket_name:9} {bar} {count:2d}解法 ({percentage:4.1f}%)")

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
        create_solution_type_performance(benchmark_data),
        "",
        create_execution_time_distribution(benchmark_data),
        "",
        create_fastest_solutions_by_problem(benchmark_data),
        "",
        create_computationally_intensive_problems(benchmark_data),
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


def convert_simple_benchmark_to_standard_format(
    simple_data: dict[str, Any],
) -> dict[str, Any]:
    """Convert simple benchmark format to standard visualization format."""
    converted_data: dict[str, Any] = {
        "problems": [],
        "summary": {
            "total_problems": 0,
            "verified_problems": 0,
            "verification_rate": 0.0,
            "algorithm_distribution": {},
            "algorithm_avg_times": {},
            "performance_stats": {},
        },
    }

    all_times: list[float] = []
    algorithm_counts: dict[str, int] = {}
    algorithm_times: dict[str, list[float]] = {}

    for problem_data in simple_data.values():
        if isinstance(problem_data, dict) and "solutions" in problem_data:
            converted_data["summary"]["total_problems"] += 1
            if problem_data.get("verified", False):
                converted_data["summary"]["verified_problems"] += 1

            problem_entry = {
                "problem_number": problem_data["problem_number"],
                "problem_title": problem_data["problem_title"],
                "solutions": [],
            }

            for solution in problem_data["solutions"]:
                exec_time = solution.get("execution_time", 0)
                if exec_time > 0:
                    all_times.append(exec_time)

                algo_type = solution.get("algorithm_type", "unknown")
                algorithm_counts[algo_type] = algorithm_counts.get(algo_type, 0) + 1

                if algo_type not in algorithm_times:
                    algorithm_times[algo_type] = []
                algorithm_times[algo_type].append(exec_time)

                problem_entry["solutions"].append(
                    {
                        "name": solution["name"],
                        "mean_time": exec_time,
                        "relative_speed": solution.get("relative_speed", 1.0),
                        "algorithm_type": algo_type,
                    }
                )

            converted_data["problems"].append(problem_entry)

    # Calculate statistics
    if all_times:
        converted_data["summary"]["performance_stats"] = {
            "mean_execution_time": statistics.mean(all_times),
            "median_execution_time": statistics.median(all_times),
            "fastest_execution_time": min(all_times),
            "slowest_execution_time": max(all_times),
        }

    converted_data["summary"]["algorithm_distribution"] = algorithm_counts

    # Calculate average times per algorithm type
    for algo_type, times in algorithm_times.items():
        converted_data["summary"]["algorithm_avg_times"][algo_type] = statistics.mean(
            times
        )

    if converted_data["summary"]["total_problems"] > 0:
        converted_data["summary"]["verification_rate"] = (
            converted_data["summary"]["verified_problems"]
            / converted_data["summary"]["total_problems"]
        )

    return converted_data


def main() -> None:
    """Main entry point for standalone execution."""
    benchmarks_dir = Path(__file__).parent.parent.parent / "benchmarks"

    # Try different benchmark result files
    possible_files = [
        benchmarks_dir / "aggregated" / "latest.json",
        # Find the most recent simple benchmark file
    ]

    # Find most recent simple benchmark file
    results_dir = benchmarks_dir / "results"
    if results_dir.exists():
        simple_files = list(results_dir.glob("simple_benchmark_*.json"))
        if simple_files:
            # Sort by modification time, get the most recent
            latest_simple = max(simple_files, key=lambda f: f.stat().st_mtime)
            possible_files.insert(0, latest_simple)

    benchmark_file = None
    for file_path in possible_files:
        if file_path.exists():
            benchmark_file = file_path
            break

    if not benchmark_file:
        print("❌ No benchmark results found. Run 'make benchmark-simple' first.")
        return

    print(f"📊 Using benchmark data from: {benchmark_file}")

    # Load and potentially convert data
    with open(benchmark_file, encoding="utf-8") as f:
        raw_data = json.load(f)

    # Check if this is simple benchmark format (needs conversion)
    if any(
        isinstance(v, dict) and "solutions" in v
        for v in raw_data.values()
        if isinstance(v, dict)
    ):
        print("🔄 Converting simple benchmark format...")
        benchmark_data = convert_simple_benchmark_to_standard_format(raw_data)
    else:
        benchmark_data = raw_data

    # Generate comprehensive report
    output_file = benchmarks_dir / "reports" / "performance_visualization.txt"
    report = generate_comprehensive_report_from_data(benchmark_data, output_file)

    print(report)
    print(f"\n📊 Visualization report saved to: {output_file}")


def generate_comprehensive_report_from_data(
    benchmark_data: dict[str, Any], output_file: Path | None = None
) -> str:
    """Generate a comprehensive performance report from already loaded data."""
    # Generate all sections
    sections = [
        create_performance_summary(benchmark_data),
        "",
        create_solution_type_performance(benchmark_data),
        "",
        create_execution_time_distribution(benchmark_data),
        "",
        create_fastest_solutions_by_problem(benchmark_data),
        "",
        create_computationally_intensive_problems(benchmark_data),
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


if __name__ == "__main__":
    main()
