"""
ファイルI/O関連のユーティリティ関数

Project Euler問題で使用されるデータファイル処理と統一的なI/O操作を提供する。
主にテキストファイル読み込み、構造化データ処理、エラーハンドリングを含む。

抽出元:
- Problem 022: 名前ファイル読み込み
- Problem 042: 単語ファイル読み込み
- Problem 054: ポーカーハンド読み込み
- Problem 079: キーログ読み込み
- Problem 089: ローマ数字ファイル読み込み
- Problem 096: 数独パズル読み込み
- Problem 098: 単語ファイル読み込み
"""

import csv
import json
from pathlib import Path
from typing import Any, cast


def load_problem_data(
    filename: str,
    data_type: str = "lines",
    project_root: str | None = None,
    encoding: str = "utf-8",
) -> list[str] | list[list[str]] | list[int] | str:
    """
    Project Eulerデータファイルを統一的に読み込む

    Args:
        filename: データファイル名（data/ディレクトリからの相対パス）
        data_type: データ形式 ("lines", "csv", "words", "numbers", "raw")
        project_root: プロジェクトルートディレクトリ（自動推定）
        encoding: ファイルエンコーディング

    Returns:
        data_type に応じた形式のデータ

    時間計算量: O(n) where n=ファイルサイズ
    空間計算量: O(n)

    Examples:
        >>> names = load_problem_data("p022_names.txt", "words")
        >>> len(names)
        5163
        >>> names[0]
        "MARY"
    """
    if project_root is None:
        root_path = Path(__file__).parent.parent.parent
    else:
        root_path = Path(project_root)

    file_path = root_path / "data" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"データファイルが見つかりません: {file_path}")

    try:
        with open(file_path, encoding=encoding) as f:
            content = f.read()
    except UnicodeDecodeError as e:
        raise ValueError(f"ファイルエンコーディングエラー: {e}") from e

    if data_type == "raw":
        return content

    if data_type == "lines":
        return [line.strip() for line in content.splitlines() if line.strip()]

    if data_type == "csv":
        lines = content.splitlines()
        return [line.split(",") for line in lines if line.strip()]

    if data_type == "words":
        # 引用符で囲まれた単語リストを処理
        if '"' in content:
            # 引用符を除去して分割
            words = [word.strip('"') for word in content.split(",")]
            return [word for word in words if word]
        # 通常の単語分割
        return content.split()

    if data_type == "numbers":
        # 数値のリストを処理
        numbers = []
        for line in content.splitlines():
            line = line.strip()
            if line:
                # カンマ区切りまたは空白区切りの数値
                if "," in line:
                    numbers.extend(
                        [int(x.strip()) for x in line.split(",") if x.strip().isdigit()]
                    )
                else:
                    numbers.extend([int(x) for x in line.split() if x.isdigit()])
        return numbers

    raise ValueError(f"サポートされていないdata_type: {data_type}")


def load_names_file(filename: str = "p022_names.txt") -> list[str]:
    """
    名前ファイルを読み込む（Problem 022用）

    Args:
        filename: 名前ファイル名

    Returns:
        名前のリスト

    Examples:
        >>> names = load_names_file()
        >>> "MARY" in names
        True
    """
    result = load_problem_data(filename, "words")
    return cast("list[str]", result)


def load_words_file(filename: str = "p042_words.txt") -> list[str]:
    """
    単語ファイルを読み込む（Problem 042, 098用）

    Args:
        filename: 単語ファイル名

    Returns:
        単語のリスト

    Examples:
        >>> words = load_words_file()
        >>> len(words) > 1000
        True
    """
    result = load_problem_data(filename, "words")
    return cast("list[str]", result)


def load_poker_hands(
    filename: str = "p054_poker.txt",
) -> list[tuple[list[str], list[str]]]:
    """
    ポーカーハンドファイルを読み込む（Problem 054用）

    Args:
        filename: ポーカーファイル名

    Returns:
        [(player1_hand, player2_hand), ...] のリスト

    Examples:
        >>> hands = load_poker_hands()
        >>> len(hands)
        1000
        >>> hands[0]
        (['8C', 'TS', 'KC', '9H', '4S'], ['7D', '2S', '5D', '3S', 'AC'])
    """
    lines = load_problem_data(filename, "lines")
    hands = []

    for line in lines:
        cards = line.split()
        if len(cards) == 10:
            player1 = cards[:5]
            player2 = cards[5:]
            hands.append((player1, player2))

    return hands


def load_keylog_data(filename: str = "0079_keylog.txt") -> list[str]:
    """
    キーログファイルを読み込む（Problem 079用）

    Args:
        filename: キーログファイル名

    Returns:
        キーログエントリのリスト

    Examples:
        >>> attempts = load_keylog_data()
        >>> len(attempts)
        50
        >>> attempts[0]
        "319"
    """
    result = load_problem_data(filename, "lines")
    return cast("list[str]", result)


def load_triangle_data(filename: str = "0067_triangle.txt") -> list[list[int]]:
    """
    三角形データファイルを読み込む（Problem 067用）

    Args:
        filename: 三角形ファイル名

    Returns:
        三角形の数値配列

    Examples:
        >>> triangle = load_triangle_data()
        >>> len(triangle)
        100
        >>> triangle[0]
        [59]
    """
    lines = load_problem_data(filename, "lines")
    triangle = []

    for line in lines:
        row = [int(x) for x in line.split()]
        triangle.append(row)

    return triangle


def load_matrix_data(filename: str, delimiter: str = ",") -> list[list[int]]:
    """
    行列データファイルを読み込む（Problem 081, 082, 083用）

    Args:
        filename: 行列ファイル名
        delimiter: 区切り文字

    Returns:
        行列の数値配列

    Examples:
        >>> matrix = load_matrix_data("p081_matrix.txt")
        >>> len(matrix)
        80
        >>> len(matrix[0])
        80
    """
    lines = load_problem_data(filename, "lines")
    matrix = []

    for line in lines:
        row = [int(x.strip()) for x in line.split(delimiter)]
        matrix.append(row)

    return matrix


def load_cipher_data(filename: str = "p059_cipher.txt") -> list[int]:
    """
    暗号データファイルを読み込む（Problem 059用）

    Args:
        filename: 暗号ファイル名

    Returns:
        暗号化された数値のリスト

    Examples:
        >>> cipher = load_cipher_data()
        >>> len(cipher) > 1000
        True
    """
    return load_problem_data(filename, "numbers")


def load_roman_numerals(filename: str = "p089_roman.txt") -> list[str]:
    """
    ローマ数字ファイルを読み込む（Problem 089用）

    Args:
        filename: ローマ数字ファイル名

    Returns:
        ローマ数字のリスト

    Examples:
        >>> romans = load_roman_numerals()
        >>> len(romans)
        1000
    """
    return load_problem_data(filename, "lines")


def load_base_exp_data(filename: str = "p099_base_exp.txt") -> list[tuple[int, int]]:
    """
    底と指数のペアを読み込む（Problem 099用）

    Args:
        filename: データファイル名

    Returns:
        (base, exponent) のタプルのリスト

    Examples:
        >>> pairs = load_base_exp_data()
        >>> len(pairs)
        1000
        >>> pairs[0]
        (519432, 525806)
    """
    lines = load_problem_data(filename, "lines")
    pairs = []

    for line in lines:
        parts = line.split(",")
        if len(parts) == 2:
            base = int(parts[0].strip())
            exp = int(parts[1].strip())
            pairs.append((base, exp))

    return pairs


def safe_file_reader(
    file_path: str | Path,
    encoding: str = "utf-8",
    fallback_encodings: list[str] | None = None,
) -> str:
    """
    エラーハンドリング付きファイル読み込み

    Args:
        file_path: ファイルパス
        encoding: 優先エンコーディング
        fallback_encodings: フォールバックエンコーディングのリスト

    Returns:
        ファイル内容

    Raises:
        FileNotFoundError: ファイルが見つからない場合
        UnicodeDecodeError: 全てのエンコーディングで読み込み失敗

    Examples:
        >>> content = safe_file_reader("data/names.txt")
        >>> isinstance(content, str)
        True
    """
    if fallback_encodings is None:
        fallback_encodings = ["utf-8", "latin-1", "cp1252", "ascii"]

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"ファイルが見つかりません: {file_path}")

    # 優先エンコーディングを最初に試す
    encodings_to_try = [encoding] + [
        enc for enc in fallback_encodings if enc != encoding
    ]

    for enc in encodings_to_try:
        try:
            with open(file_path, encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue

    raise UnicodeDecodeError(
        f"ファイルを読み込めませんでした。試行したエンコーディング: {encodings_to_try}"
    )


def parse_structured_file(content: str, structure_type: str, **kwargs) -> Any:
    """
    構造化ファイルの内容を解析

    Args:
        content: ファイル内容
        structure_type: 構造タイプ ("json", "csv", "key_value", "grid")
        **kwargs: 構造固有のパラメータ

    Returns:
        解析されたデータ

    Examples:
        >>> json_content = '{"key": "value"}'
        >>> parse_structured_file(json_content, "json")
        {"key": "value"}
    """
    if structure_type == "json":
        return json.loads(content)

    if structure_type == "csv":
        delimiter = kwargs.get("delimiter", ",")
        lines = content.strip().split("\n")
        return [line.split(delimiter) for line in lines if line.strip()]

    if structure_type == "key_value":
        separator = kwargs.get("separator", "=")
        lines = content.strip().split("\n")
        result = {}
        for line in lines:
            if separator in line:
                key, value = line.split(separator, 1)
                result[key.strip()] = value.strip()
        return result

    if structure_type == "grid":
        element_type = kwargs.get("element_type", str)
        delimiter = kwargs.get("delimiter", " ")
        lines = content.strip().split("\n")
        grid = []
        for line in lines:
            if line.strip():
                row = [element_type(x.strip()) for x in line.split(delimiter)]
                grid.append(row)
        return grid

    raise ValueError(f"サポートされていない構造タイプ: {structure_type}")


def write_results_to_file(
    results: Any,
    filename: str,
    format_type: str = "json",
    project_root: str | None = None,
) -> None:
    """
    結果をファイルに書き込む

    Args:
        results: 書き込むデータ
        filename: 出力ファイル名
        format_type: 出力形式 ("json", "csv", "text")
        project_root: プロジェクトルートディレクトリ

    Examples:
        >>> write_results_to_file({"answer": 42}, "result.json")
    """
    if project_root is None:
        project_root = Path(__file__).parent.parent.parent
    else:
        project_root = Path(project_root)

    file_path = project_root / "output" / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if format_type == "json":
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

    elif format_type == "csv":
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if isinstance(results, list) and isinstance(results[0], list | tuple):
                writer.writerows(results)
            else:
                writer.writerow(results)

    elif format_type == "text":
        with open(file_path, "w", encoding="utf-8") as f:
            if isinstance(results, str):
                f.write(results)
            else:
                f.write(str(results))

    else:
        raise ValueError(f"サポートされていない形式: {format_type}")


def get_file_stats(filename: str, project_root: str | None = None) -> dict[str, Any]:
    """
    ファイルの統計情報を取得

    Args:
        filename: ファイル名
        project_root: プロジェクトルートディレクトリ

    Returns:
        ファイル統計情報の辞書

    Examples:
        >>> stats = get_file_stats("p022_names.txt")
        >>> stats["line_count"]
        1
        >>> stats["file_size"] > 0
        True
    """
    if project_root is None:
        root_path = Path(__file__).parent.parent.parent
    else:
        root_path = Path(project_root)

    file_path = root_path / "data" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"ファイルが見つかりません: {file_path}")

    # ファイル情報
    stat_info = file_path.stat()

    # 内容分析
    content = safe_file_reader(file_path)
    lines = content.splitlines()

    return {
        "file_size": stat_info.st_size,
        "line_count": len(lines),
        "char_count": len(content),
        "non_empty_line_count": len([line for line in lines if line.strip()]),
        "max_line_length": max(len(line) for line in lines) if lines else 0,
        "encoding_detected": "utf-8",  # 簡易版
        "contains_numbers": any(char.isdigit() for char in content),
        "contains_letters": any(char.isalpha() for char in content),
    }
