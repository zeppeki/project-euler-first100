# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Project Euler problem-solving repository focused on systematically solving the first 100 problems. Each problem is implemented with multiple solution approaches in Python, emphasizing learning and optimization.

## Development Commands

### Testing
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/problems/test_problem_001.py

# Run only fast tests (exclude slow tests)
uv run pytest -m "not slow"

# Run with verbose output
uv run pytest -v
```

### Code Quality
```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check --fix

# Type checking
uv run mypy .

# Security scanning
uv run bandit -r problems/

# Run all quality checks
uv run ruff format && uv run ruff check --fix && uv run mypy . && uv run bandit -r problems/
```

### Development Setup
```bash
# Install dependencies (uv automatically manages virtual environment)
uv sync

# Setup pre-commit hooks
uv run pre-commit install
```

### Documentation
```bash
# Install MkDocs dependencies
uv pip install mkdocs-material mkdocs-git-revision-date-localized-plugin mkdocs-minify-plugin

# Start development server
mkdocs serve --dev-addr=127.0.0.1:8000

# Build static HTML files
mkdocs build

# Build with clean output and strict validation
mkdocs build --clean --strict
```

## Code Architecture

### Directory Structure
- `problems/` - Solution implementations with multiple approaches
- `docs/solutions/` - Detailed explanations and analysis
- `tests/` - Comprehensive test suites
- `docs/` - MkDocs documentation and GitHub Pages content

### Problem Implementation Pattern
Each problem follows a consistent structure:

1. **Multiple Solution Approaches**:
   - `solve_naive()` - Straightforward O(n) implementation
   - `solve_optimized()` - Optimized algorithm (often O(log n) or O(1))
   - `solve_mathematical()` - Mathematical/formula-based approach

2. **Comprehensive Testing**:
   - Unit tests with parametrized test cases
   - Edge case handling
   - Functional verification (optimized for CI speed)
   - All solutions must agree on results

3. **Performance Analysis**:
   - Time complexity documentation
   - Algorithm correctness verification
   - Memory usage analysis
   - CI-optimized test execution

4. **Documentation**:
   - Detailed problem explanation
   - Mathematical background
   - Algorithm analysis
   - Learning points
   - **IMPORTANT**: No direct answer values in GitHub Pages documentation

### Code Style Guidelines
- Follow PEP 8 standards
- Use type hints for function signatures
- Include docstrings with complexity analysis
- Implement comprehensive error handling
- Use descriptive variable names in both English and Japanese comments

### Solution Template
New problems should follow this template structure:

```python
def solve_naive(limit: int) -> int:
    """
    素直な解法: [Description in Japanese]
    時間計算量: O(n)
    空間計算量: O(1)
    """

def solve_optimized(limit: int) -> int:
    """
    最適化解法: [Description in Japanese]
    時間計算量: O(log n)
    空間計算量: O(1)
    """

def solve_mathematical(limit: int) -> int:
    """
    数学的解法: [Description in Japanese]
    時間計算量: O(1)
    空間計算量: O(1)
    """

def test_solutions() -> None:
    """テストケースで解答を検証"""

def main() -> None:
    """メイン関数 - includes performance benchmarking"""
```

## Project Status and Workflow

### Current Progress
- Completed: 7/100 problems (Problems 001, 002, 003, 004, 005, 006, 007)
- Next target: Problem 008

### Development Workflow
1. Create GitHub issue for new problem
2. Create feature branch: `gh issue develop [ISSUE_NUMBER]`
3. Implement solution with multiple approaches
4. Add comprehensive tests
5. Create solution documentation
6. Update progress tracking
7. Create PR
8. **IMPORTANT: Wait for CI completion and verify all checks pass before merging**
9. Check CI status: `gh pr view [PR_NUMBER] --json statusCheckRollup`
10. Merge PR only after confirming all CI checks are SUCCESS
11. Close issue

### Quality Standards
- Minimum 3 solution approaches per problem
- 100% test coverage for core functions
- Comprehensive documentation
- Performance analysis included
- All code passes linting and type checking
- **CI verification required**: All GitHub Actions checks must pass before merging

## Testing Strategy

### Test Categories
- Unit tests for individual functions
- Integration tests for complete solutions
- Performance tests (marked with `@pytest.mark.slow`)
- Edge case validation

### Test Execution Performance
Tests are optimized for fast CI execution:
- **Fast tests**: 191 tests run in ~0.1-0.4 seconds
- **Slow tests**: 3 tests run in ~0.03 seconds
- **Total**: 194 tests complete in under 1 second
- **CI optimization**: Fast and slow tests run in separate steps for better visibility

Tests are configured with strict settings and comprehensive markers for different test types (unit, integration, slow).

## Configuration Details

### Tool Configuration
- **Ruff**: Unified linting and formatting, replaces Black/isort/flake8/pylint
- **MyPy**: Strict typing enabled, handles import issues for problem modules
- **Pytest**: Comprehensive markers, strict configuration
- **Bandit**: Security scanning with specific exclusions for test files
- **UV**: Fast Python package manager and project management
- **Pre-commit**: Automated code quality checks with ruff-based hooks

### Import Handling
The project uses dynamic imports for problem modules in tests. MyPy configuration includes specific overrides for problem modules to handle import resolution.

## Performance Optimization History

### Test Performance Optimization (2025-06)
- **Problem**: CI execution time was 58+ seconds due to timing-based performance tests
- **Solution**: Refactored all performance tests to use functional verification instead of `time.time()` measurements
- **Results**:
  - Execution time reduced from 58s to 0.1-0.4s (99.3% improvement)
  - Maintained 100% test coverage with 194 tests (updated with Problem 007)
  - Split CI into fast tests (191) and slow tests (3) for better visibility
  - All Project Euler correctness verification preserved

## CI/CD Process

### GitHub Actions Workflow
The project uses automated CI/CD with the following checks:
- **Test (Python 3.11)**: Run all tests on Python 3.11
- **Test (Python 3.12)**: Run all tests on Python 3.12
- **Quality**: Code quality checks (ruff, mypy, bandit)

### PR Merge Requirements
**CRITICAL**: PRs must only be merged after ALL CI checks pass:

```bash
# Check CI status before merging
gh pr view [PR_NUMBER] --json statusCheckRollup

# Expected output for successful CI:
# - "conclusion": "SUCCESS" for all checks
# - test (3.11): SUCCESS
# - test (3.12): SUCCESS
# - quality: SUCCESS
```

**Never merge a PR with failing or pending CI checks.**

## Documentation Guidelines

### GitHub Pages Content Policy
- **No Direct Answer Values**: Project Eulerの解答値を直接表示しない
- **Answer Sections**: 「Project Euler公式サイトで確認してください」に統一
- **Verification Results**: 具体的な数値は「[隠匿]」で置換
- **Learning Content**: アルゴリズム解説と学習内容は保持
- **Small Examples**: 小さな例題の期待値は学習のため保持可能

### Solution Documentation Template
```markdown
## 解答

Project Euler公式サイトで確認してください。

## 検証
- **入力:** [example input]
- **解答:** [隠匿]
- **検証:** ✓
```
