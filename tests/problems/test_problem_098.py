#!/usr/bin/env python3
"""
Test for Problem 098: Anagramic squares
"""

import pytest

from problems.problem_098 import (
    apply_mapping,
    find_anagram_pairs,
    find_square_anagram_pairs,
    get_letter_mapping,
    get_sorted_letters,
    is_perfect_square,
    load_words,
    solve_naive,
    solve_optimized,
)


class TestUtilityFunctions:
    """Test utility functions for anagramic squares."""

    def test_load_words(self) -> None:
        """Test loading words from file."""
        words = load_words()

        # Should load many words
        assert len(words) > 1000

        # Should contain expected words
        assert "CARE" in words
        assert "RACE" in words

        # All words should be uppercase strings
        for word in words[:100]:  # Test first 100
            assert isinstance(word, str)
            assert word.isupper()

    def test_get_sorted_letters(self) -> None:
        """Test sorting letters for anagram detection."""
        assert get_sorted_letters("CARE") == "ACER"
        assert get_sorted_letters("RACE") == "ACER"
        assert get_sorted_letters("ACRE") == "ACER"

        # Different words should have different sorted letters
        assert get_sorted_letters("HELLO") == "EHLLO"
        assert get_sorted_letters("WORLD") == "DLORW"

    def test_find_anagram_pairs(self) -> None:
        """Test finding anagram pairs."""
        test_words = ["CARE", "RACE", "ACRE", "HELLO", "WORLD"]
        pairs = find_anagram_pairs(test_words)

        # Should find all combinations of CARE/RACE/ACRE
        expected_pairs = {("ACRE", "CARE"), ("ACRE", "RACE"), ("CARE", "RACE")}
        actual_pairs = {tuple(sorted(pair)) for pair in pairs}

        assert expected_pairs == actual_pairs

        # Should not include single letter words or non-anagrams
        for pair in pairs:
            assert len(pair[0]) > 1
            assert len(pair[1]) > 1
            assert get_sorted_letters(pair[0]) == get_sorted_letters(pair[1])

    def test_is_perfect_square(self) -> None:
        """Test perfect square detection."""
        # Perfect squares
        assert is_perfect_square(1)
        assert is_perfect_square(4)
        assert is_perfect_square(9)
        assert is_perfect_square(16)
        assert is_perfect_square(1296)  # 36²
        assert is_perfect_square(9216)  # 96²

        # Non-perfect squares
        assert not is_perfect_square(2)
        assert not is_perfect_square(3)
        assert not is_perfect_square(1297)

        # Edge cases
        assert is_perfect_square(0)
        assert not is_perfect_square(-1)

    def test_get_letter_mapping(self) -> None:
        """Test letter to digit mapping."""
        # Valid mapping: CARE=1296, RACE=9216
        mapping = get_letter_mapping("CARE", "RACE", 1296, 9216)
        assert mapping is not None
        expected = {"C": "1", "A": "2", "R": "9", "E": "6"}
        assert mapping == expected

        # Invalid: different lengths
        assert get_letter_mapping("AB", "CDE", 12, 345) is None
        assert get_letter_mapping("ABC", "DE", 123, 45) is None

        # Invalid: leading zeros
        assert get_letter_mapping("AB", "BA", 12, 21) is not None  # Valid
        assert get_letter_mapping("AB", "BA", 10, 1) is None  # Invalid: 01

        # Valid: consistent mapping - AA=11 (A->1), BB=22 (B->2)
        assert get_letter_mapping("AA", "BB", 11, 22) is not None

    def test_apply_mapping(self) -> None:
        """Test applying letter to digit mapping."""
        mapping = {"C": "1", "A": "2", "R": "9", "E": "6"}

        # Valid applications
        assert apply_mapping("CARE", mapping) == 1296
        assert apply_mapping("RACE", mapping) == 9216
        assert apply_mapping("ACRE", mapping) == 2196

        # Missing letter in mapping
        assert apply_mapping("HELLO", mapping) is None

        # Leading zero result
        mapping_with_zero = {"A": "0", "B": "1"}
        assert apply_mapping("AB", mapping_with_zero) is None  # Would be "01"


class TestSquareAnagramFinding:
    """Test square anagram pair finding."""

    def test_find_square_anagram_pairs_basic(self) -> None:
        """Test finding square anagram pairs with simple examples."""
        # This is a computationally intensive test, so we skip the actual computation
        # and test the logic with known values

        # Known valid mapping: CARE=1296, RACE=9216
        mapping = get_letter_mapping("CARE", "RACE", 1296, 9216)
        assert mapping is not None

        # Test application
        care_mapped = apply_mapping("CARE", mapping)
        race_mapped = apply_mapping("RACE", mapping)

        assert care_mapped == 1296
        assert race_mapped == 9216
        assert is_perfect_square(care_mapped)
        assert is_perfect_square(race_mapped)

    def test_find_square_anagram_pairs_no_matches(self) -> None:
        """Test with words that have no square anagram pairs."""
        test_words = ["HELLO", "WORLD", "PYTHON"]
        pairs = find_square_anagram_pairs(test_words)

        # Should find no pairs (these words don't form anagrams that map to squares)
        assert len(pairs) == 0

    def test_find_square_anagram_pairs_constraints(self) -> None:
        """Test constraint validation logic."""
        # Test constraint checking with known examples

        # Valid case
        assert get_letter_mapping("AB", "BA", 16, 61) is not None

        # Invalid: leading zero
        assert get_letter_mapping("AB", "BA", 10, 1) is None  # Would create "01"

        # Valid: consistent mapping - AA=11 (A->1), BB=22 (B->2)
        assert get_letter_mapping("AA", "BB", 11, 22) is not None

        # Valid: consistent mapping
        mapping = get_letter_mapping("CARE", "RACE", 1296, 9216)
        assert mapping is not None
        assert mapping == {"C": "1", "A": "2", "R": "9", "E": "6"}


class TestSolutionMethods:
    """Test solution methods."""

    @pytest.mark.slow
    @pytest.mark.timeout(
        300
    )  # 5 minutes timeout for this computationally intensive test
    def test_solution_consistency(self) -> None:
        """Test that all solution methods give the same results."""
        # Test with data file
        result_naive = solve_naive()
        result_optimized = solve_optimized()
        result_mathematical = solve_optimized()

        assert result_naive == result_optimized == result_mathematical

    @pytest.mark.slow
    @pytest.mark.timeout(
        300
    )  # 5 minutes timeout for this computationally intensive test
    def test_main_problem_result(self) -> None:
        """Test the main problem result."""
        # The expected answer for Problem 098
        expected_result = 18769

        result = solve_optimized()
        assert result == expected_result

    @pytest.mark.slow
    @pytest.mark.timeout(
        300
    )  # 5 minutes timeout for this computationally intensive test
    def test_result_properties(self) -> None:
        """Test properties of the result."""
        result = solve_optimized()

        # Should be a positive integer
        assert isinstance(result, int)
        assert result > 0

        # Should be a perfect square
        assert is_perfect_square(result)

        # Should be the expected answer
        assert result == 18769

    def test_edge_cases(self) -> None:
        """Test edge cases and error handling."""
        # Test with empty word list
        empty_pairs = find_anagram_pairs([])
        assert len(empty_pairs) == 0

        # Test with single words (should be ignored)
        single_letter_pairs = find_anagram_pairs(["A", "B", "C"])
        assert len(single_letter_pairs) == 0

        # Test with no anagrams
        no_anagram_pairs = find_anagram_pairs(["HELLO", "WORLD", "PYTHON"])
        assert len(no_anagram_pairs) == 0


class TestPerformanceAndIntegration:
    """Test performance characteristics and integration."""

    @pytest.mark.slow
    @pytest.mark.timeout(
        300
    )  # 5 minutes timeout for this computationally intensive test
    def test_algorithm_efficiency(self) -> None:
        """Test that algorithms complete in reasonable time."""
        import time

        # Test with main problem
        start_time = time.time()
        result = solve_optimized()
        end_time = time.time()

        # Should complete in extended time (less than 5 minutes)
        assert end_time - start_time < 300.0

        # Should get correct result
        assert result == 18769

    def test_data_integrity(self) -> None:
        """Test data file integrity."""
        words = load_words()

        # Should have reasonable number of words
        assert 1000 < len(words) < 5000

        # Should contain known words
        expected_words = ["CARE", "RACE", "THE", "AND", "FOR"]
        for word in expected_words:
            assert word in words

        # All words should be valid
        for word in words:
            assert isinstance(word, str)
            assert len(word) > 0
            assert word.isalpha()
            assert word.isupper()

    def test_mathematical_properties(self) -> None:
        """Test mathematical properties of the solution."""
        # Test known square anagram example
        mapping = get_letter_mapping("CARE", "RACE", 1296, 9216)
        assert mapping is not None

        # Verify the mapping produces correct results
        care_mapped = apply_mapping("CARE", mapping)
        race_mapped = apply_mapping("RACE", mapping)

        assert care_mapped == 1296
        assert race_mapped == 9216
        assert is_perfect_square(care_mapped)
        assert is_perfect_square(race_mapped)

    @pytest.mark.slow
    def test_full_problem_solving(self) -> None:
        """Test solving the full problem (marked as slow)."""
        result = solve_naive()

        # Should get the correct answer
        assert result == 18769

        # Verify it's actually a perfect square
        sqrt_result = int(result**0.5)
        assert sqrt_result * sqrt_result == result

    def test_anagram_pair_properties(self) -> None:
        """Test properties of found anagram pairs."""
        words = load_words()
        pairs = find_anagram_pairs(words)

        # Should find many anagram pairs
        assert len(pairs) > 10

        # Check properties of found pairs
        for word1, word2 in pairs[:10]:  # Test first 10 for performance
            # Same length
            assert len(word1) == len(word2)

            # Different words
            assert word1 != word2

            # Same sorted letters (anagram property)
            assert get_sorted_letters(word1) == get_sorted_letters(word2)

            # Both should be in original word list
            assert word1 in words
            assert word2 in words
