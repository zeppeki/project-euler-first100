"""
Runner for Problem 084: Monopoly odds
"""

import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from problems.problem_084 import BOARD_SQUARES, solve_naive
from problems.utils.display import (
    print_final_answer,
    print_solution_header,
)


def run_tests() -> None:
    """Run test cases."""
    # Test cases: (dice_sides, num_simulations, description)
    test_cases = [
        # Test with different dice configurations
        (6, 10000, "6-sided dice (small sample)"),
        (4, 10000, "4-sided dice (small sample)"),
    ]

    print("=== テストケース ===")

    for dice_sides, num_simulations, description in test_cases:
        print(f"\n{description}:")
        print(f"  サイコロ: {dice_sides}面")
        print(f"  シミュレーション回数: {num_simulations:,}")

        try:
            result = solve_naive(dice_sides=dice_sides, num_simulations=num_simulations)
            print(f"  結果: {result}")

            # Decode and display top 3 squares
            squares = [result[i : i + 2] for i in range(0, 6, 2)]
            print("  最頻訪問マス:")
            for i, square_num in enumerate(squares, 1):
                square_pos = int(square_num)
                square_name = BOARD_SQUARES[square_pos]
                print(f"    {i}. Square {square_num} ({square_name})")
            print("  ✓")

        except Exception as e:
            print(f"  エラー - {e}")


def run_problem() -> None:
    """Run the main problem."""
    print("=== 本問題の解答 ===")
    print("4面ダイスを使用したモノポリーゲームの解析...")
    print()

    # Run with high precision simulation
    from problems.utils.performance import measure_performance

    print("高精度シミュレーション実行中...")
    result, execution_time = measure_performance(
        solve_naive, dice_sides=4, num_simulations=1000000
    )

    print(f"実行時間: {execution_time:.6f}秒")
    print("シミュレーション回数: 1,000,000回")
    print()

    # Display result
    print_final_answer(result)

    # Decode and display details
    squares = [result[i : i + 2] for i in range(0, 6, 2)]
    print("最も訪問頻度の高い3つのマス:")
    for i, square_num in enumerate(squares, 1):
        square_pos = int(square_num)
        square_name = BOARD_SQUARES[square_pos]
        print(f"  {i}位: Square {square_num} ({square_name})")
    print()


def run_comparison() -> None:
    """Run comparison between different dice configurations."""
    print("=== 6面ダイス vs 4面ダイス比較 ===")

    print("6面ダイス (標準):")
    result_6 = solve_naive(dice_sides=6, num_simulations=100000)
    squares_6 = [result_6[i : i + 2] for i in range(0, 6, 2)]
    for i, square_num in enumerate(squares_6, 1):
        square_pos = int(square_num)
        square_name = BOARD_SQUARES[square_pos]
        print(f"  {i}位: Square {square_num} ({square_name})")

    print("\n4面ダイス:")
    result_4 = solve_naive(dice_sides=4, num_simulations=100000)
    squares_4 = [result_4[i : i + 2] for i in range(0, 6, 2)]
    for i, square_num in enumerate(squares_4, 1):
        square_pos = int(square_num)
        square_name = BOARD_SQUARES[square_pos]
        print(f"  {i}位: Square {square_num} ({square_name})")

    print("\n結果:")
    print(f"  6面ダイス: {result_6}")
    print(f"  4面ダイス: {result_4}")


def main() -> None:
    """Main function."""
    print_solution_header("084", "Monopoly odds")

    print("Running tests...\n")
    run_tests()

    print("\n" + "=" * 50)
    run_comparison()

    print("\n" + "=" * 50)
    run_problem()


if __name__ == "__main__":
    main()
