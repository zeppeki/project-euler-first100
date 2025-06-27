# Problem 024: Lexicographic permutations

## 問題

順列とは、モノの順番付きの配置のことである。例えば, 3124は数 1, 2, 3, 4 の一つの順列である. すべての順列を数の大きさ順あるいは辞書式順に並べたものを辞書式順列と呼ぶ. 0, 1, 2 の辞書式順列は以下の通りである.

`012, 021, 102, 120, 201, 210`

0, 1, 2, 3, 4, 5, 6, 7, 8, 9 の辞書式順列の中で100万番目は何か?

## 解答: 2783915460

## 解法

この問題は、与えられた要素の辞書式順列を考え、特定の位置（100万番目）に来る順列を求めるものです。2つのアプローチで解法を実装しました。

### 1. 素直な解法 (`solve_naive`)

最も直感的な方法は、Pythonの標準ライブラリ `itertools.permutations` を使って、すべての順列を生成し、目的のn番目の要素を取り出すことです。

- **時間計算量**: `O(d! * d)` (dは桁数)
- **空間計算量**: `O(d! * d)`

この方法は、すべての順列をメモリ上に生成するため、要素数が増えると非常に多くの時間とメモリを消費します。今回の問題（10桁）では `10! = 3,628,800` 通りの順列が生成され、実行可能ですが非効率です。

```python
from itertools import permutations
import math

def solve_naive(digits: str = "0123456789", n: int = 1_000_000) -> str:
    """
    Solves the problem by generating all permutations.
    """
    num_permutations = math.factorial(len(digits))
    if not 1 <= n <= num_permutations:
        return ""

    # The nth permutation is at index n-1
    return "".join(list(permutations(digits))[n - 1])
```

### 2. 最適化解法 (`solve_optimized`)

より効率的な方法は、階乗（factorial）の性質を利用して、先頭の桁から順番に決定していく数学的なアプローチです。

- **時間計算量**: `O(d^2)` (dは桁数)
- **空間計算量**: `O(d)`

#### 考え方

0から9までの10個の数字の順列を考えます。

1.  残りの9個の数字の順列は `9!` 通りあります。`9! = 362,880` です。
2.  求めたいのは100万番目ですが、0から数え始めると `999,999` 番目になります。
3.  `999,999` を `9!` で割ると、`999,999 // 362,880 = 2` となります。これは、最初の桁が `[0, 1, 2, ...]` の中でインデックス `2` の数字、つまり `2` であることを意味します。
4.  最初の桁が `2` に決まったので、残りの数字は `[0, 1, 3, 4, 5, 6, 7, 8, 9]` となります。次に求めるべき順列の位置は、余りである `999,999 % 362,880 = 274,239` 番目です。
5.  今度は残りの8個の数字の順列 `8! = 40,320` を考えます。
6.  `274,239 // 40,320 = 6` となり、2番目の桁は残りの数字リストのインデックス `6` の数字、つまり `7` に決まります。
7.  このプロセスを最後の桁まで繰り返すことで、目的の順列を効率的に構築できます。

```python
import math

def solve_optimized(digits: str = "0123456789", n: int = 1_000_000) -> str:
    """
    Solves the problem using a mathematical approach with factorials.
    """
    num_permutations = math.factorial(len(digits))
    if not 1 <= n <= num_permutations:
        return ""

    result = []
    digit_list = list(digits)
    n -= 1  # Use 0-based index

    for i in range(len(digit_list) - 1, -1, -1):
        f = math.factorial(i)
        index = n // f
        n %= f
        result.append(digit_list.pop(index))

    return "".join(result)
```

## パフォーマンス比較

| 解法 | 実行時間（参考） |
| :--- | :--- |
| 素直な解法 | ~0.1秒 |
| 最適化解法 | ~0.00001秒 |

最適化解法は、順列をすべて生成する必要がないため、圧倒的に高速です。

## 学習ポイント

- `itertools.permutations` の便利さと、その計算量の限界を理解する。
- 階乗を用いて組み合わせの数を計算し、目的の順列を桁ごとに決定していくアルゴリズムを学ぶ。
- 大きな問題を小さな問題に分割して考える（今回の場合は、1桁ずつ決定していく）アプローチの有効性を確認する。
