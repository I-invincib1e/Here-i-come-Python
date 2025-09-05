# Recursion Problems

Recursion involves functions that call themselves to solve problems by breaking them into smaller, similar subproblems.

## Fibonacci Sequence

**Problem**: Calculate the nth Fibonacci number where F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2).

**Iterative Solution**:
- Use two variables to track previous two numbers
- Update in loop: `a, b = b, a + b`

**Recursive with Memoization**:
- Use hash map to store computed values
- Avoid redundant calculations

**Time Complexity**: O(n) for both
**Space Complexity**: O(1) iterative, O(n) memoized

## Factorial

**Problem**: Calculate n! = n × (n-1) × ... × 1

**Solution Approach**:
- Iterative: multiply numbers from 1 to n
- Recursive: n! = n × (n-1)!

**Time Complexity**: O(n)
**Space Complexity**: O(1) iterative, O(n) recursive

## Power Function (Binary Exponentiation)

**Problem**: Calculate x^n efficiently.

**Solution Approach**:
- Use divide and conquer: x^n = (x^(n/2))^2
- Handle negative exponents by taking reciprocal
- Handle odd/even exponents differently

**Time Complexity**: O(log n)
**Space Complexity**: O(log n) due to recursion stack

## Generate Parentheses

**Problem**: Generate all combinations of n pairs of valid parentheses.

**Solution Approach**:
- Use backtracking with constraints
- Track open and close parenthesis counts
- Only add closing when more open than close

**Time Complexity**: O(4^n / √n)
**Space Complexity**: O(4^n / √n)

## Subsets

**Problem**: Given a set of distinct integers, return all possible subsets (power set).

**Solution Approach**:
- Use backtracking to include/exclude each element
- Start from current index to avoid duplicates
- Add current subset to result at each step

**Time Complexity**: O(2^n)
**Space Complexity**: O(2^n)

## Permutations

**Problem**: Given a collection of distinct integers, return all possible permutations.

**Solution Approach**:
- Use backtracking with swapping
- For each position, swap with remaining elements
- Recurse on next position, then backtrack

**Time Complexity**: O(n!)
**Space Complexity**: O(n!)

## Climbing Stairs

**Problem**: You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps. How many distinct ways?

**Solution Approach**:
- This is Fibonacci: ways(n) = ways(n-1) + ways(n-2)
- Base cases: 1 way for n=1, 2 ways for n=2

**Time Complexity**: O(n)
**Space Complexity**: O(1)

## Tower of Hanoi

**Problem**: Move n disks from source to destination using auxiliary peg, following rules: only one disk at a time, larger disk cannot be on smaller.

**Solution Approach**:
- Recursive: move n-1 disks to auxiliary
- Move largest disk to destination
- Move n-1 disks from auxiliary to destination

**Time Complexity**: O(2^n)
**Space Complexity**: O(n)

## Recursion Patterns

### Divide and Conquer
- Break problem into smaller subproblems
- Solve recursively, combine results
- Examples: binary search, merge sort

### Backtracking
- Try all possibilities at each step
- Undo choices that don't work (backtrack)
- Examples: N-Queens, Sudoku solver

### Memoization
- Cache results of expensive function calls
- Avoid redundant computations
- Trade space for time

### Tail Recursion
- Recursive call is the last operation
- Can be optimized to iterative by compiler
- Examples: factorial, sum

## Practice Tips

1. **Identify base case**: When to stop recursion
2. **Define recursive case**: How to break into smaller problems
3. **Handle edge cases**: Empty input, single element
4. **Consider stack overflow**: Large inputs may cause issues
5. **Use memoization**: For problems with overlapping subproblems
6. **Convert to iterative**: When recursion depth is too large
