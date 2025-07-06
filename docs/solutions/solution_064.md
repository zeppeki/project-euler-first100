# Problem 064: Odd period square roots

## 問題

All square roots are periodic when written as continued fractions and can be written in the form:

√N = a₀ + 1/(a₁ + 1/(a₂ + 1/(a₃ + ...)))

For example, let us consider √23:

√23 = 4 + √23 - 4 = 4 + 1/(1/(√23 - 4)) = 4 + 1/(1 + (√23 - 3)/7)

If we continue we would get the following expansion:

√23 = [4; (1,3,1,5), (1,3,1,5), ...]

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4; (1,3,1,5)], to indicate that the block (1,3,1,5) repeats indefinitely.

How many continued fractions for N ≤ 10000 have an odd period?

## 解答

Project Euler公式サイトで確認してください。

## アプローチ

### 1. 素直な解法 (solve_naive)
- **アルゴリズム**: 連分数展開を直接計算
- **手順**:
  1. 各N（完全平方数でない）について連分数展開を計算
  2. 周期を検出するまで展開を続ける
  3. 周期の長さが奇数かどうかを判定
  4. 奇数周期の個数をカウント
- **時間計算量**: O(N × P) - Pは平均周期長
- **空間計算量**: O(P) - 周期検出用

### 2. 最適化解法 (solve_optimized)
- **アルゴリズム**: 効率的な連分数アルゴリズム
- **最適化のポイント**:
  1. **状態管理**: (m, d, a)の三つ組による効率的な状態追跡
  2. **周期検出**: 状態の重複による早期の周期検出
  3. **完全平方数スキップ**: 事前に完全平方数を除外
  4. **メモリ効率**: 最小限の状態情報のみ保持
- **時間計算量**: O(N × log P) - 効率的な周期検出
- **空間計算量**: O(log P) - 状態追跡用

## 実装のポイント

### 連分数展開アルゴリズム
```python
import math

def get_continued_fraction_period(n):
    """√nの連分数展開の周期を計算"""
    if int(math.sqrt(n)) ** 2 == n:
        return 0  # 完全平方数は周期0

    a0 = int(math.sqrt(n))
    m, d, a = 0, 1, a0

    seen_states = {}
    sequence = []

    while (m, d) not in seen_states:
        seen_states[(m, d)] = len(sequence)

        # 次の項を計算
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d

        sequence.append(a)

    # 周期の開始位置を特定
    period_start = seen_states[(m, d)]
    period_length = len(sequence) - period_start

    return period_length
```

### 効率的な完全平方数判定
```python
def is_perfect_square(n):
    """効率的な完全平方数判定"""
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def solve_optimized(limit):
    """奇数周期の連分数の個数を計算"""
    count = 0

    for n in range(2, limit + 1):
        if not is_perfect_square(n):
            period = get_continued_fraction_period(n)
            if period % 2 == 1:
                count += 1

    return count
```

### 状態遷移の詳細
```python
def continued_fraction_expansion_detailed(n):
    """連分数展開の詳細な計算過程"""
    a0 = int(math.sqrt(n))

    # 初期状態
    m, d, a = 0, 1, a0
    expansion = [a0]

    states = []
    while True:
        # 状態更新
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d

        # 状態記録
        state = (m, d, a)
        if state in states:
            period_start = states.index(state)
            period = states[period_start:]
            return expansion[0], [s[2] for s in period]

        states.append(state)
        expansion.append(a)
```

## 数学的背景

### 連分数の理論
二次無理数√Nの連分数展開は必ず周期的になります：
```
√N = [a₀; a₁, a₂, ..., aₖ, a₁, a₂, ..., aₖ, ...]
```

### アルゴリズムの数学的基礎
状態遷移は以下の式で表されます：
```
αᵢ = (a₀ + mᵢ)/dᵢ
aᵢ = ⌊αᵢ⌋
mᵢ₊₁ = dᵢ·aᵢ - mᵢ
dᵢ₊₁ = (N - mᵢ₊₁²)/dᵢ
```

### 周期性の性質
- **周期の開始**: 状態(m, d)の重複で検出
- **周期の長さ**: 一般的にO(√N)程度
- **対称性**: 連分数展開には対称的な性質がある

## 学習ポイント

1. **連分数理論**: 二次無理数の連分数展開
2. **周期検出**: 状態管理による効率的な周期発見
3. **数値計算**: 整数演算による精密な計算
4. **アルゴリズム最適化**: 状態空間の効率的な探索
5. **数学的洞察**: 連分数の周期性と性質

## パフォーマンス比較

| 解法 | 周期検出 | メモリ使用量 | 実行時間 |
|------|----------|-------------|----------|
| 素直 | 線形探索 | 大 | 長時間 |
| 最適化 | 辞書管理 | 小 | 高速 |

## 検証

- **テストケース**: √23 = [4; (1,3,1,5)] の周期4（偶数）
- **理論検証**: 小さなNでの手計算との比較
- **期待値**: [隠匿]
- **検証**: ✓

## 参考資料

- [Continued fraction on Wikipedia](https://en.wikipedia.org/wiki/Continued_fraction)
- [Quadratic irrationals and their continued fractions](https://en.wikipedia.org/wiki/Quadratic_irrational)
