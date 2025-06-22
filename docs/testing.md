# テストガイド

このドキュメントでは、Project Euler First 100プロジェクトのテスト戦略と実装方法を説明します。

## 概要

このプロジェクトでは、以下のテスト戦略を採用しています：

- **単体テスト**: 各関数の動作を個別にテスト
- **統合テスト**: 複数の関数の組み合わせテスト
- **パフォーマンステスト**: 実行時間とメモリ使用量のテスト
- **回帰テスト**: 既存機能が壊れていないことを確認

## テストの種類

### 1. 単体テスト

各関数の動作を個別にテストします。

```python
def test_solve_naive():
    """素直な解法のテスト"""
    # 基本的なテストケース
    assert solve_naive(10) == 23
    
    # エッジケース
    assert solve_naive(1) == 0
    assert solve_naive(3) == 3
    assert solve_naive(5) == 5
    
    # 境界値テスト
    assert solve_naive(15) == 45
```

### 2. 統合テスト

複数の関数の組み合わせをテストします。

```python
def test_all_solutions_agree():
    """すべての解法が同じ結果を返すことを確認"""
    test_cases = [10, 100, 1000]
    
    for input_val in test_cases:
        naive_result = solve_naive(input_val)
        optimized_result = solve_optimized(input_val)
        math_result = solve_mathematical(input_val)
        
        assert naive_result == optimized_result == math_result
```

### 3. パフォーマンステスト

実行時間とメモリ使用量をテストします。

```python
import time
import pytest

@pytest.mark.slow
def test_performance():
    """パフォーマンステスト"""
    start_time = time.time()
    result = solve_optimized(1000000)
    execution_time = time.time() - start_time
    
    # 実行時間が1秒以内であることを確認
    assert execution_time < 1.0
    assert result > 0
```

### 4. 回帰テスト

既存機能が壊れていないことを確認します。

```python
def test_regression():
    """回帰テスト"""
    # 既知の解答を確認
    known_answers = {
        10: 23,
        100: 2318,
        1000: 233168,
    }
    
    for input_val, expected in known_answers.items():
        result = solve_optimized(input_val)
        assert result == expected, f"Regression: {input_val} -> {result}, expected {expected}"
```

## テストの書き方

### テストクラスの構造

```python
#!/usr/bin/env python3
"""
Test for Problem 001: Multiples of 3 and 5
"""

import pytest
import time
from problems.problem_001 import solve_naive, solve_optimized, solve_mathematical

class TestProblem001:
    """Problem 001のテストクラス"""
    
    def setup_method(self):
        """各テストメソッドの前に実行"""
        self.test_cases = [
            (10, 23),
            (100, 2318),
            (1000, 233168),
        ]
    
    def test_solve_naive_basic(self):
        """素直な解法の基本的なテスト"""
        for input_val, expected in self.test_cases:
            result = solve_naive(input_val)
            assert result == expected, f"Failed for input {input_val}"
    
    def test_solve_naive_edge_cases(self):
        """素直な解法のエッジケーステスト"""
        edge_cases = [
            (1, 0),
            (3, 3),
            (5, 5),
            (15, 45),
        ]
        
        for input_val, expected in edge_cases:
            result = solve_naive(input_val)
            assert result == expected, f"Edge case failed for input {input_val}"
    
    def test_solve_optimized(self):
        """最適化解法のテスト"""
        for input_val, expected in self.test_cases:
            result = solve_optimized(input_val)
            assert result == expected, f"Failed for input {input_val}"
    
    def test_solve_mathematical(self):
        """数学的解法のテスト"""
        for input_val, expected in self.test_cases:
            result = solve_mathematical(input_val)
            assert result == expected, f"Failed for input {input_val}"
    
    def test_all_solutions_agree(self):
        """すべての解法が同じ結果を返すことを確認"""
        test_values = [10, 100, 1000, 10000]
        
        for input_val in test_values:
            naive_result = solve_naive(input_val)
            optimized_result = solve_optimized(input_val)
            math_result = solve_mathematical(input_val)
            
            assert naive_result == optimized_result == math_result, \
                f"Solutions disagree for input {input_val}"
    
    def test_invalid_input(self):
        """無効な入力のテスト"""
        invalid_inputs = [-1, 0, "invalid", None]
        
        for invalid_input in invalid_inputs:
            with pytest.raises((ValueError, TypeError)):
                solve_naive(invalid_input)
    
    @pytest.mark.slow
    def test_large_input(self):
        """大きな入力値のテスト（時間がかかる）"""
        large_inputs = [100000, 1000000]
        
        for input_val in large_inputs:
            start_time = time.time()
            result = solve_optimized(input_val)
            execution_time = time.time() - start_time
            
            assert result > 0
            assert isinstance(result, int)
            assert execution_time < 5.0  # 5秒以内
    
    def test_performance_comparison(self):
        """パフォーマンス比較テスト"""
        input_val = 10000
        
        # 各解法の実行時間を測定
        start_time = time.time()
        naive_result = solve_naive(input_val)
        naive_time = time.time() - start_time
        
        start_time = time.time()
        optimized_result = solve_optimized(input_val)
        optimized_time = time.time() - start_time
        
        start_time = time.time()
        math_result = solve_mathematical(input_val)
        math_time = time.time() - start_time
        
        # 結果が一致することを確認
        assert naive_result == optimized_result == math_result
        
        # 最適化解法が最も高速であることを確認
        assert optimized_time <= naive_time
        assert math_time <= naive_time
```

### フィクスチャの使用

```python
import pytest

@pytest.fixture
def sample_numbers():
    """テスト用のサンプル数値"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.fixture
def prime_numbers():
    """テスト用の素数リスト"""
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

@pytest.fixture
def large_numbers():
    """テスト用の大きな数値"""
    return [1000, 10000, 100000]

class TestMathUtils:
    """数学ユーティリティのテスト"""
    
    def test_sum_numbers(self, sample_numbers):
        """数値の合計テスト"""
        result = sum(sample_numbers)
        assert result == 55
    
    def test_is_prime(self, prime_numbers):
        """素数判定テスト"""
        for num in prime_numbers:
            assert is_prime(num), f"{num} should be prime"
        
        non_primes = [1, 4, 6, 8, 9, 10]
        for num in non_primes:
            assert not is_prime(num), f"{num} should not be prime"
    
    def test_large_input_performance(self, large_numbers):
        """大きな入力値のパフォーマンステスト"""
        for num in large_numbers:
            start_time = time.time()
            result = solve_optimized(num)
            execution_time = time.time() - start_time
            
            assert result > 0
            assert execution_time < 1.0
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
def test_solve_optimized_parametrized(input_val, expected):
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
def test_is_prime_parametrized(n, expected):
    """パラメータ化された素数判定テスト"""
    assert is_prime(n) == expected

@pytest.mark.parametrize("input_val", [
    -1, 0, "invalid", None, 3.14
])
def test_invalid_input_parametrized(input_val):
    """パラメータ化された無効入力テスト"""
    with pytest.raises((ValueError, TypeError)):
        solve_naive(input_val)
```

### マーカーの使用

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    """時間がかかるテスト"""
    result = solve_optimized(1000000)
    assert result > 0

@pytest.mark.fast
def test_fast_operation():
    """高速なテスト"""
    result = solve_naive(10)
    assert result == 23

@pytest.mark.integration
def test_integration():
    """統合テスト"""
    # 複数の関数の組み合わせテスト
    pass

@pytest.mark.unit
def test_unit():
    """単体テスト"""
    # 単一の関数のテスト
    pass
```

## テストの実行

### 基本的な実行

```bash
# 全テストの実行
uv run pytest

# 特定のテストファイルを実行
uv run pytest tests/problems/test_problem_001.py

# 特定のテストクラスを実行
uv run pytest tests/problems/test_problem_001.py::TestProblem001

# 特定のテストメソッドを実行
uv run pytest tests/problems/test_problem_001.py::TestProblem001::test_solve_naive

# 詳細出力で実行
uv run pytest -v

# より詳細な出力で実行
uv run pytest -vv

# 出力を表示して実行
uv run pytest -s
```

### マーカーを使用した実行

```bash
# 高速なテストのみ実行
uv run pytest -m "fast"

# 時間がかかるテストをスキップ
uv run pytest -m "not slow"

# 統合テストのみ実行
uv run pytest -m "integration"

# 単体テストのみ実行
uv run pytest -m "unit"
```

### 並列実行

```bash
# 自動的に並列実行
uv run pytest -n auto

# 4つのプロセスで並列実行
uv run pytest -n 4

# 並列実行を無効化
uv run pytest -n 0
```

### カバレッジ付きで実行

```bash
# カバレッジレポートを生成
uv run pytest --cov=problems --cov=solutions

# HTMLレポートを生成
uv run pytest --cov=problems --cov=solutions --cov-report=html

# XMLレポートを生成
uv run pytest --cov=problems --cov=solutions --cov-report=xml

# ターミナルレポートを生成
uv run pytest --cov=problems --cov=solutions --cov-report=term-missing
```

### デバッグ実行

```bash
# デバッガーを起動
uv run pytest --pdb

# 最初の失敗で停止
uv run pytest -x

# 最大失敗数を指定
uv run pytest --maxfail=3

# 失敗したテストのみ再実行
uv run pytest --lf
```

## テストカバレッジ

### カバレッジの設定

```toml
# pyproject.toml
[tool.pytest.ini_options]
addopts = [
    "--cov=problems",
    "--cov=solutions",
    "--cov-report=term-missing",
    "--cov-report=html",
    "--cov-fail-under=90",
]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
```

### カバレッジレポートの確認

```bash
# HTMLレポートを開く
open htmlcov/index.html

# カバレッジの詳細確認
uv run pytest --cov=problems --cov-report=term-missing
```

### カバレッジの改善

```python
# カバレッジを改善するためのテスト追加例

def test_edge_case_zero():
    """ゼロのエッジケース"""
    result = solve_naive(0)
    assert result == 0

def test_edge_case_negative():
    """負の数のエッジケース"""
    with pytest.raises(ValueError):
        solve_naive(-1)

def test_edge_case_large():
    """大きな数のエッジケース"""
    result = solve_optimized(1000000)
    assert result > 0
```

## テストのベストプラクティス

### 1. テストの命名

```python
# 良い例
def test_solve_naive_with_valid_input():
    """有効な入力での素直な解法テスト"""
    pass

def test_solve_naive_with_invalid_input():
    """無効な入力での素直な解法テスト"""
    pass

def test_solve_naive_edge_case_zero():
    """ゼロのエッジケースでの素直な解法テスト"""
    pass

# 悪い例
def test1():
    """テスト1"""
    pass

def test_function():
    """関数のテスト"""
    pass
```

### 2. テストの構造

```python
def test_function():
    """テストの構造例"""
    # 準備 (Arrange)
    input_val = 10
    expected = 23
    
    # 実行 (Act)
    result = solve_naive(input_val)
    
    # 検証 (Assert)
    assert result == expected
```

### 3. アサーション

```python
# 基本的なアサーション
assert result == expected
assert result > 0
assert isinstance(result, int)
assert len(result) == 3

# 複数のアサーション
def test_multiple_assertions():
    result = solve_naive(10)
    
    assert result == 23
    assert result > 0
    assert isinstance(result, int)
    assert result % 1 == 0  # 整数であることを確認

# カスタムアサーション
def test_custom_assertion():
    result = solve_naive(10)
    
    assert result == 23, f"Expected 23, but got {result}"
    assert result > 0, f"Result should be positive, but got {result}"
```

### 4. エラーハンドリングのテスト

```python
def test_error_handling():
    """エラーハンドリングのテスト"""
    # ValueErrorのテスト
    with pytest.raises(ValueError, match="must be positive"):
        solve_naive(-1)
    
    # TypeErrorのテスト
    with pytest.raises(TypeError):
        solve_naive("invalid")
    
    # 複数の例外のテスト
    with pytest.raises((ValueError, TypeError)):
        solve_naive(None)
```

### 5. モックの使用

```python
from unittest.mock import patch, MagicMock

def test_with_mock():
    """モックを使用したテスト"""
    with patch('problems.problem_001.math.sqrt') as mock_sqrt:
        mock_sqrt.return_value = 10.0
        
        result = solve_optimized(100)
        
        mock_sqrt.assert_called_once_with(100)
        assert result == expected_value
```

## 継続的インテグレーション

### GitHub Actions

```yaml
# .github/workflows/test.yml
name: Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.9, 3.10, 3.11]
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install uv
      run: |
        curl -LsSf https://astral.sh/uv/install.sh | sh
        echo "$HOME/.cargo/bin" >> $GITHUB_PATH
    
    - name: Install dependencies
      run: uv sync
    
    - name: Run tests
      run: uv run pytest
    
    - name: Run tests with coverage
      run: uv run pytest --cov=problems --cov=solutions --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

### ローカルでのCI実行

```bash
# ローカルでCIと同じ環境を再現
uv run pytest --cov=problems --cov=solutions --cov-report=xml

# カバレッジの閾値チェック
uv run pytest --cov=problems --cov=solutions --cov-fail-under=90
```

## トラブルシューティング

### よくある問題

#### 1. テストが失敗する

```bash
# 詳細なエラー情報を確認
uv run pytest -v -s

# デバッガーを起動
uv run pytest --pdb

# 特定のテストのみ実行
uv run pytest tests/problems/test_problem_001.py::TestProblem001::test_solve_naive -v -s
```

#### 2. カバレッジが低い

```bash
# カバレッジの詳細確認
uv run pytest --cov=problems --cov-report=term-missing

# カバレッジレポートの生成
uv run pytest --cov=problems --cov-report=html
open htmlcov/index.html
```

#### 3. テストが遅い

```bash
# 並列実行
uv run pytest -n auto

# 高速なテストのみ実行
uv run pytest -m "fast"

# 時間がかかるテストをスキップ
uv run pytest -m "not slow"
```

#### 4. モックの設定

```python
# モックの設定例
@patch('problems.problem_001.time.time')
def test_timing(mock_time):
    mock_time.side_effect = [0.0, 1.0]  # 開始時刻、終了時刻
    
    result = solve_optimized(100)
    
    assert result == expected_value
```

## 参考資料

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Best Practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [Coverage.py Documentation](https://coverage.readthedocs.io/)
- [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)
- [Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) 