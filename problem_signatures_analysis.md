# Function Signatures Analysis for Problems 044-090

Based on analysis of the function signatures in problems 044-090, here's the complete mapping of required arguments for each problem:

## Problems with No Arguments (Default Project Euler problem statement)

These problems solve the specific Project Euler question with no additional parameters:

- **044**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **045**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **049**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **054**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **059**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **061**: `solve_naive()`, `solve_optimized()` - No arguments (no mathematical)
- **062**: `solve_naive()`, `solve_optimized()` - No arguments (no mathematical)
- **063**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **064**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **065**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **066**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **068**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **079**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments
- **090**: `solve_naive()`, `solve_optimized()`, `solve_mathematical()` - No arguments

## Problems with Single Integer Parameter

### limit: int
- **046**: `solve_naive(limit: int = 10000)`, `solve_optimized(limit: int = 10000)`, `solve_mathematical(limit: int = 10000)`
- **048**: `solve_naive(limit: int = 1000)`, `solve_optimized(limit: int = 1000)`, `solve_mathematical(limit: int = 1000)`
- **050**: `solve_naive(limit: int = 1000000)`, `solve_optimized(limit: int = 1000000)`, `solve_mathematical(limit: int = 1000000)`
- **055**: `solve_naive(limit: int = 10000)`, `solve_optimized(limit: int = 10000)` - No mathematical
- **057**: `solve_naive(limit: int = 1000)`, `solve_optimized(limit: int = 1000)` - No mathematical
- **069**: `solve_naive(limit: int)`, `solve_optimized(limit: int)`, `solve_mathematical(limit: int)` - **NO DEFAULT**
- **070**: `solve_naive(limit: int)`, `solve_optimized(limit: int)`, `solve_mathematical(limit: int)` - **NO DEFAULT**
- **071**: `solve_naive(limit: int)`, `solve_optimized(limit: int)`, `solve_mathematical(limit: int)` - **NO DEFAULT**
- **072**: `solve_naive(limit: int)`, `solve_optimized(limit: int)`, `solve_mathematical(limit: int)` - **NO DEFAULT**
- **073**: `solve_naive(limit: int)`, `solve_optimized(limit: int)`, `solve_mathematical(limit: int)` - **NO DEFAULT**
- **074**: `solve_naive(limit: int)`, `solve_optimized(limit: int)` - **NO DEFAULT**, No mathematical
- **075**: `solve_naive(limit: int)`, `solve_optimized(limit: int)` - **NO DEFAULT**, No mathematical

### Other single integer parameters with NO DEFAULTS:
- **047**: `solve_naive(target_factors: int)`, `solve_optimized(target_factors: int)`, `solve_mathematical(target_factors: int)`
- **051**: `solve_naive(target_family_size: int)`, `solve_optimized(target_family_size: int)`, `solve_mathematical(target_family_size: int)`
- **076**: `solve_naive(n: int)`, `solve_optimized(n: int)` - No mathematical
- **077**: `solve_naive(target: int)`, `solve_optimized(target: int)` - No mathematical
- **078**: `solve_naive(target_divisor: int)`, `solve_optimized(target_divisor: int)` - No mathematical

### Single integer parameters WITH DEFAULTS:
- **085**: `solve_naive(target: int = 2000000)`, `solve_optimized(target: int = 2000000)` - No mathematical
- **086**: `solve_naive(target: int = 1000000)`, `solve_optimized(target: int = 1000000)` - No mathematical
- **087**: `solve_naive(limit: int = 50000000)`, `solve_optimized(limit: int = 50000000)`, `solve_mathematical(limit: int = 50000000)`
- **088**: `solve_naive(max_k: int = 12000)`, `solve_optimized(max_k: int = 12000)`, `solve_mathematical(max_k: int = 12000)`

## Problems with Multiple Parameters

### Two integer parameters:
- **052**: `solve_naive(max_multiple: int = 6)`, `solve_optimized(max_multiple: int = 6)`, `solve_mathematical(max_multiple: int = 6)`
- **053**: `solve_naive(max_n: int = 100, threshold: int = 1000000)`, `solve_optimized(max_n: int = 100, threshold: int = 1000000)`, `solve_mathematical(max_n: int = 100, threshold: int = 1000000)`
- **056**: `solve_naive(limit_a: int = 100, limit_b: int = 100)`, `solve_optimized(limit_a: int = 100, limit_b: int = 100)` - No mathematical
- **080**: `solve_naive(limit: int = 100, precision: int = 100)`, `solve_optimized(limit: int = 100, precision: int = 100)` - No mathematical

### Integer and float parameters:
- **058**: `solve_naive(target_ratio: float = 0.1)`, `solve_optimized(target_ratio: float = 0.1)` - No mathematical
- **060**: `solve_naive(set_size: int = 5, prime_limit: int = 10000)`, `solve_optimized(set_size: int = 5, prime_limit: int = 10000)`, `solve_mathematical(set_size: int = 5, prime_limit: int = 10000)`

### Special case with simulation parameter:
- **084**: `solve_naive(dice_sides: int = 4, num_simulations: int = 1000000)`, `solve_optimized(dice_sides: int = 4)` - No mathematical

## Problems with Matrix/Data File Parameters

### Matrix parameter:
- **067**: `solve_naive(triangle: list[list[int]])`, `solve_optimized(triangle: list[list[int]])`, `solve_mathematical(triangle: list[list[int]])` - **NO DEFAULT**
- **081**: `solve_naive(matrix: list[list[int]])`, `solve_optimized(matrix: list[list[int]])` - **NO DEFAULT**, No mathematical
- **082**: `solve_naive(matrix: list[list[int]])`, `solve_optimized(matrix: list[list[int]])` - **NO DEFAULT**, No mathematical
- **083**: `solve_naive(matrix: list[list[int]])`, `solve_optimized(matrix: list[list[int]])` - **NO DEFAULT**, No mathematical

### Filename parameter:
- **089**: `solve_naive(filename: str = "data/p089_roman.txt")`, `solve_optimized(filename: str = "data/p089_roman.txt")`, `solve_mathematical(filename: str = "data/p089_roman.txt")`

## Summary by Argument Requirements

### No arguments needed (15 problems):
044, 045, 049, 054, 059, 061, 062, 063, 064, 065, 066, 068, 079, 090

### Single required integer (11 problems - need benchmark values):
047, 051, 069, 070, 071, 072, 073, 074, 075, 076, 077, 078

### Single integer with defaults (7 problems):
046, 048, 050, 055, 057, 085, 086, 087, 088

### Multiple parameters with defaults (7 problems):
052, 053, 056, 058, 060, 080, 084

### Matrix/data parameters (5 problems - need special handling):
067, 081, 082, 083, 089

### Special cases needing investigation:
- Problems 081, 082, 083: Need to check how they load their default matrices
- Problem 067: Need to check how it loads the default triangle
- Problem 089: Has default filename but needs data file verification

## Root Cause of Benchmark Failure

The benchmark tool failure is caused by the `get_problem_arguments()` function in `/home/zepp/cursor/project-euler-first100/problems/utils/simple_runner.py`. This function contains a hardcoded dictionary `problem_args` that only includes mappings up to problem "043". For any problem not in the dictionary (lines 151-195), it returns `((), {})` (line 197), meaning no arguments are passed to the solve functions.

This causes the benchmark to fail for problems 044-090 that require arguments.

## Required Fix: Missing Argument Mappings

The `problem_args` dictionary in `simple_runner.py` needs to be extended with the following entries:

```python
# Add to the problem_args dictionary in simple_runner.py:
"044": ((), {}),                           # No arguments needed
"045": ((), {}),                           # No arguments needed
"046": ((10000,), {}),                     # limit: int = 10000
"047": ((4,), {}),                         # target_factors: int (original problem)
"048": ((1000,), {}),                      # limit: int = 1000
"049": ((), {}),                           # No arguments needed
"050": ((1000000,), {}),                   # limit: int = 1000000
"051": ((8,), {}),                         # target_family_size: int (original problem)
"052": ((6,), {}),                         # max_multiple: int = 6
"053": ((100, 1000000), {}),               # max_n: int = 100, threshold: int = 1000000
"054": ((), {}),                           # No arguments needed
"055": ((10000,), {}),                     # limit: int = 10000
"056": ((100, 100), {}),                   # limit_a: int = 100, limit_b: int = 100
"057": ((1000,), {}),                      # limit: int = 1000
"058": ((0.1,), {}),                       # target_ratio: float = 0.1
"059": ((), {}),                           # No arguments needed
"060": ((5, 10000), {}),                   # set_size: int = 5, prime_limit: int = 10000
"061": ((), {}),                           # No arguments needed
"062": ((), {}),                           # No arguments needed
"063": ((), {}),                           # No arguments needed
"064": ((), {}),                           # No arguments needed
"065": ((), {}),                           # No arguments needed
"066": ((), {}),                           # No arguments needed
"067": # SPECIAL HANDLING NEEDED - matrix parameter
"068": ((), {}),                           # No arguments needed
"069": ((1000000,), {}),                   # limit: int (original problem)
"070": ((10000000,), {}),                  # limit: int (original problem)
"071": ((1000000,), {}),                   # limit: int (original problem)
"072": ((1000000,), {}),                   # limit: int (original problem)
"073": ((12000,), {}),                     # limit: int (original problem)
"074": ((1000000,), {}),                   # limit: int (original problem)
"075": ((1500000,), {}),                   # limit: int (original problem)
"076": ((100,), {}),                       # n: int (original problem)
"077": ((5000,), {}),                      # target: int (original problem)
"078": ((1000000,), {}),                   # target_divisor: int (original problem)
"079": ((), {}),                           # No arguments needed
"080": ((100, 100), {}),                   # limit: int = 100, precision: int = 100
"081": # SPECIAL HANDLING NEEDED - matrix parameter
"082": # SPECIAL HANDLING NEEDED - matrix parameter
"083": # SPECIAL HANDLING NEEDED - matrix parameter
"084": ((4, 1000000), {}),                 # dice_sides: int = 4, num_simulations: int = 1000000
"085": ((2000000,), {}),                   # target: int = 2000000
"086": ((1000000,), {}),                   # target: int = 1000000
"087": ((50000000,), {}),                  # limit: int = 50000000
"088": ((12000,), {}),                     # max_k: int = 12000
"089": (("data/p089_roman.txt",), {}),     # filename: str = "data/p089_roman.txt"
"090": ((), {}),                           # No arguments needed
```

## Special Cases Requiring Matrix/Data Loading

Several problems need special handling similar to the existing logic for problems 011, 018, and 022:

### Problem 067 (Triangle data):
```python
if problem_number == "067":
    try:
        problem_module = importlib.import_module(f"problems.problem_{problem_number.zfill(3)}")
        triangle_func = problem_module.get_problem_triangle
        triangle_data = triangle_func()
        return ((triangle_data,), {})
    except (ImportError, AttributeError):
        return ((), {})
```

### Problems 081, 082, 083 (Matrix data):
```python
if problem_number in ["081", "082", "083"]:
    try:
        problem_module = importlib.import_module(f"problems.problem_{problem_number.zfill(3)}")
        matrix_func = problem_module.load_matrix
        if problem_number == "081":
            matrix_data = matrix_func()  # Uses default filename
        else:
            matrix_data = matrix_func(f"data/p{problem_number}_matrix.txt")
        return ((matrix_data,), {})
    except (ImportError, AttributeError):
        return ((), {})
```

## Summary by Category

### Immediate fixes needed (35 problems):
044, 045, 046, 047, 048, 049, 050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 060, 061, 062, 063, 064, 065, 066, 068, 069, 070, 071, 072, 073, 074, 075, 076, 077, 078, 079, 080, 084, 085, 086, 087, 088, 089, 090

### Special handling needed (4 problems):
067, 081, 082, 083

### Problems that will work after the fix (39 problems):
All problems from 044-090 except for the 4 special cases
