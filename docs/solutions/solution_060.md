# Problem 060: Prime pair sets

## 問題概要

Project Euler Problem 60 の詳細な問題文は公式サイトで確認してください。
https://projecteuler.net/problem=60

任意の2つの素数を連結した結果が常に素数になる5つの素数の集合を見つけ、その最小の和を求める問題です。

## 解法アプローチ

### 1. 素直な解法 (solve_naive)

**アプローチ**: 全ての素数の組み合わせをチェックして完全な素数ペア集合を探索

**アルゴリズム**:
1. エラトステネスの篩で指定範囲の素数を生成
2. 指定サイズの全ての素数の組み合わせを生成
3. 各組み合わせが完全な素数ペア集合を形成するかチェック
4. 条件を満たす集合の中で最小の和を返す

**時間計算量**: O(C(n,k) × k² × √(max(concat)))
**空間計算量**: O(n)

```python
def solve_naive(set_size: int = 5, prime_limit: int = 10000) -> int:
    # 素数を生成
    is_prime_array = sieve_of_eratosthenes(prime_limit)
    primes = [i for i in range(2, prime_limit + 1) if is_prime_array[i]]

    min_sum = float('inf')

    # 全ての組み合わせをチェック
    for prime_set in combinations(primes, set_size):
        if can_form_complete_set(list(prime_set), set_size):
            current_sum = sum(prime_set)
            min_sum = min(min_sum, current_sum)

    return int(min_sum) if min_sum != float('inf') else -1
```

### 2. 最適化解法 (solve_optimized)

**アプローチ**: 段階的に素数ペア集合を構築し、枝刈りによる効率化

**アルゴリズム**:
1. 素数を生成
2. 再帰的に集合を構築：
   - 現在の集合の全ての素数とペアを形成できる素数のみを追加
   - 現在の合計が最小値を超えている場合は枝刈り
3. 目標サイズに達したら最小値を更新

**時間計算量**: O(n^k × √(max(concat)))
**空間計算量**: O(n)

```python
def solve_optimized(set_size: int = 5, prime_limit: int = 10000) -> int:
    # 素数を生成
    is_prime_array = sieve_of_eratosthenes(prime_limit)
    primes = [i for i in range(2, prime_limit + 1) if is_prime_array[i]]

    min_sum = float('inf')

    def build_set(current_set: list[int], remaining_primes: list[int], target_size: int) -> None:
        nonlocal min_sum

        if len(current_set) == target_size:
            current_sum = sum(current_set)
            min_sum = min(min_sum, current_sum)
            return

        # 枝刈り: 現在の合計がすでに最小値を超えている場合
        if sum(current_set) >= min_sum:
            return

        for i, prime in enumerate(remaining_primes):
            # 現在の集合の全ての素数とペアを形成できるかチェック
            if all(are_prime_pair(prime, p) for p in current_set):
                build_set(
                    current_set + [prime],
                    remaining_primes[i + 1:],
                    target_size
                )

    build_set([], primes, set_size)
    return int(min_sum) if min_sum != float('inf') else -1
```

### 3. 数学的解法 (solve_mathematical)

**アプローチ**: グラフ理論を用いたクリーク探索による効率的な解法

**アルゴリズム**:
1. 素数を頂点とし、素数ペア関係を辺とするグラフを構築
2. 隣接行列を事前計算して高速な隣接判定を実現
3. 最大クリーク探索アルゴリズムで目標サイズのクリークを発見
4. 枝刈りと候補絞り込みによる効率化

**時間計算量**: O(n² + n^k)
**空間計算量**: O(n²)

```python
def solve_mathematical(set_size: int = 5, prime_limit: int = 10000) -> int:
    # 素数を生成
    is_prime_array = sieve_of_eratosthenes(prime_limit)
    primes = [i for i in range(2, prime_limit + 1) if is_prime_array[i]]

    # 素数ペアの隣接行列を構築
    n = len(primes)
    adjacency = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if are_prime_pair(primes[i], primes[j]):
                adjacency[i][j] = True
                adjacency[j][i] = True

    min_sum = float('inf')

    def find_clique(current_indices: list[int], candidates: list[int], target_size: int) -> None:
        nonlocal min_sum

        if len(current_indices) == target_size:
            current_sum = sum(primes[i] for i in current_indices)
            min_sum = min(min_sum, current_sum)
            return

        # 枝刈り
        current_sum = sum(primes[i] for i in current_indices)
        if current_sum >= min_sum:
            return

        for i, candidate in enumerate(candidates):
            # 現在の全ての頂点と隣接しているかチェック
            if all(adjacency[candidate][idx] for idx in current_indices):
                # 新しい候補リストは現在の候補と隣接している頂点のみ
                new_candidates = [
                    c for c in candidates[i + 1:]
                    if adjacency[candidate][c]
                ]
                find_clique(
                    current_indices + [candidate],
                    new_candidates,
                    target_size
                )

    find_clique([], list(range(n)), set_size)
    return int(min_sum) if min_sum != float('inf') else -1
```

## 核心となるアルゴリズム

### 素数ペア判定

2つの素数が素数ペアを形成するかの判定:

```python
def are_prime_pair(p1: int, p2: int) -> bool:
    concat1 = concatenate_numbers(p1, p2)
    concat2 = concatenate_numbers(p2, p1)

    return is_prime(concat1) and is_prime(concat2)
```

### 数値連結

2つの数値の連結:

```python
def concatenate_numbers(a: int, b: int) -> int:
    return int(str(a) + str(b))
```

### 完全集合判定

指定した素数リストが完全な素数ペア集合を形成するかの判定:

```python
def can_form_complete_set(primes: list[int], set_size: int) -> bool:
    if len(primes) != set_size:
        return False

    # 全ての素数のペアが素数ペアであることを確認
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if not are_prime_pair(primes[i], primes[j]):
                return False

    return True
```

## 数学的背景

### 素数ペアの性質

1. **対称性**: P1とP2が素数ペアなら、P2とP1も素数ペア
2. **非反射性**: 通常、素数は自分自身と素数ペアを形成しない（例：33、77は合成数）
3. **推移性なし**: P1-P2、P2-P3が素数ペアでも、P1-P3が素数ペアとは限らない

### 連結操作の数学的側面

連結による数値の変化:
- concat(a, b) = a × 10^(digits(b)) + b
- 桁数の影響: より多くの桁を持つ数値ほど連結結果が大きくなる

### グラフ理論の応用

素数ペア集合の問題は最大クリーク問題として定式化できる:
- **頂点**: 素数
- **辺**: 素数ペア関係
- **クリーク**: 完全グラフ（全ての頂点が相互に隣接）

## 実装のポイント

### パフォーマンス最適化

1. **枝刈り**: 現在の合計が最小値を超えた時点で探索を打ち切り
2. **事前計算**: 隣接行列による高速な素数ペア判定
3. **候補絞り込み**: クリーク探索での候補リストの動的更新

### メモリ効率

1. **隣接行列**: O(n²)の空間を使用するが、高速なアクセスを実現
2. **段階的構築**: 大きな組み合わせ空間を避けた再帰的構築
3. **早期終了**: 解が見つかった時点での即座の終了

### 数値精度

1. **大きな連結数**: 連結により非常に大きな数が生成される可能性
2. **素数判定**: √nまでの試し割りによる効率的な判定
3. **オーバーフロー対策**: Python整数の任意精度を活用

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** set_size = 5, prime_limit = 10000
- **解答:** [隠匿]
- **検証:** ✓

## 学習ポイント

### 組み合わせ最適化

1. **枝刈り技法**: 探索空間の効率的な削減
2. **グラフアルゴリズム**: クリーク探索とその応用
3. **動的候補管理**: 制約に基づく候補の動的絞り込み

### 素数論の応用

1. **素数生成**: エラトステネスの篩の効率的実装
2. **素数判定**: 大きな数に対する効率的な判定法
3. **素数の性質**: 連結操作による素数の特殊な関係

### アルゴリズム設計

1. **段階的構築**: 解を段階的に構築する手法
2. **制約満足**: 複数の制約を同時に満たす解の探索
3. **最適化**: 複数の解法による性能比較と改善

## 実用的応用

### 暗号学

1. **鍵生成**: 特殊な性質を持つ素数の組み合わせ
2. **ハッシュ関数**: 連結操作による値の変換
3. **乱数生成**: 素数の組み合わせによる疑似乱数

### グラフ理論

1. **クリーク問題**: 最大クリーク探索の実装
2. **ネットワーク分析**: 完全連結成分の発見
3. **推薦システム**: 相互関係に基づく推薦

### 組み合わせ論

1. **制約満足問題**: 複数制約下での最適解探索
2. **集合論**: 特殊な性質を持つ集合の構築
3. **最適化**: 組み合わせ空間での効率的探索

## 関連問題

- **Problem 035**: 循環素数（素数の特殊な性質）
- **Problem 037**: 切り詰め可能素数（数字操作と素数）
- **Problem 050**: 連続する素数の和（素数の組み合わせ）

## 参考資料

- [Clique problem - Wikipedia](https://en.wikipedia.org/wiki/Clique_problem)
- [Prime number concatenation](https://en.wikipedia.org/wiki/Concatenation_of_primes)
- [Graph theory algorithms](https://en.wikipedia.org/wiki/Graph_theory)
- [Combinatorial optimization - Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_optimization)
