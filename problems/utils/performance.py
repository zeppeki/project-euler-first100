"""
Performance measurement utilities for Project Euler solutions.
"""

import time
from collections.abc import Callable
from typing import Any


def measure_performance(
    func: Callable[..., Any], *args: Any, **kwargs: Any
) -> tuple[Any, float]:
    """
    Measure the execution time of a function.

    Args:
        func: Function to measure
        *args: Arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function

    Returns:
        Tuple of (result, execution_time_in_seconds)
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    execution_time = time.time() - start_time
    return result, execution_time


def compare_performance(
    functions: list[tuple[str, Callable[..., Any]]], *args: Any, **kwargs: Any
) -> dict[str, dict[str, Any]]:
    """
    Compare performance of multiple functions with the same arguments.

    Args:
        functions: List of (name, function) tuples
        *args: Arguments to pass to all functions
        **kwargs: Keyword arguments to pass to all functions

    Returns:
        Dictionary with performance results for each function
    """
    results = {}

    for name, func in functions:
        result, execution_time = measure_performance(func, *args, **kwargs)
        results[name] = {"result": result, "execution_time": execution_time}

    # Calculate relative performance
    if results:
        fastest_time = min(data["execution_time"] for data in results.values())
        for data in results.values():
            data["relative_speed"] = (
                data["execution_time"] / fastest_time if fastest_time > 0 else 1.0
            )

    return results
