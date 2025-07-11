#!/usr/bin/env python3
"""
Problem 059 Runner: XOR decryption

XOR暗号の復号を実行し、パフォーマンス分析を行うランナーです。
"""

from collections.abc import Callable
from typing import Any

from problems.problem_059 import (
    calculate_ascii_sum,
    find_decryption_key,
    load_encrypted_text,
    solve_mathematical,
    solve_naive,
    solve_optimized,
    xor_decrypt,
)
from problems.runners.base_runner import BaseProblemRunner


class Problem059Runner(BaseProblemRunner):
    """Problem 059: XOR decryption のランナークラス"""

    def __init__(
        self, enable_performance_test: bool = False, enable_demonstrations: bool = False
    ) -> None:
        super().__init__(
            "059",
            "XOR decryption",
            7306,
            enable_performance_test,
            enable_demonstrations,
        )

    def get_test_cases(self) -> list[tuple[Any, ...]]:
        """
        テストケースを取得
        XOR復号の基本的なテストケースを提供
        """
        return [
            # (encrypted_data, key, expected_decrypted)
            # シンプルなテストケース: "Hello" XOR "abc"
            ([72 ^ 97, 101 ^ 98, 108 ^ 99, 108 ^ 97, 111 ^ 98], "abc", "Hello"),
            # XOR対称性テスト: "Test" XOR "key"
            ([84 ^ 107, 101 ^ 101, 115 ^ 121, 116 ^ 107], "key", "Test"),
            # 空のデータ
            ([], "abc", ""),
        ]

    def get_solution_functions(self) -> list[tuple[str, Callable[..., Any]]]:
        """解法関数を取得"""

        # テスト用のXOR復号関数をラップ
        def test_xor_decrypt(encrypted_data: list[int], key: str) -> str:
            return xor_decrypt(encrypted_data, key)

        return [
            ("XOR復号テスト", test_xor_decrypt),
        ]

    def get_main_parameters(self) -> tuple[Any, ...]:
        """メイン問題のパラメータを取得"""
        # メイン問題では引数なし（内部でデータファイルを読み込む）
        return ()

    def get_demonstration_functions(self) -> list[Callable[[], None]] | None:
        """デモンストレーション関数を取得"""
        return [
            self._demonstrate_xor_encryption,
            self._demonstrate_key_analysis,
            self._demonstrate_frequency_analysis,
        ]

    def _demonstrate_xor_encryption(self) -> None:
        """XOR暗号の基本デモンストレーション"""
        print("=== XOR暗号の基本原理 ===")

        original_text = "Hello World"
        key = "abc"

        print(f"原文: '{original_text}'")
        print(f"キー: '{key}'")

        # 暗号化
        encrypted = []
        for i, char in enumerate(original_text):
            key_char = key[i % len(key)]
            encrypted_byte = ord(char) ^ ord(key_char)
            encrypted.append(encrypted_byte)
            print(
                f"  '{char}' (ASCII {ord(char)}) XOR '{key_char}' (ASCII {ord(key_char)}) = {encrypted_byte}"
            )

        print(f"暗号化データ: {encrypted}")

        # 復号
        decrypted = xor_decrypt(encrypted, key)
        print(f"復号結果: '{decrypted}'")

        # 対称性の確認
        print(f"対称性確認: {original_text == decrypted}")

    def _demonstrate_key_analysis(self) -> None:
        """キー分析のデモンストレーション"""
        print("=== キー分析デモンストレーション ===")

        # 実際のデータを使用した分析
        encrypted_data = load_encrypted_text()
        key = find_decryption_key(encrypted_data)

        if key:
            decrypted_text = xor_decrypt(encrypted_data, key)
            ascii_sum = calculate_ascii_sum(decrypted_text)
            print(f"発見されたキー: '{key}'")
            print(f"キーのASCII値: {[ord(c) for c in key]}")
            print(f"復号テキスト（最初の100文字）: '{decrypted_text[:100]}...'")
            print(f"ASCII値の合計: {ascii_sum}")

            # キーの特徴分析
            print("\nキーの特徴分析:")
            for i, char in enumerate(key):
                print(f"  位置 {i}: '{char}' (ASCII {ord(char)})")

            # 復号テキストの統計
            print("\n復号テキストの統計:")
            print(f"  文字数: {len(decrypted_text)}")
            print(f"  単語数（概算）: {len(decrypted_text.split())}")
            print(f"  平均ASCII値: {ascii_sum / len(decrypted_text):.2f}")
        else:
            print("キーが見つかりませんでした")

    def _demonstrate_frequency_analysis(self) -> None:
        """頻度分析のデモンストレーション"""
        print("=== 頻度分析デモンストレーション ===")

        encrypted_data = load_encrypted_text()
        key = find_decryption_key(encrypted_data)
        decrypted_text = xor_decrypt(encrypted_data, key) if key else ""

        if decrypted_text:
            # 文字頻度の分析
            char_freq: dict[str, int] = {}
            for char in decrypted_text.lower():
                if char.isalpha() or char == " ":
                    char_freq[char] = char_freq.get(char, 0) + 1

            # 最も頻出する文字トップ10
            sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

            print("最も頻出する文字（トップ10）:")
            for i, (char, count) in enumerate(sorted_chars[:10]):
                percentage = (count / sum(char_freq.values())) * 100
                char_display = repr(char) if char == " " else f"'{char}'"
                print(
                    f"  {i + 1:2d}. {char_display}: {count:3d}回 ({percentage:5.2f}%)"
                )

            # 英語の典型的な頻度との比較
            english_freq_order = ["e", "t", "a", "o", "i", "n", "s", "h", "r", " "]
            actual_freq_order = [char for char, _ in sorted_chars[:10]]

            print(f"\n英語の典型的な頻度順序: {english_freq_order}")
            print(f"実際の頻度順序:         {actual_freq_order}")

            # 一致度の計算
            matches = sum(
                1
                for i in range(min(len(english_freq_order), len(actual_freq_order)))
                if english_freq_order[i] == actual_freq_order[i]
            )
            print(
                f"上位文字の一致度: {matches}/{min(len(english_freq_order), len(actual_freq_order))}"
            )

    def run_problem(self) -> Any:
        """
        メイン問題を実行
        """
        print(f"=== Problem {self.problem_number}: {self.problem_title} ===")
        print()

        # 各解法の実行とパフォーマンス比較
        solution_functions = [
            ("素直な解法", solve_naive),
            ("最適化解法", solve_optimized),
            ("数学的解法", solve_mathematical),
        ]

        results = []
        for name, func in solution_functions:
            try:
                result = func()
                results.append(result)
                print(f"{name}: {result}")
            except Exception as e:
                print(f"{name}: エラー - {e}")
                results.append(0)

        # 結果の一致確認
        if results and len(set(results)) == 1:
            print(f"\n✓ すべての解法が一致: {results[0]}")
            final_result = results[0]
        else:
            print(f"\n✗ 解法間で結果が不一致: {results}")
            final_result = results[0] if results else 0

        print()

        # デモンストレーション実行
        demonstrations = self.get_demonstration_functions()
        if demonstrations:
            for demo_func in demonstrations:
                try:
                    demo_func()
                    print()
                except Exception as e:
                    print(f"デモンストレーションエラー: {e}")
                    print()

        return final_result

    def main(self) -> None:
        """メインエントリーポイント"""
        print(f"=== Problem {self.problem_number} Runner ===")
        print()

        # テスト実行（XOR復号の基本テスト）
        print("=== 基本機能テスト ===")
        test_cases = self.get_test_cases()

        all_passed = True
        for i, (encrypted_data, key, expected) in enumerate(test_cases):
            try:
                result = xor_decrypt(encrypted_data, key)
                if result == expected:
                    print(f"テスト {i + 1}: ✓ 成功")
                else:
                    print(
                        f"テスト {i + 1}: ✗ 失敗 - 期待値: '{expected}', 実際: '{result}'"
                    )
                    all_passed = False
            except Exception as e:
                print(f"テスト {i + 1}: ✗ エラー - {e}")
                all_passed = False

        if all_passed:
            print("✓ 全ての基本テストが通過しました")
        else:
            print("✗ 一部のテストが失敗しました")

        print()

        # メイン問題実行
        self.run_problem()

        print("=== 実行完了 ===")


def main() -> None:
    """エントリーポイント"""
    runner = Problem059Runner(enable_demonstrations=True)
    runner.run_problem()


def run_benchmark() -> None:
    """Run performance benchmarks for all solution approaches."""
    runner = Problem059Runner(enable_performance_test=True)
    runner.run_problem()


if __name__ == "__main__":
    main()
