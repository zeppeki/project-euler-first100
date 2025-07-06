# Problem 065: Convergents of e

## 問題

The square root of 2 can be written as an infinite continued fraction.

√2 = [1; (2), (2), (2), (2), ...]

The infinite continued fraction can be written, √2 = [1; (2)], indicating that 2 repeats ad infinitum. In a similar way, √23 = [4; (1,3,1,5)].

It turns out that the sequence of partial convergents for continued fractions provide the best rational approximations. Let us consider the convergents for the continued fraction for √2.

Hence the sequence of the first ten convergents for √2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1, ..., 1,2k,1, ...]

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

## 解答

Project Euler公式サイトで確認してください。

## アプローチ

### 1. 素直な解法 (solve_naive)
- **アルゴリズム**: 連分数の定義に従って収束分数を計算
- **手順**:
  1. eの連分数展開パターンを生成
  2. 各項について分数の乗算・加算を実行
  3. 100番目の収束分数を計算
  4. 分子の桁の和を計算
- **時間計算量**: O(n²) - 大きな数の演算
- **空間計算量**: O(n) - 大きな整数の保存

### 2. 最適化解法 (solve_optimized)
- **アルゴリズム**: 漸化式による効率的な収束分数計算
- **最適化のポイント**:
  1. **漸化式活用**: h_n = a_n * h_{n-1} + h_{n-2}
  2. **整数演算**: 分数を分子・分母別々に管理
  3. **パターン認識**: eの連分数の規則的なパターン
  4. **大整数演算**: Pythonの任意精度整数を活用
- **時間計算量**: O(n) - 線形時間
- **空間計算量**: O(log(結果)) - 大整数のサイズ

## 実装のポイント

### eの連分数パターン
```python
def get_e_continued_fraction_term(n):
    """eの連分数のn番目の項を返す"""
    if n == 0:
        return 2  # e = [2; 1,2,1, 1,4,1, 1,6,1, ...]
    elif n % 3 == 2:  # 2,5,8,... の位置
        return 2 * ((n + 1) // 3)
    else:
        return 1

def generate_e_terms(count):
    """eの連分数の最初のcount項を生成"""
    return [get_e_continued_fraction_term(i) for i in range(count)]
```

### 収束分数の漸化式計算
```python
def calculate_convergent(continued_fraction):
    """連分数から収束分数を計算"""
    if not continued_fraction:
        return 0, 1

    # 初期値
    h_prev2, h_prev1 = 1, continued_fraction[0]
    k_prev2, k_prev1 = 0, 1

    for i in range(1, len(continued_fraction)):
        a_i = continued_fraction[i]

        # 漸化式: h_n = a_n * h_{n-1} + h_{n-2}
        h_current = a_i * h_prev1 + h_prev2
        k_current = a_i * k_prev1 + k_prev2

        # 次の反復のための更新
        h_prev2, h_prev1 = h_prev1, h_current
        k_prev2, k_prev1 = k_prev1, k_current

    return h_prev1, k_prev1  # 分子, 分母
```

### 効率的な実装
```python
def solve_optimized(n):
    """n番目の収束分数の分子の桁の和を計算"""
    # 初期値
    h_prev2, h_prev1 = 1, 2  # e = [2; ...]
    k_prev2, k_prev1 = 0, 1

    for i in range(1, n):
        a_i = get_e_continued_fraction_term(i)

        # 漸化式による更新
        h_current = a_i * h_prev1 + h_prev2
        k_current = a_i * k_prev1 + k_prev2

        h_prev2, h_prev1 = h_prev1, h_current
        k_prev2, k_prev1 = k_prev1, k_current

    # 分子の桁の和を計算
    numerator = h_prev1
    return sum(int(digit) for digit in str(numerator))
```

### 桁和の計算
```python
def sum_of_digits(n):
    """大整数の桁の和を効率的に計算"""
    return sum(int(digit) for digit in str(n))

# 代替実装（再帰的）
def sum_of_digits_recursive(n):
    """再帰的な桁の和計算"""
    if n < 10:
        return n
    return n % 10 + sum_of_digits_recursive(n // 10)
```

## 数学的背景

### eの連分数展開
自然対数の底eの連分数展開は美しいパターンを持ちます：
```
e = [2; 1,2,1, 1,4,1, 1,6,1, 1,8,1, ...]
```

一般項：
- a₀ = 2
- a₃ₖ₊₁ = 1 (k ≥ 0)
- a₃ₖ₊₂ = 2(k+1) (k ≥ 0)
- a₃ₖ₊₃ = 1 (k ≥ 0)

### 収束分数の漸化式
連分数 [a₀; a₁, a₂, ...] の収束分数 hₙ/kₙ は：
```
h₋₁ = 1, h₀ = a₀
k₋₁ = 0, k₀ = 1
hₙ = aₙ·hₙ₋₁ + hₙ₋₂
kₙ = aₙ·kₙ₋₁ + kₙ₋₂
```

### 収束分数の性質
- **最良近似**: 収束分数は最良の有理近似を提供
- **交代性**: 収束分数は真の値を交互に上下から近似
- **誤差減少**: 各収束分数はより良い近似を提供

## 学習ポイント

1. **連分数理論**: 無理数の連分数表現と収束分数
2. **漸化式活用**: 効率的な数列計算
3. **大整数演算**: 任意精度算術の重要性
4. **パターン認識**: 数学定数の美しい性質
5. **数値計算**: 高精度計算の実装技法

## パフォーマンス比較

| 解法 | 計算方法 | 精度 | 実行時間 |
|------|----------|------|----------|
| 素直 | 分数演算 | 高 | 長時間 |
| 最適化 | 漸化式 | 高 | 高速 |

## 検証

- **テストケース**: 最初の10項の収束分数確認
- **手計算**: 小さな項での検証
- **期待値**: [隠匿]
- **検証**: ✓

## 参考資料

- [Continued fraction representation of e](https://en.wikipedia.org/wiki/Continued_fraction)
- [Mathematical constant e](https://en.wikipedia.org/wiki/E_(mathematical_constant))
