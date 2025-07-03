#!/usr/bin/env python3
"""
Project Euler Problem 054: Poker hands

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens, then highest
cards in each hand are compared (see example 4 below); if the highest cards tie
then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
        2C 3S 8S 8D TD
Pair of Eights
        Player 2
2	 	5D 8C 9S JS AC
High card Ace
        2C 5C 7D 8S QH
High card Queen
        Player 1
3	 	2D 9C AS AH AC
Three Aces
        3D 6D 7D TD QD
Flush with Diamonds
        Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
        3D 6D 7H QD QS
Pair of Queens
Highest card Seven
        Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
        3C 3D 3S 9S 9D
Full House
with Three Threes
        Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the first
five are Player 1's cards and the last five are Player 2's cards. You can assume
that all hands are valid (no invalid characters or repeated cards), each player's
hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

from collections import Counter
from enum import IntEnum
from pathlib import Path
from typing import Any, NamedTuple


class Suit(IntEnum):
    """Card suits"""

    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class Rank(IntEnum):
    """Card ranks in ascending order"""

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class HandRank(IntEnum):
    """Poker hand rankings from lowest to highest"""

    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10


class Card(NamedTuple):
    """Represents a playing card"""

    rank: Rank
    suit: Suit

    @classmethod
    def from_string(cls, card_str: str) -> "Card":
        """Parse card from string representation like '5H' or 'TC'"""
        if len(card_str) != 2:
            raise ValueError(f"Invalid card string: {card_str}")

        rank_char, suit_char = card_str[0], card_str[1]

        # Parse rank
        rank_mapping = {
            "2": Rank.TWO,
            "3": Rank.THREE,
            "4": Rank.FOUR,
            "5": Rank.FIVE,
            "6": Rank.SIX,
            "7": Rank.SEVEN,
            "8": Rank.EIGHT,
            "9": Rank.NINE,
            "T": Rank.TEN,
            "J": Rank.JACK,
            "Q": Rank.QUEEN,
            "K": Rank.KING,
            "A": Rank.ACE,
        }

        # Parse suit
        suit_mapping = {
            "C": Suit.CLUBS,
            "D": Suit.DIAMONDS,
            "H": Suit.HEARTS,
            "S": Suit.SPADES,
        }

        if rank_char not in rank_mapping:
            raise ValueError(f"Invalid rank: {rank_char}")
        if suit_char not in suit_mapping:
            raise ValueError(f"Invalid suit: {suit_char}")

        return cls(rank_mapping[rank_char], suit_mapping[suit_char])


class HandEvaluation(NamedTuple):
    """Result of evaluating a poker hand"""

    hand_rank: HandRank
    tiebreakers: tuple[int, ...]  # Values for breaking ties in descending order


class PokerHand:
    """Represents a poker hand with evaluation capabilities"""

    def __init__(self, cards: list[Card]) -> None:
        if len(cards) != 5:
            raise ValueError("Poker hand must have exactly 5 cards")
        self.cards = cards
        self.evaluation = self._evaluate_hand()

    def _evaluate_hand(self) -> HandEvaluation:
        """Evaluate the poker hand and return its ranking and tiebreakers"""
        ranks = [card.rank for card in self.cards]
        suits = [card.suit for card in self.cards]

        rank_counts = Counter(ranks)
        is_flush = len(set(suits)) == 1

        # Check for straight
        sorted_ranks = sorted(ranks)
        is_straight = all(sorted_ranks[i] + 1 == sorted_ranks[i + 1] for i in range(4))

        # Special case: A-2-3-4-5 straight (wheel)
        if sorted_ranks == [Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.ACE]:
            is_straight = True
            # For ace-low straight, treat ace as 1 for max calculation
            sorted_ranks_int = [1, 2, 3, 4, 5]
        else:
            sorted_ranks_int = [int(rank) for rank in sorted_ranks]

        # Get count patterns
        count_values = sorted(rank_counts.values(), reverse=True)

        # Royal flush: A, K, Q, J, 10 all same suit
        if is_flush and sorted_ranks == [
            Rank.TEN,
            Rank.JACK,
            Rank.QUEEN,
            Rank.KING,
            Rank.ACE,
        ]:
            return HandEvaluation(HandRank.ROYAL_FLUSH, (14,))

        # Straight flush
        if is_flush and is_straight:
            return HandEvaluation(HandRank.STRAIGHT_FLUSH, (max(sorted_ranks_int),))

        # Four of a kind
        if count_values == [4, 1]:
            four_rank = next(rank for rank, count in rank_counts.items() if count == 4)
            kicker = next(rank for rank, count in rank_counts.items() if count == 1)
            return HandEvaluation(HandRank.FOUR_OF_A_KIND, (four_rank, kicker))

        # Full house
        if count_values == [3, 2]:
            three_rank = next(rank for rank, count in rank_counts.items() if count == 3)
            pair_rank = next(rank for rank, count in rank_counts.items() if count == 2)
            return HandEvaluation(HandRank.FULL_HOUSE, (three_rank, pair_rank))

        # Flush
        if is_flush:
            return HandEvaluation(HandRank.FLUSH, tuple(sorted(ranks, reverse=True)))

        # Straight
        if is_straight:
            return HandEvaluation(HandRank.STRAIGHT, (max(sorted_ranks_int),))

        # Three of a kind
        if count_values == [3, 1, 1]:
            three_rank = next(rank for rank, count in rank_counts.items() if count == 3)
            kickers = sorted(
                [rank for rank, count in rank_counts.items() if count == 1],
                reverse=True,
            )
            return HandEvaluation(HandRank.THREE_OF_A_KIND, (three_rank, *kickers))

        # Two pairs
        if count_values == [2, 2, 1]:
            pairs = sorted(
                [rank for rank, count in rank_counts.items() if count == 2],
                reverse=True,
            )
            kicker = next(rank for rank, count in rank_counts.items() if count == 1)
            return HandEvaluation(HandRank.TWO_PAIRS, (*pairs, kicker))

        # One pair
        if count_values == [2, 1, 1, 1]:
            pair_rank = next(rank for rank, count in rank_counts.items() if count == 2)
            kickers = sorted(
                [rank for rank, count in rank_counts.items() if count == 1],
                reverse=True,
            )
            return HandEvaluation(HandRank.ONE_PAIR, (pair_rank, *kickers))

        # High card
        return HandEvaluation(HandRank.HIGH_CARD, tuple(sorted(ranks, reverse=True)))

    def beats(self, other: "PokerHand") -> bool:
        """Check if this hand beats another hand"""
        # First compare hand rankings
        if self.evaluation.hand_rank != other.evaluation.hand_rank:
            return self.evaluation.hand_rank > other.evaluation.hand_rank

        # If same hand rank, compare tiebreakers
        return self.evaluation.tiebreakers > other.evaluation.tiebreakers

    @classmethod
    def from_string(cls, hand_str: str) -> "PokerHand":
        """Create hand from string of cards like '5H 5C 6S 7S KD'"""
        card_strings = hand_str.strip().split()
        if len(card_strings) != 5:
            raise ValueError(f"Hand must have exactly 5 cards, got {len(card_strings)}")

        cards = [Card.from_string(card_str) for card_str in card_strings]
        return cls(cards)


def parse_poker_game(line: str) -> tuple[PokerHand, PokerHand]:
    """Parse a line from poker file into two hands"""
    cards = line.strip().split()
    if len(cards) != 10:
        raise ValueError(f"Game line must have exactly 10 cards, got {len(cards)}")

    player1_cards = [Card.from_string(card) for card in cards[:5]]
    player2_cards = [Card.from_string(card) for card in cards[5:]]

    return PokerHand(player1_cards), PokerHand(player2_cards)


def count_player1_wins_from_file(filename: str) -> int:
    """Count how many hands Player 1 wins from poker file"""
    poker_file = Path(__file__).parent.parent / "data" / filename

    if not poker_file.exists():
        raise FileNotFoundError(f"Poker file not found: {poker_file}")

    player1_wins = 0

    with open(poker_file, encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            if not line.strip():
                continue

            try:
                player1_hand, player2_hand = parse_poker_game(line)
                if player1_hand.beats(player2_hand):
                    player1_wins += 1
            except Exception as e:
                raise ValueError(
                    f"Error parsing line {line_num}: {line.strip()}"
                ) from e

    return player1_wins


def solve_naive() -> int:
    """
    素直な解法: ポーカーハンドを直接評価してPlayer 1の勝利数を数える
    時間計算量: O(n)
    空間計算量: O(1)
    """
    return count_player1_wins_from_file("p054_poker.txt")


def solve_optimized() -> int:
    """
    最適化解法: より効率的なハンド評価（実際には同じアルゴリズム）
    時間計算量: O(n)
    空間計算量: O(1)
    """
    return count_player1_wins_from_file("p054_poker.txt")


def solve_mathematical() -> int:
    """
    数学的解法: ポーカーハンド評価の数学的最適化（実装では同じ）
    時間計算量: O(n)
    空間計算量: O(1)
    """
    return count_player1_wins_from_file("p054_poker.txt")


def analyze_poker_data(filename: str = "p054_poker.txt") -> dict[str, Any]:
    """Analyze the poker data file and return statistics"""
    poker_file = Path(__file__).parent.parent / "data" / filename

    if not poker_file.exists():
        return {"error": f"File not found: {poker_file}"}

    player1_wins = 0
    player2_wins = 0
    hand_rank_stats = {rank.name: {"player1": 0, "player2": 0} for rank in HandRank}

    with open(poker_file, encoding="utf-8") as f:
        lines = list(f)

    for line in lines:
        if not line.strip():
            continue

        player1_hand, player2_hand = parse_poker_game(line)

        # Count wins
        if player1_hand.beats(player2_hand):
            player1_wins += 1
        else:
            player2_wins += 1

        # Count hand rankings
        hand_rank_stats[player1_hand.evaluation.hand_rank.name]["player1"] += 1
        hand_rank_stats[player2_hand.evaluation.hand_rank.name]["player2"] += 1

    return {
        "total_games": len(lines),
        "player1_wins": player1_wins,
        "player2_wins": player2_wins,
        "player1_win_rate": player1_wins / len(lines),
        "hand_rank_distribution": hand_rank_stats,
    }


def demonstrate_hand_evaluation() -> list[tuple[str, str, str]]:
    """Demonstrate hand evaluation with examples"""
    examples = [
        ("5H 5C 6S 7S KD", "Pair of Fives"),
        ("2C 3S 8S 8D TD", "Pair of Eights"),
        ("5D 8C 9S JS AC", "High Card Ace"),
        ("2C 5C 7D 8S QH", "High Card Queen"),
        ("2D 9C AS AH AC", "Three Aces"),
        ("3D 6D 7D TD QD", "Flush with Diamonds"),
        ("4D 6S 9H QH QC", "Pair of Queens"),
        ("3D 6D 7H QD QS", "Pair of Queens"),
        ("2H 2D 4C 4D 4S", "Full House with Three Fours"),
        ("3C 3D 3S 9S 9D", "Full House with Three Threes"),
        ("TC JC QC KC AC", "Royal Flush"),
        ("5H 6H 7H 8H 9H", "Straight Flush"),
    ]

    results = []
    for hand_str, description in examples:
        hand = PokerHand.from_string(hand_str)
        rank_name = hand.evaluation.hand_rank.name.replace("_", " ").title()
        tiebreakers = ", ".join(map(str, hand.evaluation.tiebreakers))
        results.append((hand_str, description, f"{rank_name} ({tiebreakers})"))

    return results


def test_example_hands() -> bool:
    """Test the example hands from the problem description"""
    examples = [
        ("5H 5C 6S 7S KD", "2C 3S 8S 8D TD", False),  # Player 2 wins
        ("5D 8C 9S JS AC", "2C 5C 7D 8S QH", True),  # Player 1 wins
        ("2D 9C AS AH AC", "3D 6D 7D TD QD", False),  # Player 2 wins
        ("4D 6S 9H QH QC", "3D 6D 7H QD QS", True),  # Player 1 wins
        ("2H 2D 4C 4D 4S", "3C 3D 3S 9S 9D", True),  # Player 1 wins
    ]

    all_correct = True
    for player1_str, player2_str, expected_player1_wins in examples:
        player1_hand = PokerHand.from_string(player1_str)
        player2_hand = PokerHand.from_string(player2_str)
        actual_player1_wins = player1_hand.beats(player2_hand)

        if actual_player1_wins != expected_player1_wins:
            print(f"Test failed: {player1_str} vs {player2_str}")
            print(f"Expected Player 1 wins: {expected_player1_wins}")
            print(f"Actual Player 1 wins: {actual_player1_wins}")
            all_correct = False

    return all_correct
