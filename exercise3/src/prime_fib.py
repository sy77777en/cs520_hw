"""
HumanEval Problem 39: Prime Fibonacci Numbers
Corrected version fixing variable swap bug
"""


def is_prime(p):
    """
    Check if a number is prime.
    
    Args:
        p (int): Number to check
    
    Returns:
        bool: True if p is prime, False otherwise
    """
    if p < 2:
        return False
    for k in range(2, int(p**0.5) + 1):
        if p % k == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    Return the n-th Fibonacci number that is also prime.
    
    Args:
        n (int): Position of the prime Fibonacci number (1-indexed)
    
    Returns:
        int: The n-th prime Fibonacci number
    
    Examples:
        >>> prime_fib(1)
        2
        >>> prime_fib(2)
        3
        >>> prime_fib(3)
        5
        >>> prime_fib(4)
        13
        >>> prime_fib(5)
        89
    """
    fib1, fib2 = 0, 1
    count = 0
    
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        
        if is_prime(fib1):
            count += 1
            if count == n:
                return fib1
