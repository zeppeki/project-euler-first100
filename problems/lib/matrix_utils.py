"""
行列・データ処理関連のユーティリティ関数

Project Euler問題で使用される行列操作とデータファイル処理を提供する。
主にCSV読み込み、行列操作、隣接セル取得を含む。

抽出元:
- Problem 083: 行列データ読み込み（最短経路）
- Problem 081, 082: 行列パス問題
- Problem 011: グリッド内最大積
- Problem 096: 数独グリッド処理
"""

from pathlib import Path
from typing import Any


def load_matrix(
    filename: str,
    delimiter: str = ",",
    data_type: type = int,
    project_root: str | None = None,
) -> list[list[Any]]:
    """
    ファイルから行列データを読み込む

    Args:
        filename: データファイル名（data/ディレクトリからの相対パス）
        delimiter: 区切り文字（デフォルト: カンマ）
        data_type: データ型（デフォルト: int）
        project_root: プロジェクトルートディレクトリ（自動推定）

    Returns:
        数値の二次元リスト

    時間計算量: O(m×n) where m=行数, n=列数
    空間計算量: O(m×n)

    Examples:
        >>> matrix = load_matrix("p083_matrix.txt")
        >>> matrix[0][0]  # 最初の要素
        4445
    """
    if project_root is None:
        # 呼び出し元から2つ上のディレクトリを推定
        root_path = Path(__file__).parent.parent.parent
    else:
        root_path = Path(project_root)

    # dataディレクトリからの相対パス
    file_path = root_path / "data" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"データファイルが見つかりません: {file_path}")

    matrix = []
    with open(file_path, encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:  # 空行をスキップ
                continue

            try:
                row = [data_type(x.strip()) for x in line.split(delimiter)]
                matrix.append(row)
            except ValueError as e:
                raise ValueError(f"行{line_num}の変換エラー: {e}")

    return matrix


def parse_csv_matrix(
    csv_string: str, delimiter: str = ",", data_type: type = int
) -> list[list[Any]]:
    """
    CSV文字列を行列に変換

    Args:
        csv_string: CSV形式の文字列
        delimiter: 区切り文字
        data_type: データ型

    Returns:
        数値の二次元リスト

    時間計算量: O(m×n)
    空間計算量: O(m×n)

    Examples:
        >>> csv_str = "1,2,3\\n4,5,6\\n7,8,9"
        >>> parse_csv_matrix(csv_str)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    lines = csv_string.strip().split("\\n")
    matrix = []

    for line in lines:
        if line.strip():
            row = [data_type(x.strip()) for x in line.split(delimiter)]
            matrix.append(row)

    return matrix


def get_matrix_neighbors(
    row: int,
    col: int,
    matrix: list[list[Any]],
    directions: list[tuple[int, int]] | None = None,
    include_diagonals: bool = False,
) -> list[tuple[int, int, Any]]:
    """
    指定位置の隣接セルを取得

    Args:
        row: 行インデックス
        col: 列インデックス
        matrix: 対象行列
        directions: カスタム移動方向 [(dr, dc), ...]
        include_diagonals: 対角線方向を含むかどうか

    Returns:
        [(row, col, value), ...] の隣接セルリスト

    時間計算量: O(d) where d=方向数
    空間計算量: O(d)

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> get_matrix_neighbors(1, 1, matrix)
        [(0, 1, 2), (1, 0, 4), (1, 2, 6), (2, 1, 8)]
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    neighbors = []

    if directions is None:
        if include_diagonals:
            # 8方向（縦横斜め）
            directions = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
        else:
            # 4方向（上下左右）
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # 境界チェック
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col, matrix[new_row][new_col]))

    return neighbors


def matrix_transpose(matrix: list[list[Any]]) -> list[list[Any]]:
    """
    行列の転置を取得

    Args:
        matrix: 転置する行列

    Returns:
        転置された行列

    時間計算量: O(m×n)
    空間計算量: O(m×n)

    Examples:
        >>> matrix_transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]

    return transposed


def matrix_rotate_90(
    matrix: list[list[Any]], clockwise: bool = True
) -> list[list[Any]]:
    """
    行列を90度回転

    Args:
        matrix: 回転する行列
        clockwise: 時計回りかどうか

    Returns:
        回転された行列

    時間計算量: O(n²) for square matrix
    空間計算量: O(n²)

    Examples:
        >>> matrix_rotate_90([[1, 2], [3, 4]])
        [[3, 1], [4, 2]]
    """
    if not matrix or not matrix[0]:
        return []

    if clockwise:
        # 時計回り: transpose + reverse each row
        transposed = matrix_transpose(matrix)
        return [row[::-1] for row in transposed]
    # 反時計回り: reverse each row + transpose
    reversed_rows = [row[::-1] for row in matrix]
    return matrix_transpose(reversed_rows)


def find_max_product_in_grid(
    grid: list[list[int]],
    length: int,
    directions: list[tuple[int, int]] | None = None,
) -> int:
    """
    グリッド内で指定長の連続する数の最大積を探索

    Args:
        grid: 数値グリッド
        length: 連続する数の長さ
        directions: 探索方向 [(dr, dc), ...]

    Returns:
        最大積

    時間計算量: O(m×n×d×length) where d=方向数
    空間計算量: O(1)

    Examples:
        >>> grid = [[8, 2, 22, 97], [49, 49, 99, 40]]
        >>> find_max_product_in_grid(grid, 3)
        # 連続する3つの数の最大積
    """
    if not grid or not grid[0] or length <= 0:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_product = 0

    if directions is None:
        # 4方向: 水平、垂直、斜め2方向
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                product = 1
                valid = True

                for i in range(length):
                    new_row = row + i * dr
                    new_col = col + i * dc

                    # 境界チェック
                    if not (0 <= new_row < rows and 0 <= new_col < cols):
                        valid = False
                        break

                    product *= grid[new_row][new_col]

                if valid:
                    max_product = max(max_product, product)

    return max_product


def validate_matrix_dimensions(matrix: list[list[Any]]) -> bool:
    """
    行列の次元が正しいかチェック（全行が同じ列数）

    Args:
        matrix: チェックする行列

    Returns:
        正しい次元の場合True

    時間計算量: O(m) where m=行数
    空間計算量: O(1)
    """
    if not matrix:
        return True

    expected_cols = len(matrix[0])
    return all(len(row) == expected_cols for row in matrix)


def matrix_slice(
    matrix: list[list[Any]], row_start: int, row_end: int, col_start: int, col_end: int
) -> list[list[Any]]:
    """
    行列の部分領域を抽出

    Args:
        matrix: 元の行列
        row_start, row_end: 行の開始・終了インデックス
        col_start, col_end: 列の開始・終了インデックス

    Returns:
        部分行列

    時間計算量: O((row_end-row_start) × (col_end-col_start))
    空間計算量: O((row_end-row_start) × (col_end-col_start))

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> matrix_slice(matrix, 0, 2, 1, 3)
        [[2, 3], [5, 6]]
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])

    # 境界チェックと調整
    row_start = max(0, min(row_start, rows))
    row_end = max(row_start, min(row_end, rows))
    col_start = max(0, min(col_start, cols))
    col_end = max(col_start, min(col_end, cols))

    return [row[col_start:col_end] for row in matrix[row_start:row_end]]


def matrix_pad(
    matrix: list[list[Any]],
    pad_value: Any = 0,
    top: int = 1,
    bottom: int = 1,
    left: int = 1,
    right: int = 1,
) -> list[list[Any]]:
    """
    行列にパディングを追加

    Args:
        matrix: 元の行列
        pad_value: パディング値
        top, bottom, left, right: 各方向のパディング幅

    Returns:
        パディングされた行列

    時間計算量: O(m×n) where m,n=パディング後のサイズ
    空間計算量: O(m×n)

    Examples:
        >>> matrix_pad([[1, 2], [3, 4]], 0, 1, 1, 1, 1)
        [[0, 0, 0, 0], [0, 1, 2, 0], [0, 3, 4, 0], [0, 0, 0, 0]]
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    new_rows = rows + top + bottom
    new_cols = cols + left + right

    # パディングされた行列を初期化
    padded = [[pad_value] * new_cols for _ in range(new_rows)]

    # 元の行列をコピー
    for i in range(rows):
        for j in range(cols):
            padded[i + top][j + left] = matrix[i][j]

    return padded


def matrix_to_string(
    matrix: list[list[Any]], delimiter: str = " ", width: int | None = None
) -> str:
    """
    行列を文字列表現に変換

    Args:
        matrix: 変換する行列
        delimiter: 要素間の区切り文字
        width: 各要素の表示幅（右寄せ）

    Returns:
        行列の文字列表現

    時間計算量: O(m×n)
    空間計算量: O(m×n×avg_str_len)

    Examples:
        >>> matrix_to_string([[1, 22, 333], [4, 55, 666]], width=4)
        "   1   22  333\\n   4   55  666"
    """
    if not matrix:
        return ""

    lines = []
    for row in matrix:
        if width:
            formatted_row = [f"{item!s:>{width}}" for item in row]
        else:
            formatted_row = [str(item) for item in row]
        lines.append(delimiter.join(formatted_row))

    return "\\n".join(lines)


def create_matrix(rows: int, cols: int, fill_value: Any = 0) -> list[list[Any]]:
    """
    指定サイズの行列を作成

    Args:
        rows: 行数
        cols: 列数
        fill_value: 初期値

    Returns:
        初期化された行列

    時間計算量: O(rows×cols)
    空間計算量: O(rows×cols)

    Examples:
        >>> create_matrix(2, 3, 1)
        [[1, 1, 1], [1, 1, 1]]
    """
    return [[fill_value] * cols for _ in range(rows)]


def matrix_apply(matrix: list[list[Any]], func: Any) -> list[list[Any]]:
    """
    行列の各要素に関数を適用

    Args:
        matrix: 対象行列
        func: 適用する関数

    Returns:
        変換された行列

    時間計算量: O(m×n×f) where f=関数の計算量
    空間計算量: O(m×n)

    Examples:
        >>> matrix_apply([[1, 2], [3, 4]], lambda x: x * 2)
        [[2, 4], [6, 8]]
    """
    return [[func(item) for item in row] for row in matrix]
