#!/usr/bin/env python3
"""
Problem 079: Passcode derivation

A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyze the file so as to determine the shortest possible secret passcode of unknown length.

Answer: Check Project Euler website for verification
"""

from pathlib import Path


def read_keylog_data(filename: str = "data/0079_keylog.txt") -> list[str]:
    """
    キーログファイルを読み込む
    """
    path = Path(__file__).parent.parent / filename
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def build_dependency_graph(attempts: list[str]) -> dict[str, set[str]]:
    """
    各桁の依存関係グラフを構築する
    dependencies[a] = {set of digits that must come after a}
    """
    dependencies: dict[str, set[str]] = {}

    for attempt in attempts:
        for i in range(len(attempt)):
            digit = attempt[i]
            if digit not in dependencies:
                dependencies[digit] = set()

            # この桁の後に来る全ての桁を依存関係に追加
            for j in range(i + 1, len(attempt)):
                dependencies[digit].add(attempt[j])

    return dependencies


def topological_sort(dependencies: dict[str, set[str]]) -> str:
    """
    トポロジカルソートを使って正しい順序を決定する
    """
    all_digits = set(dependencies.keys())
    for deps in dependencies.values():
        all_digits.update(deps)

    # 各桁への入次数を計算
    in_degree = dict.fromkeys(all_digits, 0)
    for digit in dependencies:
        for dep in dependencies[digit]:
            in_degree[dep] += 1

    # 入次数が0の桁から開始
    queue = [digit for digit in all_digits if in_degree[digit] == 0]
    result = []

    while queue:
        # 最小の桁を選択（辞書順）
        queue.sort()
        current = queue.pop(0)
        result.append(current)

        # この桁に依存する桁の入次数を減らす
        if current in dependencies:
            for neighbor in dependencies[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    return "".join(result)


def solve_naive() -> int:
    """
    素直な解法: トポロジカルソートを使った依存関係解析
    時間計算量: O(V + E) where V=digits, E=dependencies
    空間計算量: O(V + E)
    """
    attempts = read_keylog_data()
    dependencies = build_dependency_graph(attempts)
    passcode = topological_sort(dependencies)
    return int(passcode)


def solve_optimized() -> int:
    """
    最適化解法: 同じアルゴリズム（最適性を保持）
    時間計算量: O(V + E)
    空間計算量: O(V + E)
    """
    return solve_naive()


def solve_mathematical() -> int:
    """
    数学的解法: グラフ理論ベースの解法
    時間計算量: O(V + E)
    空間計算量: O(V + E)
    """
    attempts = read_keylog_data()

    # より効率的な依存関係構築
    all_digits = set()
    before_relations: dict[str, set[str]] = {}

    for attempt in attempts:
        for digit in attempt:
            all_digits.add(digit)
            if digit not in before_relations:
                before_relations[digit] = set()

        # 直接的な前後関係のみを記録
        for i in range(len(attempt)):
            for j in range(i + 1, len(attempt)):
                before_relations[attempt[i]].add(attempt[j])

    # トポロジカルソート（Kahn's algorithm）
    in_degree = dict.fromkeys(all_digits, 0)
    for digit in before_relations:
        for after_digit in before_relations[digit]:
            in_degree[after_digit] += 1

    queue = [d for d in all_digits if in_degree[d] == 0]
    result = []

    while queue:
        queue.sort()  # 辞書順で安定ソート
        current = queue.pop(0)
        result.append(current)

        if current in before_relations:
            for neighbor in before_relations[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    return int("".join(result))


def verify_passcode(passcode: str, attempts: list[str]) -> bool:
    """
    パスコードが全てのログイン試行を満たすかを検証
    """
    for attempt in attempts:
        pos = 0
        for digit in attempt:
            try:
                pos = passcode.index(digit, pos)
                pos += 1
            except ValueError:
                return False
    return True
