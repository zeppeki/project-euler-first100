"""
Project Euler 共通ライブラリ

Project Euler問題解決で使用される共通関数のライブラリ。
重複コードの削減とコードの再利用性向上を目的とする。

モジュール:
- primes: 素数関連の関数
- math_utils: 数学的ユーティリティ関数
- combinatorics: 組み合わせ・順列関数
- sequences: 数列生成関数
- digits: 数字・文字列処理関数
"""

from .combinatorics import *
from .digits import *
from .math_utils import *
from .primes import *
from .sequences import *

__all__ = [
    # primes module
    "is_prime",
    "is_prime_optimized",
    "sieve_of_eratosthenes",
    "generate_primes",
    "get_prime_factors",
    "count_distinct_prime_factors",
    "is_truncatable_prime",
    # math_utils module
    "gcd",
    "lcm",
    "factorial",
    "factorial_builtin",
    "combination",
    "prime_factorization",
    "get_divisors",
    "count_divisors",
    "get_proper_divisors_sum",
    "is_abundant",
    "is_palindrome",
    "fibonacci",
    "get_triangular_number",
    "get_pentagonal_number",
    "get_hexagonal_number",
    # combinatorics module
    "combination_formula",
    "permutation_formula",
    "get_permutations",
    "get_combinations",
    "get_permutations_with_replacement",
    "get_combinations_with_replacement",
    "multinomial_coefficient",
    # sequences module
    "generate_triangle",
    "generate_pentagonal",
    "generate_hexagonal",
    "generate_octagonal",
    "generate_square",
    "generate_heptagonal",
    "fibonacci_generator",
    "triangle_generator",
    "pentagonal_generator",
    "hexagonal_generator",
    "is_triangle_number",
    "is_pentagonal_number",
    "is_hexagonal_number",
    # digits module
    "get_digit_signature",
    "get_digit_signature_tuple",
    "is_pandigital",
    "is_pandigital_1_to_9",
    "is_pandigital_0_to_9",
    "reverse_number",
    "get_rotations",
    "get_permutations_4digit",
    "are_permutations",
    "digit_factorial_sum",
    "digit_power_sum",
    "concatenated_product",
    "get_digit_at_position",
    "has_substring_divisibility",
    "is_circular_prime_candidate",
    "count_digits",
    "sum_of_digits",
]
