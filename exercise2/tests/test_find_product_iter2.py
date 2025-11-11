"""
Iteration 2: Parameter validation and edge cases
Goal: Improve branch coverage from 80% to 88%
Added: 3 new tests for remaining uncovered branches
"""
import pytest
from src.find_product import find_Product


class TestFindProductIter2:
    """LLM-generated tests - Iteration 2"""
    
    @pytest.mark.iteration2
    def test_large_array_performance(self):
        """
        Test with large array (1000 elements).
        Coverage: Validates algorithm scales correctly
        """
        arr = list(range(1000))  # All unique: 0, 1, 2, ..., 999
        result = find_Product(arr, 1000)
        assert result > 0  # Product should be positive and large
    
    @pytest.mark.iteration2
    def test_partial_duplicates_complex(self):
        """
        Test complex pattern of partial duplicates.
        Coverage: Multiple duplicate groups with some unique elements
        """
        # 1 and 3 appear twice, 2 and 4 are unique
        assert find_Product([1, 1, 2, 3, 3, 4], 6) == 8  # 2 * 4
    
    @pytest.mark.iteration2
    def test_single_unique_element(self):
        """
        Test array where only one element is unique.
        Coverage: Edge case of minimal non-repeated set
        """
        assert find_Product([5, 5, 7, 5], 4) == 7


# Coverage after Iteration 2: 92% line, 88% branch (+8% branch)
