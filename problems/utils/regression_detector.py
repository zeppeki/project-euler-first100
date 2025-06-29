#!/usr/bin/env python3
"""
Performance regression detection for Project Euler benchmarks.

This module provides automated detection of performance regressions by comparing
current benchmark results with historical baselines.
"""

import json
import statistics
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


@dataclass
class RegressionAlert:
    """Represents a performance regression alert."""

    problem_number: str
    solution_name: str
    current_time: float
    baseline_time: float
    regression_percent: float
    severity: str  # "minor", "major", "critical"
    alert_type: str  # "regression", "improvement"
    timestamp: str


@dataclass
class RegressionAnalysis:
    """Complete regression analysis results."""

    analysis_timestamp: str
    baseline_file: str
    current_file: str
    total_comparisons: int
    regressions: list[RegressionAlert]
    improvements: list[RegressionAlert]
    unchanged: int
    summary: dict[str, Any]


class PerformanceRegressionDetector:
    """Detects performance regressions in benchmark results."""

    def __init__(
        self, regression_threshold: float = 0.20, improvement_threshold: float = 0.20
    ):
        """
        Initialize regression detector.

        Args:
            regression_threshold: Threshold for detecting regressions (default 20%)
            improvement_threshold: Threshold for detecting improvements (default 20%)
        """
        self.regression_threshold = regression_threshold
        self.improvement_threshold = improvement_threshold
        self.benchmarks_dir = Path(__file__).parent.parent.parent / "benchmarks"

    def find_baseline_file(self, days_back: int = 7) -> Path | None:
        """
        Find the most recent baseline file within the specified time window.

        Args:
            days_back: Number of days to look back for baseline

        Returns:
            Path to baseline file or None if not found
        """
        historical_dir = self.benchmarks_dir / "aggregated" / "historical"
        if not historical_dir.exists():
            return None

        cutoff_date = datetime.now() - timedelta(days=days_back)

        # Look for files in historical directory
        baseline_files = []
        for file_path in historical_dir.glob("*.json"):
            try:
                # Extract timestamp from filename (assuming format: YYYY-MM-DD_HH-MM-SS.json)
                filename = file_path.stem
                if len(filename) >= 19:  # Basic sanity check
                    file_date = datetime.fromisoformat(
                        filename.replace("_", "T").replace("-", ":")
                    )
                    if file_date >= cutoff_date:
                        baseline_files.append((file_date, file_path))
            except (ValueError, TypeError):
                continue

        if not baseline_files:
            return None

        # Return the most recent baseline
        baseline_files.sort(key=lambda x: x[0], reverse=True)
        return baseline_files[0][1]

    def load_benchmark_data(self, file_path: Path) -> dict[str, Any] | None:
        """Load benchmark data from JSON file."""
        try:
            with open(file_path, encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def extract_performance_metrics(
        self, benchmark_data: dict[str, Any]
    ) -> dict[str, dict[str, float]]:
        """
        Extract performance metrics from benchmark data.

        Returns:
            Dictionary mapping problem_number -> {solution_name: mean_time}
        """
        metrics: dict[str, dict[str, float]] = {}

        problems = benchmark_data.get("problems", [])
        for problem in problems:
            problem_number = problem.get("problem_number", "")
            if not problem_number:
                continue

            metrics[problem_number] = {}
            solutions = problem.get("solutions", [])
            for solution in solutions:
                solution_name = solution.get("name", "")
                mean_time = solution.get("mean_time", 0.0)

                if solution_name and mean_time != float("inf"):
                    metrics[problem_number][solution_name] = mean_time

        return metrics

    def compare_performance(
        self,
        current_metrics: dict[str, dict[str, float]],
        baseline_metrics: dict[str, dict[str, float]],
    ) -> tuple[list[RegressionAlert], list[RegressionAlert], int]:
        """
        Compare current performance against baseline.

        Returns:
            Tuple of (regressions, improvements, unchanged_count)
        """
        regressions: list[RegressionAlert] = []
        improvements: list[RegressionAlert] = []
        unchanged = 0

        timestamp = datetime.now().isoformat()

        for problem_number, current_solutions in current_metrics.items():
            if problem_number not in baseline_metrics:
                continue

            baseline_solutions = baseline_metrics[problem_number]

            for solution_name, current_time in current_solutions.items():
                if solution_name not in baseline_solutions:
                    continue

                baseline_time = baseline_solutions[solution_name]
                if baseline_time <= 0:  # Avoid division by zero
                    continue

                # Calculate percentage change
                percent_change = (current_time - baseline_time) / baseline_time

                if percent_change > self.regression_threshold:
                    # Performance regression detected
                    severity = self._determine_severity(percent_change)
                    alert = RegressionAlert(
                        problem_number=problem_number,
                        solution_name=solution_name,
                        current_time=current_time,
                        baseline_time=baseline_time,
                        regression_percent=percent_change * 100,
                        severity=severity,
                        alert_type="regression",
                        timestamp=timestamp,
                    )
                    regressions.append(alert)

                elif percent_change < -self.improvement_threshold:
                    # Performance improvement detected
                    alert = RegressionAlert(
                        problem_number=problem_number,
                        solution_name=solution_name,
                        current_time=current_time,
                        baseline_time=baseline_time,
                        regression_percent=percent_change * 100,
                        severity="improvement",
                        alert_type="improvement",
                        timestamp=timestamp,
                    )
                    improvements.append(alert)

                else:
                    unchanged += 1

        return regressions, improvements, unchanged

    def _determine_severity(self, percent_change: float) -> str:
        """Determine the severity of a regression based on percentage change."""
        if percent_change > 1.0:  # 100% or more slowdown
            return "critical"
        if percent_change > 0.5:  # 50-100% slowdown
            return "major"
        # 20-50% slowdown
        return "minor"

    def analyze_regression(
        self, current_file: Path | None = None, baseline_file: Path | None = None
    ) -> RegressionAnalysis | None:
        """
        Perform complete regression analysis.

        Args:
            current_file: Path to current benchmark results (defaults to latest.json)
            baseline_file: Path to baseline results (auto-detected if None)

        Returns:
            RegressionAnalysis object or None if analysis cannot be performed
        """
        # Default to latest results
        if current_file is None:
            current_file = self.benchmarks_dir / "aggregated" / "latest.json"

        # Auto-detect baseline if not provided
        if baseline_file is None:
            baseline_file = self.find_baseline_file()

        if not current_file.exists():
            return None

        if baseline_file is None or not baseline_file.exists():
            return None

        # Load benchmark data
        current_data = self.load_benchmark_data(current_file)
        baseline_data = self.load_benchmark_data(baseline_file)

        if not current_data or not baseline_data:
            return None

        # Extract performance metrics
        current_metrics = self.extract_performance_metrics(current_data)
        baseline_metrics = self.extract_performance_metrics(baseline_data)

        # Perform comparison
        regressions, improvements, unchanged = self.compare_performance(
            current_metrics, baseline_metrics
        )

        # Generate summary statistics
        total_comparisons = len(regressions) + len(improvements) + unchanged

        summary = {
            "total_regressions": len(regressions),
            "total_improvements": len(improvements),
            "unchanged_solutions": unchanged,
            "regression_rate": len(regressions) / total_comparisons
            if total_comparisons > 0
            else 0,
            "improvement_rate": len(improvements) / total_comparisons
            if total_comparisons > 0
            else 0,
        }

        # Add severity breakdown
        severity_counts = {"critical": 0, "major": 0, "minor": 0}
        for regression in regressions:
            severity_counts[regression.severity] += 1
        summary["severity_breakdown"] = severity_counts

        # Add performance impact statistics
        if regressions:
            regression_percentages = [r.regression_percent for r in regressions]
            summary["regression_stats"] = {
                "mean_regression": statistics.mean(regression_percentages),
                "median_regression": statistics.median(regression_percentages),
                "max_regression": max(regression_percentages),
            }

        if improvements:
            improvement_percentages = [abs(i.regression_percent) for i in improvements]
            summary["improvement_stats"] = {
                "mean_improvement": statistics.mean(improvement_percentages),
                "median_improvement": statistics.median(improvement_percentages),
                "max_improvement": max(improvement_percentages),
            }

        return RegressionAnalysis(
            analysis_timestamp=datetime.now().isoformat(),
            baseline_file=str(baseline_file),
            current_file=str(current_file),
            total_comparisons=total_comparisons,
            regressions=regressions,
            improvements=improvements,
            unchanged=unchanged,
            summary=summary,
        )

    def save_analysis(
        self, analysis: RegressionAnalysis, output_file: Path | None = None
    ) -> None:
        """Save regression analysis to JSON file."""
        if output_file is None:
            output_file = self.benchmarks_dir / "reports" / "regression_analysis.json"

        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Convert dataclass to dictionary for JSON serialization
        analysis_dict = {
            "analysis_timestamp": analysis.analysis_timestamp,
            "baseline_file": analysis.baseline_file,
            "current_file": analysis.current_file,
            "total_comparisons": analysis.total_comparisons,
            "unchanged": analysis.unchanged,
            "summary": analysis.summary,
            "regressions": [
                {
                    "problem_number": r.problem_number,
                    "solution_name": r.solution_name,
                    "current_time": r.current_time,
                    "baseline_time": r.baseline_time,
                    "regression_percent": r.regression_percent,
                    "severity": r.severity,
                    "alert_type": r.alert_type,
                    "timestamp": r.timestamp,
                }
                for r in analysis.regressions
            ],
            "improvements": [
                {
                    "problem_number": i.problem_number,
                    "solution_name": i.solution_name,
                    "current_time": i.current_time,
                    "baseline_time": i.baseline_time,
                    "regression_percent": i.regression_percent,
                    "severity": i.severity,
                    "alert_type": i.alert_type,
                    "timestamp": i.timestamp,
                }
                for i in analysis.improvements
            ],
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(analysis_dict, f, indent=2, ensure_ascii=False)

    def generate_alert_report(self, analysis: RegressionAnalysis) -> str:
        """Generate human-readable alert report."""
        report_lines = []
        report_lines.append("PERFORMANCE REGRESSION ANALYSIS REPORT")
        report_lines.append("=" * 50)
        report_lines.append(f"Generated: {analysis.analysis_timestamp}")
        report_lines.append(f"Baseline: {analysis.baseline_file}")
        report_lines.append(f"Current: {analysis.current_file}")
        report_lines.append("")

        # Summary
        summary = analysis.summary
        report_lines.append("SUMMARY")
        report_lines.append("-" * 20)
        report_lines.append(f"Total Comparisons: {analysis.total_comparisons}")
        report_lines.append(f"Regressions: {summary['total_regressions']}")
        report_lines.append(f"Improvements: {summary['total_improvements']}")
        report_lines.append(f"Unchanged: {analysis.unchanged}")
        report_lines.append(f"Regression Rate: {summary['regression_rate']:.1%}")
        report_lines.append("")

        # Regressions by severity
        if analysis.regressions:
            severity_counts = summary["severity_breakdown"]
            report_lines.append("REGRESSIONS BY SEVERITY")
            report_lines.append("-" * 30)
            report_lines.append(f"Critical: {severity_counts['critical']}")
            report_lines.append(f"Major: {severity_counts['major']}")
            report_lines.append(f"Minor: {severity_counts['minor']}")
            report_lines.append("")

            # Detailed regression list
            report_lines.append("DETAILED REGRESSIONS")
            report_lines.append("-" * 25)
            for regression in sorted(
                analysis.regressions, key=lambda x: x.regression_percent, reverse=True
            ):
                report_lines.append(
                    f"Problem {regression.problem_number} - {regression.solution_name}: "
                    f"{regression.regression_percent:+.1f}% ({regression.severity})"
                )
                report_lines.append(
                    f"  {regression.baseline_time:.6f}s -> {regression.current_time:.6f}s"
                )
            report_lines.append("")

        # Improvements
        if analysis.improvements:
            report_lines.append("PERFORMANCE IMPROVEMENTS")
            report_lines.append("-" * 30)
            for improvement in sorted(
                analysis.improvements, key=lambda x: x.regression_percent
            ):
                report_lines.append(
                    f"Problem {improvement.problem_number} - {improvement.solution_name}: "
                    f"{improvement.regression_percent:+.1f}%"
                )
                report_lines.append(
                    f"  {improvement.baseline_time:.6f}s -> {improvement.current_time:.6f}s"
                )

        return "\n".join(report_lines)


def main() -> None:
    """Main entry point for standalone execution."""
    detector = PerformanceRegressionDetector()
    analysis = detector.analyze_regression()

    if analysis is None:
        print(
            "❌ Unable to perform regression analysis - missing baseline or current data"
        )
        return

    # Save analysis
    detector.save_analysis(analysis)

    # Generate and display report
    report = detector.generate_alert_report(analysis)
    print(report)

    # Save human-readable report
    report_path = Path("benchmarks/reports/regression_report.txt")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n📊 Analysis saved to: benchmarks/reports/regression_analysis.json")
    print("📋 Report saved to: benchmarks/reports/regression_report.txt")

    # Exit with appropriate code for CI/CD
    if analysis.regressions:
        critical_regressions = [
            r for r in analysis.regressions if r.severity == "critical"
        ]
        if critical_regressions:
            print(f"\n❌ {len(critical_regressions)} critical regression(s) detected!")
            exit(2)  # Critical regressions
        else:
            print(f"\n⚠️  {len(analysis.regressions)} regression(s) detected")
            exit(1)  # Non-critical regressions
    else:
        print("\n✅ No performance regressions detected")
        exit(0)  # All good


if __name__ == "__main__":
    main()
