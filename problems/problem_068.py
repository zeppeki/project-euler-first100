#!/usr/bin/env python3
"""
Problem 068: Magic 5-gon ring

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.

Working clockwise, starting from the group of three with the numerically
lowest external node (4,3,2 in this example); each solution can be described
uniquely. For example, the above solution can be described by the set:
4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12.
There are eight solutions in total.

By starting with the group containing the lowest external node and working
clockwise, what is the 16-digit string for the maximum magic 5-gon ring?
"""

from itertools import permutations


def is_valid_5gon(arrangement: list[int]) -> tuple[bool, list[tuple[int, int, int]]]:
    """
    5-gon配置が有効かどうかを確認し、ライン情報を返す

    Args:
        arrangement: [外部5つ, 内部5つ]の配置 (長さ10)

    Returns:
        (有効性, ライン情報のリスト)
    """
    if len(arrangement) != 10:
        return False, []

    # 外部ノード (位置0-4) と内部ノード (位置5-9)
    external = arrangement[:5]
    internal = arrangement[5:]

    # 5つのラインを構成
    # ライン構成: 外部[i] -> 内部[i] -> 内部[(i+1)%5]
    lines = []
    for i in range(5):
        line = (external[i], internal[i], internal[(i + 1) % 5])
        lines.append(line)

    # 全ラインの合計が同じかチェック
    line_sums = [sum(line) for line in lines]
    if len(set(line_sums)) != 1:
        return False, []

    return True, lines


def format_5gon_string(lines: list[tuple[int, int, int]]) -> str:
    """
    5-gonのライン情報を16桁文字列に変換

    Args:
        lines: ライン情報のリスト

    Returns:
        16桁の文字列
    """
    # 最小の外部ノードを持つラインから開始
    min_external = min(line[0] for line in lines)
    start_idx = next(i for i, line in enumerate(lines) if line[0] == min_external)

    # 時計回りに並び替え
    ordered_lines = []
    for i in range(5):
        ordered_lines.append(lines[(start_idx + i) % 5])

    # 各ラインを文字列に変換して結合
    result = ""
    for line in ordered_lines:
        result += "".join(map(str, line))

    return result


def solve_naive() -> str:
    """
    素直な解法: 全ての順列を試して最大16桁文字列を見つける

    時間計算量: O(10!) - 10! = 3,628,800通りの順列
    空間計算量: O(1)

    Returns:
        最大16桁文字列
    """
    max_string = ""

    # 1-10の数字の全順列を試す
    for perm in permutations(range(1, 11)):
        is_valid, lines = is_valid_5gon(list(perm))

        if is_valid:
            # 16桁文字列にフォーマット
            string_rep = format_5gon_string(lines)

            # 16桁であることを確認（10が含まれると17桁になる場合がある）
            if len(string_rep) == 16:
                max_string = max(max_string, string_rep)

    return max_string


def solve_optimized() -> str:
    """
    最適化解法: 対称性と制約を利用して探索空間を削減

    16桁になるためには、10は外部ノードに配置される必要がある
    （10が内部にあると、それが2つのラインに現れて17桁になる）

    時間計算量: O(9! / 5) - 対称性による削減
    空間計算量: O(1)

    Returns:
        最大16桁文字列
    """
    max_string = ""

    # 16桁にするため、10は外部ノードに配置
    # 対称性を利用し、10を外部の固定位置（位置0）に配置
    remaining_numbers = list(range(1, 10))  # 1-9

    for perm in permutations(remaining_numbers):
        # 10を外部の最初の位置に固定し、残りを配置
        arrangement = [10, *list(perm[:4]), *list(perm[4:])]

        is_valid, lines = is_valid_5gon(arrangement)

        if is_valid:
            string_rep = format_5gon_string(lines)

            # 16桁確認
            if len(string_rep) == 16:
                max_string = max(max_string, string_rep)

    return max_string


def solve_mathematical() -> str:
    """
    数学的解法: 数学的制約を活用してさらに効率的に探索

    魔法5-gonでは：
    - 各ラインの合計は同じ
    - 総和 = 1+2+...+10 = 55
    - 内部ノードは2回カウントされる
    - 5×ライン合計 = 外部の合計 + 2×内部の合計 = 55 + 内部の合計
    - よってライン合計 = (55 + 内部の合計) / 5

    時間計算量: O(C(9,5) × 4! × 4!) - 組み合わせと順列
    空間計算量: O(1)

    Returns:
        最大16桁文字列
    """
    max_string = ""

    # 1-9の数字から5つを選んで内部ノードとする
    from itertools import combinations

    remaining_numbers = list(range(1, 10))

    for internal_nums in combinations(remaining_numbers, 5):
        external_nums = [n for n in remaining_numbers if n not in internal_nums]
        external_nums.append(10)  # 10は必ず外部

        # 内部の合計を計算
        internal_sum = sum(internal_nums)

        # ライン合計を計算
        if (55 + internal_sum) % 5 != 0:
            continue  # ライン合計が整数でない場合はスキップ

        line_sum = (55 + internal_sum) // 5

        # 内部ノードの順列を試す
        for internal_perm in permutations(internal_nums):
            # 外部ノードの順列を試す
            for external_perm in permutations(external_nums):
                arrangement = list(external_perm) + list(internal_perm)

                is_valid, lines = is_valid_5gon(arrangement)

                if is_valid and all(sum(line) == line_sum for line in lines):
                    # ライン合計が期待値と一致するか確認
                    string_rep = format_5gon_string(lines)

                    if len(string_rep) == 16:
                        max_string = max(max_string, string_rep)

    return max_string


def get_example_3gon() -> tuple[list[tuple[int, int, int]], str]:
    """
    例題の3-gon ringデータを取得

    Returns:
        (ライン情報, 期待する文字列)
    """
    # 例題: 4,3,2; 6,2,1; 5,1,3 (各ライン合計=9)
    lines = [(4, 3, 2), (6, 2, 1), (5, 1, 3)]
    expected_string = "432621513"
    return lines, expected_string
