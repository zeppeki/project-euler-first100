# Problem 042: Coded triangle numbers

## 問題

三角数の第n項は、$t_n = \frac{n(n+1)}{2}$ で与えられる。最初の10個の三角数は：1, 3, 6, 10, 15, 21, 28, 36, 45, 55

単語の各文字をアルファベット順の位置番号（A=1, B=2, ...）に変換し、これらの値を足し合わせることで「単語値」を形成する。例えば、単語「SKY」の単語値は 19 + 11 + 25 = 55 = t₁₀ となる。単語値が三角数の場合、その単語を「三角単語」と呼ぶ。

words.txt（約2000の一般的な英単語を含む16Kのテキストファイル）を使用して、三角単語はいくつあるか？

## 解答

Project Euler公式サイトで確認してください。

## 解法

この問題は以下の手順で解決できる：

1. データファイルから単語リストを読み込む
2. 各単語の「単語値」を計算する（文字のアルファベット位置の合計）
3. その値が三角数かどうか判定する
4. 三角単語の個数をカウントする

### 1. 素直な解法 (Set Lookup Approach)

**アルゴリズム：**
1. 全単語の最大単語値を求める
2. その範囲内の全三角数を事前生成してSetに格納
3. 各単語の単語値を計算し、Setで三角数かどうか高速判定

**時間計算量：** O(n + √max_value) where n is number of words
**空間計算量：** O(√max_value)

```python
def solve_naive() -> int:
    words = load_words()
    max_word_value = max(get_word_value(word) for word in words)
    triangle_numbers = generate_triangle_numbers(max_word_value)

    return sum(1 for word in words
               if get_word_value(word) in triangle_numbers)
```

### 2. 最適化解法 (Mathematical Approach)

**アルゴリズム：**
各単語値について、数学的に三角数かどうか直接判定する。

三角数の公式：$t_n = \frac{n(n+1)}{2} = num$

これを$n$について解くと：$n^2 + n - 2 \cdot num = 0$

二次方程式の解：$n = \frac{-1 + \sqrt{1 + 8 \cdot num}}{2}$

$n$が正の整数なら、$num$は三角数。

**時間計算量：** O(n) where n is number of words
**空間計算量：** O(1)

```python
def is_triangle_number(num: int) -> bool:
    discriminant = 1 + 8 * num
    if discriminant < 0:
        return False

    sqrt_discriminant = math.sqrt(discriminant)
    n = (-1 + sqrt_discriminant) / 2

    return n.is_integer() and n > 0
```

## 数学的背景

### 三角数の性質

三角数は自然数の累積和として定義される：
$$t_n = 1 + 2 + 3 + \cdots + n = \sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

最初のいくつかの三角数：
- $t_1 = 1$
- $t_2 = 3$
- $t_3 = 6$
- $t_4 = 10$
- $t_5 = 15$
- $t_6 = 21$
- $t_7 = 28$
- $t_8 = 36$
- $t_9 = 45$
- $t_{10} = 55$

### 三角数判定の数学的解法

ある数$T$が三角数かどうかを判定するには、以下の方程式を解く：
$$\frac{n(n+1)}{2} = T$$

両辺に2を掛けて整理すると：
$$n^2 + n - 2T = 0$$

二次方程式の解の公式により：
$$n = \frac{-1 \pm \sqrt{1 + 8T}}{2}$$

$n > 0$なので、正の解のみを考慮：
$$n = \frac{-1 + \sqrt{1 + 8T}}{2}$$

$T$が三角数である必要十分条件は、この$n$が正の整数であること。

## 学習ポイント

1. **データ処理**: ファイルから単語データを読み込み、適切に解析
2. **文字列処理**: アルファベット文字を数値に変換する方法
3. **数学的最適化**: 数式による直接判定 vs 事前計算による高速検索
4. **計算量トレードオフ**: 時間計算量と空間計算量のバランス
5. **二次方程式の応用**: 三角数判定への数学的アプローチ

## 実装のポイント

1. **ファイルパス処理**: 相対パスを適切に解決
2. **データ形式**: CSV形式（クォート付き）の適切な解析
3. **浮動小数点精度**: `is_integer()`メソッドによる整数判定
4. **エラーハンドリング**: 平方根の判別式チェック

この問題は文字列処理、数学的解析、アルゴリズム最適化の良い組み合わせを提供している。
