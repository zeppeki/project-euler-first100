# Problem 095: Amicable chains

## 問題文

真の約数とは、ある数の約数のうち、その数自身を除いたものです。例えば、28の真の約数は1, 2, 4, 7, 14であり、これらの和は28に等しいため、28を完全数と呼びます。

興味深いことに、220の真の約数の和は284で、284の真の約数の和は220となり、2つの数の連鎖を形成します。このため、220と284は友愛数と呼ばれます。

より長い連鎖もあまり知られていません。例えば、12496から始めると、5つの数の連鎖を形成します：
12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

この連鎖は開始点に戻るため、友愛連鎖と呼ばれます。

要素が100万を超えない最長の友愛連鎖の最小メンバーを見つけてください。

## 解法

### アプローチ1: 素直な解法 (O(n * √n))

各数について個別に約数の和を計算し、連鎖を追跡します。

```python
def solve_naive(limit: int = 1000000) -> int:
    max_chain_length = 0
    result = 0
    seen = set()

    for i in range(2, limit + 1):
        if i in seen:
            continue

        chain = []
        current = i

        # Build chain
        while current not in chain and current <= limit:
            chain.append(current)
            current = sum_of_proper_divisors(current)

            if current == 0 or current == 1:
                break

        # Check if we found an amicable chain
        if current in chain:
            start_index = chain.index(current)
            if start_index == 0:  # Chain returns to start
                chain_length = len(chain)
                if chain_length > max_chain_length:
                    max_chain_length = chain_length
                    result = min(chain)

                # Mark all elements in chain as seen
                seen.update(chain)

    return result
```

### アプローチ2: 最適化解法 (O(n log n))

ふるい法的アプローチで全ての数の約数和を事前計算し、効率的に連鎖を構築します。

```python
def compute_divisor_sums(limit: int) -> list[int]:
    divisor_sums = [0] * (limit + 1)

    # Use sieve-like approach
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            divisor_sums[j] += i

    return divisor_sums

def solve_optimized(limit: int = 1000000) -> int:
    # Precompute divisor sums
    divisor_sums = compute_divisor_sums(limit)

    max_chain_length = 0
    result = 0
    seen = set()

    for i in range(2, limit + 1):
        if i in seen:
            continue

        chain_length, chain = find_chain_length(i, divisor_sums, limit)

        if chain_length > 0:
            # Found an amicable chain
            if chain_length > max_chain_length:
                max_chain_length = chain_length
                result = min(chain)

            # Mark all elements in chain as seen
            seen.update(chain)

    return result
```

### アプローチ3: 数学的解法 (O(n log n))

この問題では特別な数学的ショートカットはないため、最適化解法と同じアプローチを使用します。

```python
def solve_mathematical(limit: int = 1000000) -> int:
    return solve_optimized(limit)
```

## 重要な洞察

1. **約数和の効率的計算**: ふるい法的アプローチにより、O(n log n)で全ての数の約数和を計算できます。

2. **連鎖の種類**:
   - 完全数: 長さ1の連鎖（例: 6, 28）
   - 友愛数: 長さ2の連鎖（例: 220-284）
   - より長い連鎖: 例えば12496から始まる長さ5の連鎖

3. **連鎖検出の最適化**: 既に処理した数を記録することで、重複した計算を避けます。

4. **終了条件**: 連鎖構築時の適切な終了条件の判定が重要です：
   - 開始数に戻る → 友愛連鎖
   - より小さい数に到達 → 既に処理済み
   - 制限を超える → 無効
   - ループだが開始数に戻らない → 友愛連鎖ではない

## パフォーマンス分析

- **素直な解法**: O(n * √n) - 各数について約数和を個別計算
- **最適化解法**: O(n log n) - 約数和の事前計算により高速化
- **数学的解法**: O(n log n) - 最適化解法と同じ

ここで：
- n: 制限値（100万）
- 約数和の計算が計算量の主要部分

## 実装のポイント

1. **メモリ効率**: 100万要素の配列が必要ですが、現代のコンピュータでは問題ありません。

2. **連鎖追跡**: setを使用して効率的に既訪問要素を追跡します。

3. **エラーハンドリング**: 配列境界チェックと無効な連鎖の適切な処理が重要です。

4. **最小要素の追跡**: 最長連鎖の最小メンバーを求めるため、連鎖全体を保存する必要があります。

## 検証

小さな例での検証：
- 完全数6: 1 + 2 + 3 = 6（長さ1の連鎖）
- 友愛数220, 284: 220 → 284 → 220（長さ2の連鎖）
- 12496: 12496 → 14288 → 15472 → 14536 → 14264 → 12496（長さ5の連鎖）

## 解答

Project Euler公式サイトで確認してください。

## 学習ポイント

1. **約数計算の最適化**: ふるい法的アプローチによる効率的な計算方法

2. **グラフ理論的思考**: 連鎖をグラフの閉路として捉える視点

3. **キャッシング戦略**: 計算結果の再利用による最適化

4. **アルゴリズムの正確性**: 終了条件の適切な設定と検証

この問題は、数論とグラフ理論の要素を組み合わせた興味深い問題です。効率的な実装により、大きな制限値でも実用的な時間で解を求めることができます。
