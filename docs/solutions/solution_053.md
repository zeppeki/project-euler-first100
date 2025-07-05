# Problem 053: Combinatoric selections

## 問題概要

Project Euler Problem 53 の詳細な問題文は公式サイトで確認してください。
https://projecteuler.net/problem=53

組み合わせC(n,r) = n! / (r!(n-r)!)において、1 ≤ n ≤ 100の範囲で100万を超える値の個数を求める問題です。

## 解法アプローチ

### 1. 素直な解法 (solve_naive)

**アプローチ**: 全てのC(n,r)を計算して閾値を超える数を数える

**アルゴリズム**:
1. n = 1 から 100まで、各nについて
2. r = 0 から nまで、各rについて
3. C(n,r)を計算して閾値（100万）と比較
4. 閾値を超える場合にカウントを増やす

**時間計算量**: O(n³)
**空間計算量**: O(1)

```python
def solve_naive(max_n: int = 100, threshold: int = 1000000) -> int:
    count = 0

    for n in range(1, max_n + 1):
        for r in range(n + 1):
            if combination_formula(n, r) > threshold:
                count += 1

    return count
```

### 2. 最適化解法 (solve_optimized)

**アプローチ**: 効率的な組み合わせ計算を使用

**アルゴリズム**:
1. 最適化された組み合わせ計算関数を使用
2. 同じ探索範囲だが、より効率的な計算
3. オーバーフローを避けた実装

**時間計算量**: O(n²)
**空間計算量**: O(1)

```python
def solve_optimized(max_n: int = 100, threshold: int = 1000000) -> int:
    count = 0

    for n in range(1, max_n + 1):
        for r in range(n + 1):
            if combination_optimized(n, r) > threshold:
                count += 1

    return count
```

### 3. 数学的解法 (solve_mathematical)

**アプローチ**: 対称性と数学ライブラリを活用

**アルゴリズム**:
1. 組み合わせの対称性 C(n,r) = C(n,n-r) を活用
2. Python標準ライブラリのmath.combを使用
3. 効率的な計算による高速化

**時間計算量**: O(n²)
**空間計算量**: O(1)

```python
def solve_mathematical(max_n: int = 100, threshold: int = 1000000) -> int:
    count = 0

    for n in range(1, max_n + 1):
        for r in range(n + 1):
            if combination_math_lib(n, r) > threshold:
                count += 1

    return count
```

## 核心となるアルゴリズム

### 組み合わせ計算（効率的実装）

オーバーフローを避けた組み合わせ計算:

```python
def combination_formula(n: int, r: int) -> int:
    if r < 0 or r > n or n < 0:
        return 0

    # 対称性を利用: C(n,r) = C(n,n-r)
    r = min(r, n - r)

    if r == 0:
        return 1

    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)

    return result
```

### 数学ライブラリ版

Python標準ライブラリを使用:

```python
def combination_math_lib(n: int, r: int) -> int:
    if r < 0 or r > n or n < 0:
        return 0
    return math.comb(n, r)
```

### パスカルの三角形生成

n行目のパスカルの三角形を生成:

```python
def pascal_triangle_row(n: int) -> list[int]:
    if n < 0:
        return []

    row = [1]
    for r in range(1, n + 1):
        row.append(combination_optimized(n, r))

    return row
```

## 数学的背景

### 組み合わせの基本性質

1. **対称性**: C(n,r) = C(n,n-r)
2. **境界条件**: C(n,0) = C(n,n) = 1
3. **漸化式**: C(n,r) = C(n-1,r-1) + C(n-1,r)

### パスカルの三角形

組み合わせ係数の配列:
```
     1
   1   1
  1  2  1
 1  3  3  1
1  4  6  4  1
```

各行のn番目の値がC(n,r)に対応

### 組み合わせの成長率

C(n,r)の最大値は r ≈ n/2 付近で取られ、指数的に成長:
- C(n, n/2) ≈ 2^n / √(πn/2)

### 閾値分析

C(23,10) = 1,144,066 が初めて100万を超える値
- これより小さいnでは100万を超える値は存在しない
- n ≥ 23 から本格的な探索が必要

## 実装のポイント

### パフォーマンス最適化

1. **対称性活用**: r > n-r の場合は n-r を使用
2. **早期終了**: r=0やr=nの場合は即座に1を返す
3. **整数演算**: 浮動小数点を避けた正確な計算

### 数値安定性

1. **オーバーフロー対策**: 乗除算の順序を最適化
2. **累積計算**: 段階的な乗除算でオーバーフローを防止
3. **ライブラリ活用**: 検証済みのmath.combを併用

### メモリ効率

1. **インプレース計算**: 大きな配列を避けた直接計算
2. **最小限の変数**: 必要最小限のメモリ使用
3. **ジェネレータ**: 大量のデータを一度に保持しない

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** max_n = 100, threshold = 1,000,000
- **解答:** [隠匿]
- **検証:** ✓

## 学習ポイント

### 組み合わせ論の基礎

1. **二項係数**: 組み合わせ係数の数学的性質
2. **パスカルの三角形**: 組み合わせの視覚的表現
3. **成長率**: 指数的成長の理解

### 数値計算の技法

1. **オーバーフロー対策**: 大きな数値の安全な計算
2. **精度保持**: 整数演算による正確な結果
3. **効率性**: 計算量削減のアルゴリズム選択

### アルゴリズム設計

1. **漸化式の活用**: 動的プログラミングとの関連
2. **対称性の利用**: 計算量半減の技法
3. **ライブラリとの比較**: 自作実装と標準実装の比較

## 実用的応用

### 確率論

1. **二項分布**: 試行回数と成功確率からの確率計算
2. **組み合わせ確率**: くじ引きや抽選の確率計算
3. **統計学**: データ分析での組み合わせ応用

### 暗号学

1. **鍵空間**: 可能な鍵の組み合わせ数
2. **組み合わせ攻撃**: 総当たり攻撃の計算量見積もり
3. **情報理論**: 情報量と組み合わせの関係

### コンピュータサイエンス

1. **アルゴリズム解析**: 計算量の組み合わせ論的解析
2. **データ構造**: 組み合わせ的データ構造の設計
3. **最適化問題**: 組み合わせ最適化への応用

## 関連問題

- **Problem 015**: 格子経路（組み合わせによる経路数計算）
- **Problem 020**: 階乗の桁和（階乗計算の応用）
- **Problem 034**: 各桁の階乗の和（階乗の性質）

## 参考資料

- [Combinatorics - Wikipedia](https://en.wikipedia.org/wiki/Combinatorics)
- [Binomial coefficient - Wikipedia](https://en.wikipedia.org/wiki/Binomial_coefficient)
- [Pascal's triangle - Wikipedia](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Combinatorial explosion - Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_explosion)
