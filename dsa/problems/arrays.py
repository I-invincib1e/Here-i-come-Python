from __future__ import annotations

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers that add up to target.

    If multiple answers exist, return any one. Raise ValueError if none.
    """
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    raise ValueError("No solution")


def max_subarray(nums: List[int]) -> int:
    """Kadane's algorithm: maximum subarray sum."""
    if not nums:
        return 0
    best = current = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)
        best = max(best, current)
    return best


