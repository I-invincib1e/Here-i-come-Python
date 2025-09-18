from __future__ import annotations

from collections import deque
from typing import List, Optional


class MinStack:
    """Stack that supports push, pop, top, and getMin in O(1) time.
    
    Trick: Use auxiliary stack to track minimums
    """
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def get_min(self) -> int:
        return self.min_stack[-1]


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """Find number of days until a warmer temperature for each day.

    Uses a monotonic decreasing stack to efficiently find the next warmer temperature.
    The stack stores indices of temperatures that haven't found their warmer day yet.

    For each temperature:
    - While stack has indices with smaller temperatures, pop them and calculate days
    - Push current index onto stack

    Args:
        temperatures: Daily temperature readings

    Returns:
        List where result[i] is days until warmer temperature, or 0 if none

    Time: O(n), Space: O(n) - stack can hold up to n elements
    """
    # Initialize result array with 0s (default for no warmer temperature)
    result = [0] * len(temperatures)
    # Stack to store indices of temperatures waiting for warmer days
    stack = []

    for i, temp in enumerate(temperatures):
        # While stack has temperatures smaller than current, they found their warmer day
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            # Calculate days between: current day - previous day
            result[prev_index] = i - prev_index
        # Push current index onto stack
        stack.append(i)

    return result


def largest_rectangle_area(heights: List[int]) -> int:
    """Find largest rectangle area in histogram.
    
    Time: O(n), Space: O(n)
    Trick: Use stack to find next smaller element for each bar
    """
    stack = []
    max_area = 0
    
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)
    
    # Process remaining bars
    while stack:
        h = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * width)
    
    return max_area


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """Find maximum in each sliding window of size k.
    
    Time: O(n), Space: O(k)
    Trick: Use deque to maintain decreasing order
    """
    dq = deque()  # store indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove indices with smaller values
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


def valid_parentheses_stack(s: str) -> bool:
    """Check valid parentheses using explicit stack.
    
    Time: O(n), Space: O(n)
    Trick: Use stack to match brackets, early termination
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    """Find next greater element for each element in nums1.
    
    Time: O(n + m), Space: O(n + m)
    Trick: Use stack to find next greater element efficiently
    """
    stack = []
    next_greater = {}
    
    # Find next greater for all elements in nums2
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    # Map nums1 to their next greater elements
    return [next_greater.get(num, -1) for num in nums1]
