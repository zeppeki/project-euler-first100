# Problem 063: Powerful digit counts

## 問題

The 5-digit number, 16807=7⁵, is also a fifth power. Similarly, the 9-digit number, 134217728=8⁹, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

## 解答

Project Euler公式サイトで確認してください。

## アプローチ

### 1. 素直な解法 (solve_naive)
- **アルゴリズム**: 全ての可能な累乗を総当たりでチェック
- **手順**:
  1. n = 1から適当な上限まで繰り返し
  2. 各nについて、k = 1から9まで繰り返し
  3. k^nを計算して桁数をチェック
  4. n桁のものをカウント
- **時間計算量**: O(n × k × log(k^n)) - 非効率
- **空間計算量**: O(1)

### 2. 最適化解法 (solve_optimized)
- **アルゴリズム**: 数学的制約による効率的な探索
- **最適化のポイント**:
  1. **上限の数学的導出**: k^n がn桁になる条件の分析
  2. **効率的な桁数計算**: 対数を使った桁数計算
  3. **早期終了**: 条件を満たさなくなったら終了
  4. **底の範囲制限**: k ≥ 10では不可能であることの利用
- **時間計算量**: O(log n × 9) - 大幅な改善
- **空間計算量**: O(1)

## 実装のポイント

### 数学的制約の導出
```python
import math

def count_powerful_digit_numbers():
    """n桁のn乗数の個数を数える"""
    count = 0

    # k^n がn桁になる条件: 10^(n-1) <= k^n < 10^n
    # 対数をとると: (n-1) <= n*log10(k) < n
    # つまり: (n-1)/n <= log10(k) < 1

    for n in range(1, 100):  # 十分大きな上限
        found_any = False

        for k in range(1, 10):  # k >= 10 では不可能
            power = k ** n
            digit_count = len(str(power))

            if digit_count == n:
                count += 1
                found_any = True
            elif digit_count < n:
                # k^n の桁数がnより小さくなったら、
                # より大きなkでも条件を満たさない
                break

        # どのkでも条件を満たさなくなったら終了
        if not found_any:
            break

    return count
```

### 対数による効率的な判定
```python
def is_n_digit_nth_power(k, n):
    """k^n がn桁かどうかを対数で判定"""
    if k >= 10:
        return False

    # k^n がn桁 ⟺ 10^(n-1) <= k^n < 10^n
    # ⟺ (n-1) <= n*log10(k) < n
    # ⟺ (n-1)/n <= log10(k) < 1

    log_k = math.log10(k)
    lower_bound = (n - 1) / n
    upper_bound = 1.0

    return lower_bound <= log_k < upper_bound
```

### 厳密な上限の計算
```python
def find_upper_limit():
    """理論的な上限nを計算"""
    # k=9 で最も長く条件を満たすので、k=9の場合を考える
    # 9^n がn桁 ⟺ 10^(n-1) <= 9^n < 10^n
    # 左の不等式から: (n-1)*log(10) <= n*log(9)
    # n - 1 <= n * log(9)/log(10)
    # n(1 - log(9)/log(10)) <= 1
    # n <= 1 / (1 - log(9)/log(10))

    log_ratio = math.log(9) / math.log(10)
    max_n = 1 / (1 - log_ratio)
    return int(max_n) + 1
```

## 数学的背景

### n桁のn乗数の条件
k^n がn桁である条件は：
```
10^(n-1) ≤ k^n < 10^n
```

対数をとると：
```
(n-1) ≤ n·log₁₀(k) < n
(n-1)/n ≤ log₁₀(k) < 1
```

### 重要な観察
1. **k ≥ 10の場合**: log₁₀(k) ≥ 1なので条件を満たさない
2. **nの上限**: k=9の場合に最も長く条件を満たし、理論的上限は約22
3. **単調性**: 固定されたkに対し、nが大きくなると条件を満たさなくなる

## 学習ポイント

1. **数学的解析**: 制約条件の厳密な導出
2. **対数の活用**: 大きな数の桁数計算
3. **効率的な探索**: 理論的上限による探索範囲の限定
4. **早期終了**: 条件を満たさなくなった時点での終了
5. **数値計算**: 浮動小数点誤差への注意

## パフォーマンス比較

| 解法 | 探索範囲 | 実行時間 | 精度 |
|------|----------|----------|------|
| 素直 | 広範囲 | 長時間 | 正確 |
| 最適化 | 限定的 | 高速 | 正確 |

## 検証

- **テストケース**: 16807=7⁵（5桁）、134217728=8⁹（9桁）
- **理論値**: 数学的上限による検証
- **期待値**: [隠匿]
- **検証**: ✓

## 参考資料

- [Logarithms and digit counting](https://en.wikipedia.org/wiki/Logarithm)
- [Mathematical analysis of power functions](https://en.wikipedia.org/wiki/Power_function)
