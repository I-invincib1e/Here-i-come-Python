# Stacks & Queues Problems

Stacks (LIFO) and queues (FIFO) are essential for problems involving order, matching, and processing sequences.

## Min Stack

**Problem**: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

**Solution Approach**:
- Use two stacks: main stack and auxiliary stack for minimums
- When pushing, add to min_stack if value <= current min
- When popping, remove from min_stack if popped value equals current min

**Time Complexity**: All operations O(1)
**Space Complexity**: O(n)

## Daily Temperatures

**Problem**: Given a list of daily temperatures, return a list such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day with a warmer temperature, put `0`.

**Solution Approach**:
- Use monotonic stack to track indices of temperatures
- For each temperature, pop stack while current > stack top
- Calculate days difference for popped indices

**Time Complexity**: O(n)
**Space Complexity**: O(n)

## Largest Rectangle in Histogram

**Problem**: Given an array of integers `heights` representing the histogram's bar height, return the area of the largest rectangle in the histogram.

**Solution Approach**:
- Use stack to find next smaller element for each bar
- For each bar popped from stack, calculate area with that bar as smallest
- Width = distance to next smaller or end of array

**Time Complexity**: O(n)
**Space Complexity**: O(n)

## Sliding Window Maximum

**Problem**: Given an array `nums` and an integer `k`, return the maximum sliding window of size `k`.

**Solution Approach**:
- Use deque to maintain indices in decreasing order
- Remove indices outside current window
- Remove indices with smaller values than current
- Front of deque always contains maximum for current window

**Time Complexity**: O(n)
**Space Complexity**: O(k)

## Valid Parentheses

**Problem**: Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid.

**Solution Approach**:
- Use stack to track opening brackets
- For closing bracket, check if matches top of stack
- Return true if stack empty at end

**Time Complexity**: O(n)
**Space Complexity**: O(n)

## Next Greater Element

**Problem**: Given two arrays `nums1` and `nums2`, for each element in `nums1`, find the next greater element in `nums2`.

**Solution Approach**:
- Use stack to find next greater for all elements in nums2
- Build hash map of element -> next greater
- Map nums1 elements using the hash map

**Time Complexity**: O(n + m)
**Space Complexity**: O(n + m)

## Stack & Queue Patterns

### Monotonic Stack
- Maintain sorted order (increasing or decreasing)
- Useful for next greater/smaller element problems
- Process elements in single pass

### Stack for Matching
- Parentheses, brackets validation
- Expression evaluation
- Undo operations

### Queue for BFS
- Level-order traversal
- Sliding window problems
- First-in-first-out processing

### Deque for Sliding Window
- Maintain window maximum/minimum
- Efficient for dynamic window sizes
- O(1) access to both ends

## Practice Tips

1. **Choose the right data structure**: Stack for LIFO, queue for FIFO, deque for both ends
2. **Monotonic patterns**: Increasing stack for next greater, decreasing for next smaller
3. **Edge cases**: Empty input, single element, all increasing/decreasing
4. **Space optimization**: Use indices instead of values when possible
