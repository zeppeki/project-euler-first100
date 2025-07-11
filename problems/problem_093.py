#!/usr/bin/env python3
"""
Problem 093: Arithmetic expressions

Using the digits 1, 2, 3, 4 exactly once, and the operations +, -, *, / and brackets,
it is possible to form many different positive integers.

For example:
8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) - 1
36 = 3 * 4 * (2 + 1)

What is remarkable is that EVERY positive integer from 1 to 28 can be obtained in this manner.

Given that the set {1, 2, 3, 4} can achieve a consecutive run of 1 to 28,
find the set of four distinct digits, a < b < c < d, for which the longest run of consecutive
positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.
"""

from itertools import combinations, permutations


def evaluate_expression(a: float, b: float, op: str) -> float | None:
    """
    二つの数値に対して演算を実行
    時間計算量: O(1)
    空間計算量: O(1)
    """
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else None
    return None


def generate_all_expressions(digits: tuple[int, ...]) -> set[int]:
    """
    4つの数字から生成可能な全ての正の整数を生成
    時間計算量: O(4! × 4³ × 5) = O(1280) (定数時間)
    空間計算量: O(k) where k is number of unique results
    """
    if len(digits) != 4:
        raise ValueError("This function requires exactly 4 digits")

    results = set()

    # 全ての数字の順列を試す
    for perm in permutations(digits):
        a, b, c, d = perm

        # 全ての演算子の組み合わせを試す
        operations = ["+", "-", "*", "/"]
        for op1 in operations:
            for op2 in operations:
                for op3 in operations:
                    # 5つの括弧パターンを直接評価
                    expressions_results = []

                    # ((a op1 b) op2 c) op3 d
                    temp1 = evaluate_expression(a, b, op1)
                    if temp1 is not None:
                        temp2 = evaluate_expression(temp1, c, op2)
                        if temp2 is not None:
                            expressions_results.append(
                                evaluate_expression(temp2, d, op3)
                            )

                    # (a op1 (b op2 c)) op3 d
                    temp1 = evaluate_expression(b, c, op2)
                    if temp1 is not None:
                        temp2 = evaluate_expression(a, temp1, op1)
                        if temp2 is not None:
                            expressions_results.append(
                                evaluate_expression(temp2, d, op3)
                            )

                    # (a op1 b) op2 (c op3 d)
                    temp1 = evaluate_expression(a, b, op1)
                    temp2 = evaluate_expression(c, d, op3)
                    if temp1 is not None and temp2 is not None:
                        expressions_results.append(
                            evaluate_expression(temp1, temp2, op2)
                        )

                    # a op1 ((b op2 c) op3 d)
                    temp1 = evaluate_expression(b, c, op2)
                    if temp1 is not None:
                        temp2 = evaluate_expression(temp1, d, op3)
                        if temp2 is not None:
                            expressions_results.append(
                                evaluate_expression(a, temp2, op1)
                            )

                    # a op1 (b op2 (c op3 d))
                    temp1 = evaluate_expression(c, d, op3)
                    if temp1 is not None:
                        temp2 = evaluate_expression(b, temp1, op2)
                        if temp2 is not None:
                            expressions_results.append(
                                evaluate_expression(a, temp2, op1)
                            )

                    for result in expressions_results:
                        if (
                            result is not None
                            and result > 0
                            and abs(result - round(result)) < 1e-9
                        ):
                            # 正の整数かチェック（浮動小数点誤差を考慮）
                            results.add(round(result))

    return results


def find_consecutive_length(numbers: set[int]) -> int:
    """
    1から始まる連続した正の整数の最大長を求める
    時間計算量: O(n)
    空間計算量: O(1)
    """
    length = 0
    current = 1

    while current in numbers:
        length += 1
        current += 1

    return length


def solve_naive() -> str:
    """
    素直な解法: 全ての4桁の組み合わせを試す
    時間計算量: O(C(10,4) × 4! × 4³ × 5) = O(210 × 1280) = O(268,800)
    空間計算量: O(1)
    """
    max_length = 0
    best_digits = ""

    # 4つの異なる数字の組み合わせを全て試す (0-9)
    for digits in combinations(range(10), 4):
        # 0を含む場合は除外（割り算でエラーになる可能性が高い）
        if 0 in digits:
            continue

        # この組み合わせで生成可能な全ての数を取得
        possible_numbers = generate_all_expressions(digits)

        # 連続した長さを計算
        consecutive_length = find_consecutive_length(possible_numbers)

        # 最長の場合を記録
        if consecutive_length > max_length:
            max_length = consecutive_length
            best_digits = "".join(map(str, digits))

    return best_digits


def solve_optimized() -> str:
    """
    最適化解法: 0を除外し、より効率的な計算
    時間計算量: O(C(9,4) × 4! × 4³ × 5) = O(126 × 1280) = O(161,280)
    空間計算量: O(1)
    """
    max_length = 0
    best_digits = ""

    # 0を除外して1-9の数字のみを使用
    for digits in combinations(range(1, 10), 4):
        # この組み合わせで生成可能な全ての数を取得
        possible_numbers = generate_all_expressions(digits)

        # 連続した長さを計算
        consecutive_length = find_consecutive_length(possible_numbers)

        # 最長の場合を記録
        if consecutive_length > max_length:
            max_length = consecutive_length
            best_digits = "".join(map(str, digits))

    return best_digits


def solve_mathematical() -> str:
    """
    数学的解法: 最適化解法と同じ（この問題では数学的ショートカットがない）
    時間計算量: O(C(9,4) × 4! × 4³ × 5) = O(126 × 1280) = O(161,280)
    空間計算量: O(1)
    """
    return solve_optimized()


def get_expression_details(
    digits: tuple[int, ...],
) -> dict[str, int | set[int] | tuple[int, ...]]:
    """
    指定された数字組み合わせの詳細情報を取得
    時間計算量: O(4! × 4³ × 5) = O(1280)
    空間計算量: O(k) where k is number of unique results
    """
    possible_numbers = generate_all_expressions(digits)
    consecutive_length = find_consecutive_length(possible_numbers)

    return {
        "digits": digits,
        "possible_numbers": possible_numbers,
        "consecutive_length": consecutive_length,
        "max_consecutive": consecutive_length,
    }
