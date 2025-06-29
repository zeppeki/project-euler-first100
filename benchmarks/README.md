# Benchmark Results

This directory contains comprehensive performance analysis results for Project Euler solutions.

## Directory Structure

```
benchmarks/
├── individual/          # Individual problem benchmark results
│   ├── problem_001.json
│   ├── problem_002.json
│   └── ...
├── aggregated/          # Combined benchmark results
│   ├── latest.json      # Most recent complete benchmark run
│   ├── historical/      # Historical benchmark results
│   └── trends.json      # Performance trend analysis
├── reports/             # Generated benchmark reports
│   ├── performance_summary.html
│   ├── regression_analysis.json
│   └── visualization/   # Charts and graphs
└── README.md           # This file
```

## Benchmark Data Format

### Individual Problem Results (`individual/problem_XXX.json`)

```json
{
  "problem_number": "001",
  "problem_title": "Multiples of 3 and 5",
  "timestamp": "2025-06-29T...",
  "config": {
    "runs": 5,
    "warmup_runs": 2,
    "min_time": 0.001,
    "max_time": 10.0
  },
  "input_parameters": {
    "limit": 1000
  },
  "solutions": [
    {
      "name": "素直な解法",
      "function_name": "solve_naive",
      "algorithm_type": "naive",
      "result": 233168,
      "execution_times": [0.0001, 0.0001, ...],
      "mean_time": 0.0001,
      "median_time": 0.0001,
      "std_deviation": 0.00001,
      "min_time": 0.00009,
      "max_time": 0.00011,
      "relative_speed": 10.5,
      "complexity_class": "O(n)"
    },
    {
      "name": "最適化解法",
      "function_name": "solve_optimized",
      "algorithm_type": "optimized",
      "result": 233168,
      "execution_times": [0.00001, ...],
      "mean_time": 0.00001,
      "median_time": 0.00001,
      "std_deviation": 0.000001,
      "min_time": 0.000009,
      "max_time": 0.000011,
      "relative_speed": 1.0,
      "complexity_class": "O(1)"
    }
  ],
  "fastest_solution": "最適化解法",
  "verified": true,
  "total_benchmark_time": 0.1
}
```

### Aggregated Results (`aggregated/latest.json`)

```json
{
  "benchmark_suite_version": "1.0",
  "timestamp": "2025-06-29T...",
  "config": { /* benchmark configuration */ },
  "problems": [ /* array of individual problem results */ ],
  "summary": {
    "total_problems": 37,
    "verified_problems": 37,
    "verification_rate": 1.0,
    "total_solutions": 111,
    "algorithm_distribution": {
      "naive": 37,
      "optimized": 37,
      "mathematical": 37
    },
    "performance_stats": {
      "mean_execution_time": 0.001,
      "median_execution_time": 0.0005,
      "fastest_execution_time": 0.00001,
      "slowest_execution_time": 0.1
    }
  }
}
```

## Using Benchmark Results

### Command Line Tools

```bash
# Run benchmarks for all problems
make benchmark

# Run benchmark for specific problem
make benchmark-problem PROBLEM=001

# Generate performance reports
make benchmark-report

# Compare with historical results
make benchmark-compare
```

### Programmatic Access

```python
from pathlib import Path
from problems.utils.benchmark import BenchmarkSuite

# Load latest results
suite = BenchmarkSuite()
suite.load_results(Path("benchmarks/aggregated/latest.json"))

# Access benchmark data
for problem in suite.results:
    print(f"Problem {problem['problem_number']}: {problem['fastest_solution']}")
```

## Performance Analysis

### Key Metrics

- **Execution Time**: Wall clock time for algorithm execution
- **Relative Speed**: Performance relative to fastest solution for same problem
- **Algorithm Type Distribution**: Breakdown of naive/optimized/mathematical approaches
- **Verification Rate**: Percentage of problems where all solutions agree
- **Complexity Classes**: Big O notation for time complexity

### Regression Detection

Benchmark results are automatically compared with historical data to detect:
- Performance regressions (>20% slowdown)
- Improvements (>20% speedup)
- Algorithm complexity changes
- Solution correctness issues

## Automation

### CI/CD Integration

Benchmarks are automatically run:
- On every commit to main branch
- Before merging pull requests
- Nightly for complete performance analysis
- When benchmark configuration changes

### Reports

Automated generation of:
- HTML performance dashboards
- Trend analysis charts
- Regression detection alerts
- Performance comparison tables
