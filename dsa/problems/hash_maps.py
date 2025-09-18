from __future__ import annotations

from typing import Dict, List, Set


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group strings that are anagrams of each other.

    **Difficulty:** Medium
    **Pattern:** Hash Map / String Processing

    **Visualization:**
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sorted keys: {"aet": ["eat","tea","ate"], "ant": ["tan","nat"], "abt": ["bat"]}

    **Learning Focus:**
    - String manipulation and character counting
    - Hash map usage with non-integer keys
    - Sorting strings for canonical representation
    - Handling case sensitivity and special characters
    - Time complexity of string operations

    Anagrams are words with the same characters in different order.
    We use the sorted version of each string as a key to group them.

    Args:
        strs: List of strings to group

    Returns:
        List of lists, where each sublist contains anagrams

    Time: O(n * m log m) where n=number of strings, m=avg string length
    Space: O(n * m) for storing all strings in the hash map
    """
    # Dictionary to map sorted string -> list of anagrams
    groups = {}

    for s in strs:
        # Sort the string to create a unique key for anagrams
        key = ''.join(sorted(s))
        # Initialize list if key not seen before
        if key not in groups:
            groups[key] = []
        # Add current string to its anagram group
        groups[key].append(s)

    # Return all the grouped anagrams
    return list(groups.values())


def contains_duplicate(nums: List[int]) -> bool:
    """Check if the array contains any duplicate elements.

    This function uses a set to track seen numbers for O(1) lookup time.
    Alternative approach: sort the array and check adjacent elements (O(n log n) time, O(1) extra space).

    Args:
        nums: List of integers to check

    Returns:
        True if duplicates exist, False otherwise

    Time: O(n), Space: O(n) - can be optimized to O(1) space by sorting
    """
    # Set to track numbers we've seen
    seen = set()

    for num in nums:
        # If we've seen this number before, it's a duplicate
        if num in seen:
            return True
        # Add current number to seen set
        seen.add(num)

    # No duplicates found
    return False


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """Find the intersection of two arrays (common elements).

    Convert both arrays to sets and use set intersection operation.
    This efficiently finds common elements while removing duplicates.

    Args:
        nums1: First array of integers
        nums2: Second array of integers

    Returns:
        List of unique elements present in both arrays

    Time: O(n + m) for set creation, Space: O(min(n, m)) for smaller set
    """
    # Convert arrays to sets for O(1) lookup
    set1 = set(nums1)
    set2 = set(nums2)

    # Use set intersection to find common elements
    return list(set1 & set2)


def single_number(nums: List[int]) -> int:
    """Find the single number in an array where every other number appears twice.

    **Difficulty:** Easy
    **Pattern:** Bit Manipulation / XOR

    **Visualization:**
    nums = [4, 1, 2, 1, 2]
    4 ^ 1 ^ 2 ^ 1 ^ 2 = (1^1) ^ (2^2) ^ 4 = 0 ^ 0 ^ 4 = 4

    **Learning Focus:**
    - Bitwise operations and their properties
    - XOR as a mathematical group operation
    - Constant space algorithms vs linear space
    - Understanding binary representation
    - Trade-offs between different approaches

    Uses XOR bitwise operation. XOR has these properties:
    - a ^ a = 0 (same numbers cancel out)
    - a ^ 0 = a (XOR with zero leaves number unchanged)
    - XOR is commutative and associative

    So XORing all numbers will leave only the single number.

    Args:
        nums: Array where all numbers except one appear exactly twice

    Returns:
        The number that appears only once

    Time: O(n), Space: O(1) - no extra space needed
    """
    # Initialize result to 0 (XOR identity)
    result = 0

    # XOR all numbers together
    for num in nums:
        result ^= num

    # Result will be the single number (duplicates cancel out)
    return result


def two_sum_optimized(nums: List[int], target: int) -> List[int]:
    """Find two numbers in the array that add up to target (optimized version).

    This is the same as the basic two-sum but with early termination.
    Uses a hash map to store numbers we've seen and their indices.
    Returns immediately when a pair is found, without continuing to scan.

    Args:
        nums: Array of integers
        target: Target sum

    Returns:
        Indices of two numbers that sum to target

    Raises:
        ValueError: If no such pair exists

    Time: O(n), Space: O(n)
    """
    # Dictionary to store number -> index mapping
    seen = {}

    for i, num in enumerate(nums):
        # Calculate the complement needed
        complement = target - num

        # If complement exists in seen, we found a pair
        if complement in seen:
            return [seen[complement], i]

        # Store current number and its index
        seen[num] = i

    # If we reach here, no pair was found
    raise ValueError("No solution")


def longest_consecutive(nums: List[int]) -> int:
    """Find the length of the longest consecutive sequence of numbers.

    This algorithm uses a set for O(1) lookups and only starts counting
    sequences from their beginning (when num-1 is not in the set).
    This avoids recounting the same sequence multiple times.

    Args:
        nums: List of integers (may contain duplicates)

    Returns:
        Length of the longest consecutive sequence

    Time: O(n), Space: O(n) for the set
    """
    # Convert to set to remove duplicates and enable O(1) lookup
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if this is the beginning of a sequence
        # (i.e., the previous number is not in the set)
        if num - 1 not in num_set:
            current = num
            current_length = 1

            # Extend the sequence as far as possible
            while current + 1 in num_set:
                current += 1
                current_length += 1

            # Update the longest sequence found
            longest = max(longest, current_length)

    return longest


def subarray_sum(nums: List[int], k: int) -> int:
    """Count the number of subarrays that sum to exactly k.

    Uses prefix sums with a hash map to efficiently count subarrays.
    The key insight: if prefix_sum[j] - prefix_sum[i] = k, then
    the subarray from i+1 to j sums to k.

    This is equivalent to: prefix_sum[j] - k = prefix_sum[i]

    Args:
        nums: Array of integers
        k: Target sum

    Returns:
        Number of subarrays that sum to k

    Time: O(n), Space: O(n) for the hash map
    """
    count = 0
    prefix_sum = 0

    # Map from prefix sum to how many times it has occurred
    # Initialize with 0:1 because prefix sum of 0 occurs once (before any elements)
    sum_count = {0: 1}

    for num in nums:
        # Add current number to running prefix sum
        prefix_sum += num

        # Check if (prefix_sum - k) has been seen before
        # This means there's a subarray ending here that sums to k
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]

        # Update the count for current prefix sum
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count
