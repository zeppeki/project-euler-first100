#!/usr/bin/env python3
"""
Generate visualizations for Problem 005 benchmark results.
"""

import json
import sys
from pathlib import Path

# Add the project root to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from problems.utils.benchmark_visualizer import BenchmarkVisualizer


def main():
    """Generate visualizations for Problem 005 benchmark results."""
    print("Generating Problem 005 benchmark visualizations...")

    # Load benchmark results
    benchmark_file = Path("benchmarks/individual/problem_005.json")
    if not benchmark_file.exists():
        print(f"Error: {benchmark_file} not found. Run benchmark first.")
        return 1

    with open(benchmark_file, encoding="utf-8") as f:
        benchmark_data = json.load(f)

    # Create visualizer
    visualizer = BenchmarkVisualizer(benchmark_data)

    # Create output directory
    output_dir = Path("benchmarks/reports/problem_005")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate summary report
    print("Generating summary report...")
    report_path = visualizer.generate_summary_report(output_dir)
    print(f"  Summary report: {report_path}")

    # Generate matplotlib charts (if available)
    print("Generating matplotlib charts...")
    try:
        chart_files = visualizer.create_matplotlib_charts(output_dir)
        for chart_file in chart_files:
            print(f"  Chart: {chart_file}")
        if not chart_files:
            print("  No charts generated (matplotlib might not be available)")
    except Exception as e:
        print(f"  Error generating charts: {e}")

    # Generate interactive charts (if available)
    print("Generating interactive charts...")
    try:
        interactive_files = visualizer.create_interactive_plotly_charts(output_dir)
        for chart_file in interactive_files:
            print(f"  Interactive chart: {chart_file}")
        if not interactive_files:
            print("  No interactive charts generated (plotly might not be available)")
    except Exception as e:
        print(f"  Error generating interactive charts: {e}")

    print("\nVisualization generation completed!")
    print(f"Results saved to: {output_dir}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
