"""
MBPP Problem 25: Product of Non-Repeated Elements
Corrected version with proper function signature
"""
from collections import Counter
from functools import reduce
from operator import mul


def find_Product(arr, n):
    """
    Find the product of all non-repeated (unique) elements in array.
    
    Args:
        arr (list): List of integers
        n (int): Length of array (note: implementation uses actual array length)
    
    Returns:
        int: Product of elements that appear exactly once, or 1 if none exist
    
    Examples:
        >>> find_Product([1, 1, 2, 3], 4)
        6
        >>> find_Product([1, 2, 3, 1, 1], 5)
        6
        >>> find_Product([1, 1, 4, 5, 6], 5)
        120
    """
    element_count = Counter(arr)
    non_repeated_elements = [
        element for element, count in element_count.items() if count == 1
    ]
    
    if not non_repeated_elements:
        return 1  # Return multiplicative identity for empty product
    
    return reduce(mul, non_repeated_elements, 1)
