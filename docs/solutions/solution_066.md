# Problem 066: Diophantine equation

## 問題

Consider the Diophantine equation:

x² - Dy² = 1

For example, when D=13, the minimal solution in x is 649² - 13×180² = 1.

It can be assumed that there are no solutions in positive integers when D is a perfect square.

For D ≤ 1000, find the value of D for which the minimal solution of x² - Dy² = 1 has the largest value of x.

## 解答

Project Euler公式サイトで確認してください。

## アプローチ

### 1. 素直な解法 (solve_naive)
- **アルゴリズム**: 総当たりでペル方程式の解を探索
- **手順**:
  1. 各D（完全平方数でない）について
  2. x, yを1から順次増加させながら試行
  3. x² - Dy² = 1 を満たす最小のxを発見
  4. 全てのDの中で最大のxを持つDを返す
- **時間計算量**: O(D × x_max × y_max) - 非常に非効率
- **空間計算量**: O(1)

### 2. 最適化解法 (solve_optimized)
- **アルゴリズム**: 連分数による効率的なペル方程式解法
- **最適化のポイント**:
  1. **連分数理論**: √Dの連分数展開を利用
  2. **収束分数**: 連分数の収束分数がペル方程式の解
  3. **周期性**: 連分数の周期的性質を活用
  4. **効率的判定**: 大きな数でも高速な解の発見
- **時間計算量**: O(D × P) - Pは連分数の周期
- **空間計算量**: O(P) - 連分数の状態保存

## 実装のポイント

### ペル方程式と連分数の関係
```python
def solve_pell_equation(D):
    """ペル方程式 x² - Dy² = 1 の最小解を連分数で求める"""
    if int(D**0.5)**2 == D:
        return None  # 完全平方数は解なし

    # √D の連分数展開を計算
    m, d, a = 0, 1, int(D**0.5)
    a0 = a

    # 収束分数の初期値
    h_prev, h_curr = 1, a0
    k_prev, k_curr = 0, 1

    while True:
        # 連分数の次の項を計算
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d

        # 収束分数を更新
        h_prev, h_curr = h_curr, a * h_curr + h_prev
        k_prev, k_curr = k_curr, a * k_curr + k_prev

        # ペル方程式の解をチェック
        if h_curr * h_curr - D * k_curr * k_curr == 1:
            return h_curr, k_curr
```

### 効率的な連分数計算
```python
def get_sqrt_continued_fraction(D, max_terms=1000):
    """√D の連分数展開を計算"""
    if int(D**0.5)**2 == D:
        return [int(D**0.5)]  # 完全平方数

    a0 = int(D**0.5)
    m, d, a = 0, 1, a0

    terms = [a0]
    seen_states = {}

    while (m, d) not in seen_states and len(terms) < max_terms:
        seen_states[(m, d)] = len(terms) - 1

        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d

        terms.append(a)

    return terms
```

### 収束分数による解法
```python
def convergents_to_pell_solution(D):
    """連分数の収束分数を使ってペル方程式を解く"""
    cf_terms = get_sqrt_continued_fraction(D)

    if len(cf_terms) == 1:  # 完全平方数
        return None

    # 周期部分を特定
    a0 = cf_terms[0]
    period = cf_terms[1:]

    # 収束分数を計算
    h_prev, h_curr = 1, a0
    k_prev, k_curr = 0, 1

    # 周期を繰り返して解を探す
    for cycle in range(10):  # 十分な回数
        for a in period:
            h_prev, h_curr = h_curr, a * h_curr + h_prev
            k_prev, k_curr = k_curr, a * k_curr + k_prev

            if h_curr * h_curr - D * k_curr * k_curr == 1:
                return h_curr, k_curr

    return None
```

### メイン解法
```python
def solve_optimized(limit):
    """D ≤ limit でペル方程式の最小解のxが最大となるDを求める"""
    max_x = 0
    max_d = 0

    for D in range(2, limit + 1):
        if int(D**0.5)**2 == D:
            continue  # 完全平方数をスキップ

        solution = solve_pell_equation(D)
        if solution:
            x, y = solution
            if x > max_x:
                max_x = x
                max_d = D

    return max_d
```

## 数学的背景

### ペル方程式の理論
ペル方程式 x² - Dy² = 1 は以下の性質を持ちます：
- **基本解**: 最小の正整数解 (x₁, y₁)
- **一般解**: (xₙ, yₙ) = (x₁ + y₁√D)ⁿ の実部・虚部
- **無限解**: 基本解から無限個の解を生成可能

### 連分数との関係
√D の連分数展開の収束分数がペル方程式の解を与えます：
- **周期性**: √D の連分数は周期的
- **収束**: 収束分数はペル方程式の候補解
- **最小解**: 最初にペル方程式を満たす収束分数

### 重要な定理
**定理**: D が完全平方数でない場合、ペル方程式 x² - Dy² = 1 は
√D の連分数展開の収束分数として表される無限個の正整数解を持つ。

## 学習ポイント

1. **ペル方程式**: 古典的なディオファントス方程式の解法
2. **連分数応用**: 連分数理論の実用的応用
3. **数論的性質**: 二次無理数と有理近似
4. **効率的算法**: 大きな数に対する高速解法
5. **数学的美しさ**: 代数と解析の融合

## パフォーマンス比較

| 解法 | 探索方法 | 実行時間 | 最大扱える数 |
|------|----------|----------|-------------|
| 素直 | 総当たり | 非常に長時間 | 小さなD |
| 最適化 | 連分数 | 高速 | 大きなD |

## 検証

- **テストケース**: D=13 で x=649, y=180
- **手計算**: 小さなDでの検証
- **理論検証**: 連分数理論との整合性
- **期待値**: [隠匿]
- **検証**: ✓

## 参考資料

- [Pell's equation on Wikipedia](https://en.wikipedia.org/wiki/Pell%27s_equation)
- [Continued fractions and Pell equations](https://en.wikipedia.org/wiki/Continued_fraction)
