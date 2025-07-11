"""
Project Euler Problem 88: Product-sum numbers
=============================================

A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers,
{a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
"""


def find_minimal_product_sum_numbers(max_k: int) -> dict[int, int]:
    """
    2からmax_kまでの各kに対する最小積和数を見つける。

    Args:
        max_k: 最大のk値

    Returns:
        k値と最小積和数の辞書
    """
    # 各kに対する最小積和数
    min_ps: dict[int, int] = {}

    def search(product: int, sum_val: int, num_factors: int, min_factor: int) -> None:
        """
        再帰的に積和数を探索する。

        Args:
            product: 現在の積
            sum_val: 現在の和
            num_factors: 使用した因数の個数
            min_factor: 次に使える最小の因数
        """
        # k = 因数の個数 + (積 - 和) 個の1
        k = num_factors + product - sum_val

        if 2 <= k <= max_k and (k not in min_ps or product < min_ps[k]):
            min_ps[k] = product

        # 探索を続ける - より大きい因数を探す
        factor = min_factor
        while factor * product <= 2 * max_k:  # 上限を設定
            if num_factors + 1 + factor * product - sum_val - factor <= max_k:
                search(product * factor, sum_val + factor, num_factors + 1, factor)
            factor += 1

    # 探索開始
    search(1, 0, 0, 2)

    return min_ps


def solve_naive(max_k: int = 12000) -> int:
    """
    素直な解法: 各数について因数分解を行い、積和数となるk値を探す。

    時間計算量: O(n × √n × factors)
    空間計算量: O(k)

    Args:
        max_k: 最大のk値（デフォルト: 12000）

    Returns:
        2≤k≤max_kの最小積和数の和（重複を除く）
    """
    k_values = find_minimal_product_sum_numbers(max_k)

    # 重複を除いた和を計算
    unique_values = set()
    for k in range(2, max_k + 1):
        if k in k_values:
            unique_values.add(k_values[k])

    return sum(unique_values)


def solve_optimized(max_k: int = 12000) -> int:
    """
    最適化解法: 動的計画法を使用して効率的に探索。

    時間計算量: O(n log n)
    空間計算量: O(k)

    Args:
        max_k: 最大のk値

    Returns:
        2≤k≤max_kの最小積和数の和（重複を除く）
    """
    # 各kに対する最小積和数を保存
    min_product_sum = [float("inf")] * (max_k + 1)

    # 上限を設定（経験的に2 * max_kで十分）
    limit = 2 * max_k

    def search(prod: int, sum_val: int, factors: int, start: int) -> None:
        """積和数を探索する内部関数"""
        # k = 因数の個数 + (積 - 和) 個の1
        k = factors + prod - sum_val

        if k <= max_k:
            min_product_sum[k] = min(min_product_sum[k], prod)

            # 次の因数を探索
            for i in range(start, limit // prod + 1):
                new_prod = prod * i
                if new_prod - sum_val - i + factors + 1 > max_k:
                    break
                search(new_prod, sum_val + i, factors + 1, i)

    # 探索開始
    search(1, 0, 0, 2)

    # 重複を除いた和を計算
    unique_values = set(min_product_sum[2 : max_k + 1])
    # 無限大を除外
    unique_values.discard(float("inf"))

    return int(sum(unique_values))


def solve_mathematical(max_k: int = 12000) -> int:
    """
    数学的解法: 効率的な探索アルゴリズムを使用。

    時間計算量: O(k log k)
    空間計算量: O(k)

    Args:
        max_k: 最大のk値

    Returns:
        2≤k≤max_kの最小積和数の和（重複を除く）
    """
    # 各kに対する最小積和数
    ps = [2 * k for k in range(max_k + 1)]  # 初期値: 2k = k + k = k × 2

    def get_product_sum_k(prod: int, sum_val: int, factors: int, start: int) -> None:
        """
        与えられた積に対して、可能な全てのk値を計算する。

        Args:
            prod: 現在の積
            sum_val: 現在の和
            factors: 使用した因数の個数
            start: 次の因数の最小値
        """
        # k = 因数の個数 + (積 - 和) 個の1
        k = factors - sum_val + prod

        if k <= max_k:
            if prod < ps[k]:
                ps[k] = prod

            # 次の因数を探索
            for i in range(start, 2 * max_k // prod + 1):
                get_product_sum_k(prod * i, sum_val + i, factors + 1, i)

    # 探索開始（最小の因数は2）
    get_product_sum_k(1, 1, 1, 2)

    # 重複を除いた和を計算
    return sum(set(ps[2:]))
