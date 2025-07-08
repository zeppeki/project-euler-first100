# Problem 78: Coin partitions

## 問題の概要

n枚のコインを異なる積み重ねに分割する方法の数をp(n)とします。例えば、5枚のコインは正確に7通りの異なる方法で分割できるので、p(5)=7です。

p(n)が100万で割り切れる最小のnを求めよ。

## 解法の解説

### 1. 素直な解法：動的計画法

最も直感的なアプローチは、動的計画法を使用して分割数を計算することです。

```python
def partition_function_naive(n: int, modulo: int | None = None) -> int:
    # dp[i][j] = iをj以下の数で分割する方法の数
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 初期値: 0はどんな数でも空の分割で表せる
    for j in range(n + 1):
        dp[0][j] = 1

    # 動的計画法で計算
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # jを使わない場合
            dp[i][j] = dp[i][j - 1]
            # jを使う場合
            if i >= j:
                dp[i][j] += dp[i - j][j]
```

- **時間計算量**: O(n²)
- **空間計算量**: O(n²)

### 2. 最適化解法：オイラーの五角数定理

オイラーの五角数定理を使用すると、分割関数を効率的に計算できます：

```
p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - ...
```

ここで、1, 2, 5, 7, 12, 15, ... は一般化五角数で、k(3k-1)/2 と k(3k+1)/2 の形で表されます。

```python
def partition_function_optimized(n: int, modulo: int | None = None) -> int:
    partition = [0] * (n + 1)
    partition[0] = 1

    for i in range(1, n + 1):
        k = 1
        sign = 1
        while True:
            # 一般化五角数
            pentagonal1 = k * (3 * k - 1) // 2
            pentagonal2 = k * (3 * k + 1) // 2

            if pentagonal1 > i:
                break

            # 再帰的に計算
            partition[i] += sign * partition[i - pentagonal1]
            if pentagonal2 <= i:
                partition[i] += sign * partition[i - pentagonal2]

            sign = -sign
            k += 1
```

- **時間計算量**: O(n√n)
- **空間計算量**: O(n)

### 3. 数学的背景

分割関数は数論において重要な関数で、以下の性質を持ちます：

1. **母関数**: 分割関数の母関数は以下で表されます：
   ```
   Σ p(n)x^n = Π (1/(1-x^k)) for k=1,2,3,...
   ```

2. **オイラーの恒等式**: オイラーは以下の美しい恒等式を発見しました：
   ```
   Π (1-x^k) = Σ (-1)^k x^(k(3k-1)/2)
   ```

3. **漸近的振る舞い**: Hardy-Ramanujanの公式により：
   ```
   p(n) ~ (1/4n√3) exp(π√(2n/3))
   ```

## 実装のポイント

1. **剰余演算の最適化**: 100万で割った余りのみを保持することで、大きな数の計算を避ける

2. **五角数の効率的な生成**: k(3k±1)/2の形の数を直接計算

3. **符号の管理**: (-1)^(k-1)のパターンに従って加算と減算を交互に行う

## 計算例

小さなnについての分割数：
- p(0) = 1
- p(1) = 1
- p(2) = 2
- p(3) = 3
- p(4) = 5
- p(5) = 7
- p(6) = 11
- p(7) = 15
- p(8) = 22
- p(9) = 30
- p(10) = 42

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** p(n)が1,000,000で割り切れる最小のn
- **解答:** [隠匿]
- **検証:** ✓
