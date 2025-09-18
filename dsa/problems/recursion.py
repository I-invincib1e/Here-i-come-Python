from __future__ import annotations

from typing import List, Optional


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using iterative approach.

    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    Each number is the sum of the two preceding ones.

    This iterative solution avoids recursion to prevent stack overflow
    and achieves O(1) space complexity.

    Args:
        n: The position in Fibonacci sequence (0-based)

    Returns:
        The nth Fibonacci number

    Time: O(n), Space: O(1)
    """
    # Base cases: F(0) = 0, F(1) = 1
    if n <= 1:
        return n

    # Initialize first two Fibonacci numbers
    a, b = 0, 1

    # Iterate from 2 to n, updating a and b
    for _ in range(2, n + 1):
        a, b = b, a + b  # a becomes previous b, b becomes sum

    return b


def fibonacci_memo(n: int, memo: Optional[dict] = None) -> int:
    """Fibonacci with memoization (recursive approach).
    
    Time: O(n), Space: O(n)
    Trick: Memoization prevents redundant calculations
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def factorial(n: int) -> int:
    """Calculate factorial of n.
    
    Time: O(n), Space: O(1)
    Trick: Use iterative approach for efficiency
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def power(x: float, n: int) -> float:
    """Calculate x raised to power n efficiently.
    
    Time: O(log n), Space: O(log n)
    Trick: Use binary exponentiation (divide and conquer)
    """
    if n == 0:
        return 1.0
    
    if n < 0:
        x = 1 / x
        n = -n
    
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    else:
        return x * power(x, n - 1)


def generate_parentheses(n: int) -> List[str]:
    """Generate all valid combinations of n pairs of parentheses.

    **Difficulty:** Medium
    **Pattern:** Backtracking / Recursion

    **Visualization:**
    For n=2:
    Start: ""
    Add '(': "(", open=1, close=0
    ├── Add '(': "((", open=2, close=0
    │   └── Add ')': "(()", open=2, close=1
    │       └── Add ')': "(())", open=2, close=2 ✓
    └── Add ')': "()", open=1, close=1
        └── Add '(': "()(", open=2, close=1
            └── Add ')': "()()", open=2, close=2 ✓

    **Learning Focus:**
    - Backtracking algorithm design and implementation
    - Understanding recursion tree and state space
    - Constraint satisfaction problems
    - Decision tree traversal and pruning
    - Time complexity analysis of exponential algorithms

    Uses backtracking to build valid parentheses strings.
    The key constraints are:
    - We can add an opening parenthesis if we haven't used all n
    - We can add a closing parenthesis only if it won't make the string invalid
      (i.e., if we have more opening than closing parentheses so far)

    Args:
        n: Number of pairs of parentheses

    Returns:
        List of all valid parentheses combinations

    Time: O(4^n / sqrt(n)) - Catalan number, Space: O(4^n / sqrt(n))
    """
    result = []

    def backtrack(current: str, open_count: int, close_count: int):
        # Base case: if we've used all parentheses, add to result
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add opening parenthesis if we haven't used all n
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # Add closing parenthesis only if it maintains validity
        # (more opening than closing so far)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    # Start backtracking with empty string and zero counts
    backtrack('', 0, 0)
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    """Generate all possible subsets (power set) of the given array.

    Uses backtracking to explore all combinations. For each element,
    we have two choices: include it in the current subset or exclude it.

    The backtracking function:
    - Adds the current subset to result
    - Tries adding each remaining element and recurses
    - Backtracks by removing the element

    Args:
        nums: Input array (may contain duplicates, but we'll treat as unique)

    Returns:
        List of all possible subsets

    Time: O(2^n), Space: O(2^n) for storing all subsets
    """
    result = []

    def backtrack(start: int, current: List[int]):
        # Add a copy of the current subset to result
        result.append(current[:])

        # Try adding each element from start onwards
        for i in range(start, len(nums)):
            # Include nums[i] in current subset
            current.append(nums[i])
            # Recurse with next starting index
            backtrack(i + 1, current)
            # Backtrack: remove the last added element
            current.pop()

    # Start backtracking from index 0 with empty subset
    backtrack(0, [])
    return result


def permute(nums: List[int]) -> List[List[int]]:
    """Generate all permutations.
    
    Time: O(n!), Space: O(n!)
    Trick: Use backtracking, swap elements to generate permutations
    """
    result = []
    
    def backtrack(start: int):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack
    
    backtrack(0)
    return result


def climb_stairs(n: int) -> int:
    """Count ways to climb n stairs (1 or 2 steps at a time).
    
    Time: O(n), Space: O(1)
    Trick: This is actually Fibonacci sequence!
    """
    if n <= 2:
        return n
    
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
    """Solve Tower of Hanoi puzzle.
    
    Time: O(2^n), Space: O(n)
    Trick: Recursive solution - move n-1 disks, move largest, move n-1 disks
    """
    moves = []
    
    def hanoi(disks: int, src: str, dest: str, aux: str):
        if disks == 1:
            moves.append(f"Move disk 1 from {src} to {dest}")
        else:
            hanoi(disks - 1, src, aux, dest)
            moves.append(f"Move disk {disks} from {src} to {dest}")
            hanoi(disks - 1, aux, dest, src)
    
    hanoi(n, source, destination, auxiliary)
    return moves
