import pytest
from dsa.problems.stacks_queues import (
    MinStack, daily_temperatures, largest_rectangle_area,
    sliding_window_maximum, valid_parentheses_stack, next_greater_element
)


class TestMinStack:
    def test_min_stack_operations(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        assert stack.get_min() == -3
        stack.pop()
        assert stack.top() == 0
        assert stack.get_min() == -2
    
    def test_min_stack_single_element(self):
        stack = MinStack()
        stack.push(5)
        assert stack.get_min() == 5
        assert stack.top() == 5


class TestDailyTemperatures:
    def test_daily_temperatures(self):
        temps = [73, 74, 75, 71, 69, 72, 76, 73]
        result = daily_temperatures(temps)
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        assert result == expected
    
    def test_no_warmer_temperature(self):
        temps = [30, 40, 50, 60]
        result = daily_temperatures(temps)
        expected = [1, 1, 1, 0]
        assert result == expected
    
    def test_single_temperature(self):
        assert daily_temperatures([30]) == [0]


class TestLargestRectangleArea:
    def test_histogram_rectangles(self):
        heights = [2, 1, 5, 6, 2, 3]
        assert largest_rectangle_area(heights) == 10
    
    def test_increasing_heights(self):
        heights = [1, 2, 3, 4, 5]
        assert largest_rectangle_area(heights) == 9
    
    def test_single_bar(self):
        assert largest_rectangle_area([5]) == 5


class TestSlidingWindowMaximum:
    def test_sliding_window(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        result = sliding_window_maximum(nums, k)
        expected = [3, 3, 5, 5, 6, 7]
        assert result == expected
    
    def test_single_element_window(self):
        nums = [1, 2, 3, 4, 5]
        result = sliding_window_maximum(nums, 1)
        assert result == nums
    
    def test_window_size_equals_array(self):
        nums = [1, 3, 2]
        result = sliding_window_maximum(nums, 3)
        assert result == [3]


class TestValidParenthesesStack:
    def test_valid_parentheses(self):
        assert valid_parentheses_stack("()") is True
        assert valid_parentheses_stack("()[]{}") is True
        assert valid_parentheses_stack("([{}])") is True
    
    def test_invalid_parentheses(self):
        assert valid_parentheses_stack("(]") is False
        assert valid_parentheses_stack("([)]") is False
        assert valid_parentheses_stack("(((") is False
    
    def test_empty_string(self):
        assert valid_parentheses_stack("") is True


class TestNextGreaterElement:
    def test_next_greater_element(self):
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        result = next_greater_element(nums1, nums2)
        expected = [-1, 3, -1]
        assert result == expected
    
    def test_no_greater_element(self):
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        result = next_greater_element(nums1, nums2)
        expected = [3, -1]
        assert result == expected
