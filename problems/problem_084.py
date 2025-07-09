"""
Problem 84: Monopoly odds

In the game of Monopoly, players move around the board according to the roll of two 6-sided dice.
Without any further rules we would expect to visit each square with equal probability: 2.5%.
However, landing on G2J (Go To Jail), CC (Community Chest), and CH (Chance) changes this distribution.

The standard board has squares numbered from 00 to 39 and is arranged as follows:
GO, A1, CC1, A2, T1, R1, B1, CH1, B2, B3, JAIL,
C1, U1, C2, C3, R2, D1, CC2, D2, D3, FP,
E1, CH2, E2, E3, R3, F1, F2, U2, F3, G2J,
G1, G2, CC3, G3, R4, CH3, H1, T2, H2

What are the three most likely squares to be visited?

日本語：
モノポリーゲームにおいて、2つのサイコロを使用したときの各マスの到達確率を計算し、
最も訪問頻度の高い3つのマスを求めます。4面ダイスを使用した場合を考えます。
"""

import random
from collections import defaultdict

# Board layout (0-39)
BOARD_SQUARES = [
    "GO",
    "A1",
    "CC1",
    "A2",
    "T1",
    "R1",
    "B1",
    "CH1",
    "B2",
    "B3",  # 0-9
    "JAIL",
    "C1",
    "U1",
    "C2",
    "C3",
    "R2",
    "D1",
    "CC2",
    "D2",
    "D3",  # 10-19
    "FP",
    "E1",
    "CH2",
    "E2",
    "E3",
    "R3",
    "F1",
    "F2",
    "U2",
    "F3",  # 20-29
    "G2J",
    "G1",
    "G2",
    "CC3",
    "G3",
    "R4",
    "CH3",
    "H1",
    "T2",
    "H2",  # 30-39
]

# Special squares positions
GO = 0
JAIL = 10
G2J = 30  # Go To Jail
CC = [2, 17, 33]  # Community Chest positions
CH = [7, 22, 36]  # Chance positions
RAILROADS = [5, 15, 25, 35]  # R1, R2, R3, R4
UTILITIES = [12, 28]  # U1, U2


def apply_community_chest_card(current_pos: int) -> int:
    """
    Apply Community Chest card effect.
    1/16 chance to go to GO, 1/16 chance to go to JAIL.
    """
    card = random.randint(1, 16)
    if card == 1:
        return GO
    if card == 2:
        return JAIL
    return current_pos


def apply_chance_card(current_pos: int) -> int:
    """
    Apply Chance card effect.
    Various movement rules based on card drawn.
    """
    card = random.randint(1, 16)
    if card == 1:
        return GO
    if card == 2:
        return JAIL
    if card == 3:
        return 11  # C1
    if card == 4:
        return 24  # E3
    if card == 5:
        return 39  # H2
    if card == 6:
        return 5  # R1
    if card in [7, 8]:  # Next railway
        if current_pos == 7:
            return 15  # R2
        if current_pos == 22:
            return 25  # R3
        if current_pos == 36:
            return 5  # R1
    elif card == 9:  # Next utility
        if current_pos == 7:
            return 12  # U1
        if current_pos == 22:
            return 28  # U2
        if current_pos == 36:
            return 12  # U1
    elif card == 10:  # Go back 3 squares
        return (current_pos - 3) % 40

    return current_pos


def simulate_game(dice_sides: int, num_rolls: int) -> dict[int, int]:
    """
    Simulate Monopoly game and count square visits.

    Args:
        dice_sides: Number of sides on each die (4 or 6)
        num_rolls: Number of dice rolls to simulate

    Returns:
        Dictionary mapping square position to visit count
    """
    position = 0  # Start at GO
    consecutive_doubles = 0
    visit_counts: dict[int, int] = defaultdict(int)

    for _ in range(num_rolls):
        # Roll two dice
        die1 = random.randint(1, dice_sides)
        die2 = random.randint(1, dice_sides)

        # Check for doubles
        if die1 == die2:
            consecutive_doubles += 1
            if consecutive_doubles == 3:
                # Three consecutive doubles: go to jail
                position = JAIL
                consecutive_doubles = 0
                visit_counts[position] += 1
                continue
        else:
            consecutive_doubles = 0

        # Move by dice roll
        position = (position + die1 + die2) % 40

        # Handle special squares
        if position == G2J:
            # Go To Jail
            position = JAIL
        elif position in CC:
            # Community Chest
            position = apply_community_chest_card(position)
        elif position in CH:
            # Chance
            position = apply_chance_card(position)

        visit_counts[position] += 1

    return visit_counts


def solve_naive(dice_sides: int = 4, num_simulations: int = 1000000) -> str:
    """
    素直な解法：モンテカルロシミュレーションによる確率計算
    時間計算量：O(n) - シミュレーション回数に比例
    空間計算量：O(1) - 固定サイズのカウンタ
    """
    random.seed(42)  # For reproducible results

    total_visits: dict[int, int] = defaultdict(int)

    # Run simulation
    visit_counts = simulate_game(dice_sides, num_simulations)
    for pos, count in visit_counts.items():
        total_visits[pos] += count

    # Find top 3 most visited squares
    sorted_squares = sorted(total_visits.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_squares[:3]

    # Format as 6-digit string (2 digits per square)
    result = ""
    for pos, _ in top_3:
        result += f"{pos:02d}"

    return result


def solve_optimized(dice_sides: int = 4) -> str:
    """
    最適化解法：マルコフ連鎖による定常分布計算
    時間計算量：O(n^3) - 行列演算による
    空間計算量：O(n^2) - 遷移行列
    """
    try:
        import numpy as np  # type: ignore[import-not-found]
    except ImportError:
        # Fallback to naive solution if numpy is not available
        return solve_naive(dice_sides, 1000000)

    # Create transition matrix (40x40)
    transition_matrix = np.zeros((40, 40))

    # Calculate basic movement probabilities
    for current_pos in range(40):
        for die1 in range(1, dice_sides + 1):
            for die2 in range(1, dice_sides + 1):
                # Basic movement
                new_pos = (current_pos + die1 + die2) % 40

                # Handle special squares
                if new_pos == G2J:
                    new_pos = JAIL
                elif new_pos in CC:
                    # Community Chest: 1/16 to GO, 1/16 to JAIL, 14/16 stay
                    transition_matrix[current_pos][GO] += (1 / 16) * (
                        1 / (dice_sides**2)
                    )
                    transition_matrix[current_pos][JAIL] += (1 / 16) * (
                        1 / (dice_sides**2)
                    )
                    transition_matrix[current_pos][new_pos] += (14 / 16) * (
                        1 / (dice_sides**2)
                    )
                    continue
                elif new_pos in CH:
                    # Chance: various probabilities
                    # Simplified: 1/16 each for GO, JAIL, and other specific moves
                    transition_matrix[current_pos][GO] += (1 / 16) * (
                        1 / (dice_sides**2)
                    )
                    transition_matrix[current_pos][JAIL] += (1 / 16) * (
                        1 / (dice_sides**2)
                    )
                    # Other chance effects (simplified)
                    transition_matrix[current_pos][new_pos] += (10 / 16) * (
                        1 / (dice_sides**2)
                    )
                    continue

                transition_matrix[current_pos][new_pos] += 1 / (dice_sides**2)

    # Handle consecutive doubles (simplified approximation)
    # In practice, this requires a more complex state space

    # Find steady state distribution
    eigenvalues, eigenvectors = np.linalg.eig(transition_matrix.T)
    steady_state_index = np.argmax(eigenvalues.real)
    steady_state = eigenvectors[:, steady_state_index].real
    steady_state = steady_state / np.sum(steady_state)

    # Find top 3 squares
    top_3_indices = np.argsort(steady_state)[-3:][::-1]

    # Format as 6-digit string
    result = ""
    for pos in top_3_indices:
        result += f"{pos:02d}"

    return result


def test_solutions() -> None:
    """テストケースで解答を検証"""
    # Test with 6-sided dice (known result should be close to "102400")
    print("Testing with 6-sided dice...")
    result_6 = solve_naive(dice_sides=6, num_simulations=100000)
    print(f"6-sided dice result: {result_6}")

    # Test with 4-sided dice
    print("Testing with 4-sided dice...")
    result_4 = solve_naive(dice_sides=4, num_simulations=100000)
    print(f"4-sided dice result: {result_4}")

    print("✓ Tests completed!")


def main() -> None:
    """メイン関数"""
    import time

    # Run test cases
    print("Running test cases...")
    test_solutions()
    print()

    # Solve the main problem (4-sided dice)
    print("Solving with 4-sided dice...")
    start = time.time()
    result = solve_naive(dice_sides=4, num_simulations=1000000)
    elapsed = time.time() - start

    print(f"Result: {result}")
    print(f"Time: {elapsed:.4f} seconds")

    # Decode result
    squares = [result[i : i + 2] for i in range(0, 6, 2)]
    print("Top 3 most visited squares:")
    for i, square_num in enumerate(squares, 1):
        square_pos = int(square_num)
        square_name = BOARD_SQUARES[square_pos]
        print(f"  {i}. Square {square_num} ({square_name})")


if __name__ == "__main__":
    main()
