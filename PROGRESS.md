# Project Euler Progress

このファイルは、Project Eulerの問題の進捗状況を追跡します。

## 進捗状況

| 問題番号 | タイトル | ステータス | 言語 | 完了日 |
|---------|---------|-----------|------|--------|
| 001 | Multiples of 3 and 5 | 🟢 完了 | Python | 2024-12-19 |
| 002 | Even Fibonacci numbers | 🟢 完了 | Python | 2024-12-19 |
| 003 | Largest prime factor | 🟢 完了 | Python | 2024-12-19 |
| 004 | Largest palindrome product | 🟢 完了 | Python | 2024-12-22 |
| ... | ... | ... | ... | ... |

## 凡例

- 🔴 未着手
- 🟡 作業中
- 🟢 完了
- 🔵 最適化済み

## 統計

- 完了: 4/100
- 作業中: 0/100
- 未着手: 96/100

## 目標

- [x] 最初の10問を完了
- [ ] 最初の25問を完了
- [ ] 最初の50問を完了
- [ ] 最初の100問を完了

## 完了した問題の詳細

### Problem 001: Multiples of 3 and 5
- **解答**: 233168
- **実装言語**: Python
- **解法**:
  - 素直な解法 (O(n))
  - 最適化解法 (O(1)) - 等差数列の和の公式
  - リスト内包表記解法 (O(n))
- **ファイル**:
  - `problems/problem_001.py`
  - `solutions/solution_001.md`

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
- **解法**:
  - 素直な解法 (O(n)) - 2から順に試し割りで素因数分解
  - 最適化解法 (O(√n)) - 平方根まで試し割り、残った数が素数かチェック
  - 数学的解法 (O(√n)) - 効率的な素因数分解アルゴリズム
- **ファイル**:
  - `problems/problem_003.py`
  - `solutions/solution_003.md`

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

最終更新: 2024-12-22
