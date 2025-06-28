#!/usr/bin/env python3
"""
Runner for Problem 005: Smallest multiple

This module contains the execution code for Problem 005, separated from the
algorithm implementations for better test coverage and code organization.
"""

from problems.problem_005 import (
    prime_factorization,
    solve_builtin,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)
from problems.utils.display import (
    print_final_answer,
    print_performance_comparison,
    print_solution_header,
    print_test_results,
)
from problems.utils.performance import compare_performance


def run_tests() -> None:
    """Run test cases to verify the solutions."""
    test_cases = [
        (1, 1),  # LCM(1) = 1
        (2, 2),  # LCM(1,2) = 2
        (3, 6),  # LCM(1,2,3) = 6
        (4, 12),  # LCM(1,2,3,4) = 12
        (5, 60),  # LCM(1,2,3,4,5) = 60
        (10, 2520),  # 問題例: LCM(1,...,10) = 2520
    ]

    functions = [
        ("素直な解法", solve_naive),
        ("最適化解法", solve_optimized),
        ("数学的解法", solve_mathematical),
        ("標準ライブラリ解法", solve_builtin),
    ]

    print_test_results(test_cases, functions)


def run_problem() -> None:
    """Run the main problem with performance comparison."""
    n = 20

    print_solution_header("005", "Smallest multiple",
                         f"divisible by all numbers from 1 to {n}")

    # Run tests first
    run_tests()

    # Run main problem with performance measurement
    functions = [
        ("素直な解法", lambda: solve_naive(n)),
        ("最適化解法", lambda: solve_optimized(n)),
        ("数学的解法", lambda: solve_mathematical(n)),
        ("標準ライブラリ解法", lambda: solve_builtin(n)),
    ]

    performance_results = compare_performance(functions)

    # Verify all solutions agree
    results = [data["result"] for data in performance_results.values()]
    all_agree = len(set(results)) == 1

    if all_agree:
        answer = results[0]
        print_final_answer(answer, verified=True)
        print_performance_comparison(performance_results)

        # 素因数分解の確認
        print("=== 素因数分解の確認 ===")
        print(f"結果: {answer:,}")

        factors = prime_factorization(answer)
        factor_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factors])
        print(f"素因数分解: {factor_str}")

        # 検証: 1からnまでの各数で割り切れることを確認
        print("\n=== 除数確認 ===")
        verification_failed = False
        for i in range(1, min(n + 1, 11)):  # 表示は最初の10個まで
            if answer % i == 0:
                print(f"{answer:,} ÷ {i} = {answer // i:,} ✓")
            else:
                print(f"{answer:,} ÷ {i} = 余り{answer % i} ✗")
                verification_failed = True

        if n > 10:
            print(f"... (11から{n}まで省略)")
            for i in range(11, n + 1):
                if answer % i != 0:
                    print(f"{answer:,} ÷ {i} = 余り{answer % i} ✗")
                    verification_failed = True

        if not verification_failed:
            print("全ての数で割り切れることを確認 ✓")
    else:
        print_final_answer(None, verified=False)
        print("Results:", results)


def main() -> None:
    """Main function for standalone execution."""
    run_problem()


if __name__ == "__main__":
    main()
