# Problem 086: Cuboid route

## 問題の概要

立方体の部屋の対角の角にいるクモとハエの間の最短経路（表面経由）が整数長となる立方体の数を数える問題です。

例えば、6×5×3の立方体では最短経路長は10（整数）となります。

目標は、M×M×M以下の立方体で、整数長最短経路を持つものが100万個を初めて超える最小のMを見つけることです。

## 数学的背景

### 最短経路の計算

立方体a×b×cにおいて、対角の角の間の最短経路は、立方体を展開して2次元平面での最短距離として計算できます。

3つの展開方法があります：

1. **方法1**: a×(b+c)の長方形での対角線
   - 距離 = √(a² + (b+c)²)

2. **方法2**: b×(a+c)の長方形での対角線
   - 距離 = √(b² + (a+c)²)

3. **方法3**: c×(a+b)の長方形での対角線
   - 距離 = √(c² + (a+b)²)

最短経路長は、これら3つの最小値です。

### 例：6×5×3の立方体

```
方法1: √(6² + (5+3)²) = √(36 + 64) = √100 = 10
方法2: √(5² + (6+3)²) = √(25 + 81) = √106 ≈ 10.3
方法3: √(3² + (6+5)²) = √(9 + 121) = √130 ≈ 11.4

最短経路長 = min(10, 10.3, 11.4) = 10
```

## 解法のアプローチ

### 1. 素直な解法（全探索）

```python
def solve_naive(target: int = 1000000) -> int:
    m = 1
    while True:
        count = count_integer_paths_optimized(m)
        if count > target:
            return m
        m += 1
```

**特徴：**
- 時間計算量：O(M⁴) - M回のO(M³)計算
- Mを1から順に増やして条件を満たす最小値を探索
- 確実だが計算時間が長い

### 2. 最適化解法（二分探索）

```python
def solve_optimized(target: int = 1000000) -> int:
    left, right = 1, 2000
    
    while count_integer_paths_optimized(right) <= target:
        right *= 2
    
    while left < right:
        mid = (left + right) // 2
        count = count_integer_paths_optimized(mid)
        
        if count > target:
            right = mid
        else:
            left = mid + 1
    
    return left
```

**特徴：**
- 時間計算量：O(log M × M³)
- 二分探索で効率的に最小値を見つける
- 単調性を利用した最適化

### 3. 立方体数のカウント最適化

対称性を利用して計算量を削減：

```python
def count_integer_paths_optimized(max_size: int) -> int:
    count = 0
    
    for a in range(1, max_size + 1):
        for b in range(a, max_size + 1):
            for c in range(b, max_size + 1):
                if is_integer_path(a, b, c):
                    if a == b == c:
                        multiplicity = 1      # 1通り
                    elif a == b or b == c or a == c:
                        multiplicity = 3      # 3通り
                    else:
                        multiplicity = 6      # 6通り
                    
                    count += multiplicity
    
    return count
```

## 実装の詳細

### 整数経路の判定

```python
def is_integer_path(a: int, b: int, c: int) -> bool:
    path_length = shortest_path_length(a, b, c)
    return abs(path_length - round(path_length)) < 1e-9
```

### 重複度の計算

- **a = b = c**: 1通り（例：3×3×3）
- **2つが等しい**: 3通り（例：3×3×5は3×3×5, 3×5×3, 5×3×3）
- **全て異なる**: 6通り（例：3×4×5は6通りの順列）

## 解答

Project Euler公式サイトで確認してください。

## 検証

```python
# 問題例の確認
assert shortest_path_length(6, 5, 3) == 10.0
assert is_integer_path(6, 5, 3) == True

# 解法の一致確認
assert solve_naive(1000) == solve_optimized(1000)
```

## パフォーマンス分析

| 解法 | 時間計算量 | 空間計算量 | 実行時間（目安） |
|------|------------|------------|------------------|
| 素直な解法 | O(M⁴) | O(1) | 〜数秒 |
| 最適化解法 | O(log M × M³) | O(1) | 〜100ms |

## 学習ポイント

1. **立体幾何学**：3次元問題を2次元に展開する手法
2. **最適化**：対称性を利用した計算量削減
3. **二分探索**：単調性を持つ問題での効率的探索
4. **ピタゴラス数**：整数長経路の数学的背景
5. **組み合わせ論**：重複度の正確な計算

## 関連問題

- Problem 085: Counting rectangles（2次元版の組み合わせ問題）
- Problem 087: Prime power triples（素数の累乗組み合わせ）
- Problem 088: Product-sum numbers（積和数）
- Problem 144: Investigating multiple reflections（光線の反射経路）