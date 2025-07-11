#!/usr/bin/env python3
"""
Problem 095: Amicable chains

The proper divisors of a number are all the divisors excluding the number itself.
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14.
As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
proper divisors of 284 is 220, forming a chain of two numbers.
For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496,
we form a chain of five numbers:
12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""


def sum_of_proper_divisors(n: int) -> int:
    """
    与えられた数の真の約数（自分自身を除く約数）の和を計算
    時間計算量: O(sqrt(n))
    空間計算量: O(1)
    """
    if n <= 1:
        return 0

    total = 1  # 1 is always a divisor
    # Only need to check up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            # Add the corresponding divisor if it's different
            if i != n // i:
                total += n // i

    return total


def compute_divisor_sums(limit: int) -> list[int]:
    """
    1からlimitまでの全ての数について、真の約数の和を計算
    時間計算量: O(n * log n)
    空間計算量: O(n)
    """
    divisor_sums = [0] * (limit + 1)

    # Use sieve-like approach
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            divisor_sums[j] += i

    return divisor_sums


def find_chain_length(
    start: int, divisor_sums: list[int], limit: int
) -> tuple[int, list[int]]:
    """
    与えられた数から始まる連鎖の長さと連鎖を返す
    時間計算量: O(k) where k is chain length
    空間計算量: O(k)
    """
    chain = [start]
    seen = {start}
    current = start

    while True:
        # Get next number in chain
        if current >= len(divisor_sums):
            return 0, []

        next_num = divisor_sums[current]

        # Check various termination conditions
        if next_num > limit:
            # Chain element exceeds limit
            return 0, []

        if next_num == 0 or next_num == 1:
            # Chain terminates at 0 or 1
            return 0, []

        if next_num == start:
            # Found an amicable chain
            return len(chain), chain

        if next_num < start:
            # We should have seen this chain before
            return 0, []

        if next_num in seen:
            # Found a loop that doesn't include start
            return 0, []

        chain.append(next_num)
        seen.add(next_num)
        current = next_num


def solve_naive(limit: int = 1000000) -> int:
    """
    素直な解法: 全ての数について連鎖を計算
    時間計算量: O(n * sqrt(n))
    空間計算量: O(n)
    """
    max_chain_length = 0
    result = 0
    seen = set()

    for i in range(2, limit + 1):
        if i in seen:
            continue

        chain = []
        current = i

        # Build chain
        while current not in chain and current <= limit:
            chain.append(current)
            current = sum_of_proper_divisors(current)

            if current == 0 or current == 1:
                break

        # Check if we found an amicable chain
        if current in chain:
            start_index = chain.index(current)
            if start_index == 0:  # Chain returns to start
                chain_length = len(chain)
                if chain_length > max_chain_length:
                    max_chain_length = chain_length
                    result = min(chain)

                # Mark all elements in chain as seen
                seen.update(chain)

    return result


def solve_optimized(limit: int = 1000000) -> int:
    """
    最適化解法: 事前計算した約数和を使用
    時間計算量: O(n * log n)
    空間計算量: O(n)
    """
    # Precompute divisor sums
    divisor_sums = compute_divisor_sums(limit)

    max_chain_length = 0
    result = 0
    seen = set()

    for i in range(2, limit + 1):
        if i in seen:
            continue

        chain_length, chain = find_chain_length(i, divisor_sums, limit)

        if chain_length > 0:
            # Found an amicable chain
            if chain_length > max_chain_length:
                max_chain_length = chain_length
                result = min(chain)

            # Mark all elements in chain as seen
            seen.update(chain)

    return result


def solve_mathematical(limit: int = 1000000) -> int:
    """
    数学的解法: 最適化解法と同じ（この問題では特別な数学的ショートカットはない）
    時間計算量: O(n * log n)
    空間計算量: O(n)
    """
    return solve_optimized(limit)


def find_all_amicable_chains(limit: int = 1000000) -> list[tuple[int, list[int]]]:
    """
    指定された制限内のすべての友愛連鎖を見つける
    時間計算量: O(n * log n)
    空間計算量: O(n)
    """
    divisor_sums = compute_divisor_sums(limit)
    chains = []
    seen = set()

    for i in range(2, limit + 1):
        if i in seen:
            continue

        chain_length, chain = find_chain_length(i, divisor_sums, limit)

        if chain_length > 0:
            chains.append((chain_length, chain))
            seen.update(chain)

    return sorted(chains, key=lambda x: (-x[0], min(x[1])))


def main() -> None:
    """メイン実行関数"""
    import time

    # Small example
    print("Small example (limit=15000):")
    start_time = time.time()
    chains = find_all_amicable_chains(15000)
    print(f"Found {len(chains)} amicable chains")
    for length, chain in chains[:5]:  # Show first 5
        print(f"  Length {length}: {chain[:5]}{'...' if len(chain) > 5 else ''}")
    print(f"Time: {time.time() - start_time:.3f}s")
    print()

    # Main problem
    print("Main problem (limit=1000000):")
    start_time = time.time()
    result = solve_optimized()
    print(f"Smallest member of the longest amicable chain: {result}")
    print(f"Time: {time.time() - start_time:.3f}s")


if __name__ == "__main__":
    main()
