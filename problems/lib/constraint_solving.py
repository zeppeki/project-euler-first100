"""
制約充足問題関連のユーティリティ関数

Project Euler問題で使用される制約充足問題とバックトラッキングアルゴリズムを提供する。
主に数独、N-Queen、グラフ彩色問題などを含む。

抽出元:
- Problem 096: 数独パズル（制約充足問題）
- Problem 068: 魔法五角形（制約と組み合わせ最適化）
- Problem 043: 部分文字列可除性（制約検証）
"""

from collections.abc import Callable
from pathlib import Path
from typing import Any


def load_sudoku_puzzles(
    filename: str = "p096_sudoku.txt", project_root: str | None = None
) -> list[list[list[int]]]:
    """
    数独パズルをファイルから読み込む

    Args:
        filename: 数独ファイル名（data/ディレクトリからの相対パス）
        project_root: プロジェクトルートディレクトリ（自動推定）

    Returns:
        数独パズルのリスト（各パズルは9x9の二次元リスト）

    時間計算量: O(n) where n=パズル数
    空間計算量: O(n)

    Examples:
        >>> puzzles = load_sudoku_puzzles()
        >>> len(puzzles)  # パズル数
        50
        >>> len(puzzles[0])  # 9x9グリッド
        9
    """
    if project_root is None:
        root_path = Path(__file__).parent.parent.parent
    else:
        root_path = Path(project_root)

    file_path = root_path / "data" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"数独ファイルが見つかりません: {file_path}")

    puzzles = []
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("Grid"):
            # 9x9グリッドを読み込み
            grid = []
            for j in range(1, 10):
                if i + j < len(lines):
                    row_str = lines[i + j].strip()
                    row = [int(digit) for digit in row_str]
                    grid.append(row)

            if len(grid) == 9 and all(len(row) == 9 for row in grid):
                puzzles.append(grid)

            i += 10  # 次のグリッドにスキップ
        else:
            i += 1

    return puzzles


def is_valid_sudoku_move(
    grid: list[list[int]], row: int, col: int, num: int, size: int = 9
) -> bool:
    """
    数独の配置が有効かどうかを判定

    Args:
        grid: 数独グリッド
        row: 行インデックス
        col: 列インデックス
        num: 配置する数字
        size: グリッドサイズ（デフォルト: 9）

    Returns:
        有効な配置の場合True

    時間計算量: O(size)
    空間計算量: O(1)

    Examples:
        >>> grid = [[5,3,0,0,7,0,0,0,0], ...]  # 9x9 sudoku
        >>> is_valid_sudoku_move(grid, 0, 2, 4)
        True
    """
    box_size = int(size**0.5)

    # 行チェック
    for j in range(size):
        if grid[row][j] == num:
            return False

    # 列チェック
    for i in range(size):
        if grid[i][col] == num:
            return False

    # ボックスチェック（3x3 or NxNの小ボックス）
    box_row = (row // box_size) * box_size
    box_col = (col // box_size) * box_size
    for i in range(box_row, box_row + box_size):
        for j in range(box_col, box_col + box_size):
            if grid[i][j] == num:
                return False

    return True


def find_empty_cell(
    grid: list[list[int]], empty_value: int = 0
) -> tuple[int, int] | None:
    """
    空のセルを見つける

    Args:
        grid: グリッド
        empty_value: 空を表す値

    Returns:
        (row, col) または None

    時間計算量: O(n²) where n=グリッドサイズ
    空間計算量: O(1)
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == empty_value:
                return (i, j)
    return None


def solve_sudoku_backtrack(
    grid: list[list[int]], size: int = 9, empty_value: int = 0
) -> bool:
    """
    バックトラッキングを使用した数独解法

    Args:
        grid: 数独グリッド（インプレースで変更）
        size: グリッドサイズ
        empty_value: 空を表す値

    Returns:
        解けた場合True、解けない場合False

    時間計算量: O(size^(n²)) 最悪の場合
    空間計算量: O(n²) 再帰スタック

    Examples:
        >>> grid = [[5,3,0,0,7,0,0,0,0], ...]
        >>> solve_sudoku_backtrack(grid)
        True
        >>> grid[0][2]  # 解けた後の値
        4
    """
    empty_cell = find_empty_cell(grid, empty_value)
    if empty_cell is None:
        return True  # 全て埋まっている = 解完了

    row, col = empty_cell

    for num in range(1, size + 1):
        if is_valid_sudoku_move(grid, row, col, num, size):
            grid[row][col] = num

            if solve_sudoku_backtrack(grid, size, empty_value):
                return True

            # バックトラック
            grid[row][col] = empty_value

    return False


def is_complete_sudoku(
    grid: list[list[int]], size: int = 9, empty_value: int = 0
) -> bool:
    """
    数独が完成しているかチェック

    Args:
        grid: 数独グリッド
        size: グリッドサイズ
        empty_value: 空を表す値

    Returns:
        完成している場合True

    時間計算量: O(n²)
    空間計算量: O(1)
    """
    # 空のセルがないかチェック
    if find_empty_cell(grid, empty_value) is not None:
        return False

    # 全ての制約を満たしているかチェック
    for row in range(size):
        for col in range(size):
            current_value = grid[row][col]
            grid[row][col] = empty_value  # 一時的に空にする

            if not is_valid_sudoku_move(grid, row, col, current_value, size):
                grid[row][col] = current_value  # 復元
                return False

            grid[row][col] = current_value  # 復元

    return True


def solve_n_queens(n: int) -> list[list[tuple[int, int]]]:
    """
    N-Queen問題をバックトラッキングで解く

    Args:
        n: ボードサイズ（n×n）

    Returns:
        全ての解のリスト（各解は[(row, col), ...]のクイーン位置）

    時間計算量: O(n!)
    空間計算量: O(n)

    Examples:
        >>> solutions = solve_n_queens(4)
        >>> len(solutions)
        2
        >>> solutions[0]
        [(0, 1), (1, 3), (2, 0), (3, 2)]
    """

    def is_safe(positions: list[int], row: int, col: int) -> bool:
        """クイーンの配置が安全かチェック"""
        for r in range(row):
            # 同じ列 or 対角線上にある場合
            if positions[r] == col or abs(positions[r] - col) == abs(r - row):
                return False
        return True

    def backtrack(positions: list[int], row: int) -> list[list[int]]:
        """バックトラッキングで解を探索"""
        if row == n:
            return [positions[:]]

        solutions = []
        for col in range(n):
            if is_safe(positions, row, col):
                positions[row] = col
                solutions.extend(backtrack(positions, row + 1))

        return solutions

    # 解を探索
    all_solutions = backtrack([-1] * n, 0)

    # 結果をタプル形式に変換
    result = []
    for solution in all_solutions:
        positions = [(row, col) for row, col in enumerate(solution)]
        result.append(positions)

    return result


def solve_constraint_satisfaction(
    variables: list[Any],
    domains: dict[Any, list[Any]],
    constraints: list[Callable[[dict[Any, Any]], bool]],
    assignment: dict[Any, Any] | None = None,
) -> dict[Any, Any] | None:
    """
    汎用制約充足問題ソルバー（バックトラッキング）

    Args:
        variables: 変数のリスト
        domains: 各変数の定義域 {variable: [possible_values]}
        constraints: 制約関数のリスト [func(assignment) -> bool]
        assignment: 部分的な割り当て（初期値）

    Returns:
        解の割り当て、または解がない場合None

    時間計算量: O(d^n) where d=平均定義域サイズ, n=変数数
    空間計算量: O(n)

    Examples:
        >>> variables = ['A', 'B', 'C']
        >>> domains = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
        >>> constraints = [lambda x: x.get('A', 0) != x.get('B', 0)]
        >>> solve_constraint_satisfaction(variables, domains, constraints)
        {'A': 1, 'B': 2, 'C': 1}
    """
    if assignment is None:
        assignment = {}

    # 全ての変数が割り当てられた場合
    if len(assignment) == len(variables):
        return assignment

    # 次の未割り当て変数を選択
    unassigned = [var for var in variables if var not in assignment]
    variable = unassigned[0]

    # 定義域の各値を試す
    for value in domains[variable]:
        assignment[variable] = value

        # 制約チェック
        if all(constraint(assignment) for constraint in constraints):
            result = solve_constraint_satisfaction(
                variables, domains, constraints, assignment
            )
            if result is not None:
                return result

        # バックトラック
        del assignment[variable]

    return None


def is_magic_square(square: list[list[int]]) -> bool:
    """
    魔方陣かどうかをチェック

    Args:
        square: n×n の数値グリッド

    Returns:
        魔方陣の場合True

    時間計算量: O(n²)
    空間計算量: O(1)

    Examples:
        >>> is_magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
        True  # 各行・列・対角線の合計が15
    """
    n = len(square)
    if not all(len(row) == n for row in square):
        return False

    # 期待される合計値（最初の行の合計）
    target_sum = sum(square[0])

    # 各行の合計をチェック
    for row in square:
        if sum(row) != target_sum:
            return False

    # 各列の合計をチェック
    for col in range(n):
        if sum(square[row][col] for row in range(n)) != target_sum:
            return False

    # 対角線の合計をチェック
    if sum(square[i][i] for i in range(n)) != target_sum:
        return False
    return sum(square[i][n - 1 - i] for i in range(n)) == target_sum


def generate_permutations_with_constraints(
    elements: list[Any], constraints: list[Callable[[list[Any]], bool]]
) -> list[list[Any]]:
    """
    制約を満たす順列を生成

    Args:
        elements: 順列の要素
        constraints: 制約関数のリスト

    Returns:
        制約を満たす順列のリスト

    時間計算量: O(n! × c) where c=制約チェック時間
    空間計算量: O(n!)

    Examples:
        >>> elements = [1, 2, 3, 4]
        >>> constraints = [lambda perm: perm[0] < perm[1]]
        >>> result = generate_permutations_with_constraints(elements, constraints)
        # 最初の2要素が昇順の順列のみ
    """
    from itertools import permutations

    valid_permutations = []

    for perm in permutations(elements):
        perm_list = list(perm)
        if all(constraint(perm_list) for constraint in constraints):
            valid_permutations.append(perm_list)

    return valid_permutations


def backtrack_search(
    state: Any,
    is_complete: Callable[[Any], bool],
    get_candidates: Callable[[Any], list[Any]],
    apply_move: Callable[[Any, Any], Any],
    is_valid: Callable[[Any], bool],
) -> Any | None:
    """
    汎用バックトラッキング探索フレームワーク

    Args:
        state: 現在の状態
        is_complete: 完了状態かチェックする関数
        get_candidates: 次の候補を取得する関数
        apply_move: 移動を適用する関数
        is_valid: 状態が有効かチェックする関数

    Returns:
        解の状態、または None

    Examples:
        >>> # 数独解法での使用例
        >>> def is_complete(grid): return find_empty_cell(grid) is None
        >>> def get_candidates(grid): return [1,2,3,4,5,6,7,8,9]
        >>> solution = backtrack_search(initial_grid, is_complete, ...)
    """
    if is_complete(state):
        return state

    for candidate in get_candidates(state):
        new_state = apply_move(state, candidate)

        if is_valid(new_state):
            result = backtrack_search(
                new_state, is_complete, get_candidates, apply_move, is_valid
            )
            if result is not None:
                return result

    return None
