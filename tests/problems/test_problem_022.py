#!/usr/bin/env python3
"""
Test for Problem 022: Names Scores
"""

from pathlib import Path

import pytest

from problems.problem_022 import (
    create_sample_names,
    get_alphabetical_value,
    load_names_from_file,
    solve_mathematical,
    solve_naive,
    solve_optimized,
)


class TestProblem022:
    """Problem 022のテストクラス"""

    def test_alphabetical_value_basic(self) -> None:
        """基本的なアルファベット値計算のテスト"""
        test_cases = [
            ("A", 1),
            ("B", 2),
            ("Z", 26),
            ("AA", 2),  # 1 + 1 = 2
            ("AB", 3),  # 1 + 2 = 3
            ("COLIN", 53),  # 3 + 15 + 12 + 9 + 14 = 53
        ]

        for name, expected in test_cases:
            assert get_alphabetical_value(name) == expected, f"Failed for {name}"

    def test_alphabetical_value_case_insensitive(self) -> None:
        """大文字小文字に関係なく正しく計算されることのテスト"""
        test_cases = [
            ("colin", 53),
            ("Colin", 53),
            ("COLIN", 53),
            ("cOlIn", 53),
        ]

        for name, expected in test_cases:
            assert get_alphabetical_value(name) == expected, f"Failed for {name}"

    def test_alphabetical_value_common_names(self) -> None:
        """一般的な名前のアルファベット値テスト"""
        test_cases = [
            ("ANN", 29),  # 1 + 14 + 14 = 29
            ("MARY", 57),  # 13 + 1 + 18 + 25 = 57
            ("JOHN", 47),  # 10 + 15 + 8 + 14 = 47
            (
                "JAMES",
                50,
            ),  # 10 + 1 + 13 + 5 + 19 = 48? Let me recalculate: J(10) + A(1) + M(13) + E(5) + S(19) = 48
        ]

        for name, expected in test_cases:
            actual = get_alphabetical_value(name)
            if name == "JAMES":
                # Let me recalculate JAMES: J(10) + A(1) + M(13) + E(5) + S(19) = 48
                expected = 48
            assert actual == expected, (
                f"Failed for {name}: expected {expected}, got {actual}"
            )

    def test_create_sample_names(self) -> None:
        """サンプル名前リスト作成のテスト"""
        names = create_sample_names()

        # 基本的な検証
        assert isinstance(names, list)
        assert len(names) > 0
        assert "COLIN" in names  # 問題文の例に含まれている

        # すべて大文字の文字列であることを確認
        for name in names:
            assert isinstance(name, str)
            assert name.isupper()
            assert name.isalpha()

    def test_load_names_from_file_with_sample(self) -> None:
        """サンプルファイルからの名前読み込みテスト"""
        data_file = Path(__file__).parent.parent.parent / "data" / "p022_names.txt"

        if data_file.exists():
            names = load_names_from_file(str(data_file))

            # 基本的な検証
            assert isinstance(names, list)
            assert len(names) > 0
            assert "COLIN" in names

            # すべて文字列であることを確認
            for name in names:
                assert isinstance(name, str)
                assert name.isalpha()

    def test_load_names_from_file_not_found(self) -> None:
        """存在しないファイルの読み込みエラーテスト"""
        with pytest.raises(FileNotFoundError):
            load_names_from_file("nonexistent_file.txt")

    def test_solve_naive_basic(self) -> None:
        """素直な解法の基本テスト"""
        # 小さなサンプルでテスト
        names = ["COLIN", "ANN", "MARY"]

        result = solve_naive(names)

        # 手動計算による検証
        # ソート後: ["ANN", "COLIN", "MARY"]
        # ANN: 1位 × 29 = 29
        # COLIN: 2位 × 53 = 106
        # MARY: 3位 × 57 = 171
        # 合計: 29 + 106 + 171 = 306
        expected = 29 + 106 + 171
        assert result == expected

    def test_solve_optimized_basic(self) -> None:
        """最適化解法の基本テスト"""
        names = ["COLIN", "ANN", "MARY"]

        result = solve_optimized(names)

        # 素直な解法と同じ結果であることを確認
        expected = solve_naive(names)
        assert result == expected

    def test_solve_mathematical_basic(self) -> None:
        """数学的解法の基本テスト"""
        names = ["COLIN", "ANN", "MARY"]

        result = solve_mathematical(names)

        # 素直な解法と同じ結果であることを確認
        expected = solve_naive(names)
        assert result == expected

    def test_all_solutions_agree_sample(self) -> None:
        """すべての解法が同じ結果を返すことを確認（サンプルデータ）"""
        names = create_sample_names()

        result_naive = solve_naive(names)
        result_optimized = solve_optimized(names)
        result_math = solve_mathematical(names)

        assert result_naive == result_optimized == result_math

    def test_all_solutions_agree_small_data(self) -> None:
        """すべての解法が同じ結果を返すことを確認（小データ）"""
        test_cases = [
            ["A"],
            ["A", "B"],
            ["B", "A"],  # ソート順序が変わる
            ["COLIN", "ANN", "MARY"],
            ["MARY", "ANN", "COLIN"],  # 異なる初期順序
        ]

        for names in test_cases:
            result_naive = solve_naive(names.copy())
            result_optimized = solve_optimized(names.copy())
            result_math = solve_mathematical(names.copy())

            assert result_naive == result_optimized == result_math, (
                f"Solutions disagree for {names}: "
                f"naive={result_naive}, optimized={result_optimized}, math={result_math}"
            )

    def test_sorting_behavior(self) -> None:
        """ソート動作の確認"""
        names = ["COLIN", "ANN", "MARY", "ALICE", "BOB"]
        original = names.copy()

        # solve_naive は元のリストを変更しない
        solve_naive(names)
        assert names == original

        # solve_optimized も元のリストを変更しない（copyを使用）
        solve_optimized(names)
        assert names == original

        # solve_mathematical も元のリストを変更しない
        solve_mathematical(names)
        assert names == original

    def test_empty_list(self) -> None:
        """空リストの処理テスト"""
        empty_names: list[str] = []

        assert solve_naive(empty_names) == 0
        assert solve_optimized(empty_names) == 0
        assert solve_mathematical(empty_names) == 0

    def test_single_name(self) -> None:
        """単一名前の処理テスト"""
        single_name = ["COLIN"]

        # COLIN = 1位 × 53 = 53
        expected = 53

        assert solve_naive(single_name) == expected
        assert solve_optimized(single_name) == expected
        assert solve_mathematical(single_name) == expected

    def test_duplicate_names(self) -> None:
        """重複する名前の処理テスト"""
        names = ["COLIN", "COLIN", "ANN"]

        # ソート後: ["ANN", "COLIN", "COLIN"]
        # ANN: 1位 × 29 = 29
        # COLIN: 2位 × 53 = 106
        # COLIN: 3位 × 53 = 159
        # 合計: 29 + 106 + 159 = 294
        expected = 29 + 106 + 159

        result_naive = solve_naive(names)
        result_optimized = solve_optimized(names)
        result_math = solve_mathematical(names)

        assert result_naive == result_optimized == result_math == expected

    def test_alphabetical_order_matters(self) -> None:
        """アルファベット順序が重要であることの確認"""
        # 同じ名前、異なる初期順序
        names1 = ["COLIN", "ANN", "MARY"]
        names2 = ["MARY", "COLIN", "ANN"]
        names3 = ["ANN", "MARY", "COLIN"]

        # すべて同じ結果になるべき（ソート後は同じ順序になるため）
        result1 = solve_naive(names1)
        result2 = solve_naive(names2)
        result3 = solve_naive(names3)

        assert result1 == result2 == result3

    def test_position_calculation(self) -> None:
        """位置計算の正確性テスト"""
        names = ["D", "A", "C", "B"]  # ソート後: ["A", "B", "C", "D"]

        # A: 1位 × 1 = 1
        # B: 2位 × 2 = 4
        # C: 3位 × 3 = 9
        # D: 4位 × 4 = 16
        # 合計: 1 + 4 + 9 + 16 = 30
        expected = 30

        assert solve_naive(names) == expected
        assert solve_optimized(names) == expected
        assert solve_mathematical(names) == expected

    def test_colin_example_calculation(self) -> None:
        """問題文のCOLINの例の計算確認"""
        # COLINのアルファベット値は53
        assert get_alphabetical_value("COLIN") == 53

        # 938位での期待スコア: 938 × 53 = 49,714
        expected_score = 938 * 53
        assert expected_score == 49714

    def test_large_sample_data(self) -> None:
        """大きなサンプルデータでのテスト"""
        names = create_sample_names()

        # 基本的な妥当性チェック
        result = solve_naive(names)
        assert result > 0
        assert isinstance(result, int)

        # すべての解法が一致することを確認
        assert solve_optimized(names) == result
        assert solve_mathematical(names) == result

    @pytest.mark.slow
    def test_performance_with_sample_data(self) -> None:
        """サンプルデータでのパフォーマンステスト（機能検証ベース）"""
        names = create_sample_names()

        # すべての解法が同じ結果を返すことを確認
        result_naive = solve_naive(names)
        result_optimized = solve_optimized(names)
        result_math = solve_mathematical(names)

        assert result_naive == result_optimized == result_math
        assert result_naive > 0  # 正の数であることを確認

    def test_data_file_integration(self) -> None:
        """データファイルとの統合テスト"""
        data_file = Path(__file__).parent.parent.parent / "data" / "p022_names.txt"

        if data_file.exists():
            names = load_names_from_file(str(data_file))

            # ファイルから読み込んだデータでの処理テスト
            result_naive = solve_naive(names)
            result_optimized = solve_optimized(names)
            result_math = solve_mathematical(names)

            assert result_naive == result_optimized == result_math
            assert result_naive > 0

            # COLINが含まれていることを確認
            assert "COLIN" in names
        else:
            # データファイルがない場合はテストをスキップ
            pytest.skip("Data file p022_names.txt not found")

    def test_solution_consistency(self) -> None:
        """解答の一貫性テスト"""
        names = create_sample_names()

        # 同じ入力に対して常に同じ結果を返すことを確認
        result1 = solve_naive(names)
        result2 = solve_naive(names)
        result3 = solve_naive(names)

        assert result1 == result2 == result3

    def test_edge_cases(self) -> None:
        """エッジケースのテスト"""
        # 最短名前
        short_names = ["A", "B", "C"]
        result = solve_naive(short_names)
        assert result == 1 * 1 + 2 * 2 + 3 * 3  # 1 + 4 + 9 = 14

        # 長い名前（実際の名前として妥当な範囲）
        long_names = ["ABCDEFGHIJ"]  # A(1)+B(2)+...+J(10) = 55
        result = solve_naive(long_names)
        assert result == 55  # 1位 × 55 = 55

    def test_alphabetical_value_range(self) -> None:
        """アルファベット値の範囲テスト"""
        # 最小値（A）
        assert get_alphabetical_value("A") == 1

        # 最大値（Z）
        assert get_alphabetical_value("Z") == 26

        # 一般的な名前の範囲
        names = create_sample_names()
        for name in names:
            value = get_alphabetical_value(name)
            assert value > 0  # 正の値
            assert value <= 26 * len(name)  # 最大可能値以下

    def test_file_format_parsing(self) -> None:
        """ファイル形式解析のテスト"""
        # 手動でサンプルファイル内容を確認
        data_file = Path(__file__).parent.parent.parent / "data" / "p022_names.txt"

        if data_file.exists():
            with open(data_file, encoding="utf-8") as f:
                content = f.read()

            # カンマ区切りの引用符付き形式であることを確認
            assert '"' in content
            assert "," in content

            # 正しく解析されることを確認
            names = load_names_from_file(str(data_file))
            assert len(names) > 0

            # 引用符が除去されていることを確認
            for name in names[:10]:  # 最初の10個をチェック
                assert '"' not in name
