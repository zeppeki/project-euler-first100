# Project Euler First 100 - Makefile
# 開発作業でよく使うコマンドをまとめたMakefile

# Variables
PYTHON := uv run python
UV := uv
PYTEST := $(UV) run pytest
RUFF := $(UV) run ruff
MYPY := $(UV) run mypy
BANDIT := $(UV) run bandit
MKDOCS := $(UV) run mkdocs
PRE_COMMIT := $(UV) run pre-commit

# Colors for output
BOLD := \033[1m
RED := \033[31m
GREEN := \033[32m
YELLOW := \033[33m
BLUE := \033[34m
MAGENTA := \033[35m
CYAN := \033[36m
RESET := \033[0m

# Default target
.DEFAULT_GOAL := help

# PHONY targets
.PHONY: help install install-dev install-docs update
.PHONY: test test-fast test-slow test-cov test-problem
.PHONY: format lint lint-fix typecheck security quality
.PHONY: docs-serve docs-build docs-strict
.PHONY: pre-commit setup check run-problem
.PHONY: clean clean-docs clean-all
.PHONY: problems status new-problem

## Help
help: ## Show this help message
	@echo "$(BOLD)$(BLUE)Project Euler First 100 - Development Commands$(RESET)"
	@echo
	@echo "$(BOLD)Dependencies:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /install|update/ {printf "  $(CYAN)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo
	@echo "$(BOLD)Testing:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /test/ {printf "  $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo
	@echo "$(BOLD)Code Quality:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /format|lint|typecheck|security|quality/ {printf "  $(YELLOW)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo
	@echo "$(BOLD)Documentation:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /docs/ {printf "  $(MAGENTA)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo
	@echo "$(BOLD)Development Workflow:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /setup|check|pre-commit|run-problem/ {printf "  $(BLUE)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo
	@echo "$(BOLD)Utilities:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /clean|problems|status|new-problem/ {printf "  $(RED)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo
	@echo "$(BOLD)Examples:$(RESET)"
	@echo "  make test-problem PROBLEM=001    # Test specific problem"
	@echo "  make run-problem PROBLEM=001     # Run specific problem"
	@echo "  make new-problem PROBLEM=010     # Create new problem template"

## Dependencies
install: ## Install all dependencies (recommended)
	@echo "$(BOLD)$(CYAN)Installing all dependencies...$(RESET)"
	$(UV) sync --extra all

install-dev: ## Install development dependencies only
	@echo "$(BOLD)$(CYAN)Installing development dependencies...$(RESET)"
	$(UV) sync --extra dev

install-docs: ## Install documentation dependencies only
	@echo "$(BOLD)$(CYAN)Installing documentation dependencies...$(RESET)"
	$(UV) sync --extra docs

update: ## Update dependencies
	@echo "$(BOLD)$(CYAN)Updating dependencies...$(RESET)"
	$(UV) sync --extra all --upgrade

## Testing
test: ## Run all tests
	@echo "$(BOLD)$(GREEN)Running all tests...$(RESET)"
	$(PYTEST)

test-fast: ## Run fast tests only (exclude slow tests)
	@echo "$(BOLD)$(GREEN)Running fast tests...$(RESET)"
	$(PYTEST) -m "not slow"

test-slow: ## Run slow tests only
	@echo "$(BOLD)$(GREEN)Running slow tests...$(RESET)"
	$(PYTEST) -m "slow"

test-cov: ## Run tests with coverage report
	@echo "$(BOLD)$(GREEN)Running tests with coverage...$(RESET)"
	$(PYTEST) --cov=problems --cov=solutions --cov-report=html --cov-report=term

test-problem: ## Run tests for specific problem (use: make test-problem PROBLEM=001)
	@if [ -z "$(PROBLEM)" ]; then \
		echo "$(RED)Error: PROBLEM variable is required$(RESET)"; \
		echo "Usage: make test-problem PROBLEM=001"; \
		exit 1; \
	fi
	@echo "$(BOLD)$(GREEN)Running tests for Problem $(PROBLEM)...$(RESET)"
	$(PYTEST) tests/problems/test_problem_$(PROBLEM).py -v

## Code Quality
format: ## Format code with ruff
	@echo "$(BOLD)$(YELLOW)Formatting code...$(RESET)"
	$(RUFF) format problems/ solutions/ tests/

lint: ## Check code with ruff (no fixes)
	@echo "$(BOLD)$(YELLOW)Checking code with ruff...$(RESET)"
	$(RUFF) check problems/ solutions/ tests/

lint-fix: ## Check and fix code with ruff
	@echo "$(BOLD)$(YELLOW)Checking and fixing code with ruff...$(RESET)"
	$(RUFF) check --fix problems/ solutions/ tests/

typecheck: ## Run type checking with mypy
	@echo "$(BOLD)$(YELLOW)Running type checking...$(RESET)"
	$(MYPY) problems/ solutions/ tests/

security: ## Run security scan with bandit
	@echo "$(BOLD)$(YELLOW)Running security scan...$(RESET)"
	$(BANDIT) -r problems/ solutions/ tests/ -f json || true

quality: format lint typecheck security ## Run all code quality checks
	@echo "$(BOLD)$(GREEN)All quality checks completed!$(RESET)"

## Documentation
docs-serve: ## Start documentation development server
	@echo "$(BOLD)$(MAGENTA)Starting documentation server...$(RESET)"
	@echo "$(CYAN)Documentation will be available at: http://127.0.0.1:8000$(RESET)"
	$(MKDOCS) serve --dev-addr=127.0.0.1:8000

docs-build: ## Build documentation
	@echo "$(BOLD)$(MAGENTA)Building documentation...$(RESET)"
	$(MKDOCS) build --clean

docs-strict: ## Build documentation in strict mode (warnings as errors)
	@echo "$(BOLD)$(MAGENTA)Building documentation in strict mode...$(RESET)"
	$(MKDOCS) build --clean --strict

## Development Workflow
setup: install ## Complete initial setup for development
	@echo "$(BOLD)$(BLUE)Setting up development environment...$(RESET)"
	$(PRE_COMMIT) install
	@echo "$(BOLD)$(GREEN)Setup completed! You can now start developing.$(RESET)"

pre-commit: ## Run pre-commit hooks on all files
	@echo "$(BOLD)$(BLUE)Running pre-commit hooks...$(RESET)"
	$(PRE_COMMIT) run --all-files

check: test-fast quality docs-strict ## Run CI-equivalent checks (fast tests + quality + docs)
	@echo "$(BOLD)$(GREEN)All CI checks passed!$(RESET)"

run-problem: ## Run specific problem (use: make run-problem PROBLEM=001)
	@if [ -z "$(PROBLEM)" ]; then \
		echo "$(RED)Error: PROBLEM variable is required$(RESET)"; \
		echo "Usage: make run-problem PROBLEM=001"; \
		exit 1; \
	fi
	@if [ ! -f "problems/problem_$(PROBLEM).py" ]; then \
		echo "$(RED)Error: problems/problem_$(PROBLEM).py not found$(RESET)"; \
		exit 1; \
	fi
	@echo "$(BOLD)$(BLUE)Running Problem $(PROBLEM)...$(RESET)"
	$(PYTHON) problems/problem_$(PROBLEM).py

## Utilities
clean: ## Clean cache and temporary files
	@echo "$(BOLD)$(RED)Cleaning cache and temporary files...$(RESET)"
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@find . -name "*.pyo" -delete 2>/dev/null || true
	@find . -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

clean-docs: ## Clean documentation build files
	@echo "$(BOLD)$(RED)Cleaning documentation build files...$(RESET)"
	@rm -rf site/

clean-all: clean clean-docs ## Clean everything
	@echo "$(BOLD)$(GREEN)All cleaned!$(RESET)"

problems: ## List all available problems
	@echo "$(BOLD)$(CYAN)Available Problems:$(RESET)"
	@for file in problems/problem_*.py; do \
		if [ -f "$$file" ]; then \
			problem=$$(basename "$$file" .py | sed 's/problem_//'); \
			title=$$(grep -E '^Problem [0-9]+:' "$$file" | head -1 | sed 's/Problem [0-9]*: *//'); \
			if [ -z "$$title" ]; then \
				title="No title found"; \
			fi; \
			printf "  $(GREEN)%-6s$(RESET) %s\n" "$$problem" "$$title"; \
		fi; \
	done

status: ## Show project status
	@echo "$(BOLD)$(CYAN)Project Status:$(RESET)"
	@echo
	@echo "$(BOLD)Problems Implemented:$(RESET)"
	@problem_count=$$(ls problems/problem_*.py 2>/dev/null | wc -l); \
	echo "  Count: $$problem_count/100"
	@echo
	@echo "$(BOLD)Tests:$(RESET)"
	@test_count=$$(ls tests/problems/test_problem_*.py 2>/dev/null | wc -l); \
	echo "  Test files: $$test_count"
	@echo
	@echo "$(BOLD)Documentation:$(RESET)"
	@doc_count=$$(ls docs/solutions/solution_*.md 2>/dev/null | wc -l); \
	echo "  Solution docs: $$doc_count"
	@echo
	@echo "$(BOLD)Git Status:$(RESET)"
	@git status --porcelain | wc -l | xargs printf "  Modified files: %s\n"
	@git rev-parse --abbrev-ref HEAD | xargs printf "  Current branch: %s\n"

new-problem: ## Create new problem template (use: make new-problem PROBLEM=010)
	@if [ -z "$(PROBLEM)" ]; then \
		echo "$(RED)Error: PROBLEM variable is required$(RESET)"; \
		echo "Usage: make new-problem PROBLEM=010"; \
		exit 1; \
	fi
	@if [ -f "problems/problem_$(PROBLEM).py" ]; then \
		echo "$(RED)Error: problems/problem_$(PROBLEM).py already exists$(RESET)"; \
		exit 1; \
	fi
	@echo "$(BOLD)$(BLUE)Creating template for Problem $(PROBLEM)...$(RESET)"
	@mkdir -p problems tests/problems docs/solutions
	@echo '#!/usr/bin/env python3' > problems/problem_$(PROBLEM).py
	@echo '"""' >> problems/problem_$(PROBLEM).py
	@echo 'Problem $(PROBLEM): [Problem Title]' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo '[Problem description here]' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo 'Answer: [Answer here]' >> problems/problem_$(PROBLEM).py
	@echo '"""' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo 'import time' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo 'def solve_naive() -> int:' >> problems/problem_$(PROBLEM).py
	@echo '    """' >> problems/problem_$(PROBLEM).py
	@echo '    素直な解法: [Description]' >> problems/problem_$(PROBLEM).py
	@echo '    時間計算量: O(n)' >> problems/problem_$(PROBLEM).py
	@echo '    空間計算量: O(1)' >> problems/problem_$(PROBLEM).py
	@echo '    """' >> problems/problem_$(PROBLEM).py
	@echo '    # TODO: Implement naive solution' >> problems/problem_$(PROBLEM).py
	@echo '    pass' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo 'def solve_optimized() -> int:' >> problems/problem_$(PROBLEM).py
	@echo '    """' >> problems/problem_$(PROBLEM).py
	@echo '    最適化解法: [Description]' >> problems/problem_$(PROBLEM).py
	@echo '    時間計算量: O(log n)' >> problems/problem_$(PROBLEM).py
	@echo '    空間計算量: O(1)' >> problems/problem_$(PROBLEM).py
	@echo '    """' >> problems/problem_$(PROBLEM).py
	@echo '    # TODO: Implement optimized solution' >> problems/problem_$(PROBLEM).py
	@echo '    pass' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo 'def solve_mathematical() -> int:' >> problems/problem_$(PROBLEM).py
	@echo '    """' >> problems/problem_$(PROBLEM).py
	@echo '    数学的解法: [Description]' >> problems/problem_$(PROBLEM).py
	@echo '    時間計算量: O(1)' >> problems/problem_$(PROBLEM).py
	@echo '    空間計算量: O(1)' >> problems/problem_$(PROBLEM).py
	@echo '    """' >> problems/problem_$(PROBLEM).py
	@echo '    # TODO: Implement mathematical solution' >> problems/problem_$(PROBLEM).py
	@echo '    pass' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo 'def test_solutions() -> None:' >> problems/problem_$(PROBLEM).py
	@echo '    """テストケースで解答を検証"""' >> problems/problem_$(PROBLEM).py
	@echo '    # TODO: Add test cases' >> problems/problem_$(PROBLEM).py
	@echo '    pass' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo 'def main() -> None:' >> problems/problem_$(PROBLEM).py
	@echo '    """メイン関数"""' >> problems/problem_$(PROBLEM).py
	@echo '    print("=== Problem $(PROBLEM): [Problem Title] ===")' >> problems/problem_$(PROBLEM).py
	@echo '    # TODO: Implement main function' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo 'if __name__ == "__main__":' >> problems/problem_$(PROBLEM).py
	@echo '    main()' >> problems/problem_$(PROBLEM).py
	@echo "$(GREEN)Created: problems/problem_$(PROBLEM).py$(RESET)"
	@echo '#!/usr/bin/env python3' > tests/problems/test_problem_$(PROBLEM).py
	@echo '"""Tests for Problem $(PROBLEM)"""' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo 'import pytest' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo 'from problems.problem_$(PROBLEM) import solve_naive, solve_optimized, solve_mathematical' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo 'class TestProblem$(PROBLEM):' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '    """Test cases for Problem $(PROBLEM)"""' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '    def test_solve_naive(self) -> None:' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        """Test naive solution"""' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        # TODO: Add test cases' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        pass' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '    def test_solve_optimized(self) -> None:' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        """Test optimized solution"""' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        # TODO: Add test cases' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        pass' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '    def test_solve_mathematical(self) -> None:' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        """Test mathematical solution"""' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        # TODO: Add test cases' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        pass' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '    def test_solutions_agree(self) -> None:' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        """Test that all solutions agree"""' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        # TODO: Verify all solutions return same result' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        pass' >> tests/problems/test_problem_$(PROBLEM).py
	@echo "$(GREEN)Created: tests/problems/test_problem_$(PROBLEM).py$(RESET)"
	@echo '# Problem $(PROBLEM): [Problem Title]' > docs/solutions/solution_$(PROBLEM).md
	@echo '' >> docs/solutions/solution_$(PROBLEM).md
	@echo '## 問題' >> docs/solutions/solution_$(PROBLEM).md
	@echo '[Problem description in Japanese]' >> docs/solutions/solution_$(PROBLEM).md
	@echo '' >> docs/solutions/solution_$(PROBLEM).md
	@echo '## 解答' >> docs/solutions/solution_$(PROBLEM).md
	@echo '' >> docs/solutions/solution_$(PROBLEM).md
	@echo 'Project Euler公式サイトで確認してください。' >> docs/solutions/solution_$(PROBLEM).md
	@echo '' >> docs/solutions/solution_$(PROBLEM).md
	@echo '## 解法' >> docs/solutions/solution_$(PROBLEM).md
	@echo '' >> docs/solutions/solution_$(PROBLEM).md
	@echo '### 1. 素直な解法 (Naive Approach)' >> docs/solutions/solution_$(PROBLEM).md
	@echo '[TODO: Add solution description]' >> docs/solutions/solution_$(PROBLEM).md
	@echo '' >> docs/solutions/solution_$(PROBLEM).md
	@echo '### 2. 最適化解法 (Optimized Approach)' >> docs/solutions/solution_$(PROBLEM).md
	@echo '[TODO: Add solution description]' >> docs/solutions/solution_$(PROBLEM).md
	@echo '' >> docs/solutions/solution_$(PROBLEM).md
	@echo '### 3. 数学的解法 (Mathematical Approach)' >> docs/solutions/solution_$(PROBLEM).md
	@echo '[TODO: Add solution description]' >> docs/solutions/solution_$(PROBLEM).md
	@echo "$(GREEN)Created: docs/solutions/solution_$(PROBLEM).md$(RESET)"
	@echo "$(BOLD)$(GREEN)Problem $(PROBLEM) template created successfully!$(RESET)"
	@echo "$(CYAN)Next steps:$(RESET)"
	@echo "  1. Edit problems/problem_$(PROBLEM).py with problem description and solutions"
	@echo "  2. Add test cases to tests/problems/test_problem_$(PROBLEM).py"
	@echo "  3. Update docs/solutions/solution_$(PROBLEM).md with detailed explanation"
