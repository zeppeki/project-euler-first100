# Project Euler Progress

このファイルは、Project Eulerの問題の進捗状況を追跡します。

## 進捗状況

| 問題番号 | タイトル | ステータス | 言語 | 完了日 |
|---------|---------|-----------|------|--------|
| 001 | Multiples of 3 and 5 | 🟢 完了 | Python | 2024-12-19 |
| 002 | Even Fibonacci numbers | 🟢 完了 | Python | 2024-12-19 |
| 003 | Largest prime factor | 🟢 完了 | Python | 2024-12-19 |
| 004 | Largest palindrome product | 🟢 完了 | Python | 2024-12-22 |
| 005 | Smallest multiple | 🟢 完了 | Python | 2024-12-22 |
| 006 | Sum square difference | 🟢 完了 | Python | 2024-12-22 |
| 007 | 10001st prime | 🟢 完了 | Python | 2024-12-22 |
| 008 | Largest product in a series | 🟢 完了 | Python | 2024-12-22 |
| 009 | Special Pythagorean triplet | 🟢 完了 | Python | 2025-06-23 |
| 010 | Summation of primes | 🟢 完了 | Python | 2025-06-23 |
| 011 | Largest product in a grid | 🟢 完了 | Python | 2025-06-23 |
| 012 | Highly divisible triangular number | 🟢 完了 | Python | 2025-06-23 |
| 013 | Large sum | 🟢 完了 | Python | 2025-06-23 |
| 014 | Longest Collatz sequence | 🟢 完了 | Python | 2025-06-23 |
| 015 | Lattice paths | 🟢 完了 | Python | 2025-06-25 |
| 016 | Power digit sum | 🟢 完了 | Python | 2025-06-25 |
| 017 | Number letter counts | 🟢 完了 | Python | 2025-06-25 |
| 018 | Maximum path sum I | 🟢 完了 | Python | 2025-06-25 |
| 019 | Counting Sundays | 🟢 完了 | Python | 2025-06-25 |
| 020 | Factorial digit sum | 🟢 完了 | Python | 2025-06-25 |
| 021 | Amicable numbers | 🟢 完了 | Python | 2025-06-26 |
| 022 | Names scores | 🟢 完了 | Python | 2025-06-26 |
| 023 | Non-Abundant Sums | 🟢 完了 | Python | 2025-06-26 |
| 024 | Lexicographic permutations | 🟢 完了 | Python | 2025-06-27 |
| 025 | 1000-digit Fibonacci number | 🟢 完了 | Python | 2025-06-28 |
| 026 | Reciprocal cycles | 🟢 完了 | Python | 2025-06-28 |
| 027 | Quadratic primes | 🟢 完了 | Python | 2025-06-28 |
| 028 | Number spiral diagonals | 🟢 完了 | Python | 2025-06-28 |
| 029 | Distinct powers | 🟢 完了 | Python | 2025-06-27 |
| 030 | Digit fifth powers | 🟢 完了 | Python | 2025-06-28 |
| 031 | Coin sums | 🟢 完了 | Python | 2025-06-28 |
| 032 | Pandigital products | 🟢 完了 | Python | 2025-06-28 |
| 033 | Digit cancelling fractions | 🟢 完了 | Python | 2025-06-29 |
| 034 | Digit factorials | 🟢 完了 | Python | 2025-06-29 |
| 035 | Circular primes | 🟢 完了 | Python | 2025-06-29 |
| 036 | Double-base palindromes | 🟢 完了 | Python | 2025-06-29 |
| 037 | Truncatable primes | 🟢 完了 | Python | 2025-06-29 |
| 038 | Pandigital multiples | 🟢 完了 | Python | 2025-06-29 |
| 039 | Integer right triangles | 🟢 完了 | Python | 2025-06-29 |
| 040 | Champernowne's constant | 🟢 完了 | Python | 2025-06-29 |
| 041 | Pandigital prime | 🟢 完了 | Python | 2025-06-30 |
| 042 | Coded triangle numbers | 🟢 完了 | Python | 2025-06-30 |
| 043 | Sub-string divisibility | 🟢 完了 | Python | 2025-06-30 |
| 044 | Pentagon numbers | 🟢 完了 | Python | 2025-06-30 |
| 045 | Triangular, pentagonal, and hexagonal | 🟢 完了 | Python | 2025-06-30 |
| 046 | Goldbach's other conjecture | 🟢 完了 | Python | 2025-07-02 |
| 047 | Distinct primes factors | 🟢 完了 | Python | 2025-07-02 |
| 048 | Self powers | 🟢 完了 | Python | 2025-07-02 |
| 049 | Prime permutations | 🟢 完了 | Python | 2025-07-02 |
| 050 | Consecutive prime sum | 🟢 完了 | Python | 2025-07-02 |

## 凡例

- 🔴 未着手
- 🟡 作業中
- 🟢 完了
- 🔵 最適化済み

## 統計

- 完了: 50/100
- 作業中: 0/100
- 未着手: 50/100

## 目標

- [x] 最初の10問を完了 (10/10)
- [x] 最初の25問を完了 (25/25)
- [x] 最初の40問を完了 (40/40) - 100%進捗
- [x] 最初の50問を完了 (50/50) - 100%進捗
- [ ] 最初の100問を完了

## 完了した問題の詳細

### Problem 001: Multiples of 3 and 5
- **解答**: 233168
- **実装言語**: Python
- **解法** (2解法):
  - 素直な解法 (O(n)) - ループで全数をチェック
  - 最適化解法 (O(1)) - 等差数列の和の公式と包除原理
- **ファイル**:
  - `problems/problem_001.py`
  - `solutions/solution_001.md`
- **注意**: 数学的解法を削除 (O(n)のリスト内包表記でO(1)公式と重複)

### Problem 002: Even Fibonacci numbers
- **解答**: 4613732
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - フィボナッチ数列を生成しながら偶数項を合計
  - 最適化解法 (O(log n)) - 偶数項のみを生成する漸化式を使用
  - 数学的解法 (O(log n)) - フィボナッチ数列の偶数項の性質を利用
- **ファイル**:
  - `problems/problem_002.py`
  - `solutions/solution_002.md`

### Problem 003: Largest prime factor
- **解答**: 6857
- **実装言語**: Python
- **解法** (2解法):
  - 素直な解法 (O(n)) - 2から順に試し割りで素因数分解
  - 最適化解法 (O(√n)) - 平方根まで試し割り、残った数が素数かチェック
- **ファイル**:
  - `problems/problem_003.py`
  - `solutions/solution_003.md`
- **注意**: 数学的解法を削除 (最適化解法と完全に同一)

### Problem 004: Largest palindrome product
- **解答**: 906609
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 全ての3桁の数の積をチェック、早期終了あり
  - 最適化解法 (O(n²)) - より効果的な早期終了条件で探索空間を削減
  - 数学的解法 (O(n²)) - 6桁回文が11で割り切れる性質を活用
- **ファイル**:
  - `problems/problem_004.py`
  - `solutions/solution_004.md`

### Problem 005: Smallest multiple
- **解答**: 232792560
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(result × n)) - 1から順番に各数で割り切れるかチェック
  - 最適化解法 (O(n × log(max))) - LCMの性質を利用した効率的計算
  - 数学的解法 (O(n × log(n))) - 素因数分解による直接計算
  - 標準ライブラリ解法 (O(n × log(max))) - Python math.lcm活用
- **ファイル**:
  - `problems/problem_005.py`
  - `solutions/solution_005.md`

### Problem 006: Sum square difference
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - 順次計算による差の算出
  - 最適化解法 (O(1)) - 等差数列の和の公式を活用
  - 数学的解法 (O(1)) - 平方の和の公式を使用
- **ファイル**:
  - `problems/problem_006.py`
  - `solutions/solution_006.md`

### Problem 007: 10001st prime
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 各数について素数判定を実行
  - 最適化解法 (O(n × √p)) - 平方根まで試し割りで素数判定
  - 数学的解法 (O(n log log n)) - エラトステネスの篩を使用
- **ファイル**:
  - `problems/problem_007.py`
  - `solutions/solution_007.md`

### Problem 008: Largest product in a series
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n × k)) - 全ての隣接する桁のシーケンスをチェック
  - 最適化解法 (O(n)) - スライディングウィンドウでゼロスキップ
  - 数学的解法 (O(n)) - reduce関数を使用した効率的な積計算
- **ファイル**:
  - `problems/problem_008.py`
  - `solutions/solution_008.md`

### Problem 009: Special Pythagorean triplet
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n³)) - 3重ループで全ての組み合わせをチェック
  - 最適化解法 (O(n²)) - 2重ループでcを計算により求める
  - 数学的解法 (O(√n)) - 原始ピタゴラス数の生成公式を使用
- **ファイル**:
  - `problems/problem_009.py`
  - `solutions/solution_009.md`

### Problem 011: Largest product in a grid
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(N^2)) - 全方向・全位置から積を計算
  - 最適化解法 (O(N^2)) - 方向ごとに有効な開始位置のみ探索
  - 数学的解法 (O(N^2)) - 範囲限定・最大積シーケンスも特定
- **ファイル**:
  - `problems/problem_011.py`
  - `solutions/solution_011.md`

### Problem 014: Longest Collatz sequence
- **解答**: [隠匿]
- **実装言語**: Python
- **解法** (2解法):
  - 素直な解法 (O(n × L)) - 各数について個別にCollatz数列の長さを計算
  - 最適化解法 (O(n × log L)) - メモ化を使用して計算済みの値を再利用
- **ファイル**:
  - `problems/problem_014.py`
  - `solutions/solution_014.md`
- **注意**: 数学的解法を削除 (実質同じメモ化技法で数学的洞察不十分)

### Problem 015: Lattice paths
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 動的プログラミングで各点までの経路数を計算
  - 最適化解法 (O(n²)) - 動的プログラミングで空間効率を向上
  - 数学的解法 (O(n)) - 組み合わせ論 C(2n,n) を効率的に計算
  - 階乗解法 (O(n)) - math.factorial()を使用した直接計算
- **ファイル**:
  - `problems/problem_015.py`
  - `solutions/solution_015.md`

### Problem 016: Power digit sum
- **解答**: [隠匿]
- **実装言語**: Python
- **解法** (2解法):
  - 素直な解法 (O(power²)) - 2^powerを計算し、剰余演算で桁の和を求める
  - 最適化解法 (O(power²)) - 文字列変換を使用して桁の和を計算
- **ファイル**:
  - `problems/problem_016.py`
  - `docs/solutions/solution_016.md`
- **注意**: 数学的解法を削除 (pow() vs ** の違いのみで本質的に同一)

### Problem 017: Number letter counts
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - 各数値を英語に変換し文字数をカウント
  - 最適化解法 (O(1)) - パターンごとの文字数を事前計算
  - 数学的解法 (O(1)) - パターン分析による効率的な計算
- **ファイル**:
  - `problems/problem_017.py`
  - `docs/solutions/solution_017.md`

### Problem 018: Maximum path sum I
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(2^n)) - 全ての経路を探索
  - 最適化解法 (O(n²)) - 動的プログラミングで最大パス和を計算
- **ファイル**:
  - `problems/problem_018.py`
  - `docs/solutions/solution_018.md`
- **学習ポイント**: 動的プログラミング、三角形の経路問題

### Problem 019: Counting Sundays
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - 各年月の1日が日曜日かチェック
  - 最適化解法 (O(1)) - ツェラーの公式による効率的な曜日計算
- **ファイル**:
  - `problems/problem_019.py`
  - `docs/solutions/solution_019.md`
- **学習ポイント**: 日付計算、モジュロ演算

### Problem 020: Factorial digit sum
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n!)) - 階乗を計算し各桁の和を求める
  - 最適化解法 (O(n)) - math.factorialとstr変換による効率的計算
- **ファイル**:
  - `problems/problem_020.py`
  - `docs/solutions/solution_020.md`
- **学習ポイント**: 大数の桁和計算、階乗の性質

### Problem 021: Amicable numbers
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 各数の真約数の和を計算
  - 最適化解法 (O(n × √n)) - 平方根まで試し割りで真約数の和を計算
- **ファイル**:
  - `problems/problem_021.py`
  - `docs/solutions/solution_021.md`
- **学習ポイント**: 真約数の効率的な計算、友愛数の性質

### Problem 022: Names scores
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n log n)) - 名前をソートして順位とスコアを計算
  - 最適化解法 (O(n log n)) - より効率的なソートとスコア計算
- **ファイル**:
  - `problems/problem_022.py`
  - `docs/solutions/solution_022.md`
- **学習ポイント**: 文字列処理、ソートアルゴリズム

### Problem 023: Non-abundant sums
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 全ての過剰数を見つけて非過剰数和を判定
  - 最適化解法 (O(n × √n)) - 効率的な約数和計算で過剰数を特定
- **ファイル**:
  - `problems/problem_023.py`
  - `docs/solutions/solution_023.md`
- **学習ポイント**: 過剰数の性質、集合演算

### Problem 024: Lexicographic permutations
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(d! × d)) - itertools.permutationsで全順列を生成
  - 最適化解法 (O(d²)) - 階乗の性質を利用した数学的アプローチ
- **ファイル**:
  - `problems/problem_024.py`
  - `docs/solutions/solution_024.md`

### Problem 025: 1000-digit Fibonacci number
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - フィボナッチ数列を順次計算して桁数をチェック
  - 最適化解法 (O(log n)) - ビネットの公式で対数計算による桁数推定
- **ファイル**:
  - `problems/problem_025.py`
  - `docs/solutions/solution_025.md`

### Problem 026: Reciprocal cycles
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 長除法をシミュレートして循環周期を検出
  - 最適化解法 (O(n × log n)) - 法の性質を利用した効率的な周期計算
- **ファイル**:
  - `problems/problem_026.py`
  - `docs/solutions/solution_026.md`

### Problem 027: Quadratic primes
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(p × limit × k)) - 制約を絞り込んだ全探索
  - 最適化解法 (O(n log log n + p × limit × k)) - エラトステネスの篩で素数を事前計算
- **ファイル**:
  - `problems/problem_027.py`
  - `docs/solutions/solution_027.md`

### Problem 028: Number spiral diagonals
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - スパイラルを生成して対角線の和を計算
  - 最適化解法 (O(n)) - 対角線の数列パターンを利用
- **ファイル**:
  - `problems/problem_028.py`
  - `docs/solutions/solution_028.md`
- **学習ポイント**: 数列パターンの認識、スパイラル構造

### Problem 029: Distinct powers
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 全てのべき乗を計算して重複を除去
  - 最適化解法 (O(n²)) - 集合を使用して効率的に重複を除去
- **ファイル**:
  - `problems/problem_029.py`
  - `docs/solutions/solution_029.md`
- **学習ポイント**: べき乗の性質、重複除去

### Problem 030: Digit fifth powers
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - 各数について桁の5乗の和をチェック
  - 最適化解法 (O(n)) - 上限を数学的に求めて探索範囲を限定
- **ファイル**:
  - `problems/problem_030.py`
  - `docs/solutions/solution_030.md`
- **学習ポイント**: 桁のべき乗の性質、探索範囲の数学的限定

### Problem 031: Coin sums
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(2^n)) - 再帰で全ての組み合わせを探索
  - 最適化解法 (O(n × amount)) - 動的プログラミングで組み合わせの数を計算
- **ファイル**:
  - `problems/problem_031.py`
  - `docs/solutions/solution_031.md`
- **学習ポイント**: 動的プログラミング、コイン問題

### Problem 032: Pandigital products
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n!)) - 全ての数の組み合わせをチェック
  - 最適化解法 (O(n²)) - 制約を利用して探索範囲を限定
- **ファイル**:
  - `problems/problem_032.py`
  - `docs/solutions/solution_032.md`
- **学習ポイント**: Pandigital数の性質、探索範囲の限定

### Problem 033: Digit cancelling fractions
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 全ての2桁数の組み合わせをチェック
  - 最適化解法 (O(n²)) - 制約条件で探索範囲を限定
- **ファイル**:
  - `problems/problem_033.py`
  - `docs/solutions/solution_033.md`
- **学習ポイント**: 分数の約分、最大公約数

### Problem 034: Digit factorials
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - 各数について桁の階乗の和をチェック
  - 最適化解法 (O(n)) - 上限を数学的に求めて探索範囲を限定
- **ファイル**:
  - `problems/problem_034.py`
  - `docs/solutions/solution_034.md`
- **学習ポイント**: 階乗の性質、探索範囲の限定

### Problem 035: Circular primes
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 各素数について全ての回転をチェック
  - 最適化解法 (O(n log log n)) - エラトステネスの篩で素数を事前計算
- **ファイル**:
  - `problems/problem_035.py`
  - `docs/solutions/solution_035.md`
- **学習ポイント**: 循環素数の性質、文字列回転

### Problem 036: Double-base palindromes
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - 各数について十進数・二進数の回文判定
  - 最適化解法 (O(n)) - 効率的な回文判定アルゴリズム
- **ファイル**:
  - `problems/problem_036.py`
  - `docs/solutions/solution_036.md`
- **学習ポイント**: 回文数の性質、進数変換

### Problem 037: Truncatable primes
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 各素数について全ての切り捨てをチェック
  - 最適化解法 (O(n log log n)) - エラトステネスの篩で素数を事前計算
- **ファイル**:
  - `problems/problem_037.py`
  - `docs/solutions/solution_037.md`
- **学習ポイント**: 切断可能素数の性質、文字列操作

### Problem 038: Pandigital multiples
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - 各数について連結積をチェック
  - 最適化解法 (O(n)) - 制約条件で探索範囲を限定
- **ファイル**:
  - `problems/problem_038.py`
  - `docs/solutions/solution_038.md`
- **学習ポイント**: Pandigital数の性質、文字列連結

### Problem 039: Integer right triangles
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n³)) - 全ての組み合わせでピタゴラスの定理をチェック
  - 最適化解法 (O(n²)) - 制約条件で探索範囲を限定
- **ファイル**:
  - `problems/problem_039.py`
  - `docs/solutions/solution_039.md`
- **学習ポイント**: ピタゴラスの定理、直角三角形の性質

### Problem 040: Champernowne's constant
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n)) - 数列を順次生成して特定位置の桁を取得
  - 最適化解法 (O(log n)) - 数学的に位置を計算して直接取得
- **ファイル**:
  - `problems/problem_040.py`
  - `docs/solutions/solution_040.md`
- **学習ポイント**: Champernowne定数の性質、数列の位置計算

### Problem 041: Pandigital prime
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n! × √max_number)) - 全てのpandigital数を生成して素数判定
  - 最適化解法 (O(k! × √max_number)) - 大きい桁数から降順で探索し早期終了
  - 数学的解法 (O(k! × √max_number), k≤7) - 桁数の性質を利用して探索範囲を7桁以下に限定
- **ファイル**:
  - `problems/problem_041.py`
  - `docs/solutions/solution_041.md`
- **学習ポイント**: pandigital数の性質、桁数の和による数学的洞察、順列生成

### Problem 042: Coded triangle numbers
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n × m)) - 各単語について三角数かどうかを個別にチェック
  - 最適化解法 (O(n + m log m)) - 三角数を事前計算してセット検索
- **ファイル**:
  - `problems/problem_042.py`
  - `docs/solutions/solution_042.md`
- **学習ポイント**: 三角数の性質、文字列処理、セット検索

### Problem 043: Sub-string divisibility
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n!)) - 全てのpandigital順列について条件をチェック
  - 最適化解法 (O(n)) - 制約条件を利用した効率的な構築アルゴリズム
- **ファイル**:
  - `problems/problem_043.py`
  - `docs/solutions/solution_043.md`
- **学習ポイント**: pandigital数の性質、部分文字列の除算判定、制約満足問題

### Problem 044: Pentagon numbers
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²)) - 全ての五角数のペアについて条件をチェック
  - 最適化解法 (O(n)) - 効率的な五角数判定と探索範囲の限定
- **ファイル**:
  - `problems/problem_044.py`
  - `docs/solutions/solution_044.md`
- **学習ポイント**: 五角数の性質、数式による判定アルゴリズム

### Problem 045: Triangular, pentagonal, and hexagonal
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n × log n)) - 各数について全ての条件をチェック
  - 最適化解法 (O(n)) - 六角数を基準とした効率的な探索
- **ファイル**:
  - `problems/problem_045.py`
  - `docs/solutions/solution_045.md`
- **学習ポイント**: 三角数・五角数・六角数の関係性、数学的最適化

### Problem 046: Goldbach's other conjecture
- **解答**: 5777
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n²√n)) - 各奇数合成数について予想が成り立つかチェック
  - 最適化解法 (O(n log log n + n²√n)) - 事前に素数を生成して効率化
  - 数学的解法 (O(n log log n + n√n)) - 効率的な判定とメモ化を使用
- **ファイル**:
  - `problems/problem_046.py`
- **学習ポイント**: ゴールドバッハの予想、反例探索、素数生成の効率化

### Problem 047: Distinct primes factors
- **解答**: 134043
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n√n)) - 連続する整数をチェック
  - 最適化解法 (O(n√n)) - 効率的な探索とキャッシュの活用
  - 数学的解法 (O(n√n)) - 効率的な素因数分解とパターン分析
- **ファイル**:
  - `problems/problem_047.py`
- **学習ポイント**: 連続する数の素因数分解、キャッシュによる最適化

### Problem 048: Self powers
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n × log n)) - 各項をそのまま計算して足し合わせる
  - 最適化解法 (O(n × log n)) - モジュラー算術を使って各べき乗の計算時に余りを取る
  - 数学的解法 (O(n × log n)) - 末尾の0に寄与しない項のみを効率的に計算
- **ファイル**:
  - `problems/problem_048.py`
- **学習ポイント**: モジュラー算術、大きな数の処理、べき乗計算の最適化

### Problem 049: Prime permutations
- **解答**: [隠匿]
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n² log n)) - 全ての4桁の素数をチェックして順列グループを作り、算術数列を探す
  - 最適化解法 (O(n log log n + m²)) - エラトステネスの篩を使って素数生成を高速化
  - 数学的解法 (O(n log n)) - 算術数列の性質を利用した最適化
- **ファイル**:
  - `problems/problem_049.py`
- **学習ポイント**: 順列、算術数列、素数生成、文字列処理

### Problem 050: Consecutive prime sum
- **解答**: 997651
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n² × √max_sum)) - 全ての連続する素数の和を計算して素数判定
  - 最適化解法 (O(n²)) - 累積和を使用して計算効率を向上
  - 数学的解法 (O(n²)) - 最大長の探索範囲を数学的に制限
- **ファイル**:
  - `problems/problem_050.py`
- **学習ポイント**: 累積和、連続する素数の和、探索範囲の最適化

最終更新: 2025-07-02
