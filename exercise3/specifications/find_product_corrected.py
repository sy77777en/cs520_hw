"""
FIND_PRODUCT - Corrected Specifications
Manually corrected after evaluating LLM-generated assertions
"""


def verify_find_product_specification(arr, n, res):
    """
    Verifies all corrected specifications for find_Product
    
    Args:
        arr: Input array
        n: Length parameter (though implementation uses len(arr))
        res: Result from find_Product(arr, n)
    
    Returns:
        bool: True if all specifications pass
    """
    
    # Specification 1: If all elements appear more than once, result is 1
    # Status: CORRECTED
    # Original error: Used dictionary mutation (counts[elem] = ...)
    # Fix: Use tuple comprehension and count() to avoid mutation
    unique_count = sum(1 for elem in set(arr) if arr.count(elem) == 1)
    assert (unique_count == 0 and res == 1) or (unique_count > 0), \
        "Spec 1 failed: if no unique elements, result should be 1"
    
    
    # Specification 2: Result is product of elements that appear exactly once
    # Status: CORRECTED
    # Original error: Depended on mutated dictionary from Spec 1
    # Fix: Compute unique elements using immutable operations
    unique_elems = tuple(elem for elem in set(arr) if arr.count(elem) == 1)
    if len(unique_elems) == 0:
        assert res == 1, "Spec 2 failed: empty product should be 1"
    else:
        product = 1
        for elem in unique_elems:
            product *= elem
        assert res == product, \
            f"Spec 2 failed: result should be product of unique elements = {product}, got {res}"
    
    
    # Specification 3: If array is empty, result is 1
    # Status: CORRECT (unchanged from generated)
    assert (len(arr) > 0) or (res == 1), \
        "Spec 3 failed: empty array should return 1"
    
    
    # Specification 4: If array contains zero and zero appears once, result is 0
    # Status: CORRECT (unchanged from generated)
    assert (0 not in arr) or (arr.count(0) != 1) or (res == 0), \
        "Spec 4 failed: unique zero should make result 0"
    
    
    # Specification 5: Result sign depends on count of negative unique elements
    # Status: CORRECTED
    # Original error: Depended on mutated unique_elements list
    # Fix: Recompute using immutable operations
    unique_elems = tuple(elem for elem in set(arr) if arr.count(elem) == 1)
    if len(unique_elems) > 0 and 0 not in unique_elems:
        neg_count = sum(1 for elem in unique_elems if elem < 0)
        if neg_count % 2 == 0:
            assert res > 0, \
                f"Spec 5 failed: even number of negatives ({neg_count}) should give positive result"
        else:
            assert res < 0, \
                f"Spec 5 failed: odd number of negatives ({neg_count}) should give negative result"
    elif 0 in unique_elems and arr.count(0) == 1:
        assert res == 0, \
            "Spec 5 failed: unique zero should make result 0"
    
    
    return True


# Example usage:
if __name__ == "__main__":
    # Test the specifications
    from src.find_product import find_Product
    
    test_cases = [
        ([1, 1, 2, 3], 4, 6),
        ([1, 2, 3, 1, 1], 5, 6),
        ([1, 1, 4, 5, 6], 5, 120),
        ([], 0, 1),
        ([2, 2, 2], 3, 1),
        ([0, 1, 2], 3, 0),
        ([-2, -3, 5, 5], 4, 6),
        ([-5, 2, 3, 1, 1], 5, -30),
    ]
    
    for arr, n, expected in test_cases:
        res = find_Product(arr, n)
        try:
            verify_find_product_specification(arr, n, res)
            status = "✓" if res == expected else "?"
            print(f"{status} find_Product({arr}, {n}) = {res} - All specifications pass")
        except AssertionError as e:
            print(f"✗ find_Product({arr}, {n}) = {res} - {e}")
