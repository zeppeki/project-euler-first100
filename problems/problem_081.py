#!/usr/bin/env python3
"""
Problem 081: Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum from the top left to the bottom right by only moving right and down
in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by
80 matrix.

解法:
1. 素直な解法: 再帰的に全ての経路を探索
2. 最適化解法: 動的計画法を使用して効率的に計算
"""

from pathlib import Path


def load_matrix(filename: str = "p081_matrix.txt") -> list[list[int]]:
    """ファイルから行列を読み込む"""
    file_path = Path(__file__).parent.parent / "data" / filename
    matrix = []

    with open(file_path) as f:
        for line in f:
            row = [int(x) for x in line.strip().split(",")]
            matrix.append(row)

    return matrix


def solve_naive(matrix: list[list[int]] | None = None) -> int:
    """
    素直な解法: 再帰的に全ての経路を探索
    時間計算量: O(2^(m+n))
    空間計算量: O(m+n) (再帰スタック)

    Args:
        matrix: 2次元配列の行列（Noneの場合はファイルから読み込み）

    Returns:
        左上から右下への最小経路の合計
    """
    if matrix is None:
        matrix = load_matrix()
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    def min_path_sum(row: int, col: int) -> int:
        """位置(row, col)から右下への最小経路の合計を返す"""
        # ベースケース: 右下に到達
        if row == rows - 1 and col == cols - 1:
            return matrix[row][col]

        # 境界外の場合は大きな値を返す
        if row >= rows or col >= cols:
            return 10**9

        # 現在のセルの値 + (右に移動 or 下に移動)の最小値
        right = min_path_sum(row, col + 1)
        down = min_path_sum(row + 1, col)

        return matrix[row][col] + min(right, down)

    return min_path_sum(0, 0)


def solve_optimized(matrix: list[list[int]] | None = None) -> int:
    """
    最適化解法: 動的計画法を使用
    時間計算量: O(m*n)
    空間計算量: O(m*n)

    Args:
        matrix: 2次元配列の行列（Noneの場合はファイルから読み込み）

    Returns:
        左上から右下への最小経路の合計
    """
    if matrix is None:
        matrix = load_matrix()
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    # DPテーブルの初期化
    dp = [[0] * cols for _ in range(rows)]

    # 初期値: 左上のセル
    dp[0][0] = matrix[0][0]

    # 最初の行を埋める（右にしか移動できない）
    for col in range(1, cols):
        dp[0][col] = dp[0][col - 1] + matrix[0][col]

    # 最初の列を埋める（下にしか移動できない）
    for row in range(1, rows):
        dp[row][0] = dp[row - 1][0] + matrix[row][0]

    # 残りのセルを埋める
    for row in range(1, rows):
        for col in range(1, cols):
            # 上から来る場合と左から来る場合の最小値を選択
            dp[row][col] = matrix[row][col] + min(dp[row - 1][col], dp[row][col - 1])

    return dp[rows - 1][cols - 1]


def test_solutions() -> None:
    """テストケースで解答を検証"""
    # 問題文の例
    test_matrix = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]

    expected = 2427

    # 両方の解法をテスト
    naive_result = solve_naive(test_matrix)
    optimized_result = solve_optimized(test_matrix)

    print("テスト行列での結果:")
    print(f"素直な解法: {naive_result}")
    print(f"最適化解法: {optimized_result}")
    print(f"期待値: {expected}")
    print(
        f"テスト結果: {'成功' if naive_result == expected == optimized_result else '失敗'}"
    )


def main() -> None:
    """メイン関数"""
    import time

    # テストケースで検証
    test_solutions()
    print()

    # 小さい行列でのベンチマーク
    small_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("小さい行列 (3x3) でのベンチマーク:")

    # 素直な解法
    start = time.time()
    result_naive = solve_naive(small_matrix)
    time_naive = time.time() - start
    print(f"素直な解法: {result_naive} (時間: {time_naive:.6f}秒)")

    # 最適化解法
    start = time.time()
    result_optimized = solve_optimized(small_matrix)
    time_optimized = time.time() - start
    print(f"最適化解法: {result_optimized} (時間: {time_optimized:.6f}秒)")

    print()

    # 実際の問題を解く（ファイルが存在する場合）
    try:
        matrix = load_matrix()
        print(f"読み込んだ行列のサイズ: {len(matrix)}x{len(matrix[0])}")

        # 最適化解法のみ実行（大きい行列では素直な解法は非常に遅い）
        start = time.time()
        result = solve_optimized(matrix)
        elapsed = time.time() - start

        print(f"\n問題081の解答: {result}")
        print(f"計算時間: {elapsed:.6f}秒")

    except FileNotFoundError:
        print("行列ファイルが見つかりません。テスト用の行列で実行します。")

        # テスト用の大きめの行列を生成
        import random

        random.seed(81)
        test_size = 20
        large_test_matrix = [
            [random.randint(1, 1000) for _ in range(test_size)]  # nosec B311
            for _ in range(test_size)
        ]

        print(f"\nテスト用 {test_size}x{test_size} 行列での実行:")

        start = time.time()
        result = solve_optimized(large_test_matrix)
        elapsed = time.time() - start

        print(f"最適化解法の結果: {result}")
        print(f"計算時間: {elapsed:.6f}秒")


if __name__ == "__main__":
    main()
