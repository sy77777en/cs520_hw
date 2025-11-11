"""
Iteration 1: Input validation and helper function tests
Goal: Improve branch coverage from 62% to 78%
Added: 5 new tests targeting is_prime edge cases and early loop behavior
"""
import pytest
from src.prime_fib import prime_fib, is_prime


class TestPrimeFibIter1:
    """LLM-generated tests - Iteration 1"""
    
    @pytest.mark.iteration1
    def test_is_prime_zero(self):
        """
        Test is_prime helper with 0.
        Coverage: Validates edge case handling
        """
        assert not is_prime(0)
    
    @pytest.mark.iteration1
    def test_is_prime_one(self):
        """
        Test is_prime helper with 1.
        Coverage: 1 is not prime by definition
        """
        assert not is_prime(1)
    
    @pytest.mark.iteration1
    def test_is_prime_two(self):
        """
        Test is_prime helper with 2.
        Coverage: 2 is the only even prime
        """
        assert is_prime(2)
    
    @pytest.mark.iteration1
    def test_is_prime_three(self):
        """
        Test is_prime helper with 3.
        Coverage: Small odd prime
        """
        assert is_prime(3)
    
    @pytest.mark.iteration1
    def test_is_prime_composite(self):
        """
        Test is_prime with composite numbers.
        Coverage: Validates primality check loop
        """
        assert not is_prime(4)
        assert not is_prime(6)
        assert not is_prime(9)
        assert not is_prime(15)


# Coverage after Iteration 1: 85% line, 78% branch (+16% branch)
