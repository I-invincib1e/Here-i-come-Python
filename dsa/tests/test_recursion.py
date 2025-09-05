import pytest
from dsa.problems.recursion import (
    fibonacci, fibonacci_memo, factorial, power,
    generate_parentheses, subsets, permute, climb_stairs, tower_of_hanoi
)


class TestFibonacci:
    def test_fibonacci_basic(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
    
    def test_fibonacci_memo(self):
        assert fibonacci_memo(0) == 0
        assert fibonacci_memo(1) == 1
        assert fibonacci_memo(5) == 5
        assert fibonacci_memo(10) == 55


class TestFactorial:
    def test_factorial_basic(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
    
    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)


class TestPower:
    def test_power_basic(self):
        assert power(2, 3) == 8
        assert power(2, 0) == 1
        assert power(2, 1) == 2
        assert power(3, 2) == 9
    
    def test_power_negative_exponent(self):
        assert power(2, -1) == 0.5
        assert power(2, -2) == 0.25
    
    def test_power_zero_base(self):
        assert power(0, 5) == 0
        assert power(0, 0) == 1


class TestGenerateParentheses:
    def test_generate_parentheses_n1(self):
        result = generate_parentheses(1)
        expected = ["()"]
        assert set(result) == set(expected)
    
    def test_generate_parentheses_n2(self):
        result = generate_parentheses(2)
        expected = ["(())", "()()"]
        assert set(result) == set(expected)
    
    def test_generate_parentheses_n3(self):
        result = generate_parentheses(3)
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        assert set(result) == set(expected)
    
    def test_generate_parentheses_n0(self):
        assert generate_parentheses(0) == [""]


class TestSubsets:
    def test_subsets_basic(self):
        result = subsets([1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        # Convert to sets for comparison
        result_sets = [set(subset) for subset in result]
        expected_sets = [set(subset) for subset in expected]
        assert len(result_sets) == len(expected_sets)
        for subset in expected_sets:
            assert subset in result_sets
    
    def test_subsets_empty(self):
        assert subsets([]) == [[]]
    
    def test_subsets_single(self):
        result = subsets([1])
        expected = [[], [1]]
        assert len(result) == len(expected)
        for subset in expected:
            assert subset in result


class TestPermute:
    def test_permute_basic(self):
        result = permute([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        assert len(result) == len(expected)
        for perm in expected:
            assert perm in result
    
    def test_permute_single(self):
        assert permute([1]) == [[1]]
    
    def test_permute_empty(self):
        assert permute([]) == [[]]


class TestClimbStairs:
    def test_climb_stairs(self):
        assert climb_stairs(1) == 1
        assert climb_stairs(2) == 2
        assert climb_stairs(3) == 3
        assert climb_stairs(4) == 5
        assert climb_stairs(5) == 8


class TestTowerOfHanoi:
    def test_tower_of_hanoi_n1(self):
        moves = tower_of_hanoi(1, "A", "C", "B")
        expected = ["Move disk 1 from A to C"]
        assert moves == expected
    
    def test_tower_of_hanoi_n2(self):
        moves = tower_of_hanoi(2, "A", "C", "B")
        expected = [
            "Move disk 1 from A to B",
            "Move disk 2 from A to C",
            "Move disk 1 from B to C"
        ]
        assert moves == expected
    
    def test_tower_of_hanoi_n3(self):
        moves = tower_of_hanoi(3, "A", "C", "B")
        # Should have 7 moves total (2^n - 1)
        assert len(moves) == 7
        # First move should be moving smallest disk
        assert moves[0] == "Move disk 1 from A to C"
