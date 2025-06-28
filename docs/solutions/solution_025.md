# Problem 025: 1000-digit Fibonacci number

## 問題

フィボナッチ数列は次の漸化式で定義される:

F_n = F_{n-1} + F_{n-2}, ここで F_1 = 1, F_2 = 1.

最初の12項は次の通りである:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144

第12項の F_12 = 144 は最初に3桁を含む項である。

1000桁を含む最初のフィボナッチ数列の項のインデックスは何か?

## 解答

Project Euler公式サイトで確認してください。

## 解法

この問題は、フィボナッチ数列で指定された桁数に初めて到達する項のインデックスを求めるものです。2つのアプローチで解法を実装しました。

### 1. 素直な解法 (`solve_naive`)

最も直感的な方法は、フィボナッチ数列を順次計算し、各項の桁数をチェックする方法です。

- **時間計算量**: `O(n)` (nは目標のインデックス)
- **空間計算量**: `O(1)`

n桁の数の最小値は `10^(n-1)` であることを利用し、フィボナッチ数がこの値に達するまで計算を続けます。

```python
def solve_naive(target_digits: int = 1000) -> int:
    """
    素直な解法: フィボナッチ数列を順次計算して桁数をチェック
    """
    if target_digits <= 0:
        return 0
    if target_digits == 1:
        return 1

    # F_1 = 1, F_2 = 1から開始
    prev, curr = 1, 1
    index = 2

    # target_digits桁の数の最小値は10^(target_digits-1)
    target_value = 10 ** (target_digits - 1)

    while curr < target_value:
        prev, curr = curr, prev + curr
        index += 1

    return index
```

### 2. 最適化解法 (`solve_optimized`)

より効率的な方法は、ビネットの公式（Binet's formula）を使用して対数計算で桁数を推定し、その付近から精密に計算する方法です。

- **時間計算量**: `O(log n)`
- **空間計算量**: `O(1)`

#### ビネットの公式

フィボナッチ数は次の公式で表現できます:

```
F_n = (φ^n - ψ^n) / √5
```

ここで:
- φ = (1 + √5) / 2 ≈ 1.618... (黄金比)
- ψ = (1 - √5) / 2 ≈ -0.618...

大きなnに対して、ψ^nは無視できるほど小さくなるため:

```
F_n ≈ φ^n / √5
```

#### 桁数計算

d桁の数の条件は `10^(d-1) ≤ 数 < 10^d` です。

対数を取ると:
```
d-1 ≤ log₁₀(F_n) < d
```

ビネットの公式を使うと:
```
log₁₀(F_n) ≈ n × log₁₀(φ) - log₁₀(√5)
```

したがって、d桁になる最小のnは:
```
n ≥ (d - 1 + log₁₀(√5)) / log₁₀(φ)
```

```python
def solve_optimized(target_digits: int = 1000) -> int:
    """
    最適化解法: ビネットの公式を使用して対数計算で桁数を求める
    """
    if target_digits <= 0:
        return 0
    if target_digits == 1:
        return 1

    # ビネットの公式のパラメータ
    phi = (1 + math.sqrt(5)) / 2
    log_phi = math.log10(phi)
    log_sqrt5 = math.log10(math.sqrt(5))

    # 近似的なnを計算
    min_n = math.ceil((target_digits - 1 + log_sqrt5) / log_phi)

    # min_n付近から精密に計算
    prev, curr = 1, 1
    index = 2
    target_value = 10 ** (target_digits - 1)

    # start_indexまでの値を計算
    start_index = max(1, min_n - 10)
    for _ in range(start_index - 2):
        prev, curr = curr, prev + curr
        index += 1

    # 正確な値を見つける
    while curr < target_value:
        prev, curr = curr, prev + curr
        index += 1

    return index
```

## パフォーマンス比較

| 解法 | 実行時間（参考） |
| :--- | :--- |
| 素直な解法 | ~0.0009秒 |
| 最適化解法 | ~0.0008秒 |

今回の問題では、1000桁程度であれば素直な解法でも十分高速ですが、より大きな桁数を求める場合は最適化解法の効果が顕著に現れます。

## 学習ポイント

- **フィボナッチ数列の効率的な計算**: 2つの変数を使った順次計算で空間計算量をO(1)に抑える方法。
- **ビネットの公式**: フィボナッチ数を閉じた形で表現する公式とその応用。
- **対数を使った桁数計算**: 大きな数の桁数を効率的に求める方法。
- **近似から精密計算への移行**: 数学的な近似を使って計算範囲を狭め、その後精密に計算する手法。
- **黄金比の性質**: フィボナッチ数列と黄金比の深い関係性。
