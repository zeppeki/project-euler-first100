# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Project Euler problem-solving repository focused on systematically solving the first 100 problems. Each problem is implemented with multiple solution approaches in Python, emphasizing learning and optimization.

## Development Commands

### Testing
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/problems/test_problem_001.py

# Run tests with coverage
pytest --cov=problems --cov=solutions

# Run only fast tests (exclude slow tests)
pytest -m "not slow"

# Run with verbose output
pytest -v
```

### Code Quality
```bash
# Format code
black .

# Sort imports
isort .

# Lint code
flake8 .
pylint problems/ solutions/

# Type checking
mypy .

# Security scanning
bandit -r problems/ solutions/

# Run all quality checks
black . && isort . && flake8 . && mypy . && pylint problems/ solutions/ && bandit -r problems/ solutions/
```

### Development Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install -e .[dev]

# Setup pre-commit hooks
pre-commit install
```

## Code Architecture

### Directory Structure
- `problems/` - Solution implementations with multiple approaches
- `solutions/` - Detailed explanations and analysis  
- `tests/` - Comprehensive test suites
- `docs/` - Additional documentation

### Problem Implementation Pattern
Each problem follows a consistent structure:

1. **Multiple Solution Approaches**:
   - `solve_naive()` - Straightforward O(n) implementation
   - `solve_optimized()` - Optimized algorithm (often O(log n) or O(1))
   - `solve_mathematical()` - Mathematical/formula-based approach

2. **Comprehensive Testing**:
   - Unit tests with parametrized test cases
   - Edge case handling
   - Performance verification
   - All solutions must agree on results

3. **Performance Analysis**:
   - Time complexity documentation
   - Runtime measurement and comparison
   - Memory usage analysis

4. **Documentation**:
   - Detailed problem explanation
   - Mathematical background
   - Algorithm analysis
   - Learning points

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
- Completed: 3/100 problems (Problems 001, 002, 003)
- Next target: Problem 004

### Development Workflow
1. Create GitHub issue for new problem
2. Create feature branch: `gh issue develop [ISSUE_NUMBER]`
3. Implement solution with multiple approaches
4. Add comprehensive tests
5. Create solution documentation
6. Update progress tracking
7. Create PR and merge
8. Close issue

### Quality Standards
- Minimum 3 solution approaches per problem
- 100% test coverage for core functions
- Comprehensive documentation
- Performance analysis included
- All code passes linting and type checking

## Testing Strategy

### Test Categories
- Unit tests for individual functions
- Integration tests for complete solutions
- Performance tests (marked with `@pytest.mark.slow`)
- Edge case validation

### Test Execution
Tests are configured with strict settings and comprehensive markers for different test types (unit, integration, slow).

## Configuration Details

### Tool Configuration
- **Black**: Line length 88, Python 3.8+ target
- **MyPy**: Strict typing enabled, handles import issues for problem modules
- **Pytest**: Comprehensive markers, strict configuration
- **Coverage**: Excludes test files, includes problems and solutions
- **Bandit**: Security scanning with specific exclusions for test files

### Import Handling
The project uses dynamic imports for problem modules in tests. MyPy configuration includes specific overrides for problem modules to handle import resolution.