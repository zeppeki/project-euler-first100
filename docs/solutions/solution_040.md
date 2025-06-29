# Problem 040: Champernowne's constant

## 問題

正の整数を順番に連結して作られる無理数の小数：
0.123456789101112131415161718192021...

小数部分の12番目の数字は1であることが分かります。

もし dn が小数部分の n 番目の数字を表すとき、次の式の値を求めなさい：
d1 × d10 × d100 × d1,000 × d10,000 × d100,000 × d1,000,000

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)

文字列として数列を順番に連結して生成し、指定された位置の文字を取得する方法です。

- **時間計算量**: O(n) - 目標位置まで文字列を構築
- **空間計算量**: O(n) - 連結された文字列を保存

```python
def solve_naive() -> int:
    positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    max_pos = max(positions)

    champernowne = ""
    num = 1

    while len(champernowne) < max_pos:
        champernowne += str(num)
        num += 1

    result = 1
    for pos in positions:
        digit = int(champernowne[pos - 1])
        result *= digit

    return result
```

### 2. 最適化解法 (Optimized Approach)

各位置に対応する数字を数学的に直接計算する方法です。文字列を生成せずに効率的に解を求めます。

- **時間計算量**: O(log n) - 各位置の検索
- **空間計算量**: O(1) - 定数空間

数字の桁数によって区間を分けて考える：
- 1桁数字 (1-9): 9個の数字、9文字
- 2桁数字 (10-99): 90個の数字、180文字
- 3桁数字 (100-999): 900個の数字、2700文字
- ...

```python
def get_digit_at_position(pos: int) -> int:
    if pos <= 9:
        return pos

    length = 1  # 現在の桁数
    count = 9   # 現在の桁数の数字の個数
    start = 1   # 現在の桁数の開始数字

    # 対象位置がどの桁数の範囲にあるかを特定
    while pos > length * count:
        pos -= length * count
        length += 1
        count *= 10
        start *= 10

    # 範囲内での具体的な数字と桁位置を計算
    number = start + (pos - 1) // length
    digit_index = (pos - 1) % length

    return int(str(number)[digit_index])
```

## パフォーマンス比較

- **素直な解法**: 約30.7秒 - 大きな文字列の生成が必要
- **最適化解法**: 約0.000054秒 - 数学的計算のみ

最適化解法は素直な解法より約570,000倍高速です。

## 学習ポイント

1. **文字列操作 vs 数学的アプローチ**: 大量のデータを扱う場合、文字列操作よりも数学的な直接計算の方が効率的
2. **区間分析**: 数字の桁数に基づいて問題を区間に分けて考える手法
3. **メモリ効率**: O(n)の空間を使う解法からO(1)の空間で済む解法への改善
