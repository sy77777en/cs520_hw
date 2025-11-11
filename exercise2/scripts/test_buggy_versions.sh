#!/bin/bash
# Script to test bug detection rates
# Compares baseline vs improved test suites against seeded bugs
# Usage: bash scripts/test_buggy_versions.sh

set -e  # Exit on error

echo "========================================="
echo "Exercise 2: Bug Detection Rate Tester"
echo "========================================="
echo ""

# Navigate to exercise2 directory
cd "$(dirname "$0")/.."

# Create results directory
mkdir -p results

echo "🐛 Testing Bug Detection for find_Product"
echo "-------------------------------------------"

# Backup correct version
echo "Backing up correct implementation..."
cp src/find_product.py src/find_product_correct_backup.py

echo ""
echo "Test 1: Baseline suite vs buggy find_product"
echo "----------------------------------------------"
cp bugs/find_product_bug.py src/find_product.py
pytest tests/test_find_product_baseline.py -v --tb=short > results/find_product_baseline_detection.txt 2>&1 || true

baseline_failed=$(grep -c "FAILED" results/find_product_baseline_detection.txt || echo "0")
baseline_passed=$(grep -c "PASSED" results/find_product_baseline_detection.txt || echo "0")
echo "Baseline: $baseline_failed failed, $baseline_passed passed"

echo ""
echo "Test 2: Improved suite vs buggy find_product"
echo "----------------------------------------------"
pytest tests/test_find_product_*.py -v --tb=short > results/find_product_improved_detection.txt 2>&1 || true

improved_failed=$(grep -c "FAILED" results/find_product_improved_detection.txt || echo "0")
improved_passed=$(grep -c "PASSED" results/find_product_improved_detection.txt || echo "0")
echo "Improved: $improved_failed failed, $improved_passed passed"

# Restore correct version
echo ""
echo "Restoring correct implementation..."
mv src/find_product_correct_backup.py src/find_product.py

echo ""
echo "🐛 Testing Bug Detection for prime_fib"
echo "-------------------------------------------"

# Backup correct version
echo "Backing up correct implementation..."
cp src/prime_fib.py src/prime_fib_correct_backup.py

echo ""
echo "Test 3: Baseline suite vs buggy prime_fib"
echo "----------------------------------------------"
cp bugs/prime_fib_bug.py src/prime_fib.py
pytest tests/test_prime_fib_baseline.py -v --tb=short > results/prime_fib_baseline_detection.txt 2>&1 || true

pf_baseline_failed=$(grep -c "FAILED" results/prime_fib_baseline_detection.txt || echo "0")
pf_baseline_passed=$(grep -c "PASSED" results/prime_fib_baseline_detection.txt || echo "0")
echo "Baseline: $pf_baseline_failed failed, $pf_baseline_passed passed"

echo ""
echo "Test 4: Improved suite vs buggy prime_fib"
echo "----------------------------------------------"
pytest tests/test_prime_fib_*.py -v --tb=short > results/prime_fib_improved_detection.txt 2>&1 || true

pf_improved_failed=$(grep -c "FAILED" results/prime_fib_improved_detection.txt || echo "0")
pf_improved_passed=$(grep -c "PASSED" results/prime_fib_improved_detection.txt || echo "0")
echo "Improved: $pf_improved_failed failed, $pf_improved_passed passed"

# Restore correct version
echo ""
echo "Restoring correct implementation..."
mv src/prime_fib_correct_backup.py src/prime_fib.py

echo ""
echo "========================================="
echo "✅ Bug Detection Testing Complete!"
echo "========================================="
echo ""
echo "📊 Summary:"
echo "   find_Product:"
echo "      Baseline:  $baseline_failed/$((baseline_failed + baseline_passed)) tests caught bug"
echo "      Improved:  $improved_failed/$((improved_failed + improved_passed)) tests caught bug"
echo ""
echo "   prime_fib:"
echo "      Baseline:  $pf_baseline_failed/$((pf_baseline_failed + pf_baseline_passed)) tests caught bug"
echo "      Improved:  $pf_improved_failed/$((pf_improved_failed + pf_improved_passed)) tests caught bug"
echo ""
echo "📁 Detailed results saved in results/ directory"
echo ""
