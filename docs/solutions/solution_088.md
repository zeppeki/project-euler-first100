# Problem 088: Product-sum numbers

## 問題の概要

積和数（Product-sum numbers）に関する問題です。

自然数 N が、少なくとも2つの自然数の集合 {a₁, a₂, ..., aₖ} で以下の条件を満たすとき、N を積和数と呼びます：

```
N = a₁ + a₂ + ... + aₖ = a₁ × a₂ × ... × aₖ
```

例えば、6 = 1 + 2 + 3 = 1 × 2 × 3 です。

集合のサイズ k に対して、この性質を持つ最小の N を「最小積和数」と呼びます。

問題は、2 ≤ k ≤ 12000 の範囲で、全ての最小積和数の和（重複は除く）を求めることです。

## 数学的背景

### 積和数の性質

積和数の重要な性質：

1. **k値の計算**：因数の個数を m、それらの積を P、和を S とすると：
   ```
   k = m + (P - S)
   ```
   これは、(P - S) 個の 1 を追加することで積と和を等しくするためです。

2. **最小積和数の上限**：各 k に対する最小積和数は 2k 以下です。
   ```
   k + k = 2k かつ 2 × k = 2k
   ```

3. **探索範囲**：積 P が 2k を超える場合は探索を打ち切れます。

### 具体例

問題文の例：
- k=2: 4 = 2 × 2 = 2 + 2
- k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
- k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
- k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
- k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

## 解法のアプローチ

### 1. 素直な解法

```python
def solve_naive(max_k: int = 12000) -> int:
    k_values = find_minimal_product_sum_numbers(max_k)

    # 重複を除いた和を計算
    unique_values = set()
    for k in range(2, max_k + 1):
        if k in k_values:
            unique_values.add(k_values[k])

    return sum(unique_values)
```

**特徴：**
- 時間計算量：O(n × √n × factors)
- 再帰的探索で全ての因数分解パターンを試す
- 各数について因数分解を行い、積和数となるk値を探す

### 2. 最適化解法

```python
def solve_optimized(max_k: int = 12000) -> int:
    min_product_sum = [float("inf")] * (max_k + 1)
    limit = 2 * max_k

    def search(prod: int, sum_val: int, factors: int, start: int) -> None:
        k = factors + prod - sum_val

        if k <= max_k:
            min_product_sum[k] = min(min_product_sum[k], prod)

            for i in range(start, limit // prod + 1):
                new_prod = prod * i
                if new_prod - sum_val - i + factors + 1 > max_k:
                    break
                search(new_prod, sum_val + i, factors + 1, i)

    search(1, 0, 0, 2)
    unique_values = set(min_product_sum[2:max_k + 1])
    unique_values.discard(float("inf"))

    return int(sum(unique_values))
```

**特徴：**
- 時間計算量：O(n log n)
- 動的計画法を使用して効率的に探索
- 早期終了条件で枝刈りを最適化

### 3. 数学的解法

```python
def solve_mathematical(max_k: int = 12000) -> int:
    ps = [2 * k for k in range(max_k + 1)]  # 初期値: 2k

    def get_product_sum_k(prod: int, sum_val: int, factors: int, start: int) -> None:
        k = factors - sum_val + prod

        if k <= max_k:
            if prod < ps[k]:
                ps[k] = prod

            for i in range(start, 2 * max_k // prod + 1):
                get_product_sum_k(prod * i, sum_val + i, factors + 1, i)

    get_product_sum_k(1, 1, 1, 2)
    return sum(set(ps[2:]))
```

**特徴：**
- 時間計算量：O(k log k)
- 効率的な探索アルゴリズムを使用
- 初期値として 2k を設定し、より小さい値で更新

## 実装の詳細

### 再帰的探索

積和数の探索は再帰的に行います：

```python
def search(product: int, sum_val: int, num_factors: int, min_factor: int) -> None:
    # k = 因数の個数 + (積 - 和) 個の1
    k = num_factors + product - sum_val

    if 2 <= k <= max_k and (k not in min_ps or product < min_ps[k]):
        min_ps[k] = product

    # より大きい因数を探索
    factor = min_factor
    while factor * product <= 2 * max_k:
        if num_factors + 1 + factor * product - sum_val - factor <= max_k:
            search(product * factor, sum_val + factor, num_factors + 1, factor)
        factor += 1
```

### 重複の処理

同じ積和数が複数のkで最小値となる場合があります（例：k=4,5で共に8）。
最終的な合計では重複を除く必要があります。

### 探索の最適化

1. **上限設定**：積が 2×max_k を超える場合は探索終了
2. **早期終了**：k値が max_k を超える場合はスキップ
3. **因数の単調性**：因数を昇順で探索して重複を避ける

## 解答

Project Euler公式サイトで確認してください。

## 検証

```python
# 問題文の例（k=2〜6）
assert solve_optimized(6) == 30

# k=2〜12の場合
assert solve_optimized(12) == 61

# 具体的な最小積和数
k_values = find_minimal_product_sum_numbers(6)
assert k_values[2] == 4
assert k_values[3] == 6
assert k_values[4] == 8
assert k_values[5] == 8  # 重複
assert k_values[6] == 12
```

## パフォーマンス分析

| max_k | 最小積和数の個数 | 実行時間 | メモリ使用量 |
|-------|----------------|----------|-------------|
| 12 | 6個 | < 0.001s | 最小 |
| 100 | ~70個 | ~0.01s | 小 |
| 1,000 | ~700個 | ~0.1s | 中 |
| 12,000 | ~8,000個 | ~1s | 大 |

最適化解法が最も効率的で、数学的解法も高速です。

## 学習ポイント

1. **再帰的探索**：因数分解の系統的な列挙
2. **動的計画法**：最小値の効率的な更新
3. **枝刈り**：探索範囲の数学的制限
4. **重複処理**：セットを使った自動的な重複除去
5. **k値の計算**：積和数の数学的性質の活用

## 関連問題

- Problem 087: Prime power triples（素数べき乗の和）
- Problem 089: Roman numerals（ローマ数字）
- Problem 030: Digit fifth powers（各桁のべき乗和）
- Problem 039: Integer right triangles（直角三角形の整数解）
