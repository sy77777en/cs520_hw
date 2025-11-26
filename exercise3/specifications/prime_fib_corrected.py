"""
PRIME_FIB - Corrected Specifications
Manually corrected after evaluating LLM-generated assertions
"""


def verify_prime_fib_specification(n, res):
    """
    Verifies all corrected specifications for prime_fib
    
    Args:
        n: Input parameter (which prime Fibonacci number)
        res: Result from prime_fib(n)
    
    Returns:
        bool: True if all specifications pass
    """
    
    # Specification 1: Result must be greater than 1 (all primes are > 1)
    # Status: CORRECT (unchanged from generated)
    assert res > 1, "Spec 1 failed: result must be > 1"
    
    
    # Specification 2: Result must be prime (no divisors between 2 and sqrt(res))
    # Status: CORRECT (unchanged from generated)
    assert all(res % k != 0 for k in range(2, int(res**0.5) + 1)), \
        "Spec 2 failed: result must be prime"
    
    
    # Specification 3: Result must be in Fibonacci sequence
    # Status: CORRECTED
    # Original error: Used list.append() which is a side effect
    # Fix: Use mathematical property - a number is Fibonacci if one of 5*n^2+4 or 5*n^2-4 is a perfect square
    def is_perfect_square(x):
        if x < 0:
            return False
        root = int(x**0.5)
        return root * root == x
    
    assert is_perfect_square(5 * res * res + 4) or is_perfect_square(5 * res * res - 4), \
        "Spec 3 failed: result must be in Fibonacci sequence"
    
    
    # Specification 4: For n >= 1, result must be at least 2
    # Status: CORRECT (unchanged from generated)
    assert (n < 1) or (res >= 2), \
        "Spec 4 failed: for n >= 1, result must be >= 2"
    
    
    # Specification 5: Results must match known sequence
    # Status: CORRECTED
    # Original error: Referenced prev_res = prime_fib(n-1) which is self-reference
    # Fix: Use pre-computed known values to validate without self-reference
    known_prime_fibs = (2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437)
    if 1 <= n <= len(known_prime_fibs):
        assert res == known_prime_fibs[n-1], \
            f"Spec 5 failed: prime_fib({n}) should be {known_prime_fibs[n-1]}, got {res}"
    
    
    return True


# Example usage:
if __name__ == "__main__":
    # Test the specifications
    from src.prime_fib import prime_fib
    
    for n in range(1, 11):
        res = prime_fib(n)
        try:
            verify_prime_fib_specification(n, res)
            print(f"✓ prime_fib({n}) = {res} - All specifications pass")
        except AssertionError as e:
            print(f"✗ prime_fib({n}) = {res} - {e}")
