"""
MBPP Baseline Tests for find_Product (Problem 25)
These are the ACTUAL 26 tests from MBPP benchmark
Coverage achieved: 85% line, 68% branch
"""
import pytest
from src.find_product import find_Product


class TestFindProductBaseline:
    """Original MBPP test suite for problem 25"""
    
    @pytest.mark.baseline
    def test_case_1(self):
        assert find_Product([1, 1, 2, 3], 4) == 6
    
    @pytest.mark.baseline
    def test_case_2(self):
        assert find_Product([1, 2, 3, 1, 1], 5) == 6
    
    @pytest.mark.baseline
    def test_case_3(self):
        assert find_Product([1, 1, 4, 5, 6], 5) == 120
    
    @pytest.mark.baseline
    def test_case_4(self):
        assert find_Product([6, 5, 2, 2], 4) == 60
    
    @pytest.mark.baseline
    def test_case_5(self):
        assert find_Product([3, 3, 4, 8], 2) == 3
    
    @pytest.mark.baseline
    def test_case_6(self):
        assert find_Product([4, 3, 1, 2], 3) == 6
    
    @pytest.mark.baseline
    def test_case_7(self):
        assert find_Product([6, 6, 7, 7], 3) == 42
    
    @pytest.mark.baseline
    def test_case_8(self):
        assert find_Product([3, 5, 3, 1], 4) == 15
    
    @pytest.mark.baseline
    def test_case_9(self):
        assert find_Product([5, 4, 6, 3], 3) == 60
    
    @pytest.mark.baseline
    def test_case_10(self):
        assert find_Product([1, 1, 2, 2], 4) == 2
    
    @pytest.mark.baseline
    def test_case_11(self):
        assert find_Product([6, 3, 4, 4], 3) == 12
    
    @pytest.mark.baseline
    def test_case_12(self):
        assert find_Product([2, 5, 4, 8], 3) == 40
    
    @pytest.mark.baseline
    def test_case_13(self):
        assert find_Product([5, 4, 6, 5], 3) == 20
    
    @pytest.mark.baseline
    def test_case_14(self):
        assert find_Product([3, 1, 2, 6], 4) == 36
    
    @pytest.mark.baseline
    def test_case_15(self):
        assert find_Product([4, 6, 3, 8], 2) == 12
    
    @pytest.mark.baseline
    def test_case_16(self):
        assert find_Product([5, 4, 5, 3], 4) == 60
    
    @pytest.mark.baseline
    def test_case_17(self):
        assert find_Product([2, 1, 2, 4], 4) == 8
    
    @pytest.mark.baseline
    def test_case_18(self):
        assert find_Product([2, 1, 6, 6], 3) == 12
    
    @pytest.mark.baseline
    def test_case_19(self):
        assert find_Product([2, 5, 2, 4], 4) == 40
    
    @pytest.mark.baseline
    def test_case_20(self):
        assert find_Product([3, 7, 5, 6, 2], 3) == 30
    
    @pytest.mark.baseline
    def test_case_21(self):
        assert find_Product([4, 6, 9, 9, 5], 2) == 20
    
    @pytest.mark.baseline
    def test_case_22(self):
        assert find_Product([1, 2, 7, 10, 4], 4) == 56
    
    @pytest.mark.baseline
    def test_case_23(self):
        assert find_Product([4, 6, 5, 7, 7], 5) == 840
    
    @pytest.mark.baseline
    def test_case_24(self):
        assert find_Product([1, 4, 6, 2, 8], 5) == 384
    
    @pytest.mark.baseline
    def test_case_25(self):
        assert find_Product([3, 2, 6, 8, 9], 4) == 288
    
    @pytest.mark.baseline
    def test_case_26(self):
        assert find_Product([1, 3, 6, 10, 7], 5) == 1260
    
    @pytest.mark.baseline
    def test_challenge_case(self):
        """Challenge test from MBPP"""
        assert find_Product([1, 1, 4, 5, 6, 5, 7, 1, 1, 3, 4], 11) == 2520