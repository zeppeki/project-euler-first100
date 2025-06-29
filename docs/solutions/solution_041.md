# Problem 041: Pandigital prime

## 問題文

n桁の数がpandigital（汎桁数）であるとは、1からnまでの数字をそれぞれ1回ずつ使用している場合を言います。例えば、2143は4桁のpandigital数であり、素数でもあります。

存在する最大のn桁pandigital素数を求めなさい。

## 解答

Project Euler公式サイトで確認してください。

## 解法

### アプローチ1: 素直な解法 (O(n! × √max_number))

全ての可能なpandigital数を生成して素数判定を行います。

```python
def solve_naive() -> int:
    max_pandigital_prime = 0

    # 1桁から9桁まで順次チェック
    for n in range(1, 10):
        digits = [str(i) for i in range(1, n + 1)]

        # 全ての順列を生成
        for perm in itertools.permutations(digits):
            number = int(''.join(perm))

            # 素数判定
            if is_prime(number):
                max_pandigital_prime = max(max_pandigital_prime, number)

    return max_pandigital_prime
```

**特徴:**
- 全てのpandigital数を網羅的に探索
- 確実に最大値を見つけることができる
- 計算量が大きく、効率的ではない

### アプローチ2: 最適化解法 (O(k! × √max_number))

大きい桁数から降順で探索し、早期終了を利用します。

```python
def solve_optimized() -> int:
    # 9桁から1桁まで降順で探索
    for n in range(9, 0, -1):
        digits = [str(i) for i in range(1, n + 1)]

        # 降順で順列を生成（大きい数から順に）
        for perm in sorted(itertools.permutations(digits), reverse=True):
            number = int(''.join(perm))

            # 素数判定
            if is_prime(number):
                return number  # 最初に見つかった素数が最大値

    return 0
```

**特徴:**
- 最大値から順に探索するため早期終了が可能
- 最初に見つかった素数が確実に最大値
- 実際の探索範囲を大幅に削減

### アプローチ3: 数学的解法 (O(k! × √max_number), k ≤ 7)

桁数の性質を利用した数学的最適化を行います。

```python
def solve_mathematical() -> int:
    # 数学的洞察: 8桁、9桁のpandigital数は3で割り切れる
    # 1+2+...+8 = 36 (3で割り切れる)
    # 1+2+...+9 = 45 (3で割り切れる)

    # 7桁から1桁まで降順で探索
    for n in range(7, 0, -1):
        digits = [str(i) for i in range(1, n + 1)]

        for perm in sorted(itertools.permutations(digits), reverse=True):
            number = int(''.join(perm))

            if is_prime(number):
                return number

    return 0
```

**特徴:**
- 数学的洞察により探索範囲を7桁以下に限定
- 8桁、9桁のpandigital数は必ず3で割り切れることを利用
- 最も効率的な解法

## 重要な洞察

### 桁数の制限

8桁と9桁のpandigital数について重要な数学的性質があります：

- **8桁の場合**: 1+2+3+4+5+6+7+8 = 36
- **9桁の場合**: 1+2+3+4+5+6+7+8+9 = 45

どちらも3で割り切れるため、8桁・9桁のpandigital数は全て3で割り切れます。したがって、3より大きい8桁・9桁のpandigital素数は存在しません。

### pandigital数の性質

- 1からnまでの数字を1回ずつ使用
- 先頭が0になることはない（1以上の数字のみ使用）
- n桁の場合、n!通りの組み合わせが存在

### 素数判定の最適化

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```

- √nまでの奇数のみで試し割り
- 時間計算量: O(√n)

## 計算量分析

| 解法 | 時間計算量 | 空間計算量 | 実際の探索範囲 |
|------|------------|------------|----------------|
| 素直な解法 | O(Σ(k! × √max_k)) | O(max_k!) | 1-9桁全て |
| 最適化解法 | O(k! × √max_number) | O(k!) | 早期終了により削減 |
| 数学的解法 | O(k! × √max_number), k≤7 | O(k!) | 1-7桁のみ |

## 学習ポイント

1. **数学的洞察の重要性**: 桁数の和の性質を理解することで探索範囲を大幅に削減
2. **早期終了の効果**: 降順探索により最初に見つかった解が最適解
3. **pandigital数の生成**: 順列を使った組み合わせ生成
4. **素数判定の最適化**: √nまでの試し割りによる効率化
5. **問題の制約の活用**: 数学的性質を利用した計算量削減

## 検証

```python
# 検証用のテストケース
assert is_prime(2143) and is_pandigital(2143, 4)  # 問題文の例
assert is_prime(4231) and is_pandigital(4231, 4)  # 他の4桁pandigital素数

# 数学的洞察の検証
assert sum(range(1, 9)) % 3 == 0  # 8桁の場合
assert sum(range(1, 10)) % 3 == 0  # 9桁の場合
```
