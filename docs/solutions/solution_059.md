# Problem 059: XOR decryption

## 問題概要

Project Euler Problem 59 の詳細な問題文は公式サイトで確認してください。
https://projecteuler.net/problem=59

XOR暗号で暗号化されたテキストを復号し、元のテキストのASCII値の合計を求める問題です。

## 解法アプローチ

### 1. 素直な解法 (solve_naive)

**アプローチ**: 可能な3文字の小文字キーをすべて試して、英語として妥当なテキストが復号できるキーを見つける

**アルゴリズム**:
1. 26^3 = 17,576個の可能なキーを生成
2. 各キーでXOR復号を実行
3. 復号結果が英語テキストとして妥当かを判定
4. 妥当なテキストが見つかったらASCII値の合計を計算

**時間計算量**: O(26^3 × n) - nは暗号化データの長さ
**空間計算量**: O(n)

```python
def solve_naive() -> int:
    encrypted_data = load_encrypted_text()

    for key in generate_three_letter_keys():
        decrypted_text = xor_decrypt(encrypted_data, key)
        if is_valid_english_text(decrypted_text):
            return calculate_ascii_sum(decrypted_text)

    return 0
```

### 2. 最適化解法 (solve_optimized)

**アプローチ**: 頻度分析を使用してキー候補を絞り込む

**アルゴリズム**:
1. 暗号化データの各位置（3で割った余り）での文字頻度を分析
2. 最も頻出するバイトがスペース文字の暗号化と仮定
3. 推定されたキーとその周辺のキーを優先的に試行
4. 失敗した場合は全探索にフォールバック

**時間計算量**: 平均 O(n + k) - kは試行するキー数（通常数十個）
**空間計算量**: O(n)

```python
def solve_optimized() -> int:
    encrypted_data = load_encrypted_text()

    # 頻度分析によるキー推定
    space_ascii = ord(' ')
    position_frequencies = [{} for _ in range(3)]

    for i, byte_val in enumerate(encrypted_data):
        pos = i % 3
        position_frequencies[pos][byte_val] = position_frequencies[pos].get(byte_val, 0) + 1

    # 推定キーの生成と試行
    # ...
```

### 3. 数学的解法 (solve_mathematical)

**アプローチ**: カイ二乗検定による統計的分析を使用

**アルゴリズム**:
1. 英語テキストの理論的文字頻度分布を定義
2. 各キーで復号したテキストの文字頻度を測定
3. カイ二乗検定により理論分布との適合度を計算
4. 最も英語らしいスコアを持つキーを選択

**時間計算量**: O(26^3 + n)
**空間計算量**: O(n)

```python
def solve_mathematical() -> int:
    # 英語の文字頻度分布
    english_freq = {
        'a': 8.12, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.02,
        # ...
    }

    best_score = float('inf')
    best_key = None

    for key in generate_three_letter_keys():
        decrypted_text = xor_decrypt(encrypted_data, key)
        chi_square = calculate_chi_square(decrypted_text, english_freq)

        if chi_square < best_score and is_valid_english_text(decrypted_text):
            best_score = chi_square
            best_key = key
```

## 核心となるアルゴリズム

### XOR復号

XOR演算の対称性を利用: `A XOR B XOR B = A`

```python
def xor_decrypt(encrypted_data: List[int], key: str) -> str:
    decrypted = []
    key_bytes = [ord(c) for c in key]
    key_length = len(key_bytes)

    for i, byte_val in enumerate(encrypted_data):
        key_byte = key_bytes[i % key_length]
        decrypted_byte = byte_val ^ key_byte
        decrypted.append(chr(decrypted_byte))

    return "".join(decrypted)
```

### 英語テキスト判定

```python
def is_valid_english_text(text: str) -> bool:
    if not text:
        return False

    # 印刷可能文字の割合チェック
    printable_ratio = sum(1 for c in text if c.isprintable()) / len(text)
    if printable_ratio < 0.9:
        return False

    # 一般的な英単語の出現チェック
    common_words = ["the", "and", "of", "to", "a", "in", ...]
    text_lower = text.lower()
    word_count = sum(1 for word in common_words if word in text_lower)

    return word_count >= 5
```

## 数学的背景

### XOR暗号の性質

1. **対称性**: `A ⊕ B = B ⊕ A`
2. **逆元**: `A ⊕ B ⊕ B = A`
3. **自己逆元**: `A ⊕ A = 0`

### 頻度分析

英語テキストにおける文字の出現頻度は特徴的なパターンを持ちます：
- 'E'が最も頻出（約12%）
- スペース文字も高頻度（約12%）
- 'Q', 'X', 'Z'は低頻度（1%未満）

### カイ二乗検定

観測された頻度と期待される頻度の差異を測定：

```
χ² = Σ((観測値 - 期待値)² / 期待値)
```

値が小さいほど英語テキストらしい分布を示します。

## 実装のポイント

### パフォーマンス最適化

1. **キー生成の最適化**: 一度生成したキーリストを再利用
2. **早期終了**: 有効なキーが見つかった時点で探索を停止
3. **頻度分析**: 全探索前にキー候補を絞り込み

### エラーハンドリング

1. **ファイル読み込み**: データファイルが存在しない場合のフォールバック
2. **文字コード**: 非ASCII文字や制御文字の適切な処理
3. **境界値**: 空のデータや無効なキーに対する対応

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** 暗号化されたASCIIコードのリスト
- **解答:** [隠匿]
- **検証:** ✓

## 学習ポイント

### 暗号学の基礎

1. **XOR暗号**: 最も基本的な暗号方式の一つ
2. **鍵空間**: 可能な鍵の総数（26³ = 17,576）
3. **暗号解読**: 統計的手法による解読技術

### アルゴリズム設計

1. **全探索vs最適化**: 問題の制約に応じた手法選択
2. **ヒューリスティック**: 頻度分析による探索空間の削減
3. **統計的手法**: カイ二乗検定による客観的評価

### プログラミング技法

1. **文字列処理**: 効率的な文字操作とエンコーディング
2. **データ構造**: 頻度分析のための辞書活用
3. **例外処理**: ロバストなファイル処理

## 関連問題

- **Problem 022**: 名前のスコア計算（ASCII値の利用）
- **Problem 042**: 単語の分類（英語テキストの処理）
- **暗号解読一般**: 頻度分析とパターン認識

## 参考資料

- [XOR cipher - Wikipedia](https://en.wikipedia.org/wiki/XOR_cipher)
- [Frequency analysis - Wikipedia](https://en.wikipedia.org/wiki/Frequency_analysis)
- [Chi-squared test - Wikipedia](https://en.wikipedia.org/wiki/Chi-squared_test)
- [ASCII - Wikipedia](https://en.wikipedia.org/wiki/ASCII)
