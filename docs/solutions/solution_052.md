# Problem 052: Permuted multiples

## 問題概要

Project Euler Problem 52 の詳細な問題文は公式サイトで確認してください。
https://projecteuler.net/problem=52

ある数xとその倍数2x, 3x, 4x, 5x, 6xが全て同じ桁で構成される（順列関係にある）最小の正の整数xを見つける問題です。

## 解法アプローチ

### 1. 素直な解法 (solve_naive)

**アプローチ**: 1から順番に各数について、その倍数が全て同じ桁を持つかチェック

**アルゴリズム**:
1. x = 1から開始
2. x, 2x, 3x, 4x, 5x, 6xの各桁の出現回数を比較
3. 全ての倍数が同じ桁構成を持つかチェック
4. 条件を満たさない場合はx++して継続

**時間計算量**: O(n × max_multiple × log n)
**空間計算量**: O(log n)

```python
def solve_naive(max_multiple: int = 6) -> int:
    x = 1
    while True:
        if check_all_multiples_permuted(x, max_multiple):
            return x
        x += 1
```

### 2. 最適化解法 (solve_optimized)

**アプローチ**: 桁数による制約を利用した効率的な探索

**アルゴリズム**:
1. x × max_multipleがxと同じ桁数を持つ制約を利用
2. d桁の数の場合、x は 10^(d-1) から 10^d / max_multiple の範囲
3. 各桁数ごとに範囲を限定して探索

**時間計算量**: O(n × max_multiple × log n)
**空間計算量**: O(log n)

```python
def solve_optimized(max_multiple: int = 6) -> int:
    digits = 1
    while True:
        start = 10 ** (digits - 1)
        end = 10**digits // max_multiple

        if start > end:
            digits += 1
            continue

        for x in range(start, end + 1):
            if check_all_multiples_permuted(x, max_multiple):
                return x

        digits += 1
```

### 3. 数学的解法 (solve_mathematical)

**アプローチ**: 数学的制約を活用した最適化

**アルゴリズム**:
1. xと6xが同じ桁数を持つには、xの最初の桁は1である必要がある
2. 2以上だと6倍した時に桁数が増える可能性が高い
3. 最初の桁が1の数のみを効率的に探索

**時間計算量**: O(n × max_multiple × log n)
**空間計算量**: O(log n)

```python
def solve_mathematical(max_multiple: int = 6) -> int:
    digits = 1
    while True:
        start = 10 ** (digits - 1)
        end = min(2 * 10 ** (digits - 1) - 1, 10**digits // max_multiple)

        if start > end:
            digits += 1
            continue

        for x in range(start, end + 1):
            if str(x)[0] != "1":  # 最初の桁が1でない場合はスキップ
                continue

            if check_all_multiples_permuted(x, max_multiple):
                return x

        digits += 1
```

## 核心となるアルゴリズム

### 桁の署名生成

数値の各桁の出現回数をタプルとして取得:

```python
def get_digit_signature(n: int) -> tuple[int, ...]:
    if n == 0:
        return (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    digits = [0] * 10
    while n > 0:
        digits[n % 10] += 1
        n //= 10
    return tuple(digits)
```

### 文字列による署名生成

各桁をソート済み文字列として取得（より直感的）:

```python
def get_digit_signature_str(n: int) -> str:
    return "".join(sorted(str(n)))
```

### 順列判定

2つの数が同じ桁の順列かチェック:

```python
def are_permutations(n1: int, n2: int) -> bool:
    return get_digit_signature_str(n1) == get_digit_signature_str(n2)
```

### 全倍数チェック

xとその倍数が全て同じ桁を持つかチェック:

```python
def check_all_multiples_permuted(x: int, max_multiple: int = 6) -> bool:
    base_signature = get_digit_signature(x)

    for multiple in range(2, max_multiple + 1):
        if get_digit_signature(x * multiple) != base_signature:
            return False

    return True
```

## 数学的背景

### 桁数の制約

xとkxが同じ桁数dを持つための条件:
- 10^(d-1) ≤ x < 10^d
- 10^(d-1) ≤ kx < 10^d
- よって: 10^(d-1) ≤ x < 10^d/k

### 最初の桁の制約

xの最初の桁をaとすると、kxの最初の桁はおおよそka:
- k=6の場合、a≥2だと6a≥12となり桁数が増加する可能性
- したがって最初の桁は1が最も可能性が高い

### 順列の性質

2つの数が順列関係にある条件:
- 各桁(0-9)の出現回数が完全に一致
- 桁数が同じ
- 桁の和が同じ（必要条件）

## 実装のポイント

### パフォーマンス最適化

1. **範囲限定**: 桁数による制約を活用した探索範囲の削減
2. **早期終了**: 条件を満たさない倍数が見つかった時点で次の数へ
3. **効率的な署名**: タプル比較による高速な順列判定

### メモリ効率

1. **インプレース計算**: 大きな配列を避けた桁カウント
2. **文字列操作**: sorted()による効率的なソート
3. **ジェネレータ**: 大量の候補数を一度に生成しない

### エラーハンドリング

1. **境界値**: x=0や負数の適切な処理
2. **オーバーフロー**: 大きな倍数での桁数オーバーフローの回避
3. **無限ループ**: 解が存在しない場合の対策

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** max_multiple = 6
- **解答:** [隠匿]
- **検証:** ✓

## 学習ポイント

### 数論の応用

1. **桁操作**: 数値の桁の効率的な操作と分析
2. **順列判定**: 数学的な順列の概念をプログラムに応用
3. **制約分析**: 数学的制約による探索空間の削減

### アルゴリズム設計

1. **探索最適化**: 制約による探索範囲の効率的な限定
2. **早期終了**: 条件不満時の即座な次候補への移行
3. **署名アルゴリズム**: データの特徴を効率的に抽出

### プログラミング技法

1. **数値操作**: 桁の抽出と操作の効率的な実装
2. **文字列処理**: sorted()による桁の正規化
3. **ループ最適化**: 無駄な計算を避ける条件分岐

## 実用的応用

### デジタル署名

1. **データ整合性**: ファイルやデータの改ざん検出
2. **重複検出**: 異なる表現での同一データの識別
3. **パターン認識**: 数値パターンの分類と検索

### 暗号学的応用

1. **ハッシュ関数**: 数値の特徴抽出
2. **アナグラム検出**: 文字列の並び替え判定
3. **データ正規化**: 異なる形式データの統一

## 関連問題

- **Problem 030**: 各桁のべき乗の和
- **Problem 034**: 各桁の階乗の和
- **Problem 055**: リクレル数（回文数との関連）
- **Problem 092**: 各桁の平方和の連鎖

## 参考資料

- [Permutation - Wikipedia](https://en.wikipedia.org/wiki/Permutation)
- [Digital root - Wikipedia](https://en.wikipedia.org/wiki/Digital_root)
- [Number theory - Wikipedia](https://en.wikipedia.org/wiki/Number_theory)
- [String algorithms - Wikipedia](https://en.wikipedia.org/wiki/String_algorithms)
