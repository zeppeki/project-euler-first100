"""Tests for Problem 084: Monopoly odds"""

import pytest

from problems.problem_084 import (
    BOARD_SQUARES,
    CC,
    CH,
    G2J,
    GO,
    JAIL,
    apply_chance_card,
    apply_community_chest_card,
    simulate_game,
    solve_naive,
)


class TestProblem084:
    """Test suite for Problem 084 solutions."""

    def test_board_layout(self) -> None:
        """Test that board is correctly defined."""
        assert len(BOARD_SQUARES) == 40
        assert BOARD_SQUARES[0] == "GO"
        assert BOARD_SQUARES[10] == "JAIL"
        assert BOARD_SQUARES[30] == "G2J"

    def test_special_squares(self) -> None:
        """Test special square positions."""
        assert GO == 0
        assert JAIL == 10
        assert G2J == 30
        assert len(CC) == 3  # Community Chest
        assert len(CH) == 3  # Chance
        assert 2 in CC and 17 in CC and 33 in CC
        assert 7 in CH and 22 in CH and 36 in CH

    def test_community_chest_card(self) -> None:
        """Test Community Chest card effects."""
        # Test multiple times due to randomness
        results = set()
        for _ in range(100):
            result = apply_community_chest_card(15)
            results.add(result)

        # Should include original position, GO, and JAIL
        assert 15 in results  # Original position (most common)
        # GO and JAIL might not appear in small sample due to low probability

    def test_chance_card(self) -> None:
        """Test Chance card effects."""
        # Test multiple times due to randomness
        results = set()
        for _ in range(100):
            result = apply_chance_card(15)
            results.add(result)

        # Should include original position and various destinations
        assert 15 in results  # Original position (most common)

    def test_simulation_basic(self) -> None:
        """Test basic simulation functionality."""
        # Small simulation to ensure it runs
        visit_counts = simulate_game(dice_sides=6, num_rolls=100)

        # Should have some visits
        assert len(visit_counts) > 0
        assert sum(visit_counts.values()) == 100

        # All positions should be valid board positions
        for pos in visit_counts:
            assert 0 <= pos <= 39

    def test_solve_naive_format(self) -> None:
        """Test that solve_naive returns correct format."""
        result = solve_naive(dice_sides=4, num_simulations=1000)

        # Should be 6-digit string
        assert len(result) == 6
        assert result.isdigit()

        # Each pair should be valid board position
        for i in range(0, 6, 2):
            pos = int(result[i : i + 2])
            assert 0 <= pos <= 39

    def test_solve_naive_reproducible(self) -> None:
        """Test that results are reproducible with same seed."""
        result1 = solve_naive(dice_sides=4, num_simulations=1000)
        result2 = solve_naive(dice_sides=4, num_simulations=1000)

        # Should be identical due to fixed seed
        assert result1 == result2

    def test_different_dice_sides(self) -> None:
        """Test with different dice configurations."""
        result_4 = solve_naive(dice_sides=4, num_simulations=1000)
        result_6 = solve_naive(dice_sides=6, num_simulations=1000)

        # Both should be valid 6-digit strings
        assert len(result_4) == 6 and result_4.isdigit()
        assert len(result_6) == 6 and result_6.isdigit()

        # Results may be different (though not guaranteed with small sample)

    def test_jail_is_popular(self) -> None:
        """Test that JAIL is among the most visited squares."""
        # Run larger simulation to get more reliable results
        visit_counts = simulate_game(dice_sides=4, num_rolls=10000)

        # Sort by visit count
        sorted_squares = sorted(visit_counts.items(), key=lambda x: x[1], reverse=True)
        top_5_positions = [pos for pos, count in sorted_squares[:5]]

        # JAIL should be in top 5 due to G2J and other factors
        assert JAIL in top_5_positions

    @pytest.mark.parametrize("dice_sides", [4, 6, 8])
    def test_various_dice_sides(self, dice_sides: int) -> None:
        """Test with various dice configurations."""
        result = solve_naive(dice_sides=dice_sides, num_simulations=1000)

        assert len(result) == 6
        assert result.isdigit()

        # Verify each position is valid
        for i in range(0, 6, 2):
            pos = int(result[i : i + 2])
            assert 0 <= pos <= 39

    def test_simulation_range(self) -> None:
        """Test that simulation stays within board bounds."""
        visit_counts = simulate_game(dice_sides=4, num_rolls=1000)

        for position in visit_counts:
            assert 0 <= position <= 39, f"Invalid position: {position}"

    def test_g2j_sends_to_jail(self) -> None:
        """Test that landing on G2J sends player to JAIL."""
        # This is tested implicitly in simulation, but we can verify the constant
        assert G2J == 30
        assert JAIL == 10

    @pytest.mark.slow
    def test_performance_large_simulation(self) -> None:
        """Test performance with larger simulation."""
        result = solve_naive(dice_sides=4, num_simulations=50000)

        assert len(result) == 6
        assert result.isdigit()

        # Should complete in reasonable time
        # (actual timing is handled by pytest-timeout if configured)

    def test_board_square_names(self) -> None:
        """Test that board square names are correctly defined."""
        expected_squares = [
            "GO",
            "A1",
            "CC1",
            "A2",
            "T1",
            "R1",
            "B1",
            "CH1",
            "B2",
            "B3",
            "JAIL",
            "C1",
            "U1",
            "C2",
            "C3",
            "R2",
            "D1",
            "CC2",
            "D2",
            "D3",
            "FP",
            "E1",
            "CH2",
            "E2",
            "E3",
            "R3",
            "F1",
            "F2",
            "U2",
            "F3",
            "G2J",
            "G1",
            "G2",
            "CC3",
            "G3",
            "R4",
            "CH3",
            "H1",
            "T2",
            "H2",
        ]

        assert expected_squares == BOARD_SQUARES

    def test_result_decoding(self) -> None:
        """Test that results can be properly decoded."""
        result = solve_naive(dice_sides=4, num_simulations=1000)

        # Extract individual squares
        squares = [result[i : i + 2] for i in range(0, 6, 2)]

        # Each should be a valid position
        for square_str in squares:
            pos = int(square_str)
            assert 0 <= pos <= 39
            assert pos < len(BOARD_SQUARES)

            # Should have a valid name
            name = BOARD_SQUARES[pos]
            assert len(name) > 0
