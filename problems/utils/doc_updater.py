#!/usr/bin/env python3
"""
Documentation updater for Project Euler benchmark results.

This module automatically updates solution documentation with performance
analysis while respecting the GitHub Pages content policy (no direct answers).
"""

import json
import re
from pathlib import Path
from typing import Any


class DocumentationUpdater:
    """Updates solution documentation with benchmark results."""

    def __init__(self):
        """Initialize the documentation updater."""
        self.benchmarks_dir = Path(__file__).parent.parent.parent / "benchmarks"
        self.docs_dir = Path(__file__).parent.parent.parent / "docs" / "solutions"

    def load_benchmark_results(self) -> dict[str, Any] | None:
        """Load the latest benchmark results."""
        latest_file = self.benchmarks_dir / "aggregated" / "latest.json"
        if not latest_file.exists():
            return None

        try:
            with open(latest_file, encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def format_performance_section(self, problem_data: dict[str, Any]) -> str:
        """Format the performance analysis section for a problem."""
        solutions = problem_data.get("solutions", [])
        if not solutions:
            return ""

        lines = []
        lines.append("## パフォーマンス分析")
        lines.append("")

        # Create performance comparison table
        lines.append("### 実行時間比較")
        lines.append("")
        lines.append("| 解法 | 実行時間 | 相対速度 | 時間計算量 |")
        lines.append("|------|----------|----------|------------|")

        for solution in solutions:
            name = solution.get("name", "")
            mean_time = solution.get("mean_time", 0.0)
            relative_speed = solution.get("relative_speed", 1.0)
            complexity = solution.get("complexity_class", "")

            # Format execution time appropriately
            if mean_time < 0.001:  # Less than 1ms
                time_str = f"{mean_time * 1_000_000:.1f}μs"
            elif mean_time < 1.0:  # Less than 1s
                time_str = f"{mean_time * 1000:.1f}ms"
            else:  # 1s or more
                time_str = f"{mean_time:.2f}s"

            lines.append(
                f"| {name} | {time_str} | {relative_speed:.1f}x | {complexity} |"
            )

        lines.append("")

        # Add verification status
        verified = problem_data.get("verified", False)
        verification_emoji = "✅" if verified else "❌"
        lines.append(
            f"**検証結果**: {verification_emoji} {'全解法で一致' if verified else '解法間で不一致'}"
        )
        lines.append("")

        # Add fastest solution
        fastest_solution = problem_data.get("fastest_solution", "")
        if fastest_solution:
            lines.append(f"**最速解法**: {fastest_solution}")
            lines.append("")

        # Add benchmark metadata
        timestamp = problem_data.get("timestamp", "")
        if timestamp:
            lines.append(f"*ベンチマーク実行時刻: {timestamp[:19].replace('T', ' ')}*")
            lines.append("")

        return "\n".join(lines)

    def find_performance_section(self, content: str) -> tuple[int, int] | None:
        """
        Find the existing performance section in documentation.

        Returns:
            Tuple of (start_line, end_line) indices or None if not found
        """
        lines = content.split("\n")

        # Look for performance section markers
        start_patterns = [
            r"^## パフォーマンス分析",
            r"^## Performance Analysis",
            r"^## 実行時間",
            r"^## Execution Time",
        ]

        start_index = None
        for i, line in enumerate(lines):
            for pattern in start_patterns:
                if re.match(pattern, line):
                    start_index = i
                    break
            if start_index is not None:
                break

        if start_index is None:
            return None

        # Find the end of the section (next ## header or end of file)
        end_index = len(lines)
        for i in range(start_index + 1, len(lines)):
            if lines[i].startswith("## "):
                end_index = i
                break

        return (start_index, end_index)

    def update_solution_doc(
        self, problem_number: str, problem_data: dict[str, Any]
    ) -> bool:
        """Update a single solution document with benchmark results."""
        doc_file = self.docs_dir / f"solution_{problem_number}.md"
        if not doc_file.exists():
            print(f"  ⚠ Warning: Documentation file not found: {doc_file}")
            return False

        try:
            # Read existing content
            with open(doc_file, encoding="utf-8") as f:
                content = f.read()

            # Generate new performance section
            performance_section = self.format_performance_section(problem_data)
            if not performance_section:
                print(f"  ⚠ Warning: No performance data for problem {problem_number}")
                return False

            # Find existing performance section
            section_bounds = self.find_performance_section(content)

            lines = content.split("\n")

            if section_bounds:
                # Replace existing section
                start_index, end_index = section_bounds
                new_lines = (
                    lines[:start_index]
                    + performance_section.split("\n")
                    + lines[end_index:]
                )
            else:
                # Add new section before the final line (if it exists)
                # Insert before any "参考文献" or "References" section
                insert_index = len(lines)

                # Look for common end sections
                end_section_patterns = [
                    r"^## 参考文献",
                    r"^## References",
                    r"^## リンク",
                    r"^## Links",
                ]

                for i, line in enumerate(lines):
                    for pattern in end_section_patterns:
                        if re.match(pattern, line):
                            insert_index = i
                            break
                    if insert_index < len(lines):
                        break

                # Insert the performance section
                new_lines = [
                    *lines[:insert_index],
                    "",  # Empty line before new section
                    *performance_section.split("\n"),
                    *lines[insert_index:],
                ]

            # Write updated content
            new_content = "\n".join(new_lines)
            with open(doc_file, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"  ✓ Updated: {doc_file.name}")
            return True

        except Exception as e:
            print(f"  ✗ Error updating {doc_file.name}: {e}")
            return False

    def update_all_docs(self) -> tuple[int, int]:
        """
        Update all solution documents with benchmark results.

        Returns:
            Tuple of (successful_updates, total_attempts)
        """
        benchmark_data = self.load_benchmark_results()
        if not benchmark_data:
            print("❌ No benchmark results found. Run 'make benchmark' first.")
            return (0, 0)

        problems = benchmark_data.get("problems", [])
        if not problems:
            print("❌ No problem data in benchmark results.")
            return (0, 0)

        print(f"Updating documentation for {len(problems)} problems...")

        successful_updates = 0
        total_attempts = len(problems)

        for problem_data in problems:
            problem_number = problem_data.get("problem_number", "")
            if not problem_number:
                continue

            print(f"Processing Problem {problem_number}...")
            if self.update_solution_doc(problem_number, problem_data):
                successful_updates += 1

        return (successful_updates, total_attempts)

    def generate_benchmark_index(self) -> bool:
        """Generate an index page for all benchmark results."""
        benchmark_data = self.load_benchmark_results()
        if not benchmark_data:
            return False

        problems = benchmark_data.get("problems", [])
        summary = benchmark_data.get("summary", {})

        # Create benchmark index content
        lines = []
        lines.append("# ベンチマーク結果インデックス")
        lines.append("")
        lines.append("Project Eulerソリューションの総合パフォーマンス分析結果です。")
        lines.append("")

        # Summary statistics
        lines.append("## 概要統計")
        lines.append("")
        lines.append(f"- **分析問題数**: {summary.get('total_problems', 0)}")
        lines.append(f"- **検証済み解法**: {summary.get('verified_problems', 0)}")
        lines.append(f"- **検証率**: {summary.get('verification_rate', 0):.1%}")
        lines.append(f"- **総解法数**: {summary.get('total_solutions', 0)}")
        lines.append("")

        # Algorithm distribution
        algo_dist = summary.get("algorithm_distribution", {})
        if algo_dist:
            lines.append("## アルゴリズム分布")
            lines.append("")
            for algo_type, count in algo_dist.items():
                lines.append(f"- **{algo_type}**: {count}個")
            lines.append("")

        # Performance statistics
        perf_stats = summary.get("performance_stats", {})
        if perf_stats:
            lines.append("## パフォーマンス統計")
            lines.append("")
            mean_time = perf_stats.get("mean_execution_time", 0.0)
            median_time = perf_stats.get("median_execution_time", 0.0)
            fastest_time = perf_stats.get("fastest_execution_time", 0.0)
            slowest_time = perf_stats.get("slowest_execution_time", 0.0)

            lines.append(f"- **平均実行時間**: {mean_time * 1000:.2f}ms")
            lines.append(f"- **中央値実行時間**: {median_time * 1000:.2f}ms")
            lines.append(f"- **最速解法**: {fastest_time * 1_000_000:.1f}μs")
            lines.append(f"- **最遅解法**: {slowest_time * 1000:.2f}ms")
            lines.append("")

        # Problem index table
        lines.append("## 問題別結果")
        lines.append("")
        lines.append("| 問題 | 最速解法 | 実行時間 | 検証 |")
        lines.append("|------|----------|----------|------|")

        for problem in problems:
            problem_number = problem.get("problem_number", "")
            fastest_solution = problem.get("fastest_solution", "")
            verified = problem.get("verified", False)

            # Find fastest time
            fastest_time = float("inf")
            solutions = problem.get("solutions", [])
            for solution in solutions:
                if solution.get("name") == fastest_solution:
                    fastest_time = solution.get("mean_time", float("inf"))
                    break

            # Format time
            if fastest_time < 0.001:
                time_str = f"{fastest_time * 1_000_000:.1f}μs"
            elif fastest_time < 1.0:
                time_str = f"{fastest_time * 1000:.1f}ms"
            else:
                time_str = f"{fastest_time:.2f}s"

            verification_emoji = "✅" if verified else "❌"

            lines.append(
                f"| [{problem_number}](solution_{problem_number}.md) | "
                f"{fastest_solution} | {time_str} | {verification_emoji} |"
            )

        lines.append("")

        # Metadata
        timestamp = benchmark_data.get("timestamp", "")
        if timestamp:
            lines.append(f"*最終更新: {timestamp[:19].replace('T', ' ')}*")

        # Write index file
        index_file = self.docs_dir / "benchmark_index.md"
        try:
            with open(index_file, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            print(f"✓ Generated benchmark index: {index_file}")
            return True
        except Exception as e:
            print(f"✗ Error generating benchmark index: {e}")
            return False


def main() -> None:
    """Main entry point for standalone execution."""
    updater = DocumentationUpdater()

    # Update all solution documents
    successful, total = updater.update_all_docs()

    print("\n📊 Documentation Update Results:")
    print(f"  Successfully updated: {successful}/{total} documents")

    # Generate benchmark index
    if updater.generate_benchmark_index():
        print("  ✓ Benchmark index generated")
    else:
        print("  ✗ Failed to generate benchmark index")

    if successful == total and total > 0:
        print("\n✅ All documentation successfully updated!")
    elif successful > 0:
        print(f"\n⚠️  Partial success: {successful}/{total} documents updated")
    else:
        print("\n❌ No documents were updated")


if __name__ == "__main__":
    main()
