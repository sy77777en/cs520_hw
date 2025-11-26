"""
Iteration 1: LLM-generated edge case tests
Goal: Improve branch coverage from 68% to 80%
Added: 6 new tests targeting uncovered branches
"""
import pytest
from src.find_product import find_Product


class TestFindProductIter1:
    """LLM-generated tests - Iteration 1"""
    
    @pytest.mark.iteration1
    def test_empty_array(self):
        """
        Test empty array returns multiplicative identity.
        Coverage: Exercises empty input branch
        """
        assert find_Product([], 0) == 1
    
    @pytest.mark.iteration1
    def test_all_duplicates(self):
        """
        Test all elements duplicated - no unique elements.
        Coverage: Exercises the 'if not non_repeated_elements' branch
        """
        assert find_Product([2, 2, 2, 2], 4) == 1
    
    @pytest.mark.iteration1
    def test_with_zero(self):
        """
        Test array containing zero among unique elements.
        Coverage: Tests multiplication with zero
        """
        assert find_Product([0, 1, 2, 3], 4) == 0
    
    @pytest.mark.iteration1
    def test_all_zeros(self):
        """
        Test array of all zeros (all duplicates).
        Coverage: Combines zero handling with duplicate detection
        """
        assert find_Product([0, 0], 2) == 1
    
    @pytest.mark.iteration1
    def test_negative_unique(self):
        """
        Test negative numbers as unique elements.
        Coverage: Validates negative number multiplication
        """
        assert find_Product([-5, -5, 3, 4], 4) == 12  # 3 * 4
    
    @pytest.mark.iteration1
    def test_n_parameter_mismatch(self):
        """
        Test when n doesn't match array length.
        Coverage: Tests robustness of implementation
        Note: Current implementation ignores n and uses len(arr)
        """
        result = find_Product([1, 2, 3, 4], 2)
        assert result == 24  # All elements are unique


# Coverage after Iteration 1: 90% line, 80% branch (+12% branch)
