# Problem 062: Cubic permutations

## 問題

The cube, 41063625 (345³), can be permuted to produce two other cubes: 56623104 (384³) and 66430125 (405³). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cubes.

Find the smallest cube for which exactly five permutations of its digits are cubes.

## 解答

Project Euler公式サイトで確認してください。

## アプローチ

### 1. 素直な解法 (solve_naive)
- **アルゴリズム**: 立方数を生成して順列チェック
- **手順**:
  1. 立方数を順次生成
  2. 各立方数について全ての順列を生成
  3. 各順列が立方数かどうかをチェック
  4. 立方数の順列が正確に5個あるものを探す
- **時間計算量**: O(n × k! × log m) - 非効率
- **空間計算量**: O(k!) - 順列の保存

### 2. 最適化解法 (solve_optimized)
- **アルゴリズム**: 桁のソートによる効率的な分類
- **最適化のポイント**:
  1. **桁ソート**: 数字の桁をソートして正規化キーを作成
  2. **辞書分類**: 同じキーを持つ立方数をグループ化
  3. **早期判定**: 5個のグループが見つかったら即座に返す
  4. **効率的な立方数判定**: 立方根の整数判定で高速化
- **時間計算量**: O(n × k log k) - 大幅な改善
- **空間計算量**: O(n) - 辞書による効率的な分類

## 実装のポイント

### 桁ソートによる正規化
```python
def get_digit_signature(n):
    """数字の桁をソートして正規化キーを生成"""
    return ''.join(sorted(str(n)))

def solve_optimized():
    """効率的な立方数の順列探索"""
    signature_groups = {}
    n = 1

    while True:
        cube = n ** 3
        signature = get_digit_signature(cube)

        if signature not in signature_groups:
            signature_groups[signature] = []
        signature_groups[signature].append(cube)

        # 5個の立方数を持つグループを発見
        if len(signature_groups[signature]) == 5:
            return min(signature_groups[signature])

        n += 1
```

### 立方数の判定
```python
def is_perfect_cube(n):
    """効率的な立方数判定"""
    if n < 0:
        return False

    cube_root = round(n ** (1/3))
    return cube_root ** 3 == n
```

### 順列生成（素直な解法用）
```python
from itertools import permutations

def get_all_permutations(n):
    """数字の全順列を生成（先頭0を除く）"""
    digits = str(n)
    perms = set()

    for perm in permutations(digits):
        if perm[0] != '0':  # 先頭が0でない場合のみ
            num = int(''.join(perm))
            perms.add(num)

    return perms
```

## 数学的背景

### 立方数の性質
立方数は n³ の形で表される数で、以下の性質があります：
- **成長率**: 立方数は3次関数的に成長
- **桁数**: n桁の立方数の範囲は限定的
- **分布**: 大きな数ほど立方数の密度は低下

### 順列の数学
- **桁の順列**: k桁の数は最大k!個の順列を持つ
- **先頭0制約**: 先頭が0の順列は無効
- **重複桁**: 同じ桁が複数ある場合、順列数は減少

## 学習ポイント

1. **効率的な分類**: 桁ソートによる正規化キーの活用
2. **辞書活用**: グループ化による効率的な探索
3. **数学的性質**: 立方数の特性と成長パターン
4. **早期終了**: 条件達成時の即座の終了
5. **メモリ効率**: 必要最小限のデータ保持

## パフォーマンス比較

| 解法 | 計算量 | 実行時間 | メモリ使用量 |
|------|--------|----------|-------------|
| 素直 | O(n×k!×log m) | 長時間 | 大 |
| 最適化 | O(n×k log k) | 高速 | 小 |

## 検証

- **テストケース**: 3つの順列を持つ41063625の確認
- **期待値**: [隠匿]
- **実行時間**: 桁ソートにより大幅短縮
- **検証**: ✓

## 参考資料

- [Perfect cube on Wikipedia](https://en.wikipedia.org/wiki/Cube_(arithmetic))
- [Permutation algorithms](https://en.wikipedia.org/wiki/Permutation)
