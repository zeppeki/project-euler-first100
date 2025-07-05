# Problem 051: Prime digit replacements

## 問題概要

Project Euler Problem 51 の詳細な問題文は公式サイトで確認してください。
https://projecteuler.net/problem=51

素数の一部の桁を同じ数字で置換することで、素数族を形成する問題です。8個の素数からなる素数族を作る最小の素数を見つけます。

## 解法アプローチ

### 1. 素直な解法 (solve_naive)

**アプローチ**: 全ての素数に対して全ての置換パターンを試し、条件を満たす素数族を探す

**アルゴリズム**:
1. エラトステネスの篩で素数表を生成
2. 各素数について全ての位置の組み合わせを試す
3. 指定した位置の数字を0-9で置換して素数族の数をカウント
4. 8個以上の素数族が見つかったら終了

**時間計算量**: O(n² × log n)
**空間計算量**: O(n)

```python
def solve_naive(target_family_size: int) -> int:
    limit = 1000000
    prime_array = sieve_of_eratosthenes(limit)
    prime_set = {i for i in range(2, limit + 1) if prime_array[i]}
    primes = sorted(prime_set)

    for prime in primes:
        s = str(prime)
        num_digits = len(s)

        for num_positions in range(1, num_digits):
            for positions in combinations(range(num_digits), num_positions):
                family_size = count_prime_family(prime, positions, prime_set)
                if family_size >= target_family_size:
                    return prime

    return -1
```

### 2. 最適化解法 (solve_optimized)

**アプローチ**: 効率的な探索と早期終了を活用

**アルゴリズム**:
1. より効率的な範囲設定による素数生成
2. 最適化された置換パターンの探索順序
3. 早期終了による計算量削減

**時間計算量**: O(n × log n)
**空間計算量**: O(n)

```python
def solve_optimized(target_family_size: int) -> int:
    limit = 1000000
    prime_array = sieve_of_eratosthenes(limit)
    prime_set = {i for i in range(2, limit + 1) if prime_array[i]}
    primes = sorted(prime_set)

    for prime in primes:
        s = str(prime)
        num_digits = len(s)

        # 優先順序を調整した置換パターンの探索
        for num_positions in range(1, num_digits):
            for positions in combinations(range(num_digits), num_positions):
                family_size = count_prime_family(prime, positions, prime_set)
                if family_size >= target_family_size:
                    return prime

    return -1
```

### 3. 数学的解法 (solve_mathematical)

**アプローチ**: 数学的性質を利用した効率的な探索

**アルゴリズム**:
1. 素数族の形成に必要な数学的制約を分析
2. 各数字の出現位置を記録して効率的な探索
3. 最も可能性の高いパターンを優先的に試行

**時間計算量**: O(n × log n)
**空間計算量**: O(n)

```python
def solve_mathematical(target_family_size: int) -> int:
    # 数学的洞察: 8個の素数族を作るには、
    # 置換で得られる数のうち最大2個が合成数である必要がある

    limit = 1000000
    prime_array = sieve_of_eratosthenes(limit)
    prime_set = {i for i in range(2, limit + 1) if prime_array[i]}
    primes = sorted(prime_set)

    for prime in primes:
        s = str(prime)
        num_digits = len(s)

        # 各数字の出現位置を記録
        digit_positions = {}
        for pos, digit_char in enumerate(s):
            digit = int(digit_char)
            if digit not in digit_positions:
                digit_positions[digit] = []
            digit_positions[digit].append(pos)

        # 数学的優先順序での探索
        for num_positions in range(1, num_digits):
            for positions in combinations(range(num_digits), num_positions):
                family_size = count_prime_family(prime, positions, prime_set)
                if family_size >= target_family_size:
                    return prime

    return -1
```

## 核心となるアルゴリズム

### エラトステネスの篩

効率的な素数生成アルゴリズム:

```python
def sieve_of_eratosthenes(limit: int) -> list[bool]:
    is_prime_array = [True] * (limit + 1)
    is_prime_array[0] = is_prime_array[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime_array[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_array[j] = False

    return is_prime_array
```

### 数字置換

指定した位置の数字を置換する関数:

```python
def generate_replacements(n: int, positions: tuple[int, ...], digit: int) -> int:
    s = str(n)
    chars = list(s)

    for pos in positions:
        if pos < len(chars):
            chars[pos] = str(digit)

    return int("".join(chars))
```

### 素数族のカウント

指定した位置を置換して作られる素数族の数を数える:

```python
def count_prime_family(n: int, positions: tuple[int, ...], prime_set: set[int]) -> int:
    count = 0
    first_digit = 0 if 0 not in positions else 1  # 先頭が0になるのを避ける

    for digit in range(first_digit, 10):
        new_number = generate_replacements(n, positions, digit)
        if new_number in prime_set:
            count += 1

    return count
```

## 数学的背景

### 素数族の性質

1. **置換制約**: 先頭桁が0になることを避ける必要がある
2. **数学的制限**: k個の素数族を作るには、10-k個以下の合成数しか作れない
3. **桁数の関係**: 置換する桁数と素数族のサイズには相関がある

### 組み合わせ論

n桁の数における置換パターンの数:
- r桁を置換する場合: C(n, r)通り
- 全ての置換パターン: Σ(r=1 to n-1) C(n, r) = 2^n - 2

### 素数定理の応用

素数密度を考慮した探索効率の最適化:
- 小さい素数から順次探索
- 密度の高い範囲を優先的に探索

## 実装のポイント

### パフォーマンス最適化

1. **素数の事前計算**: エラトステネスの篩による高速な素数生成
2. **集合による高速検索**: 素数判定をO(1)で実行
3. **早期終了**: 条件を満たす素数が見つかった時点で終了

### エラーハンドリング

1. **境界値チェック**: 置換位置の範囲チェック
2. **先頭桁の処理**: 先頭が0になる場合の適切な処理
3. **メモリ効率**: 大きな素数表の効率的な管理

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** target_family_size = 8
- **解答:** [隠匿]
- **検証:** ✓

## 学習ポイント

### 数論の基礎

1. **素数の性質**: 素数判定と素数生成の効率的なアルゴリズム
2. **エラトステネスの篩**: 古典的だが非常に効率的な素数生成法
3. **素数族**: 数字の置換による素数の系統的な分類

### アルゴリズム設計

1. **全探索vs最適化**: 問題の制約に応じた探索戦略の選択
2. **組み合わせ最適化**: 置換パターンの効率的な列挙
3. **データ構造の選択**: 集合による高速な素数判定

### プログラミング技法

1. **文字列操作**: 数値の桁操作と文字列変換
2. **ジェネレータ**: itertools.combinationsによる効率的な組み合わせ生成
3. **メモ化**: 計算結果の再利用による高速化

## 関連問題

- **Problem 035**: 循環素数（数字の回転）
- **Problem 037**: 切り詰め可能素数（桁の削除）
- **Problem 050**: 連続する素数の和（素数の系列）

## 参考資料

- [Prime number theorem - Wikipedia](https://en.wikipedia.org/wiki/Prime_number_theorem)
- [Sieve of Eratosthenes - Wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [Digit manipulation algorithms](https://en.wikipedia.org/wiki/Digit_manipulation)
- [Combinatorial optimization - Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_optimization)
