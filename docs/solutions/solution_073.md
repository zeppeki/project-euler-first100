# Problem 073: Counting fractions in a range

## 問題

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the set of reduced proper fractions for d ≤ 12,000?

## 解答

Project Euler公式サイトで確認してください。

## アプローチ

### 1. 素直な解法 (solve_naive)
- **アルゴリズム**: 全分数を生成して範囲内をカウント
- **手順**:
  1. d = 2 to 12,000 の各分母について
  2. n = 1 to d-1 の各分子について
  3. gcd(n, d) = 1 かつ 1/3 < n/d < 1/2 なら カウント
- **時間計算量**: O(d² log d) - GCD計算を含む
- **空間計算量**: O(1)

### 2. 最適化解法 (solve_optimized)
- **アルゴリズム**: 範囲制約による効率的探索
- **最適化のポイント**:
  1. **範囲制約**: 1/3 < n/d < 1/2 から n の範囲を限定
  2. **GCD最適化**: ユークリッドの互除法
  3. **早期終了**: 条件を満たさない場合の処理短縮
- **数学的制約**:
  ```
  1/3 < n/d < 1/2
  d/3 < n < d/2
  ⌊d/3⌋ + 1 ≤ n ≤ ⌈d/2⌉ - 1
  ```
- **時間計算量**: O(d log d) - 大幅な効率化
- **空間計算量**: O(1)

## 実装のポイント

### 範囲計算の最適化
```python
def count_fractions_in_range(max_d):
    count = 0
    for d in range(2, max_d + 1):
        # 1/3 < n/d < 1/2 の範囲を計算
        min_n = d // 3 + 1
        max_n = (d - 1) // 2  # d/2未満の最大整数

        for n in range(min_n, max_n + 1):
            if gcd(n, d) == 1:
                count += 1
    return count
```

### 数学的検証
```python
def verify_range(n, d):
    # 浮動小数点誤差を避けた範囲チェック
    return 3 * n > d and 2 * n < d
```

## 数学的背景

### フェイレイ数列との関係
- **フェイレイ数列 F_n**: 分母がn以下の既約分数の昇順列
- **隣接性**: フェイレイ数列で隣接する分数の性質
- **メディアント**: 二つの分数の間の分数生成

### 既約分数の性質
```
二つの既約分数 a/b と c/d が隣接する条件:
|bc - ad| = 1
```

## 学習ポイント

1. **範囲制約**: 数学的不等式による探索範囲の限定
2. **効率的なGCD**: ユークリッドの互除法の活用
3. **数論的性質**: 既約分数とフェイレイ数列
4. **計算量削減**: 制約条件による大幅な効率化

## 検証

- **小さな例**: d ≤ 8 で3個の確認
- **期待値**: [隠匿]
- **実行時間**: 範囲制約により高速化
- **検証**: ✓

## 参考資料

- [Farey sequence on Wikipedia](https://en.wikipedia.org/wiki/Farey_sequence)
- [Continued fractions and their applications](https://en.wikipedia.org/wiki/Continued_fraction)
