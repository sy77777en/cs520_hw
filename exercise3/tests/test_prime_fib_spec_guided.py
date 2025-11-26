"""
Spec-guided tests for prime_fib
Generated from formal specifications in Exercise 3
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
