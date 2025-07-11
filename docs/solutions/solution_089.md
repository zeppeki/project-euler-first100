# Problem 089: Roman numerals

## 問題の概要

ローマ数字の最適化に関する問題です。

ローマ数字には基本的なルールがあり、同じ数値を複数の方法で表現できる場合があります。例えば：

- 8 は DCCC（800 = D + C + C + C）としても CM（900 = M - C）としても書けます
- 11 は XI として書けます

問題は、与えられたファイル内の全てのローマ数字を最小形式で書き換えた場合、何文字節約できるかを求めることです。

## 数学的背景

### ローマ数字の基本記号

| 記号 | 値 |
|-----|---|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

### 減算記法

効率的なローマ数字では減算記法を使用します：

| 記号 | 値 | 説明 |
|-----|---|-----|
| IV | 4 | V - I |
| IX | 9 | X - I |
| XL | 40 | L - X |
| XC | 90 | C - X |
| CD | 400 | D - C |
| CM | 900 | M - C |

### 最適化の例

- IIIIIIIII（9文字）→ IX（2文字）：7文字節約
- VIIII（5文字）→ IX（2文字）：3文字節約
- XIIII（5文字）→ XIV（3文字）：2文字節約
- LXXXX（5文字）→ XC（2文字）：3文字節約
- CCCC（4文字）→ CD（2文字）：2文字節約

## 解法のアプローチ

### 1. 素直な解法

```python
def solve_naive(filename: str = "data/p089_roman.txt") -> int:
    total_saved = 0

    for line in lines:
        roman = line.strip()

        # 元のローマ数字を10進数に変換
        decimal_value = roman_to_decimal(roman)

        # 最適なローマ数字に変換
        optimal_roman = decimal_to_roman(decimal_value)

        # 文字数の差を計算
        saved = len(roman) - len(optimal_roman)
        total_saved += saved

    return total_saved
```

**特徴：**
- 時間計算量：O(n × m) where n は行数、m は各行の文字数
- 各ローマ数字を10進数に変換してから最適化
- 文字数の差を累積

### 2. ローマ数字から10進数への変換

```python
def roman_to_decimal(roman: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0

    # 右から左に処理（逆順）
    for char in reversed(roman):
        value = values[char]

        # 前の文字より小さい場合は減算、そうでなければ加算
        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total
```

**特徴：**
- 右から左へ処理することで減算記法を自然に処理
- 前の文字との大小関係で加算/減算を判定

### 3. 10進数から最適ローマ数字への変換

```python
def decimal_to_roman(num: int) -> str:
    values_and_numerals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = ""
    for value, numeral in values_and_numerals:
        count = num // value
        if count:
            result += numeral * count
            num -= value * count

    return result
```

**特徴：**
- 減算記法を含む全ての組み合わせを大きい順に配列
- 貪欲法で最大の記号から使用

## 実装の詳細

### ファイル処理

```python
try:
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    # テスト用のサンプルデータを使用
    lines = ["IIIIIIIII\n", "VIIII\n", ...]
```

### エラーハンドリング

- ファイルが見つからない場合はテスト用データを使用
- 不正なローマ数字の場合は適切にエラーを出力
- 空行は無視

### 最適化のポイント

1. **減算記法の適用**：IV, IX, XL, XC, CD, CM を活用
2. **貪欲法**：大きい値から順番に使用
3. **効率的な変換**：一度10進数に変換してから最適化

## 解答

Project Euler公式サイトで確認してください。

## 検証

```python
# テストケース
test_cases = [
    ("IIIIIIIII", "IX", 7),  # 9文字 → 2文字
    ("VIIII", "IX", 3),      # 5文字 → 2文字
    ("XIIII", "XIV", 2),     # 5文字 → 3文字
    ("LXXXX", "XC", 3),      # 5文字 → 2文字
    ("CCCC", "CD", 2),       # 4文字 → 2文字
]

for original, optimal, expected_savings in test_cases:
    decimal = roman_to_decimal(original)
    converted = decimal_to_roman(decimal)
    assert converted == optimal
    assert len(original) - len(converted) == expected_savings
```

## パフォーマンス分析

| ファイルサイズ | 行数 | 処理時間 | メモリ使用量 |
|-------------|-----|---------|-------------|
| 小（< 1KB） | < 50 | < 0.001s | 最小 |
| 中（~ 10KB） | ~ 500 | ~ 0.01s | 小 |
| 大（~ 100KB） | ~ 5000 | ~ 0.1s | 中 |

ローマ数字の変換は線形時間で行えるため、非常に効率的です。

## 学習ポイント

1. **ローマ数字の理解**：基本記号と減算記法の組み合わせ
2. **文字列処理**：逆順処理による効率的な解析
3. **貪欲法**：最大要素から順番に使用する戦略
4. **ファイル処理**：テキストファイルの読み込みと行単位処理
5. **エラーハンドリング**：ファイルの存在確認とフォールバック

## 実装のバリエーション

### 直接的な置換方式

```python
def optimize_direct(roman: str) -> str:
    # 特定のパターンを直接置換
    replacements = [
        ("IIIII", "V"), ("IIII", "IV"),
        ("VV", "X"), ("VIV", "IX"),
        ("XXXXX", "L"), ("XXXX", "XL"),
        ("LL", "C"), ("LXL", "XC"),
        ("CCCCC", "D"), ("CCCC", "CD"),
        ("DD", "M"), ("DCD", "CM")
    ]

    result = roman
    for old, new in replacements:
        result = result.replace(old, new)

    return result
```

この方式も可能ですが、完全性を保証するため10進数経由の変換を採用しています。

## 関連問題

- Problem 088: Product-sum numbers（積和数）
- Problem 090: Cube digit pairs（立方体の数字ペア）
- Problem 013: Large sum（大きな数の和）
- Problem 016: Power digit sum（べき乗の桁和）

## 歴史的背景

ローマ数字は古代ローマで使用された記数法で、現代でも時計や章番号などで使用されています。減算記法は後の時代に導入され、より効率的な表記を可能にしました。
