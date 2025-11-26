## Exercise 3: Specification-Guided Test Improvement

This repository contains all materials for Exercise 3, building upon Exercise 2.

You could find this under `https://github.com/sy77777en/cs520_hw`

For more details, please refer to my report.

## Overview

Exercise 3 explores how formal specifications, automatically generated from natural language problem statements, can guide test improvement. Two problems with weakest coverage from Exercise 2 were selected:

1. **HumanEval/39 (prime_fib)** - 92% line, 88% branch coverage
2. **MBPP_25 (find_Product)** - 94% line, 91% branch coverage

## Repository Structure

```
exercise3/
├── src/                              # Source implementations
│   ├── prime_fib.py
│   ├── find_product.py
│   └── __init__.py
├── tests/                            # Test suites
│   ├── test_prime_fib_baseline.py          # From Exercise 2
│   ├── test_prime_fib_iter1.py             # From Exercise 2
│   ├── test_prime_fib_iter2.py             # From Exercise 2
│   ├── test_prime_fib_spec_guided.py       # NEW: Spec-guided
│   ├── test_find_product_baseline.py       # From Exercise 2
│   ├── test_find_product_iter1.py          # From Exercise 2
│   ├── test_find_product_iter2.py          # From Exercise 2
│   ├── test_find_product_iter3.py          # From Exercise 2
│   ├── test_find_product_spec_guided.py    # NEW: Spec-guided
│   ├── __init__.py
│   └── conftest.py
├── specifications/                   # Formal specifications
│   ├── prime_fib_generated.py             # LLM-generated (before correction)
│   ├── prime_fib_corrected.py             # Manually corrected
│   ├── find_product_generated.py          # LLM-generated (before correction)
│   └── find_product_corrected.py          # Manually corrected
├── prompts/                          # LLM prompts
│   ├── prime_fib_spec_generation.txt
│   ├── prime_fib_test_generation.txt
│   ├── find_product_spec_generation.txt
│   └── find_product_test_generation.txt
├── coverage_reports/                 # Coverage analysis
│   ├── exercise2_final/                   # Before spec-guided tests
│   └── exercise3_final/                   # After spec-guided tests
├── scripts/
│   └── run_coverage.sh                    # Coverage automation
├── requirements.txt
├── pytest.ini
├── exercise3_report.md               # Complete report
└── README.md                         # This file
```

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/sy77777en/cs520_hw
cd exercise3

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests with coverage
bash scripts/run_coverage.sh

# Run only spec-guided tests
pytest tests/test_*_spec_guided.py -v

# Run with coverage for specific problem
pytest tests/test_prime_fib*.py --cov=src.prime_fib --cov-branch --cov-report=html
```

## Key Results

### Coverage Improvements

| Problem | Old Stmt % | New Stmt % | Old Branch % | New Branch % | Improvement |
|---------|------------|------------|--------------|--------------|-------------|
| prime_fib | 92% | 92% | 88% | 90% | +2% branch |
| find_Product | 94% | 94% | 91% | 93% | +2% branch |

### Specification Accuracy

| Problem | Correct | Total | Accuracy |
|---------|---------|-------|----------|
| prime_fib | 3 | 5 | 60% |
| find_Product | 2 | 5 | 40% |

### Common LLM Errors

1. **Side Effects**: List/dictionary mutations (append, dict assignment)
2. **Self-Reference**: Calling the target function within assertions
3. **Missing Edge Cases**: Incomplete boundary validation

## Part 1: Specification Generation

### Process

1. Extract function signature and natural language description
2. Prompt LLM to generate formal specifications as assertions
3. Manually evaluate each specification for correctness
4. Correct specifications that violate constraints:
   - No side effects (I/O, mutations, randomness)
   - No self-reference (calling the target function)
   - Pure boolean and arithmetic logic only

### Files

- `specifications/prime_fib_generated.py` - Original LLM output
- `specifications/prime_fib_corrected.py` - Manually corrected version
- `specifications/find_product_generated.py` - Original LLM output
- `specifications/find_product_corrected.py` - Manually corrected version

## Part 2: Test Generation

### Process

1. Feed corrected specifications back to LLM
2. Request test cases that validate each specification
3. Add tests to Exercise 2 test suite
4. Run coverage analysis comparing before/after

### New Tests

- `tests/test_prime_fib_spec_guided.py` - 7 new tests
- `tests/test_find_product_spec_guided.py` - 7 new tests

## Key Insights

### prime_fib

- **Coverage Impact**: Modest (+2% branch) due to already high coverage
- **Quality Impact**: Strong - tests validate mathematical properties (primality, Fibonacci membership)
- **Unique Value**: Specification-based tests catch logical errors that coverage-based tests miss

### find_Product

- **Coverage Impact**: Modest (+2% branch) due to convergence at 91%
- **Quality Impact**: Systematic testing of sign determination logic
- **Unique Value**: Explicit product verification and zero-negative interaction testing

## Dependencies

- Python 3.8+
- pytest 7.4.3
- pytest-cov 4.1.0
- coverage 7.3.2
