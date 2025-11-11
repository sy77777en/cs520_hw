"""
Original Exercise 1 Submission - FAILED
Bug: Variable swap error (checking wrong variable after swap)
This was the actual bug GPT-4o generated in Exercise 1
"""


def is_prime(p):
    """Check if a number is prime."""
    if p < 2:
        return False
    for k in range(2, int(p**0.5) + 1):
        if p % k == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    Attempts to return n-th prime Fibonacci number.
    Bug: Checks and returns fib2 instead of fib1 after swap.
    """
    fib1, fib2 = 0, 1
    count = 0
    
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        
        if is_prime(fib2):  # ❌ Bug: Should check fib1 (the newly computed value)
            count += 1
            if count == n:
                return fib2  # ❌ Bug: Should return fib1


# Result: All 10 HumanEval tests failed
# Example: prime_fib(1) returned 1 instead of 2
#          prime_fib(2) returned 2 instead of 3
