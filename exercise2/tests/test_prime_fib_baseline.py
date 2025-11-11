"""
HumanEval Baseline Tests for prime_fib
These are the original 10 tests provided with HumanEval benchmark
Coverage achieved: 75% line, 62% branch
"""
import pytest
from src.prime_fib import prime_fib


class TestPrimeFibBaseline:
    """Original HumanEval test suite for problem 39"""
    
    @pytest.mark.baseline
    def test_first_prime_fib(self):
        """First prime Fibonacci number is 2"""
        assert prime_fib(1) == 2
    
    @pytest.mark.baseline
    def test_second_prime_fib(self):
        """Second prime Fibonacci number is 3"""
        assert prime_fib(2) == 3
    
    @pytest.mark.baseline
    def test_third_prime_fib(self):
        """Third prime Fibonacci number is 5"""
        assert prime_fib(3) == 5
    
    @pytest.mark.baseline
    def test_fourth_prime_fib(self):
        """Fourth prime Fibonacci number is 13"""
        assert prime_fib(4) == 13
    
    @pytest.mark.baseline
    def test_fifth_prime_fib(self):
        """Fifth prime Fibonacci number is 89"""
        assert prime_fib(5) == 89
    
    @pytest.mark.baseline
    def test_sixth_prime_fib(self):
        """Sixth prime Fibonacci number is 233"""
        assert prime_fib(6) == 233
    
    @pytest.mark.baseline
    def test_seventh_prime_fib(self):
        """Seventh prime Fibonacci number is 1597"""
        assert prime_fib(7) == 1597
    
    @pytest.mark.baseline
    def test_eighth_prime_fib(self):
        """Eighth prime Fibonacci number is 28657"""
        assert prime_fib(8) == 28657
    
    @pytest.mark.baseline
    def test_ninth_prime_fib(self):
        """Ninth prime Fibonacci number is 514229"""
        assert prime_fib(9) == 514229
    
    @pytest.mark.baseline
    def test_tenth_prime_fib(self):
        """Tenth prime Fibonacci number is 433494437"""
        assert prime_fib(10) == 433494437
