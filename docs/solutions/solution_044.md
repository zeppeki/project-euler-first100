# Problem 044: Pentagon numbers

## 問題

五角数は公式 $P_n = n(3n-1)/2$ で生成される。最初の10個の五角数は：

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

$P_4 + P_7 = 22 + 70 = 92 = P_8$ であることが分かる。しかし、それらの差 $70 - 22 = 48$ は五角数ではない。

五角数のペア $P_j$ と $P_k$ について、それらの和と差が両方とも五角数であり、$D = |P_k - P_j|$ が最小となるものを見つけよ。Dの値を求めよ。

## 解答

Project Euler公式サイトで確認してください。

## 解法

この問題は五角数の特殊なペアを見つける問題である。和と差が両方とも五角数になる最小の差を求める必要がある。

### 1. 素直な解法 (Brute Force)

**アルゴリズム：**
1. 五角数を順次生成してリストに保存
2. 全てのペア $(P_j, P_k)$ について和と差を計算
3. 和と差が両方とも五角数かチェック
4. 条件を満たす最小の差を記録

**時間計算量：** O(n²) - 五角数ペアの総当たり
**空間計算量：** O(n) - 五角数のキャッシュ

```python
def solve_naive() -> int:
    pentagonals = []
    n = 1
    min_difference = float('inf')

    while n <= 10000:
        pent = generate_pentagonal(n)
        pentagonals.append(pent)

        # 現在の五角数と過去の五角数の組み合わせをチェック
        for prev_pent in pentagonals[:-1]:
            pk, pj = pent, prev_pent
            pent_sum = pk + pj
            pent_diff = pk - pj

            if is_pentagonal(pent_sum) and is_pentagonal(pent_diff):
                if pent_diff < min_difference:
                    min_difference = pent_diff
        n += 1

    return int(min_difference)
```

**特徴：**
- 実装が分かりやすい
- 全ての可能性を体系的にチェック
- 計算時間が長い

### 2. 最適化解法 (Optimized Search)

**アルゴリズム：**
1. setを使った高速な五角数判定
2. 早期終了条件の導入
3. 適応的探索範囲の設定

**時間計算量：** O(n log n) - 適応的探索と最適化
**空間計算量：** O(n)

```python
def solve_optimized() -> int:
    pentagonals = set()
    pentagonal_list = []
    min_difference = float('inf')

    n = 1
    while n <= 5000:
        pent = generate_pentagonal(n)
        pentagonals.add(pent)
        pentagonal_list.append(pent)

        for prev_pent in pentagonal_list[:-1]:
            pk, pj = pent, prev_pent
            pent_sum = pk + pj
            pent_diff = pk - pj

            if pent_diff >= min_difference:
                continue

            # setを使った高速判定
            if pent_sum in pentagonals and is_pentagonal(pent_diff):
                min_difference = pent_diff

        n += 1

        # 早期終了条件
        if min_difference < 10000:
            # 更に小さい差の可能性をチェック
            continue_search = False
            for i in range(n, min(n + 1000, 5000)):
                test_pent = generate_pentagonal(i)
                if test_pent - pentagonal_list[-1] >= min_difference:
                    continue_search = True
                    break
            if not continue_search:
                break

    return int(min_difference)
```

**特徴：**
- setによる高速な五角数判定 (O(1))
- 早期終了による計算時間短縮
- 適応的探索範囲

### 3. 数学的解法 (Mathematical Approach)

**アルゴリズム：**
より洗練された数学的アプローチで、順序付けられた探索を行う。

**時間計算量：** O(n)
**空間計算量：** O(1)

```python
def solve_mathematical() -> int:
    min_difference = float('inf')

    # j < k の順序で探索
    for j in range(1, 3000):
        pj = generate_pentagonal(j)

        for k in range(j + 1, 3000):
            pk = generate_pentagonal(k)
            pent_sum = pk + pj
            pent_diff = pk - pj

            # 差が現在の最小値以上なら以降の k は無意味
            if pent_diff >= min_difference:
                break

            if is_pentagonal(pent_sum) and is_pentagonal(pent_diff):
                min_difference = pent_diff

    return int(min_difference)
```

## 数学的背景

### 五角数の性質

五角数 $P_n = \frac{n(3n-1)}{2}$ には以下の性質がある：

1. **生成公式**: $P_n = \frac{n(3n-1)}{2}$
2. **逆公式**: $n = \frac{1 + \sqrt{1 + 24P}}{6}$ (Pが五角数の場合)
3. **差分**: $P_{n+1} - P_n = 3n + 1$

### 五角数判定アルゴリズム

数 $P$ が五角数かどうかを判定するには：

1. $\Delta = 1 + 24P$ を計算
2. $\sqrt{\Delta}$ が整数かチェック
3. $(1 + \sqrt{\Delta})$ が6で割り切れるかチェック

```python
def is_pentagonal(num: int) -> bool:
    if num <= 0:
        return False

    discriminant = 1 + 24 * num
    sqrt_discriminant = int(math.sqrt(discriminant))

    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return False

    if (1 + sqrt_discriminant) % 6 != 0:
        return False

    n = (1 + sqrt_discriminant) // 6
    return n > 0 and generate_pentagonal(n) == num
```

### 問題の制約

この問題では以下の条件を満たすペア $(P_j, P_k)$ を探す：

1. $P_j + P_k$ が五角数
2. $P_k - P_j$ が五角数
3. $P_k - P_j$ が最小

## 検証

**例の確認:**
- $P_4 = 22$, $P_7 = 70$, $P_8 = 92$
- $P_4 + P_7 = 92 = P_8$ ✓ (和が五角数)
- $P_7 - P_4 = 48$ は五角数ではない ✗

**解答の検証:**
- **入力:** 五角数の全ペア
- **解答:** [隠匿]
- **検証:** 和と差が両方とも五角数である最小差 ✓

## 学習ポイント

1. **数学的判定**: 逆公式を使った効率的な五角数判定
2. **最適化技法**: 早期終了と適応的探索範囲
3. **データ構造**: setを使った高速検索 (O(1))
4. **探索戦略**: 順序付けられた探索による枝刈り
5. **数値計算**: 平方根の整数判定と割り切れ判定

## 実装のポイント

1. **効率的判定**: 五角数判定の逆公式の実装
2. **メモリ管理**: 必要最小限の五角数のキャッシュ
3. **早期終了**: 無意味な計算の回避
4. **数値精度**: 大きな数での平方根計算の正確性

この問題は数論とアルゴリズム最適化の良い例を提供している。特に、数学的性質を利用した効率的な判定アルゴリズムと、探索の最適化が重要である。
