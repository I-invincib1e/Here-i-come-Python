import pytest
from dsa.problems.hash_maps import (
    group_anagrams, contains_duplicate, intersection,
    single_number, two_sum_optimized, longest_consecutive, subarray_sum
)


class TestGroupAnagrams:
    def test_group_anagrams(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        # Sort each group for comparison
        result = [sorted(group) for group in result]
        expected = [sorted(group) for group in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]]
        assert len(result) == len(expected)
        for group in expected:
            assert group in result
    
    def test_empty_list(self):
        assert group_anagrams([]) == []
    
    def test_single_string(self):
        assert group_anagrams(["a"]) == [["a"]]


class TestContainsDuplicate:
    def test_has_duplicates(self):
        assert contains_duplicate([1, 2, 3, 1]) is True
    
    def test_no_duplicates(self):
        assert contains_duplicate([1, 2, 3, 4]) is False
    
    def test_empty_array(self):
        assert contains_duplicate([]) is False
    
    def test_single_element(self):
        assert contains_duplicate([1]) is False


class TestIntersection:
    def test_has_intersection(self):
        result = set(intersection([1, 2, 2, 1], [2, 2]))
        assert result == {2}
    
    def test_no_intersection(self):
        assert intersection([1, 2, 3], [4, 5, 6]) == []
    
    def test_empty_arrays(self):
        assert intersection([], []) == []


class TestSingleNumber:
    def test_single_number(self):
        assert single_number([2, 2, 1]) == 1
        assert single_number([4, 1, 2, 1, 2]) == 4
    
    def test_single_element(self):
        assert single_number([1]) == 1


class TestTwoSumOptimized:
    def test_two_sum_exists(self):
        result = two_sum_optimized([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]
    
    def test_two_sum_no_solution(self):
        with pytest.raises(ValueError):
            two_sum_optimized([1, 2, 3], 7)
    
    def test_two_sum_duplicates(self):
        result = two_sum_optimized([3, 3], 6)
        assert sorted(result) == [0, 1]


class TestLongestConsecutive:
    def test_consecutive_sequence(self):
        assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    
    def test_no_consecutive(self):
        assert longest_consecutive([1, 3, 5, 7]) == 1
    
    def test_empty_array(self):
        assert longest_consecutive([]) == 0


class TestSubarraySum:
    def test_subarray_sum_exists(self):
        assert subarray_sum([1, 1, 1], 2) == 2
    
    def test_no_subarray_sum(self):
        assert subarray_sum([1, 2, 3], 7) == 0
    
    def test_single_element(self):
        assert subarray_sum([1], 1) == 1
