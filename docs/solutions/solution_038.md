# Problem 038: Pandigital multiples

## 問題

ある整数に 1, 2, 3, ... , n をかけた積を連結して、1から9の各数字がちょうど1回ずつ現れる9桁のパンデジタル数を作ることを考える。

例えば、192に(1,2,3)をかけると：
- 192 × 1 = 192
- 192 × 2 = 384
- 192 × 3 = 576
- 連結結果：192384576（9桁のパンデジタル数）

整数に(1, 2, ..., n)（ここでn > 1）をかけた積を連結して作られる最大の9桁パンデジタル数を求めよ。

## 解答

Project Euler公式サイトで確認してください。

## 解法

### 1. 素直な解法 (Naive Approach)

全ての可能な基数と乗数の組み合わせを試す方法：

1. 基数を1から9999まで試行
2. 各基数について、n=2から9まで試行
3. 基数×(1,2,...,n)の積を連結
4. 連結結果が9桁でパンデジタル数かチェック
5. 最大値を記録

**時間計算量：** O(N × M) （Nは基数の範囲、Mは最大乗数）

**検証例：**
- 192 × (1,2,3) = 192384576 ✓
- 9 × (1,2,3,4,5) = 918273645 ✓

### 2. 最適化解法 (Optimized Approach)

効率的な範囲制限とブレイク条件を使用：

1. 基数ごとに動的に乗数を増やしながら連結
2. 9桁に達した時点でパンデジタル性をチェック
3. 9桁を超えた時点で次の基数へ
4. n > 1の条件も同時にチェック

**改善点：**
- 不要な計算の早期終了
- メモリ効率の向上
- 範囲の動的調整

**時間計算量：** O(N × log N)

## アルゴリズムの詳細

### パンデジタル数の判定

```python
def is_pandigital(num_str: str) -> bool:
    return len(num_str) == 9 and set(num_str) == set('123456789')
```

### 連結積の生成

```python
def concatenated_product(base: int, n: int) -> str:
    result = ""
    for i in range(1, n + 1):
        result += str(base * i)
    return result
```

## 学習ポイント

1. **パンデジタル数の性質**：1から9の各数字がちょうど1回ずつ現れる
2. **連結操作**：数値を文字列として結合する処理
3. **探索の最適化**：不要な計算を避ける条件分岐
4. **範囲の制限**：問題の制約から効率的な探索範囲を導出

## 数学的考察

- 9桁のパンデジタル数は 362880 通り（9!）存在
- n=2の場合：基数は4桁以下でなければ9桁を超える
- n=3の場合：基数は3桁以下が中心
- n≥5の場合：基数は1桁でなければ9桁を超える

これらの制約により、実際の探索範囲は大幅に限定される。
