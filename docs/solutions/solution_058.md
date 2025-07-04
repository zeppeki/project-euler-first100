# Problem 058: Spiral primes

## 問題
1から始まり、反時計回りに螺旋を描く正方形の対角線に沿って、素数の割合が10%を下回る最初の正方形の辺の長さを求めよ。

## 詳細
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

```
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
```

興味深いことに、奇数の平方数は右下の対角線に沿って位置しているが、より興味深いのは両対角線に沿った13個の数のうち8個が素数であることである。つまり、比率は8/13 ≈ 62%である。

If one complete new layer is wrapped around the spiral above, a square with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Brute Force)
```python
def solve_naive(target_ratio=0.1):
    side_length = 3

    while True:
        ratio = calculate_prime_ratio(side_length)

        if ratio < target_ratio:
            return side_length

        side_length += 2
```

**特徴:**
- 辺の長さ3から始めて2ずつ増やす
- 各段階で全ての対角線上の値を再計算
- 素数比率が目標値を下回るまで線形探索

**時間計算量:** O(n² × √m) - nは辺の長さ、mは対角線上の最大値
**空間計算量:** O(n)

### 2. 最適化解法 (Incremental Calculation)
```python
def solve_optimized(target_ratio=0.1):
    side_length = 3
    prime_count = 0
    total_count = 1  # 中央の1から始める

    while True:
        # 現在の辺の長さでの対角線の値を取得
        diagonal_values = get_diagonal_values(side_length)

        # 新しい対角線の値で素数をカウント
        new_primes = sum(1 for value in diagonal_values if is_prime(value))

        prime_count += new_primes
        total_count += len(diagonal_values)

        # 比率を計算
        ratio = prime_count / total_count

        if ratio < target_ratio:
            return side_length

        side_length += 2
```

**特徴:**
- 各層の対角線値を段階的に計算
- 素数カウントと総数を累積的に更新
- 重複計算を避けて効率化

**時間計算量:** O(n × √m) - より効率的
**空間計算量:** O(1)

## 数学的背景

### スパイラルの構造
反時計回りスパイラルの各層において、辺の長さnの対角線上の値は以下の公式で計算される：

```python
def get_diagonal_values(side_length):
    # 右下の角 (n²)
    bottom_right = side_length * side_length

    # 右上の角 (n² - (n-1))
    top_right = bottom_right - (side_length - 1)

    # 左上の角 (n² - 2*(n-1))
    top_left = bottom_right - 2 * (side_length - 1)

    # 左下の角 (n² - 3*(n-1))
    bottom_left = bottom_right - 3 * (side_length - 1)

    return [bottom_right, top_right, top_left, bottom_left]
```

### 対角線の値の計算
- **右下の角**: n² (奇数の平方数)
- **右上の角**: n² - (n-1)
- **左上の角**: n² - 2(n-1)
- **左下の角**: n² - 3(n-1)

### 素数判定
```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))
```

**特徴:**
- 2未満は素数ではない
- 2は唯一の偶数素数
- 3以上の奇数について√nまで試し割り

## 具体例

### 辺の長さ3のスパイラル
```
5 4 3
6 1 2
7 8 9
```

**対角線の値**: [1, 3, 5, 7, 9]
- **素数**: 3, 5, 7 (3個)
- **総数**: 5個
- **比率**: 3/5 = 0.6 (60%)

### 辺の長さ5のスパイラル
```
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
```

**対角線の値**: [1, 3, 5, 7, 9, 13, 17, 21, 25]
- **素数**: 3, 5, 7, 13, 17 (5個)
- **総数**: 9個
- **比率**: 5/9 ≈ 0.556 (55.6%)

### 辺の長さ7のスパイラル（問題例）
**対角線の値**: [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]
- **素数**: 3, 5, 7, 13, 17, 31, 37, 43 (8個)
- **総数**: 13個
- **比率**: 8/13 ≈ 0.615 (61.5%)

## パターン分析

### 素数比率の推移
| 辺の長さ | 対角線数 | 素数数 | 総数 | 比率 | パーセント |
|----------|----------|---------|------|------|----------|
| 1        | 1        | 0       | 1    | 0.000 | 0.00%   |
| 3        | 4        | 3       | 5    | 0.600 | 60.00%  |
| 5        | 4        | 2       | 9    | 0.556 | 55.56%  |
| 7        | 4        | 3       | 13   | 0.615 | 61.54%  |
| 9        | 4        | 1       | 17   | 0.471 | 47.06%  |
| 11       | 4        | 1       | 21   | 0.381 | 38.10%  |
| 13       | 4        | 2       | 25   | 0.320 | 32.00%  |

### 比率の傾向
- 初期は高い比率を示す
- 層が増えるにつれて一般的に減少
- 局所的な変動あり（素数の分布による）

## パフォーマンス比較

| 解法 | 時間計算量 | 空間計算量 | 特徴 |
|------|-----------|-----------|------|
| 素直な解法 | O(n²√m) | O(n) | 全体再計算、理解しやすい |
| 最適化解法 | O(n√m) | O(1) | 段階的計算、効率的 |

### 実行時間の傾向
- **小さな目標比率**: 両解法とも高速
- **大きな目標比率**: 最適化の効果が顕著
- **素数判定**: 主要な計算ボトルネック

## 学習ポイント

1. **スパイラルパターンの理解**: 数学的な規則性の発見
2. **段階的計算**: 重複計算の回避による効率化
3. **素数判定の最適化**: √nまでの試し割りアルゴリズム
4. **比率の計算**: 累積的な素数カウント

## 応用と発展

### 関連する数学概念
- **Ulam spiral**: 素数の分布パターン
- **Prime-generating polynomials**: 対角線の値の多項式表現
- **Diophantine equations**: 対角線の値の数論的性質

### スパイラルの変種
- **時計回りスパイラル**: 異なる対角線パターン
- **矩形スパイラル**: 非正方形の螺旋構造
- **3次元スパイラル**: 立体的な螺旋パターン

### 実世界での応用
- **画像処理**: スパイラルスキャンパターン
- **アルゴリズム**: 2次元探索戦略
- **データ構造**: 螺旋配置による効率化

## アルゴリズムの詳細

### 対角線値の生成
```python
def get_all_diagonal_values(side_length):
    all_diagonal_values = [1]  # 中央の1から始める

    # 辺の長さ3から始めて、2ずつ増やす
    for current_side in range(3, side_length + 1, 2):
        diagonal_values = get_diagonal_values(current_side)
        all_diagonal_values.extend(diagonal_values)

    return all_diagonal_values
```

### 素数カウントの最適化
```python
def count_primes_in_diagonals(side_length):
    diagonal_values = get_all_diagonal_values(side_length)

    # 1は素数ではないので除外
    prime_count = sum(1 for value in diagonal_values if value > 1 and is_prime(value))
    total_count = len(diagonal_values)

    return prime_count, total_count
```

## 数学的考察

### 対角線の性質
- **右下対角線**: 完全平方数 (1, 9, 25, 49, ...)
- **他の対角線**: 平方数から等差数列的に減少
- **素数分布**: 対角線における素数の非均等分布

### 確率論的考察
- **素数定理**: 大きな数における素数の密度
- **対角線の特殊性**: 特定の形式の数の素数性
- **比率の収束**: 長期的な素数比率の傾向

## 検証と実装

### 例の検証
```python
def verify_example_spiral():
    side_length = 7
    diagonal_values = get_all_diagonal_values(side_length)

    # 期待される対角線の値
    expected_diagonal = [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]

    # 素数の数をカウント
    prime_count = sum(1 for value in diagonal_values if value > 1 and is_prime(value))

    # 問題文の8個の素数と比較
    return prime_count == 8
```

### エラーハンドリング
- **無効な辺の長さ**: 偶数の辺の長さの処理
- **境界条件**: 1の場合の特別処理
- **数値オーバーフロー**: 大きな数での精度問題

## 関連問題
- Project Euler Problem 028: Number spiral diagonals（数列の対角線）
- Project Euler Problem 035: Circular primes（循環素数）
- Project Euler Problem 037: Truncatable primes（切り詰め可能素数）
- Project Euler Problem 050: Consecutive prime sum（連続素数和）
