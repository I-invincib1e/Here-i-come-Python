from __future__ import annotations

from typing import List, Optional


def fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number.
    
    Time: O(n), Space: O(1)
    Trick: Use iterative approach instead of recursion to avoid stack overflow
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
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
    """Generate all valid parentheses combinations.
    
    Time: O(4^n / sqrt(n)), Space: O(4^n / sqrt(n))
    Trick: Use backtracking with constraints
    """
    result = []
    
    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    """Generate all possible subsets.
    
    Time: O(2^n), Space: O(2^n)
    Trick: Use backtracking, each element can be included or excluded
    """
    result = []
    
    def backtrack(start: int, current: List[int]):
        result.append(current[:])  # Add copy of current subset
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()  # Backtrack
    
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
