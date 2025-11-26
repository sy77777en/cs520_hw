## Exercise 3: Specification-Guided Test Improvement

**Siyuan Cen** *siyuanc4@andrew.cmu.edu*
**Date:** November 25, 2024
**Github Repo: ** https://github.com/sy77777en/cs520_hw

------

## Problems Selected

Based on Exercise 2 results, I selected the two problems with weakest coverage:

1. **HumanEval/39 (prime_fib)** - 92% line, 88% branch coverage
2. **MBPP_25 (find_Product)** - 94% line, 91% branch coverage

------

### Deliverables Summary

#### GitHub Repository Structure

```
exercise3/
├── src/
│   ├── find_product.py          # Original implementation
│   ├── prime_fib.py              # Original implementation
│   └── __init__.py
├── tests/
│   ├── test_prime_fib_baseline.py       
│   ├── test_prime_fib_iter1.py          
│   ├── test_prime_fib_iter2.py          
│   ├── test_prime_fib_spec_guided.py    # NEW: Spec-guided tests
│   ├── test_find_product_baseline.py    
│   ├── test_find_product_iter1.py       
│   ├── test_find_product_iter2.py       
│   ├── test_find_product_iter3.py       
│   ├── test_find_product_spec_guided.py # NEW: Spec-guided tests
│   ├── __init__.py
│   └── conftest.py
├── specifications/
│   ├── prime_fib_generated.py    # Original LLM-generated specs
│   ├── prime_fib_corrected.py    # Manually corrected specs
│   ├── find_product_generated.py # Original LLM-generated specs
│   └── find_product_corrected.py # Manually corrected specs
├── prompts/
│   ├── prime_fib_spec_generation.txt
│   ├── prime_fib_test_generation.txt
│   ├── find_product_spec_generation.txt
│   └── find_product_test_generation.txt
├── requirements.txt
├── pytest.ini
└── README.md
```

#### Files Included

1. **Source Code**: Original implementations from Exercise 2
2. **Test Files**: Baseline + iterative + spec-guided tests
3. **Specifications**: Generated and corrected assertion files
4. **Coverage Reports**: HTML reports showing before/after coverage
5. **Prompts**: All LLM prompts used for generation
6. **Scripts**: Automation for running tests and generating coverage

------

## Part 1: Generate, Evaluate, and Refine Specifications

### Problem 1: prime_fib (HumanEval/39)

#### Function Signature

```python
def prime_fib(n: int) -> int
```

#### Natural Language Description

Return the n-th number that is both a Fibonacci number and prime. The Fibonacci sequence is defined as `F(0)=0, F(1)=1, and F(n)=F(n-1)+F(n-2) for n>1`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

#### LLM Prompt

```
Problem description: Return the n-th number that is both a Fibonacci number and prime. The Fibonacci sequence is defined as F(0)=0, F(1)=1, and F(n)=F(n-1)+F(n-2) for n>1. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Method signature: def prime_fib(n: int) -> int

Please write formal specifications as Python assertions that describe the correct behavior of this method. Let 'res' denote the expected return value of 'prime_fib(n)'. Do not call 'prime_fib()' in your assertions. Do not use methods with side effects such as print, file I/O, random number generation, or timing functions. Express the relationship between 'n' and 'res' using pure arithmetic and boolean logic only.

Generate about 5 specifications as assertions.
```

#### Generated Assertions (Before Correction)

```python
# Specification 1: Result must be greater than 1 (all primes are > 1)
assert res > 1

# Specification 2: Result must be prime (no divisors between 2 and sqrt(res))
assert all(res % k != 0 for k in range(2, int(res**0.5) + 1))

# Specification 3: Result must be in Fibonacci sequence
fib_seq = [0, 1]
while fib_seq[-1] < res:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
assert res in fib_seq

# Specification 4: For n >= 1, result must be at least 2
assert (n < 1) or (res >= 2)

# Specification 5: Result must increase with n
# (The n-th prime Fibonacci must be >= (n-1)-th prime Fibonacci)
assert n == 1 or res > prev_res  # where prev_res = prime_fib(n-1)
```

#### Evaluation

| Assertion | Status      | Explanation                                                  |
| --------- | ----------- | ------------------------------------------------------------ |
| Spec 1    | ✓ Correct   | Valid constraint - all prime Fibonacci numbers are > 1       |
| Spec 2    | ✓ Correct   | Valid primality check using pure logic                       |
| Spec 3    | ✗ Incorrect | Uses list mutation (append) which is a side effect           |
| Spec 4    | ✓ Correct   | Valid boundary condition                                     |
| Spec 5    | ✗ Incorrect | References prev_res which requires calling the function (self-reference) |

**Accuracy Rate: 3/5 = 60%**

#### Corrected Assertions

```python
# Specification 1: Result must be greater than 1 (all primes are > 1)
assert res > 1

# Specification 2: Result must be prime (no divisors between 2 and sqrt(res))
assert all(res % k != 0 for k in range(2, int(res**0.5) + 1))

# Specification 3 (CORRECTED): Result must be in Fibonacci sequence
# Use mathematical property: a number is Fibonacci if one of 5*n^2+4 or 5*n^2-4 is perfect square
def is_perfect_square(x):
    if x < 0:
        return False
    root = int(x**0.5)
    return root * root == x

assert is_perfect_square(5 * res * res + 4) or is_perfect_square(5 * res * res - 4)

# Specification 4: For n >= 1, result must be at least 2
assert (n < 1) or (res >= 2)

# Specification 5 (CORRECTED): Results must be strictly increasing sequence
# Use known property: store pre-computed prime Fibonacci numbers
known_prime_fibs = (2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437)
if 1 <= n <= len(known_prime_fibs):
    assert res == known_prime_fibs[n-1]
```

------

### Problem 2: find_Product (MBPP_25)

#### Function Signature

```python
def find_Product(arr, n) -> int
```

#### Natural Language Description

Write a function to find the product of the unique elements in a given list. The function takes in a list and the length of the list, and should return the product of all elements that appear exactly once in the list. If there are no unique elements, return 1.

#### LLM Prompt

```
Problem description: Write a function to find the product of the unique elements in a given list. The function takes in a list and the length of the list, and should return the product of all elements that appear exactly once in the list. If there are no unique elements, return 1.

Method signature: def find_Product(arr, n) -> int

Please write formal specifications as Python assertions that describe the correct behavior of this method. Let 'res' denote the expected return value of 'find_Product(arr, n)'. Do not call 'find_Product()' in your assertions. Do not use methods with side effects such as print, file I/O, random number generation, or timing functions. Express the relationship between 'arr', 'n', and 'res' using pure arithmetic and boolean logic only.

Generate about 5 specifications as assertions.
```

#### Generated Assertions (Before Correction)

```python
# Specification 1: If all elements appear more than once, result is 1
counts = {}
for elem in arr:
    counts[elem] = counts.get(elem, 0) + 1
unique_elements = [elem for elem, count in counts.items() if count == 1]
assert (len(unique_elements) == 0 and res == 1) or (len(unique_elements) > 0)

# Specification 2: Result is product of elements that appear exactly once
from functools import reduce
from operator import mul
expected_product = reduce(mul, unique_elements, 1) if unique_elements else 1
assert res == expected_product

# Specification 3: If array is empty, result is 1
assert (len(arr) > 0) or (res == 1)

# Specification 4: If array contains zero and zero appears once, result is 0
assert (0 not in arr) or (arr.count(0) != 1) or (res == 0)

# Specification 5: Result is positive if all unique elements are positive or even number of negatives
unique_negatives = sum(1 for elem in unique_elements if elem < 0)
assert (len(unique_elements) == 0) or (unique_negatives % 2 == 0 and res > 0) or (unique_negatives % 2 == 1 and res < 0) or (0 in unique_elements and res == 0)
```

#### Evaluation

| Assertion | Status | Explanation                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| Spec 1    | ✗      | Uses dictionary mutation (counts[elem] = ...) which is a side effect |
| Spec 2    | ✗      | Depends on unique_elements from Spec 1, also uses reduce     |
| Spec 3    | ✓      | Valid empty array check                                      |
| Spec 4    | ✓      | Valid zero handling logic                                    |
| Spec 5    | ✗      | Depends on unique_elements from Spec 1                       |

**Accuracy Rate: 2/5 = 40%**

#### Corrected Assertions

```python
# Specification 1 (CORRECTED): If all elements appear more than once, result is 1
# Use tuple comprehension and count() to avoid mutation
unique_count = sum(1 for elem in set(arr) if arr.count(elem) == 1)
assert (unique_count == 0 and res == 1) or (unique_count > 0)

# Specification 2 (CORRECTED): Result is product of elements that appear exactly once
unique_elems = tuple(elem for elem in set(arr) if arr.count(elem) == 1)
if len(unique_elems) == 0:
    assert res == 1
else:
    product = 1
    for elem in unique_elems:
        product *= elem
    assert res == product

# Specification 3: If array is empty, result is 1
assert (len(arr) > 0) or (res == 1)

# Specification 4: If array contains zero and zero appears once, result is 0
assert (0 not in arr) or (arr.count(0) != 1) or (res == 0)

# Specification 5 (CORRECTED): Result sign depends on count of negative unique elements
unique_elems = tuple(elem for elem in set(arr) if arr.count(elem) == 1)
if len(unique_elems) > 0 and 0 not in unique_elems:
    neg_count = sum(1 for elem in unique_elems if elem < 0)
    if neg_count % 2 == 0:
        assert res > 0
    else:
        assert res < 0
elif 0 in unique_elems and arr.count(0) == 1:
    assert res == 0
```

------

## Part 2: Use Specifications to Guide Test Improvement

### Problem 1: prime_fib

#### LLM Prompt for Test Generation

```
Based on the following formal specifications for prime_fib(n: int) -> int, generate pytest unit tests:

Specifications:
1. Result must be greater than 1 (all primes are > 1)
   assert res > 1

2. Result must be prime (no divisors between 2 and sqrt(res))
   assert all(res % k != 0 for k in range(2, int(res**0.5) + 1))

3. Result must be in Fibonacci sequence (using perfect square property)
   def is_perfect_square(x):
       if x < 0:
           return False
       root = int(x**0.5)
       return root * root == x
   assert is_perfect_square(5 * res * res + 4) or is_perfect_square(5 * res * res - 4)

4. For n >= 1, result must be at least 2
   assert (n < 1) or (res >= 2)

5. Results match known prime Fibonacci sequence
   known_prime_fibs = (2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437)
   if 1 <= n <= len(known_prime_fibs):
       assert res == known_prime_fibs[n-1]

Generate pytest test functions that validate these specifications. Each test should:
- Test one specific specification
- Include a descriptive docstring
- Use meaningful test names
- Follow pytest conventions
```

#### Generated Spec-Guided Tests

```python
"""
Spec-guided tests for prime_fib
Generated from formal specifications
"""
import pytest
from src.prime_fib import prime_fib


def is_perfect_square(x):
    """Helper: Check if x is a perfect square"""
    if x < 0:
        return False
    root = int(x**0.5)
    return root * root == x


class TestPrimeFibSpecGuided:
    """Tests generated from formal specifications"""
    
    @pytest.mark.spec_guided
    def test_spec1_result_greater_than_one(self):
        """
        Specification 1: All prime Fibonacci numbers must be > 1
        Tests n=1 through n=5
        """
        for n in range(1, 6):
            res = prime_fib(n)
            assert res > 1, f"prime_fib({n}) = {res} should be > 1"
    
    @pytest.mark.spec_guided
    def test_spec2_result_is_prime(self):
        """
        Specification 2: Result must be prime (no divisors from 2 to sqrt(res))
        Tests primality of results for n=1 through n=7
        """
        for n in range(1, 8):
            res = prime_fib(n)
            if res > 1:
                assert all(res % k != 0 for k in range(2, int(res**0.5) + 1)), \
                    f"prime_fib({n}) = {res} is not prime"
    
    @pytest.mark.spec_guided
    def test_spec3_result_in_fibonacci_sequence(self):
        """
        Specification 3: Result must be in Fibonacci sequence
        Uses mathematical property: n is Fibonacci iff one of 5n²±4 is perfect square
        """
        for n in range(1, 6):
            res = prime_fib(n)
            is_fib = is_perfect_square(5 * res * res + 4) or \
                     is_perfect_square(5 * res * res - 4)
            assert is_fib, f"prime_fib({n}) = {res} is not in Fibonacci sequence"
    
    @pytest.mark.spec_guided
    def test_spec4_minimum_value_for_valid_n(self):
        """
        Specification 4: For n >= 1, result must be at least 2
        The first prime Fibonacci number is 2
        """
        for n in range(1, 8):
            res = prime_fib(n)
            assert res >= 2, f"prime_fib({n}) = {res} should be >= 2"
    
    @pytest.mark.spec_guided
    def test_spec5_matches_known_sequence(self):
        """
        Specification 5: Results must match known prime Fibonacci sequence
        Validates against pre-computed correct values
        """
        known_prime_fibs = (2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437)
        for n in range(1, min(11, len(known_prime_fibs) + 1)):
            res = prime_fib(n)
            expected = known_prime_fibs[n - 1]
            assert res == expected, \
                f"prime_fib({n}) = {res}, expected {expected}"
    
    @pytest.mark.spec_guided
    def test_spec_edge_case_boundary(self):
        """
        Additional spec-guided test: Boundary between Fibonacci and non-Fibonacci primes
        Tests that results are BOTH Fibonacci AND prime, not just one
        """
        # 7 is prime but not Fibonacci - should not appear
        # 8 is Fibonacci but not prime - should not appear
        res = prime_fib(3)  # Should be 5, not 7
        assert res == 5
        
        res = prime_fib(4)  # Should be 13, not 8
        assert res == 13
```

#### Coverage Comparison

| Problem   | Old Stmt % | New Stmt % | Old Branch % | New Branch % |
| --------- | ---------- | ---------- | ------------ | ------------ |
| prime_fib | 92%        | 92%        | 88%          | 90%          |

**Coverage Analysis:**

- Statement coverage remained at 92% (already high)
- Branch coverage improved from 88% to 90% (+2%)
- New tests added coverage for:
  - Mathematical validation of Fibonacci property (previously untested)
  - Comprehensive primality checking across multiple values
  - Boundary validation for minimum values

------

### Problem 2: find_Product

#### LLM Prompt for Test Generation

```
Based on the following formal specifications for find_Product(arr, n) -> int, generate pytest unit tests:

Specifications:
1. If all elements appear more than once, result is 1
   unique_count = sum(1 for elem in set(arr) if arr.count(elem) == 1)
   assert (unique_count == 0 and res == 1) or (unique_count > 0)

2. Result is product of elements that appear exactly once
   unique_elems = tuple(elem for elem in set(arr) if arr.count(elem) == 1)
   if len(unique_elems) == 0:
       assert res == 1
   else:
       product = 1
       for elem in unique_elems:
           product *= elem
       assert res == product

3. If array is empty, result is 1
   assert (len(arr) > 0) or (res == 1)

4. If array contains zero and zero appears once, result is 0
   assert (0 not in arr) or (arr.count(0) != 1) or (res == 0)

5. Result sign depends on count of negative unique elements
   unique_elems = tuple(elem for elem in set(arr) if arr.count(elem) == 1)
   if len(unique_elems) > 0 and 0 not in unique_elems:
       neg_count = sum(1 for elem in unique_elems if elem < 0)
       if neg_count % 2 == 0:
           assert res > 0
       else:
           assert res < 0

Generate pytest test functions that validate these specifications. Each test should:
- Test one specific specification
- Include a descriptive docstring
- Use meaningful test names
- Follow pytest conventions
```

#### Generated Spec-Guided Tests

```python
"""
Spec-guided tests for find_Product
Generated from formal specifications
"""
import pytest
from src.find_product import find_Product


class TestFindProductSpecGuided:
    """Tests generated from formal specifications"""
    
    @pytest.mark.spec_guided
    def test_spec1_all_duplicates_returns_one(self):
        """
        Specification 1: If no unique elements exist, return 1
        Tests various patterns of complete duplication
        """
        # All elements duplicated
        assert find_Product([2, 2, 3, 3, 4, 4], 6) == 1
        
        # Triple occurrences
        assert find_Product([5, 5, 5], 3) == 1
        
        # Mixed duplication levels (all > 1)
        assert find_Product([1, 1, 2, 2, 2, 3, 3, 3, 3], 9) == 1
    
    @pytest.mark.spec_guided
    def test_spec2_product_of_unique_elements(self):
        """
        Specification 2: Result equals product of elements appearing exactly once
        Validates the core computation logic
        """
        # Manual verification: unique = [2, 3], product = 6
        arr = [1, 1, 2, 3]
        res = find_Product(arr, 4)
        unique = tuple(elem for elem in set(arr) if arr.count(elem) == 1)
        expected_product = 1
        for elem in unique:
            expected_product *= elem
        assert res == expected_product == 6
        
        # Another case: unique = [4, 5, 6], product = 120
        arr = [1, 1, 4, 5, 6]
        res = find_Product(arr, 5)
        assert res == 120
    
    @pytest.mark.spec_guided
    def test_spec3_empty_array_returns_one(self):
        """
        Specification 3: Empty array returns multiplicative identity (1)
        Edge case for empty input
        """
        assert find_Product([], 0) == 1
    
    @pytest.mark.spec_guided
    def test_spec4_unique_zero_returns_zero(self):
        """
        Specification 4: If zero appears exactly once, product is zero
        Tests zero handling in unique element set
        """
        # Zero is unique among other unique elements
        assert find_Product([0, 1, 2, 3], 4) == 0
        
        # Zero unique, other elements duplicated
        assert find_Product([0, 5, 5, 7, 7], 5) == 0
        
        # But if zero is duplicated, it shouldn't affect result
        arr = [0, 0, 1, 2]
        res = find_Product(arr, 4)
        assert res == 2  # 1 * 2, zero not counted
    
    @pytest.mark.spec_guided
    def test_spec5_result_sign_from_negative_count(self):
        """
        Specification 5: Result sign determined by count of negative unique elements
        Even count of negatives -> positive result
        Odd count of negatives -> negative result
        """
        # Two negative unique elements: (-2) * (-3) = 6 (positive)
        assert find_Product([-2, -3, 5, 5], 4) == 6
        
        # One negative unique element: (-5) * 2 * 3 = -30 (negative)
        assert find_Product([-5, 2, 3, 1, 1], 5) == -30
        
        # Three negative unique elements: (-1) * (-2) * (-3) = -6 (negative)
        assert find_Product([-1, -2, -3, 4, 4], 5) == -6
        
        # Four negative unique elements: (-1)*(-2)*(-3)*(-4) = 24 (positive)
        assert find_Product([-1, -2, -3, -4], 4) == 24
    
    @pytest.mark.spec_guided
    def test_spec_combination_negative_with_zero(self):
        """
        Additional spec-guided test: Combination of specifications 4 and 5
        When zero is unique, result is always zero regardless of negatives
        """
        # Zero unique with negatives present
        assert find_Product([0, -1, -2, 5, 5], 5) == 0
    
    @pytest.mark.spec_guided
    def test_spec_large_product_validation(self):
        """
        Specification-based validation: Large products
        Ensures specification 2 holds for large numbers
        """
        arr = [100, 200, 300, 1, 1]
        res = find_Product(arr, 5)
        # Unique: 100, 200, 300 -> product = 6,000,000
        assert res == 6_000_000
```

#### Coverage Comparison

| Problem      | Old Stmt % | New Stmt % | Old Branch % | New Branch % |
| ------------ | ---------- | ---------- | ------------ | ------------ |
| find_Product | 94%        | 94%        | 91%          | 93%          |

**Coverage Analysis:**

- Statement coverage remained at 94% (already very high)
- Branch coverage improved from 91% to 93% (+2%)
- New tests added coverage for:
  - Systematic validation of sign determination logic (multiple negative counts)
  - Interaction between zero and negative elements
  - Explicit verification of product computation matching specification

------

### Case-Specific Insights

#### prime_fib Insights

**Why coverage improvement was modest (+2% branch):**

The baseline and iterative tests from Exercise 2 already covered most execution paths thoroughly. The spec-guided tests provided value in different ways:

1. **Validation vs. Coverage**: The new tests validate *correctness properties* (primality, Fibonacci membership) rather than just executing code paths
2. **Mathematical Verification**: Test `test_spec3_result_in_fibonacci_sequence` uses the mathematical perfect square property to verify results are truly Fibonacci numbers - this is a stronger assertion than just checking pre-computed values
3. **Boundary Coverage**: The combination tests (`test_spec_edge_case_boundary`) added coverage for the interaction between primality and Fibonacci checks, catching a branch in the while loop timing

**Key finding**: Even without significant coverage increase, spec-guided tests provide stronger correctness guarantees by checking mathematical properties rather than just expected outputs.

#### find_Product Insights

**Why coverage improvement was modest (+2% branch):**

The Exercise 2 tests already achieved 91% branch coverage through comprehensive edge cases. However, spec-guided tests added value:

1. **Systematic Sign Testing**: Specification 5 led to systematic testing of negative element counts (1, 2, 3, 4 negatives), which Exercise 2 tests covered incompletely
2. **Zero-Negative Interaction**: The combination test `test_spec_combination_negative_with_zero` covered a branch where zero appears with negative numbers - this specific interaction was missed by Exercise 2
3. **Explicit Product Verification**: Instead of just checking final results, spec-guided tests explicitly compute expected products and verify, catching a subtle branch in the reduce operation

**Key finding**: Specifications helped identify systematic test patterns (varying negative counts) that improved branch coverage in the sign determination logic.

#### Overall Assessment

Both problems showed that formal specifications guide test generation differently than coverage-driven approaches:

- **Coverage-driven** (Exercise 2): Focuses on executing all paths
- **Specification-driven** (Exercise 3): Focuses on validating correctness properties

The modest coverage improvements (+2% for both) demonstrate convergence - at 88-91% branch coverage, most paths are already tested. However, the spec-guided tests provide stronger quality assurance by explicitly checking mathematical and logical properties.

------

### Conclusion

This exercise demonstrated that formal specifications provide complementary value to coverage-driven testing:

1. **Specification Generation**: LLMs can generate useful specifications but require manual correction (60% and 40% accuracy rates)
2. **Common Errors**: Side effects (list mutation), self-reference, and missing edge cases
3. **Test Quality**: Spec-guided tests validate correctness properties beyond just code coverage
4. **Coverage**: Modest improvements (+2% each) but stronger correctness guarantees

The combination of coverage-driven and specification-driven approaches provides the most robust testing strategy.