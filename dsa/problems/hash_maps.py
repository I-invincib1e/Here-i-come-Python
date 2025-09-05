from __future__ import annotations

from typing import Dict, List, Set


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group anagrams together.
    
    Time: O(n * m) where n=strings, m=avg length, Space: O(n * m)
    Trick: Use sorted string as key for grouping
    """
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())


def contains_duplicate(nums: List[int]) -> bool:
    """Check if array contains duplicates.
    
    Time: O(n), Space: O(n)
    Trick: Use set for O(1) lookup, or sort for O(1) space
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """Find intersection of two arrays.
    
    Time: O(n + m), Space: O(min(n, m))
    Trick: Use set intersection for efficiency
    """
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)


def single_number(nums: List[int]) -> int:
    """Find single number in array where others appear twice.
    
    Time: O(n), Space: O(1)
    Trick: XOR all numbers - duplicates cancel out
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def two_sum_optimized(nums: List[int], target: int) -> List[int]:
    """Two sum with early termination.
    
    Time: O(n), Space: O(n)
    Trick: One pass with hash map, return immediately when found
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No solution")


def longest_consecutive(nums: List[int]) -> int:
    """Find longest consecutive sequence length.
    
    Time: O(n), Space: O(n)
    Trick: Use set for O(1) lookup, only start counting from sequence starts
    """
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Only start counting if this is the start of a sequence
        if num - 1 not in num_set:
            current = num
            current_length = 1
            
            while current + 1 in num_set:
                current += 1
                current_length += 1
            
            longest = max(longest, current_length)
    
    return longest


def subarray_sum(nums: List[int], k: int) -> int:
    """Count subarrays that sum to k.
    
    Time: O(n), Space: O(n)
    Trick: Use prefix sum with hash map
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # prefix sum 0 appears once
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
