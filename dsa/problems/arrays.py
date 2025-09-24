from __future__ import annotations

from typing import List


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers that add up to target (brute force approach).

    **Difficulty:** Easy
    **Pattern:** Brute Force / Nested Loops

    **Approach Evolution:** This is the naive O(n²) solution. We check every possible pair
    of numbers in the array. While correct, it's inefficient for large arrays.

    **Learning Focus:**
    - Understanding why brute force works but is slow
    - Recognizing when O(n²) algorithms become impractical
    - Building intuition for optimization opportunities
    - The importance of considering all constraints (time, space, readability)

    **Performance:** O(n²) time, O(1) space - acceptable only for small arrays (n ≤ 1000)

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        List of two indices that sum to target

    Raises:
        ValueError: If no such pair exists
    """
    # Check every possible pair of numbers
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    # If no pair found, raise error
    raise ValueError("No solution")


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers that add up to target (optimized approach).

    **Difficulty:** Easy
    **Pattern:** Hash Map / Dictionary

    **Approach Evolution:** This optimizes the brute force O(n²) solution to O(n) time
    by using a hash map for O(1) lookups. We trade space for time efficiency.

    **Performance Comparison:**
    - Brute Force: O(n²) time, O(1) space
    - Optimized: O(n) time, O(n) space
    - Break-even point: Around n=1000 elements

    **Visualization:**
    nums = [2, 7, 11, 15], target = 9
    seen = {}
    i=0, num=2, need=7, seen={2:0}
    i=1, num=7, need=2, found! return [0,1]

    **Learning Focus:**
    - Understanding hash table lookups for O(1) average-case performance
    - Handling edge cases: no solution, duplicate numbers, negative numbers
    - Time-space tradeoff: O(n) space for O(n) time vs O(n²) brute force
    - Index vs value tracking in array problems
    - When to optimize: performance requirements, input size expectations

    Uses a hash map to store numbers we've seen and their indices.
    For each number, calculate what we need to reach the target,
    and check if we've seen it before.

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        List of two indices that sum to target

    Raises:
        ValueError: If no such pair exists

    Time: O(n), Space: O(n)
    """
    # Dictionary to store number -> index mapping
    seen = {}
    for i, n in enumerate(nums):
        # Calculate the complement needed to reach target
        need = target - n
        # If we've seen the complement before, return the pair
        if need in seen:
            return [seen[need], i]
        # Otherwise, store current number and its index
        seen[n] = i
    # If no pair found, raise error
    raise ValueError("No solution")


def max_subarray(nums: List[int]) -> int:
    """Find the maximum sum of any contiguous subarray using Kadane's algorithm.

    **Difficulty:** Medium
    **Pattern:** Dynamic Programming / Greedy

    **Visualization Available:** Run `python -c "from dsa.visualization.kadane_visualizer import demonstrate_kadane_visualization; demonstrate_kadane_visualization()"`
    to see the algorithm in action!

    **Visualization:**
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    i=0: current=-2, best=-2
    i=1: current=max(1, -2+1)=1, best=max(-2,1)=1
    i=2: current=max(-3,1-3)=-2, best=max(1,-2)=1
    i=3: current=max(4,-2+4)=4, best=max(1,4)=4
    i=4: current=max(-1,4-1)=3, best=max(4,3)=4
    i=5: current=max(2,3+2)=5, best=max(4,5)=5
    i=6: current=max(1,5+1)=6, best=max(5,6)=6
    i=7: current=max(-5,6-5)=1, best=max(6,1)=6
    i=8: current=max(4,1+4)=5, best=max(6,5)=6

    **Learning Focus:**
    - Greedy algorithm design: making locally optimal choices
    - Dynamic programming concepts: optimal substructure
    - Handling negative numbers and edge cases
    - Single-pass algorithms vs multiple passes
    - Space optimization: O(1) space solution
    - Visual learning: Watch the algorithm track current vs global maximums

    This algorithm efficiently finds the maximum subarray sum in O(n) time.
    It keeps track of the current subarray sum and the best (maximum) sum found so far.
    At each step, it decides whether to start a new subarray or extend the current one.

    Args:
        nums: List of integers (can be positive, negative, or zero)

    Returns:
        Maximum sum of any contiguous subarray

    Time: O(n), Space: O(1)
    """
    # Handle empty array edge case
    if not nums:
        return 0

    # Initialize both current and best sums with first element
    best = current = nums[0]

    # Iterate through remaining elements, tracking two sums:
    # - current: sum of current subarray being considered
    # - best: maximum sum found so far across all subarrays
    for n in nums[1:]:
        # Kadane's key decision: start new subarray or extend current?
        # If current element is larger than current sum + element,
        # start fresh with just this element (handles negative prefixes)
        current = max(n, current + n)
        # Update global maximum if current subarray is better
        best = max(best, current)

    return best
