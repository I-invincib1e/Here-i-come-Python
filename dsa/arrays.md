# Array Problems

This section covers fundamental array manipulation problems, focusing on efficiency and common patterns.

## Two Sum

**Problem**: Given an array of integers `nums` and an integer `target`, return indices of two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Examples**:
- Input: `nums = [2, 7, 11, 15]`, `target = 9`
- Output: `[0, 1]` (because `nums[0] + nums[1] == 9`)

**Solution Approach**:
- Use a hash map to store numbers we've seen and their indices
- For each number, calculate `need = target - num`
- If `need` is in the hash map, return the indices
- Otherwise, store the current number and index

**Time Complexity**: O(n) - single pass through array
**Space Complexity**: O(n) - hash map storage

**Edge Cases**:
- Duplicate numbers (e.g., `[3, 3]`, target `6`)
- Negative numbers
- No solution (though problem assumes one exists)

## Maximum Subarray Sum (Kadane's Algorithm)

**Problem**: Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Examples**:
- Input: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- Output: `6` (subarray `[4, -1, 2, 1]`)

**Solution Approach**:
- Track current maximum sum ending at current position
- Track global maximum sum seen so far
- For each element, decide whether to start new subarray or extend current
- `current = max(num, current + num)`

**Time Complexity**: O(n) - single pass
**Space Complexity**: O(1) - constant space

**Edge Cases**:
- All negative numbers (return largest single element)
- Empty array (return 0)
- Single element array

## Common Patterns in Array Problems

### Two Pointers
- Use when searching for pairs or checking conditions from both ends
- Move pointers based on comparison with target
- Example: Finding pairs that sum to target in sorted array

### Sliding Window
- Use for subarray problems with constraints
- Maintain window of valid elements
- Expand/contract window as needed

### Frequency Counting
- Use hash maps to count occurrences
- Useful for finding duplicates, anagrams, etc.

## Practice Tips

1. **Start with brute force**: Understand the problem by implementing O(n²) solution first
2. **Optimize step-by-step**: Look for ways to reduce time/space complexity
3. **Test edge cases**: Empty arrays, single elements, all negatives
4. **Understand constraints**: Consider input size limits for time complexity choices
