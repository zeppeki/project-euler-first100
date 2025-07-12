# Problem 098: Anagramic squares

## 問題文

CARE という単語の各文字を 1, 2, 9, 6 に置き換えることで、平方数 1296 = 36² を作ることができます。

興味深いことに、同じ置き換えを使って、アナグラムである RACE も平方数 9216 = 96² を作ることができます。

CARE（および RACE）を平方アナグラム単語ペアと呼び、先頭にゼロは許可されず、異なる文字が同じ数字の値を持つこともできないことを指定します。

16K の テキストファイル words.txt（右クリックして「リンク/ターゲットを名前を付けて保存...」）を使用して、約2000の一般的な英単語が含まれているファイルから、すべての平方アナグラム単語ペアを見つけてください（回文単語は、それ自体のアナグラムとは見なされません）。

そのようなペアのメンバーによって形成される最大の平方数は何ですか？

注：形成されるすべてのアナグラムは、指定されたテキストファイルに含まれている必要があります。

## アプローチ

### 1. 素直な解法 (Naive Approach)

```python
def solve_naive(filename: str = "p098_words.txt") -> int:
    words = load_words(filename)
    square_pairs = find_square_anagram_pairs(words)

    if not square_pairs:
        return 0

    max_square = 0
    for _, _, square1, square2 in square_pairs:
        max_square = max(max_square, square1, square2)

    return max_square
```

**特徴:**
- 全ての単語ペアと平方数の組み合わせをチェック
- 制約チェック後に最大値を探索
- 実装が分かりやすい

**時間計算量:** O(n × m × s²) where n=単語ペア数, m=文字数, s=平方数
**空間計算量:** O(s + n)

### 2. 最適化解法 (Optimized Approach)

```python
def solve_optimized(filename: str = "p098_words.txt") -> int:
    words = load_words(filename)
    pairs = find_anagram_pairs(words)

    # Group pairs by word length for efficiency
    pairs_by_length = defaultdict(list)
    for pair in pairs:
        length = len(pair[0])
        pairs_by_length[length].append(pair)

    # Process each length group with targeted square generation
    for length, length_pairs in pairs_by_length.items():
        min_val = 10 ** (length - 1) if length > 1 else 1
        max_val = 10 ** length - 1

        squares = generate_squares_in_range(min_val, max_val)
        # Check pairs against these squares
```

**特徴:**
- 文字数別にグループ化して効率化
- 必要な平方数のみを生成
- 早期終了と制約チェック最適化

**時間計算量:** O(n × m × s) - 大幅に改善
**空間計算量:** O(s + n)

### 3. 数学的解法 (Mathematical Approach)

この問題では、数学的最適化は主に効率的な平方数生成とマッピング検証に集約されるため、最適化解法と同じアプローチを使用します。

## 核心となるアルゴリズム

### アナグラム検出

```python
def find_anagram_pairs(words: list[str]) -> list[tuple[str, str]]:
    anagram_groups = defaultdict(list)

    for word in words:
        if len(word) > 1:
            sorted_letters = ''.join(sorted(word))
            anagram_groups[sorted_letters].append(word)

    # Extract pairs from groups with 2+ words
    pairs = []
    for group in anagram_groups.values():
        if len(group) >= 2:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    pairs.append((group[i], group[j]))

    return pairs
```

### 文字→数字マッピング検証

```python
def get_letter_mapping(word1: str, word2: str, num1: int, num2: int) -> dict[str, str] | None:
    str1, str2 = str(num1), str(num2)

    # 制約チェック
    if len(word1) != len(str1) or len(word2) != len(str2):
        return None
    if str1[0] == '0' or str2[0] == '0':  # 先頭ゼロ禁止
        return None

    # 一意マッピング構築
    letter_to_digit = {}
    digit_to_letter = {}

    for word, num_str in [(word1, str1), (word2, str2)]:
        for letter, digit in zip(word, num_str):
            if letter in letter_to_digit:
                if letter_to_digit[letter] != digit:
                    return None  # 矛盾
            else:
                if digit in digit_to_letter:
                    if digit_to_letter[digit] != letter:
                        return None  # 重複
                letter_to_digit[letter] = digit
                digit_to_letter[digit] = letter

    return letter_to_digit
```

### 効率的な平方数生成

```python
def generate_squares_for_length(length: int) -> list[int]:
    min_val = 10 ** (length - 1) if length > 1 else 1
    max_val = 10 ** length - 1

    min_root = int(min_val ** 0.5)
    max_root = int(max_val ** 0.5) + 1

    squares = []
    for root in range(min_root, max_root + 1):
        square = root * root
        if min_val <= square <= max_val:
            squares.append(square)

    return squares
```

## 実装のポイント

### 1. 効率的なデータ構造

- **アナグラムグループ化**: `defaultdict`でO(1)挿入
- **文字数別分類**: 不要な計算を削減
- **平方数キャッシュ**: 再計算を避ける

### 2. 制約チェック最適化

- **早期終了**: 無効条件を最初にチェック
- **段階的検証**: 軽い制約から重い制約へ
- **重複マッピング防止**: 双方向辞書使用

### 3. メモリ効率

- **必要最小限の平方数生成**: 文字数に応じた範囲制限
- **on-demand処理**: 大きなデータセットを一度に保持しない

## 数学的洞察

### 平方数の性質

- **桁数と範囲**: n桁の平方数は 10^(n-1) ≤ square < 10^n
- **平方根の範囲**: 対応する平方根は限定的
- **分布**: 平方数は疎らに分布（大きな数ほど間隔が広い）

### アナグラムの性質

- **文字頻度不変**: ソート後の文字列で同一性判定
- **組み合わせ数**: n文字の単語から最大 n!/2 のペア
- **制約による絞り込み**: 実際の有効ペアは大幅に少ない

## テストケース

### 基本例

```python
# 既知の例
word1, word2 = "CARE", "RACE"
square1, square2 = 1296, 9216  # 36², 96²

# マッピング: C=1, A=2, R=9, E=6
assert apply_mapping("CARE", mapping) == 1296
assert apply_mapping("RACE", mapping) == 9216
```

### エッジケース

```python
# 先頭ゼロ
assert get_letter_mapping("AB", "BA", 10, 1) is None  # "01"は無効

# 重複マッピング
assert get_letter_mapping("AA", "BB", 11, 22) is None  # A→1,1は無効

# 長さ不一致
assert get_letter_mapping("ABC", "DE", 123, 45) is None
```

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** words.txt（約2000単語）
- **解答:** [隠匿]
- **検証:** ✓

## 学習のポイント

1. **組み合わせ最適化**
   - 制約満足問題の効率的解法
   - 早期枝刈りの重要性

2. **アルゴリズム設計**
   - データ構造の選択による性能向上
   - 問題固有の性質の活用

3. **文字列処理**
   - アナグラム検出の効率的実装
   - 文字→数字マッピングの検証

4. **数学的最適化**
   - 平方数生成の範囲制限
   - 計算量削減テクニック

## 発展的考察

### 拡張可能性

- **より大きなデータセット**: スケーラビリティの検討
- **他の数学的性質**: 立方数、完全数への応用
- **並列処理**: 独立な計算の並列化

### 関連問題

- **Problem 079**: パスコード推定（類似の制約満足）
- **Problem 052**: 順列倍数（数字の並び替え）
- **Problem 062**: 立方順列（立方数への拡張）

この問題は、効率的なアルゴリズム設計と数学的洞察の組み合わせで、複雑な制約満足問題を解決する優れた例です。
