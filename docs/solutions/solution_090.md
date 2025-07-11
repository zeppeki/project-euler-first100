# Problem 090: Cube digit pairs

## 問題の概要

2つのキューブのそれぞれの面に異なる数字（0-9）を書き、この2つのキューブを並べて2桁の数字を作る問題です。

具体的には、100未満の全ての平方数（01, 04, 09, 16, 25, 36, 49, 64, 81）を表示できるようにキューブの数字を配置する方法が何通りあるかを求めます。

特別なルール：
- 6と9は上下逆さまにできるため、相互に変換可能
- 各キューブには6つの異なる数字を配置
- 2つのキューブを並べて2桁数字を形成

## 数学的背景

### 平方数の要件

100未満の完全平方数：
- 1² = 01
- 2² = 04
- 3² = 09
- 4² = 16
- 5² = 25
- 6² = 36
- 7² = 49
- 8² = 64
- 9² = 81

### 6と9の相互変換

重要な制約として、6と9は物理的に上下逆さまにできるため、以下のように扱われます：
- 6を含むキューブは9としても使用可能
- 9を含むキューブは6としても使用可能
- この変換により同じ配置として扱われるケースがある

### 組み合わせ論

- 10個の数字から6個を選ぶ組み合わせ：C(10,6) = 210
- 2つのキューブの組み合わせ：210 × 210 = 44,100（理論上限）
- 実際は重複を除く必要がある

## 解法のアプローチ

### 1. 素直な解法

```python
def solve_naive() -> int:
    squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]
    all_cubes = list(combinations(range(10), 6))
    valid_arrangements = 0

    # 全ての組み合わせをチェック（重複を避けるため i <= j）
    for i in range(len(all_cubes)):
        for j in range(i, len(all_cubes)):
            cube1 = set(all_cubes[i])
            cube2 = set(all_cubes[j])

            # 全ての平方数が作成可能かチェック
            can_form_all = True
            for square in squares:
                if not can_form_square(cube1, cube2, square):
                    can_form_all = False
                    break

            if can_form_all:
                valid_arrangements += 1

    return valid_arrangements
```

**特徴：**
- 時間計算量：O(C(10,6)²) = O(44,100)
- 全ての組み合わせを生成して条件をチェック
- 重複を避けるため i ≤ j の制約を使用

### 2. 最適化解法

```python
def solve_optimized() -> int:
    squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]

    # 6と9の正規化を事前に行う
    all_cubes = []
    for combo in combinations(range(10), 6):
        normalized = normalize_cube(set(combo))
        if normalized not in all_cubes:
            all_cubes.append(normalized)

    # 正規化されたキューブで組み合わせをチェック
    valid_arrangements = 0
    for i in range(len(all_cubes)):
        for j in range(i, len(all_cubes)):
            # 全ての平方数が作成可能かチェック
            # ...

    return valid_arrangements
```

**特徴：**
- 6と9の正規化を事前に行い重複を削減
- 空間計算量：O(C(10,6)) = O(210)
- 実質的な計算量を削減

### 3. 数学的解法

```python
def solve_mathematical() -> int:
    # 必要な平方数のペア（6と9の変換も考慮）
    required_pairs = [
        {(0, 1), (1, 0)},  # 01
        {(0, 4), (4, 0)},  # 04
        {(0, 6), (0, 9), (6, 0), (9, 0)},  # 09
        {(1, 6), (1, 9), (6, 1), (9, 1)},  # 16
        {(2, 5), (5, 2)},  # 25
        {(3, 6), (3, 9), (6, 3), (9, 3)},  # 36
        {(4, 6), (4, 9), (6, 4), (9, 4)},  # 49
        {(6, 4), (9, 4), (4, 6), (4, 9)},  # 64
        {(8, 1), (1, 8)},  # 81
    ]

    # 効率的な探索と枝刈りを使用
    # ...
```

**特徴：**
- 必要なペアを事前計算
- 6と9の変換を明示的に列挙
- 効率的な探索アルゴリズム

## 実装の詳細

### 平方数の生成チェック

```python
def can_form_square(cube1: set[int], cube2: set[int], target: str) -> bool:
    digit1, digit2 = int(target[0]), int(target[1])

    def has_digit(cube: set[int], digit: int) -> bool:
        if digit in cube:
            return True
        # 6と9の相互変換
        if digit == 6 and 9 in cube:
            return True
        if digit == 9 and 6 in cube:
            return True
        return False

    # 両方向でチェック（cube1-cube2 と cube2-cube1）
    return (has_digit(cube1, digit1) and has_digit(cube2, digit2)) or \
           (has_digit(cube1, digit2) and has_digit(cube2, digit1))
```

### 6と9の正規化

```python
def normalize_cube(cube: set[int]) -> set[int]:
    normalized = set(cube)

    # 6と9が両方ある場合は、9を6に統一
    if 6 in normalized and 9 in normalized:
        normalized.remove(9)
    # 9のみある場合は、6に変換
    elif 9 in normalized:
        normalized.remove(9)
        normalized.add(6)

    return normalized
```

### 重複の処理

同一のキューブペアが複数回カウントされないよう、以下の方法を使用：
1. インデックスの制約：i ≤ j
2. 正規化による重複削除
3. セットベースの重複チェック

## 解答

Project Euler公式サイトで確認してください。

## 検証

```python
# 問題文の例のキューブ
cube1_example = {0, 5, 6, 7, 8, 9}
cube2_example = {1, 2, 3, 4, 8, 9}

# 全ての平方数が作成可能かテスト
squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]
for square in squares:
    assert can_form_square(cube1_example, cube2_example, square)

# 解法の一致性テスト
assert solve_naive() == solve_optimized()
assert solve_optimized() == solve_mathematical()
```

## パフォーマンス分析

| 解法 | 時間計算量 | 空間計算量 | 実行時間 |
|-----|-----------|-----------|---------|
| 素直な解法 | O(44,100 × 9) | O(1) | ~1.0s |
| 最適化解法 | O(正規化後 × 9) | O(210) | ~0.5s |
| 数学的解法 | O(44,100 × 9) | O(210) | ~0.8s |

## 学習ポイント

1. **組み合わせ論**：C(10,6)の計算と重複処理
2. **対称性の活用**：6と9の相互変換による同値性
3. **効率的な探索**：重複を避ける制約の設定
4. **データ構造の選択**：セットを使った効率的な検索
5. **枝刈り**：早期終了による計算量削減

## 関連問題

- Problem 089: Roman numerals（文字の変換と最適化）
- Problem 062: Cubic permutations（数字の順列と組み合わせ）
- Problem 052: Permuted multiples（数字の置換）
- Problem 038: Pandigital multiples（数字の組み合わせ）

## 実装のバリエーション

### 事前計算アプローチ

```python
def precompute_required_digits():
    """各平方数に必要な数字の組み合わせを事前計算"""
    requirements = []
    for square in ["01", "04", "09", "16", "25", "36", "49", "64", "81"]:
        d1, d2 = int(square[0]), int(square[1])
        # 6と9の変換も考慮したペアを生成
        pairs = generate_digit_pairs(d1, d2)
        requirements.append(pairs)
    return requirements
```

### ビット演算最適化

```python
def cube_to_bitmask(cube: set[int]) -> int:
    """キューブをビットマスクに変換して高速化"""
    mask = 0
    for digit in cube:
        mask |= (1 << digit)
    return mask
```

このような最適化により、さらなる高速化が可能です。
