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
.PHONY: test test-fast test-slow test-cov test-cov-clean test-problem
.PHONY: format lint lint-fix typecheck security quality
.PHONY: coverage dependency-check metrics ci-full ci-check validate
.PHONY: docs-serve docs-build docs-strict docs-update-dashboard docs-build-with-data
.PHONY: pre-commit setup check run-problem
.PHONY: clean clean-docs clean-all clean-reports
.PHONY: problems status stats progress new-problem
.PHONY: benchmark benchmark-simple benchmark-simple-problem benchmark-problem benchmark-comprehensive benchmark-problem-timeout benchmark-problem-extended benchmark-retry-failed
.PHONY: issue-create issue-develop pr-create pr-status pr-merge issue-close

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
	@echo "$(BOLD)GitHub Workflow:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /issue-|pr-/ {printf "  $(MAGENTA)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo
	@echo "$(BOLD)Performance & Analysis:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /benchmark|stats|progress/ {printf "  $(CYAN)%-30s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo
	@echo "$(BOLD)Utilities:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / && /clean|problems|status|new-problem/ {printf "  $(RED)%-20s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo
	@echo "$(BOLD)Examples:$(RESET)"
	@echo "  make test-problem PROBLEM=001              # Test specific problem"
	@echo "  make run-problem PROBLEM=001               # Run specific problem"
	@echo "  make benchmark-simple-problem PROBLEM=001 # Quick benchmark"
	@echo "  make benchmark-comprehensive               # Full benchmark with timeout"
	@echo "  make benchmark-problem-extended PROBLEM=086 TIMEOUT=300  # Extended timeout benchmark"
	@echo "  make new-problem PROBLEM=010               # Create new problem template"
	@echo "  make issue-create PROBLEM=025              # Create GitHub issue for problem"
	@echo "  make pr-create ISSUE=123                   # Create PR for issue"

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

test-cov: ## Run tests with coverage report (problems only, excludes runners/utils)
	@echo "$(BOLD)$(GREEN)Running tests with coverage (problems only)...$(RESET)"
	$(PYTEST) --cov=problems --cov-report=html --cov-report=term

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
	$(RUFF) format problems/ tests/

lint: ## Check code with ruff (no fixes)
	@echo "$(BOLD)$(YELLOW)Checking code with ruff...$(RESET)"
	$(RUFF) check problems/ tests/

lint-fix: ## Check and fix code with ruff
	@echo "$(BOLD)$(YELLOW)Checking and fixing code with ruff...$(RESET)"
	$(RUFF) check --fix problems/ tests/

typecheck: ## Run type checking with mypy
	@echo "$(BOLD)$(YELLOW)Running type checking...$(RESET)"
	$(MYPY) problems/ tests/

security: ## Run security scan with bandit
	@echo "$(BOLD)$(YELLOW)Running security scan...$(RESET)"
	$(BANDIT) -r problems/ tests/ --skip B101 -f json || true

coverage: ## Generate test coverage report (problems only, excludes runners/utils)
	@echo "$(BOLD)$(YELLOW)Generating coverage report (problems only)...$(RESET)"
	$(PYTEST) --cov=problems --cov-report=html --cov-report=xml --cov-report=term

dependency-check: ## Run dependency security scan
	@echo "$(BOLD)$(YELLOW)Running dependency security scan...$(RESET)"
	$(UV) run safety check --json > safety-report.json || echo '[]' > safety-report.json
	@echo "$(CYAN)Report saved to safety-report.json$(RESET)"

metrics: ## Run code metrics analysis
	@echo "$(BOLD)$(YELLOW)Running code metrics analysis...$(RESET)"
	@echo "$(CYAN)Radon - Code complexity metrics...$(RESET)"
	$(UV) run radon cc problems/ -s -j > radon-cc.json
	$(UV) run radon mi problems/ -s -j > radon-mi.json
	$(UV) run radon hal problems/ -j > radon-hal.json
	@echo "$(CYAN)Xenon - Cyclomatic complexity...$(RESET)"
	$(UV) run xenon problems/ --max-absolute A --max-modules A --max-average A > xenon-report.txt || echo 'No complexity issues found' > xenon-report.txt
	@echo "$(CYAN)Reports saved: radon-*.json, xenon-report.txt$(RESET)"

quality: format lint typecheck security ## Run all code quality checks
	@echo "$(BOLD)$(GREEN)All quality checks completed!$(RESET)"

ci-full: test coverage quality dependency-check metrics docs-strict ## Run complete CI/CD pipeline locally
	@echo "$(BOLD)$(GREEN)Complete CI/CD pipeline completed successfully!$(RESET)"

ci-check: test-fast quality docs-strict ## Run CI-equivalent checks locally (fast)
	@echo "$(BOLD)$(GREEN)Local CI checks completed successfully!$(RESET)"

validate: ## Validate project configuration files
	@echo "$(BOLD)$(YELLOW)Validating project configuration...$(RESET)"
	@echo "$(CYAN)Checking pyproject.toml...$(RESET)"
	@$(UV) run python -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))" && echo "  ✓ pyproject.toml is valid"
	@echo "$(CYAN)Checking mkdocs.yml...$(RESET)"
	@$(MKDOCS) build --strict --quiet && echo "  ✓ mkdocs.yml is valid"
	@echo "$(CYAN)Checking .pre-commit-config.yaml...$(RESET)"
	@$(PRE_COMMIT) validate-config && echo "  ✓ .pre-commit-config.yaml is valid"
	@echo "$(BOLD)$(GREEN)All configuration files are valid!$(RESET)"

## Documentation
docs-serve: ## Start documentation development server
	@echo "$(BOLD)$(MAGENTA)Starting documentation server...$(RESET)"
	@echo "$(CYAN)Documentation will be available at: http://127.0.0.1:8000$(RESET)"
	@echo "$(YELLOW)Note: Use Ctrl+C to stop the server$(RESET)"
	@lsof -ti :8000 | xargs -r kill 2>/dev/null || true
	$(MKDOCS) serve --dev-addr=127.0.0.1:8000

docs-build: ## Build documentation
	@echo "$(BOLD)$(MAGENTA)Building documentation...$(RESET)"
	$(MKDOCS) build --clean

docs-strict: ## Build documentation in strict mode (warnings as errors)
	@echo "$(BOLD)$(MAGENTA)Building documentation in strict mode...$(RESET)"
	$(MKDOCS) build --clean --strict

docs-update-dashboard: ## Update dashboard with latest benchmark data
	@echo "$(BOLD)$(MAGENTA)Updating dashboard with latest benchmark data...$(RESET)"
	$(PYTHON) scripts/generate_dashboard_data.py
	@echo "$(GREEN)Dashboard data updated successfully!$(RESET)"

docs-build-with-data: docs-update-dashboard docs-build ## Build documentation with updated dashboard data
	@echo "$(BOLD)$(GREEN)Documentation built with latest benchmark data!$(RESET)"

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
	@if [ -f "problems/runners/problem_$(PROBLEM)_runner.py" ]; then \
		echo "$(BOLD)$(BLUE)Running Problem $(PROBLEM) (using runner)...$(RESET)"; \
		$(PYTHON) problems/runners/problem_$(PROBLEM)_runner.py; \
	elif [ -f "problems/problem_$(PROBLEM).py" ]; then \
		echo "$(BOLD)$(BLUE)Running Problem $(PROBLEM) (direct)...$(RESET)"; \
		$(PYTHON) problems/problem_$(PROBLEM).py; \
	else \
		echo "$(RED)Error: Neither problems/runners/problem_$(PROBLEM)_runner.py nor problems/problem_$(PROBLEM).py found$(RESET)"; \
		exit 1; \
	fi

## Performance & Analysis

benchmark: ## Run simple benchmark for all problems
	@echo "$(BOLD)$(CYAN)Running simple benchmark for all problems...$(RESET)"
	$(PYTHON) -m problems.utils.simple_runner

benchmark-simple: ## Run simple benchmark for all problems (alias for backward compatibility)
	@echo "$(BOLD)$(CYAN)Running simple benchmark for all problems...$(RESET)"
	$(PYTHON) -m problems.utils.simple_runner

benchmark-simple-problem: ## Run simple benchmark for specific problem (use: make benchmark-simple-problem PROBLEM=001)
	@if [ -z "$(PROBLEM)" ]; then \
		echo "$(RED)Error: PROBLEM variable is required$(RESET)"; \
		echo "Usage: make benchmark-simple-problem PROBLEM=001"; \
		exit 1; \
	fi
	@echo "$(BOLD)$(CYAN)Running simple benchmark for Problem $(PROBLEM)...$(RESET)"
	$(PYTHON) -m problems.utils.simple_runner $(PROBLEM)

benchmark-problem: ## Run performance benchmark for specific problem (use: make benchmark-problem PROBLEM=001)
	@if [ -z "$(PROBLEM)" ]; then \
		echo "$(RED)Error: PROBLEM variable is required$(RESET)"; \
		echo "Usage: make benchmark-problem PROBLEM=001"; \
		exit 1; \
	fi
	@if [ -f "problems/runners/problem_$(PROBLEM)_runner.py" ]; then \
		echo "$(BOLD)$(CYAN)Running performance benchmark for Problem $(PROBLEM) (using runner)...$(RESET)"; \
		$(PYTHON) problems/runners/problem_$(PROBLEM)_runner.py benchmark; \
	else \
		echo "$(RED)Error: problems/runners/problem_$(PROBLEM)_runner.py not found$(RESET)"; \
		echo "Please create a runner for Problem $(PROBLEM) first."; \
		exit 1; \
	fi
	@echo "$(BOLD)$(GREEN)Benchmark completed for Problem $(PROBLEM)$(RESET)"

benchmark-comprehensive: ## Run comprehensive benchmark with timeout for all problems
	@echo "$(BOLD)$(CYAN)Running comprehensive benchmark with timeout for all problems...$(RESET)"
	@echo "$(YELLOW)Warning: This may take significant time. Solutions exceeding 60s will timeout.$(RESET)"
	$(PYTHON) -m problems.utils.comprehensive_benchmark

benchmark-problem-timeout: ## Run comprehensive benchmark with timeout for specific problem (use: make benchmark-problem-timeout PROBLEM=001)
	@if [ -z "$(PROBLEM)" ]; then \
		echo "$(RED)Error: PROBLEM variable is required$(RESET)"; \
		echo "Usage: make benchmark-problem-timeout PROBLEM=001"; \
		exit 1; \
	fi
	@echo "$(BOLD)$(CYAN)Running comprehensive benchmark with timeout for Problem $(PROBLEM)...$(RESET)"
	$(PYTHON) -m problems.utils.comprehensive_benchmark --problems $(PROBLEM)

benchmark-problem-extended: ## Run comprehensive benchmark with extended timeout for specific problem (use: make benchmark-problem-extended PROBLEM=086 TIMEOUT=300)
	@if [ -z "$(PROBLEM)" ]; then \
		echo "$(RED)Error: PROBLEM variable is required$(RESET)"; \
		echo "Usage: make benchmark-problem-extended PROBLEM=086 TIMEOUT=300"; \
		exit 1; \
	fi
	@TIMEOUT_VAL=$${TIMEOUT:-300}; \
	echo "$(BOLD)$(CYAN)Running comprehensive benchmark with extended timeout ($$TIMEOUT_VAL seconds) for Problem $(PROBLEM)...$(RESET)"; \
	$(PYTHON) -m problems.utils.comprehensive_benchmark --problems $(PROBLEM) --timeout $$TIMEOUT_VAL

benchmark-retry-failed: ## Retry benchmarking for previously failed problems
	@echo "$(BOLD)$(CYAN)Retrying benchmarks for previously failed problems...$(RESET)"
	@echo "$(YELLOW)Note: This requires a previous comprehensive benchmark run.$(RESET)"
	$(PYTHON) -c "from problems.utils.comprehensive_benchmark import ComprehensiveBenchmark; cb = ComprehensiveBenchmark(); cb.retry_failed_problems()"

stats: ## Show detailed project statistics
	@echo "$(BOLD)$(CYAN)Project Euler First 100 - Detailed Statistics$(RESET)"
	@echo
	@echo "$(BOLD)Implementation Progress:$(RESET)"
	@problem_count=$$(ls problems/problem_*.py 2>/dev/null | wc -l); \
	progress_percent=$$(echo "scale=1; $$problem_count * 100 / 100" | bc 2>/dev/null || echo "$$problem_count"); \
	echo "  Problems implemented: $$problem_count/100 ($$progress_percent%)"
	@test_count=$$(ls tests/problems/test_problem_*.py 2>/dev/null | wc -l); \
	echo "  Test files: $$test_count"
	@doc_count=$$(ls docs/solutions/solution_*.md 2>/dev/null | wc -l); \
	echo "  Documentation files: $$doc_count"
	@echo
	@echo "$(BOLD)Code Quality Metrics:$(RESET)"
	@total_lines=$$(find problems/ -name "*.py" -exec wc -l {} + 2>/dev/null | tail -1 | awk '{print $$1}' || echo "0"); \
	echo "  Total lines of code: $$total_lines"
	@total_functions=$$(grep -r "^def " problems/ 2>/dev/null | wc -l || echo "0"); \
	echo "  Total functions: $$total_functions"
	@echo
	@echo "$(BOLD)Test Coverage:$(RESET)"
	@test_files=$$(find tests/ -name "*.py" -not -name "__*" | wc -l); \
	echo "  Test files: $$test_files"
	@total_tests=$$(grep -r "def test_" tests/ 2>/dev/null | wc -l || echo "0"); \
	echo "  Total test functions: $$total_tests"
	@echo
	@echo "$(BOLD)Repository Status:$(RESET)"
	@git status --porcelain | wc -l | xargs printf "  Modified files: %s\n"
	@git rev-parse --abbrev-ref HEAD | xargs printf "  Current branch: %s\n"
	@git log --oneline -1 | cut -d' ' -f2- | xargs printf "  Latest commit: %s\n"

progress: ## Show progress toward 100 problems goal
	@echo "$(BOLD)$(CYAN)Progress Toward 100 Problems Goal$(RESET)"
	@echo
	@problem_count=$$(ls problems/problem_*.py 2>/dev/null | wc -l); \
	remaining=$$((100 - $$problem_count)); \
	progress_percent=$$(echo "scale=1; $$problem_count * 100 / 100" | bc 2>/dev/null || echo "$$problem_count"); \
	echo "$(BOLD)Current Progress:$(RESET) $$problem_count/100 problems ($$progress_percent%)"; \
	echo "$(BOLD)Remaining:$(RESET) $$remaining problems"; \
	echo; \
	echo "$(BOLD)Progress Bar:$(RESET)"; \
	completed_bars=$$(($$problem_count / 2)); \
	remaining_bars=$$((50 - $$completed_bars)); \
	printf "  ["; \
	for i in $$(seq 1 $$completed_bars); do printf "$(GREEN)█$(RESET)"; done; \
	for i in $$(seq 1 $$remaining_bars); do printf "$(RED)░$(RESET)"; done; \
	printf "] $$progress_percent%%\n"; \
	echo; \
	if [ $$problem_count -ge 90 ]; then \
		echo "$(BOLD)$(GREEN)🎉 Excellent progress! Almost at the goal!$(RESET)"; \
	elif [ $$problem_count -ge 50 ]; then \
		echo "$(BOLD)$(YELLOW)💪 Great progress! Halfway there!$(RESET)"; \
	elif [ $$problem_count -ge 25 ]; then \
		echo "$(BOLD)$(BLUE)📈 Good progress! Keep it up!$(RESET)"; \
	else \
		echo "$(BOLD)$(CYAN)🚀 Just getting started!$(RESET)"; \
	fi

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

clean-reports: ## Clean generated reports
	@echo "$(BOLD)$(RED)Cleaning generated reports...$(RESET)"
	@rm -f bandit-report.json safety-report.json xenon-report.txt radon-*.json coverage.xml
	@rm -rf htmlcov/ .coverage benchmarks/

clean-all: clean clean-docs clean-reports ## Clean everything
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
	@echo "$(BOLD)$(BLUE)Creating template for Problem $(PROBLEM) (refactored structure)...$(RESET)"
	@mkdir -p problems/runners tests/problems docs/solutions

	# Create algorithm file (problems/problem_XXX.py)
	@echo '#!/usr/bin/env python3' > problems/problem_$(PROBLEM).py
	@echo '"""' >> problems/problem_$(PROBLEM).py
	@echo 'Problem $(PROBLEM): [Problem Title]' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo '[Problem description here]' >> problems/problem_$(PROBLEM).py
	@echo '' >> problems/problem_$(PROBLEM).py
	@echo 'Answer: [Answer here]' >> problems/problem_$(PROBLEM).py
	@echo '"""' >> problems/problem_$(PROBLEM).py
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
	@echo "$(GREEN)Created: problems/problem_$(PROBLEM).py (algorithm functions only)$(RESET)"

	# Create runner file (problems/runners/problem_XXX_runner.py)
	@echo '#!/usr/bin/env python3' > problems/runners/problem_$(PROBLEM)_runner.py
	@echo '"""' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'Runner for Problem $(PROBLEM): [Problem Title]' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'This module contains the execution code for Problem $(PROBLEM), separated from the' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'algorithm implementations for better test coverage and code organization.' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '"""' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'from problems.problem_$(PROBLEM) import solve_naive, solve_optimized' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'from problems.utils.display import (' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    print_final_answer,' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    print_performance_comparison,' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    print_solution_header,' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    print_test_results,' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo ')' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'from problems.utils.performance import compare_performance' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'def run_tests() -> None:' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    """Run test cases to verify the solutions."""' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    test_cases = [' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        # TODO: Add test cases as (input, expected_output) tuples' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        # (10, 23),' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    ]' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    functions = [' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        ("素直な解法", solve_naive),' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        ("最適化解法", solve_optimized),' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    ]' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    print_test_results(test_cases, functions)' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'def run_problem() -> None:' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    """Run the main problem with performance comparison."""' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    # TODO: Set problem parameters' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    # limit = 1000' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    print_solution_header("$(PROBLEM)", "[Problem Title]", "[limit or description]")' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    # Run tests first' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    run_tests()' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    # Run main problem with performance measurement' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    functions = [' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        ("素直な解法", lambda: solve_naive()),' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        ("最適化解法", lambda: solve_optimized()),' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    ]' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    performance_results = compare_performance(functions)' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    # Verify all solutions agree' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    results = [data["result"] for data in performance_results.values()]' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    all_agree = len(set(results)) == 1' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    if all_agree:' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        answer = results[0]' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        print_final_answer(answer, verified=True)' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        print_performance_comparison(performance_results)' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    else:' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        print_final_answer(None, verified=False)' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '        print("Results:", results)' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'def main() -> None:' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    """Main function for standalone execution."""' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    run_problem()' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo 'if __name__ == "__main__":' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo '    main()' >> problems/runners/problem_$(PROBLEM)_runner.py
	@echo "$(GREEN)Created: problems/runners/problem_$(PROBLEM)_runner.py (execution and display code)$(RESET)"

	# Create test file (tests/problems/test_problem_XXX.py)
	@echo '#!/usr/bin/env python3' > tests/problems/test_problem_$(PROBLEM).py
	@echo '"""Tests for Problem $(PROBLEM)"""' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo 'import pytest' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '' >> tests/problems/test_problem_$(PROBLEM).py
	@echo 'from problems.problem_$(PROBLEM) import solve_naive, solve_optimized' >> tests/problems/test_problem_$(PROBLEM).py
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
	@echo '    def test_solutions_agree(self) -> None:' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        """Test that all solutions agree"""' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        # TODO: Verify all solutions return same result' >> tests/problems/test_problem_$(PROBLEM).py
	@echo '        pass' >> tests/problems/test_problem_$(PROBLEM).py
	@echo "$(GREEN)Created: tests/problems/test_problem_$(PROBLEM).py (unit tests)$(RESET)"
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

## GitHub Workflow
issue-create: ## Create GitHub issue for new problem (use: make issue-create PROBLEM=025 TITLE="Problem Title")
	@if [ -z "$(PROBLEM)" ]; then \
		echo "$(RED)Error: PROBLEM variable is required$(RESET)"; \
		echo "Usage: make issue-create PROBLEM=025 TITLE=\"Problem Title\""; \
		exit 1; \
	fi
	@if [ -z "$(TITLE)" ]; then \
		title="Solve Problem $(PROBLEM)"; \
	else \
		title="$(TITLE)"; \
	fi
	@echo "$(BOLD)$(MAGENTA)Creating GitHub issue for Problem $(PROBLEM)...$(RESET)"
	@issue_url=$$(gh issue create \
		--title "Solve Problem $(PROBLEM): $$title" \
		--body "## 目標\nProject Euler Problem $(PROBLEM)の実装\n\n## タスク\n- [ ] 問題の理解と分析\n- [ ] 素直な解法の実装\n- [ ] 最適化解法の実装\n- [ ] 数学的解法の実装（必要に応じて）\n- [ ] テストケースの作成\n- [ ] ドキュメントの作成\n- [ ] パフォーマンステスト\n\n## 関連ファイル\n- problems/problem_$(PROBLEM).py\n- tests/problems/test_problem_$(PROBLEM).py\n- docs/solutions/solution_$(PROBLEM).md\n\n## 参考\n- [Project Euler Problem $(PROBLEM)](https://projecteuler.net/problem=$(PROBLEM))" \
		--label "enhancement,problem" \
		--assignee @me); \
	echo "$(GREEN)Issue created: $$issue_url$(RESET)"

issue-develop: ## Create development branch for issue (use: make issue-develop ISSUE=123)
	@if [ -z "$(ISSUE)" ]; then \
		echo "$(RED)Error: ISSUE variable is required$(RESET)"; \
		echo "Usage: make issue-develop ISSUE=123"; \
		exit 1; \
	fi
	@echo "$(BOLD)$(MAGENTA)Creating development branch for issue #$(ISSUE)...$(RESET)"
	@gh issue develop $(ISSUE) --checkout; \
	current_branch=$$(git rev-parse --abbrev-ref HEAD); \
	echo "$(GREEN)Development branch created and checked out: $$current_branch$(RESET)"

pr-create: ## Create pull request for issue (use: make pr-create ISSUE=123 TITLE="Problem Title")
	@if [ -z "$(ISSUE)" ]; then \
		echo "$(RED)Error: ISSUE variable is required$(RESET)"; \
		echo "Usage: make pr-create ISSUE=123 TITLE=\"Problem Title\""; \
		exit 1; \
	fi
	@if [ -z "$(TITLE)" ]; then \
		title="Solve Problem"; \
	else \
		title="$(TITLE)"; \
	fi
	@echo "$(BOLD)$(MAGENTA)Creating pull request for issue #$(ISSUE)...$(RESET)"
	@current_branch=$$(git rev-parse --abbrev-ref HEAD); \
	if [ "$$current_branch" = "main" ]; then \
		echo "$(RED)Error: Cannot create PR from main branch$(RESET)"; \
		exit 1; \
	fi; \
	git push -u origin $$current_branch; \
	pr_body="## Summary\nProblem solution and implementation\n\n## Changes\n- [ ] Problem solution implementation\n- [ ] Test case additions\n- [ ] Documentation updates\n\n## Test Plan\n- [ ] Unit test execution\n- [ ] Performance testing\n- [ ] Code quality checks\n\nCloses #$(ISSUE)\n\n🤖 Generated with [Claude Code](https://claude.ai/code)"; \
	pr_url=$$(gh pr create \
		--title "$$title" \
		--body "$$pr_body" \
		--assignee @me); \
	echo "$(GREEN)Pull request created: $$pr_url$(RESET)"

pr-status: ## Check pull request status (use: make pr-status PR=123)
	@if [ -z "$(PR)" ]; then \
		echo "$(RED)Error: PR variable is required$(RESET)"; \
		echo "Usage: make pr-status PR=123"; \
		exit 1; \
	fi
	@echo "$(BOLD)$(MAGENTA)Checking status of PR #$(PR)...$(RESET)"
	@gh pr view $(PR) --json statusCheckRollup,reviewDecision,mergeable,title,url \
		--template '{{.title}} - {{.url}}\nReview Status: {{.reviewDecision}}\nMergeable: {{.mergeable}}\nChecks:\n{{range .statusCheckRollup}}  - {{.context}}: {{.conclusion}}\n{{end}}'

pr-merge: ## Merge pull request after checks (use: make pr-merge PR=123)
	@if [ -z "$(PR)" ]; then \
		echo "$(RED)Error: PR variable is required$(RESET)"; \
		echo "Usage: make pr-merge PR=123"; \
		exit 1; \
	fi
	@echo "$(BOLD)$(MAGENTA)Checking PR #$(PR) status before merge...$(RESET)"
	@failure_count=$$(gh pr view $(PR) --json statusCheckRollup | jq '[.statusCheckRollup[] | select(.conclusion == "FAILURE" or .conclusion == "ERROR" or .conclusion == "CANCELLED" or .conclusion == "TIMED_OUT")] | length'); \
	if [ "$$failure_count" -gt 0 ]; then \
		echo "$(RED)Error: PR has failing checks. Cannot merge.$(RESET)"; \
		echo "$(YELLOW)Run 'make pr-status PR=$(PR)' to see details$(RESET)"; \
		exit 1; \
	fi
	@echo "$(GREEN)All checks passed. Merging PR #$(PR)...$(RESET)"
	@gh pr merge $(PR) --squash --delete-branch
	@git checkout main && git pull
	@echo "$(BOLD)$(GREEN)PR #$(PR) merged successfully!$(RESET)"

issue-close: ## Close issue (use: make issue-close ISSUE=123)
	@if [ -z "$(ISSUE)" ]; then \
		echo "$(RED)Error: ISSUE variable is required$(RESET)"; \
		echo "Usage: make issue-close ISSUE=123"; \
		exit 1; \
	fi
	@echo "$(BOLD)$(MAGENTA)Closing issue #$(ISSUE)...$(RESET)"
	@gh issue close $(ISSUE) --comment "✅ 実装完了しました。"
	@echo "$(GREEN)Issue #$(ISSUE) closed$(RESET)"
