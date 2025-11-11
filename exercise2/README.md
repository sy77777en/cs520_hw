# Exercise 2: Automated Testing & Coverage

This directory contains all materials for Exercise 2.

## Structure

- `src/` - Corrected implementations + original failing code
- `tests/` - Baseline tests + 3 iterations of LLM-generated tests
- `bugs/` - Seeded bugs for fault detection analysis
- `prompts/` - LLM prompts used for test generation
- `coverage_reports/` - HTML/XML coverage reports
- `scripts/` - Automation scripts for running tests

## Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests with coverage
bash scripts/run_coverage.sh

# View coverage report
open coverage_reports/final/htmlcov/index.html
```

## Problems Analyzed

### MBPP_25 (find_Product)
- **Exercise 1 Result:** FAILED (wrong function name)
- **Baseline Coverage:** 85% line, 68% branch
- **Final Coverage:** 94% line, 91% branch
- **Iterations:** 3

### HumanEval/39 (prime_fib)
- **Exercise 1 Result:** FAILED (variable swap bug)
- **Baseline Coverage:** 75% line, 62% branch
- **Final Coverage:** 92% line, 88% branch
- **Iterations:** 2

## Key Results

- Improved branch coverage by average of 24.5%
- Bug detection rate increased from 11.5% to 22.2% (MBPP_25)
- Fault localization time reduced from 15min to 1min (HumanEval/39)

## Report

See `report.pdf` for complete analysis.