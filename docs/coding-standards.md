# コーディング規約

このドキュメントでは、Project Euler First 100プロジェクトのコーディング規約を定義します。

## 概要

このプロジェクトでは、以下の規約に従ってコードを記述します：

- **PEP 8**: Python公式のスタイルガイド
- **PEP 257**: ドキュメント文字列の規約
- **PEP 484**: 型ヒントの規約
- **PEP 585**: 標準ライブラリの型ヒント（Python 3.9+）
- **PEP 695**: 型パラメータの構文（Python 3.12+）
- **PEP 695**: 型エイリアスの構文（Python 3.12+）

## 基本原則

### 1. 可読性
- コードは書くよりも読まれることが多い
- 明確で理解しやすいコードを書く
- 適切なコメントとドキュメントを追加

### 2. 一貫性
- プロジェクト全体で一貫したスタイルを維持
- 既存のコードスタイルに合わせる
- チーム全体で統一された規約を守る

### 3. 保守性
- 将来の変更を考慮した設計
- 適切な抽象化とモジュール化
- テスト可能なコードを書く

## Pythonコーディング規約（PEP 8準拠）

### インデント
```python
# 正しい例
def solve_problem(n: int) -> int:
    """問題を解決する関数"""
    if n <= 0:
        return 0

    result = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result

# 間違った例
def solve_problem(n: int) -> int:
  """問題を解決する関数"""
  if n <= 0:
      return 0  # インデントが混在
```

### 行の長さ
```python
# 88文字以内に収める（ruffのデフォルト）
def calculate_sum_of_squares_and_square_of_sum(
    numbers: list[int]
) -> tuple[int, int]:
    """二乗の和と和の二乗を計算"""
    sum_of_squares = sum(x * x for x in numbers)
    square_of_sum = sum(numbers) ** 2
    return sum_of_squares, square_of_sum
```

### インポート
```python
# 標準ライブラリ
import math
import time
from typing import Optional, Union, Callable, TypeVar

# サードパーティライブラリ
import numpy as np
import pandas as pd

# ローカルモジュール
from problems.problem_001 import solve_naive
from utils.math_utils import is_prime
```

### 変数名と関数名
```python
# 変数名: 小文字とアンダースコア
max_number = 1000
prime_factors = []
sum_result = 0

# 関数名: 小文字とアンダースコア
def find_prime_factors(n: int) -> list[int]:
    """素因数を求める"""
    pass

def calculate_fibonacci_sum(limit: int) -> int:
    """フィボナッチ数列の和を計算"""
    pass

# クラス名: パスカルケース
class PrimeFactorizer:
    """素因数分解を行うクラス"""
    pass

# 定数: 大文字とアンダースコア
MAX_ITERATIONS = 10000
DEFAULT_TIMEOUT = 30
```

### 文字列
```python
# ダブルクォートを使用（ruffのデフォルト）
message = "Hello, World!"
docstring = """
複数行のドキュメント文字列
"""

# f-stringを使用
name = "Alice"
age = 30
print(f"{name} is {age} years old")

# 文字列の連結
long_string = (
    "This is a very long string that "
    "needs to be split across multiple lines"
)
```

## 関数・クラスの命名規則

### 関数名
```python
# 動詞 + 名詞の形式
def solve_problem(n: int) -> int:
    """問題を解決する"""
    pass

def find_largest_prime_factor(n: int) -> int:
    """最大の素因数を見つける"""
    pass

def calculate_sum_of_multiples(limit: int, divisors: list[int]) -> int:
    """倍数の和を計算する"""
    pass

# ブール値を返す関数は is_ または has_ で始める
def is_prime(n: int) -> bool:
    """素数かどうかを判定する"""
    pass

def has_even_digits(n: int) -> bool:
    """偶数桁を含むかどうかを判定する"""
    pass

# テスト関数は test_ で始める
def test_solve_problem():
    """solve_problem関数のテスト"""
    pass
```

### クラス名
```python
# パスカルケース（PascalCase）
class PrimeFactorizer:
    """素因数分解を行うクラス"""
    pass

class FibonacciCalculator:
    """フィボナッチ数列を計算するクラス"""
    pass

class PalindromeChecker:
    """回文をチェックするクラス"""
    pass

# 例外クラスは Error で終わる
class InvalidInputError(Exception):
    """無効な入力に対する例外"""
    pass

class TimeoutError(Exception):
    """タイムアウト例外"""
    pass
```

### 変数名
```python
# ローカル変数: 小文字とアンダースコア
current_number = 1
prime_factors = []
sum_result = 0

# ループ変数: 短い名前（i, j, k等）
for i in range(10):
    for j in range(i):
        pass

# 定数: 大文字とアンダースコア
MAX_ITERATIONS = 10000
DEFAULT_TIMEOUT = 30
PI = 3.14159265359

# プライベート変数: アンダースコアで始める
class Calculator:
    def __init__(self):
        self._cache = {}
        self._max_cache_size = 1000
```

## ドキュメント文字列の書き方

### 関数のドキュメント文字列
```python
def solve_naive(n: int) -> int:
    """
    素直な解法で問題を解決する

    時間計算量: O(n)
    空間計算量: O(1)

    Args:
        n: 入力値（正の整数）

    Returns:
        解答値

    Raises:
        ValueError: nが正の整数でない場合

    Example:
        >>> solve_naive(10)
        23
        >>> solve_naive(1000)
        233168
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    result = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result
```

### クラスのドキュメント文字列
```python
class PrimeFactorizer:
    """
    素因数分解を行うクラス

    このクラスは、与えられた数の素因数分解を効率的に行います。
    キャッシュ機能により、同じ数の素因数分解を高速化します。

    Attributes:
        _cache: 素因数分解結果のキャッシュ
        _max_cache_size: キャッシュの最大サイズ

    Example:
        >>> factorizer = PrimeFactorizer()
        >>> factorizer.factorize(12)
        [2, 2, 3]
        >>> factorizer.factorize(100)
        [2, 2, 5, 5]
    """

    def __init__(self, max_cache_size: int = 1000):
        """
        初期化

        Args:
            max_cache_size: キャッシュの最大サイズ
        """
        self._cache = {}
        self._max_cache_size = max_cache_size
```

### モジュールのドキュメント文字列
```python
#!/usr/bin/env python3
"""
Problem 001: Multiples of 3 and 5

このモジュールは、Project Euler Problem 001の解答を提供します。

問題:
1から999までの自然数のうち、3または5の倍数の和を求めよ。

解答: 233168

実装:
- solve_naive: 素直な解法（O(n)）
- solve_optimized: 最適化解法（O(1)）
- solve_mathematical: 数学的解法（O(1)）

Author: Your Name
Date: 2024-12-19
"""
```

## 型ヒントの使用方法（Python 3.11+）

### 基本的な型ヒント（新しい形式）
```python
# 基本的な型
def add_numbers(a: int, b: int) -> int:
    return a + b

def get_name() -> str:
    return "Alice"

def is_valid(n: int) -> bool:
    return n > 0

# リスト（新しい形式）
def sum_list(numbers: list[int]) -> int:
    return sum(numbers)

# タプル（新しい形式）
def get_coordinates() -> tuple[int, int]:
    return (10, 20)

# 辞書（新しい形式）
def count_occurrences(items: list[str]) -> dict[str, int]:
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    return result

# セット（新しい形式）
def get_unique_numbers(numbers: list[int]) -> set[int]:
    return set(numbers)
```

### 複雑な型ヒント（新しい形式）
```python
from typing import Optional, Union, Callable, TypeVar

# Optional型
def find_prime_factor(n: int) -> Optional[int]:
    """素因数を見つける（見つからない場合はNone）"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return None

# Union型
def process_number(n: Union[int, float]) -> str:
    """数値を処理する"""
    return str(n)

# Callable型
def apply_function(func: Callable[[int], int], n: int) -> int:
    """関数を適用する"""
    return func(n)

# ジェネリック型
T = TypeVar('T')

class Stack[T]:
    """ジェネリックなスタッククラス"""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()
```

### 型エイリアス（Python 3.12+）
```python
# 型エイリアスの定義（新しい形式）
type Number = Union[int, float]
type NumberList = list[Number]
type Coordinate = tuple[int, int]
type PrimeFactors = dict[int, int]

# 使用例
def process_numbers(numbers: NumberList) -> Number:
    return sum(numbers)

def get_position() -> Coordinate:
    return (10, 20)

def factorize(n: int) -> PrimeFactors:
    factors = {}
    # 実装
    return factors
```

### 型パラメータ（Python 3.12+）
```python
# 型パラメータを使用したジェネリッククラス
class Container[T]:
    """型パラメータを使用したコンテナクラス"""

    def __init__(self, value: T) -> None:
        self._value = value

    def get_value(self) -> T:
        return self._value

    def set_value(self, value: T) -> None:
        self._value = value

# 使用例
int_container = Container[int](42)
str_container = Container[str]("hello")
```

## テストコードの書き方

### テストクラスの構造
```python
#!/usr/bin/env python3
"""
Test for Problem 001: Multiples of 3 and 5
"""

import pytest
from problems.problem_001 import solve_naive, solve_optimized, solve_mathematical

class TestProblem001:
    """Problem 001のテストクラス"""

    def test_solve_naive_basic(self):
        """素直な解法の基本的なテスト"""
        # 準備
        expected = 23

        # 実行
        result = solve_naive(10)

        # 検証
        assert result == expected

    def test_solve_naive_edge_cases(self):
        """素直な解法のエッジケーステスト"""
        # 境界値テスト
        assert solve_naive(1) == 0
        assert solve_naive(3) == 3
        assert solve_naive(5) == 5
        assert solve_naive(15) == 45

    def test_solve_optimized(self):
        """最適化解法のテスト"""
        test_cases = [
            (10, 23),
            (100, 2318),
            (1000, 233168),
        ]

        for input_val, expected in test_cases:
            result = solve_optimized(input_val)
            assert result == expected, f"Failed for input {input_val}"

    def test_solve_mathematical(self):
        """数学的解法のテスト"""
        test_cases = [
            (10, 23),
            (100, 2318),
            (1000, 233168),
        ]

        for input_val, expected in test_cases:
            result = solve_mathematical(input_val)
            assert result == expected, f"Failed for input {input_val}"

    def test_all_solutions_agree(self):
        """すべての解法が同じ結果を返すことを確認"""
        test_cases = [10, 100, 1000]

        for input_val in test_cases:
            naive_result = solve_naive(input_val)
            optimized_result = solve_optimized(input_val)
            math_result = solve_mathematical(input_val)

            assert naive_result == optimized_result == math_result, \
                f"Solutions disagree for input {input_val}"

    def test_invalid_input(self):
        """無効な入力のテスト"""
        with pytest.raises(ValueError):
            solve_naive(-1)

        with pytest.raises(ValueError):
            solve_naive(0)

    @pytest.mark.slow
    def test_large_input(self):
        """大きな入力値のテスト（時間がかかる）"""
        result = solve_optimized(1000000)
        assert result > 0
        assert isinstance(result, int)
```

### フィクスチャの使用
```python
import pytest

@pytest.fixture
def sample_numbers() -> list[int]:
    """テスト用のサンプル数値"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.fixture
def prime_numbers() -> list[int]:
    """テスト用の素数リスト"""
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

class TestMathUtils:
    """数学ユーティリティのテスト"""

    def test_sum_numbers(self, sample_numbers: list[int]) -> None:
        """数値の合計テスト"""
        result = sum(sample_numbers)
        assert result == 55

    def test_is_prime(self, prime_numbers: list[int]) -> None:
        """素数判定テスト"""
        for num in prime_numbers:
            assert is_prime(num), f"{num} should be prime"

        non_primes = [1, 4, 6, 8, 9, 10]
        for num in non_primes:
            assert not is_prime(num), f"{num} should not be prime"
```

### パラメータ化テスト
```python
import pytest

@pytest.mark.parametrize("input_val,expected", [
    (10, 23),
    (100, 2318),
    (1000, 233168),
    (10000, 23331668),
])
def test_solve_optimized_parametrized(input_val: int, expected: int) -> None:
    """パラメータ化された最適化解法のテスト"""
    result = solve_optimized(input_val)
    assert result == expected

@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
])
def test_is_prime_parametrized(n: int, expected: bool) -> None:
    """パラメータ化された素数判定テスト"""
    assert is_prime(n) == expected
```

## エラーハンドリング

### 例外の定義
```python
class ProjectEulerError(Exception):
    """Project Euler関連の基本例外クラス"""
    pass

class InvalidInputError(ProjectEulerError):
    """無効な入力に対する例外"""
    pass

class TimeoutError(ProjectEulerError):
    """タイムアウト例外"""
    pass

class SolutionNotFoundError(ProjectEulerError):
    """解答が見つからない例外"""
    pass
```

### 例外の使用
```python
def solve_problem(n: int) -> int:
    """
    問題を解決する

    Args:
        n: 入力値

    Returns:
        解答値

    Raises:
        InvalidInputError: nが無効な場合
        TimeoutError: 計算がタイムアウトした場合
    """
    if n <= 0:
        raise InvalidInputError(f"n must be positive, got {n}")

    if n > 1000000:
        raise InvalidInputError(f"n too large: {n}")

    try:
        # 計算処理
        result = perform_calculation(n)
        return result
    except Exception as e:
        raise ProjectEulerError(f"Failed to solve problem: {e}") from e
```

## パフォーマンス最適化

### アルゴリズムの選択
```python
# 悪い例: O(n²)のアルゴリズム
def find_duplicates_bad(numbers: list[int]) -> list[int]:
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
    return duplicates

# 良い例: O(n)のアルゴリズム
def find_duplicates_good(numbers: list[int]) -> list[int]:
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
```

### メモリ使用量の最適化
```python
# 悪い例: 大きなリストを一度に作成
def generate_numbers_bad(n: int) -> list[int]:
    return list(range(n))

# 良い例: ジェネレータを使用
def generate_numbers_good(n: int):
    for i in range(n):
        yield i

# 使用例
def process_large_dataset(n: int) -> int:
    total = 0
    for num in generate_numbers_good(n):
        if num % 2 == 0:
            total += num
    return total
```

## セキュリティ

### 入力検証
```python
def validate_input(n: int) -> None:
    """入力を検証する"""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        raise ValueError("n must be positive")

    if n > 1000000:
        raise ValueError("n too large")

def safe_divide(a: int, b: int) -> float:
    """安全な除算"""
    if b == 0:
        raise ValueError("Division by zero")

    return a / b
```

## コードレビューのチェックリスト

### 機能面
- [ ] 正しい結果を返すか
- [ ] エッジケースを適切に処理しているか
- [ ] エラーハンドリングは適切か
- [ ] パフォーマンスは適切か

### コード品質
- [ ] PEP 8に準拠しているか
- [ ] 型ヒントは適切か（新しい形式を使用）
- [ ] ドキュメント文字列は十分か
- [ ] 変数名・関数名は分かりやすいか

### テスト
- [ ] テストケースは十分か
- [ ] エッジケースのテストがあるか
- [ ] テストは理解しやすいか
- [ ] テストカバレッジは適切か

### 保守性
- [ ] コードは読みやすいか
- [ ] 適切に抽象化されているか
- [ ] 将来の変更を考慮しているか
- [ ] 依存関係は最小限か

## 自動化ツール

### 使用するツール
- **ruff**: コードフォーマットとリンティング
- **mypy**: 型チェック
- **pytest**: テスト実行
- **pre-commit**: Gitフックによる自動チェック

### 設定例
```toml
# pyproject.toml
[tool.ruff]
target-version = "py311"
line-length = 88
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
disallow_untyped_defs = true
```

## 参考資料

- [PEP 8 -- Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 -- Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 484 -- Type Hints](https://peps.python.org/pep-0484/)
- [PEP 585 -- Type Hinting Generics In Standard Collections](https://peps.python.org/pep-0585/)
- [PEP 695 -- Type Parameter Syntax](https://peps.python.org/pep-0695/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
