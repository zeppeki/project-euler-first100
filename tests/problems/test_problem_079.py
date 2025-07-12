#!/usr/bin/env python3
"""Tests for Problem 079"""

from problems.lib.file_io import load_keylog_data
from problems.lib.graph_algorithms import build_dependency_graph, topological_sort
from problems.problem_079 import (
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


def verify_passcode(passcode: str, attempts: list[str]) -> bool:
    """
    パスコードがすべてのログイン試行を満たすか検証
    """
    for attempt in attempts:
        # attemptの文字がパスコード中に正しい順序で含まれているかチェック
        pos = -1
        for char in attempt:
            new_pos = passcode.find(char, pos + 1)
            if new_pos == -1:
                return False
            pos = new_pos
    return True


class TestUtilityFunctions:
    """Test utility functions"""

    def test_read_keylog_data(self) -> None:
        """Test keylog data reading"""
        attempts = load_keylog_data()
        assert isinstance(attempts, list)
        assert len(attempts) > 0
        assert all(isinstance(attempt, str) for attempt in attempts)
        assert all(len(attempt) == 3 for attempt in attempts)
        assert all(attempt.isdigit() for attempt in attempts)

    def test_build_dependency_graph(self) -> None:
        """Test dependency graph construction"""
        test_attempts = ["319", "680", "180"]
        dependencies = build_dependency_graph(test_attempts)

        # Check that dependencies exist
        assert isinstance(dependencies, dict)
        assert "3" in dependencies
        assert "1" in dependencies["3"]
        assert "9" in dependencies["3"]

        # Check 680 dependencies
        assert "6" in dependencies
        assert "8" in dependencies["6"]
        assert "0" in dependencies["6"]
        assert "0" in dependencies["8"]

        # Check 180 dependencies
        assert "1" in dependencies
        assert "8" in dependencies["1"]
        assert "0" in dependencies["1"]

    def test_topological_sort(self) -> None:
        """Test topological sorting"""
        # Simple test case
        dependencies = {
            "3": {"1", "9"},
            "1": {"9"},
            "9": set(),
        }
        result = topological_sort(dependencies)
        assert "".join(result) == "319"

        # More complex case
        dependencies = {
            "7": {"3", "0"},
            "3": {"0"},
            "0": set(),
        }
        result = topological_sort(dependencies)
        assert "".join(result) == "730"

    def test_verify_passcode(self) -> None:
        """Test passcode verification"""
        # Valid passcode
        assert verify_passcode("319", ["319"])
        assert verify_passcode("319", ["31", "19", "39"])
        assert verify_passcode("7390", ["739", "790", "390"])

        # Invalid passcode
        assert not verify_passcode("319", ["391"])  # Wrong order
        assert not verify_passcode("39", ["319"])  # Missing digit


class TestSolutionFunctions:
    """Test main solution functions"""

    def test_solve_naive(self) -> None:
        """Test naive solution"""
        result = solve_naive()
        assert isinstance(result, int)
        assert result > 0

        # Verify the result works with all attempts
        attempts = load_keylog_data()
        passcode_str = str(result)
        assert verify_passcode(passcode_str, attempts)

    def test_solve_optimized(self) -> None:
        """Test optimized solution"""
        result = solve_optimized()
        assert isinstance(result, int)
        assert result > 0

        # Verify the result works with all attempts
        attempts = load_keylog_data()
        passcode_str = str(result)
        assert verify_passcode(passcode_str, attempts)

    def test_solve_mathematical(self) -> None:
        """Test mathematical solution"""
        result = solve_mathematical()
        assert isinstance(result, int)
        assert result > 0

        # Verify the result works with all attempts
        attempts = load_keylog_data()
        passcode_str = str(result)
        assert verify_passcode(passcode_str, attempts)

    def test_solutions_agree(self) -> None:
        """Test that all solutions agree"""
        naive_result = solve_naive()
        optimized_result = solve_optimized()
        mathematical_result = solve_mathematical()

        assert naive_result == optimized_result, (
            f"Naive and optimized disagree: {naive_result} != {optimized_result}"
        )
        assert naive_result == mathematical_result, (
            f"Naive and mathematical disagree: {naive_result} != {mathematical_result}"
        )


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_empty_dependencies(self) -> None:
        """Test empty dependency graph"""
        dependencies: dict[str, set[str]] = {}
        result = topological_sort(dependencies)
        assert "".join(result) == ""

    def test_single_digit(self) -> None:
        """Test single digit cases"""
        dependencies: dict[str, set[str]] = {"5": set()}
        result = topological_sort(dependencies)
        assert "".join(result) == "5"

    def test_small_example(self) -> None:
        """Test with a small known example"""
        test_attempts = ["531", "278", "317"]
        dependencies = build_dependency_graph(test_attempts)
        result = topological_sort(dependencies)

        # Verify the result satisfies all attempts
        assert verify_passcode("".join(result), test_attempts)

        # Check specific ordering constraints
        assert result.index("5") < result.index("3")
        assert result.index("3") < result.index("1")
        assert result.index("2") < result.index("7")
        assert result.index("7") < result.index("8")
        assert result.index("3") < result.index("1")
        assert result.index("1") < result.index("7")

    def test_passcode_properties(self) -> None:
        """Test properties of the final passcode"""
        result = solve_naive()
        passcode_str = str(result)

        # Should be a reasonable length
        assert 3 <= len(passcode_str) <= 10

        # Should contain only unique digits for this specific problem
        assert len(set(passcode_str)) == len(passcode_str)

        # Should contain all digits that appear in the keylog
        attempts = load_keylog_data()
        all_digits_in_keylog: set[str] = set()
        for attempt in attempts:
            all_digits_in_keylog.update(attempt)

        for digit in all_digits_in_keylog:
            assert digit in passcode_str, f"Missing digit {digit} in passcode"


class TestComplexScenarios:
    """Test complex scenarios"""

    def test_with_custom_keylog(self) -> None:
        """Test with a custom simple keylog"""
        test_attempts = ["123", "456", "147"]
        dependencies = build_dependency_graph(test_attempts)

        # Should have dependencies: 1->2->3, 4->5->6, 1->4->7
        assert "2" in dependencies["1"]
        assert "3" in dependencies["2"]
        assert "5" in dependencies["4"]
        assert "6" in dependencies["5"]
        assert "4" in dependencies["1"]
        assert "7" in dependencies["4"]

        result = topological_sort(dependencies)
        assert verify_passcode("".join(result), test_attempts)

    def test_ordering_consistency(self) -> None:
        """Test that ordering is consistent across runs"""
        # Since we use lexicographic ordering for stability,
        # results should be consistent
        result1 = solve_naive()
        result2 = solve_naive()
        assert result1 == result2

        result3 = solve_mathematical()
        result4 = solve_mathematical()
        assert result3 == result4
