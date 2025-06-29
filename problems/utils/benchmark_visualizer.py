#!/usr/bin/env python3
"""
Visualization utilities for benchmark results.

This module provides comprehensive visualization capabilities for Problem 005
benchmark results, including performance comparison charts, scalability analysis,
and memory usage visualization.
"""

import math
from pathlib import Path
from typing import Any

try:
    import matplotlib.pyplot as plt

    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

try:
    import plotly.graph_objects as go
    import plotly.offline as pyo
    from plotly.subplots import make_subplots

    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False


class BenchmarkVisualizer:
    """Comprehensive visualization suite for benchmark results."""

    def __init__(self, benchmark_data: dict[str, Any]):
        """Initialize visualizer with benchmark data."""
        self.data = benchmark_data
        self.problem_number = benchmark_data.get("problem_number", "005")
        self.problem_title = benchmark_data.get("problem_title", "Smallest multiple")

    def extract_performance_data(self) -> dict[str, Any]:
        """Extract and organize performance data for visualization."""
        performance_data: dict[str, Any] = {
            "algorithms": set(),
            "input_values": [],
            "execution_times": {},
            "memory_usage": {},
            "timeout_status": {},
            "relative_speeds": {},
            "stages": list(self.data.get("stages", {}).keys()),
        }

        # Process each stage
        for _stage_name, stage_data in self.data.get("stages", {}).items():
            for input_str, results in stage_data.items():
                input_value = int(input_str)
                if input_value not in performance_data["input_values"]:
                    performance_data["input_values"].append(input_value)

                for result in results:
                    alg_name = result["name"]
                    performance_data["algorithms"].add(alg_name)

                    # Initialize data structures
                    if alg_name not in performance_data["execution_times"]:
                        performance_data["execution_times"][alg_name] = {}
                        performance_data["memory_usage"][alg_name] = {}
                        performance_data["timeout_status"][alg_name] = {}
                        performance_data["relative_speeds"][alg_name] = {}

                    # Store performance metrics
                    if result["timeout_occurred"]:
                        performance_data["execution_times"][alg_name][input_value] = (
                            None
                        )
                        performance_data["timeout_status"][alg_name][input_value] = True
                        performance_data["relative_speeds"][alg_name][input_value] = (
                            float("inf")
                        )
                    else:
                        performance_data["execution_times"][alg_name][input_value] = (
                            result["mean_time"]
                        )
                        performance_data["timeout_status"][alg_name][input_value] = (
                            False
                        )
                        performance_data["relative_speeds"][alg_name][input_value] = (
                            result["relative_speed"]
                        )

                    # Store memory usage if available
                    if result.get("memory_metrics"):
                        memory_metrics = result["memory_metrics"]
                        performance_data["memory_usage"][alg_name][input_value] = {
                            "peak_mb": memory_metrics["peak_memory_mb"],
                            "current_mb": memory_metrics["current_memory_mb"],
                        }

        performance_data["algorithms"] = sorted(performance_data["algorithms"])
        performance_data["input_values"] = sorted(performance_data["input_values"])

        return performance_data

    def create_matplotlib_charts(self, output_dir: Path) -> list[Path]:
        """Create comprehensive charts using matplotlib."""
        if not MATPLOTLIB_AVAILABLE:
            print("Matplotlib not available, skipping matplotlib charts")
            return []

        output_dir.mkdir(parents=True, exist_ok=True)
        chart_files = []

        perf_data = self.extract_performance_data()

        # Chart 1: Execution Time Comparison
        chart_files.append(self._create_execution_time_chart(perf_data, output_dir))

        # Chart 2: Scalability Analysis
        chart_files.append(self._create_scalability_chart(perf_data, output_dir))

        # Chart 3: Memory Usage Analysis
        chart_files.append(self._create_memory_usage_chart(perf_data, output_dir))

        # Chart 4: Algorithm Comparison Matrix
        chart_files.append(self._create_comparison_matrix(perf_data, output_dir))

        return [f for f in chart_files if f]

    def _create_execution_time_chart(
        self, perf_data: dict[str, Any], output_dir: Path
    ) -> Path | None:
        """Create execution time comparison chart."""
        fig, ax = plt.subplots(figsize=(12, 8))

        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
        markers = ["o", "s", "^", "D"]

        for i, algorithm in enumerate(perf_data["algorithms"]):
            input_vals = []
            exec_times = []
            timeout_vals = []

            for input_val in perf_data["input_values"]:
                if input_val in perf_data["execution_times"][algorithm]:
                    time_val = perf_data["execution_times"][algorithm][input_val]
                    if time_val is not None:  # Not timeout
                        input_vals.append(input_val)
                        exec_times.append(time_val)
                    else:  # Timeout
                        timeout_vals.append(input_val)

            # Plot successful measurements
            if input_vals and exec_times:
                ax.plot(
                    input_vals,
                    exec_times,
                    marker=markers[i % len(markers)],
                    color=colors[i % len(colors)],
                    linewidth=2,
                    markersize=8,
                    label=algorithm,
                )

            # Mark timeouts
            if timeout_vals:
                ax.scatter(
                    timeout_vals,
                    [ax.get_ylim()[1] * 0.9] * len(timeout_vals),
                    marker="x",
                    color=colors[i % len(colors)],
                    s=100,
                    label=f"{algorithm} (timeout)",
                )

        ax.set_xlabel("Input Value (n)", fontsize=12)
        ax.set_ylabel("Execution Time (seconds)", fontsize=12)
        ax.set_title(
            f"Problem {self.problem_number}: {self.problem_title}\nExecution Time Comparison",
            fontsize=14,
            fontweight="bold",
        )
        ax.set_yscale("log")
        ax.grid(True, alpha=0.3)
        ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

        plt.tight_layout()
        output_path = output_dir / "execution_time_comparison.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()

        return output_path

    def _create_scalability_chart(
        self, perf_data: dict[str, Any], output_dir: Path
    ) -> Path | None:
        """Create scalability analysis chart."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

        # Left plot: Linear scale
        for i, algorithm in enumerate(perf_data["algorithms"]):
            input_vals = []
            exec_times = []

            for input_val in perf_data["input_values"]:
                if (
                    input_val in perf_data["execution_times"][algorithm]
                    and perf_data["execution_times"][algorithm][input_val] is not None
                ):
                    input_vals.append(input_val)
                    exec_times.append(
                        perf_data["execution_times"][algorithm][input_val]
                    )

            if input_vals and exec_times:
                ax1.plot(
                    input_vals,
                    exec_times,
                    marker="o",
                    color=colors[i % len(colors)],
                    linewidth=2,
                    markersize=6,
                    label=algorithm,
                )

        ax1.set_xlabel("Input Value (n)")
        ax1.set_ylabel("Execution Time (seconds)")
        ax1.set_title("Scalability Analysis (Linear Scale)")
        ax1.grid(True, alpha=0.3)
        ax1.legend()

        # Right plot: Log-log scale
        for i, algorithm in enumerate(perf_data["algorithms"]):
            input_vals = []
            exec_times = []

            for input_val in perf_data["input_values"]:
                if (
                    input_val in perf_data["execution_times"][algorithm]
                    and perf_data["execution_times"][algorithm][input_val] is not None
                    and input_val > 0
                ):  # Log scale requires positive values
                    input_vals.append(input_val)
                    exec_times.append(
                        perf_data["execution_times"][algorithm][input_val]
                    )

            if input_vals and exec_times:
                ax2.loglog(
                    input_vals,
                    exec_times,
                    marker="o",
                    color=colors[i % len(colors)],
                    linewidth=2,
                    markersize=6,
                    label=algorithm,
                )

        ax2.set_xlabel("Input Value (n)")
        ax2.set_ylabel("Execution Time (seconds)")
        ax2.set_title("Scalability Analysis (Log-Log Scale)")
        ax2.grid(True, alpha=0.3)
        ax2.legend()

        plt.tight_layout()
        output_path = output_dir / "scalability_analysis.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()

        return output_path

    def _create_memory_usage_chart(
        self, perf_data: dict[str, Any], output_dir: Path
    ) -> Path | None:
        """Create memory usage analysis chart."""
        # Check if we have memory data
        has_memory_data = False
        for algorithm in perf_data["algorithms"]:
            if perf_data["memory_usage"][algorithm]:
                has_memory_data = True
                break

        if not has_memory_data:
            return None

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

        # Left plot: Peak memory usage
        for i, algorithm in enumerate(perf_data["algorithms"]):
            input_vals = []
            memory_vals = []

            for input_val in perf_data["input_values"]:
                if input_val in perf_data["memory_usage"][algorithm]:
                    memory_data = perf_data["memory_usage"][algorithm][input_val]
                    input_vals.append(input_val)
                    memory_vals.append(memory_data["peak_mb"])

            if input_vals and memory_vals:
                ax1.plot(
                    input_vals,
                    memory_vals,
                    marker="o",
                    color=colors[i % len(colors)],
                    linewidth=2,
                    markersize=6,
                    label=algorithm,
                )

        ax1.set_xlabel("Input Value (n)")
        ax1.set_ylabel("Peak Memory Usage (MB)")
        ax1.set_title("Peak Memory Usage by Algorithm")
        ax1.grid(True, alpha=0.3)
        ax1.legend()

        # Right plot: Memory efficiency (memory per unit time)
        for i, algorithm in enumerate(perf_data["algorithms"]):
            input_vals = []
            efficiency_vals = []

            for input_val in perf_data["input_values"]:
                if (
                    input_val in perf_data["memory_usage"][algorithm]
                    and input_val in perf_data["execution_times"][algorithm]
                    and perf_data["execution_times"][algorithm][input_val] is not None
                ):
                    memory_data = perf_data["memory_usage"][algorithm][input_val]
                    exec_time = perf_data["execution_times"][algorithm][input_val]

                    if exec_time > 0:
                        efficiency = memory_data["peak_mb"] / exec_time
                        input_vals.append(input_val)
                        efficiency_vals.append(efficiency)

            if input_vals and efficiency_vals:
                ax2.plot(
                    input_vals,
                    efficiency_vals,
                    marker="o",
                    color=colors[i % len(colors)],
                    linewidth=2,
                    markersize=6,
                    label=algorithm,
                )

        ax2.set_xlabel("Input Value (n)")
        ax2.set_ylabel("Memory Efficiency (MB/second)")
        ax2.set_title("Memory Efficiency by Algorithm")
        ax2.grid(True, alpha=0.3)
        ax2.legend()

        plt.tight_layout()
        output_path = output_dir / "memory_usage_analysis.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()

        return output_path

    def _create_comparison_matrix(
        self, perf_data: dict[str, Any], output_dir: Path
    ) -> Path | None:
        """Create algorithm comparison matrix heatmap."""
        algorithms = perf_data["algorithms"]
        input_values = perf_data["input_values"]

        # Create relative performance matrix
        n_algs = len(algorithms)
        n_inputs = len(input_values)

        fig, ax = plt.subplots(figsize=(max(8, n_inputs), max(6, n_algs)))

        # Prepare data for heatmap
        heatmap_data = []
        for algorithm in algorithms:
            row = []
            for input_val in input_values:
                if input_val in perf_data["relative_speeds"][algorithm] and perf_data[
                    "relative_speeds"
                ][algorithm][input_val] != float("inf"):
                    rel_speed = perf_data["relative_speeds"][algorithm][input_val]
                    row.append(rel_speed)
                else:
                    row.append(float("nan"))  # Timeout or no data
            heatmap_data.append(row)

        # Create heatmap
        im = ax.imshow(heatmap_data, cmap="RdYlGn_r", aspect="auto")

        # Set ticks and labels
        ax.set_xticks(range(n_inputs))
        ax.set_yticks(range(n_algs))
        ax.set_xticklabels([f"n={val}" for val in input_values], rotation=45)
        ax.set_yticklabels(algorithms)

        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label("Relative Speed (lower is better)", rotation=270, labelpad=20)

        # Add text annotations
        for i in range(n_algs):
            for j in range(n_inputs):
                if not math.isnan(heatmap_data[i][j]):
                    text = f"{heatmap_data[i][j]:.2f}"
                    ax.text(
                        j,
                        i,
                        text,
                        ha="center",
                        va="center",
                        color="white" if heatmap_data[i][j] > 5 else "black",
                    )

        ax.set_title(
            f"Problem {self.problem_number}: Algorithm Performance Matrix\n"
            f"(Relative Speed Comparison)",
            fontsize=14,
            fontweight="bold",
        )

        plt.tight_layout()
        output_path = output_dir / "algorithm_comparison_matrix.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()

        return output_path

    def create_interactive_plotly_charts(self, output_dir: Path) -> list[Path]:
        """Create interactive charts using Plotly."""
        if not PLOTLY_AVAILABLE:
            print("Plotly not available, skipping interactive charts")
            return []

        output_dir.mkdir(parents=True, exist_ok=True)
        chart_files = []

        perf_data = self.extract_performance_data()

        # Interactive performance dashboard
        chart_files.append(self._create_interactive_dashboard(perf_data, output_dir))

        return [f for f in chart_files if f]

    def _create_interactive_dashboard(
        self, perf_data: dict[str, Any], output_dir: Path
    ) -> Path | None:
        """Create comprehensive interactive dashboard."""
        # Create subplots
        fig = make_subplots(
            rows=2,
            cols=2,
            subplot_titles=(
                "Execution Time Comparison",
                "Relative Speed Comparison",
                "Memory Usage Analysis",
                "Algorithm Performance Matrix",
            ),
            specs=[
                [{"secondary_y": False}, {"secondary_y": False}],
                [{"secondary_y": False}, {"type": "heatmap"}],
            ],
        )

        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

        # Plot 1: Execution times
        for i, algorithm in enumerate(perf_data["algorithms"]):
            input_vals = []
            exec_times = []

            for input_val in perf_data["input_values"]:
                if (
                    input_val in perf_data["execution_times"][algorithm]
                    and perf_data["execution_times"][algorithm][input_val] is not None
                ):
                    input_vals.append(input_val)
                    exec_times.append(
                        perf_data["execution_times"][algorithm][input_val]
                    )

            if input_vals and exec_times:
                fig.add_trace(
                    go.Scatter(
                        x=input_vals,
                        y=exec_times,
                        mode="lines+markers",
                        name=algorithm,
                        line={"color": colors[i % len(colors)]},
                        hovertemplate=f"<b>{algorithm}</b><br>"
                        + "Input: %{x}<br>"
                        + "Time: %{y:.6f}s<extra></extra>",
                    ),
                    row=1,
                    col=1,
                )

        # Plot 2: Relative speeds
        for i, algorithm in enumerate(perf_data["algorithms"]):
            input_vals = []
            rel_speeds = []

            for input_val in perf_data["input_values"]:
                if input_val in perf_data["relative_speeds"][algorithm] and perf_data[
                    "relative_speeds"
                ][algorithm][input_val] != float("inf"):
                    input_vals.append(input_val)
                    rel_speeds.append(
                        perf_data["relative_speeds"][algorithm][input_val]
                    )

            if input_vals and rel_speeds:
                fig.add_trace(
                    go.Scatter(
                        x=input_vals,
                        y=rel_speeds,
                        mode="lines+markers",
                        name=algorithm,
                        line={"color": colors[i % len(colors)]},
                        showlegend=False,
                        hovertemplate=f"<b>{algorithm}</b><br>"
                        + "Input: %{x}<br>"
                        + "Relative Speed: %{y:.2f}x<extra></extra>",
                    ),
                    row=1,
                    col=2,
                )

        # Update layout
        fig.update_layout(
            title=f"Problem {self.problem_number}: {self.problem_title} - Interactive Benchmark Dashboard",
            height=800,
            showlegend=True,
        )

        fig.update_xaxes(title_text="Input Value (n)", row=1, col=1)
        fig.update_yaxes(
            title_text="Execution Time (seconds)", type="log", row=1, col=1
        )
        fig.update_xaxes(title_text="Input Value (n)", row=1, col=2)
        fig.update_yaxes(title_text="Relative Speed", row=1, col=2)

        # Save interactive chart
        output_path = output_dir / "interactive_dashboard.html"
        pyo.plot(fig, filename=str(output_path), auto_open=False)

        return output_path

    def generate_summary_report(self, output_dir: Path) -> Path:
        """Generate a comprehensive text summary report."""
        output_dir.mkdir(parents=True, exist_ok=True)
        report_path = output_dir / "benchmark_summary_report.txt"

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"Problem {self.problem_number}: {self.problem_title}\n")
            f.write("=" * 60 + "\n")
            f.write(f"Benchmark Timestamp: {self.data.get('timestamp', 'Unknown')}\n\n")

            # Summary statistics
            summary = self.data.get("summary", {})
            f.write("SUMMARY STATISTICS\n")
            f.write("-" * 20 + "\n")
            f.write(
                f"Stages Completed: {', '.join(summary.get('stages_completed', []))}\n"
            )
            f.write(
                f"Input Values Tested: {summary.get('total_input_values_tested', 0)}\n"
            )
            f.write(
                f"Algorithms Tested: {', '.join(summary.get('algorithms_tested', []))}\n"
            )
            f.write(
                f"Total Benchmark Time: {self.data.get('total_benchmark_time', 0):.2f} seconds\n\n"
            )

            # Timeout analysis
            timeout_stats = summary.get("timeout_statistics", {})
            f.write("TIMEOUT ANALYSIS\n")
            f.write("-" * 16 + "\n")
            f.write(
                f"Total Measurements: {timeout_stats.get('total_measurements', 0)}\n"
            )
            f.write(
                f"Timeout Rate: {timeout_stats.get('timeout_rate', 0) * 100:.1f}%\n"
            )

            timeout_by_alg = timeout_stats.get("timeout_by_algorithm", {})
            if timeout_by_alg:
                f.write("Timeouts by Algorithm:\n")
                f.writelines(
                    f"  - {alg}: {count} timeouts\n"
                    for alg, count in timeout_by_alg.items()
                )
            f.write("\n")

            # Performance insights
            insights = summary.get("performance_insights", {})
            fastest_by_stage = insights.get("fastest_by_stage", {})
            if fastest_by_stage:
                f.write("FASTEST ALGORITHM BY STAGE\n")
                f.write("-" * 25 + "\n")
                for stage, fastest_map in fastest_by_stage.items():
                    f.write(f"{stage.upper()} Stage:\n")
                    f.writelines(
                        f"  n={input_val}: {fastest_alg}\n"
                        for input_val, fastest_alg in fastest_map.items()
                    )
                    f.write("\n")

            # Detailed results by stage
            f.write("DETAILED RESULTS BY STAGE\n")
            f.write("-" * 26 + "\n")
            for stage_name, stage_data in self.data.get("stages", {}).items():
                if not stage_data:
                    continue

                f.write(f"\n{stage_name.upper()} STAGE:\n")
                for input_str, results in stage_data.items():
                    f.write(f"\n  Input n={input_str}:\n")
                    for result in results:
                        alg_name = result["name"]
                        if result["timeout_occurred"]:
                            f.write(f"    {alg_name}: TIMEOUT\n")
                        else:
                            time_val = result["mean_time"]
                            rel_speed = result["relative_speed"]
                            runs = result.get("adaptive_runs", result.get("runs", "?"))
                            f.write(
                                f"    {alg_name}: {time_val:.6f}s "
                                f"({rel_speed:.2f}x, {runs} runs)\n"
                            )

        return report_path
