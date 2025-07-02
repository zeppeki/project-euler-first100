# Problem 049: Prime permutations

## 問題

算術数列 1487, 4817, 8147 は各項が 3330 ずつ増加しており、次の2つの特殊な性質を持つ：
(i) 3つの項はすべて素数である
(ii) 3つの4桁の数はすべて互いの順列である

この性質を示す1桁、2桁、3桁の素数からなる算術数列は存在しないが、もう1つの4桁の増加数列が存在する。

この数列の3つの項を連結して得られる12桁の数は何か？

## 解答

Project Euler公式サイトで確認してください。

## 解法

この問題は素数の順列グループの中で算術数列を見つける問題である。既知の例 (1487, 4817, 8147) 以外の数列を探す必要がある。

### 1. 素直な解法 (Brute force with basic primality)

**アルゴリズム：**
1. 4桁のすべての素数を生成
2. 桁の順列によってグループ化
3. 各グループで算術数列を探索
4. 既知の例を除外して結果を返す

**時間計算量：** O(n² log n) - n は4桁の素数の数
**空間計算量：** O(n)

```python
def solve_naive() -> int:
    # 4桁の素数をすべて生成
    primes = []
    for n in range(1000, 10000):
        if is_prime(n):
            primes.append(n)

    # 順列グループごとに分類
    permutation_groups = {}
    for prime in primes:
        signature = get_digit_signature(prime)
        if signature not in permutation_groups:
            permutation_groups[signature] = []
        permutation_groups[signature].append(prime)

    # 各グループで算術数列を探す
    for signature, group in permutation_groups.items():
        if len(group) >= 3:
            sequences = find_arithmetic_sequences(group)
            for seq in sequences:
                if seq != (1487, 4817, 8147):
                    return int(f"{seq[0]}{seq[1]}{seq[2]}")
```

**特徴：**
- 実装が直感的
- 基本的な素数判定を使用
- すべての4桁数を順次チェック

### 2. 最適化解法 (Sieve of Eratosthenes)

**アルゴリズム：**
1. エラトステネスの篩で4桁の素数を効率的に生成
2. 素数を順列グループに分類
3. 各グループで算術数列を探索

**時間計算量：** O(n log log n + m²) - n は範囲、m は各グループのサイズ
**空間計算量：** O(n)

```python
def solve_optimized() -> int:
    # エラトステネスの篩で4桁の素数を効率的に生成
    def sieve_of_eratosthenes(limit: int) -> list[bool]:
        is_prime_arr = [True] * (limit + 1)
        is_prime_arr[0] = is_prime_arr[1] = False

        for i in range(2, int(limit**0.5) + 1):
            if is_prime_arr[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime_arr[j] = False

        return is_prime_arr

    is_prime_arr = sieve_of_eratosthenes(9999)
    primes = [n for n in range(1000, 10000) if is_prime_arr[n]]

    # 順列グループ化と算術数列探索
    # ... (rest of implementation)
```

**特徴：**
- 篩を使った高速な素数生成
- メモリ効率的な素数判定
- 大量の素数判定に最適

### 3. 数学的解法 (Optimized arithmetic sequence search)

**アルゴリズム：**
1. エラトステネスの篩で素数生成
2. 順列グループをsetとして管理（高速な検索）
3. 算術数列の性質を利用した効率的な探索

**時間計算量：** O(n log n) - 最適化された探索
**空間計算量：** O(n)

```python
def solve_mathematical() -> int:
    primes = sieve_of_eratosthenes(9999)

    # 順列グループを作成
    permutation_groups = {}
    for prime in primes:
        signature = get_digit_signature(prime)
        if signature not in permutation_groups:
            permutation_groups[signature] = set()
        permutation_groups[signature].add(prime)

    # 3つ以上の順列を持つグループのみ処理
    for signature, group in permutation_groups.items():
        if len(group) >= 3:
            group_list = sorted(list(group))

            # 効率的な算術数列探索
            for i in range(len(group_list)):
                for j in range(i + 1, len(group_list)):
                    a, b = group_list[i], group_list[j]
                    c = b + (b - a)  # 算術数列の第3項

                    if c in group and (a, b, c) != (1487, 4817, 8147):
                        return int(f"{a}{b}{c}")
```

**特徴：**
- setを使った高速な存在チェック
- 算術数列の性質を活用
- 不要な計算を削減

## 数学的背景

### 素数と順列の性質

1. **順列の同値性**: 同じ桁を持つ数は同じ「桁シグネチャ」を持つ
2. **算術数列**: 等差数列 a, a+d, a+2d の形
3. **素数分布**: 4桁の範囲での素数の分布パターン

### 桁シグネチャ

数の桁を並び替えたシグネチャを使って順列グループを識別：

```python
def get_digit_signature(n: int) -> str:
    return "".join(sorted(str(n)))

# 例：
# 1487 → "1478"
# 4817 → "1478"
# 8147 → "1478"
```

### 算術数列の探索

3つの数 a < b < c が算術数列を形成する条件：
- b - a = c - b
- すなわち、c = 2b - a

効率的な探索アルゴリズム：
1. 順列グループ内のすべてのペア (a, b) を考慮
2. c = 2b - a を計算
3. c がグループ内に存在するかチェック

## 検証

**既知の例の確認:**
- 1487, 4817, 8147
- 差分: 4817 - 1487 = 3330, 8147 - 4817 = 3330 ✓
- すべて素数: ✓
- 順列関係: get_digit_signature(1487) = get_digit_signature(4817) = get_digit_signature(8147) = "1478" ✓

**解答の検証:**
- **入力:** 既知の例以外の4桁素数順列算術数列
- **解答:** [隠匿]
- **検証:** 3つの4桁素数の算術数列で互いが順列 ✓

## 学習ポイント

1. **組み合わせ問題**: 素数・順列・算術数列の組み合わせ
2. **効率的な素数生成**: エラトステネスの篩の活用
3. **グループ化アルゴリズム**: 順列による分類手法
4. **数学的最適化**: 算術数列の性質を利用した探索効率化
5. **データ構造の選択**: set vs list の性能差の理解

## 実装のポイント

1. **素数判定の最適化**: 篩を使った一括生成
2. **順列の効率的な分類**: 桁シグネチャによるハッシュ化
3. **算術数列の探索**: 数学的性質を利用した効率化
4. **メモリ管理**: 大量の順列データの効率的な処理

## パフォーマンス分析

| 解法 | 時間計算量 | 特徴 |
|------|------------|------|
| 素直な解法 | O(n² log n) | 基本的な素数判定、直接的な実装 |
| 最適化解法 | O(n log log n + m²) | エラトステネスの篩、高速な素数生成 |
| 数学的解法 | O(n log n) | setによる高速検索、最適化された探索 |

実際の実行では、エラトステネスの篩を使った解法が最も効率的である。

この問題は数論、組み合わせ論、アルゴリズム最適化の良い例を提供している。特に、数学的性質を理解することで計算量を大幅に削減できることが重要である。
