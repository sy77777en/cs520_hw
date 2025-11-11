#!/bin/bash
# Script to run coverage analysis for all test iterations
# Usage: bash scripts/run_coverage.sh

set -e  # Exit on error

echo "========================================="
echo "Exercise 2: Coverage Analysis Runner"
echo "========================================="
echo ""

# Navigate to exercise2 directory
cd "$(dirname "$0")/.."

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "❌ pytest not found. Installing dependencies..."
    pip install -r requirements.txt
fi

# Create coverage reports directory if it doesn't exist
mkdir -p coverage_reports/{baseline,iteration_1,iteration_2,iteration_3,final}

echo "📊 Running Baseline Tests..."
echo "-------------------------------------------"
pytest tests/test_*_baseline.py \
    --cov=src \
    --cov-branch \
    --cov-report=html:coverage_reports/baseline/htmlcov \
    --cov-report=term \
    --cov-report=xml:coverage_reports/baseline/coverage.xml
echo ""

echo "📊 Running Iteration 1 Tests..."
echo "-------------------------------------------"
pytest tests/test_*_baseline.py tests/test_*_iter1.py \
    --cov=src \
    --cov-branch \
    --cov-report=html:coverage_reports/iteration_1/htmlcov \
    --cov-report=term \
    --cov-report=xml:coverage_reports/iteration_1/coverage.xml
echo ""

echo "📊 Running Iteration 2 Tests..."
echo "-------------------------------------------"
pytest tests/test_*_baseline.py tests/test_*_iter1.py tests/test_*_iter2.py \
    --cov=src \
    --cov-branch \
    --cov-report=html:coverage_reports/iteration_2/htmlcov \
    --cov-report=term \
    --cov-report=xml:coverage_reports/iteration_2/coverage.xml
echo ""

echo "📊 Running Iteration 3 Tests (find_product only)..."
echo "-------------------------------------------"
pytest tests/test_find_product_*.py \
    --cov=src.find_product \
    --cov-branch \
    --cov-report=html:coverage_reports/iteration_3/htmlcov \
    --cov-report=term \
    --cov-report=xml:coverage_reports/iteration_3/coverage.xml
echo ""

echo "📊 Running All Tests (Final)..."
echo "-------------------------------------------"
pytest tests/ \
    --cov=src \
    --cov-branch \
    --cov-report=html:coverage_reports/final/htmlcov \
    --cov-report=term \
    --cov-report=xml:coverage_reports/final/coverage.xml
echo ""

echo "========================================="
echo "✅ Coverage Analysis Complete!"
echo "========================================="
echo ""
echo "📁 View HTML reports:"
echo "   - Baseline:    coverage_reports/baseline/htmlcov/index.html"
echo "   - Iteration 1: coverage_reports/iteration_1/htmlcov/index.html"
echo "   - Iteration 2: coverage_reports/iteration_2/htmlcov/index.html"
echo "   - Iteration 3: coverage_reports/iteration_3/htmlcov/index.html"
echo "   - Final:       coverage_reports/final/htmlcov/index.html"
echo ""
echo "💡 Tip: Open with 'open coverage_reports/final/htmlcov/index.html' (macOS)"
echo "        or 'xdg-open coverage_reports/final/htmlcov/index.html' (Linux)"
echo ""
