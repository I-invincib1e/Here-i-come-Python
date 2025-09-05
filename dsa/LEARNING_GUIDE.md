# DSA Learning Guide

## Core Concepts & Patterns

### 1. Time & Space Complexity
- **Big O Notation**: Describes worst-case performance
- **Common complexities**: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
- **Space-time tradeoff**: Use more memory to reduce time complexity

### 2. Two Pointers Technique
- **When to use**: Sorted arrays, palindromes, finding pairs
- **Pattern**: Start from both ends, move inward based on condition
- **Example**: `is_palindrome`, `two_sum` in sorted array

### 3. Hash Maps (Dictionaries)
- **When to use**: Need O(1) lookup, counting frequencies, grouping
- **Tricks**: 
  - Use `collections.defaultdict` for cleaner code
  - Use set for membership testing
  - Use Counter for frequency counting

### 4. Sliding Window
- **When to use**: Subarray/substring problems with fixed/variable window
- **Pattern**: Expand right, contract left based on condition
- **Example**: `sliding_window_maximum`, `longest_substring_without_repeating`

### 5. Stack & Queue Patterns
- **Stack**: LIFO - use for matching, parsing, undo operations
- **Queue**: FIFO - use for BFS, level-order traversal
- **Monotonic stack**: Maintain sorted order for next greater/smaller

### 6. Recursion & Backtracking
- **Base case**: When to stop recursion
- **Recursive case**: How to break problem into smaller pieces
- **Backtracking**: Try all possibilities, undo when needed

## Efficiency Tips

### Memory Optimization
1. **In-place operations**: Modify input array instead of creating new one
2. **Generator expressions**: Use `(x for x in iterable)` instead of `[x for x in iterable]`
3. **Early termination**: Return as soon as you find the answer
4. **Bit manipulation**: Use XOR for certain operations (e.g., `single_number`)

### Time Optimization
1. **Sorting**: Often O(n log n) but enables O(n) algorithms
2. **Hash maps**: Trade space for O(1) lookup time
3. **Two pointers**: Avoid nested loops when possible
4. **Binary search**: O(log n) instead of O(n) for sorted data

### Common Patterns
1. **Prefix sums**: For subarray sum problems
2. **Frequency counting**: For anagram, duplicate problems
3. **Monotonic stack**: For next greater/smaller element problems
4. **Sliding window**: For substring/subarray optimization

## Problem-Solving Strategy

1. **Understand the problem**: Read carefully, identify constraints
2. **Think of brute force**: Start with obvious solution
3. **Look for patterns**: Can you use known techniques?
4. **Optimize**: Can you reduce time/space complexity?
5. **Test edge cases**: Empty inputs, single elements, duplicates

## Practice Progression

### Beginner (Arrays & Strings)
- Two Sum, Contains Duplicate
- Valid Parentheses, First Unique Character
- Longest Common Prefix

### Intermediate (Hash Maps & Stacks)
- Group Anagrams, Single Number
- Daily Temperatures, Largest Rectangle
- Next Greater Element

### Advanced (Recursion & Complex Patterns)
- Generate Parentheses, Subsets
- Tower of Hanoi, Climb Stairs
- Sliding Window Maximum

## Testing Strategy

1. **Edge cases**: Empty inputs, single elements
2. **Boundary conditions**: Min/max values
3. **Normal cases**: Typical inputs
4. **Invalid inputs**: Test error handling
5. **Performance**: Test with large inputs

## Common Mistakes to Avoid

1. **Off-by-one errors**: Check loop bounds carefully
2. **Index out of bounds**: Validate array access
3. **Infinite recursion**: Ensure base case is reachable
4. **Memory leaks**: Clean up resources in recursion
5. **Wrong data structure**: Choose appropriate DS for the problem
