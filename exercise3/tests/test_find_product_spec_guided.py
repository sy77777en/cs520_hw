"""
Spec-guided tests for find_Product
Generated from formal specifications in Exercise 3
"""
import pytest
from src.find_product import find_Product


class TestFindProductSpecGuided:
    """Tests generated from formal specifications"""
    
    @pytest.mark.spec_guided
    def test_spec1_all_duplicates_returns_one(self):
        """
        Specification 1: If no unique elements exist, return 1
        Tests various patterns of complete duplication
        """
        # All elements duplicated
        assert find_Product([2, 2, 3, 3, 4, 4], 6) == 1
        
        # Triple occurrences
        assert find_Product([5, 5, 5], 3) == 1
        
        # Mixed duplication levels (all > 1)
        assert find_Product([1, 1, 2, 2, 2, 3, 3, 3, 3], 9) == 1
    
    @pytest.mark.spec_guided
    def test_spec2_product_of_unique_elements(self):
        """
        Specification 2: Result equals product of elements appearing exactly once
        Validates the core computation logic
        """
        # Manual verification: unique = [2, 3], product = 6
        arr = [1, 1, 2, 3]
        res = find_Product(arr, 4)
        unique = tuple(elem for elem in set(arr) if arr.count(elem) == 1)
        expected_product = 1
        for elem in unique:
            expected_product *= elem
        assert res == expected_product == 6
        
        # Another case: unique = [4, 5, 6], product = 120
        arr = [1, 1, 4, 5, 6]
        res = find_Product(arr, 5)
        assert res == 120
    
    @pytest.mark.spec_guided
    def test_spec3_empty_array_returns_one(self):
        """
        Specification 3: Empty array returns multiplicative identity (1)
        Edge case for empty input
        """
        assert find_Product([], 0) == 1
    
    @pytest.mark.spec_guided
    def test_spec4_unique_zero_returns_zero(self):
        """
        Specification 4: If zero appears exactly once, product is zero
        Tests zero handling in unique element set
        """
        # Zero is unique among other unique elements
        assert find_Product([0, 1, 2, 3], 4) == 0
        
        # Zero unique, other elements duplicated
        assert find_Product([0, 5, 5, 7, 7], 5) == 0
        
        # But if zero is duplicated, it shouldn't affect result
        arr = [0, 0, 1, 2]
        res = find_Product(arr, 4)
        assert res == 2  # 1 * 2, zero not counted
    
    @pytest.mark.spec_guided
    def test_spec5_result_sign_from_negative_count(self):
        """
        Specification 5: Result sign determined by count of negative unique elements
        Even count of negatives -> positive result
        Odd count of negatives -> negative result
        """
        # Two negative unique elements: (-2) * (-3) = 6 (positive)
        assert find_Product([-2, -3, 5, 5], 4) == 6
        
        # One negative unique element: (-5) * 2 * 3 = -30 (negative)
        assert find_Product([-5, 2, 3, 1, 1], 5) == -30
        
        # Three negative unique elements: (-1) * (-2) * (-3) = -6 (negative)
        assert find_Product([-1, -2, -3, 4, 4], 5) == -6
        
        # Four negative unique elements: (-1)*(-2)*(-3)*(-4) = 24 (positive)
        assert find_Product([-1, -2, -3, -4], 4) == 24
    
    @pytest.mark.spec_guided
    def test_spec_combination_negative_with_zero(self):
        """
        Additional spec-guided test: Combination of specifications 4 and 5
        When zero is unique, result is always zero regardless of negatives
        """
        # Zero unique with negatives present
        assert find_Product([0, -1, -2, 5, 5], 5) == 0
    
    @pytest.mark.spec_guided
    def test_spec_large_product_validation(self):
        """
        Specification-based validation: Large products
        Ensures specification 2 holds for large numbers
        """
        arr = [100, 200, 300, 1, 1]
        res = find_Product(arr, 5)
        # Unique: 100, 200, 300 -> product = 6,000,000
        assert res == 6_000_000
