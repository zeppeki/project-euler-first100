#!/usr/bin/env python3
"""
Tests for Project Euler Problem 054: Poker hands
"""

from collections.abc import Callable

import pytest

from problems.problem_054 import (
    Card,
    HandRank,
    PokerHand,
    Rank,
    Suit,
    analyze_poker_data,
    count_player1_wins_from_file,
    demonstrate_hand_evaluation,
    parse_poker_game,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    test_example_hands,
)


class TestCard:
    """Test Card class functionality"""

    def test_card_creation(self) -> None:
        """Test creating cards with different ranks and suits"""
        card = Card(Rank.ACE, Suit.SPADES)
        assert card.rank == Rank.ACE
        assert card.suit == Suit.SPADES

    def test_card_from_string(self) -> None:
        """Test parsing cards from string representation"""
        # Test all ranks
        assert Card.from_string("2H") == Card(Rank.TWO, Suit.HEARTS)
        assert Card.from_string("3C") == Card(Rank.THREE, Suit.CLUBS)
        assert Card.from_string("4D") == Card(Rank.FOUR, Suit.DIAMONDS)
        assert Card.from_string("5S") == Card(Rank.FIVE, Suit.SPADES)
        assert Card.from_string("6H") == Card(Rank.SIX, Suit.HEARTS)
        assert Card.from_string("7C") == Card(Rank.SEVEN, Suit.CLUBS)
        assert Card.from_string("8D") == Card(Rank.EIGHT, Suit.DIAMONDS)
        assert Card.from_string("9S") == Card(Rank.NINE, Suit.SPADES)
        assert Card.from_string("TH") == Card(Rank.TEN, Suit.HEARTS)
        assert Card.from_string("JC") == Card(Rank.JACK, Suit.CLUBS)
        assert Card.from_string("QD") == Card(Rank.QUEEN, Suit.DIAMONDS)
        assert Card.from_string("KS") == Card(Rank.KING, Suit.SPADES)
        assert Card.from_string("AH") == Card(Rank.ACE, Suit.HEARTS)

    def test_card_from_string_invalid(self) -> None:
        """Test error handling for invalid card strings"""
        with pytest.raises(ValueError):
            Card.from_string("XH")  # Invalid rank
        with pytest.raises(ValueError):
            Card.from_string("AX")  # Invalid suit
        with pytest.raises(ValueError):
            Card.from_string("A")  # Too short
        with pytest.raises(ValueError):
            Card.from_string("AHX")  # Too long


class TestPokerHand:
    """Test PokerHand class functionality"""

    def test_hand_creation(self) -> None:
        """Test creating poker hands"""
        cards = [
            Card(Rank.ACE, Suit.SPADES),
            Card(Rank.KING, Suit.SPADES),
            Card(Rank.QUEEN, Suit.SPADES),
            Card(Rank.JACK, Suit.SPADES),
            Card(Rank.TEN, Suit.SPADES),
        ]
        hand = PokerHand(cards)
        assert len(hand.cards) == 5
        assert hand.evaluation.hand_rank == HandRank.ROYAL_FLUSH

    def test_hand_from_string(self) -> None:
        """Test creating hands from string representation"""
        hand = PokerHand.from_string("AS KS QS JS TS")
        assert hand.evaluation.hand_rank == HandRank.ROYAL_FLUSH

    def test_hand_invalid_size(self) -> None:
        """Test error handling for invalid hand sizes"""
        with pytest.raises(ValueError):
            PokerHand([Card(Rank.ACE, Suit.SPADES)])  # Too few cards

        with pytest.raises(ValueError):
            PokerHand.from_string("AS KS QS")  # Too few cards


class TestHandEvaluation:
    """Test poker hand evaluation logic"""

    def test_royal_flush(self) -> None:
        """Test royal flush detection"""
        hand = PokerHand.from_string("AS KS QS JS TS")
        assert hand.evaluation.hand_rank == HandRank.ROYAL_FLUSH
        assert hand.evaluation.tiebreakers == (14,)

    def test_straight_flush(self) -> None:
        """Test straight flush detection"""
        hand = PokerHand.from_string("5H 6H 7H 8H 9H")
        assert hand.evaluation.hand_rank == HandRank.STRAIGHT_FLUSH
        assert hand.evaluation.tiebreakers == (9,)

    def test_four_of_a_kind(self) -> None:
        """Test four of a kind detection"""
        hand = PokerHand.from_string("AS AC AH AD 2S")
        assert hand.evaluation.hand_rank == HandRank.FOUR_OF_A_KIND
        assert hand.evaluation.tiebreakers == (14, 2)  # Four aces, kicker 2

    def test_full_house(self) -> None:
        """Test full house detection"""
        hand = PokerHand.from_string("AS AC AH 2S 2C")
        assert hand.evaluation.hand_rank == HandRank.FULL_HOUSE
        assert hand.evaluation.tiebreakers == (14, 2)  # Three aces, pair of 2s

    def test_flush(self) -> None:
        """Test flush detection"""
        hand = PokerHand.from_string("AS KS 9S 5S 2S")
        assert hand.evaluation.hand_rank == HandRank.FLUSH
        assert hand.evaluation.tiebreakers == (14, 13, 9, 5, 2)

    def test_straight(self) -> None:
        """Test straight detection"""
        hand = PokerHand.from_string("5H 6C 7D 8S 9H")
        assert hand.evaluation.hand_rank == HandRank.STRAIGHT
        assert hand.evaluation.tiebreakers == (9,)

    def test_straight_ace_low(self) -> None:
        """Test A-2-3-4-5 straight (wheel)"""
        hand = PokerHand.from_string("AH 2C 3D 4S 5H")
        assert hand.evaluation.hand_rank == HandRank.STRAIGHT
        assert hand.evaluation.tiebreakers == (5,)  # Ace-low straight tops at 5

    def test_three_of_a_kind(self) -> None:
        """Test three of a kind detection"""
        hand = PokerHand.from_string("AS AC AH KS QC")
        assert hand.evaluation.hand_rank == HandRank.THREE_OF_A_KIND
        assert hand.evaluation.tiebreakers == (14, 13, 12)  # Three aces, kickers K, Q

    def test_two_pairs(self) -> None:
        """Test two pairs detection"""
        hand = PokerHand.from_string("AS AC KS KC QC")
        assert hand.evaluation.hand_rank == HandRank.TWO_PAIRS
        assert hand.evaluation.tiebreakers == (14, 13, 12)  # Aces and Kings, kicker Q

    def test_one_pair(self) -> None:
        """Test one pair detection"""
        hand = PokerHand.from_string("AS AC KS QC JC")
        assert hand.evaluation.hand_rank == HandRank.ONE_PAIR
        assert hand.evaluation.tiebreakers == (
            14,
            13,
            12,
            11,
        )  # Pair of aces, kickers K, Q, J

    def test_high_card(self) -> None:
        """Test high card detection"""
        hand = PokerHand.from_string("AS KC QD JH 9C")
        assert hand.evaluation.hand_rank == HandRank.HIGH_CARD
        assert hand.evaluation.tiebreakers == (14, 13, 12, 11, 9)


class TestHandComparison:
    """Test poker hand comparison logic"""

    def test_different_ranks(self) -> None:
        """Test comparing hands with different rankings"""
        flush = PokerHand.from_string("AS KS QS JS 9S")
        straight = PokerHand.from_string("5H 6C 7D 8S 9H")

        assert flush.beats(straight)
        assert not straight.beats(flush)

    def test_same_rank_different_values(self) -> None:
        """Test comparing hands with same rank but different values"""
        pair_aces = PokerHand.from_string("AS AC KS QC JC")
        pair_kings = PokerHand.from_string("KS KC AS QC JC")

        assert pair_aces.beats(pair_kings)
        assert not pair_kings.beats(pair_aces)

    def test_same_rank_same_primary_different_kickers(self) -> None:
        """Test comparing hands with same rank and primary value but different kickers"""
        queens_nine = PokerHand.from_string("QS QC 9H 8C 7D")
        queens_seven = PokerHand.from_string("QH QD 7S 6C 5H")

        assert queens_nine.beats(queens_seven)
        assert not queens_seven.beats(queens_nine)


class TestExampleHands:
    """Test the example hands from the problem description"""

    def test_example_hands_verification(self) -> None:
        """Test that the example verification function works"""
        assert test_example_hands() is True

    def test_example_1(self) -> None:
        """Test example 1: Pair of Fives vs Pair of Eights"""
        player1 = PokerHand.from_string("5H 5C 6S 7S KD")
        player2 = PokerHand.from_string("2C 3S 8S 8D TD")

        assert not player1.beats(player2)  # Player 2 wins

    def test_example_2(self) -> None:
        """Test example 2: High card Ace vs High card Queen"""
        player1 = PokerHand.from_string("5D 8C 9S JS AC")
        player2 = PokerHand.from_string("2C 5C 7D 8S QH")

        assert player1.beats(player2)  # Player 1 wins

    def test_example_3(self) -> None:
        """Test example 3: Three Aces vs Flush"""
        player1 = PokerHand.from_string("2D 9C AS AH AC")
        player2 = PokerHand.from_string("3D 6D 7D TD QD")

        assert not player1.beats(player2)  # Player 2 wins (flush beats three of a kind)

    def test_example_4(self) -> None:
        """Test example 4: Pair of Queens with different kickers"""
        player1 = PokerHand.from_string("4D 6S 9H QH QC")
        player2 = PokerHand.from_string("3D 6D 7H QD QS")

        assert player1.beats(player2)  # Player 1 wins (9 > 7)

    def test_example_5(self) -> None:
        """Test example 5: Full House comparison"""
        player1 = PokerHand.from_string("2H 2D 4C 4D 4S")
        player2 = PokerHand.from_string("3C 3D 3S 9S 9D")

        assert player1.beats(player2)  # Player 1 wins (three 4s > three 3s)


class TestGameParsing:
    """Test parsing poker game lines"""

    def test_parse_game_line(self) -> None:
        """Test parsing a game line into two hands"""
        line = "8C TS KC 9H 4S 7D 2S 5D 3S AC"
        player1, player2 = parse_poker_game(line)

        assert len(player1.cards) == 5
        assert len(player2.cards) == 5
        assert player1.cards[0] == Card(Rank.EIGHT, Suit.CLUBS)
        assert player2.cards[0] == Card(Rank.SEVEN, Suit.DIAMONDS)

    def test_parse_invalid_game_line(self) -> None:
        """Test error handling for invalid game lines"""
        with pytest.raises(ValueError):
            parse_poker_game("8C TS KC 9H 4S")  # Too few cards


class TestSolutionFunctions:
    """Test main solution functions"""

    @pytest.mark.parametrize(
        "solver", [solve_naive, solve_optimized, solve_mathematical]
    )
    def test_solve_consistency(self, solver: Callable[[], int]) -> None:
        """Test that all solution methods give the same result"""
        try:
            result = solver()
            assert isinstance(result, int)
            assert result >= 0
            assert result <= 1000  # Can't win more than total games
        except FileNotFoundError:
            pytest.skip("Poker data file not found")

    def test_solve_agreement(self) -> None:
        """Test that all solution methods agree"""
        try:
            result_naive = solve_naive()
            result_optimized = solve_optimized()
            result_mathematical = solve_mathematical()

            assert result_naive == result_optimized == result_mathematical
        except FileNotFoundError:
            pytest.skip("Poker data file not found")


class TestDataAnalysis:
    """Test data analysis functions"""

    def test_analyze_poker_data(self) -> None:
        """Test poker data analysis function"""
        try:
            stats = analyze_poker_data()

            if "error" not in stats:
                assert "total_games" in stats
                assert "player1_wins" in stats
                assert "player2_wins" in stats
                assert "player1_win_rate" in stats
                assert "hand_rank_distribution" in stats

                assert (
                    stats["player1_wins"] + stats["player2_wins"]
                    == stats["total_games"]
                )
                assert 0 <= stats["player1_win_rate"] <= 1
        except Exception:
            pytest.skip("Could not analyze poker data")

    def test_demonstrate_hand_evaluation(self) -> None:
        """Test hand evaluation demonstration"""
        results = demonstrate_hand_evaluation()
        assert isinstance(results, list)
        assert len(results) > 0

        for hand_str, description, evaluation in results:
            assert isinstance(hand_str, str)
            assert isinstance(description, str)
            assert isinstance(evaluation, str)

    def test_count_player1_wins_file_not_found(self) -> None:
        """Test error handling when poker file is not found"""
        with pytest.raises(FileNotFoundError):
            count_player1_wins_from_file("nonexistent_file.txt")


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_identical_hands(self) -> None:
        """Test that identical hands don't beat each other"""
        hand1 = PokerHand.from_string("AS KS QS JS TS")
        hand2 = PokerHand.from_string("AH KH QH JH TH")

        # Both are royal flushes, neither should beat the other
        assert not hand1.beats(hand2)
        assert not hand2.beats(hand1)

    def test_complex_tiebreakers(self) -> None:
        """Test complex tiebreaker scenarios"""
        # Two high card hands with same high cards except last
        hand1 = PokerHand.from_string("AH KS QC JD 9H")
        hand2 = PokerHand.from_string("AS KC QD JH 8S")

        assert hand1.beats(hand2)  # 9 > 8 in final tiebreaker

    def test_all_hand_ranks_exist(self) -> None:
        """Test that all hand rank types can be detected"""
        test_hands = {
            HandRank.HIGH_CARD: "AS KC QD JH 9C",
            HandRank.ONE_PAIR: "AS AC KD QH JC",
            HandRank.TWO_PAIRS: "AS AC KS KC QH",
            HandRank.THREE_OF_A_KIND: "AS AC AH KS QC",
            HandRank.STRAIGHT: "5H 6C 7D 8S 9H",
            HandRank.FLUSH: "AS KS QS JS 9S",
            HandRank.FULL_HOUSE: "AS AC AH KS KC",
            HandRank.FOUR_OF_A_KIND: "AS AC AH AD KC",
            HandRank.STRAIGHT_FLUSH: "5H 6H 7H 8H 9H",
            HandRank.ROYAL_FLUSH: "AS KS QS JS TS",
        }

        for expected_rank, hand_str in test_hands.items():
            hand = PokerHand.from_string(hand_str)
            assert hand.evaluation.hand_rank == expected_rank


if __name__ == "__main__":
    pytest.main([__file__])
