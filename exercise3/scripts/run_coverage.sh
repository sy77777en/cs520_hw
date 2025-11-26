#!/bin/bash
# Script to run coverage analysis for Exercise 3
# Compares Exercise 2 baseline with spec-guided tests
# Usage: bash scripts/run_coverage.sh

set -e  # Exit on error

echo "========================================="
echo "Exercise 3: Specification-Guided Coverage"
echo "========================================="
echo ""

# Navigate to exercise3 directory (adjust if needed)
cd "$(dirname "$0")/.."

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "❌ pytest not found. Installing dependencies..."
    pip install -r requirements.txt
fi

# Create coverage reports directory if it doesn't exist
mkdir -p coverage_reports/{exercise2_final,exercise3_final}

echo "📊 Step 1: Running Exercise 2 Tests (Baseline + Iterations)"
echo "-----------------------------------------------------------"
pytest tests/test_prime_fib_baseline.py tests/test_prime_fib_iter*.py \
       tests/test_find_product_baseline.py tests/test_find_product_iter*.py \
    --cov=src \
    --cov-branch \
    --cov-report=html:coverage_reports/exercise2_final/htmlcov \
    --cov-report=term \
    --cov-report=xml:coverage_reports/exercise2_final/coverage.xml
echo ""

echo "📊 Step 2: Running All Tests (Exercise 2 + Spec-Guided)"
echo "--------------------------------------------------------"
pytest tests/ \
    --cov=src \
    --cov-branch \
    --cov-report=html:coverage_reports/exercise3_final/htmlcov \
    --cov-report=term \
    --cov-report=xml:coverage_reports/exercise3_final/coverage.xml
echo ""

echo "📊 Step 3: Running Only Spec-Guided Tests"
echo "-----------------------------------------"
pytest tests/test_*_spec_guided.py -v
echo ""

echo "========================================="
echo "✅ Coverage Analysis Complete!"
echo "========================================="
echo ""
echo "📁 View HTML reports:"
echo "   - Exercise 2 (before): coverage_reports/exercise2_final/htmlcov/index.html"
echo "   - Exercise 3 (after):  coverage_reports/exercise3_final/htmlcov/index.html"
echo ""
echo "📊 Summary of spec-guided tests:"
pytest tests/test_*_spec_guided.py --collect-only -q | head -20
echo ""
echo "💡 Tip: Open with 'open coverage_reports/exercise3_final/htmlcov/index.html' (macOS)"
echo "        or 'xdg-open coverage_reports/exercise3_final/htmlcov/index.html' (Linux)"
echo ""
