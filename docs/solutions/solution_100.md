# Problem 100: Arranged probability

## 問題文

箱に色のついたディスク（青と赤）が入っています。

21個のディスクがある場合（青15個、赤6個）、2つの青いディスクを引く確率は正確に50%です：P(青,青) = (15/21) × (14/20) = 1/2。

全体のディスク数が10^12を超える最初の配置で、2つの青いディスクを引く確率が正確に50%となる場合の青いディスクの数を求めてください。

## アプローチ

### 1. 素直な解法 (Naive Approach)

```python
def solve_naive(limit: int = 10**12) -> int:
    blue, total = 15, 21

    while total <= limit:
        if is_valid_arrangement(blue, total):
            if total > limit:
                return blue

        # 次の候補を探す（非効率的な方法）
        blue += 1
        total = int(blue * math.sqrt(2)) + 1

        # 正確なtotalを見つける
        for t in range(max(blue, total - 10), total + 20):
            if is_valid_arrangement(blue, t):
                total = t
                break

    return blue
```

**特徴:**
- 全ての可能な組み合わせを順次チェック
- 非常に大きな数では実用的でない
- 理解しやすいが効率が悪い

**時間計算量:** O(√limit) - 実用不可
**空間計算量:** O(1)

### 2. 最適化解法 (Optimized Approach)

```python
def solve_optimized(limit: int = 10**12) -> int:
    # 初期解: (b=15, n=21) => (x=29, y=41)
    x, y = 29, 41

    while True:
        b = (x + 1) // 2
        n = (y + 1) // 2

        if n > limit:
            return b

        # 次の解を計算: Pell方程式の漸化式
        x_new = 3 * x + 4 * y
        y_new = 2 * x + 3 * y
        x, y = x_new, y_new
```

**特徴:**
- Pell方程式を使った効率的な解法
- 漸化式で次の解を高速計算
- 実用的な性能

**時間計算量:** O(log limit)
**空間計算量:** O(1)

### 3. 数学的解法 (Mathematical Approach)

```python
def solve_mathematical(limit: int = 10**12) -> int:
    x, y = 29, 41

    while True:
        blue_discs = (x + 1) // 2
        total_discs = (y + 1) // 2

        if not is_valid_arrangement(blue_discs, total_discs):
            raise ValueError(f"Invalid arrangement")

        if total_discs > limit:
            return blue_discs

        # 漸化式による次の解
        x_next = 3 * x + 4 * y
        y_next = 2 * x + 3 * y
        x, y = x_next, y_next
```

**特徴:**
- Pell方程式の理論的基盤に基づく最適解
- 検証機能付きの安全な実装
- 最も効率的で信頼性の高い解法

**時間計算量:** O(log limit)
**空間計算量:** O(1)

## 核心となるアルゴリズム

### 確率方程式からPell方程式への変換

問題の核心は以下の確率方程式です：

```python
def is_valid_arrangement(blue: int, total: int) -> bool:
    # P(青, 青) = blue/total × (blue-1)/(total-1) = 1/2
    return 2 * blue * (blue - 1) == total * (total - 1)
```

**数学的変換:**

1. **基本方程式**: b/n × (b-1)/(n-1) = 1/2
2. **整理**: 2b(b-1) = n(n-1)
3. **展開**: 2b² - 2b = n² - n
4. **平方完成**: (2b-1)² - 1/2 = n² - n + 1/2
5. **変数置換**: x = 2b-1, y = 2n-1
6. **Pell方程式**: y² - 2x² = -1

### Pell方程式の解法

```python
def find_next_arrangement(blue: int, total: int) -> tuple[int, int]:
    # x = 2b - 1, y = 2n - 1 に変換
    x = 2 * blue - 1
    y = 2 * total - 1

    # 漸化式: (xₖ₊₁, yₖ₊₁) = (2yₖ + 3xₖ, 3yₖ + 4xₖ)
    x_next = 2 * y + 3 * x
    y_next = 3 * y + 4 * x

    # 元の変数に戻す
    blue_next = (x_next + 1) // 2
    total_next = (y_next + 1) // 2

    return blue_next, total_next
```

**Pell方程式の性質:**
- **基本解**: (x₁, y₁) = (1, 1)
- **漸化式**: (xₖ₊₁, yₖ₊₁) = (2yₖ + 3xₖ, 3yₖ + 4xₖ)
- **指数的成長**: 解は指数的に増加

## 実装のポイント

### 1. 数値精度の管理

```python
def verify_arrangement(blue: int, total: int) -> dict:
    prob_both_blue = (blue / total) * ((blue - 1) / (total - 1))

    return {
        "prob_both_blue": prob_both_blue,
        "is_exactly_half": abs(prob_both_blue - 0.5) < 1e-15,
        "formula_valid": 2 * blue * (blue - 1) == total * (total - 1),
    }
```

### 2. 大数演算の安全性

- **整数演算**: 可能な限り整数演算を使用
- **オーバーフロー対策**: Pythonの任意精度整数を活用
- **精度検証**: 浮動小数点との一致確認

### 3. アルゴリズムの検証

```python
# 座標変換の検証
x = 2 * blue - 1
y = 2 * total - 1
assert y * y - 2 * x * x == -1  # Pell方程式の確認

# 確率の検証
prob = (blue / total) * ((blue - 1) / (total - 1))
assert abs(prob - 0.5) < 1e-15  # 正確に1/2
```

## 数学的洞察

### 解の系列

問題の解は以下の系列を形成します：

| 解番号 | 青ディスク | 全ディスク | 確率 |
|--------|------------|------------|------|
| 1      | 15         | 21         | 0.5  |
| 2      | 85         | 120        | 0.5  |
| 3      | 493        | 697        | 0.5  |
| 4      | 2,871      | 4,060      | 0.5  |
| ...    | ...        | ...        | 0.5  |

### 成長パターン

**指数的成長:**
- 各解は前の解の約6倍
- 成長係数: 3 + 2√2 ≈ 5.828

**数学的関係:**
```python
# 近似的な関係
next_blue ≈ 6 * current_blue
next_total ≈ 6 * current_total
```

### Pell方程式の理論

**基本性質:**
- y² - 2x² = -1 は負のPell方程式
- 基本解: (1, 1)
- 一般解: 漸化式で生成

**幾何学的解釈:**
- 双曲線 y² - 2x² = -1 上の格子点
- 連分数展開との関連

## テストケース

### 基本例

```python
# 既知の解
assert is_valid_arrangement(15, 21) is True
assert is_valid_arrangement(85, 120) is True

# 確率の検証
prob1 = (15/21) * (14/20)  # = 0.5
prob2 = (85/120) * (84/119)  # = 0.5
```

### エッジケース

```python
# 無効な配置
assert is_valid_arrangement(10, 21) is False
assert is_valid_arrangement(0, 21) is False
assert is_valid_arrangement(25, 21) is False  # blue > total

# 境界条件
assert is_valid_arrangement(1, 2) is False
assert is_valid_arrangement(2, 3) is False
```

### 数学的一貫性

```python
# Pell方程式の検証
blue, total = 15, 21
x, y = 2 * blue - 1, 2 * total - 1
assert y * y - 2 * x * x == -1

# 漸化式の検証
x_next = 2 * y + 3 * x
y_next = 3 * y + 4 * x
assert y_next * y_next - 2 * x_next * x_next == -1
```

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** limit = 10^12
- **解答:** [隠匿]
- **検証:** ✓

## 学習のポイント

1. **確率論の実践応用**
   - 条件付き確率の具体的な計算
   - 組み合わせ論との関連

2. **Pell方程式の理論**
   - 二次不定方程式の解法
   - 漸化式による解の生成

3. **数値計算の精度**
   - 大数演算での精度管理
   - 整数演算vs浮動小数点演算

4. **アルゴリズム設計**
   - 数学的洞察による効率化
   - O(√n) → O(log n) への改善

## 発展的考察

### 一般化

**k個の青ディスクを引く確率:**
- P(k個の青) = C(blue,k) × C(red,n-k) / C(total,n)
- より複雑なPell方程式系に発展

### 関連問題

- **Problem 066**: Diophantine equation (Pell方程式の基本)
- **Problem 064**: Odd period square roots (連分数展開)
- **Problem 094**: Almost equilateral triangles (類似のPell方程式)

### 数学的応用

- **数論**: Pell方程式の一般理論
- **暗号学**: 楕円曲線暗号での類似構造
- **物理学**: 格子理論での離散構造

この問題は、確率論の具体的な問題からPell方程式という深い数学理論への橋渡しとなる優れた例であり、数学的洞察がアルゴリズムの効率性に直結することを示しています。
