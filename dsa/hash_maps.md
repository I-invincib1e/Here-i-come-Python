# Hash Maps & Sets Problems

Hash maps (dictionaries) and sets are fundamental data structures for efficient lookups, counting, and grouping operations.

## Group Anagrams

**Problem**: Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

**Examples**:
- Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- Output: `[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]`

**Solution Approach**:
- Sort each string to create a key (anagrams will have same sorted string)
- Use hash map with sorted string as key, list of anagrams as value
- Return list of grouped anagrams

**Time Complexity**: O(n * m log m) where n=strings, m=avg string length
**Space Complexity**: O(n * m)

## Contains Duplicate

**Problem**: Given an integer array `nums`, return `true` if any value appears at least twice, `false` if every element is distinct.

**Solution Approach**:
- Use a set to track seen numbers
- For each number, check if already in set
- Return true if found, false otherwise

**Time Complexity**: O(n)
**Space Complexity**: O(n)

**Alternative**: Sort array and check adjacent elements (O(n log n) time, O(1) space)

## Intersection of Two Arrays

**Problem**: Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element must appear as many times as it shows in both arrays.

**Solution Approach**:
- Convert both arrays to sets
- Use set intersection to find common elements
- Convert back to list

**Time Complexity**: O(n + m)
**Space Complexity**: O(min(n, m))

## Single Number

**Problem**: Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

**Solution Approach**:
- Use XOR operation: `a ^ a = 0`, `a ^ 0 = a`
- XOR all numbers - duplicates cancel out, single number remains

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Examples**:
- `[2, 2, 1]` → `1`
- `[4, 1, 2, 1, 2]` → `4`

## Longest Consecutive Sequence

**Problem**: Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

**Examples**:
- Input: `[100, 4, 200, 1, 3, 2]`
- Output: `4` (sequence `[1, 2, 3, 4]`)

**Solution Approach**:
- Convert array to set for O(1) lookups
- For each number, check if it's the start of a sequence (num-1 not in set)
- If start, count consecutive numbers
- Track maximum length

**Time Complexity**: O(n)
**Space Complexity**: O(n)

## Subarray Sum Equals K

**Problem**: Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

**Solution Approach**:
- Use prefix sums with hash map
- Track cumulative sum and count occurrences
- For each prefix sum, check if `prefix_sum - k` exists in map
- That gives number of subarrays ending at current position

**Time Complexity**: O(n)
**Space Complexity**: O(n)

## Hash Map Patterns

### Frequency Counting
- Use `collections.Counter` for counting occurrences
- Useful for finding most frequent elements, duplicates

### Grouping
- Use hash map to group items by key
- Common for anagrams, grouping by property

### Prefix Sums
- Store cumulative sums in hash map
- Efficient for subarray sum problems

### Two-Pass with Hash Map
- First pass: build hash map
- Second pass: use hash map for lookups

## Practice Tips

1. **Choose the right data structure**: Set for membership, dict for key-value
2. **Consider trade-offs**: Hash maps use O(n) space for O(1) lookups
3. **Handle edge cases**: Empty arrays, single elements, all duplicates
4. **Use built-in optimizations**: `collections.defaultdict`, `set` operations
