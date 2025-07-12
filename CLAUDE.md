# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Project Euler problem-solving repository focused on systematically solving the first 100 problems. Each problem is implemented with multiple solution approaches in Python, emphasizing learning and optimization.

## Development Commands

**IMPORTANT**: This project now uses an enhanced Makefile that provides simplified commands for all development tasks. Use `make help` to see all available commands.

### Quick Start
```bash
# See all available commands
make help

# Complete initial setup
make setup

# Run all CI checks locally (fast)
make ci-check
```

### Dependencies
```bash
# Install all dependencies (recommended)
make install

# Install development dependencies only
make install-dev

# Install documentation dependencies only
make install-docs

# Update dependencies
make update
```

### Testing
```bash
# Run all tests
make test

# Run fast tests only (exclude slow tests)
make test-fast

# Run slow tests only
make test-slow

# Run tests with coverage report
make test-cov

# Run tests for specific problem
make test-problem PROBLEM=001
```

### Code Quality
```bash
# Format code with ruff
make format

# Check code with ruff (no fixes)
make lint

# Check and fix code with ruff
make lint-fix

# Run type checking with mypy
make typecheck

# Run security scan with bandit
make security

# Run all code quality checks
make quality
```

### CI/CD
```bash
# Run CI-equivalent checks locally (fast)
make ci-check

# Run complete CI/CD pipeline locally
make ci-full

# Validate project configuration files
make validate
```

### GitHub Workflow
```bash
# Create GitHub issue for new problem
make issue-create PROBLEM=025 TITLE="Problem Title"

# Create development branch for issue
make issue-develop ISSUE=123

# Create pull request for issue
make pr-create ISSUE=123 TITLE="Problem Title"

# Check pull request status
make pr-status PR=123

# Merge pull request after checks
make pr-merge PR=123

# Close issue
make issue-close ISSUE=123
```

### Performance & Analysis
```bash
# Run performance benchmarks for all problems
make benchmark

# Run benchmark for specific problem
make benchmark-problem PROBLEM=001

# Run simple benchmark (learning-optimized)
make benchmark-simple

# Run simple benchmark for specific problem
make benchmark-simple-problem PROBLEM=001

# Show detailed project statistics
make stats

# Show progress toward 100 problems goal
make progress
```

### Documentation
```bash
# Start documentation development server
make docs-serve

# Build documentation
make docs-build

# Build documentation in strict mode
make docs-strict
```

### Development Workflow
```bash
# Complete initial setup for development
make setup

# Run pre-commit hooks on all files
make pre-commit

# Run CI-equivalent checks (fast tests + quality + docs)
make check

# Run specific problem
make run-problem PROBLEM=001
```

### Utilities
```bash
# Clean cache and temporary files
make clean

# Clean documentation build files
make clean-docs

# Clean generated reports
make clean-reports

# Clean everything
make clean-all

# List all available problems
make problems

# Show project status
make status

# Create new problem template
make new-problem PROBLEM=010
```

### Legacy Commands (Still Available)
For direct access to underlying tools:
```bash
# Direct pytest commands
uv run pytest
uv run pytest tests/problems/test_problem_001.py
uv run pytest -m "not slow"
uv run pytest -v

# Direct ruff commands
uv run ruff format
uv run ruff check --fix

# Direct mypy command
uv run mypy .

# Direct bandit command
uv run bandit -r problems/

# Direct mkdocs commands
uv run mkdocs serve --dev-addr=127.0.0.1:8000
uv run mkdocs build
uv run mkdocs build --clean --strict
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
   - `solve_naive()` - Straightforward implementation for understanding
   - `solve_optimized()` - Optimized algorithm with better complexity
   - `solve_mathematical()` - Mathematical/formula-based approach (only when there's clear mathematical insight)

2. **Comprehensive Testing**:
   - Unit tests with parametrized test cases
   - Edge case handling
   - Functional verification (optimized for CI speed)
   - All solutions must agree on results

3. **Performance Analysis**:
   - Time complexity documentation
   - Algorithm correctness verification
   - Project Euler's one-minute rule verification
   - CI-optimized test execution
   - Simple learning-focused benchmarks

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

**Standard template (2 approaches):**
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

def test_solutions() -> None:
    """テストケースで解答を検証"""

def main() -> None:
    """メイン関数 - includes performance benchmarking"""
```

**Extended template (3 approaches, only when mathematical insight exists):**
```python
def solve_mathematical(limit: int) -> int:
    """
    数学的解法: [Description in Japanese with clear mathematical insight]
    時間計算量: O(1)
    空間計算量: O(1)
    """
```

**Note**: Mathematical solutions are only implemented when there's a clear mathematical insight that differs significantly from the optimized approach.

## Project Status and Workflow

### Current Progress
Use `make progress` and `make stats` commands to get up-to-date project statistics.

```bash
# View visual progress toward 100 problems goal
make progress

# View detailed project statistics
make stats
```

**🎉 PROJECT COMPLETED! 🎉**
- **Completed**: 100/100 problems (100.0%)
- **Status**: All first 100 Project Euler problems successfully implemented
- **Achievement**: Goal reached with comprehensive solutions, tests, and documentation
- **Next Phase**: Repository serves as reference implementation for Project Euler solutions

### Development Workflow
The enhanced Makefile provides streamlined commands for the complete development workflow:

1. **Create GitHub issue for new problem**:
   ```bash
   make issue-create PROBLEM=025 TITLE="Reciprocal cycles"
   ```

2. **Create feature branch from issue**:
   ```bash
   make issue-develop ISSUE=123
   ```

3. **Implement solution with multiple approaches**:
   ```bash
   make new-problem PROBLEM=025  # Generate template files
   # Edit problems/problem_025.py
   # Edit tests/problems/test_problem_025.py
   # Edit docs/solutions/solution_025.md
   ```

4. **Test and validate locally**:
   ```bash
   make test-problem PROBLEM=025  # Test specific problem
   make ci-check                  # Run full CI checks locally
   make validate                  # Validate configuration files
   ```

5. **Performance analysis**:
   ```bash
   make benchmark-problem PROBLEM=025  # Benchmark performance
   make stats                          # Check project statistics
   make progress                       # View progress toward goal
   ```

6. **Create PR**:
   ```bash
   make pr-create ISSUE=123 TITLE="Solve Problem 025: Reciprocal cycles"
   ```

7. **Monitor CI and merge**:
   ```bash
   make pr-status PR=124          # Check PR status and CI results
   make pr-merge PR=124           # Merge after CI passes
   ```

8. **Close issue**:
   ```bash
   make issue-close ISSUE=123     # Close completed issue
   ```

9. **Cleanup**:
   ```bash
   # Branches are automatically deleted during merge
   make clean                     # Clean temporary files
   make stats                     # View updated statistics
   ```

### Quality Standards
- Minimum 2 solution approaches per problem (3 approaches only when clear mathematical insight exists)
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
- **Fast tests**: All problems tested in ~0.1-0.4 seconds
- **Slow tests**: Performance-intensive tests in ~0.03 seconds
- **Total**: All 100 problems tested in under 1 second
- **CI optimization**: Fast and slow tests run in separate steps for better visibility

Tests are configured with strict settings and comprehensive markers for different test types (unit, integration, slow).

## Enhanced Makefile Features

### GitHub CLI Integration
The Makefile provides seamless GitHub workflow automation:
- **Issue Management**: Create, develop, and close issues
- **Branch Management**: Automatic branch creation from issues
- **PR Management**: Create, monitor, and safely merge pull requests
- **CI Integration**: Automated status checking and validation

### Performance Analysis
Built-in performance monitoring and analysis tools:
- **Benchmarking**: Individual and bulk problem performance testing
- **Statistics**: Comprehensive project metrics and progress tracking
- **Progress Visualization**: Visual progress bars and milestone tracking
- **JSON Reporting**: Machine-readable benchmark results

### Development Workflow Automation
Streamlined commands for common development tasks:
- **Local CI**: Fast local validation matching GitHub Actions
- **Configuration Validation**: Automated checks for project configuration files
- **Template Generation**: Automated creation of problem files with proper structure
- **Cleanup Operations**: Intelligent cache and artifact management

### Color-Coded Help System
The Makefile includes an enhanced help system with:
- **Categorized Commands**: Logical grouping of related commands
- **Color Coding**: Visual distinction between command types
- **Usage Examples**: Clear examples for complex commands
- **Error Handling**: Comprehensive validation and user-friendly error messages

## Configuration Details

### Tool Configuration
- **Ruff**: Unified linting and formatting, replaces Black/isort/flake8/pylint
- **MyPy**: Strict typing enabled, handles import issues for problem modules
- **Pytest**: Comprehensive markers, strict configuration
- **Bandit**: Security scanning with specific exclusions for test files
- **UV**: Fast Python package manager and project management
- **Pre-commit**: Automated code quality checks with ruff-based hooks
- **GitHub CLI**: Integrated workflow automation and PR management

### Import Handling
The project uses dynamic imports for problem modules in tests. MyPy configuration includes specific overrides for problem modules to handle import resolution.

## Performance Optimization History

### Test Performance Optimization (2025-06)
- **Problem**: CI execution time was 58+ seconds due to timing-based performance tests
- **Solution**: Refactored all performance tests to use functional verification instead of `time.time()` measurements
- **Results**:
  - Execution time reduced from 58s to 0.1-0.4s (99.3% improvement)
  - Maintained 100% test coverage for all 100 problems
  - Split CI into fast tests and slow tests for better visibility
  - All Project Euler correctness verification preserved

### Makefile Enhancement (2025-06)
- **Problem**: Complex development workflow required multiple manual commands and GitHub CLI operations
- **Solution**: Comprehensive Makefile with GitHub CLI integration and automation
- **Results**:
  - 95% reduction in manual commands for common workflows
  - Automated GitHub issue/PR creation and management
  - Built-in performance benchmarking and project statistics
  - Enhanced error handling and validation
  - Color-coded help system with categorized commands

## CI/CD Process

### GitHub Actions Workflow
The project uses automated CI/CD with the following checks:
- **Test (Python 3.11)**: Run all tests on Python 3.11
- **Test (Python 3.12)**: Run all tests on Python 3.12
- **Quality**: Code quality checks (ruff, mypy, bandit)

### PR Merge Requirements
**CRITICAL**: PRs must only be merged after ALL CI checks pass:

```bash
# Check CI status before merging (automated in Makefile)
make pr-status PR=123

# Safe merge with automated validation
make pr-merge PR=123  # Will fail if CI checks are not passing

# Manual verification (if needed)
gh pr view [PR_NUMBER] --json statusCheckRollup

# Expected output for successful CI:
# - "conclusion": "SUCCESS" for all checks
# - test (3.11): SUCCESS
# - test (3.12): SUCCESS
# - quality: SUCCESS
```

**The `make pr-merge` command automatically validates CI status and prevents merging if any checks are failing.**

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

## Git and PR Guidelines

### PR Submission Guidelines

**CRITICAL**: PRs must only be created after ALL local checks pass to prevent CI failures.

#### Pre-PR Checklist (Required)

**Step 1: Complete Local Quality Checks**
```bash
# Run all code quality checks locally
make quality

# Alternative: Run full CI-equivalent checks
make ci-check
```

**Step 2: Verify Pre-commit Hooks Pass**
```bash
# Add all changes and test commit WITHOUT --no-verify
git add .
git commit -m "Your commit message"
```

**IMPORTANT**: If pre-commit hooks fail:
- **DO NOT** use `--no-verify` to bypass failures
- Fix the issues first, then commit again

**Step 3: Fix Any Pre-commit Hook Failures**
```bash
# Automatically fix common issues
make lint-fix
make format

# Re-add files and commit
git add .
git commit --amend --no-edit  # Include fixes in the same commit
```

**Step 4: Verify Clean State**
```bash
# Ensure all checks pass
make ci-check

# Verify git status is clean
git status
```

**Step 5: Push and Create PR**
```bash
# Push to remote branch
git push

# Create pull request
make pr-create ISSUE=123 TITLE="Your PR Title"
```

#### Common Pre-commit Hook Issues

**Formatting Issues:**
- Missing trailing newlines (`W292`)
- Trailing whitespace
- Import sorting
- Code formatting

**Quality Issues:**
- Linting errors (ruff)
- Type checking errors (mypy)
- Security issues (bandit - low severity acceptable)

**Quick Fix Commands:**
```bash
# Fix most formatting issues automatically
make lint-fix

# Format code consistently
make format

# Check types
make typecheck
```

#### Why This Process Matters

1. **Prevents CI Failures**: Catches issues before they reach GitHub Actions
2. **Reduces Review Cycles**: Cleaner PRs require fewer back-and-forth corrections
3. **Maintains Code Quality**: Ensures consistent standards across the codebase
4. **Saves Time**: Avoids the need for additional "fix linting" commits

#### Workflow Integration

This checklist integrates with the existing development workflow:

```bash
# After implementing solution
make test-problem PROBLEM=033
make ci-check                    # ← Critical step

# Commit with pre-commit hook validation
git add .
git commit -m "Implement solution"  # ← No --no-verify

# Only proceed if commit succeeds
git push
make pr-create ISSUE=123 TITLE="Solution"
```

### Additional PR Guidelines
- **Branch Verification**: Ensure you're pushing to the correct feature branch
- **Commit Messages**: Use descriptive commit messages following project conventions
- **CI Status**: Monitor CI status after PR creation using `make pr-status PR=123`

### Git Worktree for Parallel Development

Git worktrees enable parallel development on multiple problems simultaneously by creating separate working directories that share the same Git repository. This is particularly useful for Project Euler problems where you might want to work on multiple problems at once without context switching.

#### Benefits of Git Worktrees
- **Parallel Development**: Work on multiple problems simultaneously without branch switching
- **Isolated Environments**: Each worktree has its own working directory and index
- **Shared Repository**: All worktrees share the same Git repository and remote references
- **Fast Context Switching**: No need to stash changes or commit incomplete work

#### Setting Up Worktrees

**Create a worktree for a new problem:**
```bash
# Create worktree for problem 025 in a subdirectory
git worktree add ../project-euler-problem-025 problem-025

# Or create in a dedicated worktrees directory
mkdir -p ../worktrees
git worktree add ../worktrees/problem-025 problem-025

# Create worktree with new branch from issue
make issue-develop ISSUE=123  # Creates branch from GitHub issue
git worktree add ../worktrees/problem-025 problem-025-branch-name
```

**List existing worktrees:**
```bash
git worktree list
```

**Navigate between worktrees:**
```bash
# Switch to different worktree directory
cd ../worktrees/problem-025

# Each worktree can run Makefile commands independently
make test-problem PROBLEM=025
make run-problem PROBLEM=025
make ci-check
```

#### Workflow Integration

**Parallel problem development:**
```bash
# Main repository: working on problem 024
cd project-euler-first100
make test-problem PROBLEM=024

# Worktree 1: working on problem 025
cd ../worktrees/problem-025
make new-problem PROBLEM=025
make test-problem PROBLEM=025

# Worktree 2: working on problem 026
cd ../worktrees/problem-026
make new-problem PROBLEM=026
make run-problem PROBLEM=026

# Each worktree maintains its own virtual environment and dependencies
```

**Independent CI checks:**
```bash
# Run CI checks in each worktree independently
cd ../worktrees/problem-025
make ci-check

cd ../worktrees/problem-026
make ci-check
```

#### Best Practices

**Worktree Organization:**
```bash
# Recommended directory structure
project-euler-first100/          # Main repository
../worktrees/
  ├── problem-025/               # Problem-specific worktrees
  ├── problem-026/
  ├── refactor-testing/          # Feature worktrees
  └── docs-update/
```

**Naming Conventions:**
- Problem worktrees: `problem-XXX` (matches branch names)
- Feature worktrees: `feature-description` or `issue-123`
- Maintenance worktrees: `refactor-component`, `docs-update`

**Shared Dependencies:**
```bash
# Each worktree needs its own virtual environment
cd ../worktrees/problem-025
uv sync --extra dev           # Create separate .venv for this worktree

# Or use shared UV cache to avoid re-downloading
export UV_CACHE_DIR="$HOME/.cache/uv"  # Shared cache location
```

#### Common Commands

**Create worktree from existing branch:**
```bash
git worktree add ../worktrees/existing-branch existing-branch-name
```

**Create worktree with new branch:**
```bash
git worktree add -b new-branch-name ../worktrees/new-feature origin/main
```

**Remove completed worktree:**
```bash
# First, delete the worktree directory (after merging branch)
git worktree remove ../worktrees/problem-025

# Or remove and clean up automatically
git worktree remove --force ../worktrees/problem-025
```

**Move worktree location:**
```bash
git worktree move ../worktrees/problem-025 ../new-location/problem-025
```

#### Integration with GitHub Workflow

**PR creation from worktrees:**
```bash
# In any worktree, create PR normally
cd ../worktrees/problem-025
make pr-create ISSUE=123 TITLE="Solve Problem 025"

# Monitor PR status
make pr-status PR=124

# Merge and cleanup
make pr-merge PR=124
git worktree remove ../worktrees/problem-025  # After successful merge
```

**Branch synchronization:**
```bash
# All worktrees share the same repository
# Changes in main branch are visible across all worktrees
git fetch origin                    # Updates all worktrees
git branch -a                       # Shows all branches across worktrees
```

#### Troubleshooting

**Common issues and solutions:**

```bash
# Issue: Worktree directory already exists
git worktree add ../worktrees/problem-025 problem-025
# Error: '../worktrees/problem-025' already exists

# Solution: Remove directory first or use different path
rm -rf ../worktrees/problem-025
git worktree add ../worktrees/problem-025 problem-025

# Issue: Branch already checked out in another worktree
# Error: 'problem-025' is already checked out at '../worktrees/problem-025'

# Solution: Use different branch name or remove other worktree
git worktree list                   # Find where branch is checked out
git worktree remove path/to/worktree

# Issue: Virtual environment conflicts
# Make sure each worktree has its own .venv
cd ../worktrees/problem-025
uv sync --extra dev                 # Creates separate .venv

# Issue: Stale worktree references
git worktree prune                  # Clean up deleted worktree references
```

**Cleanup:**
```bash
# List all worktrees
git worktree list

# Remove unused worktrees (after branches are merged)
git worktree prune

# Force remove worktree (if directory was manually deleted)
git worktree remove --force path/to/worktree
```

#### When to Use Worktrees

**Recommended scenarios:**
- Working on multiple problems simultaneously
- Long-running feature development alongside quick fixes
- Testing different algorithmic approaches in parallel
- Maintaining separate environments for different Python versions

**When to avoid:**
- Simple single-problem development (traditional branching is sufficient)
- When disk space is limited (each worktree needs separate dependencies)
- For beginners unfamiliar with Git (stick to basic branching initially)

# important-instruction-reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.

**CRITICAL PR SUBMISSION REQUIREMENT**:
ALWAYS follow the PR Submission Guidelines above. NEVER create pull requests without first:
1. Running `make ci-check` locally
2. Committing without `--no-verify` to test pre-commit hooks
3. Fixing any pre-commit hook failures before proceeding
4. Ensuring all local checks pass before pushing and creating PR

This prevents CI failures and maintains code quality standards.
