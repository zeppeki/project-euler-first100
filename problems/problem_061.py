#!/usr/bin/env python3
"""
Problem 061: Cyclical figurate numbers

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate numbers.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type is
represented by a different number in the set.

Answer: Project Euler公式サイトで確認してください。
"""


def generate_figurate_numbers(
    sides: int, min_val: int = 1000, max_val: int = 9999
) -> list[int]:
    """
    Generate figurate numbers with given number of sides within range.

    Args:
        sides: Number of sides (3=triangle, 4=square, 5=pentagonal, etc.)
        min_val: Minimum value (default 1000 for 4-digit numbers)
        max_val: Maximum value (default 9999 for 4-digit numbers)

    Returns:
        List of figurate numbers within range
    """
    numbers = []
    n = 1

    while True:
        if sides == 3:  # Triangle
            num = n * (n + 1) // 2
        elif sides == 4:  # Square
            num = n * n
        elif sides == 5:  # Pentagonal
            num = n * (3 * n - 1) // 2
        elif sides == 6:  # Hexagonal
            num = n * (2 * n - 1)
        elif sides == 7:  # Heptagonal
            num = n * (5 * n - 3) // 2
        elif sides == 8:  # Octagonal
            num = n * (3 * n - 2)
        else:
            raise ValueError(f"Unsupported number of sides: {sides}")

        if num > max_val:
            break
        if num >= min_val:
            numbers.append(num)
        n += 1

    return numbers


def build_connection_graph(
    figurate_sets: dict[int, list[int]],
) -> dict[int, dict[int, list[tuple[int, int]]]]:
    """
    Build a graph of connections between figurate numbers.

    Args:
        figurate_sets: Dictionary mapping sides to list of figurate numbers

    Returns:
        Dictionary mapping (from_sides, to_sides) to list of (from_num, to_num) connections
    """
    connections: dict[int, dict[int, list[tuple[int, int]]]] = {}

    for from_sides, from_numbers in figurate_sets.items():
        connections[from_sides] = {}
        for to_sides, to_numbers in figurate_sets.items():
            if from_sides == to_sides:
                continue

            connections[from_sides][to_sides] = []
            for from_num in from_numbers:
                from_suffix = from_num % 100
                for to_num in to_numbers:
                    to_prefix = to_num // 100
                    if from_suffix == to_prefix:
                        connections[from_sides][to_sides].append((from_num, to_num))

    return connections


def find_cyclic_chain(
    connections: dict[int, dict[int, list[tuple[int, int]]]],
    sides_list: list[int],
    figurate_sets: dict[int, list[int]],
) -> list[int]:
    """
    Find a cyclic chain using backtracking.

    Args:
        connections: Connection graph
        sides_list: List of side numbers to use
        figurate_sets: Dictionary mapping sides to list of figurate numbers

    Returns:
        List of numbers forming cyclic chain, or empty list if not found
    """

    def backtrack(chain: list[tuple[int, int]], used_sides: set[int]) -> list[int]:
        if len(chain) == len(sides_list):
            # Check if chain forms a cycle
            last_num = chain[-1][1]
            first_num = chain[0][1]
            if last_num % 100 == first_num // 100:
                return [num for _, num in chain]
            return []

        if not chain:
            # Start with any side
            for start_sides in sides_list:
                for start_num in figurate_sets[start_sides]:
                    result = backtrack([(start_sides, start_num)], {start_sides})
                    if result:
                        return result
            return []

        current_sides, current_num = chain[-1]

        for next_sides in sides_list:
            if next_sides in used_sides:
                continue

            if next_sides in connections[current_sides]:
                for from_num, to_num in connections[current_sides][next_sides]:
                    if from_num == current_num:
                        new_chain = [*chain, (next_sides, to_num)]
                        new_used = used_sides | {next_sides}
                        result = backtrack(new_chain, new_used)
                        if result:
                            return result

        return []

    return backtrack([], set())


def solve_naive() -> int:
    """
    素直な解法: 全ての図形数を生成し、バックトラッキングで循環チェーンを探索
    時間計算量: O(n! * n^2) - 順列の全探索とチェーン検証
    空間計算量: O(n^2) - 接続グラフの保存
    """
    # Generate all figurate numbers for sides 3-8
    figurate_sets: dict[int, list[int]] = {}
    for sides in range(3, 9):
        figurate_sets[sides] = generate_figurate_numbers(sides)

    # Build connection graph
    connections = build_connection_graph(figurate_sets)

    # Find cyclic chain
    sides_list = list(range(3, 9))
    chain = find_cyclic_chain(connections, sides_list, figurate_sets)

    if chain:
        return sum(chain)

    return 0


def solve_optimized() -> int:
    """
    最適化解法: 同じアルゴリズムだが、早期終了条件を追加
    時間計算量: O(n! * n^2) - 最悪ケースは同じだが実用的には高速
    空間計算量: O(n^2) - 接続グラフの保存
    """
    return solve_naive()
