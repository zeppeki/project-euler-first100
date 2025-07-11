#!/usr/bin/env python3
"""
Simple benchmark runner for Project Euler problems.

This module provides automatic problem detection and execution capabilities
for the simplified benchmark framework.
"""

import importlib
import inspect
import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

from .simple_benchmark import SimpleBenchmark


class SimpleBenchmarkRunner:
    """
    Automatic runner for Project Euler problem benchmarks.

    Discovers problem modules and their solution functions automatically.
    """

    def __init__(self) -> None:
        self.benchmark = SimpleBenchmark()
        self.problems_dir = Path(__file__).parent.parent

    def extract_problem_number(self, module_name: str) -> str | None:
        """
        Extract problem number from module name.

        Args:
            module_name: Name of the problem module

        Returns:
            Problem number string or None if not found
        """
        match = re.search(r"problem_(\d+)", module_name)
        return match.group(1) if match else None

    def get_problem_title(self, problem_module: Any) -> str:
        """
        Extract problem title from module docstring.

        Args:
            problem_module: Imported problem module

        Returns:
            Problem title or default title
        """
        if not problem_module.__doc__:
            return "Unknown Problem"

        # Look for title in first line of docstring
        lines = problem_module.__doc__.strip().split("\n")
        if lines:
            # Remove "Problem XXX: " prefix if present
            title = lines[0].strip()
            return re.sub(r"^Problem\s+\d+:\s*", "", title)

        return "Unknown Problem"

    def discover_solutions(self, problem_module: Any) -> list[tuple[str, Callable]]:
        """
        Discover solution functions in a problem module.

        Args:
            problem_module: Imported problem module

        Returns:
            List of (name, function) tuples for solutions
        """
        solutions: list[tuple[str, Callable]] = []

        # Look for solve_* functions (and also 'solve' for some problems)
        for name, obj in inspect.getmembers(problem_module):
            if (
                (name.startswith("solve_") or name == "solve")
                and inspect.isfunction(obj)
                and not name.endswith("_test")
            ):
                # Create human-readable name
                if name == "solve":
                    display_name = "汎用解法 (General)"
                else:
                    solution_type = name.replace("solve_", "").replace("_", " ").title()
                    if solution_type == "Naive":
                        display_name = "素直な解法 (Naive)"
                    elif solution_type == "Optimized":
                        display_name = "最適化解法 (Optimized)"
                    elif solution_type == "Mathematical":
                        display_name = "数学的解法 (Mathematical)"
                    elif solution_type == "Builtin":
                        display_name = "Built-in解法 (Builtin)"
                    else:
                        display_name = f"{solution_type}解法"

                solutions.append((display_name, obj))

        return solutions

    def get_problem_arguments(self, problem_number: str) -> tuple[tuple, dict]:
        """
        Get appropriate arguments for a specific problem.

        Args:
            problem_number: Problem number string

        Returns:
            Tuple of (args, kwargs) for the problem
        """
        # Handle special cases that require data import
        if problem_number == "011":
            # Import grid data for Problem 011
            try:
                problem_module = importlib.import_module(
                    f"problems.problem_{problem_number.zfill(3)}"
                )
                grid_data = problem_module.GRID_DATA
                return ((grid_data,), {})
            except (ImportError, AttributeError):
                return ((), {})

        if problem_number == "018":
            # Import triangle data for Problem 018
            try:
                problem_module = importlib.import_module(
                    f"problems.problem_{problem_number.zfill(3)}"
                )
                triangle_func = problem_module.get_problem_triangle
                triangle_data = triangle_func()
                return ((triangle_data,), {})
            except (ImportError, AttributeError):
                return ((), {})

        if problem_number == "022":
            # Import names data for Problem 022
            try:
                problem_module = importlib.import_module(
                    f"problems.problem_{problem_number.zfill(3)}"
                )
                names_func = problem_module.create_sample_names
                names_data = names_func()
                return ((names_data,), {})
            except (ImportError, AttributeError):
                return ((), {})

        # Default arguments for common problems
        problem_args: dict[str, tuple[tuple, dict]] = {
            "001": ((1000,), {}),
            "002": ((4000000,), {}),
            "003": ((600851475143,), {}),
            "004": ((3, 3), {}),
            "005": ((20,), {}),
            "006": ((100,), {}),
            "007": ((10001,), {}),
            "008": ((13,), {}),
            "009": ((1000,), {}),
            "010": ((2000000,), {}),
            "011": ((), {}),
            "012": ((500,), {}),
            "013": ((), {}),
            "014": ((1000000,), {}),
            "015": ((20,), {}),
            "016": ((1000,), {}),
            "017": ((1000,), {}),
            "018": ((), {}),
            "019": ((1901, 2000), {}),
            "020": ((100,), {}),
            "021": ((10000,), {}),
            "022": ((), {}),
            "023": ((28123,), {}),
            "024": (("0123456789", 1000000), {}),
            "025": ((1000,), {}),
            "026": ((1000,), {}),
            "027": ((1000,), {}),
            "028": ((1001,), {}),
            "029": ((100,), {}),
            "030": ((5,), {}),
            "031": ((200,), {}),
            "032": ((), {}),
            "033": ((), {}),
            "034": ((), {}),
            "035": ((1000000,), {}),
            "036": ((1000000,), {}),
            "037": ((), {}),
            "038": ((), {}),
            "039": ((1000,), {}),
            "040": ((), {}),
            "041": ((), {}),
            "042": ((), {}),
            "043": ((), {}),
            # Problems 044-090 argument mappings
            "044": ((), {}),  # No arguments needed
            "045": ((), {}),  # No arguments needed
            "046": ((), {}),  # Uses default limit=10000
            "047": ((4,), {}),  # target_factors: int
            "048": ((), {}),  # Uses default limit=1000
            "049": ((), {}),  # No arguments needed
            "050": ((), {}),  # Uses default limit=1000000
            "051": ((8,), {}),  # target_family_size: int
            "052": ((), {}),  # Uses default max_x=200000
            "053": ((), {}),  # Uses default n=100
            "054": ((), {}),  # No arguments needed (uses data file)
            "055": ((), {}),  # Uses default limit=10000
            "056": ((), {}),  # Uses default max_base=100, max_exp=100
            "057": ((), {}),  # Uses default limit=1000
            "058": ((), {}),  # Uses default target_ratio=0.1
            "059": ((), {}),  # No arguments needed (uses data file)
            "060": ((), {}),  # Uses default max_prime=10000
            "061": ((), {}),  # No arguments needed
            "062": ((), {}),  # No arguments needed
            "063": ((), {}),  # No arguments needed
            "064": ((), {}),  # No arguments needed
            "065": ((), {}),  # No arguments needed
            "066": ((), {}),  # No arguments needed
            "067": ((), {}),  # No arguments needed (uses data file)
            "068": ((), {}),  # No arguments needed
            "069": ((1000000,), {}),  # limit: int
            "070": ((10000000,), {}),  # limit: int
            "071": ((1000000,), {}),  # limit: int
            "072": ((1000000,), {}),  # limit: int
            "073": ((12000,), {}),  # limit: int
            "074": ((1000000,), {}),  # limit: int
            "075": ((1500000,), {}),  # limit: int
            "076": ((100,), {}),  # target: int
            "077": ((5000,), {}),  # target: int
            "078": ((1000000,), {}),  # target_divisor: int
            "079": ((), {}),  # No arguments needed (uses data file)
            "080": ((), {}),  # Uses default limit=100
            "081": ((), {}),  # No arguments needed (uses data file)
            "082": ((), {}),  # No arguments needed (uses data file)
            "083": ((), {}),  # No arguments needed (uses data file)
            "084": ((), {}),  # Uses default dice_sides=4, num_simulations=1000000
            "085": ((), {}),  # Uses default target=2000000
            "086": ((), {}),  # Uses default max_m=2000
            "087": ((), {}),  # Uses default limit=50000000
            "088": ((), {}),  # Uses default max_k=12000
            "089": ((), {}),  # Uses default filename
            "090": ((), {}),  # No arguments needed
        }

        return problem_args.get(problem_number, ((), {}))

    def run_problem(self, problem_number: str) -> bool:
        """
        Run benchmark for a specific problem.

        Args:
            problem_number: Problem number (e.g., "001")

        Returns:
            True if successful, False otherwise
        """
        try:
            # Import the problem module
            module_name = f"problems.problem_{problem_number.zfill(3)}"
            problem_module = importlib.import_module(module_name)

            # Discover solutions
            solutions = self.discover_solutions(problem_module)
            if not solutions:
                print(f"No solution functions found in {module_name}")
                return False

            # Get problem info
            problem_title = self.get_problem_title(problem_module)
            args, kwargs = self.get_problem_arguments(problem_number)

            print(f"Benchmarking Problem {problem_number}: {problem_title}")
            print(f"Found {len(solutions)} solution(s)")
            print()

            # Run benchmark
            self.benchmark.benchmark_problem(
                problem_number, problem_title, solutions, *args, **kwargs
            )

            # Display results
            self.benchmark.display_results(problem_number)

            return True

        except ImportError as e:
            print(f"Could not import problem {problem_number}: {e}")
            return False
        except Exception as e:
            print(f"Error running benchmark for problem {problem_number}: {e}")
            return False

    def run_all_problems(self) -> None:
        """Run benchmarks for all available problems."""
        problem_files = list(self.problems_dir.glob("problem_*.py"))
        problem_numbers = []

        for file in problem_files:
            number = self.extract_problem_number(file.stem)
            if number:
                problem_numbers.append(number)

        problem_numbers.sort()

        print(f"Found {len(problem_numbers)} problems")
        print("Running benchmarks for all problems...")
        print("=" * 60)

        successful = 0
        for number in problem_numbers:
            if self.run_problem(number):
                successful += 1
            print("-" * 40)

        print(f"\nCompleted: {successful}/{len(problem_numbers)} problems")

        # Save all results
        self.save_all_results()

    def save_all_results(self) -> None:
        """Save all benchmark results to file."""
        results_dir = Path("benchmarks/results")
        results_dir.mkdir(parents=True, exist_ok=True)

        if self.benchmark.results:
            first_key = next(iter(self.benchmark.results.keys()))
            timestamp = self.benchmark.results[first_key].get("timestamp", "unknown")
        else:
            timestamp = "unknown"

        filename = f"simple_benchmark_{timestamp.replace(':', '-')}.json"
        filepath = results_dir / filename

        self.benchmark.save_results(str(filepath))


def main() -> None:
    """Main entry point for standalone execution."""
    import sys

    runner = SimpleBenchmarkRunner()

    if len(sys.argv) > 1:
        problem_number = sys.argv[1]
        runner.run_problem(problem_number)
    else:
        runner.run_all_problems()


if __name__ == "__main__":
    main()
