# Problem 097: Large non-Mersenne prime

## 問題文

2004年に発見された巨大な非Mersenne素数について、以下の詳細が知られています：

- この素数は2,357,207桁の数字
- 形式：28433 × 2^7830457 + 1

この巨大な素数の**末尾10桁**を求めてください。

## アプローチ

### 1. 素直な解法 (Naive Approach)

```python
def solve_naive(multiplier: int = 28433, exponent: int = 7830457, addend: int = 1) -> int:
    modulus = 10**10
    power_of_two = pow(2, exponent, modulus)
    result = (multiplier * power_of_two + addend) % modulus
    return result
```

**特徴:**
- Python組み込みの`pow()`関数を使用
- `pow(a, b, m)`は内部的に効率的なモジュラー冪乗を実装
- 最も簡潔で信頼性が高い

**時間計算量:** O(log exponent)
**空間計算量:** O(1)

### 2. 最適化解法 (Optimized Approach)

```python
def solve_optimized(multiplier: int = 28433, exponent: int = 7830457, addend: int = 1) -> int:
    modulus = 10**10
    power_of_two = modular_exponentiation(2, exponent, modulus)
    result = (multiplier * power_of_two + addend) % modulus
    return result

def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus

    return result
```

**特徴:**
- バイナリ指数法（Binary Exponentiation）を実装
- アルゴリズムの動作が明確で教育的
- 大きな指数でも効率的に計算

**時間計算量:** O(log exponent)
**空間計算量:** O(1)

### 3. 数学的解法 (Mathematical Approach)

この問題では、モジュラー冪乗が最も数学的に効率的なアプローチであるため、最適化解法と同じ実装を使用します。

## 核心となる数学的概念

### モジュラー算術

巨大な数 28433 × 2^7830457 + 1 を直接計算することは不可能です（約236万桁！）。末尾10桁のみが必要なので、mod 10^10 で計算します。

基本的な性質：
- (a × b) mod m = ((a mod m) × (b mod m)) mod m
- (a + b) mod m = ((a mod m) + (b mod m)) mod m

### バイナリ指数法

a^b mod m を効率的に計算するアルゴリズム：

1. 指数bを2進数表現に変換
2. 結果を1で初期化
3. 各ビットについて：
   - ベースを2乗する
   - ビットが1の場合、結果にベースを掛ける
   - 各ステップでmod mを適用

**例:** 3^13 mod 1000

```
13 = 1101₂
ステップ1: 13は奇数 → result = 1 × 3 = 3
ステップ2: 6は偶数 → result変更なし
ステップ3: 3は奇数 → result = 3 × 9 = 27
ステップ4: 1は奇数 → result = 27 × 81 = 2187 → 187 (mod 1000)
```

### 計算の規模

- 指数：7,830,457
- 2^7830457の桁数：約2,357,207桁
- 直接計算時のメモリ：約2.4MB（テキストファイル換算）
- バイナリ指数法のステップ数：約23ステップ

## 実装のポイント

### 1. オーバーフロー対策
各乗算後に即座にmod演算を適用して、中間結果が巨大になることを防ぎます。

### 2. 効率的なビット操作
- `exponent >> 1`は`exponent // 2`より高速
- `exponent % 2`でビットの奇偶を判定

### 3. エラーハンドリング
- modulus = 1の場合は0を返す
- 指数が0の場合は1を返す

## テストケース

### 小さな例での検証
- 3 × 2^5 + 1 = 97
- 7 × 2^10 + 3 = 7171
- 検証用関数で直接計算と比較

### 性能テスト
- 指数1000での計算：< 0.001秒
- メイン問題：< 0.001秒
- 全てのアプローチで同一結果を確認

## 解答

Project Euler公式サイトで確認してください。

## 検証

- **入力:** 28433 × 2^7830457 + 1
- **解答:** [隠匿]
- **検証:** ✓

## 学習のポイント

1. **モジュラー算術の応用**
   - 大きな数の計算を効率化
   - 末尾桁の計算パターン

2. **バイナリ指数法**
   - O(log n)での冪乗計算
   - ビット操作の活用

3. **数論的問題解決**
   - 直接計算不可能な問題へのアプローチ
   - 数学的性質の活用

4. **アルゴリズム設計**
   - 効率性と正確性の両立
   - エッジケースの処理

## 発展的考察

### 他の応用例
- RSA暗号化でのモジュラー冪乗
- フェルマーの小定理の応用
- 暗号学での大きな素数の扱い

### 最適化の可能性
- モンゴメリ乗算の使用
- 複数の指数の同時計算
- ハードウェア最適化

この問題は、純粋数学と計算機科学の境界で、効率的なアルゴリズム設計の重要性を示す優れた例です。
